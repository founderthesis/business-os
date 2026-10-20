"""Pipeline review: guest research (tier, tags, blurb, better guest; decision 342) and one recommendation per open Engagement, on the Anthropic API credits (decision 358).

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
SEARCH_USD = 0.01  # web search, per search
PRICE = {"input_tokens": 2.0, "output_tokens": 10.0, "cache_read_input_tokens": 0.2, "cache_creation_input_tokens": 2.5}  # USD per MTok
DIR = "data/pipeline_review"

SYSTEM = """You research one guest and review their open conversation for ThePodium, a podcast agency run by Akshay Datt.
Shows: Founder Thesis (FT), un#, Built to Share (B2S), Human by Design (HBD). Zoya is the AI team member who sends routine follow-ups.

Part 1, research the guest (decision 342). Use web search, at most 5 searches, then web fetch to open at most 3 pages that carry the key numbers (funding, revenue, valuation). Use only facts you found, each with its full source URL and date.
- guest_tier: "Tier 1" = founder or co-founder, still active, of a unicorn, a listed or IPO-filed company, revenue or ARR above about USD 50M, a serial founder with a real exit, or widely known. "Tier 1.5" = founder of a funded growth-stage company (Series B or later, or USD 20M+ raised) or a strong niche name. "Tier 2" = early or small, a hired executive, or left the company. Fame never lowers the tier. Not a founder: tier on the bar of the show they best fit. A researcher with HBD-level stature (top citations, landmark work, still active) or the top AI executive at a Fortune 500 company is Tier 1; a genuinely senior, public-facing digital-assets leader at a systemically important institution (un#) is Tier 1; a VC fund GP of an established fund is Tier 1 or 1.5 by fund size and track record.
- research_tags: any that apply, only from this list: Big Indian founder, Big global founder, Global unicorn, Unicorn, Listed, Pre-IPO, Recently IPO'd, Serial founder, Outlier, Bootstrapped, Family business, ESOP track record, Hard to get, Needs research, Fintech, B2B SaaS, Edtech, Consumer, D2C, Healthtech, Deeptech, AI, Climate, Logistics, Marketplace, Mobility, Media, Gaming, Manufacturing, IT services, Crypto, Fortune 500, India, US, Europe, Middle East, Southeast Asia. Big Indian founder and Big global founder are for founders only, never academics or hired executives. Fortune 500 = the guest leads, or the company counts as customers, Fortune 500 firms. India, US, Europe, Middle East, Southeast Asia = the company's headquarters, plus its main market only when a source says most revenue comes from there; an office, team or a few customers in a region is not enough; regions outside the list get no tag (an Israeli company gets none for Israel). Use Needs research when the facts are thin.
- blurb: 2 to 3 neutral lines: who they are and the company in numbers (funding, valuation, revenue or ARR, customers, team), host-safe for any show.
- blurb_evidence: each fact with its full source URL and the publication date read from the page (open it with web fetch when the search result shows no date); write "date not found" only when the page itself has none.
- better_guest: if a co-founder or another leader at the company is a stronger guest (more stature, their own media presence), name them, their role and why; otherwise null.
- best_show: every show whose guest bar they clear, best first, from FT, un#, B2S, HBD; [] if none. best_show_why: one line.
  FT (Founder Thesis, Akshay): founders with real scale an Indian founder and operator audience recognises (IPO'd, unicorn, serious revenue or funding); hard deep tech (semis, drones, AI infra, climate hardware, novel finance) and VC fund GPs get a lift; young founders with under ~3 years of real operating tenure, hired CEOs of big corporates and pre-revenue founders in generic SaaS, D2C or marketplaces don't clear it.
  un# (Unhashed, Sri Misra): founder of a notable crypto org, or a genuinely senior, public-facing leader of digital assets at a systemically important institution; regulated tokenisation (tokenised funds, credit, transfer agents, licensed marketplaces) is the current tilt; commentators and mid-level people don't clear it.
  B2S (Built to Share, Satish Mugulavalli, Hissa): one of three lanes: an outlier business model or ownership structure (Jaipur Rugs, AppsForBharat), a famous discovery-name founder (Sanjeev Bikhchandani, Jaydeep Barman), or a global unicorn founder with a best practice to share; ESOPs and ownership are the theme; anyone linked to Qapita or another cap-table competitor of Hissa is out.
  HBD (Human by Design, Arjun Jain, FastCode AI): rock-star AI researchers (Hinton, Karpathy, Fei-Fei Li level, ~8,000+ citations), the top AI executive at a Fortune 500 company, or founders who turned AI research into products; never quantum, defence or classified, regulated patient-data healthcare, simulation-only, anyone who has worked with Arjun, or anyone with nothing notable in ~3 years. Before listing HBD for a researcher, search their citation count (Google Scholar or Semantic Scholar) and whether they co-authored with Arjun Jain or shared his labs (MPI Informatik, NYU with LeCun, IIT Bombay, IISc); put both findings in best_show_why, and leave HBD out if either can't be checked.

Part 2, recommend exactly one action on the conversation:
- chase: a live conversation where it's our move or a reply is overdue; Zoya follows up.
- nurture: no near-term deal but worth keeping warm; a slow, dated touch.
- drop: closed in substance (clear decline, gone silent after the full sequence and no Tier 1 or sponsored value, wrong fit).
- ask_akshay: needs his judgement (Tier 1, sponsored price, a guest decision, a relationship only he holds).
Rules: respect explicit declines and anyone who asked us to stop. Revive a decline only if the no was to the sponsored price (decision 355). Silence alone never ends a Tier 1, sponsored or approved pursuit; move it to nurture (decision 335). A drop of a Tier 1 or sponsored lead is always ask_akshay. A Tier 1 or sponsored row at Booking whose next step is the other side's is chase, not nurture, unless they named a later date. Use only the row and thread facts given for part 2. When no thread is given, judge from the row (status, dates, next action, last activity) and say so in the reason; choose ask_akshay only when the row itself is unclear.

Reply with JSON only, no other text:
{"guest_tier": "Tier 1|Tier 1.5|Tier 2", "research_tags": ["..."], "blurb": "...", "blurb_evidence": ["<fact> (<source>, <date>)"],
 "better_guest": null or {"name": "...", "role": "...", "why": "..."}, "best_show": ["FT|un#|B2S|HBD"], "best_show_why": "...",
 "action": "chase|nurture|drop|ask_akshay", "reason": "<one sentence>", "last_exchange": "<date, who, what>",
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
        "max_tokens": 8000,
        "output_config": {"effort": "low"},
        "system": [{"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}],
        "tools": [{"type": "web_search_20260209", "name": "web_search", "max_uses": 5},
                  {"type": "web_fetch_20260209", "name": "web_fetch", "max_uses": 3, "max_content_tokens": 6000}],
        "messages": [{"role": "user", "content": f"Engagement: {row['name']}\n\nRow:\n{row['row']}\n\nThreads:\n{row['threads']}"}],
    }


def parse(msg):
    if msg.stop_reason not in ("end_turn", "pause_turn"):
        return {"action": "ask_akshay", "reason": f"model stopped: {msg.stop_reason}"}
    text = "".join(b.text for b in msg.content if b.type == "text")
    try:
        return json.loads(text[text.find("{"):text.rfind("}") + 1])
    except ValueError:
        return {"action": "ask_akshay", "reason": "unparseable model output", "raw": text[:500]}


def add(tot, usage):
    for k in PRICE:
        tot[k] = tot.get(k, 0) + (getattr(usage, k, 0) or 0)
    stu = getattr(usage, "server_tool_use", None)
    tot["web_searches"] = tot.get("web_searches", 0) + ((getattr(stu, "web_search_requests", 0) or 0) if stu else 0)


def write(results, tot, n, discount=1.0):
    with open(f"{DIR}/output.jsonl", "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    for r in results:
        print(f"\n{r.get('name', r['id'])}: {r.get('action')}")
        for k in ("guest_tier", "research_tags", "blurb", "blurb_evidence", "better_guest", "best_show", "best_show_why", "reason", "last_exchange", "best_route", "current_status", "next_step"):
            print(f"  {k}: {r.get(k, '')}")
    cost = discount * sum(tot.get(k, 0) * PRICE[k] for k in PRICE) / 1e6 + tot.get("web_searches", 0) * SEARCH_USD
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
        p = params(r)
        msg = c.messages.create(**p)
        add(tot, msg.usage)
        for _ in range(3):  # a long web-search turn can pause; continue it
            if msg.stop_reason != "pause_turn":
                break
            p["messages"] = p["messages"][:1] + [{"role": "assistant", "content": msg.content}]
            msg = c.messages.create(**p)
            add(tot, msg.usage)
        results.append({"id": r["id"], "name": r["name"], **parse(msg)})
    write(results, tot, len(rows))


if __name__ == "__main__":
    os.makedirs(DIR, exist_ok=True)
    main()
