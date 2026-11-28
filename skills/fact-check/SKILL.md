---
name: fact-check
description: Audit any near-final written draft for factual accuracy before it reaches the client or goes live. Voice- and client-agnostic: works for any ghostwriter on any client's post, newsletter, carousel, or article. Trigger on "/fact-check", "fact-check this", "claim audit", "verify the claims", "is this accurate", "verify before posting", "audit this draft", or run automatically as the last gate on any draft that makes factual claims. Extracts every factual assertion, numeric AND qualitative (what the product or company is, where it comes from, who founded it, superlatives like first/only/largest, what a named person said), verifies each against primary sources, and returns a claim ledger with a verdict, source, and confidence per claim. Hard-blocks output on any claim that is contradicted, or unverified while in a load-bearing position (hook, central claim, or close). Carries no voice rules, like post-polish; route voice to the client drafting skill.
---

# Fact-Check / Claim-Audit Gate

The last gate before a draft reaches the client or goes live. Its only job is to make sure no factual claim in the piece is wrong — especially not in the first line.

This skill is **client- and voice-agnostic by design.** Facts are facts regardless of whose voice the piece is in. It carries no banned phrases, no hook patterns, no length budgets. For voice, route to the client's drafting skill before or after this gate. This skill only checks whether the claims are true.

## The failure this prevents

The canonical example: a draft opens by calling Liquid Death "tap water." It is mountain spring water. A model summarised a source loosely, the error landed in the opening line, and it discredited the whole piece. Number-checking would never have caught it — it was not a number. It was a claim about what the product *is*.

The principle is absolute: **facts can't be wrong.** A single wrong fact in a load-bearing position discredits the whole piece and forces the client to re-verify everything themselves — the exact burden a ghostwriting operation exists to remove. The opening line carries most of the trust; protect it hardest.

## When to run this

- After a draft is written, before it is sent to the client or published. Always, on any piece that makes factual claims.
- When a writer pastes a draft and asks to verify it.
- As a standalone audit of a piece drafted elsewhere.

Run it on the **near-final** draft, not a rough one — checking claims that will be cut wastes effort.

## Step 1 — Extract every factual claim

A "claim" is any sentence or clause that asserts something checkable about the world. Most writers check class 1 below and stop. **The Liquid Death error lived in class 2.** All seven classes must be extracted.

| # | Claim class | What it covers | Why it bites |
|---|---|---|---|
| 1 | **Numeric / financial** | Revenue, raise, valuation, exit price, growth multiples, dates, market size, headcount, share, percentages | The class everyone already checks — keep checking |
| 2 | **Product / company truth, origin, sourcing** | What the product or company *is*, what it is made of, where it comes from, how it is produced or operated | The class that gets missed. "Mountain spring water," not "tap water" |
| 3 | **Category-position superlative** | "first", "only", "largest", "fastest-growing", "the original", "category-defining", "#1" | A wrong superlative is as discrediting as a wrong number, and easy to assert lazily |
| 4 | **People** | Who founded/built/runs it, when, their background, the origin moment, titles, who acquired or invested | "Two brothers" when it was a husband-and-wife is a factual error |
| 5 | **Event** | Acquisition (by whom, when), IPO, funding round, partnership, recall, lawsuit, launch, shutdown | Dates and counterparties must be exact |
| 6 | **Causal / mechanism** | "it scaled because X", "the acquirer was buying Y", "the insight was Z", "this caused that" | The load-bearing causal claim needs a real source, not inference dressed as fact |
| 7 | **Attribution / quote** | Anything in quotation marks or attributed to a named person or named source | Never attribute a fabricated or paraphrased line as a verbatim quote |

List every claim found, tagged by class. Miss none — the cost of a missed class-2 claim is another tap-water error.

## Step 2 — Mark load-bearing position

Position determines scrutiny. The same claim is higher-stakes in the hook than buried mid-body.

- **Load-bearing (maximum scrutiny):** any claim in the **opening line / hook**, the **central claim** the piece is built on, or the **close**. For longer pieces (newsletters, articles), also: any **section lede** and any **pulled stat or callout** — anything visually or structurally elevated. A wrong fact here kills the piece. These get verified to High confidence or they do not ship.
- **Supporting:** claims that carry the argument but are not the spine. Verified to at least Medium, or flagged.
- **Incidental:** colour details, asides. Verified if quick; flagged if not.

Tag each extracted claim L / S / I.

## Step 3 — Verify against primary sources

For each claim, search for confirmation. **Prefer primary and authoritative sources; distrust aggregators and AI summaries** — the canonical error came from trusting a summary.

Source quality, best to worst:
1. The company's own site, SEC/regulatory filings, official press release, named on-record founder/executive interview
2. Reputable press with a named reporter (WSJ, FT, Reuters, Bloomberg, trade press of record)
3. Well-sourced secondary coverage that cites primaries
4. Aggregators, listicles, SEO content, unsourced wikis — **treat as a lead to verify, never as proof**

Rules:
- **Surface source conflicts explicitly. Never silently resolve them.** If two credible sources disagree on a figure, report both and flag it. Picking one quietly is how a wrong number ships.
- A claim supported only by a single weak source is **Low confidence**, not verified.
- For class-6 causal claims, the bar is: is there a real source that supports this reading, or is it inference dressed as fact? Inference is allowed in the *framing*; it must not be stated as established fact if no source backs it.

Assign each claim a verdict:

| Verdict | Meaning |
|---|---|
| ✅ **Verified — High** | Multiple credible sources, at least one primary, agree |
| 🟡 **Verified — Medium** | One solid source; no contradiction found |
| 🟠 **Low** | Single weak source, or sources thin; treat as soft |
| ⚠️ **Unverified** | Could not confirm in available sources |
| ❌ **Contradicted** | Found credible evidence the claim is wrong |
| 🔀 **Conflicted** | Credible sources disagree; both reported |

## Step 4 — Apply the gate

The verdict plus the position decides whether the piece ships.

- **Any ❌ Contradicted claim → BLOCKED.** Must be corrected before the piece goes anywhere. State the correct fact and the source.
- **Any ⚠️ Unverified claim in a Load-bearing position → BLOCKED.** Either source it to confidence, or rewrite the line so the piece does not depend on the unverified claim.
- **🔀 Conflicted in a Load-bearing position → FIX-THEN-SHIP.** Surface both versions, let the writer/client choose which to state, or soften to the safe overlap.
- **⚠️ Unverified or 🟠 Low in a Supporting/Incidental position → FLAG.** May ship with the flag noted so the client can decide; offer to cut or soften.
- **All Load-bearing claims ✅/🟡 → CLEAR.**

## Step 5 — Output: the claim ledger

Return a ledger the client (or writer) can scan in under a minute.

```
FACT-CHECK — [client / piece title]
Verdict: [CLEAR / FIX-THEN-SHIP / BLOCKED]

LOAD-BEARING CLAIMS
1. [claim, verbatim from draft] — [class] — [verdict] — [source link] — [confidence note]
   ...
SUPPORTING CLAIMS
   ...
INCIDENTAL
   ...

MUST FIX BEFORE SENDING
- [exact line] → [the correct fact] — [source]
  (example) Opening line says "tap water." It is mountain spring water, sourced from
  an aquifer in Virginia. → rewrite the opener. Source: [link]

FLAGGED (ship-able, client's call)
- [claim] — [why it is soft] — [suggested handling]
```

If everything clears, say "All claims verified — clear" and do not manufacture doubt.

## Important behaviours

- **Do not rewrite the piece here.** This skill verifies and flags. Fixing the line is the drafting skill's job (or a targeted edit on instruction). Hand back the exact correction and the source; let the rewrite happen in the client's voice.
- **The opening line gets read twice.** Most of the trust is won or lost in the first sentence. Whatever else you check, never let a class-2 or class-3 claim sit unverified in the hook.
- **Quotes are verbatim or they are not quotes.** If a line is in quotation marks and attributed, it must match the source word for word. If it is a paraphrase, remove the quotation marks. Never present an invented line as something a real person said.
- **"Probably true" is not verified.** Confidence in the model's own prior is not a source. If it cannot be sourced, it is Unverified, full stop. This is the discipline the canonical error skipped.
- **Feed corrections to a learning loop, if the client has one.** Every ❌ Contradicted claim is a near-miss worth recording. Where a client maintains an edit-harvest or correction log, note the error there so recurring error types (e.g. product-sourcing claims) get promoted into standing pre-draft checks. Over time the same fact never has to be caught twice.
