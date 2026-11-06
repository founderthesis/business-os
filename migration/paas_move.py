"""PaaS move: the real Deals become Engagements on Show "PaaS" (Akshay, 6 Nov, 5/nov page item 7: "Start the movement,
put template approval in my queue"). Re-runnable and read-only: it reads snapshots, never Notion, and writes a dry-run
CSV plus a write plan the CTO executes with the Notion connector (one writer), then checks with --verify.

Usage:
  python3 migration/paas_move.py plan <deals snapshot.json> <people snapshot.json> <PaaS show page id> <YYYY-MM-DD> <out dir>
  python3 migration/paas_move.py verify <out dir>/plan.json <read-back.json>

Snapshots: the SQL results of docs/proposals/paas-move/README.md's two queries, saved under data/paas/ (git-ignored).
Selection: Warm or cold is Warm or Slow, any Stage (33 rows on 6 Nov). Cold outreach rows stay in Deals, Parked ones
included; they are listed in the CSV as excluded so the count reconciles.
"""
import sys, json, csv, os, re, hashlib

STATUS = {  # Deal Stage -> Engagement Status (Engagements has no deal ladder; the Stage is kept in the page body)
    "New": "New",
    "Contacted": "Contacted",
    "Interested": "Interested",
    "In conversation": "Interested",
    "Proposal sent": "Decision pending",
    "Parked": "Parked",
    "Unresponsive": "Unresponsive",
    "Won": "Booked",
    "Declined": "They declined",
}
INCLUDE = {"Warm", "Slow"}
OPEN = {"New", "Contacted", "Interested", "Decision pending", "Booked"}
TEAM_OK = {"Akshay", "Guest or PR", "Sarika", "Jaya"}  # Waiting on values carried; Mamatha never (decision 352)
BATCH = "paas-move-2026-11-06"


def pid(url):
    m = re.search(r"([0-9a-f]{32})", url or "")
    return m.group(1) if m else None


def jl(v):
    return json.loads(v) if v else []


def short_date(iso):
    y, m, d = iso.split("-")
    return "%d %s" % (int(d), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][int(m) - 1])


def plan(deals_p, people_p, show_id, today, out):
    deals = json.load(open(deals_p))
    people = {pid(p["url"]): p for p in json.load(open(people_p))}
    assert re.fullmatch(r"[0-9a-f]{32}", show_id), "PaaS show page id: 32 hex"
    rows, ops, problems = [], [], []
    for d in sorted(deals, key=lambda r: (r["Stage"] or "", r["Company"] or "")):
        did = pid(d["url"])
        inc = d["Warm or cold"] in INCLUDE
        contacts = [pid(u) for u in jl(d["Contacts"])]
        for c in contacts:
            if c not in people:
                problems.append("%s: contact %s not in the people snapshot" % (d["Company"], c))
        non_pr = [c for c in contacts if "PR contact" not in jl((people.get(c) or {}).get("Tags"))]
        guest = (non_pr or contacts or [None])[0]
        stake = [c for c in contacts if c != guest]
        gname = (people.get(guest) or {}).get("Name") or ""
        status = STATUS.get(d["Stage"])
        row = {
            "deal_id": did, "company": d["Company"], "stage": d["Stage"], "warm_or_cold": d["Warm or cold"],
            "include": "yes" if inc else "no (Cold outreach stays in Deals)",
            "status": status if inc else "", "guest": gname, "guest_id": guest or "",
            "stakeholders": "; ".join((people.get(c) or {}).get("Name", c) for c in stake),
            "organisation_id": ";".join(pid(u) for u in jl(d["Organisation"])),
            "activities": len(jl(d["Activities"])), "proposal_link": d["Proposal link"] or "",
            "next_date": (d["next_date"] or "")[:10], "amount": d["Amount"] or "",
        }
        if not inc:
            rows.append(row); continue
        if not guest:
            problems.append("%s: no contact, Guest left empty" % d["Company"])
        if not status:
            problems.append("%s: Stage %r has no mapping" % (d["Company"], d["Stage"]))
        if not jl(d["Organisation"]):
            problems.append("%s: no Organisation on the Deal" % d["Company"])
        name = ("%s @ %s, PaaS" % (gname, d["Company"])) if gname else ("%s, PaaS" % d["Company"])
        # Decision 496: no templates to wait for; each row starts with its real next step from the Deal.
        nxt = (d["Next action"] or "").strip()
        wait = [w for w in jl(d["Waiting on"]) if w in TEAM_OK]
        if status in OPEN:
            if not nxt:
                nxt = "Akshay: next step for %s? (moved from Deals %s)" % (d["Company"], short_date(today))
            if not wait:
                wait = ["Akshay"]
        body = ["## PaaS deal (moved %s)" % today,
                "- Deal: https://app.notion.com/p/%s" % did,
                "- Stage: %s (%s), Heat %s, Result %s" % (d["Stage"], d["Warm or cold"], d["Heat"] or "none", d["Result"] or "none"),
                "- Proposal link: %s" % (d["Proposal link"] or "none"),
                "- Pitch note: %s" % (d["Pitch note"] or "none"),
                "- Budget read: %s" % (d["Budget read"] or "none"),
                "- Last activity on the Deal: %s" % (d["Last activity"] or "none"),
                "- Deal Next action at the move: %s" % (d["Next action"] or "none"),
                "- Deal Source ID: %s" % (d["Source ID"] or "none"),
                "- Chase step: %s" % ("" if d["Chase step"] is None else int(d["Chase step"]))]
        props = {
            "Name": name, "Show": [show_id], "Status": status, "Waiting on": wait,
            "Next action": nxt,
            "Guest": [guest] if guest else [], "Stakeholders": stake,
            "Organisation": [pid(u) for u in jl(d["Organisation"])],
            "Source": "Agent", "Source ID": "deal:%s" % did, "Captured": today, "Migration batch": BATCH,
            "Claude note": "%s: moved from Deals (Stage %s -> Status %s); Deal next action: %s"
                           % (today, d["Stage"], status, (d["Next action"] or "none")[:300]),
            "Claude updated": today,
        }
        if d["next_date"]:
            props["Next date"] = d["next_date"][:10]
        if d["Amount"]:
            props["Amount"] = d["Amount"]
        ops.append({"deal_id": did, "company": d["Company"],
                    "find_first": "Engagement with Source ID deal:%s (exists: skip the create, reuse it)" % did,
                    "create_engagement": props, "page_body": "\n".join(body),
                    "activities_add_engagement": [pid(u) for u in jl(d["Activities"])],
                    "deal_update": {"Next action": "Moved to Engagements {engagement_url}"}})
        rows.append(row)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "dry-run.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    p = {"today": today, "show_id": show_id, "count": len(ops), "status_map": STATUS, "ops": ops, "problems": problems}
    b = json.dumps(p, indent=1, ensure_ascii=False, sort_keys=True).encode()
    open(os.path.join(out, "plan.json"), "wb").write(b)
    inc = sum(1 for r in rows if r["include"] == "yes")
    print("deals read %d, moving %d, staying %d, activities to relink %d, problems %d, plan sha256 %s"
          % (len(rows), inc, len(rows) - inc, sum(len(o["activities_add_engagement"]) for o in ops),
             len(problems), hashlib.sha256(b).hexdigest()[:16]))
    for x in problems:
        print("  problem:", x)


def verify(plan_p, back_p):
    """read-back.json: list of {"source_id", "url", "Name", "Status", "Show", "Waiting on", "Next action", "Guest",
    "Stakeholders", "Organisation", "activities": [ids linked to it], "deal_next_action"}."""
    p = json.load(open(plan_p)); back = {r["source_id"]: r for r in json.load(open(back_p))}
    bad = 0
    for o in p["ops"]:
        sid = o["create_engagement"]["Source ID"]; r = back.get(sid)
        if not r:
            print("MISSING", o["company"]); bad += 1; continue
        want = o["create_engagement"]
        for k in ("Name", "Status", "Next action"):
            if r.get(k) != want[k]:
                print("DIFF", o["company"], k, repr(r.get(k)), "!=", repr(want[k])); bad += 1
        for k in ("Show", "Waiting on", "Guest", "Stakeholders", "Organisation"):
            if sorted(r.get(k) or []) != sorted(want[k]):
                print("DIFF", o["company"], k); bad += 1
        if sorted(set(o["activities_add_engagement"]) - set(r.get("activities") or [])):
            print("ACTIVITY NOT LINKED", o["company"]); bad += 1
        if not (r.get("deal_next_action") or "").startswith("Moved to Engagements "):
            print("DEAL NOT MARKED", o["company"]); bad += 1
    extra = set(back) - {o["create_engagement"]["Source ID"] for o in p["ops"]}
    print("checked %d of %d, %d problems, %d unexpected rows" % (len(p["ops"]) - 0, p["count"], bad, len(extra)))
    return bad


if __name__ == "__main__":
    if sys.argv[1] == "plan":
        plan(*sys.argv[2:7])
    elif sys.argv[1] == "verify":
        sys.exit(1 if verify(sys.argv[2], sys.argv[3]) else 0)
