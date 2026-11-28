"""Build Notion page payloads for master-list people once Organisation page URLs are known.

Usage: python migration/build_people_batches.py data/out/org_urls.json
org_urls.json maps organisation name -> Notion page URL.
"""
import json, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
people = json.load(open(root / "data/out/master_people.json"))
org_urls = json.load(open(sys.argv[1]))
B = "master-list-2026-10-02"
out = root / "data/out/batches"
missing = 0
pages = []
for p in people:
    props = {"Name": p["Name"], "Source": "Migration", "Source ID": f"Master People List row {p['source_row']}",
             "date:Captured:start": "2026-10-02", "Migration batch": B, "Match status": "Clean",
             "FT guest": "__YES__" if p["FT guest"] else "__NO__",
             "In WhatsApp group": "__YES__" if p["In WhatsApp group"] else "__NO__"}
    for k in ["Role", "What they do", "LinkedIn", "Phone"]:
        if p[k]:
            props[k] = p[k]
    if p["Tags"]:
        props["Tags"] = json.dumps(p["Tags"])
    if p["Company"]:
        if p["Company"] in org_urls:
            props["Organisation"] = json.dumps([org_urls[p["Company"]]])
        else:
            missing += 1
    lines = []
    if p["Episode link"]:
        lines.append(f"FT episode: [{p['Episode title'] or 'Episode'}]({p['Episode link']})")
    if p["Transcript link"]:
        lines.append(f"Transcript: {p['Transcript link']}")
    if p["Other profile"]:
        lines.append(f"Profile: {p['Other profile']}")
    if p["In welcome doc"]:
        lines.append("Listed in the Founder Thesis community welcome doc.")
    content = "## Research\n\n" + "\n\n".join(lines) if lines else "## Research\n"
    pages.append({"properties": props, "content": content})
for i in range(0, len(pages), 100):
    json.dump(pages[i:i + 100], open(out / f"people_{i // 100 + 1:02d}.json", "w"), ensure_ascii=False)
print(f"{len(pages)} people in {(len(pages) + 99) // 100} batches; organisation not found for {missing}")
