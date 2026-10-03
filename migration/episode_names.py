"""Name every episode "Guest @ Company - Show" and merge re-uploads into one episode.

Usage: python migration/episode_names.py

Akshay, 3 Oct 2026:
  - An episode is named by who and which show, never by its title: "Pranav Pai @ 3one4 Capital - Founder Thesis".
    Titles change and differ between YouTube and Spotify, so they live in "YouTube title" / "Spotify title".
  - A guest recorded more than once gets V1, V2 in recording order. A recording split in parts keeps "Part N".
  - Episodes uploaded twice under the same title are one episode (all ten he was shown).
  - Beyond Campus was rebranded to Spotlight; FT episodes were republished on that feed as is. So a
    "Beyond Campus" video of a guest who has another episode is the same recording, published twice.

Reads data/out/episodes/{episodes_new,created}.json, data/out/blue_inflight_summary.json and the raw sources.
Writes data/out/episodes/renames.json (page, new name, YouTube title) and merges.json (keep, drop, what moves),
plus data/review/episode_names_review.csv for anything it could not decide. Re-run safely.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paas import name_key  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data/out/episodes"
SHOW_NAME = {"5776": "Founder Thesis", "afe1": "alpha un#", "d025": "Built to Share", "ab23": "Human by Design"}

# Rows already marked for deletion by hand on 3 Oct (CleverTap card, two Shorts, Arvind's second upload)
ALREADY_DELETED = {"3ed19a301a7f81a38cd8c5f48106821c", "3ed19a301a7f81c7b60ffa3b4807a134",
                   "3ed19a301a7f81b9b00ddc1677eb08d9", "3ed19a301a7f81a2a41bedec5c724b0b",
                   "3ed19a301a7f81c8851ed91407ff33ea"}  # Saurabh Garg B2S practice recording (Akshay)


# Inventory rows whose guest field was empty, resolved from the matching Blue inventory card (3 Oct)
GUEST_FIX = {"3ed19a301a7f81f6a24cdc836860e2a1": ("Vikrant Singh", "BatX Energies"),
             "3ed19a301a7f81eea284db08ac4ac18a": ("Aditya Tulsian", "Numberz")}


# Akshay's answers on repeat guests (3 Oct): these drops are the same recording as the keep
SAME_RECORDING = {
    "3ed19a301a7f812b98afc3f3373d56e4": ["3ed19a301a7f81bb98d9d12d66391842"],  # Ankit Mehrotra, Dineout
    "3ed19a301a7f813195fdc08fdd614dda": ["3ed19a301a7f8109b514e83626dba424"],  # Nakul Kumar, Cashify
    "3ed19a301a7f81bba588e11132ee5a29": ["3ed19a301a7f815aa8ccc97b32899308"],  # Preksha Kaparwan, Alphaa AI
    "3ed19a301a7f816085c9f768c3d4d44b": ["3ed19a301a7f8160b7bcf310ea09caad"],  # Bharat Sethi, Rage Coffee
    "3ed19a301a7f817283d7fbb99f4b5d0c": ["3ed19a301a7f81c19ef6d310433fe2ee", "3ed19a301a7f8174acfbfc8578c39792"],  # Hitesh
    "3ed19a301a7f8185adeffb1931befb24": ["3ed19a301a7f813bb72ec6ba095954f3"],  # Bhavik Vasa, GetVantage
}
# Not episodes: three Roshan Abbas Spotlight clips (Akshay: "ignore those clips")
NOT_EPISODES = {"3ed19a301a7f812d98b7d245952d3659", "3ed19a301a7f81089822cb980fd9fb9f", "3ed19a301a7f8183bebfdd00ac4eda7e"}
# Second recordings confirmed (V1/V2 stays): Amit Gupta (Yulu), Ankit Mehta (ideaForge), Ashish Munjal (Sunstone),
# Anand Jain (CleverTap). Vijesh Sharma's two Spotlight masterclasses are left as they are.


def show_of(url):
    return SHOW_NAME[url[-4:]]


def split_title(t):
    """Old titles look like 'Theme | Guest @ Company' or 'Episode 52 | Theme | Guest @ Company'."""
    num = re.search(r"\b(?:Episode|Ep)\.?\s*(\d+)", t, re.I)
    part = re.search(r"\bPart\s*(\d+)", t, re.I)
    theme = [p.strip() for p in t.split("|") if p.strip() and not re.match(r"(?i)^(episode|ep)\.?\s*\d+", p.strip())]
    return (int(num.group(1)) if num else None, int(part.group(1)) if part else None,
            re.sub(r"[^a-z0-9]", "", re.sub(r"(?i)\bpart\s*\d+", "", theme[0]).lower()) if theme else "")


def main():
    eps = json.load(open(OUT / "episodes_new.json"))
    created = json.load(open(OUT / "created.json"))
    ei = {f"ei:{r['id']}": r for r in json.load(open(ROOT / "data/raw/notion/episode_inventory.json"))}
    aq = {f"aq:{r['id']}": r for r in json.load(open(ROOT / "data/raw/notion/article_queue.json"))}
    blue = {f"blue:{r['original_id']}": r for r in json.load(open(ROOT / "data/raw/blue/records.json"))}
    inflight = json.load(open(ROOT / "data/out/blue_inflight_summary.json"))["records"]
    review = []

    rows = []
    for e in eps:
        page = created.get(e["key"])
        if not page or page in ALREADY_DELETED or page in NOT_EPISODES:
            continue
        old = e["props"]["Title"]
        src = ei.get(e["key"]) or aq.get(e["key"])
        if src:
            guest, company = (src.get("Guest") or "").strip(), (src.get("Company") or "").strip()
        else:
            b = blue[e["key"]]
            cf = b["custom_fields"]
            guest = (cf.get("Guest Name") or b["title"].split("@")[0]).strip()
            company = old.split("@", 1)[1].strip() if "@" in old else (cf.get("Co Name") or cf.get("Company Name") or "")
        guest, company = GUEST_FIX.get(page, (guest, company))
        guest = re.sub(r"\s+and\s+", " & ", re.sub(r"^(Mr|Mrs|Ms|Dr|Prof)\.?\s+", "", guest)).strip()
        if not guest:
            review.append({"page": page, "old": old, "issue": "no guest name; kept the old title"})
        num, part, theme = split_title(old)
        rows.append({"page": page, "key": e["key"], "old": old, "guest": guest, "company": company.strip(),
                     "show": show_of(e["show"]), "num": num, "part": part, "theme": theme,
                     "views": e["props"].get("YouTube views") or 0, "yt": e["props"].get("YouTube"),
                     "rec": e["props"].get("date:Recording date:start"),
                     "beyond": bool(re.match(r"(?i)beyond campus", old)),
                     "tags": json.loads(e["props"].get("Tags") or "[]")})
    for r in inflight:
        guest, _, company = r["title"].partition("@")
        rows.append({"page": r["notion_episode_url"].split("/")[-1].split("?")[0], "key": f"inflight:{r['blue_id']}",
                     "old": r["title"], "guest": guest.strip(), "company": company.strip(), "show": "Founder Thesis",
                     "num": None, "part": None, "theme": "", "views": 0, "yt": None, "rec": r.get("recording_date"),
                     "beyond": False, "tags": []})

    # A row with no company borrows the company the same guest has on their other episodes
    companies = defaultdict(list)
    for r in rows:
        if r["company"]:
            companies[name_key(r["guest"])].append(r["company"])
    for r in rows:
        if not r["company"] and companies.get(name_key(r["guest"])):
            r["company"] = max(set(companies[name_key(r["guest"])]), key=companies[name_key(r["guest"])].count)

    # Merges: same guest and show, and either the same theme title or one of them is a Beyond Campus republish
    merges, dropped = [], set()
    by_guest = defaultdict(list)
    for r in rows:
        by_guest[(name_key(r["guest"]), r["show"])].append(r)
    for (g, show), group in by_guest.items():
        if len(group) < 2 or not g:
            continue
        clusters = []
        for r in sorted(group, key=lambda x: -x["views"]):
            home = next((c for c in clusters if (r["theme"] and r["theme"] == c[0]["theme"] and r["part"] == c[0]["part"])), None)
            (home.append(r) if home else clusters.append([r]))
        # a Beyond Campus video folds into the guest's other recording when there is exactly one
        bc = [c for c in clusters if all(x["beyond"] for x in c)]
        others = [c for c in clusters if not all(x["beyond"] for x in c)]
        for c in bc:
            if len(others) == 1:
                others[0].extend(c)
            else:
                others.append(c)
                if others[:-1]:
                    review.append({"page": c[0]["page"], "old": c[0]["old"],
                                   "issue": "Beyond Campus video; guest has several other episodes, left separate"})
        for c in others:
            if len(c) > 1:
                keep = max(c, key=lambda x: (not x["beyond"], x["views"]))
                drops = [x for x in c if x is not keep]
                merges.append({"keep": keep["page"], "drop": [x["page"] for x in drops],
                               "drop_youtube": [x["yt"] for x in drops if x["yt"]],
                               "drop_titles": [x["old"] for x in drops],
                               "drop_views": [x["views"] for x in drops]})
                dropped.update(x["page"] for x in drops)

    for keep, drops in SAME_RECORDING.items():
        merges.append({"keep": keep, "drop": drops, "drop_youtube": [], "drop_titles": [], "drop_views": []})
        dropped.update(drops)

    # Names, with V1/V2 for genuine repeat recordings and Part N for split recordings
    live = [r for r in rows if r["page"] not in dropped]
    base = defaultdict(list)
    for r in live:
        r["base"] = f"{r['guest']} @ {r['company']} - {r['show']}" if r["company"] else f"{r['guest']} - {r['show']}"
        base[(r["base"], r["part"])].append(r)
    renames = []
    for (b, part), group in base.items():
        group.sort(key=lambda x: (x["num"] is None, x["num"] or 0, x["rec"] or "9999"))
        for i, r in enumerate(group, 1):
            name = b + (f" - V{i}" if len(group) > 1 else "") + (f" - Part {part}" if part else "")
            renames.append({"page": r["page"], "name": name if r["guest"] else r["old"],
                            # only inventory and Article Queue titles are real published titles
                            "youtube_title": r["old"] if r["key"][:3] in ("ei:", "aq:") else None})
        if len(group) > 1:
            review.append({"page": group[0]["page"], "old": " / ".join(x["old"] for x in group),
                           "issue": f"{len(group)} recordings named V1..V{len(group)}; order by episode number then date"})
    for m in merges:
        keep_name = next(x["name"] for x in renames if x["page"] == m["keep"])
        m["drop_name"] = f"DELETE: same recording as {keep_name}"

    OUT.mkdir(parents=True, exist_ok=True)
    json.dump(renames, open(OUT / "renames.json", "w"), indent=1, ensure_ascii=False)
    json.dump(merges, open(OUT / "merges.json", "w"), indent=1, ensure_ascii=False)
    pd.DataFrame(review).to_csv(ROOT / "data/review/episode_names_review.csv", index=False)
    print(f"episodes {len(rows)}; renamed {len(renames)}; merged groups {len(merges)} dropping {len(dropped)} rows")
    print(f"versioned names {sum(1 for r in renames if ' - V' in r['name'])}; review rows {len(review)}")
    assert len(renames) + len(dropped) == len(rows), "counts do not reconcile"
    print("still versioned:", sorted({r["name"].rsplit(" - V", 1)[0] for r in renames if " - V" in r["name"]}))


if __name__ == "__main__":
    sys.exit(main())
