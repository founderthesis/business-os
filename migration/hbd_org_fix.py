"""Clean the Organisation names the HBD load (batch hbd-pipeline-2026-10-10) took from the sheet's affiliation column.

Usage:
  python migration/hbd_org_fix.py

Some names were affiliations ("CMU / Bosch Research", "UCLA (emeritus)", "Visiting, Stanford Digital Economy Lab") and some
places came in twice. Each messy row is renamed to the real organisation; a row that duplicates another (from this batch or
already in Organisations) has its links moved to the row kept and is renamed "DELETE: duplicate of ..." for a human to delete
(the connector cannot delete rows). Writes data/out/hbd_pipeline/notion_ai_hbd_org_fix.md. Reads the 10 Oct Organisations
export, which predates the HBD load, to find rows that already existed.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data/out/hbd_pipeline"
ORGS_DB = "https://app.notion.com/p/4e484b1c510b42ce9ea979307bff31e4"
PEOPLE_DB = "https://app.notion.com/p/f54094b86c3549dead74c0034afad86c"
ENGS_DB = "https://app.notion.com/p/5e77c373909a4bf6b9195570de46c63b"

# HBD org key -> clean name (research: each person's current main affiliation)
RENAME = {
    "041": "MIT Media Lab", "043": "Inkbit", "044": "Georgia Tech", "052": "University of British Columbia",
    "054": "Weizmann Institute of Science", "055": "LMU Munich", "056": "Carnegie Mellon University", "057": "CUHK",
    "060": "National University of Singapore", "063": "Mila", "064": "UC San Diego", "068": "Purdue University",
    "072": "UCL", "076": "Rutgers University", "078": "NYU", "081": "Udacity", "087": "Michigan State University",
    "089": "Princeton University", "090": "Johns Hopkins University", "097": "Strategy Robot", "098": "Mobileye",
    "101": "UCLA", "105": "University of Tokyo", "107": "Ai2", "108": "Arizona State University", "110": "Vercept",
    "111": "Cornell University", "112": "UMass Amherst",
}
# spare HBD org key -> HBD org key kept (same place)
MERGE = {
    "047": "044", "070": "056", "084": "056", "102": "056", "104": "056",   # Georgia Tech; CMU (Veloso, Mitchell are CMU)
    "059": "075", "062": "006", "066": "060", "080": "028", "092": "031",
    "094": "028", "095": "028",                                             # Leskovec, Manning: Stanford faculty
    "109": "089",
}


def main():
    orgs = json.load(open(OUT / "candidates.json"))["orgs"]
    name = {o["key"][-3:]: o["name"] for o in orgs.values()}
    existing = {}
    for line in json.load(open(ROOT / "data/raw/hbd/notion_orgs_2026-10-10.json")):
        oid, nm = line.split("|")[:2]
        existing.setdefault(nm.strip().lower(), oid)
    final = {k: RENAME.get(k, name[k]) for k in name}
    renames, merges = [], []
    for k, keep in MERGE.items():
        target = existing.get(final[keep].lower())   # the kept place may itself predate this batch
        ref = f"https://app.notion.com/p/{target}" if target else f"Organisations row with Source ID \"HBD org {keep}\""
        merges.append((k, ref, final[keep]))
    for k, new in RENAME.items():
        if new.lower() in existing:     # the place already had a row before this batch: fold into it
            merges.append((k, f"https://app.notion.com/p/{existing[new.lower()]}", new))
        else:
            renames.append((k, name[k], new))
    for k in ("006", "028", "031", "075"):  # keep rows not renamed, but they may still duplicate an older row
        if name[k].lower() in existing:
            merges.append((k, f"https://app.notion.com/p/{existing[name[k].lower()]}", name[k]))
    L = ["# Human by Design: clean up Organisation names", "",
         "You are working in Akshay's ThePodium Business OS. Yesterday's HBD load (Migration batch hbd-pipeline-2026-10-10) created some "
         "Organisations whose names are affiliations, not organisations, and some places twice. This file fixes them.", "",
         f"- Organisations: {ORGS_DB}", f"- People: {PEOPLE_DB}", f"- Engagements: {ENGS_DB}", "",
         "Only touch the rows named below (find each by its Source ID). Do not send email. Do not delete anything.", "",
         f"## Part 1: rename ({len(renames)} rows)", "", "| Source ID | Current name | New name |", "|---|---|---|"]
    L += [f"| HBD org {k} | {old} | {new} |" for k, old, new in renames]
    L += ["", f"## Part 2: fold duplicates into one row ({len(merges)} rows)", "",
          "Do Part 1 first. For each line: every People row whose Organisation is the duplicate gets the row to keep instead, and every "
          "Engagements row whose Organisation is the duplicate gets the row to keep instead. Then rename the duplicate to "
          "\"DELETE: duplicate of <name of the row to keep>\" for a human to delete.", "",
          "| Duplicate (Source ID) | Current name | Row to keep | Its name |", "|---|---|---|---|"]
    L += [f"| HBD org {k} | {name[k]} | {ref} | {kn} |" for k, ref, kn in merges]
    L += ["", "## Check", "", f"Report: rows renamed in Part 1 (expected {len(renames)}), duplicates folded in Part 2 (expected {len(merges)}), "
          "and the number of People and Engagements rows whose Organisation you changed. After this, no People or Engagements row should "
          "link to an Organisation named \"DELETE: ...\".", "", "Report anything you could not complete."]
    (OUT / "notion_ai_hbd_org_fix.md").write_text("\n".join(L) + "\n")
    print(f"renames {len(renames)}, merges {len(merges)}")
    for m in merges:
        print("merge", m[0], name[m[0]], "->", m[2], "(existing row)" if m[1].startswith("http") else "")


if __name__ == "__main__":
    main()
