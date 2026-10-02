"""Turn the old PaaS Leads and US VC Podcast Outreach tables into Organisations, People and PaaS Engagements.

Usage: python migration/paas.py

Reads (all git-ignored):
  data/raw/notion/us_vc.json, paas_leads.json        old tables, extracted read-only
  data/raw/notion/people_snapshot.json, orgs_snapshot.json   current Notion rows, for matching
Writes:
  data/out/paas/orgs_new.json       Organisations to create
  data/out/paas/people_new.json     People to create (each with a local key)
  data/out/paas/engagements.json    Engagements, pointing at people and orgs by local key or Notion URL
  data/out/paas/activities.json     last-call notes from PaaS Leads
  data/review/paas_review.csv       name-only matches and other calls a human should check

Matching: LinkedIn slug, then email, then exact name at the same organisation. A name match at a
different organisation is never merged: the new row is created as "Possible duplicate" and listed
for review. Never edits the raw files. Re-run safely.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data/raw/notion"
OUT = ROOT / "data/out/paas"
BATCH_VC = "us-vc-2026-10-02"
BATCH_PAAS = "paas-leads-2026-10-02"
TODAY = "2026-10-02"

EMAIL = re.compile(r"[A-Za-z0-9._%+'-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
ROLE_LOCAL = {"info", "hello", "contact", "team", "admin", "office", "media", "press", "pr", "ir", "investors",
              "invest", "general", "inquiries", "enquiries", "partners", "founders", "deals", "pitch", "pitches",
              "submissions", "support", "marketing", "comms", "communications", "news", "careers", "jobs"}
LEGAL = re.compile(r"\b(llc|inc|ltd|limited|pvt|private|lp|llp|gmbh|co|corp|corporation|capital|ventures|partners|vc|fund|funds|management|group)\b")


def fold(s):
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", s)).strip()


def name_key(s):
    s = re.sub(r"^(dr|mr|ms|mrs|prof)\.?\s+", "", fold(s))
    return s


def org_key(s):
    s = fold(re.sub(r"\.(com|in|vc|io|ai|one|co)\b", " ", str(s or ""), flags=re.I))
    return re.sub(r"\s+", "", LEGAL.sub(" ", s)) or re.sub(r"\s+", "", fold(s))


def li_slug(u):
    m = re.search(r"linkedin\.com/in/([^/?#\s]+)", str(u or ""), re.I)
    return m.group(1).lower().rstrip("/") if m else None


def li_url(u):
    s = li_slug(u)
    return f"https://www.linkedin.com/in/{s}" if s else None


def emails(text):
    return [e.lower().strip(".") for e in EMAIL.findall(str(text or ""))]


def is_role(e):
    return e.split("@")[0].lower() in ROLE_LOCAL


def domain_of(url):
    m = re.search(r"https?://(?:www\.)?([^/]+)", str(url or ""))
    return m.group(1).lower() if m else None


def page_url(u):
    m = re.search(r"([0-9a-f]{32})", str(u or "").replace("-", ""))
    return f"https://app.notion.com/p/{m.group(1)}" if m else None


class Index:
    """Existing Notion People and Organisations, plus anything created in this run."""

    def __init__(self, people, orgs):
        self.by_li, self.by_email, self.by_name = {}, {}, {}
        for p in people:
            if p.get("Match status") == "Merged into another row":
                continue
            ref = page_url(p["url"])
            if li_slug(p.get("LinkedIn")):
                self.by_li[li_slug(p["LinkedIn"])] = ref
            for e in emails(p.get("Email")) + emails(p.get("Other emails")):
                self.by_email.setdefault(e, ref)
            org_val = p.get("Organisation") or []
            orgs_of = [page_url(o) for o in (json.loads(org_val) if isinstance(org_val, str) else org_val)]
            self.by_name.setdefault(name_key(p["Name"]), []).append((ref, orgs_of))
        self.org_by_key, self.org_by_domain = {}, {}
        for o in orgs:
            ref = page_url(o["url"])
            self.org_by_key.setdefault(org_key(o["Name"]), ref)
            d = (o.get("Domain") or domain_of(o.get("Website")) or "").lower()
            if d:
                self.org_by_domain.setdefault(d, ref)

    def org(self, name, domain=None):
        if domain and domain in self.org_by_domain:
            return self.org_by_domain[domain]
        return self.org_by_key.get(org_key(name))

    def person(self, name, li, mails, org_ref):
        """Return (ref, how) or (None, why) with why describing a name-only clash for review."""
        if li and li in self.by_li:
            return self.by_li[li], "linkedin"
        for e in mails:
            if e in self.by_email:
                return self.by_email[e], "email"
        hits = self.by_name.get(name_key(name), [])
        for ref, orgs_of in hits:
            if org_ref and org_ref in orgs_of:
                return ref, "name and organisation"
        # a full name that matches one existing row with no organisation (e.g. guests created from Blue)
        orgless = [ref for ref, orgs_of in hits if not orgs_of]
        if len(hits) == 1 and orgless and len(name_key(name).split()) >= 2:
            return orgless[0], "name, existing row had no organisation"
        if hits:
            return None, "same name at a different organisation"
        return None, None

    def add_person(self, ref, name, li, mails, org_ref):
        if li:
            self.by_li[li] = ref
        for e in mails:
            self.by_email.setdefault(e, ref)
        self.by_name.setdefault(name_key(name), []).append((ref, [org_ref] if org_ref else []))

    def add_org(self, ref, name, domain):
        self.org_by_key.setdefault(org_key(name), ref)
        if domain:
            self.org_by_domain.setdefault(domain, ref)


class Run:
    def __init__(self, idx):
        self.idx = idx
        self.orgs, self.people, self.engs, self.acts, self.review = [], [], [], [], []
        self.matched = {"linkedin": 0, "email": 0, "name and organisation": 0, "name, existing row had no organisation": 0}
        self.link_org = []  # existing people matched here who have no organisation yet

    def org(self, name, domain, props, body):
        ref = self.idx.org(name, domain)
        if ref:
            return ref, False
        ref = f"new-org-{len(self.orgs) + 1}"
        self.orgs.append({"key": ref, "props": {"Name": name, **props}, "body": body})
        self.idx.add_org(ref, name, domain)
        return ref, True

    def person(self, name, title, li, mails, org_ref, source_id, batch, tags, src_label):
        personal = [e for e in mails if not is_role(e)]
        ref, how = self.idx.person(name, li, personal, org_ref)
        if ref:
            self.matched[how] += 1
            if how.startswith("name, existing") and org_ref:
                self.link_org.append({"person": ref, "org": org_ref, "name": name})
                self.review.append({"source": src_label, "name": name, "issue": "matched by full name only",
                                    "action": "Linked to the existing person; check it is the same human"})
            return ref
        props = {"Name": name, "Source": "Migration", "Source ID": source_id, "Migration batch": batch,
                 "date:Captured:start": TODAY, "Match status": "Possible duplicate" if how else "Clean",
                 "Tags": json.dumps(tags + ([] if personal else ["No email"]))}
        if title:
            props["Role"] = title
        if li:
            props["LinkedIn"] = li_url(li)
        if personal:
            props["Email"] = personal[0]
            if personal[1:]:
                props["Other emails"] = ", ".join(personal[1:])
        ref = f"new-person-{len(self.people) + 1}"
        self.people.append({"key": ref, "props": props, "org": org_ref})
        self.idx.add_person(ref, name, li, personal, org_ref)
        if how:
            self.review.append({"source": src_label, "name": name, "issue": how,
                                "action": "Created as Possible duplicate; merge in Notion if same person"})
        return ref


def parse_contacts(r):
    """Contact 1-3 columns, then Other Contacts lines 'name | title | email'. Bare email lines belong to the line above."""
    out = []
    for i in (1, 2, 3):
        n = (r.get(f"Contact {i}") or "").strip()
        if n:
            out.append({"name": n, "title": (r.get(f"Contact {i} Title") or "").strip() or None,
                        "li": li_slug(r.get(f"Contact {i} LinkedIn")), "emails": emails(r.get(f"Contact {i} Email"))})
    for line in str(r.get("Other Contacts") or "").splitlines():
        line = line.strip()
        if not line:
            continue
        if "|" in line:
            parts = [p.strip() for p in line.split("|")]
            n = parts[0]
            if not n or n.lower() in {"not disclosed", "-", "n/a"}:
                continue
            out.append({"name": n, "title": parts[1] if len(parts) > 1 and parts[1] not in {"", "-"} else None,
                        "li": None, "emails": emails(parts[2] if len(parts) > 2 else "")})
        elif emails(line) and out:
            out[-1]["emails"] += emails(line)
    # the same person can appear in a Contact column and again in Other Contacts
    seen, uniq = {}, []
    for c in out:
        k = c["li"] or name_key(c["name"])
        if k in seen:
            seen[k]["emails"] += [e for e in c["emails"] if e not in seen[k]["emails"]]
            continue
        seen[k] = c
        uniq.append(c)
    return uniq


def us_vc(run, rows):
    for r in rows:
        firm = r["Firm"].strip()
        domain = domain_of(r.get("Website"))
        generic = emails(r.get("Generic Email"))
        contacts = parse_contacts(r)
        any_mail = bool(generic) or any(c["emails"] for c in contacts)
        sid = f"US VC Podcast Outreach {r['id']}"
        has_pod = r.get("Has Podcast") == "Yes"
        org_tags = ["US VC"] + (["Has podcast"] if has_pod else []) + ([] if any_mail else ["No email"])
        oprops = {"Type": "Fund", "Source": "Migration", "Source ID": sid, "Migration batch": BATCH_VC,
                  "date:Captured:start": TODAY, "Tags": json.dumps(org_tags)}
        if r.get("Website"):
            oprops["Website"] = r["Website"]
        if domain:
            oprops["Domain"] = domain
        if generic:
            oprops["General email"] = generic[0]
        org_ref, _ = run.org(firm, domain, oprops, vc_body(r, generic))
        refs = [run.person(c["name"], c["title"], c["li"], c["emails"], org_ref, sid, BATCH_VC,
                           ["Prospect", "US VC", "Investor"], f"US VC: {firm}") for c in contacts]
        tags = ["US VC"] + ([f"Priority {r['Priority']}"] if r.get("Priority") else []) + \
               (["Has podcast"] if has_pod else []) + ([] if any_mail else ["No email"])
        props = {"Name": f"{firm}, PaaS", "Type": "PaaS", "Stage": "Identified", "Source": "Migration",
                 "Source ID": sid, "Migration batch": BATCH_VC, "date:Captured:start": TODAY, "Tags": json.dumps(tags)}
        if r.get("Fit Rank"):
            props["Rank"] = r["Fit Rank"]
        run.engs.append({"props": props, "org": org_ref, "guest": refs[:1], "stakeholders": refs[1:],
                         "body": eng_body_vc(r)})


def vc_body(r, generic):
    keys = ["Overview", "City", "State", "Founded", "Team Size", "Portfolio Count", "Investment Score", "Sectors",
            "Stages", "Unicorns", "IPOs", "Recent Deals", "Has Podcast", "Podcast Name", "Podcast URL",
            "Podcast Activity", "Partners On Other Podcasts", "LinkedIn", "Tracxn"]
    lines = [f"- **{k}:** {r[k]}" for k in keys if r.get(k) not in (None, "")]
    if len(generic) > 1:
        lines.append(f"- **Other general email:** {', '.join(generic[1:])}")
    return "## Research (US VC Podcast Outreach, enriched Sep 2026)\n\n" + "\n".join(lines)


def eng_body_vc(r):
    keys = ["Pitch Line", "Fit Note", "Budget Read", "Budget Rationale", "Enrichment Notes", "Sources"]
    return "## Why this firm\n\n" + "\n".join(f"- **{k}:** {r[k]}" for k in keys if r.get(k))


PAAS_STAGE = {"Send Pitch": "Identified", "In discussion": "In conversation", "Proposal sent": "Proposal sent",
              "Later": "Contacted", "Renew": "Identified", "Identified": "Identified", None: "Contacted"}
# PaaS founders entered by first name only, resolved by hand against People (2 Oct)
FOUNDER_FULL_NAME = {"Wissen": "Raghu Pareddy"}
HEAT = {"hot": "Hot", "warm": "Warm", "lukewarm": "Warm", "cold": "Cold"}


def paas(run, rows):
    for r in rows:
        company = r["Company"].strip()
        sid = f"Podcast-as-a-Service Leads {r['id']}"
        founder = r.get("Founder") or ""
        mails = emails(founder)
        founder = re.sub(r"\(.*?\)", "", founder).strip()
        name, _, title = founder.partition(",")
        name, title = re.sub(r"^(Dr|Mr|Ms)\.?\s+", "", name.strip()), title.strip() or None
        name = FOUNDER_FULL_NAME.get(company, name)
        domain = next((domain_of(l.get("href")) for l in r.get("property_links") or []
                       if l.get("property") == "Company" and l.get("href")), None)
        org_ref, _ = run.org(company, domain, {"Type": "Startup", "Source": "Migration", "Source ID": sid,
                                               "Migration batch": BATCH_PAAS, "date:Captured:start": TODAY}, "")
        tags = ["Prospect"] + (["Client"] if r.get("Status") == "Renew" else [])
        pref = run.person(name, title, None, mails, org_ref, sid, BATCH_PAAS, tags, f"PaaS: {company}") if name else None
        if name and " " not in name:
            run.review.append({"source": f"PaaS: {company}", "name": name, "issue": "first name only",
                               "action": "Check the person linked to this engagement is right"})
        status, nxt = r.get("Status"), (r.get("Next Action") or "").strip()
        stage = PAAS_STAGE.get(status, "Identified")
        if status == "Send Pitch" and re.search(r"\b(sent|replied)\b", nxt, re.I):
            stage = "Contacted"
        props = {"Name": f"{company}, PaaS", "Type": "Client" if status == "Renew" else "PaaS", "Stage": stage,
                 "Source": "Migration", "Source ID": sid, "Migration batch": BATCH_PAAS, "date:Captured:start": TODAY}
        if HEAT.get(str(r.get("Hot or not") or "").lower()):
            props["Heat"] = HEAT[r["Hot or not"].lower()]
        if nxt:
            props["Next action"] = ("Renewal: " if status == "Renew" else "") + nxt
        if r.get("date:Next follow-up:start"):
            props["date:Next date:start"] = r["date:Next follow-up:start"]
        if r.get("Owner") == "Akshay":
            props["Whose move"] = "Akshay"
        if r.get("Pitch note"):
            props["Pitch link"] = r["Pitch note"]
        if r.get("Follow-ups sent"):
            props["Chase step"] = r["Follow-ups sent"]
        run.engs.append({"props": props, "org": org_ref, "guest": [pref] if pref else [], "stakeholders": [],
                         "body": paas_body(r), "old_page": r["url"]})
        if r.get("date:Last call:start") or r.get("Last call details"):
            run.acts.append({"props": {"Summary": f"Call with {name or company} ({company}, PaaS)", "Kind": "Call notes",
                                       "date:Date:start": r.get("date:Last call:start") or TODAY},
                             "people": [pref] if pref else [], "engagement_source_id": sid,
                             "body": r.get("Last call details") or ""})


def paas_body(r):
    lines = []
    for k, label in [("short link", "Short link"), ("Chat Link", "Working chat"), ("Guest note", "Guest note"),
                     ("Next Action AD", "Next action (AD)")]:
        if r.get(k):
            v = r[k]
            lines.append(f"- **{label}:** {'https://' + v if label == 'Short link' and not v.startswith('http') else v}")
    for c in r.get("child_pages") or []:
        lines.append(f"- **{c.get('title')}:** {c.get('url')}")
    for l in r.get("external_links") or []:
        u = l.get("url") if isinstance(l, dict) else l
        if u and u not in "\n".join(lines):
            lines.append(f"- {l.get('text') + ': ' if isinstance(l, dict) and l.get('text') else ''}{u}")
    lines.append(f"- **Old Notion page:** {r['url']}")
    body = "## Pitch\n\n" + "\n".join(lines)
    if (r.get("body") or "").strip():
        body += "\n\n## Notes from the old page\n\n" + r["body"].strip()
    return body


def main():
    us = json.load(open(RAW / "us_vc.json"))
    pl = json.load(open(RAW / "paas_leads.json"))
    idx = Index(json.load(open(RAW / "people_snapshot.json")), json.load(open(RAW / "orgs_snapshot.json")))
    run = Run(idx)
    paas(run, pl)      # first, so the live deals win any org match
    us_vc(run, us)

    OUT.mkdir(parents=True, exist_ok=True)
    (ROOT / "data/review").mkdir(parents=True, exist_ok=True)
    for name, data in [("orgs_new", run.orgs), ("people_new", run.people), ("engagements", run.engs),
                       ("activities", run.acts), ("link_org", run.link_org)]:
        json.dump(data, open(OUT / f"{name}.json", "w"), indent=1, ensure_ascii=False)
    pd.DataFrame(run.review).to_csv(ROOT / "data/review/paas_review.csv", index=False)

    n_vc = sum(1 for e in run.engs if e["props"]["Migration batch"] == BATCH_VC)
    n_pl = len(run.engs) - n_vc
    print(f"engagements: US VC {n_vc} (raw {len(us)}), PaaS leads {n_pl} (raw {len(pl)})")
    print(f"organisations new {len(run.orgs)}; people new {len(run.people)}; matched existing people {run.matched}")
    print(f"no-email engagements {sum('No email' in e['props']['Tags'] for e in run.engs if 'Tags' in e['props'])}; "
          f"new people without email {sum('No email' in p['props']['Tags'] for p in run.people)}")
    print(f"activities {len(run.acts)}; review rows {len(run.review)}")
    assert n_vc == len(us) and n_pl == len(pl), "engagement counts do not reconcile"


if __name__ == "__main__":
    sys.exit(main())
