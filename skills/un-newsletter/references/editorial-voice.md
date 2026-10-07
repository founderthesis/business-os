# Editorial voice guide — un#

This file is the working calibration of Sri Misra's voice for the un# newsletter. Read it before drafting. It encodes patterns Sri has explicitly pushed back on, with examples and fixes.

## The voice in one paragraph

Observation-first. Concrete before abstract. Short standalone sentences alternating with longer paragraphs. Plain language for big ideas. Sceptical of generic frameworks. Trusts the reader's intelligence. Builder's discipline visible in the prose — the writer has clearly operated something and is talking about what they have seen, not what they have read about.

Reference for tone outside the publication: thiccy's "time is event based" essay (Scimitar Capital Substack). Galaxy Research's longer pieces. NOT Bankless newsletter, NOT generic crypto-Twitter analysis, NOT McKinsey-style framework decks.

## AI-tells — banned patterns

### 1. Em-dashes in reader-visible prose

Never use the em-dash (—) in body prose. It is the strongest single signal that a piece is AI-generated. Use a comma, a period, or a parenthetical instead.

Acceptable: en-dashes for number ranges and date ranges only.
- `5–7%` ✓
- `April–May 2026` ✓
- `Talos provides infrastructure — from major banks to small funds — and...` ✗
- `Talos provides infrastructure for trading desks ranging from major banks down to small funds, and...` ✓

### 2. Mirror-construction sentences

The pattern: short sentence stating X. Short sentence stating not-X or related-X. Often paired in immediate succession.

- `Audits establish a baseline for code correctness. They do not guarantee system resilience.` (un#50 — Sri-rejected pattern)
- `Yield isn't just return. It's embedded risk.` (un#50 — same)
- `The volume is real. The committed capital is not.` (would be rejected)

Mirror construction is allowed exactly **once** per piece, and only when it lands the thesis at the moment of maximum analytical weight. Example from un#51 that survives:

> Open interest cannot be wash-traded without incurring real capital costs. Volume can.

This works because the contrast carries the thesis (committed capital ≠ headline volume) and earns the mirror.

Default fix: collapse to one sentence with a relative clause, or expand into a longer flowing sentence.
- Bad: `Audits establish a baseline. They do not guarantee resilience.`
- Fix: `Audits establish a baseline for code correctness without guaranteeing system resilience.`

### 3. Sentence-fragment triads

The pattern: three single-word or two-word fragments separated by periods, used for rhythm.

- `Concrete. Specific. Named.` ✗
- `Open. Permissionless. Composable.` ✗
- `It doesn't break. It doesn't bend. It doesn't ask.` ✗

This reads as AI-generated prose every time. Replace with a flowing sentence using commas.

### 4. Trailing rhetorical flourishes

The pattern: a closing line that restates the obvious for dramatic effect.

- `And that is the question.` ✗
- `That is the story.` ✗
- `That is the bet.` ✗

These are AI-prose tells. Cut the sentence. The reader already knows.

### 5. "Simply" + mystery construction

- `It is simply X` ✗
- `The answer is simply Y` ✗
- `What this really means is simply...` ✗

"Simply" is hedging that pretends to be confidence. Cut it.

### 6. Trailing "depends on" softeners

- `Whether X is a feature or a bug depends on which problem you weight more.` (this is the un#51 close to "what design can still do" section — it works because it earns the qualification by acknowledging a real trade-off)
- `Whether the future is X or Y depends on what we decide.` ✗ (vague, evasive)

Allowed when the trade-off is genuinely contested in the prose above. Banned when used as a vague graceful exit.

### 7. "It's worth noting that..."

Cut. The reader doesn't need to be told what's worth noting. Just note it.

### 8. "In a world where..."

Banned opener. Reads as McKinsey deck or AI-prose. Open with the concrete observation instead.

### 9. Adjective stacks

Three or more adjectives in a row.
- `the deeply researched, primary-sourced, analytically rigorous piece` ✗
- `the analytically rigorous piece` ✓

One adjective or none. The noun does most of the work.

## Word-choice patterns Sri has flagged

- **"algorithm"** is too reductive for AI / ML systems. Use "model", "system", or the specific technical term.
- **"machine"** is too mechanical for autonomous systems. Use "system" or name what it is.
- **"trader"** is too narrow for the DeFi-native audience. Use "participant", "counterparty", or the role (LP, market maker, allocator).
- **"users"** is acceptable but often improvable. "Retail counterparties", "the flow on the other side", "the addresses on the public mempool" — depending on context.
- **"crypto"** can be replaced with the specific (DeFi, on-chain, decentralised) where the distinction matters.

## Factual precision

Soften unverifiable specifics. Sri pushes back on numbers that overstate.

- `Five companies use this stack` ✗ (sounds precise but isn't sourced)
- `A handful of firms use this stack` ✓ (honest about the imprecision)
- `Approximately a hundred venues` ✓
- `100+ venues` ✓ (when sourced)
- `100 venues` ✗ (overprecise without source)

Never invent precision. The newsletter's authority comes from sourcing, not from confidence.

## Calling out companies and individuals

Sri does not publicly call out specific companies or individuals as negative examples. This is partly editorial taste and partly relationship management — many subjects are potential future podcast guests.

- `Aave's recent governance proposal demonstrates the pattern` ✗ (names a likely guest)
- `Recent governance proposals across major lending protocols demonstrate the pattern` ✓
- `A 2024 incident at <protocol X> showed...` ✗
- `A 2024 incident in the lending sector showed...` ✓

Critique the pattern, not the entity. Praise specific entities is okay (un#51 praises CoW Protocol explicitly for its batch auction model). The asymmetry is intentional: positive callouts build relationships, negative callouts burn them.

Exceptions:
- Companies that are squarely competitors or critics already (and not future guests)
- Companies cited as positive examples
- Companies whose actions are public record being referenced factually without judgement (e.g., "Hyperliquid launched HIP-3 in October 2025" — this is reporting, not calling out)

## Voice in section openers

Each section banner is followed by an opening line that does work. Three patterns that work:

### Pattern A: The concrete observation

> There is a twelve-second gap between when an Ethereum transaction is broadcast and when it lands in a confirmed block.

The opener describes a specific thing in the world. The thesis emerges from the observation.

### Pattern B: The thesis-in-disguise

> To see the gap, look at the toolkit on each side.

The opener tells the reader what the next paragraph is going to show them. Used sparingly.

### Pattern C: The pivot from the prior section

> This dynamic is not limited to the trading side.

The opener connects to what came before. Used when a section is extending a thesis rather than starting a new one.

Banned opener patterns:

- "In today's [adjective] [noun]..." ✗
- "The world of X is changing..." ✗
- "It's no secret that..." ✗
- "Many people don't realise..." ✗
- "Picture this:..." ✗
- "Imagine if..." ✗

These are all delay tactics. The first sentence should do work.

## Voice in section closers

Three patterns that work:

### Pattern A: The compression

> What is left in the public mempool is the flow that did not.

A single sentence that compresses the section's thesis into something quotable.

### Pattern B: The escalation

> The same pool, advertised at the same APY, returns radically different realised yields depending on whether the LP has institutional-grade tooling or not.

The section's evidence funnels into a single declarative claim.

### Pattern C: The pivot

> The composition of where institutional flow actually lands is no longer abstract. It is observable on a public order book.

Closes the section and sets up the next.

Banned closer patterns:

- Rhetorical questions ("What does this mean for the future?") ✗
- Sweeping universal claims ("This changes everything.") ✗
- Calls to action ("Allocators should consider...") ✗

## Voice in the IN PRACTICE sidebar

The sidebar is the only place aarnâ appears in the body. It is ~50 words, written as a treasury-allocator observation that lands on the aarnâ approach without selling it.

Three principles:

1. **Frame it as a question the prior section left open.** The sidebar answers "given what we've just argued, what does a treasury actually do?"
2. **Describe what aarnâ is, not what it claims.** "Built around exactly that question: capital deployment as continuous optimisation under enforceable constraints" — describes the design. "Built to solve DeFi yield" — sells a benefit. The former works; the latter doesn't.
3. **One link at the end. No call-to-action.** "Read more at aarna.ai" or similar. Never "Sign up", "Try now", "Get started".

The sidebar from un#51 as exemplar:

> For treasuries deploying stablecoins into DeFi yield, the question this leaves is no longer simply *what is the APY*. It is what flow the pool sits across from, what execution model the protocol uses, and what mechanism inside the protocol reintroduces symmetry against more sophisticated counterparties. Pools without a defensible answer to those questions are not safer for being decentralised. They are simply more opaque about who is paying whom.
>
> **aarnâ** is built around exactly that question: capital deployment as continuous optimisation under enforceable constraints, with concentration caps, liquidity-aware sizing, pre-simulated execution, and full on-chain logging. The vault is not smarter than the institution on the other side of the trade. It is bound by rules that prevent the same disadvantage from compounding silently. Read more at [aarna.ai](https://aarna.ai).

Note: the first paragraph is the *editorial framing* (the question), the second paragraph is the *product description* (what aarnâ does). The reader can stop after paragraph one and the analytical piece still resolves. Paragraph two is for the reader who wants to know what aarnâ does about it.

## The Galaxy Research benchmark

When evaluating a draft, ask: would a Galaxy Research analyst publish this under their own name?

Galaxy pieces:
- Open with a concrete observation, not a framework
- Cite primary sources extensively, secondary sources only for context
- Acknowledge counter-evidence explicitly
- Use one chart where data shape is the punchline
- Close with a thesis-restatement that earns the position
- Never call to action

If the draft fails any of these against the Galaxy benchmark, revise. The aarnâ newsletter is positioned as research-grade analysis, not crypto-Twitter takes.

## The Sri calibration history (for context)

Past iterations of newsletter prose have failed in patterns worth knowing:

- **The "Paul Graham style" failure:** Trying to apply PG's voice to crypto analysis produced prose that was too declarative and not enough data-grounded. PG works in essays, not in research notes.
- **The "Walter Isaacson style" failure:** Trying to apply a biographer's voice produced prose that personified protocols and over-narrativised events. Sri rejected the romanticism.
- **The un#50 pattern failure:** Aphoristic claims without sourcing, mirror-construction throughout, generic framework-feel ("risk lives in incentives"), product CTA at close. Sri's calibration since has been deliberately away from this register.
- **The "five companies" failure:** Specific numbers that weren't actually sourced. Sri sees these instantly. Always soften to "a handful" or cite.

The current target voice (post-calibration) is closer to: Galaxy Research's long-form, with thiccy's tonal restraint, with a builder's matter-of-fact register from Sri's Milk Mantra operating background.

## When in doubt

Cut. The voice is restrained. The publication earns authority by not overclaiming, by not over-styling, and by letting the citations carry the weight. If a sentence feels clever, ask whether it's earning its cleverness. If it isn't, cut it.
