"""Pipeline review: one chase / nurture / drop / ask-Akshay verdict per open guest row.

Two stages, because Gmail and Notion are only reachable through the session
connectors, while the reasoning is cheapest as one Message Batches request:

1. gather (in a Claude session with the Notion and Gmail connectors): Sonnet
   subagents read each Engagement row and its own mail thread(s) and write one
   JSON object per row to data/pipeline_review/gathered/<batch>.jsonl.
   Shape: see GATHERED_EXAMPLE below. No reasoning happens there.
2. reason (anywhere with ANTHROPIC_API_KEY): this script.

    python3 migration/pipeline_review.py build  data/pipeline_review/gathered/*.jsonl
    python3 migration/pipeline_review.py submit data/pipeline_review/requests.jsonl
    python3 migration/pipeline_review.py poll   <batch_id>
    python3 migration/pipeline_review.py collect <batch_id>

build is offline: it writes the request file and prints the row count, so the
run can be checked before anything is spent. collect writes
data/pipeline_review/results/<batch_id>.jsonl (one verdict per row) and
usage.json (input, cache read, cache write and output tokens, per row and total).

Re-runnable: build skips rows that already have a result unless --all is given.
Nothing is written to Notion or sent anywhere. The key is read from the
environment only; never commit it.
"""

import argparse
import glob
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "pipeline_review")
MODEL = "claude-sonnet-5-5"

GATHERED_EXAMPLE = {
    "id": "<Engagement page id>",
    "url": "<Engagement row URL>",
    "name": "Guest @ Company, Show",
    "show": "FT | un# | B2S | HBD",
    "status": "LT chase",
    "legacy353": False,
    "row": {"waiting_on": "", "next_action": "", "chase_step": 0, "next_date": "",
            "tier": "", "eval_verdict": "", "your_call": "", "claude_note": ""},
    "people": [{"name": "", "role": "guest | PR (agency) | EA | comms"}],
    "threads": [{"view_url": "", "subject": "",
                 "messages": [{"date": "YYYY-MM-DD", "from": "us | them",
                               "who": "first name (role)", "excerpt": "<= 800 chars"}]}],
}

SYSTEM = """You review one open guest Engagement for ThePodium, a podcast production agency run by Akshay Datt. Shows: Founder Thesis (FT), un# (host Sri), Built to Share (B2S, host Satish), Human by Design (HBD, host Arjun). Zoya is the AI team member who sends every routine follow-up; Akshay sends what needs the host (offers, decisions, negotiation).

You get the row's fields, the people on it (names and roles only) and excerpts of its own mail threads, newest last. Decide one recommendation:
- chase: a live, worthwhile lead and a follow-up is due now or soon.
- nurture: worth keeping, no ask due; a light check-in later (name the month).
- drop: no reply after the chase span, wrong fit per a decision or eval, contact dead, or they said no.
- ask Akshay: only he can decide (fit, price, a host's yes, a conflict between the row and the mail).

House rules that bound the recommendation:
- Akshay's own calls win. A "Your call" value or an "Akshay's call" line in the note is final; never recommend against it, flag the conflict instead.
- Sponsored price is fixed (FT INR 50,000 + GST). A lower-price ask gets The Spotlight Podcast offer; a counter below INR 30,000 or a custom package goes to Akshay.
- The 7-day rule counts per guest thread, and a PR person gets at most 2 mails a week. Loop-ins and incidental Cc don't count as mail.
- Three unanswered chases move a row to long-term chase; only sponsored-price declines are ever revived.
- A deferral ("after Diwali", "next quarter", "January") sets a hold date; nothing goes before it.
- Legacy FT long-term chase rows (legacy353 true) go to Akshay in one owner mail: for these, also say whether to still chase and how (direct mail, mail to PR, other), and give up to 4 dated lines of mail history.
- Built to Share rows on hold because Satish's approval was rescinded stay on hold: ask Akshay, never chase.

Evidence: use only the row and the excerpts. If a fact is not there, leave it out. Never output email addresses, phone numbers or handles; names and roles only. No em dashes.

Return JSON matching the schema. "line" is the whole verdict in one sentence a busy owner can act on, e.g. "Rishwin Devaya (FT, Sponsored offered): chase. Pranika (Provoqe PR) promised the brand's call by 9 Oct, nothing since; step 3 on 27 Oct via Pranika." "evidence" lists the row URL and the view_url of each thread you relied on."""

SCHEMA = {
    "type": "object",
    "properties": {
        "recommendation": {"type": "string", "enum": ["chase", "nurture", "drop", "ask Akshay"]},
        "line": {"type": "string"},
        "why": {"type": "string"},
        "last_exchange": {
            "type": "object",
            "properties": {"date": {"type": "string"}, "from": {"type": "string", "enum": ["us", "them", "none"]},
                           "who": {"type": "string"}, "summary": {"type": "string"}},
            "required": ["date", "from", "who", "summary"], "additionalProperties": False},
        "route": {"type": "string"},
        "guest_status": {"type": "string"},
        "row_conflict": {"type": "string"},
        "mail_history": {"type": "array", "items": {"type": "string"}},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
        "evidence": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["recommendation", "line", "why", "last_exchange", "route", "guest_status",
                 "row_conflict", "mail_history", "confidence", "evidence"],
    "additionalProperties": False,
}

EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE = re.compile(r"\+?\d[\d ()-]{8,}\d")


def scrub(text):
    return PHONE.sub("[phone]", EMAIL.sub("[email]", text or ""))


def load_jsonl(paths):
    rows = []
    for p in paths:
        with open(p) as f:
            rows += [json.loads(line) for line in f if line.strip()]
    return rows


def client():
    import anthropic  # imported here so build works without the SDK installed
    return anthropic.Anthropic()


def build(args):
    rows = load_jsonl([p for pat in args.files for p in glob.glob(pat)])
    done = set()
    if not args.all:
        for p in glob.glob(os.path.join(OUT, "results", "*.jsonl")):
            done |= {r["id"] for r in load_jsonl([p])}
    seen, reqs = set(), []
    for r in rows:
        if r["id"] in done or r["id"] in seen:
            continue
        seen.add(r["id"])
        user = scrub(json.dumps({k: v for k, v in r.items() if k != "id"}, ensure_ascii=False))
        reqs.append({
            "custom_id": r["id"].replace("-", "")[:64],
            "params": {
                "model": MODEL,
                "max_tokens": 4000,
                "system": [{"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}],
                "output_config": {"effort": args.effort,
                                  "format": {"type": "json_schema", "schema": SCHEMA}},
                "messages": [{"role": "user", "content": user}],
            },
        })
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "requests.jsonl")
    with open(path, "w") as f:
        f.writelines(json.dumps(q, ensure_ascii=False) + "\n" for q in reqs)
    with open(os.path.join(OUT, "id_map.json"), "w") as f:
        json.dump({r["id"].replace("-", "")[:64]: r for r in rows if r["id"] in seen}, f)
    print(f"gathered rows {len(rows)}, already done {len(done & {r['id'] for r in rows})}, "
          f"duplicates {len(rows) - len(seen) - len(done & {r['id'] for r in rows})}, requests {len(reqs)} -> {path}")


def submit(args):
    reqs = load_jsonl([args.requests])
    if not reqs:
        sys.exit("no requests")
    batch = client().messages.batches.create(requests=reqs)
    print(batch.id, batch.processing_status, len(reqs))


def poll(args):
    c = client()
    while True:
        b = c.messages.batches.retrieve(args.batch_id)
        print(b.processing_status, dict(b.request_counts))
        if b.processing_status == "ended" or not args.wait:
            return
        time.sleep(60)


def collect(args):
    id_map = json.load(open(os.path.join(OUT, "id_map.json")))
    os.makedirs(os.path.join(OUT, "results"), exist_ok=True)
    out = os.path.join(OUT, "results", f"{args.batch_id}.jsonl")
    usage, failed = {}, []
    with open(out, "w") as f:
        for res in client().messages.batches.results(args.batch_id):
            src = id_map.get(res.custom_id, {"id": res.custom_id})
            if res.result.type != "succeeded":
                failed.append({"id": src["id"], "type": res.result.type})
                continue
            msg = res.result.message
            if msg.stop_reason != "end_turn":
                failed.append({"id": src["id"], "type": msg.stop_reason})
                continue
            text = next(b.text for b in msg.content if b.type == "text")
            verdict = json.loads(text)
            u = msg.usage
            usage[src["id"]] = {"input": u.input_tokens, "cache_read": u.cache_read_input_tokens or 0,
                                "cache_write": u.cache_creation_input_tokens or 0, "output": u.output_tokens}
            row = {"id": src["id"], "name": src.get("name"), "show": src.get("show"),
                   "status": src.get("status"), "legacy353": src.get("legacy353", False), **verdict}
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    total = {k: sum(v[k] for v in usage.values()) for k in ("input", "cache_read", "cache_write", "output")}
    n = max(len(usage), 1)
    summary = {"batch_id": args.batch_id, "rows": len(usage), "failed": failed, "total": total,
               "per_row": {k: round(v / n) for k, v in total.items()}, "rows_usage": usage}
    json.dump(summary, open(os.path.join(OUT, f"usage_{args.batch_id}.json"), "w"), indent=1)
    print(f"ok {len(usage)}, failed {len(failed)} -> {out}")
    print("per row:", summary["per_row"])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build"); b.add_argument("files", nargs="+")
    b.add_argument("--all", action="store_true", help="include rows that already have a result")
    b.add_argument("--effort", default="medium", choices=["low", "medium", "high"])
    s = sub.add_parser("submit"); s.add_argument("requests")
    p = sub.add_parser("poll"); p.add_argument("batch_id"); p.add_argument("--wait", action="store_true")
    c = sub.add_parser("collect"); c.add_argument("batch_id")
    args = ap.parse_args()
    {"build": build, "submit": submit, "poll": poll, "collect": collect}[args.cmd](args)


if __name__ == "__main__":
    main()
