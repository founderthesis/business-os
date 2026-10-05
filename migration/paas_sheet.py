"""Migrate the three PAAS tabs of the FT Pipeline sheet into the Deals table.

Usage:
  python migration/paas_sheet.py                       parse, match, export JSON and the review CSV (read-only, re-runnable)
  python migration/paas_sheet.py --batches orgs        write create-pages payloads (batches of 100) for orgs | people | deals
  python migration/paas_sheet.py --created KIND FILE   record created page URLs from a saved Notion query result (Source ID -> url)
  python migration/paas_sheet.py --updates             write update-page payloads for Deals that already exist
  python migration/paas_sheet.py --reconcile           print the counts to check against COUNT queries in Notion

"Apply" is a sequence: --batches orgs, create them in Notion, query the batch back and --created orgs FILE, then the same
for people and deals, then --updates. Each step reads created.json, so a half-finished run picks up where it stopped.

Reads (all git-ignored):
  data/raw/sheets/ft_pipeline.xlsx                 tabs "PAAS - FT", "PAAS - Direct", "PAAS new"
  data/raw/notion/paas_sheet/{orgs,people_1,people_2,deals,ft_engagements}.json
                                                   SQL group_concat snapshots of Notion taken on 5 Oct before this run
Writes:
  data/out/paas_sheet/{orgs_new,people_new,deals_new,deals_update}.json, created.json, updates.json, batches/*.json
  data/review/paas_sheet_review.csv

Rules (agreed 5 Oct, docs/statuses.md "Deals"):
  Stage   Cold or blank = New, Emailed / Chase / initial mail sent = Contacted, warm = Interested, a planning call or meeting
          in Last conversation = In conversation, shared pricing or a proposal = Proposal sent, Later = Parked (next date
          180 days after the last touch), Declined / Reject = Declined, Unresponsive with every follow-up sent = Unresponsive.
          A Cold row whose notes show outreach is Contacted, and Unresponsive once the notes say the final mail got no reply.
  Dedupe  one Deal per Organisation. Rows that land on the same organisation collapse, PAAS - FT first. A Deal that already
          exists for the organisation is updated: empty fields filled, Stage only moved forward, the sheet row appended to
          Source ID. Nothing is merged or deleted.
  People  matched with migration/paas.py's Index (LinkedIn, email, name at the organisation). PR addresses become PR
          contacts with the name guessed from the address (migration/pr_contacts.py). Never edits the raw files.
"""
import argparse
import collections
import csv
import datetime as dt
import json
import re
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paas import Index, EMAIL, fold, is_role, name_key, org_key, page_url  # noqa: E402
from pr_contacts import FREE_MAIL, domain_stem, guess_name  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data/raw"
SNAP = RAW / "notion/paas_sheet"
OUT = ROOT / "data/out/paas_sheet"
REVIEW = ROOT / "data/review/paas_sheet_review.csv"
BATCH = "paas-sheet-2026-10-05"
TODAY = dt.date(2026, 10, 5)
BATCH_SIZE = 100
SOURCES = {"orgs": "collection://c43c280a-3b37-4821-96ef-dab688a53aea",
           "people": "collection://e6c44319-7f81-4da6-8b80-8441a4875d7a",
           "deals": "collection://1a981c5a-912a-4972-b3fc-8c9f2abb329a"}
FT_SHOW = "3ed19a301a7f817c9367e0d88afc5776"
TABS = ["PAAS - FT", "PAAS - Direct", "PAAS new"]
TAB_RANK = {t: i for i, t in enumerate(TABS)}

LADDER = ["New", "Contacted", "Interested", "In conversation", "Proposal sent", "Agreed"]
OUTCOMES = {"Parked", "Declined", "Unresponsive"}
OPEN = set(LADDER) | {"Parked"}
PHONE = re.compile(r"(?<![\w@.])\+?\d[\d \-]{8,}\d")
HONORIFIC = re.compile(r"^(dr|mr|ms|mrs|prof)\.?\s+", re.I)
PR_DOMAIN = re.compile(r"(^|[.-])(pr|media|comms?|communications?)([.-]|$)|publicis|consult|80-db|adfactors|edelman|ketchum", re.I)
PR_NOTE = re.compile(r"press|media|publicist|\bpr\b", re.I)
PR_LOCAL = {"pr", "press", "media", "mediaqueries", "mediacentre", "mediarelations", "comms", "communications",
            "corpcomm", "publicrelations"}
# PAAS - FT rows 82 to 95 list a founder with company inboxes and no "@ Company". The company is written here once.
COMPANY_FOR = {"Srikanth Bolla": "Bollant Industries", "Hardik Kothiya": "Rayzon Energies", "Chirag Nakrani": "Rayzon Energies",
               "Kanika Tekriwal": "JetSetGo", "Shaily Mehrotra": "Fixderma", "Mohit Yadav": "Minimalist",
               "Radhika Gupta": "Edelweiss Mutual Fund", "Varun Dua": "Acko", "Azhar Iqubal": "Inshorts",
               "Amit Jain": "CarDekho", "Kunal Bahl": "Titan Capital", "Viraj Bahl": "Veeba", "Ghazal Alagh": "Honasa Consumer",
               "Varun Alagh": "Honasa Consumer"}


# ---------------------------------------------------------------- small helpers

def clean(s):
    return re.sub(r"\s+", " ", re.sub(r"[\u200b-\u200d\ufeff]", "", str(s or "")).replace("\t", " ")).strip()


def as_date(v):
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    return None


def bare_id(ref):
    m = re.search(r"([0-9a-f]{32})", str(ref or "").replace("-", ""))
    return m.group(1) if m else None


def load_snapshot(name, fields):
    """A saved SQL result: one row with n and rows = fields joined by US, records joined by RS."""
    out = []
    for path in sorted(SNAP.glob(f"{name}*.json")):
        res = json.load(open(path))["results"][0]
        recs = res["rows"].split("\x1e") if res.get("rows") else []
        assert len(recs) == res["n"], f"{path.name}: {len(recs)} records, query said {res['n']}"
        for rec in recs:
            vals = rec.split("\x1f")
            assert len(vals) == len(fields), f"{path.name}: {len(vals)} fields, expected {len(fields)}"
            out.append(dict(zip(fields, vals)))
    return out


def rel(cell):
    try:
        return [bare_id(u) for u in json.loads(cell)] if cell else []
    except json.JSONDecodeError:
        return []


def compact(s):
    return re.sub(r"[^a-z0-9]", "", fold(s))


def domain_fits(domain, company):
    """True when an email domain plausibly belongs to the company (acadly.com for Acadly, not smytten.com for PulseAI)."""
    if not domain or not company:
        return False
    stem, ck = compact(domain_stem(domain)), compact(company)
    if len(stem) < 3 or len(ck) < 3:
        return False
    return stem in ck or ck in stem or stem[:5] == ck[:5]


def name_in_local(local, name):
    """Does the address look like this person's own? priya.sharma, psharma, sb (Shaurya Bhutani), reachrg."""
    lc = compact(local)
    toks = [compact(t) for t in name.split() if len(compact(t)) >= 3]
    if any(t in lc for t in toks):
        return True
    parts = [compact(t) for t in name.split() if compact(t)]
    if len(parts) >= 2:
        ini = parts[0][0] + parts[-1][0]
        return lc == ini or lc.endswith(ini) and len(lc) > 4 or lc == parts[0][0] + parts[-1]
    return False


# ---------------------------------------------------------------- sheet parsing

def split_name(cell):
    """'Name @ Company' -> (name, company, note). The company drops role words and asides in brackets."""
    s = clean(cell)
    if "@" not in s:
        return HONORIFIC.sub("", s).strip(), None, None
    person, company = [p.strip(" ,-") for p in s.split("@", 1)]
    person = HONORIFIC.sub("", person).strip()
    company = re.sub(r"\(.*?\)", "", company).strip()
    company = re.sub(r"^(author\s+and\s+)?(co-?founder|founder|ceo)(\s+and\s+(co-?founder|founder|ceo))*\s+of\s+", "", company, flags=re.I)
    company = re.sub(r"\s+and\s+author$", "", company, flags=re.I).strip(" ,-")
    note = None
    if not person or len(person.split()) > 4:
        note = "founder name unparseable"
    elif len(person.split()) == 1:
        note = "first name only"
    if re.search(r"\bcoach\b|\bauthor\b", company, re.I):
        note = (note + "; " if note else "") + "company looks like a description"
    return person, company or None, note


def read_rows(wb, tab):
    ws = wb[tab]
    rows = []
    for i, r in enumerate(ws.iter_rows(min_row=2, values_only=True), 2):
        if not any(v is not None and clean(v) for v in r):
            continue
        rows.append({"tab": tab, "row": i, "cells": list(r) + [None] * (30 - len(r))})
    return rows


def parse_emails(cell, tab):
    """-> (addresses, pr addresses, phones). In PAAS - FT, anything after 'PR -' or noted as press is a PR address."""
    text = str(cell or "")
    phones = [p.strip() for p in PHONE.findall(EMAIL.sub(" ", text))]
    addrs, pr = [], []
    after_pr = False
    for part in re.split(r"(\bPR\s*-\s*)|;|,|/|\band\b", text):
        if part is None:
            continue
        if re.fullmatch(r"\bPR\s*-\s*", part):
            after_pr = True
            continue
        for e in EMAIL.findall(part):
            e = e.lower().strip(".")
            local, domain = e.split("@", 1)
            if after_pr or (tab == "PAAS - FT" and PR_NOTE.search(part.replace(e, ""))) or local in PR_LOCAL:
                pr.append(e)
            else:
                addrs.append(e)
        after_pr = False if not re.search(r"\bPR\s*-", part) else after_pr
    bad = [w for w in re.findall(r"\S+@\S+", text) if not EMAIL.search(w)]
    return list(dict.fromkeys(addrs)), list(dict.fromkeys(pr)), phones, bad


def follow_ups(cells, idxs):
    """-> (dates filled, texts that are not dates)."""
    dates, texts = [], []
    for i in idxs:
        v = cells[i] if i < len(cells) else None
        d = as_date(v)
        if d:
            dates.append(d)
        elif v is not None and clean(v):
            texts.append(clean(v))
    return dates, texts


def parse(r):
    c, tab = r["cells"], r["tab"]
    name, company, note = split_name(c[0])
    out = {**r, "sid": f"FT Pipeline/{tab}/{r['row']}", "name": name, "company": company, "note": note, "heat": None,
           "next_action": None, "next_date": None, "chase": None, "blurb": None, "last_conv": None, "lines": []}
    if tab == "PAAS - FT":
        status = clean(c[1])
        out.update(status=status, last_conv=clean(c[2]) or None, blurb=clean(c[9]) or None)
        if not company and name in COMPANY_FOR:
            out["company"], out["note"] = COMPANY_FOR[name], None
            out["company_from"] = "hand map"
        addrs, pr, phones, bad = parse_emails(c[8], tab)
        last_fu, rec = as_date(c[3]), as_date(c[7])
        m_act, ad_act, fd = clean(c[4]), clean(c[5]), clean(c[6])
        notes = " ".join([out["last_conv"] or "", m_act, ad_act, fd]).lower()
        s = status.lower()
        stage, heat = "New", None
        if s == "declined":
            stage = "Declined"
        elif s == "unresponsive":
            stage = "Unresponsive"
        elif s in ("later", "maybe later", "lt chase"):
            stage = "Parked"
        elif s == "chase":
            stage, out["chase"] = "Contacted", 2
        elif s == "emailed":
            stage = "Contacted"
        elif s in ("warm", "interested"):
            stage, heat = "Interested", ("Warm" if s == "warm" else None)
        elif s == "cold":
            heat = "Cold"
            if re.search(r"final (email|follow ?up)[^.]*\. no reply|final email sent", notes):
                stage = "Unresponsive"
            elif "connected through" in notes or "mails are not getting delivered" in notes:
                stage = "Contacted"
        elif s:
            out["note"] = (out["note"] + "; " if out["note"] else "") + f"status not mapped: {status}"
        if stage in ("Interested", "New", "Contacted"):
            lc = (out["last_conv"] or "").lower()
            if re.search(r"shared pricing|proposal", lc):
                stage = "Proposal sent"
            elif re.search(r"planning call|meeting", lc):
                stage = "In conversation"
        out["heat"] = heat
        if out["chase"] is None and last_fu:
            out["chase"] = 1
        if stage == "Parked":
            base = max([d for d in (last_fu, rec) if d] or [TODAY])
            out["next_date"] = base + dt.timedelta(days=180)
        elif stage in OPEN and rec:
            out["next_date"] = rec
        if stage in OPEN:
            out["next_action"] = ad_act or m_act or None
        out["lines"] = [("Status", status or "blank"), ("Next action (Mamatha)", m_act), ("Next action (AD)", ad_act),
                        ("FD", fd), ("Last follow-up", last_fu), ("Follow-up or recording date", rec)]
    else:
        direct = tab == "PAAS - Direct"
        status = clean(c[3])
        addrs, pr, phones, bad = parse_emails(c[1], tab)
        if direct:
            out["blurb"] = clean(c[2]) or None
            initial, _ = follow_ups(c, [5])
            li_d, li_t = follow_ups(c, [6])
            fu, fu_txt = follow_ups(c, [7, 8, 9, 10])  # the unlabelled column after Followup 3 holds a fourth follow-up date
            n_named = 3
            named = [as_date(c[i]) for i in (7, 8, 9)]
            out["lines"] = [("Status", status or "blank"), ("Type", clean(c[4])), ("Initial mail or LinkedIn message", initial[0] if initial else None),
                            ("LinkedIn", li_d[0] if li_d else (li_t[0] if li_t else None))] + \
                           [(f"Follow-up {k + 1}", as_date(c[i]) or clean(c[i]) or None) for k, i in enumerate((7, 8, 9, 10))]
        else:
            out["x_handle"] = clean(c[2]) or None  # People has no X field, so this is not carried
            initial, li_d = [], []
            fu, fu_txt = follow_ups(c, [4, 5, 6, 7])
            n_named = 4
            named = [as_date(c[i]) for i in (4, 5, 6, 7)]
            out["lines"] = [("Status", status or "blank")] + [(f"Follow-up {k + 1}", as_date(c[i])) for k, i in enumerate((4, 5, 6, 7))]
        for t in fu_txt:
            if not re.search(r"\d+\s*-\s*\d+\s*months?", t, re.I):
                out["note"] = (out["note"] + "; " if out["note"] else "") + f"follow-up cell is not a date: {t}"
        sent = [d for d in initial + li_d + fu if d <= TODAY]
        all_sent = all(d and d <= TODAY for d in named[:n_named])
        s = status.lower()
        if s == "reject":
            stage = "Declined"
        elif s == "later":
            stage = "Parked"
        elif s == "unresponsive":
            stage = "Unresponsive" if all_sent else "Contacted"
        elif s:
            stage = "New"
            out["note"] = (out["note"] + "; " if out["note"] else "") + f"status not mapped: {status}"
        else:
            stage = "Contacted" if sent else "New"
        out["chase"] = len(fu) or None
        future = sorted(d for d in fu if d > TODAY)
        if stage == "Parked":
            out["next_date"] = max(sent or [TODAY]) + dt.timedelta(days=180)
        elif stage in OPEN and future:
            out["next_date"] = future[0]
    out.update(stage=stage, emails=addrs, pr=pr, phones=phones, bad_emails=bad)
    return out


# ---------------------------------------------------------------- the run

class Run:
    def __init__(self, people, orgs, deals, ft_engs):
        self.idx = Index(people, orgs)
        self.people_by_ref = {page_url(p["url"]): p for p in people}
        self.org_names = {page_url(o["url"]): o["Name"] for o in orgs}
        self.org_by_name = collections.defaultdict(set)
        self.org_alias = collections.defaultdict(set)
        for o in orgs:
            self.org_by_name[org_key(o["Name"])].add(page_url(o["url"]))
            # "SilverX (formerly Silverneedle)" answers to both names
            for part in [re.sub(r"\(.*?\)", "", o["Name"])] + re.findall(r"\((?:formerly\s+)?(.*?)\)", o["Name"], re.I):
                if compact(part) and compact(part) != compact(o["Name"]):
                    self.org_by_name[org_key(part)].add(page_url(o["url"]))
                    self.org_alias[page_url(o["url"])].add(compact(part))
        self.org_by_domain = collections.defaultdict(set)
        self.org_domain = {}
        for o in orgs:
            d = (o.get("Domain") or "").lower().removeprefix("www.")
            if not d and o.get("Website"):
                m = re.search(r"https?://(?:www\.)?([^/]+)", o["Website"])
                d = m.group(1).lower() if m else ""
            if d:
                self.org_by_domain[d].add(page_url(o["url"]))
                self.org_domain[page_url(o["url"])] = d
        self.deals = deals
        self.deal_by_org = collections.defaultdict(list)
        self.deal_by_name = collections.defaultdict(list)
        for d in deals:
            for o in rel(d["Organisation"]):
                self.deal_by_org[page_url(o)].append(d)
            self.deal_by_name[org_key(d["Company"])].append(d)
        self.eng_by_guest = collections.defaultdict(list)
        for e in ft_engs:
            for g in rel(e["Guest"]):
                self.eng_by_guest[page_url(g)].append(e)
        self.orgs, self.people, self.review = [], [], []
        self.matched = collections.Counter()
        self.org_matched = collections.Counter()

    def flag(self, source, name, issue, action, c1="", c2=""):
        self.review.append({"source": source, "name": name, "issue": issue, "candidate_1": c1, "candidate_2": c2, "action": action})

    # organisations
    def org(self, company, domain, sid, general=None, person=None):
        if not company:
            return None
        own_domain = domain if domain and domain_fits(domain, company) else None
        by_dom = sorted(self.org_by_domain.get(own_domain, set())) if own_domain else []
        by_name = []
        for ref in sorted(self.org_by_name.get(org_key(company), set())):
            if compact(company) in {compact(self.org_names.get(ref, ""))} | self.org_alias.get(ref, set()):
                by_name.append(ref)
                continue
            # a loose match (Coefficient vs Coefficient Capital, Hopscotch vs Hopscotch.in) needs a second signal
            od = self.org_domain.get(ref)
            person_there = person and any(ref in orgs_of for _, orgs_of in self.idx.by_name.get(name_key(person), []))
            if person_there or (own_domain and od == own_domain):
                by_name.append(ref)
            else:
                self.flag(sid, company, f"name close to an existing organisation: {self.org_names.get(ref)}",
                          "Created a separate organisation; merge if the same company", ref)
        cands = list(dict.fromkeys(by_dom + by_name))
        if len(cands) > 1:
            self.flag(sid, company, "two organisation candidates", "Used the email-domain match" if by_dom else "Used the first name match",
                      cands[0], cands[1])
        if cands:
            self.org_matched["domain" if by_dom else "name"] += 1
            return cands[0]
        key = f"{sid}/org"
        props = {"Name": company, "Source": "Migration", "Source ID": key, "Migration batch": BATCH, "date:Captured:start": str(TODAY)}
        if domain and domain_fits(domain, company):
            props["Domain"] = domain
        if general:
            props["General email"] = general
        self.orgs.append({"key": key, "props": props})
        self.org_by_name[org_key(company)].add(key)
        if props.get("Domain"):
            self.org_by_domain[domain].add(key)
        self.org_names[key] = company
        self.idx.add_org(key, company, props.get("Domain"))
        self.org_matched["new"] += 1
        return key

    # people
    def person(self, name, mails, org_ref, sid, tags, label, phone=None, extra=None, ft_guest=False):
        personal = [e for e in mails if not is_role(e)]
        ref, how = self.idx.person(name, None, personal, org_ref)
        if ref:
            self.matched[how] += 1
            return ref
        hits = self.idx.by_name.get(name_key(name), [])
        with_eng = [h[0] for h in hits if h[0] in self.eng_by_guest]
        if ft_guest and len(with_eng) == 1 and len(name_key(name).split()) >= 2:
            # PAAS - FT lists FT guests: one person with this full name already has an FT engagement
            self.matched["name, FT guest with an engagement"] += 1
            return with_eng[0]
        if len(name.split()) == 1 and org_ref:
            # a first name only: take the one person at this organisation with that first name
            hits = [r for k, rows in self.idx.by_name.items() if k.split()[:1] == [name_key(name)]
                    for r, orgs_of in rows if org_ref in orgs_of]
            hits = list(dict.fromkeys(hits))
            if len(hits) == 1:
                self.matched["first name at the organisation"] += 1
                return hits[0]
        hits = self.idx.by_name.get(name_key(name), [])
        props = {"Name": name, "Source": "Migration", "Source ID": sid, "Migration batch": BATCH, "date:Captured:start": str(TODAY),
                 "Match status": "Possible duplicate" if hits else "Clean",
                 "Tags": json.dumps(tags + ([] if personal or "PR contact" in tags else ["No email"]))}
        if personal:
            props["Email"] = personal[0]
            if personal[1:]:
                props["Other emails"] = ", ".join(personal[1:])
        if phone:
            props["Phone"] = phone
        if extra:
            props.update(extra)
        self.people.append({"key": sid, "props": props, "org": org_ref})
        self.idx.add_person(sid, name, None, personal, org_ref)
        if hits:
            self.flag(label, name, "same name exists at another organisation", "Created as Possible duplicate; merge in Notion if the same person",
                      hits[0][0], hits[1][0] if len(hits) > 1 else "")
        self.matched["new"] += 1
        return sid

    def pr_contact(self, email, sid, label):
        ref = self.idx.by_email.get(email)
        if ref:
            self.matched["PR contact by email"] += 1
            return ref
        local, domain = email.split("@", 1)
        name, conf, role = guess_name(local)
        role = role or local in PR_LOCAL
        if role:
            stem = domain_stem(domain)
            name = f"{stem.capitalize()} {local} inbox"
        tags = ["PR contact"] + (["Role inbox"] if role else ["Name guessed"])
        org_ref = None
        if domain not in FREE_MAIL:
            hits = sorted(self.org_by_domain.get(domain, set()))
            org_ref = hits[0] if hits else None
        props = {"Name": name, "Source": "Migration", "Source ID": sid, "Migration batch": BATCH, "date:Captured:start": str(TODAY),
                 "Match status": "Clean", "Tags": json.dumps(tags), "Email": email}
        self.people.append({"key": sid, "props": props, "org": org_ref})
        self.idx.by_email[email] = sid
        self.matched["PR contact new"] += 1
        if conf == "low" or role:
            self.flag(label, name, "PR contact name guessed from the address" if not role else "PR role inbox",
                      "Check the name from a signature")
        return sid


def stage_rank(s):
    return LADDER.index(s) if s in LADDER else 1.5


def forward(new, old):
    """Is moving a Deal from old to new a step forward? Outcomes only replace New or Contacted."""
    if not old:
        return True
    if new == old:
        return False
    if new in OUTCOMES:
        return old in ("New", "Contacted")
    if old in OUTCOMES:
        return False
    return stage_rank(new) > stage_rank(old)


def body_for(rs):
    parts = []
    blurbs = list(dict.fromkeys(r["blurb"] for r in rs if r.get("blurb")))
    if blurbs:
        parts.append("## Blurb\n\n" + "\n\n".join(blurbs))
    convs = list(dict.fromkeys(r["last_conv"] for r in rs if r.get("last_conv")))
    if convs:
        parts.append("## Last conversation\n\n" + "\n\n".join(convs))
    lines = ["## From the FT Pipeline sheet (5 Oct 2026)", ""]
    for r in rs:
        facts = [f"{k.lower() if k != 'FD' else k} {v}" for k, v in r["lines"] if v not in (None, "")]
        if r.get("inboxes"):
            facts.append("company inboxes " + ", ".join(r["inboxes"]))
        lines.append(f"- {r['tab']} row {r['row']}: {clean(r['cells'][0])}" + (". " + "; ".join(facts) if facts else ""))
    parts.append("\n".join(lines))
    return "\n\n".join(parts)


def build():
    people = load_snapshot("people_", ["url", "Name", "Email", "Other emails", "LinkedIn", "Organisation", "Match status", "Tags"])
    orgs = load_snapshot("orgs", ["url", "Name", "Domain", "Website", "Type"])
    deals = load_snapshot("deals", ["url", "Company", "Organisation", "Contacts", "Stage", "Heat", "Next action", "date:Next date:start",
                                    "Chase step", "Entry path", "From engagement", "Source ID", "Migration batch", "Tags",
                                    "Budget read", "Proposal link", "Pitch note"])
    ft_engs = load_snapshot("ft_engagements", ["url", "Name", "Guest", "Status"])
    print(f"Notion snapshot: people {len(people)}, organisations {len(orgs)}, deals {len(deals)}, FT engagements {len(ft_engs)}")
    run = Run(people, orgs, deals, ft_engs)

    wb = openpyxl.load_workbook(RAW / "sheets/ft_pipeline.xlsx", read_only=True)
    rows, per_tab = [], {}
    for tab in TABS:
        raw = read_rows(wb, tab)
        if tab == "PAAS - Direct":
            end = [r for r in raw if clean(r["cells"][0]).upper() == "END"]
            for r in end:
                run.flag(f"FT Pipeline/{tab}/{r['row']}", "END", "marker row, not a lead", "Skipped")
            raw = [r for r in raw if clean(r["cells"][0]).upper() != "END"]
        per_tab[tab] = len(raw)
        rows += [parse(r) for r in raw]
    print("rows per tab (blank rows skipped):", per_tab, "total", len(rows))

    # resolve each row's organisation and people
    for r in rows:
        label = r["sid"]
        if r["note"]:
            run.flag(label, clean(r["cells"][0])[:80], r["note"], "Check the deal and its contact in Notion")
        for b in r["bad_emails"]:
            run.flag(label, r["name"], "address without a valid domain, not used", "Fix the address on the person by hand")
        founder_mails, others, inboxes = [], [], []
        for i, e in enumerate(r["emails"]):
            local, domain = e.split("@", 1)
            if is_role(e) or local in {"help", "cs", "grievance", "gro", "legal", "compliance", "investments", "startups",
                                       "investorrelations"} or local.startswith("reach") and not name_in_local(local, r["name"]):
                inboxes.append(e)
            elif name_in_local(local, r["name"]) or (r["tab"] != "PAAS - FT" and i == 0) or \
                    (r["tab"] == "PAAS - FT" and len([x for x in r["emails"] if not is_role(x)]) == 1 and "@" in clean(r["cells"][0])):
                founder_mails.append(e)
            elif PR_DOMAIN.search(domain) and not domain_fits(domain, r["company"]):
                r["pr"].append(e)
            else:
                others.append(e)
        r["inboxes"] = inboxes
        dom = next((m.split("@", 1)[1] for m in founder_mails + others + inboxes if m.split("@", 1)[1] not in FREE_MAIL
                    and domain_fits(m.split("@", 1)[1], r["company"])), None)
        r["org"] = run.org(r["company"], dom, r["sid"], general=next((m for m in inboxes if domain_fits(m.split("@", 1)[1], r["company"])), None),
                           person=r["name"])
        if not r["company"]:
            run.flag(label, r["name"], "no company on the row", "Deal not created; add the company by hand")
            r["people_refs"] = []
            continue
        refs = []
        if r["name"] and r["note"] != "founder name unparseable" or r["name"] and r["note"] and "unparseable" not in r["note"]:
            refs.append(run.person(r["name"], founder_mails, r["org"], r["sid"], ["PaaS prospect"], label,
                                   phone=r["phones"][0] if r["phones"] else None, ft_guest=r["tab"] == "PAAS - FT"))
        for k, e in enumerate(others):
            ref = run.idx.by_email.get(e)
            if not ref:
                local = e.split("@", 1)[0]
                nm, conf, role = guess_name(local)
                if not nm or len(compact(local)) < 4:
                    run.flag(label, e.split("@", 1)[0], "second address on the row, owner unknown", "Kept in the deal body only")
                    r["inboxes"].append(e)
                    continue
                ref = run.person(nm, [e], r["org"], f"{r['sid']}/c{k + 2}", ["PaaS prospect", "Name guessed"], label)
                run.flag(label, nm, "colleague created from a second address, name guessed", "Check the name from a signature")
            else:
                run.matched["colleague by email"] += 1
            refs.append(ref)
        for k, e in enumerate(dict.fromkeys(r["pr"])):
            refs.append(run.pr_contact(e, f"{r['sid']}/pr{k + 1}", label))
        r["people_refs"] = list(dict.fromkeys(refs))

    # one deal per organisation; PAAS - FT first, then Direct, then new; the earliest row within a tab
    groups = collections.OrderedDict()
    for r in sorted(rows, key=lambda r: (TAB_RANK[r["tab"]], r["row"])):
        if r["org"]:
            groups.setdefault(r["org"], []).append(r)
    for org_ref, rs in groups.items():
        # PAAS - FT wins; within the winning tabs the most advanced stage leads, then the earliest row
        pool = [r for r in rs if r["tab"] == "PAAS - FT"] or rs
        lead = max(pool, key=lambda r: (stage_rank(r["stage"]), -TAB_RANK[r["tab"]], -r["row"]))
        groups[org_ref] = [lead] + [r for r in rs if r is not lead]
    collapsed = sum(len(g) - 1 for g in groups.values())
    print(f"deals after collapsing rows on the same organisation: {len(groups)} ({collapsed} rows folded in)")

    new_deals, upd_deals = [], []
    for org_ref, rs in groups.items():
        p = rs[0]
        stage = p["stage"]
        fields = {"Heat": p["heat"], "Next action": p["next_action"], "Next date": p["next_date"], "Chase step": p["chase"]}
        for r in rs[1:]:
            for k, v in (("Heat", r["heat"]), ("Next action", r["next_action"]), ("Next date", r["next_date"]), ("Chase step", r["chase"])):
                if fields[k] in (None, "") and v not in (None, "") and r["stage"] == stage:
                    fields[k] = v
        if stage not in OPEN:
            fields["Next action"] = fields["Next date"] = None
        contacts = list(dict.fromkeys(ref for r in rs for ref in r["people_refs"]))
        entry = "FT guest first" if p["tab"] == "PAAS - FT" else "Cold outreach"
        from_eng = None
        if entry == "FT guest first" and p["people_refs"]:
            engs = run.eng_by_guest.get(p["people_refs"][0], [])
            if engs:
                engs = sorted(engs, key=lambda e: (e["Status"] in ("Recorded", "Form filled"), e["url"]))
                from_eng = page_url(engs[-1]["url"])
                if len(engs) > 1:
                    run.flag(p["sid"], p["name"], "person has several FT engagements", "Linked the recorded one; check From engagement",
                             page_url(engs[-1]["url"]), page_url(engs[0]["url"]))
        sids = [r["sid"] for r in rs]
        no_email = not any(r["emails"] for r in rs)
        if len(rs) > 1 and len({r["stage"] for r in rs}) > 1:
            run.flag(p["sid"], p["company"], "rows on the same organisation disagree on stage",
                     f"Kept {stage} from {p['tab']} row {p['row']}; others: " + ", ".join(f"{r['tab']}/{r['row']} {r['stage']}" for r in rs[1:]))

        existing = run.deal_by_org.get(org_ref, []) if org_ref.startswith("http") else []
        if not existing:
            existing = [d for d in run.deal_by_name.get(org_key(p["company"]), []) if compact(d["Company"]) == compact(p["company"])]
            if existing:
                run.flag(p["sid"], p["company"], "existing deal matched by company name, not by organisation",
                         "Updated that deal; check its Organisation", page_url(existing[0]["url"]))
        if len(existing) > 1:
            run.flag(p["sid"], p["company"], "two existing deals for the organisation", "Updated the first",
                     page_url(existing[0]["url"]), page_url(existing[1]["url"]))
        if existing:
            d = existing[0]
            props = {}
            if forward(stage, d["Stage"]):
                props["Stage"] = stage
            elif stage != d["Stage"] and not (stage == "New"):
                run.flag(p["sid"], p["company"], f"sheet says {stage}, Deals says {d['Stage']}", "Stage left as it was")
            if fields["Heat"] and not d["Heat"]:
                props["Heat"] = fields["Heat"]
            if fields["Next action"] and not d["Next action"]:
                props["Next action"] = fields["Next action"]
            if fields["Next date"] and not d["date:Next date:start"]:
                props["date:Next date:start"] = str(fields["Next date"])
            if fields["Chase step"] and not d["Chase step"]:
                props["Chase step"] = fields["Chase step"]
            if not d["Entry path"]:
                props["Entry path"] = entry
            if from_eng and not rel(d["From engagement"]):
                props["From engagement"] = [from_eng]
            have = [page_url(u) for u in rel(d["Contacts"])]
            add = [c for c in contacts if c not in have]
            if add:
                props["Contacts"] = have + add
            if not rel(d["Organisation"]):
                props["Organisation"] = [org_ref]
            props["Source ID"] = "; ".join([d["Source ID"]] + [s for s in sids if s not in d["Source ID"]]) if d["Source ID"] else "; ".join(sids)
            upd_deals.append({"page": page_url(d["url"]), "company": d["Company"], "old_stage": d["Stage"], "props": props,
                              "body": body_for(rs), "rows": sids})
            continue
        props = {"Company": run.org_names.get(org_ref) or p["company"], "Stage": stage, "Entry path": entry, "Source": "Migration",
                 "Source ID": "; ".join(sids), "Migration batch": BATCH, "date:Captured:start": str(TODAY)}
        if fields["Heat"]:
            props["Heat"] = fields["Heat"]
        if fields["Next action"]:
            props["Next action"] = fields["Next action"]
        if fields["Next date"]:
            props["date:Next date:start"] = str(fields["Next date"])
        if fields["Chase step"]:
            props["Chase step"] = fields["Chase step"]
        if no_email:
            props["Tags"] = json.dumps(["No email"])
        new_deals.append({"key": p["sid"], "props": props, "org": org_ref, "contacts": contacts,
                          "from_engagement": from_eng, "body": body_for(rs), "rows": sids})

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "batches").mkdir(exist_ok=True)
    REVIEW.parent.mkdir(parents=True, exist_ok=True)
    for name, data in [("orgs_new", run.orgs), ("people_new", run.people), ("deals_new", new_deals), ("deals_update", upd_deals)]:
        json.dump(data, open(OUT / f"{name}.json", "w"), indent=1, ensure_ascii=False, default=str)
    with open(REVIEW, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["source", "name", "issue", "candidate_1", "candidate_2", "action"])
        w.writeheader()
        w.writerows(run.review)

    no_org = sum(1 for r in rows if not r["org"])
    print(f"organisations: matched {run.org_matched['name'] + run.org_matched['domain']} "
          f"(name {run.org_matched['name']}, domain {run.org_matched['domain']}), new {len(run.orgs)}; rows without a company {no_org}")
    m = {k: v for k, v in run.matched.items() if k not in ("new", "PR contact new")}
    print(f"people: matched {sum(m.values())} {m}, new {len(run.people)} "
          f"(prospects {run.matched['new']}, PR contacts {run.matched['PR contact new']}, "
          f"possible duplicates {sum(1 for x in run.people if x['props']['Match status'] == 'Possible duplicate')})")
    print(f"deals: new {len(new_deals)}, update existing {len(upd_deals)}")
    print("stage of new deals:", dict(collections.Counter(d["props"]["Stage"] for d in new_deals)))
    print("entry path of new deals:", dict(collections.Counter(d["props"]["Entry path"] for d in new_deals)))
    print("stage changes on existing deals:", dict(collections.Counter(f"{u['old_stage']} -> {u['props'].get('Stage', 'same')}" for u in upd_deals)))
    after = collections.Counter(d["Stage"] for d in deals)
    for u in upd_deals:
        if "Stage" in u["props"]:
            after[u["old_stage"]] -= 1
            after[u["props"]["Stage"]] += 1
    for d in new_deals:
        after[d["props"]["Stage"]] += 1
    print(f"Deals Stage after the run ({sum(after.values())} rows):", {s: after[s] for s in LADDER + sorted(OUTCOMES) if after[s]})
    print("review rows", len(run.review), dict(collections.Counter(r["issue"].split(":")[0] for r in run.review).most_common()))
    assert len(rows) == sum(per_tab.values())
    assert sum(len(g) for g in groups.values()) + no_org == len(rows), "rows do not reconcile with deals"
    assert len(new_deals) + len(upd_deals) == len(groups)
    return run, new_deals, upd_deals


# ---------------------------------------------------------------- apply helpers

def load_created():
    p = OUT / "created.json"
    return json.load(open(p)) if p.exists() else {"orgs": {}, "people": {}, "deals": {}}


def resolve(ref, created):
    if ref is None:
        return None
    if not ref.startswith("http"):
        for kind in ("orgs", "people", "deals"):
            if ref in created[kind]:
                ref = created[kind][ref]
                break
        else:
            raise KeyError(f"unresolved reference {ref}: create its table first and record it with --created")
    return bare_id(ref)


def write_batches(kind):
    created = load_created()
    pages = []
    if kind == "orgs":
        pages = [{"properties": o["props"]} for o in json.load(open(OUT / "orgs_new.json")) if o["key"] not in created["orgs"]]
    elif kind == "people":
        for p in json.load(open(OUT / "people_new.json")):
            if p["key"] in created["people"]:
                continue
            props = dict(p["props"])
            if p["org"]:
                props["Organisation"] = [resolve(p["org"], created)]
            pages.append({"properties": props})
    else:
        for d in json.load(open(OUT / "deals_new.json")):
            if d["key"] in created["deals"]:
                continue
            props = dict(d["props"])
            props["Organisation"] = [resolve(d["org"], created)]
            if d["contacts"]:
                props["Contacts"] = [resolve(c, created) for c in d["contacts"]]
            if d["from_engagement"]:
                props["From engagement"] = [bare_id(d["from_engagement"])]
            pages.append({"properties": props, "content": d["body"]})
    for old in (OUT / "batches").glob(f"{kind}_*.json"):
        old.unlink()
    for i in range(0, len(pages), BATCH_SIZE):
        json.dump(pages[i:i + BATCH_SIZE], open(OUT / "batches" / f"{kind}_{i // BATCH_SIZE + 1:02d}.json", "w"),
                  ensure_ascii=False, separators=(",", ":"))
    print(f"{kind}: {len(pages)} pages to create in {(len(pages) + BATCH_SIZE - 1) // BATCH_SIZE} batches (data source {SOURCES[kind]})")


def record_created(kind, path):
    """FILE: a saved SQL result with rows = url US Source ID, records joined by RS, for Migration batch = BATCH."""
    created = load_created()
    res = json.load(open(path))["results"][0]
    recs = res["rows"].split("\x1e") if res.get("rows") else []
    n = 0
    for rec in recs:
        url, sid = rec.split("\x1f")[:2]
        if kind == "deals":
            sid = sid.split("; ")[0]
        if sid not in created[kind]:
            n += 1
        created[kind][sid] = page_url(url)
    json.dump(created, open(OUT / "created.json", "w"), indent=1)
    print(f"{kind}: {len(recs)} rows in Notion with Migration batch {BATCH}; {n} newly recorded; {len(created[kind])} mapped")


def write_updates():
    created = load_created()
    out = []
    for u in json.load(open(OUT / "deals_update.json")):
        props = dict(u["props"])
        for k in ("Contacts", "Organisation", "From engagement"):
            if k in props:
                props[k] = [resolve(v, created) for v in props[k]]
        out.append({"page_id": bare_id(u["page"]), "company": u["company"], "properties": props, "body": u["body"]})
    json.dump(out, open(OUT / "updates.json", "w"), indent=1, ensure_ascii=False)
    print(f"updates: {len(out)} existing deals")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batches", choices=["orgs", "people", "deals"])
    ap.add_argument("--created", nargs=2, metavar=("KIND", "FILE"))
    ap.add_argument("--updates", action="store_true")
    ap.add_argument("--reconcile", action="store_true")
    args = ap.parse_args()
    if args.created:
        return record_created(*args.created)
    if args.batches:
        return write_batches(args.batches)
    if args.updates:
        return write_updates()
    run, new_deals, upd_deals = build()
    if args.reconcile:
        print({"orgs": len(run.orgs), "people": len(run.people), "deals_new": len(new_deals), "deals_updated": len(upd_deals)})


if __name__ == "__main__":
    sys.exit(main())
