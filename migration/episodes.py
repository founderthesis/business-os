"""Merge every episode source into Episodes, with guest People and Engagements.

Usage: python migration/episodes.py

Sources (all git-ignored, extracted read-only):
  data/raw/notion/episode_inventory.json   old Notion Episode Inventory (FT 460, Spotlight 122)
  data/raw/notion/article_queue.json       old Notion Article Queue (439, the Substack back-catalogue work)
  data/raw/blue/records.json               all Blue records
  data/out/blue_inflight_summary.json      the 31 in-flight FT episodes already created in Notion
  data/raw/notion/people_snapshot.json, orgs_snapshot.json  + data/out/paas/*  current People and Organisations
  data/out/pr_contacts.json                PR contacts guessed from Blue guest forms (migration/pr_contacts.py)

Rules (Akshay, 2 Oct):
  - Match episodes on the YouTube video id; Blue cards without a video fall back to guest name.
  - Archived Blue cards come in tagged Archived. A card whose episode is live on YouTube merges into
    that episode instead, so a live episode is never hidden.
  - Post-release stages (Shorts, Medium, Newsletter) all become Published.
  - Every Blue guest card gets an Engagement holding the dossier and all stakeholders (PR contacts).
  - Inner Journeys guests come in as People only. Design jobs and prompts stay out.

Writes data/out/episodes/{episodes_new, episodes_update, people_new, orgs_new, engagements}.json and
data/review/episodes_review.csv. Never edits the raw files. Re-run safely.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paas import Index, Run, emails, fold, li_slug, name_key, org_key, page_url, domain_of  # noqa: E402
from pr_contacts import FREE_MAIL, domain_stem  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data/raw"
OUT = ROOT / "data/out/episodes"
BATCH = "episodes-2026-10-02"
TODAY = "2026-10-02"

SHOWS = {"FT": "https://app.notion.com/p/3ed19a301a7f817c9367e0d88afc5776",
         "AU": "https://app.notion.com/p/3ed19a301a7f8111b5e4d46002a7afe1",
         "B2S": "https://app.notion.com/p/3ed19a301a7f819e8f45de04a7c9d025",
         "HBD": "https://app.notion.com/p/3ed19a301a7f815585e7e6c8accaab23"}
SHOW_NAME = {"FT": "Founder Thesis", "AU": "alpha un#", "B2S": "Built to Share", "HBD": "Human by Design"}
WORKSPACE_SHOW = {"FT & Spotlight": "FT", "alpha un#": "AU", "Hissa Podcast": "B2S", "FastCode Podcast": "HBD"}
STATUS = {"Recorded": "Recorded", "Hold": "Recorded", "Slotted": "Recorded", "Doc Ready": "Copy in progress",
          "Video QC": "Editing", "Published": "Published", "Shorts In Progress": "Published",
          "Medium in progress": "Published", "Newsletter Published": "Published"}
# Blue cards with no video whose guest has several episodes, resolved by hand (Akshay, 3 Oct)
BLUE_EPISODE_FIX = {"cm2sspr5m0r43qzcwht4yy9vg": "ei:3c419a30-1a7f-8189-832c-e3bffd8405c9"}  # CleverTap, recorded 27 Oct 2024
SECTORS = {"Fintech", "SaaS", "D2C", "Marketplace", "Deeptech", "Edtech", "Healthtech", "Services", "Gaming"}

# Blue field names differ by workspace
F = {
    "youtube": ["Youtube Link", "YouTube Link", "You Tube Link"],
    "spotify": ["Spotify Link", "Spofity Link"],
    "apple": ["Apple Podcast", "Apple Podcast Link"],
    "amazon": ["Amazon Music Link"],
    "substack": ["Substack Published Page", "Substack Link", "Published Newsletter Link"],
    "guest": ["Guest Name"],
    "company": ["Guest Organisation Name", "Co Name", "Company Name", "Org Name"],
    "title": ["Formal Designation of the guest", "Guest Title"],
    "linkedin": ["Guest LinkedIn Profile Link", "Guest Linkedin Profile", "Guest LinkedIn profile"],
    "email": ["Guest Email ID", "Email ID"],
    "working_doc": ["Link to working doc", "Link to Working Doc", "Link to working Doc"],
    "dossier": ["Dossier", "Dossier#2"],
    "short": ["podm.in Short Link", "short link", "Shortlink"],
    "website": ["Co Website", "Org Website"],
}


def get(rec, key):
    cf = rec["custom_fields"]
    for k in F[key]:
        if cf.get(k):
            return str(cf[k]).strip()
    return None


def yt_id(u):
    m = re.search(r"(?:v=|youtu\.be/|/shorts/|/live/|/embed/)([A-Za-z0-9_-]{11})", str(u or ""))
    return m.group(1) if m else None


def clean_url(u):
    u = str(u or "").strip()
    return u if u.startswith("http") else None


HONORIFIC = re.compile(r"^(mr|mrs|ms|dr|prof)\.?\s+", re.I)
ROLE_WORDS = re.compile(r"\b(ceo|founder|co-founder|president|director|partner|cto|coo|cfo)\b", re.I)


def clean_name(n):
    return HONORIFIC.sub("", re.sub(r"\s+", " ", str(n or "")).strip()) or None


def guest_from_title(title):
    left = str(title).split("@")[0].strip()
    return left if "@" in str(title) else None


def load_people_orgs():
    people = json.load(open(RAW / "notion/people_snapshot.json"))
    orgs = json.load(open(RAW / "notion/orgs_snapshot.json"))
    created = json.load(open(ROOT / "data/out/paas/created.json"))
    url = lambda i: f"https://app.notion.com/p/{i}"
    for o in json.load(open(ROOT / "data/out/paas/orgs_new.json")):
        if o["key"] in created["orgs"]:
            orgs.append({"url": url(created["orgs"][o["key"]]), "Name": o["props"]["Name"],
                         "Domain": o["props"].get("Domain"), "Website": o["props"].get("Website")})
    for p in json.load(open(ROOT / "data/out/paas/people_new.json")):
        if p["key"] in created["people"]:
            org = p["org"] if p["org"].startswith("http") else url(created["orgs"].get(p["org"], ""))
            people.append({"url": url(created["people"][p["key"]]), "Name": p["props"]["Name"],
                           "LinkedIn": p["props"].get("LinkedIn"), "Email": p["props"].get("Email"),
                           "Other emails": p["props"].get("Other emails"), "Organisation": [org]})
    return people, orgs


class Episodes:
    def __init__(self):
        self.rows = {}          # key -> episode dict
        self.by_yt = {}
        self.by_guest = defaultdict(list)
        self.by_company = defaultdict(list)

    def add(self, key, ep):
        self.rows[key] = ep
        if ep.get("yt"):
            self.by_yt[ep["yt"]] = key
        for g in ep["guest_names"]:
            self.by_guest[(ep["show"], name_key(g))].append(key)
        if ep.get("company"):
            self.by_company[(ep["show"], org_key(ep["company"]))].append(key)
        return key

    def find(self, show, yt, guest, company, strict=False):
        """YouTube id first; then a unique guest-name match; then a unique company match.
        strict: a card with its own unknown video is a different episode, so it may only fall back
        onto an episode that has no video yet (a repeat guest must not merge into their old episode)."""
        if yt and yt in self.by_yt:
            return self.by_yt[yt]
        ok = lambda k: not (strict and yt and self.rows[k].get("yt"))
        for g in re.split(r"\s+(?:&|and)\s+", guest or ""):
            hits = [k for k in self.by_guest.get((show, name_key(g)), []) if ok(k)] if g else []
            if len(hits) == 1:
                return hits[0]
        hits = [k for k in self.by_company.get((show, org_key(company)), []) if ok(k)] if company else []
        return hits[0] if len(hits) == 1 else None


def main():
    ei = json.load(open(RAW / "notion/episode_inventory.json"))
    aq = json.load(open(RAW / "notion/article_queue.json"))
    blue = json.load(open(RAW / "blue/records.json"))
    inflight = {r["blue_id"]: r for r in json.load(open(ROOT / "data/out/blue_inflight_summary.json"))["records"]}
    pr = json.load(open(ROOT / "data/out/pr_contacts.json"))

    people, orgs = load_people_orgs()
    run = Run(Index(people, orgs))
    # existing rows already tagged Guest: a full-name match to exactly one of them is the same guest,
    # even when the company is spelled differently (e.g. "GOQii" vs "Goqii Technologies")
    known_guests = defaultdict(list)
    for p in people:
        tags = p.get("Tags") or []
        tags = json.loads(tags) if isinstance(tags, str) else tags
        if "Guest" in tags and p.get("Match status") != "Merged into another row":
            known_guests[name_key(p["Name"])].append(page_url(p["url"]))
    eps = Episodes()
    review = run.review

    # 1. Old Notion Episode Inventory is the base for the FT and Spotlight back catalogue
    for r in ei:
        spot = r.get("Show") == "Spotlight"
        theme = [t for t in json.loads(r.get("Theme") or "[]") if t in SECTORS]
        guests = [g.strip() for g in re.split(r"\s+(?:&|and)\s+|,", r.get("Guest") or "") if g.strip()]
        props = {"Title": r["Episode"], "Status": "Published", "Source": "Migration", "Migration batch": BATCH,
                 "Source ID": f"Episode Inventory {r['id']}", "date:Captured:start": TODAY,
                 "Old Notion page": page_url(r["url"]), "Tags": ["Tier 3 Spotlight"] if spot else []}
        for k, src in [("YouTube", "YouTube URL"), ("Spotify", "Spotify URL"), ("Apple", "Apple URL"),
                       ("Substack", "Substack URL")]:
            if clean_url(r.get(src)):
                props[k] = clean_url(r[src])
        if r.get("Views"):
            props["YouTube views"] = float(r["Views"])
        if theme:
            props["Sector"] = theme
        if r.get("Article state"):
            props["Article state"] = r["Article state"]
        if r.get("date:Published:start"):
            props["date:Actual release:start"] = r["date:Published:start"]
        eps.add(f"ei:{r['id']}", {"show": "FT", "yt": yt_id(r.get("YouTube URL")), "props": props,
                                  "guest_names": guests, "company": r.get("Company"), "body": [], "blue": []})

    # 2. Article Queue: priority, drafting state and a link to the old article working page
    aq_new = 0
    for r in aq:
        key = eps.by_yt.get(yt_id(r.get("YouTube URL")))
        if not key and re.search(r"\|\s*Shorts\s*\d", r.get("Episode") or ""):
            review.append({"source": "Article Queue", "name": r.get("Guest"), "issue": "a Short, not an episode",
                           "action": "Not imported"})
            continue
        if not key:
            spot = r.get("Show") == "Spotlight"
            props = {"Title": r["Episode"], "Status": "Published", "Source": "Migration", "Migration batch": BATCH,
                     "Source ID": f"Article Queue {r['id']}", "date:Captured:start": TODAY,
                     "Old Notion page": page_url(r["url"]), "Tags": ["Tier 3 Spotlight"] if spot else []}
            if clean_url(r.get("YouTube URL")):
                props["YouTube"] = clean_url(r["YouTube URL"])
            if clean_url(r.get("Substack URL")):
                props["Substack"] = clean_url(r["Substack URL"])
            key = eps.add(f"aq:{r['id']}", {"show": "FT", "yt": yt_id(r.get("YouTube URL")), "props": props,
                                            "guest_names": [r["Guest"]] if r.get("Guest") else [],
                                            "company": r.get("Company"), "body": [], "blue": []})
            aq_new += 1
            review.append({"source": "Article Queue", "name": r.get("Guest"), "issue": "no Episode Inventory row",
                           "action": "Created as its own episode; probably a Spotlight video missing from the inventory"})
        ep = eps.rows[key]
        if r.get("Priority"):
            ep["props"]["Article priority"] = float(r["Priority"])
        if r.get("Pipeline") == "Drafted":
            ep["props"]["Article state"] = "Drafted"
        elif r.get("Pipeline") == "Published":
            ep["props"]["Article state"] = "Full"
        ep["body"].append(f"- **Article working page (old Notion):** {page_url(r['url'])}")
        if r.get("Agent notes"):
            ep["body"].append(f"- **Article agent notes:** {r['Agent notes']}")

    # 3. Blue Episodes Inventory: tier tags and old working docs onto the same episodes
    blue_ei_unmatched = 0
    for r in [b for b in blue if b["workspace"] == "Episodes Inventory"]:
        key = eps.find("FT", yt_id(get(r, "youtube")), get(r, "guest") or guest_from_title(r["title"]), get(r, "company"))
        if not key:
            blue_ei_unmatched += 1
            review.append({"source": "Blue Episodes Inventory", "name": r["title"], "issue": "no matching episode",
                           "action": "Not imported; the audit found every inventory card already in Notion"})
            continue
        ep = eps.rows[key]
        for t in r["tags"] or []:
            if t in ("Tier 1", "Tier 2") and "Tier 3 Spotlight" not in ep["props"]["Tags"]:
                ep["props"]["Tags"].append(t)
        if get(r, "working_doc"):
            ep["body"].append(f"- **Working doc (Google, from Blue):** {get(r, 'working_doc')}")
        if not ep["props"].get("Spotify") and clean_url(get(r, "spotify")):
            ep["props"]["Spotify"] = clean_url(get(r, "spotify"))
        if not ep["props"].get("Apple") and clean_url(get(r, "apple")):
            ep["props"]["Apple"] = clean_url(get(r, "apple"))
        ep["blue"].append(r["original_id"])

    # 4. Blue guest cards (FT, alpha un#, Hissa, FastCode): episodes plus an Engagement each
    pr_by_record = defaultdict(list)
    for c in pr:
        for rid in c["blue_records"]:
            pr_by_record[rid].append(c)
    new_from_blue, merged_from_blue = Counter(), Counter()
    engagement_cards = []
    for r in [b for b in blue if b["workspace"] in WORKSPACE_SHOW]:
        show = WORKSPACE_SHOW[r["workspace"]]
        rid = r["original_id"]
        guest = clean_name(get(r, "guest") or guest_from_title(r["title"]))
        company = get(r, "company") or (r["title"].split("@", 1)[1].strip() if "@" in r["title"] else None)
        if company and ROLE_WORDS.search(company):  # a designation typed into the company field
            company = r["title"].split("@", 1)[1].strip() if "@" in r["title"] else r["title"].strip()
        archived = r["list"] == "Archived"
        yt = yt_id(get(r, "youtube"))
        if rid in inflight:
            key = f"existing:{rid}"
            eps.rows[key] = {"show": show, "existing_url": page_url(inflight[rid]["notion_episode_url"]),
                             "props": {}, "guest_names": [guest] if guest else [], "company": company,
                             "body": [], "blue": [rid]}
        else:
            key = BLUE_EPISODE_FIX.get(rid) or eps.find(show, yt, guest, company, strict=True)
            if not key and not yt and guest and len(eps.by_guest.get((show, name_key(guest)), [])) > 1:
                review.append({"source": f"Blue {r['workspace']}", "name": r["title"],
                               "issue": "no video and the guest has several episodes",
                               "action": "Add the card to BLUE_EPISODE_FIX; no new episode created"})
                continue
            if key:
                merged_from_blue[r["workspace"]] += 1
            else:
                tags = []
                if "SL" in (r["tags"] or []):
                    tags.append("Tier 3 Spotlight")
                if "FT Tier 2" in (r["tags"] or []) or "Tier 2" in (r["tags"] or []):
                    tags.append("Tier 2")
                if "Paid" in (r["tags"] or []):
                    tags.append("Sponsored")
                if archived:
                    tags.append("Archived")
                if show == "HBD":
                    tags.append("Guest review")
                title = (r["custom_fields"].get("Episode Title") or
                         (f"{guest} @ {company}" if guest and company else r["title"])).strip()
                props = {"Title": title, "Source": "Migration", "Migration batch": BATCH,
                         "Source ID": f"Blue {rid}", "date:Captured:start": TODAY, "Tags": tags}
                status = STATUS.get(r["list"]) or ("Published" if yt else None)
                if status:
                    props["Status"] = status
                key = eps.add(f"blue:{rid}", {"show": show, "yt": yt, "props": props,
                                              "guest_names": [guest] if guest else [], "company": company,
                                              "body": [], "blue": []})
                new_from_blue[r["workspace"]] += 1
            ep = eps.rows[key]
            p = ep["props"]
            for k, fk in [("YouTube", "youtube"), ("Spotify", "spotify"), ("Apple", "apple"), ("Substack", "substack")]:
                if not p.get(k) and clean_url(get(r, fk)):
                    p[k] = clean_url(get(r, fk))
            rec = r["custom_fields"].get("Date of recording")
            if rec and not p.get("date:Recording date:start"):
                p["date:Recording date:start"] = rec[:10]
            if show == "FT" and r.get("created_via_form"):
                p["Guest form in"] = "__YES__"
            for label, fk in [("Working doc (Google, from Blue)", "working_doc"), ("Amazon Music", "amazon"),
                              ("Short link", "short")]:
                if get(r, fk):
                    ep["body"].append(f"- **{label}:** {get(r, fk)}")
            ep["blue"].append(rid)
        engagement_cards.append((r, key, show, guest, company, archived, yt))

    # 5. Guests -> People, for every episode
    def guest_ref(name, company, li=None, mail=None, title=None, show="FT", label=""):
        hits = known_guests.get(name_key(name), [])
        if len(hits) == 1 and len(name_key(name).split()) >= 2:
            run.matched["name, existing guest"] = run.matched.get("name, existing guest", 0) + 1
            return hits[0], None
        org_ref = None
        if company:
            org_ref, _ = run.org(company.strip(), None, {"Type": "Startup", "Source": "Migration", "Source ID": label,
                                                          "Migration batch": BATCH, "date:Captured:start": TODAY}, "")
        ref = run.person(name.strip(), title, li_slug(li), emails(mail), org_ref, label, BATCH, ["Guest"], label)
        newp = next((x for x in run.people if x["key"] == ref), None)
        if newp is not None and show == "FT":
            newp["props"]["FT guest"] = "__YES__"
        return ref, org_ref

    card_by_key = defaultdict(list)
    for card in engagement_cards:
        card_by_key[card[1]].append(card)
    for key, ep in eps.rows.items():
        refs = []
        cards = card_by_key.get(key, [])
        if cards:
            for (r, _, show, guest, company, _, _) in cards:
                if guest:
                    ref, _ = guest_ref(guest, company, get(r, "linkedin"), get(r, "email"), get(r, "title"), show,
                                       f"Blue {r['original_id']}")
                    refs.append(ref)
        else:
            for g in ep["guest_names"]:
                ref, _ = guest_ref(g, ep.get("company"), show=ep["show"], label=ep["props"].get("Source ID", ""))
                refs.append(ref)
        ep["guests"] = list(dict.fromkeys(refs))
        if len(ep["guests"]) > 1 and "props" in ep and "Tags" in ep["props"] and "Two guests" not in ep["props"]["Tags"]:
            ep["props"]["Tags"].append("Two guests")

    # 6. PR contacts -> People, linked as stakeholders on the guest's Engagement
    domain_guests = defaultdict(set)
    for c in pr:
        if c.get("domain"):
            domain_guests[c["domain"]].update(filter(None, c["guests"]))
    pr_ref = {}
    for c in pr:
        org_ref = None
        if c.get("domain"):
            # a domain seen across several guests is a PR agency; otherwise it is the guest company's own comms
            # team, linked only if that company is already an organisation (no orgs named after bare domains)
            if len(domain_guests[c["domain"]]) > 1:
                org_ref, _ = run.org(c["org_stem"].capitalize(), c["domain"],
                                     {"Type": "PR agency", "Domain": c["domain"], "Source": "Migration",
                                      "Source ID": "Blue guest forms", "Migration batch": BATCH,
                                      "date:Captured:start": TODAY}, "")
            else:
                org_ref = run.idx.org(c["org_stem"], c["domain"])
        name = c["name"] or c["email"].split("@")[0]
        ref = run.person(name, None, None, [c["email"]] if not c["role_inbox"] else [], org_ref, "Blue guest forms",
                         BATCH, c["tags"], f"PR contact {c['email'].split('@')[1]}")
        newp = next((x for x in run.people if x["key"] == ref), None)
        if newp is not None and c["role_inbox"]:
            newp["props"]["Email"] = c["email"]
            newp["props"]["Tags"] = json.dumps([t for t in json.loads(newp["props"]["Tags"]) if t != "No email"])
        pr_ref[c["email"]] = ref

    # 7. Engagements, one per Blue guest card
    engagements = []
    for (r, key, show, guest, company, archived, yt) in engagement_cards:
        ep = eps.rows[key]
        guest_refs = [g for g in ep.get("guests", [])][:1] if guest else []
        stake = [pr_ref[c["email"]] for c in pr_by_record.get(r["original_id"], []) if c["email"] in pr_ref]
        published = ep["props"].get("Status") == "Published" or STATUS.get(r["list"]) == "Published"
        outcome = "Done" if published else ("Dropped out" if archived and not yt else "Live")
        props = {"Name": f"{guest or r['title']}{' @ ' + company if company and guest else ''}, {SHOW_NAME[show]}",
                 "Stage": "Agreed", "Outcome": outcome, "Source": "Migration", "Source ID": f"Blue {r['original_id']}",
                 "Migration batch": BATCH, "date:Captured:start": TODAY}
        if get(r, "dossier"):
            props["Dossier link"] = clean_url(get(r, "dossier")) or None
        engagements.append({"props": {k: v for k, v in props.items() if v is not None}, "show": SHOWS[show],
                            "episode": key, "guest": guest_refs, "stakeholders": list(dict.fromkeys(stake)),
                            "org": run.idx.org(company) if company else None})

    # 8. Inner Journeys guests: People only
    ij = 0
    for r in [b for b in blue if b["workspace"] == "Inner Journeys"]:
        guest = get(r, "guest") or guest_from_title(r["title"])
        if not guest:
            continue
        guest_ref(guest, get(r, "company"), get(r, "linkedin"), get(r, "email"), get(r, "title"), "IJ",
                  f"Blue {r['original_id']}")
        ij += 1

    # Output
    OUT.mkdir(parents=True, exist_ok=True)
    new_eps, upd_eps = [], []
    for key, ep in eps.rows.items():
        body = "\n".join(dict.fromkeys(ep["body"]))
        if key.startswith("existing:"):
            upd_eps.append({"url": ep["existing_url"], "guests": ep.get("guests", []), "body": body})
            continue
        p = ep["props"]
        p["Tags"] = json.dumps(list(dict.fromkeys(p.get("Tags", []))))
        if isinstance(p.get("Sector"), list):
            p["Sector"] = json.dumps(p["Sector"])
        if ep["blue"]:
            body = (body + "\n" if body else "") + f"- **Blue cards:** {', '.join(ep['blue'])}"
        new_eps.append({"key": key, "props": p, "show": SHOWS[ep["show"]], "guests": ep.get("guests", []),
                        "body": ("## Links from the old systems\n\n" + body) if body else ""})
    for name, data in [("episodes_new", new_eps), ("episodes_update", upd_eps), ("people_new", run.people),
                       ("orgs_new", run.orgs), ("engagements", engagements)]:
        json.dump(data, open(OUT / f"{name}.json", "w"), indent=1, ensure_ascii=False)
    pd.DataFrame(review).to_csv(ROOT / "data/review/episodes_review.csv", index=False)

    blue_cards = sum(1 for b in blue if b["workspace"] in WORKSPACE_SHOW)
    print(f"episode inventory {len(ei)} + article-queue-only {aq_new} + new from Blue {sum(new_from_blue.values())} "
          f"= {len(new_eps)} new episodes; {len(upd_eps)} in-flight episodes updated")
    print(f"Blue guest cards {blue_cards}: in-flight {len(upd_eps)}, merged into an existing episode "
          f"{dict(merged_from_blue)}, new {dict(new_from_blue)}")
    print(f"Blue inventory cards unmatched {blue_ei_unmatched}; Inner Journeys guests {ij}")
    print(f"engagements {len(engagements)}; stakeholders linked {sum(len(e['stakeholders']) for e in engagements)}")
    print(f"people new {len(run.people)}; orgs new {len(run.orgs)}; matched existing {run.matched}")
    print(f"tags: {Counter(t for e in new_eps for t in json.loads(e['props']['Tags']))}")
    print(f"review rows {len(review)}")
    assert len(new_eps) == len(ei) + aq_new + sum(new_from_blue.values()), "episode counts do not reconcile"
    assert len(upd_eps) + sum(merged_from_blue.values()) + sum(new_from_blue.values()) == blue_cards, \
        "Blue card counts do not reconcile"


if __name__ == "__main__":
    sys.exit(main())
