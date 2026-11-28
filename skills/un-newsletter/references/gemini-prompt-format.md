# Gemini Deep Research prompt format

The prompt is what the user pastes into Gemini Deep Research to surface the primary-sourced evidence the newsletter needs. The prompt should be substantial (300-500 words for an initial pass, 150-300 for a follow-up gap-filling pass). Short prompts produce shallow research.

## The standard structure

```
# Research request: [thesis title]

## The thesis I'm exploring

[2-3 sentence statement of the analytical claim. Write this as a declarative thesis, not a question. The Gemini agent should know exactly what claim it's gathering evidence for.]

## Why this thesis matters now

[2-3 sentences on what makes this timely. References a recent event, a market shift, or a structural change that makes the thesis worth arguing in 2026.]

## Background context (what I already know)

[Brief bullet list of established facts so Gemini doesn't waste research time re-establishing them. This shapes the search toward what's genuinely unknown.]

## Specific data and sources needed

### A. [Topic area 1]

1. [Specific data point — what figure, what source type preferred]
2. [Another data point]
3. [...]

### B. [Topic area 2]

1. [...]
2. [...]

### C. [Topic area 3]

[Continue for as many topic areas as the thesis requires. Usually 3-5 areas.]

## Counter-evidence requested

What is the strongest case against this thesis? Specifically:
- [Named critics or contrasting analyses to find]
- [Specific data points that would refute the claim]
- [Alternative framings that other analysts have used]

## Recency requirements

- Prefer sources from [last N months — typically 6 to 12]
- Flag if forced to cite older data
- Note any data points that may have updated since cutoff
- Where time-series data exists, prefer the most recent observation with date

## Citation format

- URL and publication date for every figure
- Distinguish primary sources (company filings, official dashboards, peer-reviewed papers, regulatory disclosures) from secondary sources (aggregator articles, Medium posts, X threads)
- Where a figure is cited only via aggregator, dig to find the original
- Flag where primary source is unavailable so I know not to overstate
- Note disagreements between sources rather than silently picking one
```

## Worked example — Phase 1 prompt for un#51

Source material: Anton Katz / Talos interview on Unhashed. Thesis identified through the zoom-out move: permissionless ≠ symmetric — DeFi protocols are open but execution has bifurcated into two tiers.

```
# Research request: permissionless isn't symmetric — institutional vs retail execution in DeFi 2026

## The thesis I'm exploring

DeFi's protocol layer is permissionless and open, but its execution layer has bifurcated into a two-tier market. Institutional flow uses private mempools, smart order routers, and intent-based aggregators. Retail flow goes through the public mempool by default. The same Uniswap pool now serves two different execution surfaces depending on which side of the trade you're on. The asymmetry is structural, not adversarial.

## Why this thesis matters now

By 2026 the empirical record from the last 18 months has made the bifurcation visible in data. Flashbots Protect, MEV Blocker, BuilderNet, CoW Protocol, and intent-based aggregators have scaled to the point where their cumulative protected volume tells a clear story about who has migrated where. Perp DEX volume vs open-interest divergence on Hyperliquid and others provides another lens. The question is no longer whether the asymmetry exists, but how to characterise it precisely.

## Background context (what I already know)

- Ethereum has a ~12 second block time during which transactions sit in the public mempool
- MEV (maximal extractable value) extraction has been studied since ~2019
- Talos, GSR, Wintermute, Amber Group, Jump Trading are major institutional execution providers
- Flashbots Protect is the largest private-mempool service
- CoW Protocol pioneered batch-auction settlement
- Uniswap V2 vs V3 differ in concentrated liquidity design
- Loss-Versus-Rebalancing (LVR) is the formalised cost of being a passive LP

## Specific data and sources needed

### A. Institutional execution stack — venue connectivity and trade volume

1. Talos venue connectivity count (primary source: their docs or recent interview)
2. GSR Markets venue connectivity count
3. Wintermute venue connectivity count and inventory coverage
4. Amber Group daily trading volume and token coverage
5. Jump Trading compute infrastructure scale (number of nodes, simulations per day)
6. Cumberland (DRW) institutional OTC volume

### B. Private mempool / MEV protection adoption

1. Flashbots Protect cumulative protected volume (primary: their transparency report)
2. Flashbots Protect unique addresses served
3. Flashbots Protect transactions protected
4. MEV Blocker adoption figures
5. BuilderNet adoption figures
6. Daily MEV revenue on Ethereum 2021–2026 (primary: Flashbots dashboard)

### C. MEV / sandwich attack persistence on public mempool

1. Percentage of Uniswap V2 blocks containing front-runnable transactions (peer-reviewed source preferred)
2. Confirmed sandwich attack rate per block
3. Cumulative sandwich attacks identified across Ethereum DEXs
4. CoW Protocol's characterisation of MEV cost to traders (primary: cow.fi)

### D. LP-side asymmetry — LVR and realised yield

1. LVR as % of pool value annually across major AMMs (academic source)
2. Per-trade LVR figures
3. Realised LP returns on Uniswap V3 volatile pairs vs buy-and-hold
4. Algorithmic LP management performance vs static positions (Gamma Strategies or similar)
5. Stablecoin pool yields and LVR characteristics

### E. Perp DEX volume vs open interest divergence

1. Monthly perp DEX trading volume time series 2024–2026 (DefiLlama)
2. Hyperliquid market share of decentralised perp OI
3. Hyperliquid weekly trading volume and current OI
4. Aster, Lighter, edgeX OI/volume ratios — current snapshot
5. HIP-3 framework launch date and current OI
6. HIP-3 top markets by volume (tokenized RWA vs crypto pairs)
7. TradeXYZ market share within HIP-3

### F. Intent-based aggregators and design mitigations

1. CoW Protocol annual settled volume 2024 vs 2025
2. CoW Swap vs UniswapX vs 1inch Fusion market share
3. Solver concentration within CoW Protocol
4. Trade-offs cited by critics: settlement latency, solver centralisation, gossip network bypass

## Counter-evidence requested

What is the strongest case against the bifurcation thesis? Specifically:
- Arguments that the public mempool remains the dominant execution venue for sophisticated flow
- Data showing MEV decline reflects genuine reduction in extraction, not migration
- Analysts who frame the LP-side asymmetry as fixable through better tooling rather than structural
- Counter-arguments on the perp DEX OI/volume ratio (e.g., that low ratios reflect different market dynamics, not capital quality)
- Critiques of intent-based aggregators (centralisation concerns from BlockEden, etc.)

## Recency requirements

- Prefer sources from the last 6 months for figures that update frequently (perp DEX volume, OI, MEV revenue, intent aggregator share)
- Historical sources okay for foundational data (Wormhole exploit, sandwich attack academic papers)
- Flag any data point that may have updated since Gemini's last refresh
- For Hyperliquid figures specifically, note the date of the snapshot

## Citation format

- URL and publication date for every figure
- Distinguish primary sources (company dashboards, transparency reports, academic papers, official protocol docs) from secondary aggregators (TradingView, Cointelegraph, Medium)
- Where a figure is cited only via aggregator, dig to find the original
- Flag where primary source is unavailable
- Note where multiple sources disagree on a figure and surface both
```

## Worked example — Phase 2 follow-up prompt (gap-filling)

Suppose the first research pass came back strong on institutional execution and MEV but weak on the LP-side and perp DEX divergence. A follow-up prompt would look like:

```
# Follow-up research: LP-side asymmetry and perp DEX divergence

The earlier research established the institutional execution stack and the MEV migration story well. I'm coming back for primary-sourced figures on two specific areas where the evidence was thin.

## What I still need

### A. LP-side asymmetry — concrete numbers

1. LVR as a % of pool value annually — academic-source confirmation. CoW docs cited 5-7% but I need the underlying paper or methodology.
2. Realised LP returns on Uniswap V3 ETH/USDC vs buy-and-hold over a measurable window (60 days, 90 days, etc.). I need an actual study, not a forum post.
3. Stablecoin pool APY range at the 0.01% fee tier — current snapshot.

### B. Perp DEX volume and OI snapshot

1. Hyperliquid current OI (May 2026 if available; flag if I'm getting a March figure).
2. Hyperliquid weekly volume (current; confirm with DefiLlama or aotrading source).
3. OI-to-volume ratios for Aster, Lighter, edgeX — same snapshot date for all if possible.
4. HIP-3 OI trajectory — start of 2026 to most recent. I have $280M start and $2.47B mid-May but want the in-between points.

### C. HIP-3 markets composition

1. Top 10 markets by volume on HIP-3 as of April-May 2026. I have the headline ("7 of 10 are RWAs") but want the per-asset volumes for silver, WTI, Brent, gold, S&P 500, Nasdaq 100, individual equities.

## Recency

All of section B and C should be from April-May 2026 snapshots. Flag where I'm forced to use older data.

## Format

Same as before: URL + date for every figure, primary source preferred, flag where aggregator-only.
```

## Patterns to use

### State the thesis as a declarative claim, not a question

- `The thesis I'm exploring: permissionless protocols don't produce symmetric execution.` ✓
- `Is permissionless really symmetric?` ✗ (Gemini will search for both sides equally, not for evidence supporting the thesis)

### Group data requests by topic area, not by source type

Grouping by topic area (institutional stack, MEV data, LP-side) makes the research output easier to map back to newsletter sections. Grouping by source type (papers, dashboards, articles) doesn't help anyone.

### Ask for counter-evidence by name

"What's the strongest case against this thesis" is good. "What does Galaxy Research think about this" is better — Gemini will fetch named-source rebuttals.

### Always include a "background context" section

Without it, Gemini wastes research budget explaining Ethereum block times and what MEV is. With it, every result is at the depth Sri actually wants.

### Specify what counts as a primary source

In crypto, the hierarchy is roughly:
1. Official protocol docs, dashboards, transparency reports
2. SEC filings, formal regulatory disclosures
3. Peer-reviewed academic papers (especially financial economics journals)
4. Direct quotes in news articles from named principals
5. DefiLlama, Dune, Coin Metrics dashboards
6. Aggregator articles citing the above
7. Medium posts, X threads
8. Generic "industry reports" from non-domain publishers

The prompt should ask for the top three categories where possible.

## Patterns to avoid

### Don't ask for "everything about X"

- `Tell me everything about how DeFi execution works` ✗ — produces a textbook, not research
- `I need primary-sourced figures on the institutional execution stack covering venue connectivity, daily trade volume, and infrastructure scale for Talos, GSR, Wintermute, Amber, Jump, and Cumberland` ✓

### Don't ask for opinions

- `What do experts think about the future of DeFi execution?` ✗
- `Find named analysts who have argued specifically that the bifurcation is reversible or overstated` ✓

### Don't be vague about recency

- `Recent data preferred` ✗
- `For figures that update monthly (perp DEX volume, OI, MEV revenue), source from the last 60 days. For foundational figures (academic papers on LVR, the Wormhole exploit), older sources fine` ✓

### Don't include the source material verbatim in the prompt

If the source is a podcast transcript, don't paste the transcript into the Gemini prompt. The prompt is about the thesis, not the source. Cite the source briefly ("This research is for a piece informed by an Anton Katz interview, but the piece itself isn't about Talos — it's about the broader institutional execution pattern") if at all.

## Length calibration

- Phase 1 (initial pass): 300-500 words. Long enough to specify thesis, background, and 4-6 topic areas with detail. Short enough that Gemini doesn't run out of budget on the prompt itself.
- Phase 2 (gap-filling): 150-300 words. Focused on the specific gaps. Reference the earlier research briefly so Gemini knows what's already covered.

## When the user pushes back on the prompt

If the user says "this prompt is too long" — push back gently. Short prompts produce shallow research. A 500-word prompt is a 10-minute Gemini run; the alternative is a draft that gets rejected for thin sourcing.

If the user says "just include the transcript and let Gemini figure it out" — push back. The transcript anchors the research to the source instead of to the thesis. The result is a transcript summary with citations, not a Galaxy-grade analytical piece.

If the user says "I'll add my own questions" — let them. Their context will improve the prompt.
