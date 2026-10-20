"""Pipeline review: one recommendation per open Engagement, on the Anthropic API credits (decision 358).

Read-only. Input is gathered by the API worker session (Notion row + Gmail excerpts) into
data/pipeline_review/input.jsonl, one JSON object per line:
  {"id": "<engagement page id>", "name": "...", "row": "<status, tier, show, next action, dates>",
   "threads": "<last exchanges, oldest first, with dates and senders>"}

  python3 -I migration/pipeline_review.py            # pilot: one Messages call per row
  python3 -I migration/pipeline_review.py --batch    # full run: one Message Batches request (half price)
  python3 -I migration/pipeline_review.py --collect <batch_id>

Output: data/pipeline_review/output.jsonl, plus token totals and an estimated cost.
The key is read from PODIUM_API_KEY and never printed or written. Needs: pip install anthropic
"""
import json
import os
import sys

import anthropic

MODEL = "claude-sonnet-5-5"
PRICE = {"input_tokens": 2.0, "output_tokens": 10.0, "cache_read_input_tokens": 0.2, "cache_creation_input_tokens": 2.5}  # USD per MTok
DIR = "data/pipeline_review"

SYSTEM = """You review one open guest or sponsor conversation for ThePodium, a podcast agency run by Akshay Datt.
Shows: Founder Thesis (FT), un#, Built to Share (B2S), Human by Design (HBD). Zoya is the AI team member who sends routine follow-ups.
Recommend exactly one action:
- chase: a live conversation where it's our move or a reply is overdue; Zoya follows up.
- nurture: no near-term deal but worth keeping warm; a slow, dated touch.
- drop: closed in substance (clear decline, gone silent after the full sequence and no Tier 1 or sponsored value, wrong fit).
- ask_akshay: needs his judgement (Tier 1, sponsored price, a guest decision, a relationship only he holds).
Rules: respect explicit declines and anyone who asked us to stop. Revive a decline only if the no was to the sponsored price (decision 355). Silence alone never ends a Tier 1, sponsored or approved pursuit; move it to nurture (decision 335). A drop of a Tier 1 or sponsored lead is always ask_akshay. Use only the facts given; if the evidence is missing say so and choose ask_akshay.
Reply with JSON only, no other text:
{"action": "chase|nurture|drop|ask_akshay", "reason": "<one sentence>", "last_exchange": "<date, who, what>",
 "best_route": "<direct mail | via PR <name> | WhatsApp | other>", "current_status": "<one line>",
 "next_step": "<one line, what Zoya or Akshay does>"}"""


def client():
    k = os.environ.get("PODIUM_API_KEY")
    if not k:
        sys.exit("PODIUM_API_KEY is not set")
    return anthropic.Anthropic(api_key=k)


def params(row):
    # Sonnet 5.5 thinks by default and thinking counts against max_tokens; low effort keeps it short.
    return {
        "model": MODEL,
        "max_tokens": 4000,
        "output_config": {"effort": "low"},
        "system": [{"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}],
        "messages": [{"role": "user", "content": f"Engagement: {row['name']}\n\nRow:\n{row['row']}\n\nThreads:\n{row['threads']}"}],
    }


def parse(msg):
    if msg.stop_reason != "end_turn":
        return {"action": "ask_akshay", "reason": f"model stopped: {msg.stop_reason}"}
    text = "".join(b.text for b in msg.content if b.type == "text")
    try:
        return json.loads(text[text.find("{"):text.rfind("}") + 1])
    except ValueError:
        return {"action": "ask_akshay", "reason": "unparseable model output", "raw": text[:500]}


def add(tot, usage):
    for k in PRICE:
        tot[k] = tot.get(k, 0) + (getattr(usage, k, 0) or 0)


def write(results, tot, n, discount=1.0):
    with open(f"{DIR}/output.jsonl", "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    cost = discount * sum(tot[k] * PRICE[k] for k in tot) / 1e6
    print(f"rows {n}, results {len(results)}")
    print("tokens", json.dumps(tot))
    print(f"cost about ${cost:.3f}, ${cost / max(n, 1):.4f} per row, ${330 * cost / max(n, 1):.2f} for 330 rows")


def main():
    c = client()
    rows = [json.loads(l) for l in open(f"{DIR}/input.jsonl", encoding="utf-8") if l.strip()]
    tot, results = {}, []
    if "--collect" in sys.argv:
        bid = sys.argv[sys.argv.index("--collect") + 1]
        b = c.messages.batches.retrieve(bid)
        if b.processing_status != "ended":
            sys.exit(f"batch {bid}: {b.processing_status}")
        names = {r["id"]: r["name"] for r in rows}
        for item in c.messages.batches.results(bid):
            if item.result.type == "succeeded":
                add(tot, item.result.message.usage)
                out = parse(item.result.message)
            else:
                out = {"action": "ask_akshay", "reason": f"batch {item.result.type}"}
            results.append({"id": item.custom_id, "name": names.get(item.custom_id, ""), **out})
        return write(results, tot, len(rows), discount=0.5)
    if "--batch" in sys.argv:
        b = c.messages.batches.create(requests=[{"custom_id": r["id"], "params": params(r)} for r in rows])
        print("batch", b.id, b.processing_status)
        return
    for r in rows:
        msg = c.messages.create(**params(r))
        add(tot, msg.usage)
        results.append({"id": r["id"], "name": r["name"], **parse(msg)})
    write(results, tot, len(rows))


if __name__ == "__main__":
    os.makedirs(DIR, exist_ok=True)
    main()
