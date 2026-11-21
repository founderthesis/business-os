---
name: un-newsletter
description: Convert a podcast transcript, topic, theme, or news event into a Galaxy Research-grade newsletter for aarnâ's un# publication. Trigger on "draft un#52", "new un# issue", "un# from this transcript", "make this into a newsletter", "next un#", "newsletter for aarna", "Galaxy-style piece on X", or whenever Akshay pastes a transcript or names a theme with newsletter intent. Runs a three-phase workflow with hard STOPs. Phase 1a proposes 2-3 candidate theses for Akshay to pick from. Phase 1b builds a Gemini Deep Research prompt for the chosen thesis and stops. Phase 2 reviews the research pasted back and decides if another pass is needed (emits another prompt and stops) or proceeds. Phase 3 drafts the newsletter as HTML matching the un#51 template. The podcast is supporting material never the spine, aarnâ confined to one sidebar, one pull quote in the second half, no em-dashes, no AI-tells. Trigger whenever Akshay supplies source material with newsletter intent even when he doesn't say "skill".
---

# un# Newsletter Drafting

Convert source material into a deeply researched newsletter that reads like a Galaxy Research analyst wrote it. The published artifact is HTML, structured like un#51 (`references/template.html`), published fortnightly at `unhashed.aarna.ai`.

The single most important thing this skill does is **not start drafting on first contact**. The newsletter is not a transcript rewrite or a topic explainer. It is an analytical piece that uses a primary-sourced research base, and that base does not exist until the user has run Gemini Deep Research and pasted the result back. The skill enforces this with two hard STOP gates.

## Input

One of:
- A podcast transcript (Unhashed episode) — most common case
- A theme or topic Akshay wants explored (e.g. "the bifurcation of crypto custody in 2026")
- A news event with a thesis attached ("Aave just shipped X — make a piece on what this means for governance")
- An idea fragment with a hunch ("there's something interesting about how oracles fail under stress — turn it into un#52")

The user may signal which issue number it is (un#52, un#53, etc.) or leave it blank for the skill to fill in later.

## Output

A standalone HTML file styled to match `references/template.html`, named `un<N>_<slug>.html` (e.g. `un52_when_oracles_lag.html`), saved to `/mnt/user-data/outputs/` and presented to the user. The HTML is fortnightly newsletter chrome with all analytical prose filled in.

## The three-phase workflow

These phases are sequential and gated. Never skip a phase. Never draft before Phase 3.

### Phase 1 — Source assessment and thesis selection

This phase has **two STOPs**, not one. First propose thesis options and wait for Akshay to pick. Then build the Gemini prompt for the chosen thesis and wait for the research. Never collapse these into a single output.

#### Phase 1a — Thesis options

Read the source material carefully. Then do the zoom-out move (see below) to identify the candidate theses. Aim for **2-3 genuinely distinct theses** whenever the source supports them. Fall back to a single thesis only when the source points so overwhelmingly to one angle that proposing alternatives would feel forced — and even then, flag the obvious-second alternative briefly so Akshay can redirect.

Each thesis option should:
- Have a genuinely different analytical claim (not three restatements of one idea)
- Connect to a different broader pattern (different zoom-out)
- Require different evidence to research (not the same data set with different framing)

Output the options in this format:

```
**Thesis 1 — [Short label, 3-5 words]**
- **Claim:** [1-2 sentence statement of the thesis]
- **The zoom-out:** [What broader pattern this is an instance of]
- **Why this angle:** [What makes this an aarnâ/Sri lens, not a generic take]
- **What evidence we'd need:** [3-4 specific data types, briefly — not the full Gemini prompt]

**Thesis 2 — [Short label]**
- [Same fields]

**Thesis 3 — [Short label]**
- [Same fields]
```

Close with this exact line:

> Which thesis should I research? You can also tell me to combine two, refine one, or sketch a fourth angle.

Then **STOP**. Wait for Akshay to pick. Do not write the Gemini prompt yet. Do not draft. Do not preview HTML.

If only one thesis is genuinely viable, output it as Thesis 1 with one short paragraph above explaining why the source pointed strongly to one angle, then still close with: "Want me to proceed with this, or push me to find a second angle?" — never assume the user wants to skip the gate.

#### Phase 1b — Gemini prompt for chosen thesis

Once Akshay has picked a thesis (or asked for a combine/refine/fourth), construct the Gemini Deep Research prompt structured around the chosen thesis. Read `references/gemini-prompt-format.md` if not already loaded.

Output:
1. A short paragraph acknowledging the choice and naming briefly why this angle will produce a strong piece (2-3 sentences, conversational, not a presentation)
2. The Gemini Deep Research prompt in a code block, ready to copy

Then **STOP**. Do not draft. Do not preview the newsletter. Do not produce HTML. Akshay will run the prompt on Gemini, paste the result back, and Phase 2 begins.

### Phase 2 — Research assessment

The user has pasted back the Gemini Deep Research output. Read it carefully. Evaluate it against the thesis from Phase 1:

**Sufficient research has all of these:**
- Every load-bearing statistic has a primary source with a URL
- Data is current (within ~6 months of the publication date, or older only where the historical figure is the point)
- The thesis is supported from at least 3 angles — not three restatements of the same fact
- At least one named counter-position or contrasting view, with evidence
- Specific named players, dollar figures, percentages — not generic claims
- Source quality is mixed correctly: primary sources (company docs, SEC filings, academic papers, official dashboards) over secondary aggregators

**Trigger another research pass when:**
- A key claim has no primary source and the aggregator citing it is generic
- Data is stale and current data is available (e.g., a 2024 figure for something that updates monthly)
- The thesis is supported by only one angle (one data type, one source, one analytical frame)
- No counter-evidence surfaced — a Galaxy piece always considers the bull case for the opposite
- Specific load-bearing numbers are missing (the chart can't be built, the section can't be written)

If more research is needed: output a short paragraph naming the specific gaps, then a follow-up Gemini Deep Research prompt focused on those gaps only. Then **STOP** again.

If research is sufficient: proceed to Phase 3 without further questions. Do not ask the user "should I draft now?" — that's the gate the workflow has already passed.

### Phase 3 — Drafting

Before writing a word of prose:

1. **Read `references/template.html` in full.** This is the canonical visual structure. The new newsletter must match it visually (hero banner with title + issue pill, masthead, dek, lede, section banners, subheadings, pull quote, sidebar, references list, closing footer).

2. **Read `references/editorial-voice.md` in full.** This contains the voice rules, banned phrases, and AI-tell patterns Sri has explicitly pushed back on. Drafting without reading this guarantees voice failure.

3. **Plan the section structure before writing.** Sketch the section banners and what each section argues. The piece should have 5-7 section banners, with subheadings (`> subhead`) inside the 2-3 longest sections.

4. **Place the pull quote in the second half.** If the source was a podcast transcript, pick the one quote that crystallises the thesis from a primary-source position (the institutional insider describing institutional behaviour, the protocol founder describing the protocol's choices). If the source was a theme with no transcript, either skip the pull quote or pull a quote from the deep research if one is salient.

5. **Place the IN PRACTICE sidebar between the last analytical section and the in-closing banner.** This is the only place aarnâ appears in the newsletter body. The sidebar is ~50 words, written as a treasury-allocator observation that lands on the aarnâ approach. Never inside an analytical section. Never mid-paragraph.

6. **Build the references list as you write.** Every superscript number in the prose links to a numbered entry at the bottom with URL and date. Aim for ~20 references. Each is one line.

7. **Write the HTML directly into `/mnt/user-data/outputs/un<N>_<slug>.html`** following the template structure. Copy the template's CSS verbatim — do not "improve" the styling.

8. **Call present_files at the end** to make the file visible to the user.

## The zoom-out move

This is the single most important intellectual step. The newsletter is never about the surface topic. It is about the systemic pattern the surface topic is an instance of.

In Phase 1a, run this move **2-3 times** to generate genuinely distinct theses. Each pass should land on a different broader pattern, not three restatements of one idea. The point of offering multiple theses is to surface angles Akshay might not have considered, not to give him minor variations of the same take.

Three questions to walk through for each candidate thesis:

1. **What is the surface topic?** (The podcast guest, the news event, the protocol — the concrete thing.)
2. **What is this an instance of?** What broader industry pattern, market structure shift, or analytical phenomenon does it manifest? Try to find multiple plausible answers here — a strong piece of source material usually points at several systemic phenomena, not just one.
3. **What is the thesis statement?** A 1-2 sentence claim about the broader pattern that the surface topic provides evidence for.

Examples of the move:

| Surface topic | Zoom-out | Thesis |
|---|---|---|
| Anton Katz interview about Talos | DeFi execution has bifurcated into institutional vs retail tiers | Permissionless ≠ symmetric: the same Uniswap pool serves two different execution surfaces |
| AAVE governance proposal X | DeFi governance is concentrating in oligopolistic patterns | Governance capture is the new smart contract risk |
| Hyperliquid HIP-3 launch | Tokenized RWAs are migrating onto crypto-native venues, not the reverse | The institutional perp narrative is wrong about which infrastructure wins |
| Pendle PT/YT market growth | Yield is being decomposed into tradeable primitives | Fixed-income on-chain is happening not via tokenized treasuries but via yield stripping |

The test for a good zoom-out: the thesis is something a Galaxy Research analyst would publish even if the podcast/news event never happened. The source material is *evidence* for the thesis, not *the subject* of the piece.

A bad zoom-out (and a signal to redo the move): the thesis is a paraphrase of the guest's bio or the news event's headline. "Talos provides institutional execution infrastructure" is not a thesis. "Permissionless isn't symmetric" is.

### Worked example — three theses from one source

The Anton Katz / Talos interview was used to produce un#51's "permissionless isn't symmetric" thesis. But the same source could have supported other angles. A strong Phase 1a output from that interview would have looked like:

1. **Permissionless isn't symmetric** — DeFi execution has bifurcated into institutional and retail tiers using the same contracts. *(The angle un#51 took.)*
2. **The hidden moat is the data layer** — Reference rate vendors like Kaiko and Coin Metrics sit below the execution stack and price institutional flow at seven-figure annual fees retail can't access. The pricing layer is where institutional crypto's actual asymmetry lives.
3. **Crypto-native execution has reached TradFi parity** — Venue connectivity counts at Talos, GSR, and Wintermute now rival Bloomberg/FactSet. The institutional infrastructure question for digital assets is no longer "is the stack ready" but "what does it route around."

These three theses use overlapping evidence (the same Talos data, the same MEV figures) but make genuinely different analytical claims, point at different broader patterns, and would result in different newsletters. That is what Phase 1a should produce.

## The Gemini Deep Research prompt

The prompt is constructed around the thesis, not the source. The user is asking Gemini to find primary-sourced evidence for a specific analytical claim, not to summarise a topic.

Read `references/gemini-prompt-format.md` for the full structure and worked examples. The short version:

1. State the thesis upfront
2. Provide brief context for why this thesis is timely
3. List the specific data and sources needed, grouped by topic area
4. Request counter-evidence explicitly
5. Specify recency requirements
6. Specify citation format

The prompt should be substantial (300-500 words is typical for Gemini Deep Research). Short prompts produce shallow research.

## What "looks like un#51" means

When Phase 3 produces a draft, it should be recognisable as the next issue of the same publication. The visual and structural recognition cues are:

- Hero banner card at top (dark teal-black gradient) with title in Newsreader italic teal-glow, issue pill (`un#NN`) in teal outline below
- Slim masthead above (brand + date)
- Dek in italic Newsreader on cream
- Lede paragraph with teal left border
- Section banners (dark gradient cards with lowercase teal-glow titles and faint subtitles)
- `> subheading` device inside 2-3 longest sections, never used in short sections
- Pull quote treatment with teal left border, italic serif, mono caps citation, located in the second half
- Inline SVG chart where data is the punchline
- IN PRACTICE sidebar (subtle teal tint, mono caps label, ~50 words, the only aarnâ mention)
- Closing banner ("in closing" or similar)
- Podcast plug footer (italic Newsreader, brief)
- References section (mono caps heading, numbered teal-prefixed entries with URLs)

These are scaffolding cues. The analytical prose inside them is what changes between issues.

## Editorial non-negotiables

These are the rules Sri has explicitly pushed back on in past calibration. Violating them is the fastest way to get a draft rejected.

1. **No em-dashes in reader-visible prose.** En-dashes okay for number ranges (5–7%) and date ranges (April–May 2026) only.
2. **No mirror-construction sentences except at thesis moments.** "X is Y. Z is W." patterns read as AI-prose unless they're earning emphasis at the actual thesis statement. One per piece, maximum.
3. **No sentence-fragment triads.** "Concrete. Specific. Named." reads as AI. Use commas or full sentences.
4. **No "simply"+ mystery construction.** "It is simply X" reads as AI hedging. State the thing.
5. **No trailing rhetorical flourishes.** "And that is the story." / "That is the question." — cut these.
6. **No promotional language for aarnâ.** The IN PRACTICE sidebar is observational, not a sales pitch. "aarnâ is built around exactly that question" not "aarnâ solves this problem".
7. **No naming specific companies as negative examples.** Sri does not publicly call out specific protocols or individuals, especially potential future podcast guests. Critique the pattern, not the entity.
8. **No hashtags. No emojis. No call-to-action language.** ("Subscribe", "Stay tuned", "Don't miss" — never.)

See `references/editorial-voice.md` for the full pattern library with examples of each violation and its fix.

## Quality bar

A draft is ready when:

- Every statistic has a superscript reference linking to a primary source with URL and date
- The thesis stated in the dek is the thesis the piece actually argues (not a topic label)
- A reader could follow the argument without ever knowing there was a podcast involved
- The pull quote, if used, sits in the second half and supports the analysis rather than driving it
- The aarnâ mention is one sidebar, not threaded through paragraphs
- The piece would survive the test: would a Galaxy Research analyst publish this? Would a treasury allocator forward it to colleagues?

If any of these fail, revise before presenting.

## Important behaviours

### Don't skip the research gate

Even if Phase 1 produces a thesis that feels obviously correct, do not draft on what you already know. The whole point of the skill is that the newsletter is primary-sourced. Skipping the research gate produces a piece that *sounds* researched but is built on training data — and Sri will spot it immediately because the specific numbers and sources won't be there.

If the user pushes back ("just draft it, you have enough"), respond: "I want to run one Gemini pass first — without it the citations will be soft and the piece reads as opinion not research. It's 10 minutes of your time on Gemini and the draft will be much stronger." Then output the Gemini prompt.

### Don't over-format Phase 1 output

Phase 1a should feel like options on a table, not a formal brief. The 4-field format for each thesis is tight; each field is 1-2 lines, not a paragraph. Akshay is glancing across 2-3 options to pick — not reading a presentation. No headers like "Overview" or "Plan", no bulleted preambles, no closing summary. Just the labelled thesis cards and the one-line ask.

Phase 1b should feel conversational. A short paragraph confirming the choice, then the prompt in a code block. Do not produce a structured plan, an outline, or a "Plan for the newsletter" section.

### Handle the no-transcript case

If the source is a topic or theme without a transcript, the structural changes are:
- The pull quote is optional. If the deep research surfaces a strong primary-source quote (a SEC filing line, a CEO statement on a public earnings call, an academic paper's load-bearing sentence), use it. If not, skip the pull quote section entirely and let the chart or a key statistic do that visual work instead.
- The podcast plug footer is omitted or replaced with a thematic close.
- Everything else (zoom-out, research, draft) is the same.

### Issue numbering

If the user specifies the issue number (un#52, un#53, etc.), use it. If not, ask once at the end of Phase 1 ("which issue number is this — un#52?") and don't ask again. If the user doesn't answer, use a placeholder `un#NN` in the draft so they can find-and-replace later.

### File naming

Final HTML file: `un<N>_<slug>.html` where slug is 3-6 lowercased words from the title joined by underscores. Examples:
- `un51_permissionless_isnt_symmetric.html`
- `un52_when_oracles_lag.html`
- `un53_the_governance_layer.html`

Save to `/mnt/user-data/outputs/`. Always call `present_files` after creation.

## Reference files

- **`references/template.html`** — The canonical un#51 v3 HTML. Read this in full before drafting; it contains all CSS, all structural elements, and the working pattern for hero banner, section banners, subheadings, pull quote, sidebar, chart, and references list. The new draft should copy the CSS verbatim and follow the structural pattern element-for-element.

- **`references/editorial-voice.md`** — The voice rules in full. Read before drafting. Contains banned phrases, AI-tell patterns with examples and fixes, the Sri calibration history, and worked examples of voice failures and recoveries.

- **`references/gemini-prompt-format.md`** — How to construct the Gemini Deep Research prompt. Read when entering Phase 1 or when emitting a follow-up prompt in Phase 2. Contains the prompt template, worked examples for both transcript-based and theme-based sources, and patterns for asking for counter-evidence.

## The standard, restated

A Galaxy Research analyst reading the finished newsletter would not be able to tell it was generated from a podcast transcript. They would see a primary-sourced thesis-driven piece that uses one supporting quote in the second half and treats it as evidence among twenty other citations.

That is the bar.
