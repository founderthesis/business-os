"""Episode context dump: one JSON and one Markdown file per episode, made from its transcript.

Akshay approved this on 5 Nov (feedback item 9). Runs on the Anthropic API credits in the
environment (ANTHROPIC_API_KEY), through the Message Batches API (50% off) with the shared
instruction block prompt-cached (decision 358).

Usage:
  python migration/episode_context.py estimate <episode_id> ...   # tokens and cost, no generation
  python migration/episode_context.py submit   <episode_id> ...   # build and submit one batch
  python migration/episode_context.py collect  [<batch_id>]       # poll, then write JSON + Markdown
  python migration/episode_context.py render                      # re-render Markdown from saved JSON

Inputs (git-ignored, written read-only from Notion by the session that picks the episodes):
  data/episode_context/manifest.json   {episode_id: {name, show, transcript_path | transcript_url,
                                         release, recorded}}
  data/episode_context/transcripts/    the transcript files the manifest points at

Outputs:
  data/episode_context/out/<episode_id>.json   the structured dump plus provenance and usage
  data/episode_context/out/<episode_id>.md     the same, as Markdown
  data/episode_context/batches.json            every batch submitted, with its episode ids
  data/episode_context/usage.csv               tokens and cost per episode (appended per collect)

The Markdown is what gets committed (docs/proposals/episode-context/...) and what the CTO writes
to Notion. This script never writes to Notion (one Notion writer at a time).

Re-run safely: submit skips episodes that already have an output JSON unless --force is given;
collect only writes results for its own batch; render only reads the JSON.
"""
import argparse
import csv
import datetime as dt
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "data" / "episode_context"
MANIFEST = BASE / "manifest.json"
OUT = BASE / "out"
BATCHES = BASE / "batches.json"
USAGE = BASE / "usage.csv"

# Model and prices come from the claude-api skill (cached 2026-10-06), not memory.
# Claude Sonnet 5.5: $2 input / $10 output per MTok, cache reads $0.20, 5-minute cache writes
# 1.25x input. The Batches API halves every token price.
MODEL = "claude-sonnet-5-5"
PRICE = {  # USD per million tokens, standard (non-batch)
    "input": 2.00,
    "output": 10.00,
    "cache_write": 2.00 * 1.25,
    "cache_read": 0.20,
}
BATCH_DISCOUNT = 0.5
MAX_TOKENS = 16000
EFFORT = "medium"  # extraction from a long document; thinking stays adaptive

# The shared instruction block. It is byte-identical across every request so the cache
# prefix holds; nothing episode-specific may go in here.
INSTRUCTIONS = """You turn one podcast transcript into an "episode context dump" for ThePodium, a podcast production agency. ThePodium runs Founder Thesis (host Akshay Datt, Indian founders and investors), un# or alpha un# (host Sri Misra, crypto, digital assets and tokenisation), Built to Share (host Satish Mugulavalli, people decisions, teams and ownership in startups) and Human by Design (host Dr. Arjun Jain, AI and technology built around people). The dump is reference material: writers, editors and agents will draw blog posts, show notes, social posts and sales notes from it, so it must be accurate, specific and easy to scan.

Source rules. These matter more than anything else.
1. Use only the transcript. Do not add facts from your own knowledge: no funding rounds, valuations, dates, titles or company details that are not said in the transcript. If the guest's company or role is not clear from the transcript, say so rather than guess.
2. The transcript is a raw recording transcript. It may include pre-show chatter, retakes, crosstalk, speech-to-text errors and off-the-record moments. Skip setup talk and anything the speakers say is off the record or to be cut. Correct an obvious speech-to-text error in a name only when the transcript itself makes the right spelling clear; otherwise keep the transcript's spelling.
3. Timestamps: copy them exactly as they appear in the transcript at the start of the relevant turn (for example 00:12:41.20 or 12:41.200). Never invent, round or convert a timestamp. If a point spans several turns, use the timestamp of the turn where it starts.
4. Never include an email address, phone number, WhatsApp or Telegram handle, street address or any other contact detail, even if one is said aloud.
5. Never use an em dash or en dash. Use a comma, a colon, a full stop or plain words instead.
6. Plain, direct English. Short sentences, specifics over generalities. Do not use the words "delve", "leverage", "unlock", "robust" or "seamless", and do not write "it's not X, it's Y".
7. The guest is the person being interviewed; the host is the person asking questions. Attribute every claim to whoever actually said it.

What to produce (fill every field of the schema):

summary: about 150 words (130 to 170). Who the guest is, what they built or do, the arc of the conversation and the two or three ideas a listener leaves with. Third person, present tense.

story_beats: the guest's own story in chronological order of their life and career, not the order of the conversation. Each beat is one or two sentences with the timestamp where it is told. Cover origin, turning points, setbacks, decisions and where things stand now. Usually 6 to 12 beats. If the episode is about a topic rather than a founder's life (for example an investor or an expert on a theme), give the beats of the guest's career and of the argument they make.

key_insights: 8 to 12 insights. Each is one line, a claim a reader could act on or argue with, not a topic label. Each carries the timestamp where it is said and who said it.

numbers_and_facts: every number, metric or checkable fact said on air: revenue, users, margins, prices, team size, funding, years, market sizes, growth rates. Quote the figure as said, give a few words of context, the timestamp, and who said it. Put "said by guest" in said_by when the guest said it, otherwise the host's name or "host". These are claims made on air, not verified facts.

mentions: companies, people, books, and tools or products named in the conversation. One entry per distinct name, each with a few words on the context in which it came up. Do not list the guest's own name or the host's in people.

blog_angles: 3 to 5 angles for a written piece. Each has a working title (specific, no clickbait, no colon-separated subtitle chains) and an angle of about two lines: what the piece argues and why a reader would care, grounded in what the guest said.

quotes: exactly 10 short quotable lines, verbatim from the transcript, each 8 to 35 words, with the timestamp of the turn and the speaker. Verbatim means the exact words in the transcript; you may cut filler words such as "um", "ah", "you know" or a false start, and mark a cut with an ellipsis, but you may not paraphrase, reorder or tidy grammar. Prefer the guest's lines. Pick lines that stand alone without context.

topics: 5 to 10 broad topics the episode covers (for example "D2C apparel", "bootstrapping", "stablecoin payments").

search_keywords: 10 to 20 search phrases a person might type to find this episode, as real people search: guest name plus company, the company plus what it does, the problems discussed.

guest_name and guest_company: as stated in the transcript, or as given in the episode details if the transcript does not say.

transcript_notes: one or two lines on anything that limits the dump: missing sections, heavy crosstalk, a transcript that cuts off, speaker labels that look wrong. Empty string if there is nothing to note."""

SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "guest_name", "guest_company", "summary", "story_beats", "key_insights",
        "numbers_and_facts", "mentions", "blog_angles", "quotes", "topics",
        "search_keywords", "transcript_notes",
    ],
    "properties": {
        "guest_name": {"type": "string"},
        "guest_company": {"type": "string"},
        "summary": {"type": "string"},
        "story_beats": {
            "type": "array",
            "items": {
                "type": "object", "additionalProperties": False,
                "required": ["timestamp", "beat"],
                "properties": {"timestamp": {"type": "string"}, "beat": {"type": "string"}},
            },
        },
        "key_insights": {
            "type": "array",
            "items": {
                "type": "object", "additionalProperties": False,
                "required": ["timestamp", "speaker", "insight"],
                "properties": {
                    "timestamp": {"type": "string"}, "speaker": {"type": "string"},
                    "insight": {"type": "string"},
                },
            },
        },
        "numbers_and_facts": {
            "type": "array",
            "items": {
                "type": "object", "additionalProperties": False,
                "required": ["timestamp", "figure", "context", "said_by"],
                "properties": {
                    "timestamp": {"type": "string"}, "figure": {"type": "string"},
                    "context": {"type": "string"}, "said_by": {"type": "string"},
                },
            },
        },
        "mentions": {
            "type": "object", "additionalProperties": False,
            "required": ["companies", "people", "books", "tools"],
            "properties": {
                k: {
                    "type": "array",
                    "items": {
                        "type": "object", "additionalProperties": False,
                        "required": ["name", "context"],
                        "properties": {"name": {"type": "string"}, "context": {"type": "string"}},
                    },
                }
                for k in ("companies", "people", "books", "tools")
            },
        },
        "blog_angles": {
            "type": "array",
            "items": {
                "type": "object", "additionalProperties": False,
                "required": ["working_title", "angle"],
                "properties": {"working_title": {"type": "string"}, "angle": {"type": "string"}},
            },
        },
        "quotes": {
            "type": "array",
            "items": {
                "type": "object", "additionalProperties": False,
                "required": ["timestamp", "speaker", "quote"],
                "properties": {
                    "timestamp": {"type": "string"}, "speaker": {"type": "string"},
                    "quote": {"type": "string"},
                },
            },
        },
        "topics": {"type": "array", "items": {"type": "string"}},
        "search_keywords": {"type": "array", "items": {"type": "string"}},
        "transcript_notes": {"type": "string"},
    },
}

EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
# Phone shapes only: an international +number, an Indian 5-5 mobile, or a 3-3-4 number. A bare
# figure such as 1200000000 is a number said on air and is left alone.
PHONE = re.compile(r"\+\d[\d\s-]{8,}\d|(?<!\d)\d{5}[\s-]\d{5}(?!\d)|(?<!\d)\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}(?!\d)")
TIMESTAMPISH = re.compile(r"^\(?\d{1,2}:\d{2}(?::\d{2})?(?:\.\d+)?\)?$")


# ---------------------------------------------------------------- helpers

def load_manifest():
    if not MANIFEST.exists():
        sys.exit(f"missing {MANIFEST.relative_to(ROOT)}: write it from Notion first")
    return json.loads(MANIFEST.read_text())


def norm_id(eid):
    return eid.replace("-", "").lower()


def read_transcript(meta):
    path = meta.get("transcript_path")
    if path:
        p = ROOT / path
        if not p.exists():
            raise FileNotFoundError(path)
        return p.read_text(encoding="utf-8", errors="replace")
    url = meta.get("transcript_url")
    if url:
        import urllib.request
        with urllib.request.urlopen(url, timeout=60) as r:  # noqa: S310 (approved transcript host)
            return r.read().decode("utf-8", errors="replace")
    raise FileNotFoundError("no transcript_path or transcript_url")


def user_block(meta, transcript):
    details = (
        f"Episode details (from the Episodes database, not the transcript):\n"
        f"Episode: {meta['name']}\nShow: {meta['show']}\n"
        f"Released: {meta.get('release') or 'not released or unknown'}\n"
        f"Recorded: {meta.get('recorded') or 'unknown'}\n"
    )
    return f"{details}\n<transcript>\n{transcript}\n</transcript>"


def params_for(meta, transcript):
    return {
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "thinking": {"type": "adaptive"},
        "output_config": {
            "effort": EFFORT,
            "format": {"type": "json_schema", "schema": SCHEMA},
        },
        # Breakpoint at the end of the shared block: every request reads it back.
        "system": [{"type": "text", "text": INSTRUCTIONS, "cache_control": {"type": "ephemeral"}}],
        "messages": [{"role": "user", "content": user_block(meta, transcript)}],
    }


def cost(usage, batch=True):
    f = BATCH_DISCOUNT if batch else 1.0
    return f * (
        usage.get("input_tokens", 0) * PRICE["input"]
        + usage.get("output_tokens", 0) * PRICE["output"]
        + usage.get("cache_creation_input_tokens", 0) * PRICE["cache_write"]
        + usage.get("cache_read_input_tokens", 0) * PRICE["cache_read"]
    ) / 1e6


def scrub(obj):
    """Remove contact details and em/en dashes from every string, whatever the model returned."""
    if isinstance(obj, dict):
        return {k: scrub(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [scrub(v) for v in obj]
    if isinstance(obj, str):
        if TIMESTAMPISH.match(obj.strip()):
            return obj
        s = EMAIL.sub("[contact removed]", obj)
        s = PHONE.sub("[contact removed]", s)
        s = s.replace(" \u2014 ", ", ").replace("\u2014", ", ").replace("\u2013", "-")
        return s
    return obj


def client():
    import anthropic
    return anthropic.Anthropic()


def load_batches():
    return json.loads(BATCHES.read_text()) if BATCHES.exists() else []


# ---------------------------------------------------------------- commands

def cmd_estimate(ids):
    """Token counts per episode. Uses count_tokens when a key is set, else ~4 chars per token."""
    man = load_manifest()
    have_key = True
    try:
        c = client()
        c.messages.count_tokens(model=MODEL, messages=[{"role": "user", "content": "x"}])
    except Exception as e:  # no key, no network: fall back to the heuristic and say so
        have_key = False
        print(f"count_tokens unavailable ({type(e).__name__}); using ~4 chars per token")
    total = 0
    for eid in ids:
        meta = man[norm_id(eid)]
        t = read_transcript(meta)
        if have_key:
            p = params_for(meta, t)
            n = c.messages.count_tokens(model=MODEL, system=p["system"], messages=p["messages"]).input_tokens
        else:
            n = (len(INSTRUCTIONS) + len(user_block(meta, t))) // 4
        total += n
        print(f"{n:>8}  {meta['name']}")
    print(f"{total:>8}  total input tokens ({'measured' if have_key else 'estimated'})")


def cmd_submit(ids, force=False, dry_run=False):
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request

    man = load_manifest()
    OUT.mkdir(parents=True, exist_ok=True)
    reqs, skipped, unreadable = [], [], []
    for eid in ids:
        key = norm_id(eid)
        meta = man.get(key)
        if not meta:
            unreadable.append((eid, "not in manifest"))
            continue
        if (OUT / f"{key}.json").exists() and not force:
            skipped.append(meta["name"])
            continue
        try:
            t = read_transcript(meta)
        except Exception as e:
            unreadable.append((meta["name"], f"{type(e).__name__}: {e}"))
            continue
        if len(t.strip()) < 2000:
            unreadable.append((meta["name"], f"transcript too short ({len(t)} chars)"))
            continue
        reqs.append(Request(custom_id=key, params=MessageCreateParamsNonStreaming(**params_for(meta, t))))
    for n in skipped:
        print(f"skip (already done): {n}")
    for n, why in unreadable:
        print(f"UNREADABLE: {n}: {why}")
    if not reqs:
        print("nothing to submit")
        return
    if dry_run:
        dump = BASE / "dry_run_requests.jsonl"
        dump.write_text("".join(json.dumps(dict(r)) + "\n" for r in reqs))
        print(f"dry run: {len(reqs)} requests built, written to {dump.relative_to(ROOT)}, nothing sent")
        return
    b = client().messages.batches.create(requests=reqs)
    log = load_batches()
    log.append({"batch_id": b.id, "submitted": dt.datetime.now(dt.timezone.utc).isoformat(),
                "model": MODEL, "episode_ids": [r["custom_id"] for r in reqs]})
    BATCHES.write_text(json.dumps(log, indent=2))
    print(f"submitted {len(reqs)} requests as {b.id}")


def cmd_collect(batch_id=None, poll=60):
    log = load_batches()
    if not batch_id:
        if not log:
            sys.exit("no batches submitted")
        batch_id = log[-1]["batch_id"]
    man = load_manifest()
    c = client()
    while True:
        b = c.messages.batches.retrieve(batch_id)
        if b.processing_status == "ended":
            break
        print(f"{batch_id}: {b.processing_status}, {b.request_counts.processing} processing")
        time.sleep(poll)
    rows, failed = [], []
    for r in c.messages.batches.results(batch_id):  # results come in any order: key by custom_id
        key = r.custom_id
        meta = man.get(key, {"name": key, "show": ""})
        if r.result.type != "succeeded":
            failed.append((meta["name"], r.result.type))
            continue
        msg = r.result.message
        if msg.stop_reason in ("refusal", "max_tokens"):
            failed.append((meta["name"], f"stop_reason {msg.stop_reason}"))
            continue
        text = next((blk.text for blk in msg.content if blk.type == "text"), "")
        try:
            data = scrub(json.loads(text))
        except json.JSONDecodeError:
            failed.append((meta["name"], "output was not valid JSON"))
            continue
        u = msg.usage
        usage = {
            "input_tokens": u.input_tokens, "output_tokens": u.output_tokens,
            "cache_creation_input_tokens": u.cache_creation_input_tokens or 0,
            "cache_read_input_tokens": u.cache_read_input_tokens or 0,
        }
        usd = cost(usage)
        rec = {
            "episode_id": key, "episode": meta["name"], "show": meta["show"],
            "provenance": {
                "source": "transcript", "transcript": meta.get("transcript_path") or meta.get("transcript_url"),
                "model": msg.model, "batch_id": batch_id, "message_id": msg.id,
                "made": dt.date.today().isoformat(),
            },
            "usage": usage, "cost_usd": round(usd, 5),
            "context": data,
        }
        (OUT / f"{key}.json").write_text(json.dumps(rec, indent=2, ensure_ascii=False))
        (OUT / f"{key}.md").write_text(to_markdown(rec))
        rows.append({"episode_id": key, "episode": meta["name"], **usage, "cost_usd": f"{usd:.5f}",
                     "batch_id": batch_id})
    if rows:
        new = not USAGE.exists()
        with USAGE.open("a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            if new:
                w.writeheader()
            w.writerows(rows)
    tot = {k: sum(int(r[k]) for r in rows) for k in
           ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")}
    usd = sum(float(r["cost_usd"]) for r in rows)
    print(f"written {len(rows)}, failed {len(failed)}")
    for n, why in failed:
        print(f"FAILED: {n}: {why}")
    print(json.dumps(tot), f"cost ${usd:.4f}")
    if rows:
        print(f"per episode ${usd / len(rows):.4f}")


def cmd_render():
    n = 0
    for p in sorted(OUT.glob("*.json")):
        rec = json.loads(p.read_text())
        p.with_suffix(".md").write_text(to_markdown(rec))
        n += 1
    print(f"rendered {n}")


# ---------------------------------------------------------------- markdown

def to_markdown(rec):
    c = rec["context"]
    L = [f"# {rec['episode']}", ""]
    L += [f"Show: {rec['show']}. Episode id: {rec['episode_id']}. Made {rec['provenance']['made']} "
          f"from the transcript by {rec['provenance']['model']}. Timestamps are the transcript's own.", ""]
    if c.get("transcript_notes"):
        L += [f"Transcript notes: {c['transcript_notes']}", ""]
    L += ["## Summary", "", c["summary"], ""]
    L += ["## Story beats", ""] + [f"{i}. `{b['timestamp']}` {b['beat']}" for i, b in enumerate(c["story_beats"], 1)] + [""]
    L += ["## Key insights", ""] + [f"- `{x['timestamp']}` {x['insight']} ({x['speaker']})" for x in c["key_insights"]] + [""]
    L += ["## Numbers and facts said on air", "",
          "Claims as said in the conversation, not verified.", "",
          "| Time | Figure | Context | Said by |", "|---|---|---|---|"]
    L += [f"| `{x['timestamp']}` | {cell(x['figure'])} | {cell(x['context'])} | {cell(x['said_by'])} |"
          for x in c["numbers_and_facts"]] + [""]
    L += ["## Mentions", ""]
    for k, title in (("companies", "Companies"), ("people", "People"), ("books", "Books"), ("tools", "Tools and products")):
        items = c["mentions"].get(k) or []
        L += [f"**{title}:** " + ("; ".join(f"{m['name']} ({m['context']})" for m in items) if items else "none"), ""]
    L += ["## Blog angles", ""]
    for i, a in enumerate(c["blog_angles"], 1):
        L += [f"{i}. **{a['working_title']}**  ", f"   {a['angle']}"]
    L += ["", "## Quotable lines", ""] + [f"- `{q['timestamp']}` {q['speaker']}: \"{q['quote']}\"" for q in c["quotes"]] + [""]
    L += ["## Topics", "", ", ".join(c["topics"]), ""]
    L += ["## Search keywords", "", ", ".join(c["search_keywords"]), ""]
    return "\n".join(L)


def cell(s):
    return str(s).replace("|", "/").replace("\n", " ")


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("estimate", "submit"):
        s = sub.add_parser(name)
        s.add_argument("ids", nargs="*", help="Episode ids (Notion page ids); default: every manifest entry")
        if name == "submit":
            s.add_argument("--force", action="store_true", help="redo episodes that already have output")
            s.add_argument("--dry-run", action="store_true", help="build the requests, send nothing")
    s = sub.add_parser("collect")
    s.add_argument("batch_id", nargs="?")
    s.add_argument("--poll", type=int, default=60)
    sub.add_parser("render")
    a = ap.parse_args()
    if a.cmd in ("estimate", "submit") and not a.ids:
        a.ids = list(load_manifest())
    if a.cmd == "estimate":
        cmd_estimate(a.ids)
    elif a.cmd == "submit":
        cmd_submit(a.ids, a.force, a.dry_run)
    elif a.cmd == "collect":
        cmd_collect(a.batch_id, a.poll)
    else:
        cmd_render()


if __name__ == "__main__":
    main()
