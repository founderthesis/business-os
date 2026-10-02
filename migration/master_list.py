"""Clean Founder_Thesis_Master_People_List into People and Organisation rows.

Usage: python migration/master_list.py data/raw/master_people_list.xlsx

Writes:
  data/out/master_people.json    one record per person, ready for Notion
  data/out/master_orgs.json      one record per organisation name
  data/review/master_review.csv  rows held back or flagged for a human

Never edits the raw file. Re-run safely.
"""
import json
import re
import sys
from pathlib import Path

import pandas as pd

BATCH = "master-list-2026-10-02"
ROLE_FIX = {"founder": "Founder", "co founder": "Co-founder", "co-founder": "Co-founder"}

# Rows the audit showed belong together (same person held twice). Keep the first, merge the second.
MERGE = {579: 205, 589: 583}  # Somdutta Singh, Sri Misra / Srikumar Misra


def clean_name(s):
    s = re.sub(r"https?://\S+", "", str(s)).strip()
    return re.sub(r"\s+", " ", s)


def clean_url(u):
    if pd.isna(u):
        return None
    u = str(u).strip().split("?")[0].rstrip("/")
    return u or None


def yes(v):
    return str(v).strip().lower() == "yes"


def main(path):
    root = Path(__file__).resolve().parent.parent
    out, review = root / "data/out", root / "data/review"
    out.mkdir(parents=True, exist_ok=True)
    review.mkdir(parents=True, exist_ok=True)

    df = pd.read_excel(path, sheet_name="Master List")
    print(f"read {len(df)} rows")

    flags = []
    df["LinkedIn"] = df["LinkedIn"].map(clean_url)

    # LinkedIn shared by two different people (not in MERGE) is a data error: blank it, flag both.
    merged_ids = set(MERGE) | set(MERGE.values())
    dup_li = df[df["LinkedIn"].notna() & df["LinkedIn"].duplicated(keep=False)]
    for li, grp in dup_li.groupby("LinkedIn"):
        if set(grp["#"]) <= merged_ids:
            continue
        for _, r in grp.iterrows():
            flags.append({"#": r["#"], "name": r["Name"], "issue": "Shares a LinkedIn URL with a different person; URL removed",
                          "action": "Add the right LinkedIn in Notion"})
        df.loc[grp.index, "LinkedIn"] = None

    # Human-checked corrections (data/fixes/linkedin.csv: row,linkedin,basis) override the blanking above.
    fixes_path = root / "data/fixes/linkedin.csv"
    if fixes_path.exists():
        fixes = pd.read_csv(fixes_path)
        for _, f in fixes.iterrows():
            df.loc[df["#"] == f["row"], "LinkedIn"] = f["linkedin"]
            flags = [x for x in flags if not (x["#"] == f["row"] and "LinkedIn" in x["issue"])]
        print(f"applied {len(fixes)} LinkedIn fixes")

    people = {}
    for _, r in df.iterrows():
        n = r["#"]
        if pd.isna(r["Name"]):
            flags.append({"#": n, "name": "", "issue": "No name (unidentified WhatsApp number)", "action": "Held back"})
            continue
        if n in MERGE:
            keep = people[MERGE[n]]
            keep["merged_from"].append(int(n))
            if not keep["Phone"] and pd.notna(r["Phone"]):
                keep["Phone"] = str(r["Phone"])
            flags.append({"#": n, "name": r["Name"], "issue": f"Same person as row {MERGE[n]}", "action": "Merged"})
            continue
        role = None if pd.isna(r["Role"]) else ROLE_FIX.get(str(r["Role"]).strip().lower(), str(r["Role"]).strip())
        url = r["LinkedIn"] if isinstance(r["LinkedIn"], str) else None
        li = url if url and "linkedin.com/in/" in url else None
        other_url = url if url and not li else None
        published = yes(r["Published?"])
        tags = ["Guest"] if published else []
        if role == "VC":
            tags.append("Investor")
        people[n] = {
            "source_row": int(n),
            "Name": clean_name(r["Name"]),
            "Company": None if pd.isna(r["Company"]) else str(r["Company"]).strip(),
            "Role": role,
            "What they do": None if pd.isna(r["Short Descriptor"]) else str(r["Short Descriptor"]).strip(),
            "LinkedIn": li,
            "Other profile": other_url,
            "Phone": None if pd.isna(r["Phone"]) else str(r["Phone"]).strip(),
            "In WhatsApp group": yes(r["In WhatsApp Group?"]),
            "FT guest": published,
            "Tags": tags,
            "Episode title": None if pd.isna(r["Episode Title"]) else str(r["Episode Title"]),
            "Episode link": None if pd.isna(r["Episode Link"]) else str(r["Episode Link"]),
            "Transcript link": None if pd.isna(r["Transcript Link"]) else str(r["Transcript Link"]),
            "In welcome doc": yes(r['Part of the "Welcome to the Founder Thesis Community!" doc?']),
            "merged_from": [],
        }

    recs = list(people.values())
    orgs = sorted({p["Company"] for p in recs if p["Company"]})
    json.dump(recs, open(out / "master_people.json", "w"), indent=1, ensure_ascii=False)
    json.dump([{"Name": o} for o in orgs], open(out / "master_orgs.json", "w"), indent=1, ensure_ascii=False)
    pd.DataFrame(flags).to_csv(review / "master_review.csv", index=False)

    held = sum(1 for f in flags if f["action"] == "Held back")
    merged = sum(1 for f in flags if f["action"] == "Merged")
    print(f"people {len(recs)} + merged {merged} + held back {held} = {len(recs) + merged + held} (raw {len(df)})")
    print(f"organisations {len(orgs)}; flagged rows {len(flags)}")
    print(f"FT guests {sum(p['FT guest'] for p in recs)}; in WhatsApp group {sum(p['In WhatsApp group'] for p in recs)}; "
          f"with LinkedIn {sum(bool(p['LinkedIn']) for p in recs)}; with phone {sum(bool(p['Phone']) for p in recs)}")
    assert len(recs) + merged + held == len(df), "row counts do not reconcile"


if __name__ == "__main__":
    main(sys.argv[1])
