"""Build the Notion AI upload for the FT eval refresh.

Reads the per-guest eval files the research agents wrote to
data/review/ft_evals_<date>/*.md and writes one prompt file Notion AI can run
in a single pass: Eval verdict, a dated Claude note line, Claude updated,
Latest eval verdict on the guest's People row, and an "## Eval (<date>)"
section at the top of each Engagement page.

Usage: python migration/ft_eval_refresh_notion_ai.py 2026-10-10
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERDICTS = {"Book immediately", "Strong consider", "Pre-call needed", "Decline", "Sponsored track"}
# People "Latest eval verdict" has no Sponsored track option
PEOPLE_VERDICT = {"Sponsored track": "Decline"}
HEADER_KEYS = ["Engagement", "Status", "Old verdict", "New verdict", "Route",
               "Audience Fit", "Sales Fit", "Flag"]


def parse(path):
    text = path.read_text(encoding="utf-8")
    head, sep, body = text.partition("\n## Eval (")
    if not sep:
        raise ValueError(f"{path.name}: no '## Eval (' section")
    row = {"file": path.name, "title": head.splitlines()[0].lstrip("# ").strip()}
    for key in HEADER_KEYS:
        m = re.search(rf"^{re.escape(key)}:\s*(.+)$", head, re.M)
        row[key] = m.group(1).strip() if m else ""
    row["section"] = "## Eval (" + body.strip()
    problems = []
    if row["New verdict"] not in VERDICTS:
        problems.append(f"verdict '{row['New verdict']}'")
    if not row["Engagement"].startswith("https://app.notion.com/"):
        problems.append("engagement url")
    if "—" in text:
        problems.append("em dash")
    row["problems"] = problems
    return row


def build(date, rows, part, parts, extras):
    out = [
        f"# FT eval refresh ({date}), part {part} of {parts}: apply to Engagements",
        "",
        "You are updating the ThePodium Business OS. Engagements data source: "
        "collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5. People data source: "
        "collection://e6c44319-7f81-4da6-8b80-8441a4875d7a. "
        f"There are {len(rows)} rows below. Do every one, then report the count.",
        "",
        "For each row below, on the Engagement page at the URL given:",
        "1. Set Eval verdict to the New verdict.",
        f"2. Add one line at the very top of Claude note, keeping every existing line below it: "
        f"\"{date}: eval refreshed, <Old verdict> -> <New verdict>\". If the row has a Flag, "
        "append \". Flag: <flag text>\" to that line.",
        "3. Set Claude updated to today (the day you run this).",
        f"4. Insert the eval section (the text between the ``` fences, starting with \"## Eval ({date})\") "
        "at the top of the page body, above everything already there. Keep the existing body. "
        "If an \"## Eval\" section with the same date already exists, replace it instead of adding a second.",
        "5. On the People row linked in the Engagement's Guest relation, set Latest eval verdict to the "
        "People verdict given.",
        "6. If Eval link holds a link, clear it and add \" (old eval: <that link>)\" to the end of the Claude note line "
        "from step 2. The new eval lives in the page body; a later Claude session publishes it as a claude.ai page "
        "and sets Eval link again (decision 141).",
        "",
        "Do not change Status, Tier, Next date, Next action, Waiting on, Eval link, Chase step or any "
        "other field" + (", except where the \"Status fixes\" section at the end names a field for a row"
                         if extras else "") + ". "
        "Do not create or delete any row. If a URL does not open, skip it and list it at the end.",
        "",
    ]
    for i, r in enumerate(rows, 1):
        old = r["Old verdict"] or "none"
        people = PEOPLE_VERDICT.get(r["New verdict"], r["New verdict"])
        out += [
            f"## {i}. {r['title']}",
            f"- Engagement: {r['Engagement']}",
            f"- Old verdict: {old}",
            f"- New verdict: {r['New verdict']}",
            f"- People verdict: {people}",
            f"- Flag: {r['Flag'] or 'none'}",
            "",
            "```",
            r["section"],
            "```",
            "",
        ]
    if extras:
        out += [extras, ""]
    dest = ROOT / "data" / "review" / f"ft_eval_refresh_{date}_notion_ai_part{part}.md"
    dest.write_text("\n".join(out), encoding="utf-8")
    print(f"part {part}: {len(rows)} evals -> {dest.relative_to(ROOT)}")


def main(date, size=31):
    src = ROOT / "data" / "review" / f"ft_evals_{date}"
    rows = [parse(p) for p in sorted(src.glob("[A-Z]-*.md"))]
    # Live check against Notion just before upload: drop rows closed since, or re-evaluated by another chat
    lives = sorted(src.glob("_live_*.json"))
    if lives:
        skip = json.loads(lives[-1].read_text(encoding="utf-8"))["skip"]
        for r in rows:
            pid = re.search(r"([0-9a-f]{32})", r["Engagement"]).group(1)
            if pid in skip:
                print(f"SKIP {r['title']}: {skip[pid]}")
        rows = [r for r in rows if re.search(r"([0-9a-f]{32})", r["Engagement"]).group(1) not in skip]
    bad = [r for r in rows if r["problems"]]
    for r in bad:
        print(f"PROBLEM {r['file']}: {', '.join(r['problems'])}")
    if bad:
        sys.exit(1)
    # Two uploads keep each Notion AI prompt near 100 KB; hand-checked status fixes ride part 1
    fixes = src / "_status_fixes.md"
    extras = fixes.read_text(encoding="utf-8").strip() if fixes.exists() else ""
    chunks = [rows[i:i + size] for i in range(0, len(rows), size)]
    for n, chunk in enumerate(chunks, 1):
        build(date, chunk, n, len(chunks), extras if n == 1 else "")

    moves = Counter((r["Old verdict"] or "none", r["New verdict"]) for r in rows)
    print(f"{len(rows)} evals in {len(chunks)} parts")
    print("New verdicts:", dict(Counter(r["New verdict"] for r in rows)))
    for (old, new), n in sorted(moves.items()):
        print(f"  {old} -> {new}: {n}")
    for r in rows:
        if r["Flag"] and r["Flag"].lower() != "none":
            print(f"FLAG {r['title']}: {r['Flag']}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "2026-10-10")
