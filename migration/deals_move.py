"""Move the commercial Engagements (PaaS, Client, Sponsor, Partner, Vendor) into the Deals table.

Usage:
  python migration/deals_move.py          build the Deals rows and the create-pages batches
  python migration/deals_move.py --plan   after created.json exists: write the repoint and retire plans

Reads (all git-ignored):
  data/out/deals/from_engagements.json   SQL export of the commercial Engagements, joined to the
                                         Organisation title ("Org name", "Org url")
  data/out/deals/ft_guest_ids.json       People ids that are the Guest on a Founder Thesis engagement
  data/out/deals/linked_rows.json        Activities and Queue rows that point at an Engagement
  data/out/paas/engagements.json         bodies written by paas.py on 2 Oct; the US VC "Budget Read"
                                         line is read from here instead of fetching 774 pages
  data/out/deals/created.json            (--plan only) old engagement url -> new deal url
Writes:
  data/out/deals/deals_new.json          one row per deal: old_url plus the create-pages properties
  data/out/deals/batches/deals_NN.json   the same, in batches of 70 for notion-create-pages
                                         (relations as bare page ids to keep each batch small)
  data/out/deals/repoint_plan.json       (--plan) Activities and Queue updates: set Deal, clear Engagement
  data/out/deals/retire_plan.json        (--plan) Engagement updates: DELETE prefix, relations cleared
  data/review/deals_move_review.csv      anything that did not map cleanly

Never edits the raw export. Re-run safely.
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data/out/deals"
REVIEW = ROOT / "data/review/deals_move_review.csv"
BATCH = "deals-move-2026-10-05"
BATCH_SIZE = 70
COMMERCIAL = {"PaaS", "Client", "Sponsor", "Partner", "Vendor"}
SHOW_SUFFIX = re.compile(r",\s*(PaaS|Founder Thesis|alpha un#|Built to Share|Human by Design)\s*$", re.I)

STAGE = {
    "Identified": "New",
    "Contacted": "Contacted",
    "In conversation": "In conversation",
    "Proposal sent": "Proposal sent",
    "Agreed": "Agreed",
    "Won": "Agreed",
}
OUTCOME = {"Declined": "Declined", "No response": "Unresponsive", "Dropped out": "Parked"}
DEAL_TAGS = {"US VC", "HK/SG", "Has podcast", "Priority A", "Priority B", "Priority C", "No email"}
BUDGET = re.compile(r"\*\*Budget Read:\*\*\s*(.+)")


def page_id(url):
    m = re.search(r"([0-9a-f]{32})", (url or "").replace("-", ""))
    return m.group(1) if m else None


def urls(cell):
    return json.loads(cell) if cell else []


def company_name(r):
    if r.get("Org name"):
        return r["Org name"].strip()
    return SHOW_SUFFIX.sub("", r["Name"] or "").strip()


def build():
    rows = json.load(open(OUT / "from_engagements.json"))
    ft_guests = set(json.load(open(OUT / "ft_guest_ids.json")))
    bodies = {}
    paas_path = ROOT / "data/out/paas/engagements.json"
    if paas_path.exists():
        for e in json.load(open(paas_path)):
            bodies[e["props"].get("Source ID")] = e.get("body") or ""

    deals, review = [], []
    for r in rows:
        if r["Type"] not in COMMERCIAL:
            review.append([r["url"], r["Name"], "Type not commercial, skipped", r["Type"]])
            continue
        guests = urls(r["Guest"])
        stakeholders = urls(r["Stakeholders"])
        contacts = []
        for u in guests + stakeholders:
            if page_id(u) not in contacts:
                contacts.append(page_id(u))
        orgs = [page_id(u) for u in urls(r["Organisation"])]

        stage = STAGE.get(r["Stage"])
        if r["Outcome"] in OUTCOME:
            stage = OUTCOME[r["Outcome"]]
        if stage is None:
            review.append([r["url"], r["Name"], "Stage not mapped", f"{r['Stage']} / {r['Outcome']}"])
            stage = "New"

        tags = [t for t in urls(r["Tags"]) if t in DEAL_TAGS]
        for t in urls(r["Tags"]):
            if t not in DEAL_TAGS:
                review.append([r["url"], r["Name"], "Tag not in Deals, dropped", t])

        entry = "FT guest first" if any(page_id(g) in ft_guests for g in guests) else "Cold outreach"

        budget = None
        m = BUDGET.search(bodies.get(r["Source ID"], ""))
        if m:
            budget = m.group(1).strip()

        source_id = r["Source ID"]
        if not source_id:
            source_id = f"Engagement {page_id(r['url'])}"
            review.append([r["url"], r["Name"], "No Source ID, set to the old engagement id", source_id])
        captured = r["date:Captured:start"] or (r["createdTime"] or "")[:10]
        if not r["date:Captured:start"]:
            review.append([r["url"], r["Name"], "No Captured date, used created time", captured])
        if not guests:
            review.append([r["url"], r["Name"], "No Guest on the engagement", ""])
        if len(orgs) != 1:
            review.append([r["url"], r["Name"], "Organisation count is not 1", str(len(orgs))])

        props = {
            "Company": company_name(r),
            "Organisation": orgs,
            "Contacts": contacts,
            "Entry path": entry,
            "Stage": stage,
            "Heat": r["Heat"],
            "Proposal link": r["Pitch link"],
            "Fit rank": r["Rank"],
            "Budget read": budget,
            "Amount": r["Amount"],
            "Next action": r["Next action"],
            "date:Next date:start": r["date:Next date:start"],
            "date:Next date:is_datetime": r["date:Next date:is_datetime"] if r["date:Next date:start"] else None,
            "Chase step": r["Chase step"],
            "Tags": json.dumps(tags) if tags else None,
            "Source": "Migration",
            "Source ID": source_id,
            "Migration batch": BATCH,
            "date:Captured:start": captured,
        }
        props = {k: v for k, v in props.items() if v not in (None, "", [])}
        deals.append({"old_url": r["url"], "old_name": r["Name"], "properties": props})

    deals.sort(key=lambda d: d["old_url"])
    json.dump(deals, open(OUT / "deals_new.json", "w"), indent=1)
    bdir = OUT / "batches"
    bdir.mkdir(exist_ok=True)
    for old in bdir.glob("deals_*.json"):
        old.unlink()
    for i in range(0, len(deals), BATCH_SIZE):
        json.dump([{"properties": d["properties"]} for d in deals[i:i + BATCH_SIZE]],
                  open(bdir / f"deals_{i // BATCH_SIZE + 1:02d}.json", "w"), separators=(",", ":"))

    REVIEW.parent.mkdir(exist_ok=True)
    with open(REVIEW, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["engagement_url", "name", "issue", "detail"])
        w.writerows(review)

    print(f"export rows {len(rows)}, deals built {len(deals)}, batches {(len(deals) + BATCH_SIZE - 1) // BATCH_SIZE}, review rows {len(review)}")
    from collections import Counter
    print("stage", dict(Counter(d["properties"]["Stage"] for d in deals)))
    print("entry path", dict(Counter(d["properties"]["Entry path"] for d in deals)))
    print("budget read", dict(Counter(d["properties"].get("Budget read") for d in deals)))
    print("company from org title", sum(1 for r in rows if r.get("Org name")), "from name", sum(1 for r in rows if not r.get("Org name")))


def plan():
    deals = json.load(open(OUT / "deals_new.json"))
    created = json.load(open(OUT / "created.json"))
    linked = json.load(open(OUT / "linked_rows.json"))
    by_old_id = {page_id(d["old_url"]): d for d in deals}
    new_for = {page_id(old): new for old, new in created.items()}
    missing = [d["old_url"] for d in deals if page_id(d["old_url"]) not in new_for]
    if missing:
        print(f"WARNING {len(missing)} deals have no created url yet")

    repoint = {"activities": [], "queue": []}
    for kind in ("activities", "queue"):
        for row_id, eng in linked[kind].items():
            eng_id = page_id(eng)
            if eng_id in by_old_id and eng_id in new_for:
                repoint[kind].append({"page_id": row_id, "Deal": [new_for[eng_id]], "Engagement": []})
    json.dump(repoint, open(OUT / "repoint_plan.json", "w"), indent=1)

    retire = [{"page_id": page_id(d["old_url"]),
               "Name": "DELETE: moved to Deals " + d["old_name"],
               "Guest": [], "Stakeholders": [], "Organisation": [], "Show": []}
              for d in deals if page_id(d["old_url"]) in new_for]
    json.dump(retire, open(OUT / "retire_plan.json", "w"), indent=1)
    print(f"repoint activities {len(repoint['activities'])}, queue {len(repoint['queue'])}; retire {len(retire)} engagements")


if __name__ == "__main__":
    plan() if "--plan" in sys.argv else build()
