# Optional — Deep Research prompt for data-heavy thesis posts

Most Sri LinkedIn posts need only the Step 1 web searches. Use this **only** when the angle is a sophisticated thesis piece (tokenization, market infrastructure, India financial markets, GIFT City) and Step 1 surfaces a real research gap — load-bearing numbers that a few searches can't pin down to primary sources.

When that happens, hand Akshay a Gemini Deep Research prompt rather than drafting on soft ground, and STOP until he pastes the research back.

## Output format to Akshay

One short line naming the gap, then the prompt in a code block:

> The thesis leans on [specific numbers] and I can't pin those to primary sources from a quick search. Here's a Deep Research prompt — run it on Gemini and paste the result back, and the post will rest on solid figures.

```
[prompt here]
```

## Prompt template

```
I am researching for a thought-leadership LinkedIn post arguing the following thesis:

[ONE-LINE THESIS — the finance → DeFi reframe being claimed]

The audience is sophisticated but not crypto-native, largely Indian. I need primary-sourced evidence, current within the last 6 months where possible.

Find and cite, with source URLs and dates:

1. [The familiar-finance baseline] — the current state, size, friction, or cost of the mainstream-finance thing being reframed. Specific figures (market size, settlement times, minimum ticket sizes, fees, access rates).

2. [The on-chain / tokenized alternative] — current adoption, volume, TVL, named protocols or institutions, real figures, not projections.

3. [The India angle, if relevant] — GIFT City, SEBI/RBI position, Indian retail access data, rupee-rail or UPI-adjacent context that anchors the reframe for an Indian reader.

4. [Counter-evidence] — the strongest case against the thesis. Where the on-chain approach has failed, where custody or regulation remains an open problem, named examples.

For every statistic, give a primary source (company docs, regulatory filings, official dashboards, academic papers) over secondary aggregators. Flag any figure you cannot source primarily.
```

Fill the bracketed sections from the chosen angle. Keep the counter-evidence request in every time — Sri's honest-edge close needs the open questions, and a post that ignores them reads as a pitch, not thought leadership.
