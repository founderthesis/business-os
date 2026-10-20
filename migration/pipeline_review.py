"""Pipeline review: one recommendation per open Engagement, on the Anthropic API credits (decision 358).

Read-only. Input is gathered by the API worker session (Notion row + Gmail excerpts) into
data/pipeline_review/input.jsonl, one JSON object per line:
  {"id": "<engagement page id>", "name": "...", "row": "<status, tier, show, next action, dates>",
   "threads": "<last exchanges, oldest first, with dates and senders>"}

  python3 -I migration/pipeline_review.py            # pilot: one Messages call per row
  python3 -I migration/pipeline_review.py --batch    # full run: one Message Batches request
  python3 -I migration/pipeline_review.py --collect <batch_id>

Output: data/pipeline_review/output.jsonl, plus token totals printed at the end.
The key is read from PODIUM_API_KEY and never printed or written.
"""
import json
import os
import sys
import time
import urllib.request

API = "https://api.anthropic.com/v1"
MODEL = "claude-sonnet-5-5"
DIR = "data/pipeline_review"

SYSTEM = """You review one open guest or sponsor conversation for ThePodium, a podcast agency run by Akshay Datt.
Shows: Founder Thesis (FT), un#, Built to Share (B2S), Human by Design (HBD). Zoya is the AI team member who sends routine follow-ups.
Recommend exactly one action:
- chase: a live conversation where it's our move or a reply is overdue; Zoya follows up.
- nurture: no near-term deal but worth keeping warm; a slow, dated touch.
- drop: closed in substance (clear decline, gone silent after the full sequence and no Tier 1 or sponsored value, wrong fit).
- ask_akshay: needs his judgement (Tier 1, sponsored price, a guest decision, a relationship only he holds).
Rules: respect explicit declines and anyone who asked us to stop. Revive a decline only if the no was to the sponsored price (decision 355). Silence alone never ends a Tier 1, sponsored or approved pursuit; move it to nurture (decision 335). A drop of a Tier 1 or sponsored lead is always ask_akshay. Use only the facts given; if the evidence is missing say so and choose ask_akshay.
Reply with JSON only:
{"action": "chase|nurture|drop|ask_akshay", "reason": "<one sentence>", "last_exchange": "<date, who, what>",
 "best_route": "<direct mail | via PR <name> | WhatsApp | other>", "current_status": "<one line>",
 "next_step": "<one line, what Zoya or Akshay does>"}"""


def key():
    k = os.environ.get("PODIUM_API_KEY")
    if not k:
        sys.exit("PODIUM_API_KEY is not set")
    return k


def call(path, body=None, method="POST"):
    req = urllib.request.Request(API + path, method=method, data=None if body is None else json.dumps(body).encode())
    req.add_header("x-api-key", key())
    req.add_header("anthropic-version", "2023-06-01")
    req.add_header("content-type", "application/json")
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())


def params(row):
    return {
        "model": MODEL,
        "max_tokens": 400,
        "system": [{"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}],
        "messages": [{"role": "user", "content": f"Engagement: {row['name']}\n\nRow:\n{row['row']}\n\nThreads:\n{row['threads']}"}],
    }


def parse(msg):
    text = "".join(b.get("text", "") for b in msg.get("content", []))
    try:
        return json.loads(text[text.find("{"):text.rfind("}") + 1])
    except ValueError:
        return {"action": "ask_akshay", "reason": "unparseable model output", "raw": text}


def add(tot, usage):
    for k in ("input_tokens", "output_tokens", "cache_read_input_tokens", "cache_creation_input_tokens"):
        tot[k] = tot.get(k, 0) + (usage.get(k) or 0)


def write(results, tot, n):
    with open(f"{DIR}/output.jsonl", "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"rows {n}, results {len(results)}")
    print("tokens", json.dumps(tot), "per row", {k: round(v / max(n, 1)) for k, v in tot.items()})


def main():
    rows = [json.loads(l) for l in open(f"{DIR}/input.jsonl", encoding="utf-8") if l.strip()]
    tot, results = {}, []
    if "--collect" in sys.argv:
        bid = sys.argv[sys.argv.index("--collect") + 1]
        b = call(f"/messages/batches/{bid}", method="GET")
        if b["processing_status"] != "ended":
            sys.exit(f"batch {bid}: {b['processing_status']}")
        req = urllib.request.Request(b["results_url"], headers={"x-api-key": key(), "anthropic-version": "2023-06-01"})
        with urllib.request.urlopen(req, timeout=120) as r:
            for line in r.read().decode().splitlines():
                item = json.loads(line)
                res = item["result"]
                if res["type"] == "succeeded":
                    add(tot, res["message"]["usage"])
                    results.append({"id": item["custom_id"], **parse(res["message"])})
                else:
                    results.append({"id": item["custom_id"], "action": "ask_akshay", "reason": f"batch {res['type']}"})
        return write(results, tot, len(rows))
    if "--batch" in sys.argv:
        b = call("/messages/batches", {"requests": [{"custom_id": r["id"], "params": params(r)} for r in rows]})
        print("batch", b["id"], b["processing_status"])
        return
    for r in rows:
        msg = call("/messages", params(r))
        add(tot, msg["usage"])
        results.append({"id": r["id"], "name": r["name"], **parse(msg)})
        time.sleep(0.5)
    write(results, tot, len(rows))


if __name__ == "__main__":
    os.makedirs(DIR, exist_ok=True)
    main()
