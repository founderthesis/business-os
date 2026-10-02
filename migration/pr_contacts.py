"""Turn the PR / comms emails on Blue guest-form records into People rows.

Usage: python migration/pr_contacts.py

Reads:
  data/raw/blue/records.json          full Blue extraction
  data/out/blue_inflight_summary.json which Blue records are already Episodes in Notion
Writes:
  data/out/pr_contacts.json           one record per distinct address, with guessed name, org and the guests it serves
  data/review/pr_contacts_review.csv  guesses a human should glance at (single-token names, shared inboxes)

Blue keeps PR contacts as bare addresses. The name is guessed from the address and tagged
"Name guessed" so the enrichment routine (or a person) can correct it from a signature later.
Role inboxes (pr@, media@) become one row per inbox, tagged "Role inbox", because they still
have to be copied on guest emails. Never edits the raw file. Re-run safely.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
BATCH = "blue-pr-contacts-2026-10-02"

EMAIL = re.compile(r"[A-Za-z0-9._%+'-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
FREE_MAIL = {"gmail.com", "googlemail.com", "yahoo.com", "yahoo.co.in", "outlook.com", "hotmail.com",
             "live.com", "icloud.com", "me.com", "rediffmail.com", "protonmail.com", "proton.me", "aol.com"}
ROLE_WORDS = {"pr", "press", "media", "comms", "communications", "communication", "marketing", "info", "hello",
              "contact", "team", "admin", "support", "office", "ea", "assistant", "partnerships", "brand",
              "social", "news", "corpcomm", "corporatecommunications", "publicrelations", "events", "hr",
              "careers", "founders", "founder", "ceo", "invest", "investors", "ir", "sales", "mediarelations"}


def norm(s):
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def domain_stem(domain):
    parts = domain.lower().split(".")
    # drop common second-level suffixes: co.in, com.sg, co.uk
    while len(parts) > 2 and parts[-2] in {"co", "com", "org", "net", "ac", "gov"}:
        parts = parts[:-2] + [parts[-1]]
    return parts[-2] if len(parts) >= 2 else parts[0]


def guess_name(local):
    """Return (name, confidence, is_role). Confidence: high (two tokens), low (one token or initials)."""
    base = re.sub(r"\+.*$", "", local.lower())
    tokens = [t for t in re.split(r"[._-]+", base) if t]
    tokens = [re.sub(r"\d+", "", t) for t in tokens]
    tokens = [t for t in tokens if t]
    if not tokens or norm(base) in ROLE_WORDS or tokens[0] in ROLE_WORDS:
        return None, None, True
    if len(tokens) >= 2:
        # "p.sharma" -> "P Sharma"; "priya.sharma" -> "Priya Sharma"
        name = " ".join(t.capitalize() if len(t) > 1 else t.upper() for t in tokens[:3])
        return name, "high" if all(len(t) > 1 for t in tokens[:2]) else "low", False
    return tokens[0].capitalize(), "low", False


def pr_emails(rec):
    """Every address in a PR / comms field (FT guest form) or an "Other Email IDs" field (alpha un#, Hissa, FastCode).
    Field names differ a little by workspace."""
    out = []
    for k, v in (rec.get("fields") or rec.get("custom_fields") or {}).items():
        if v and re.search(r"\b(pr|comms?|communications?)\b|^other email id", k, re.I):
            out += EMAIL.findall(str(v))
    return [e.strip(".").lower() for e in out]


def main():
    records = json.load(open(ROOT / "data/raw/blue/records.json"))
    inflight = json.load(open(ROOT / "data/out/blue_inflight_summary.json"))["records"]
    in_notion = {r["blue_id"]: r for r in inflight if r.get("notion_episode_url")}

    contacts = defaultdict(lambda: {"records": [], "guests": []})
    seen_records = 0
    for rec in records:
        emails = pr_emails(rec)
        if not emails:
            continue
        seen_records += 1
        for e in dict.fromkeys(emails):
            c = contacts[e]
            c["records"].append(rec["original_id"])
            c["guests"].append(rec.get("title"))

    rows, review = [], []
    for e, c in sorted(contacts.items()):
        local, domain = e.split("@", 1)
        name, conf, role = guess_name(local)
        free = domain in FREE_MAIL
        org = None if free else domain_stem(domain)
        if role:
            name = f"{org.capitalize() if org else 'Unknown'} {local} inbox"
        tags = ["PR contact"] + (["Role inbox"] if role else ["Name guessed"])
        row = {"email": e, "name": name, "confidence": conf, "role_inbox": role, "org_stem": org,
               "domain": None if free else domain, "tags": tags,
               "blue_records": c["records"], "guests": c["guests"],
               "in_notion_now": [in_notion[r]["notion_episode_url"] for r in c["records"] if r in in_notion]}
        rows.append(row)
        if conf == "low" or role or len(set(c["guests"])) > 1:
            review.append({"email": e, "guessed_name": name, "why": "role inbox" if role else
                           ("one-token name" if conf == "low" else "serves several guests"),
                           "guests": "; ".join(sorted(set(filter(None, c["guests"]))))})

    out = ROOT / "data/out"
    (ROOT / "data/review").mkdir(parents=True, exist_ok=True)
    json.dump(rows, open(out / "pr_contacts.json", "w"), indent=1, ensure_ascii=False)
    pd.DataFrame(review).to_csv(ROOT / "data/review/pr_contacts_review.csv", index=False)
    print(f"Blue records {len(records)}; with PR emails {seen_records}; distinct addresses {len(rows)}")
    print(f"named high {sum(r['confidence'] == 'high' for r in rows)}, low {sum(r['confidence'] == 'low' for r in rows)}, "
          f"role inboxes {sum(r['role_inbox'] for r in rows)}; tied to in-flight episodes {sum(bool(r['in_notion_now']) for r in rows)}")
    print(f"review rows {len(review)}")


if __name__ == "__main__":
    sys.exit(main())
