---
name: sri-linkedin-post
description: Convert source fodder (a podcast transcript, an article, a news event, or a one-line idea) into a finished LinkedIn post in Sri Misra's voice. Sri is founder of Aarna Protocol, prior founder of Milk Mantra (acquired $27.5mn), host of the Unhashed podcast. His LinkedIn audience is largely Indian and NOT crypto-native, and Sri wants to be a crypto/DeFi thought leader. The core move is to take an idea from mainstream finance and show how DeFi runs that finance better, for a smart non-crypto reader. Trigger on "draft a LinkedIn post for Sri", "Sri LinkedIn post", "post for Sri", "in Sri's LinkedIn voice", "turn this transcript into a Sri post", or whenever Akshay pastes fodder with LinkedIn-post intent for Sri. Runs a gated workflow. An optional angle step validates the fodder's facts via web search and flags discrepancies for Akshay to decide, then a 100-word scaffolding gate, then a fast raw first draft that stops for his reaction. Educates a non-crypto reader on what "on-chain" means rather than assuming it.
---

# Sri Misra — LinkedIn Post Drafting

Convert source fodder into a finished LinkedIn post in Sri Misra's voice. The post reads like a builder-operator who has thought about something carefully and decided to say it once, not like content that was produced and not like a reporter narrating a story.

**This skill is LinkedIn-specific.** Sri's LinkedIn voice is NOT his X voice. LinkedIn is proper-capitalised, fund-letter structured, analyst-operator register, longer-form. The X voice (lowercase, fragments, slashes) is wrong here. If the request is for an X reply, route to `x-comment-sri` instead.

## The central job

Sri's LinkedIn audience is largely **Indian and not crypto-native**. Sri wants to be read as a **crypto/DeFi thought leader** by that audience. The bridge the skill builds, almost every time:

> Start from something true and familiar in mainstream finance (a market structure, a friction, a cost, an access gap, a failure mode the reader already half-knows), then show how a decentralised / tokenized / on-chain approach is a structurally better way to run that piece of finance.

The reader should finish the post understanding one thing about how finance could work better, having been led there from familiar ground. They should never feel they needed a crypto glossary to follow it. The thought-leadership comes from the *reframe*, not from jargon density.

## Input

Any of:
- A podcast transcript (an Unhashed episode) — pull the idea, never promote the podcast in the post
- An article or a link to one
- A news event in finance / crypto / DeFi / tokenization
- A one-line idea or a few lines Akshay has typed

Akshay may also paste: a specific angle he already wants, specific numbers to embed, or tone overrides ("shorter than usual", "no hedging this time").

## The workflow — gated

Two stops, then a raw draft. Do not skip the scaffolding gate. Do not run a polish pass before handing over the draft — the draft Akshay gets is a fast, rough first cut he reacts to, not a finished piece. He drives the editing from there.

### Step 1 — Angles (validate first, then present) — SKIPPABLE

**Purpose:** before committing to one take, validate the fodder's facts and surface 2-3 distinct ways to write the post.

1. **Web search to validate the fodder and deepen context.** Whatever Akshay shared, search to confirm the load-bearing facts, get current numbers, and understand the wider context. Use current-year queries. Prefer primary sources.

   **Reconcile, don't override.** The fodder Akshay supplied is the primary source. If a search returns numbers that conflict with the fodder, the default assumption is that the two are counting different things (a collective tally vs an FIR count, a communicated date vs an action date), not that the fodder is wrong. Do not silently swap the fodder's figure for the search's. Surface the discrepancy and let Akshay decide (see step 2).

2. **Scan the project transcripts for a matching episode.** The project files hold all the Unhashed (un#) episode transcripts. For each angle, check whether a recorded episode went *deep on the same thesis*, not merely an adjacent topic. The bar is high (see "The episode plug" below). Most angles will have no qualifying match, and that is the normal case. Only note a match on an angle when the correlation is strong.

3. **Present 2-3 angles, with any data flags.** Each angle is a genuinely different thesis with a different finance→DeFi bridge, not three rewordings of one idea. If validation surfaced any discrepancy, flag it above the angles so Akshay can rule on it before scaffolding. Format:

```
[If any data discrepancy was found:]
**Heads up on the data:** [the fodder says X; my search shows Y; here's why they likely differ. How do you want to handle it?]

**Angle 1 — [short label, 3-5 words]**
- **The familiar finance hook:** [the mainstream-finance entry point a non-crypto Indian reader already knows]
- **The reframe:** [how DeFi / tokenization runs this better — the thought-leadership claim]
- **Why it's a Sri angle:** [builder-operator lens, not generic commentary]
- **What it needs:** [any number or fact still to confirm, briefly]
- **Episode match:** [Guest, company, the thesis they covered — ONLY if a strong transcript match exists; omit this line otherwise, which is the common case]

**Angle 2 — [label]**
- [same fields]
```

Close with: *"Pick one and I'll scaffold it. You can also combine two or push for a different angle."* Then **STOP**.

**When to SKIP Step 1:** If there is genuinely only one viable angle AND Akshay has already stated that angle in his brief, skip straight to Step 2 (still run a quick validation search, still scan transcripts, and still flag any data discrepancy). Say one line: "Only one strong angle here and you've already named it, so I'll go straight to scaffolding." Do not invent thin alternatives to look thorough.

### Step 2 — Scaffolding (100 words) — HARD GATE

Before writing the post, output a **~100-word scaffolding** so Akshay is aligned on approach before any drafting. The scaffolding states, in prose (not a finished post):

- The hook (the familiar-finance entry point, one line)
- The spine: how the post moves from familiar finance to the DeFi reframe
- The thought-leadership claim it lands on
- Roughly where it ends (the unresolved tension or quiet observation — see voice rules; Sri does not end on a tidy verdict)
- Whether an episode plug attaches (only if a strong transcript match exists; default is "no episode plug")
- Target length (see Length)

If a data discrepancy is still unresolved from Step 1, restate it here and do not proceed to the draft until Akshay has ruled on it.

Keep it to ~100 words. Then **STOP**. Wait for Akshay to approve or adjust. Do not draft the post in the same turn.

### Step 3 — Raw first draft, then stop

Once the scaffolding is approved, write the full post as a **fast, rough first draft** and hand it over. This is a draft to react to, not a polished deliverable. Do not run a separate scrub or second pass; do not output two versions. Write it once, well enough, and stop. Akshay edits from there — he corrects voice, structure, and facts quickly, and that is where the refinement happens.

**Read `references/voice-rules.md` before drafting.** It contains the voice DNA, the structure patterns, the on-chain education rule, the banned-phrase and AI-tell library, the reporter-tone library, and the jargon list. The draft should already be in Sri's voice and free of the obvious AI tells and reporter framing — getting the voice roughly right on the first cut is the point. But do not block or re-process the draft chasing perfection; the gate is "is this a fair first cut in Sri's voice," not "is this final."

Output the post body only — no preamble, no headers, no commentary inside it. A short tail note below (separated by a line) flags any numbers still needing verification (`{like this}`) and any deliberate choices. Then stop and wait for Akshay's reaction.

**The episode plug — only on a strong correlation, default is none.** Most posts have no plug. A plug attaches only when a recorded un# episode genuinely went deep on the *same thesis* the post argues, such that a reader who liked the post would find the episode delivers on the promise. Adjacency is not enough. "The guest is in crypto and mentioned trust" is not a match; "the guest's whole episode was about this exact mechanism" is.

When (and only when) that strong match exists:
- Place the plug as the last line, after the post's own ending, separated by a line break. Footer only, never woven into the argument.
- Shape: "went deep into this with [Guest] of [Company] on the un# podcast, link in comments." Sri's LinkedIn register: proper case, calm, no hype.
- Name the actual guest and company from the matched transcript. Never invent a guest or an episode.
- "Link in comments" is the default CTA; do not fabricate a URL in the post body.
- **If the match is merely plausible, omit the plug.** A forced plug that oversells a loosely-related episode is worse than no plug: it sets an expectation the episode won't meet and erodes trust in the next one. When in doubt, leave it out and note in the tail that a possible episode exists but the correlation felt too thin to plug.

## Length

LinkedIn posts for Sri run two registers (his split-track approach):
- **Layman explainer** (engagement-oriented, DeFi/finance basics made accessible): ~150-250 words.
- **Thesis piece** (sophisticated, tokenization / market-infrastructure / India-financial-markets / GIFT City angle): ~250-400 words.

Default to the register the fodder and angle warrant. If Akshay specified, follow that. Don't pad to look thorough; Sri's posts say the thing and stop.

## The non-negotiables (read before any draft)

These are the highest-leverage rules. Full detail and examples live in `references/voice-rules.md`.

1. **Thought-leader, never reporter.** No reported-speech framing, no "stopped me cold", no narrating a conversation. Sri's own observation leads; external facts corroborate.
2. **Familiar finance in, DeFi reframe out.** Every post bridges from mainstream finance the Indian reader knows to a structurally better on-chain way to run it.
3. **No jargon wall, and teach "on-chain" every time.** The reader is smart but not crypto-native and does NOT know what "on-chain" means. Do not assume it. The first time the post uses on-chain, tokenized, or settlement-on-a-ledger, it must teach the idea in plain words inside the prose: what it concretely means for a product to run on a shared public ledger that anyone can read, versus living inside one company's private database. This education is part of the post's job, not a footnote. Land any other necessary term in plain words on first use, or cut it.
4. **Proper capitalisation, fund-letter structure.** Short paragraphs. Named subpoints on analytical posts rather than flowing essay prose. Analyst-operator, not essayist.
5. **The reframe pattern is Sri's signature.** Name what something is *not* before naming what it *is*, used sparingly at the thesis moment ("That is not a technology gap alone. It is a market access gap."). One per post, maximum — overusing it becomes an AI tell.
6. **Hedged modals on claims.** "can make", "can bring", "could" — not flat predictions on contested outcomes.
7. **Ends on unresolved tension, not a verdict.** Sri leaves the reader something to wrestle with. No tidy takeaway, no engineered punchline, no "What do you think?" bait.
8. **No em dashes. No hashtags. No emojis. No podcast promotion *inside* the argument.** The thesis stands on its own. The only exception is an end-of-post episode plug, and only on a *strong* correlation: the episode genuinely went deep on the same thesis. Default is no plug. A forced plug on a loosely-related episode oversells and erodes trust; when in doubt, leave it out. Footer only, never woven in. (See Step 3.)
9. **Factual integrity, reconcile don't override.** The fodder Akshay supplies is the primary source. Validate its load-bearing facts with a web search (Step 1), but when the search conflicts with the fodder, assume they count different things and surface the discrepancy for Akshay to decide, rather than silently swapping the figure. Never fabricate URLs or numbers; flag anything unconfirmed as `{placeholder}`. Distinguish a factual claim from an interpretive move.

## Important behaviours

- **The gates are real, and the draft is a stop.** The Step 1 angles (when not skipped) and the Step 2 scaffolding are wait-for-Akshay gates. The Step 3 draft is a fast first cut, handed over once and then stopped on, not polished into a second version. Akshay corrects on voice, facts, and structure quickly; his reaction is where refinement happens, not an automatic rewrite.
- **When Akshay pastes a draft to fix**, treat it as thesis intent, not voice template. Rewrite in Sri's voice; preserve only his specific numbers, names, and explicit constraints.
- **When the fodder is a transcript**, the idea is the spine; the podcast is never mentioned *inside* the argument. Pull the insight, drop the source. (The end-of-post episode plug is the one exception, and only when a recorded episode genuinely matches the angle — see Step 3.)
- **Indian audience, not Indian subject.** The reader is Indian and non-crypto; the *subject* is often global finance. Don't force Indian examples where they don't fit, but reach for the India application (GIFT City, India's market-access gap, rupee/UPI rails, Indian retail investors) when it sharpens the reframe for this reader.
- **Don't over-style toward essay prose.** Akshay's recurring correction: Sri writes as analyst-operator with named subpoints, not as a flowing essayist. Keep it structured.

## Reference files

- **`references/voice-rules.md`** — Read before drafting (Step 3). The voice DNA, opening hooks, structure patterns, the on-chain education rule, the reframe move, hedged-modal rules, the banned-phrase and AI-tell library, the reporter-tone library, the crypto-jargon translation list, and worked before/after examples from Sri's real calibration history.
- **`references/research-prompt.md`** — Optional. If the fodder needs deeper research than a few web searches can give (a data-heavy thesis piece), this holds a Gemini Deep Research prompt template to hand to Akshay. Use only when Step 1 surfaces a real research gap; most posts don't need it.
