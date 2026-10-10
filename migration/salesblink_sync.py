"""Salesblink campaigns into Engagements: who was mailed, who replied, who bounced, who is queued, and what the
manual chase rows become now that the manual campaign has stopped (decision 113).

Usage:
  python migration/salesblink_sync.py

Reads (git-ignored, data/raw/salesblink/):
  seq_b2s1_2026-10-10.csv, seq_hbd1_2026-10-10.csv, seq_hbd2_2026-10-10.csv   Salesblink "export sequence leads"
  list_b2s1_2026-10-10.json      every contact on the B2S 1 list (started or queued)
  list_hbd2_2026-10-10.json      every contact on the HBD 2 list (optional)
  replies_2026-10-10.json        replies read from the Salesblink inbox, with an outcome per reply
  notion_engagements_2026-10-10.json   Built to Share and Human by Design Engagements from Notion
and data/out/b2s_pipeline/candidates.json, data/out/hbd_pipeline/candidates.json for emails and mail dates.
Writes:
  data/out/salesblink/notion_ai_salesblink_sync.md   one Notion AI prompt (decision 91)
  data/review/salesblink_sync_review.csv              leads with no Engagement, and double-mail risks

Rules:
- A lead Salesblink has mailed is Contacted, Waiting on Guest or PR. Next date is the day after the last step
  plus a week; if nobody has replied by then the row goes Unresponsive. Until then it stays out of "today".
- A bounce asks Chaandini for a new address. A reply sets the status from its outcome.
- A lead on a list but not yet mailed keeps its status; Next action says it is queued, so no one mails it by hand.
- Built to Share rows that were being chased by hand, are not in Salesblink and have had 3 or more mails become
  Unresponsive with a re-engage date 60 days after the last mail. Rows with 1 or 2 mails are listed for a call.
Re-run safely; never edits the raw files.
"""
import csv
import datetime as dt
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data/raw/salesblink"
OUT = ROOT / "data/out/salesblink"
REVIEW = ROOT / "data/review"
TODAY = dt.date(2026, 10, 10)
ENG_DB = "https://app.notion.com/p/5e77c373909a4bf6b9195570de46c63b"
PEOPLE_DB = "https://app.notion.com/p/f54094b86c3549dead74c0034afad86c"
ORGS_DB = "https://app.notion.com/p/4e484b1c510b42ce9ea979307bff31e4"
SHOW_PAGE = {"Human by Design": "https://app.notion.com/p/3ed19a301a7f815585e7e6c8accaab23",
             "Built to Share": "https://app.notion.com/p/3ed19a301a7f819e8f45de04a7c9d025"}
BATCH = "salesblink-sync-2026-10-10"

# name, show, csv, delays between steps in days (from Salesblink), paused?
SEQS = {
    "B2S 1": ("Built to Share", "seq_b2s1_2026-10-10.csv", [3, 5, 7, 7, 7], True),
    "HBD 1": ("Human by Design", "seq_hbd1_2026-10-10.csv", [3, 4, 7, 7], False),
    "HBD 2": ("Human by Design", "seq_hbd2_2026-10-10.csv", [3, 4, 7, 7], False),
}
LISTS = {"B2S 1": "list_b2s1_2026-10-10.json", "HBD 2": "list_hbd2_2026-10-10.json"}
FREE_MAIL = {"gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com"}
# Arjun's yes covers Fortune 500 AI heads and CTOs (decision 110); other titles stay Tier 1.5 for him to call
AI_HEAD = re.compile(r"\bAI\b|Artificial Intelligence|Chief Technology Officer|\bCTO\b|Chief Digital and Information|"
                     r"Chief Data and Analytics|\bCIO\b", re.I)
NOT_AI_HEAD = {"stuartfeld", "joelhellermark"}


def key(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z]", "", s)


def person_of(eng_name):
    base = eng_name.rsplit(",", 1)[0]
    return base.split(" @ ")[0].strip()


def load_cands():
    by_email = {}
    for show, p in (("Built to Share", "data/out/b2s_pipeline/candidates.json"),
                    ("Human by Design", "data/out/hbd_pipeline/candidates.json")):
        for c in json.load(open(ROOT / p))["cands"]:
            for e in (c.get("email"), c.get("other_email")):
                if e:
                    by_email[(show, e.lower())] = c
    return by_email


def main():
    eng = json.load(open(RAW / "notion_engagements_2026-10-10.json"))
    rows = {}
    for r in eng:
        show = "Built to Share" if r["Name"].endswith("Built to Share") else "Human by Design"
        rows.setdefault((show, key(person_of(r["Name"]))), []).append(r)
    cands = load_cands()
    replies = {x["email"].lower(): x for x in json.load(open(RAW / "replies_2026-10-10.json"))}

    def find(show, email, first, last):
        c = cands.get((show, (email or "").lower()))
        for name in ([c["name"]] if c else []) + [f"{first} {last}"]:
            hit = rows.get((show, key(name)))
            if hit and len(hit) == 1:
                return hit[0], c
        return None, c

    updates, review, seen, new = {}, [], set(), {}
    for seq, (show, f, delays, paused) in SEQS.items():
        n_steps = len(delays) + 1
        for l in csv.DictReader(open(RAW / f)):
            r, c = find(show, l["email"], l["first_name"], l["last_name"])
            if not r:
                review.append({"seq": seq, "lead": f"{l['first_name']} {l['last_name']}", "company": l["company_name"],
                               "issue": "mailed by Salesblink, no Engagement in Notion", "salesblink_status": l["status"]})
                new[(show, key(l["first_name"] + l["last_name"]))] = dict(l, seq=seq, show=show, mailed=True)
                continue
            seen.add(r["url"])
            sent = int(l["sent"] or 0)
            first = dt.date.fromisoformat(l["created_date"][:10])
            prior = int(r["Chase step"] or 0) if r["Status"] != "New" else 0
            u = {"Status": "Contacted", "Waiting on": "Guest or PR", "Chase step": prior + sent}
            rep = replies.get(l["email"].lower())
            if l["bounced"] == "1":
                u = {"Next action": "Find a new email: Salesblink bounced", "Waiting on": "Chaandini",
                     "Next date": TODAY.isoformat()}
                if r["Status"] == "New":
                    u["Status"] = "New"
            elif rep and rep["outcome"] == "declined":
                u.update(Status="They declined", **{"Waiting on": "", "Next date": "", "Next action": ""})
                u["Claude note"] = f"Declined by reply to Salesblink {seq} on {rep['date']}: {rep['text']}"
            elif rep and rep["outcome"] == "wrong_email":
                u.update(**{"Next action": "Find a new email: they have moved on", "Waiting on": "Chaandini",
                            "Next date": TODAY.isoformat()})
                u["Claude note"] = f"Salesblink {seq} reply on {rep['date']}: {rep['text']}"
            elif rep and rep["outcome"] == "auto_ack":
                u = {"Claude note": f"Salesblink {seq} got an auto-reply on {rep['date']}: {rep['text']} "
                                    "Salesblink stops on any reply, so the next chase is by hand."}
                if r["Status"] in ("New", "Contacted"):
                    u.update(Status="Contacted", **{"Next action": "Chase the media team by hand",
                                                    "Waiting on": "Guest or PR",
                                                    "Next date": (TODAY + dt.timedelta(days=5)).isoformat()})
            else:
                end = first + dt.timedelta(days=sum(delays) + 7)
                u["Next date"] = end.isoformat()
                u["Next action"] = (f"Salesblink {seq}: {sent} of {n_steps} sent"
                                    + (" (paused)" if paused else "") + ". No reply by this date: Unresponsive")
            if prior >= 3 and seq.startswith("B2S"):
                review.append({"seq": seq, "lead": r["Name"], "company": l["company_name"],
                               "issue": f"already had {prior} manual mails before Salesblink started again at Email 1",
                               "salesblink_status": l["status"]})
            updates[r["url"]] = (r, u)
        lf = LISTS.get(seq)
        if lf and (RAW / lf).exists():
            for l in json.load(open(RAW / lf)):
                r, c = find(show, l["email"], l["first_name"], l["last_name"])
                if not r:
                    k = (show, key(l["first_name"] + l["last_name"]))
                    if k in new:
                        new[k].setdefault("job_title", l.get("job_title"))
                    else:
                        review.append({"seq": seq, "lead": f"{l['first_name']} {l['last_name']}",
                                       "company": l["company_name"],
                                       "issue": "queued in Salesblink, no Engagement in Notion",
                                       "salesblink_status": "queued"})
                        new[k] = dict(l, seq=seq, show=show, mailed=False)
                    continue
                if r["url"] in seen:
                    continue
                seen.add(r["url"])
                personal = l["email"].split("@")[-1].lower() in FREE_MAIL
                if r["Status"] in ("New",):
                    updates[r["url"]] = (r, {"Next action": f"Queued in Salesblink {seq}: don't mail by hand"
                                             + ("; swap the personal address for a work one" if personal else "")})
                else:
                    if int(r["Chase step"] or 0) >= 1:
                        updates[r["url"]] = (r, {"Next action": f"Take out of Salesblink {seq} before it resumes: "
                                                               f"{r['Chase step']} mails already sent by hand",
                                                 "Waiting on": "Chaandini", "Next date": TODAY.isoformat()})
                    review.append({"seq": seq, "lead": r["Name"], "company": l["company_name"],
                                   "issue": f"queued in Salesblink while Notion says {r['Status']}"
                                            + (f", {r['Chase step']} mails already" if r["Chase step"] else ""),
                                   "salesblink_status": "queued"})

    # Built to Share manual chase rows not in Salesblink: the manual campaign has stopped
    b2s_c = {}
    for c in json.load(open(ROOT / "data/out/b2s_pipeline/candidates.json"))["cands"]:
        b2s_c.setdefault(key(c["name"]), c)
    stopped, small = 0, []
    for r in eng:
        if not r["Name"].endswith("Built to Share") or r["url"] in seen:
            continue
        if r["Status"] != "Contacted" or "Warm intro" in (r["Tags"] or "") or "Guest or PR" not in (r["Waiting on"] or ""):
            continue
        if not (r["Next action"] or "").startswith("Follow-up"):
            continue
        chase = int(r["Chase step"] or 0)
        c = b2s_c.get(key(person_of(r["Name"])))
        sent = sorted(d for d in (c or {}).get("sent", []) if d <= TODAY.isoformat())
        last = dt.date.fromisoformat(sent[-1]) if sent else TODAY
        if chase >= 3:
            updates[r["url"]] = (r, {"Status": "Unresponsive", "Waiting on": "",
                                     "Next action": "Re-engage: 2 months since the last mail",
                                     "Next date": (last + dt.timedelta(days=60)).isoformat()})
            stopped += 1
        else:
            small.append(r)
            review.append({"seq": "manual", "lead": r["Name"], "company": "",
                           "issue": f"manual chase stopped after {chase} mail(s); not in Salesblink",
                           "salesblink_status": ""})

    for r in eng:
        if "Fortune 500 AI leader" in (r["Tags"] or ""):
            tier = "Tier 1.5" if key(person_of(r["Name"])) in NOT_AI_HEAD else "Tier 1"
            r0, u = updates.get(r["url"], (r, {}))
            if tier != r["Tier"]:
                u["Tier"] = tier
            if r["url"] not in seen and r["Status"] == "New" and tier == "Tier 1":
                u["Next action"] = "First mail: not in Salesblink HBD 2 yet, find a current work email"
            if tier == "Tier 1.5":
                u["Next action"] = "Ask Arjun: not an AI head or CTO" + (
                    " (already in Salesblink HBD 2)" if u.get("Status") == "Contacted" else "")
                u["Waiting on"] = "Arjun"
            if u:
                updates[r["url"]] = (r0, u)

    OUT.mkdir(parents=True, exist_ok=True)
    REVIEW.mkdir(parents=True, exist_ok=True)
    with open(REVIEW / "salesblink_sync_review.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["seq", "lead", "company", "issue", "salesblink_status"])
        w.writeheader()
        w.writerows(review)

    groups = {}
    for url, (r, u) in updates.items():
        groups.setdefault(json.dumps(sorted(k for k in u)), []).append((r, u))
    cols = ["Status", "Tier", "Next action", "Next date", "Waiting on", "Chase step", "Claude note"]
    L = ["# Salesblink campaigns into Engagements", "",
         "You are working in Akshay's ThePodium Business OS. Chaandini moved guest outreach from manual mail to "
         "Salesblink. This file brings Engagements up to date with what Salesblink has sent, closes the manual "
         "chase she stopped, and adds the people Salesblink is mailing who are not in Notion yet.", "",
         f"Databases: Engagements {ENG_DB}, People {PEOPLE_DB}, Organisations {ORGS_DB}", "",
         "Do not delete anything, do not send email, do not change any row or property not named below.", "",
         f"## Part 1: update {len(updates)} Engagements", "",
         "Change only the properties in each row's table. An empty cell means clear that property; a dash means "
         "leave it as it is. Claude note is appended to the existing note, never replacing it.", "",
         "| Row | Name | " + " | ".join(cols) + " |", "|" + "---|" * (len(cols) + 2)]
    for url, (r, u) in sorted(updates.items(), key=lambda kv: kv[1][0]["Name"]):
        cells = [str(u[c]) if c in u else "-" for c in cols]
        cells = [x.replace("|", "/") for x in cells]
        L.append(f"| {url} | {r['Name']} | " + " | ".join(cells) + " |")
    from collections import Counter
    after = Counter()
    for url, (r, u) in updates.items():
        after[u.get("Status", r["Status"])] += 1
    nl = sorted(new.values(), key=lambda x: (x["show"], x["first_name"]))
    if nl:
        L += ["", f"## Part 2: add {len(nl)} people Salesblink is mailing", "",
              "For each row: look in People for this person by name and email. If found, use that row; if not, create "
              f"one (Name, Email, Title, Source system Salesblink, Migration batch {BATCH}). Find the Organisation by "
              "name, or create it. Then create one Engagement: Name \"Person @ Organisation, Show\", Guest = the "
              "People row, Organisation, Show, Host verdict Not asked, Tags Fortune 500 AI leader, "
              f"Migration batch {BATCH}, and the Status, Tier, Next action, Next date, Waiting on and Chase step "
              "in the table. Skip any person who already has an Engagement on that show, and report them.", "",
              "| Person | Email | Title | Organisation | Show | Status | Tier | Next action | Next date | "
              "Waiting on | Chase step |", "|" + "---|" * 11]
        for x in nl:
            tier = "Tier 1" if AI_HEAD.search(x.get("job_title") or "AI") else "Tier 1.5"
            personal = x["email"].split("@")[-1].lower() in FREE_MAIL
            delays = SEQS[x["seq"]][2]
            if x["mailed"]:
                st, na = "Contacted", f"Salesblink {x['seq']}: {x['sent']} of {len(delays) + 1} sent. No reply by this date: Unresponsive"
                nd = (dt.date.fromisoformat(x["created_date"][:10]) + dt.timedelta(days=sum(delays) + 7)).isoformat()
                wo, cs = "Guest or PR", x["sent"]
            else:
                st, na, nd, wo, cs = "New", f"Queued in Salesblink {x['seq']}: don't mail by hand" + (
                    "; swap the personal address for a work one" if personal else ""), "", "", ""
            L.append(f"| {x['first_name']} {x['last_name']} | {x['email']} | {(x.get('job_title') or '').replace('|', '/')} | "
                     f"{x['company_name']} | {SHOW_PAGE[x['show']]} | {st} | {tier} | {na} | {nd} | {wo} | {cs} |")
    L += ["", "## Check", "", f"Report how many rows you changed (expected {len(updates)}) and, among them, how many "
          "now have each Status. Expected:", "", "| Status | Rows |", "|---|---|"]
    L += [f"| {s} | {n} |" for s, n in sorted(after.items())]
    L += ["", "Report anything you could not complete."]
    (OUT / "notion_ai_salesblink_sync.md").write_text("\n".join(L) + "\n")

    print("updates", len(updates), dict(after))
    kinds = Counter()
    for url, (r, u) in updates.items():
        na = u.get("Next action", "")
        kinds[("queued" if na.startswith("Queued") else "salesblink" if na.startswith("Salesblink")
               else "bounce/new email" if na.startswith("Find") else "manual stopped" if na.startswith("Re-engage")
               else u.get("Status", "note"))] += 1
    print("kinds", dict(kinds))
    print("manual stopped", stopped, "manual 1-2 mails left as is", len(small))
    print("review rows", len(review), Counter(x["issue"].split(",")[0][:45] for x in review))


if __name__ == "__main__":
    main()
