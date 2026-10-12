"""Build the Notion AI upload that starts the sponsored nurture (decision 158).

Reads the per-lead research files in data/review/sponsored_nurture_<date>/
(<page id>.json, written by read-only research agents) plus _plan.json
(dispositions, overrides and send dates), and writes Notion AI prompt files
that set each Engagement's next step and put the planned mail at the top of
the page body, where the daily sweep picks it up.

Usage: python migration/sponsored_nurture_notion_ai.py 2026-10-13
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ANGLE = {"0": "reply owed", "R": "restart, B2B influencer marketing and peers", "1": "soft bump",
         "2": "peers", "3": "audience seniority", "4": "due diligence story", "5": "founder news",
         "6": "premium audience", "7": "community deals story", "8": "search long tail",
         "9": "peers again", "10": "close the loop"}
KIND = {"REPLY": "commercials they asked for", "CALL": "call link they asked for",
        "GST": "GST details for the advance invoice"}


def fmt(d):
    from datetime import date
    return date.fromisoformat(d).strftime("%-d %b")


def section(p, r):
    step = p["step"]
    label = KIND.get(p.get("kind"), ANGLE.get(step, step))
    to = ", ".join(r.get("to_names") or []) or p.get("to", "")
    head = (f"## Next sponsored mail\nPlanned: {p['date']} · Step: {step} ({label}) · To: {to} · "
            f"Cc: everyone already on the thread · Thread: \"{r.get('thread_subject') or p.get('thread', '')}\""
            + (f" ({r['thread_id']}), reply to message {r['reply_to_message_id']}" if r.get("thread_id") else ""))
    return head + "\n\n```\n" + p["mail"].strip() + "\n```"


def row_block(i, p, r):
    pid = p["id"]
    url = f"https://app.notion.com/p/{pid}"
    out = [f"## {i}. {p['name']}", f"- Engagement: {url}"]
    d = p["disp"]
    if d == "NURTURE":
        step = p["step"]
        label = KIND.get(p.get("kind"), ANGLE.get(step, step))
        status = "Booking" if p.get("kind") == "GST" else "Sponsored offered"
        cs = 0 if step in ("R", "0") else int(step) - 1
        out += [f"- Status: {status}", "- Waiting on: Guest or PR (remove every other value)",
                f"- Next date: {p['date']}", f"- Chase step: {cs}",
                f"- Next action: Agent: sponsored step {step} ({label}) on {fmt(p['date'])}; mail planned in the page body",
                f"- Claude note line: {DATE}: sponsored nurture planned, step {step} on {fmt(p['date'])} (decision 158). {p['reason']}"]
        if p.get("kind") == "GST":
            out.append("- Payment: Not started")
        out += ["- Page body: insert this section at the very top:", "", "````", section(p, r), "````"]
    else:
        f = p["fields"]
        for k, v in f.items():
            out.append(f"- {k}: {v}")
        out.append(f"- Claude note line: {DATE}: sponsored review (decision 158): {p['reason']}")
    return "\n".join(out) + "\n"


def build(rows, part, parts):
    hdr = [f"# Sponsored nurture start ({DATE}), part {part} of {parts}", "",
           "You are updating the ThePodium Business OS. Engagements data source: "
           "collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5. "
           f"There are {len(rows)} rows below. Do every one, then report the count and list any you skipped.", "",
           "For each row, open the Engagement page at the URL and:",
           "1. Set every field listed for it, exactly as written. For Waiting on, replace the whole value. "
           "\"empty\" means clear the field.",
           "2. Add the Claude note line at the very top of Claude note, keeping every existing line below it.",
           "3. Set Claude updated to today.",
           "4. If the row has a page body section (between the ```` fences), insert it at the very top of the page body, "
           "above everything already there, keeping the inner ``` code block as a code block. If a section headed "
           "\"## Next sponsored mail\" already exists, replace it instead of adding a second.",
           "Do not change any other field. Do not create or delete rows. Do not send any mail.", ""]
    body = [row_block(i, p, R.get(p["id"], {})) for i, p in enumerate(rows, 1)]
    dest = ROOT / "data" / "review" / f"sponsored_nurture_{DATE}_notion_ai_part{part}.md"
    dest.write_text("\n".join(hdr) + "\n" + "\n".join(body), encoding="utf-8")
    print(f"part {part}: {len(rows)} rows -> {dest.relative_to(ROOT)}")


if __name__ == "__main__":
    DATE = sys.argv[1] if len(sys.argv) > 1 else "2026-10-13"
    src = ROOT / "data" / "review" / f"sponsored_nurture_{DATE}"
    R = {p.stem: json.loads(p.read_text()) for p in src.glob("*.json") if re.fullmatch(r"[0-9a-f]{32}", p.stem)}
    plan = json.loads((src / "_plan.json").read_text())
    bad = [p["name"] for p in plan if "—" in json.dumps(p, ensure_ascii=False) or re.search(r"\S+@\S+\.\w", p.get("mail") or "")]
    if bad:
        sys.exit(f"em dash or address in: {bad}")
    plan.sort(key=lambda p: (p["disp"] != "NURTURE", p.get("date") or "", p["name"]))
    half = (len(plan) + 1) // 2
    build(plan[:half], 1, 2)
    build(plan[half:], 2, 2)
