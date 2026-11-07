# 10-row enrichment test (5 Nov)

Test of live web-search screening on cold FT outbound rows (Direction Outbound, Status New). Per-row results, names and source URLs are in `data/enrich_test/results.json` (git-ignored).

## Cost

- Total USD 0.378 for 10 rows, about USD 0.038 a row. Cap was USD 5 and USD 0.065 a row.
- One row went over the per-row cap (USD 0.072); the other nine were USD 0.022 to 0.050.
- First attempt failed on all 10 rows at no cost: the sandbox no longer allows the web fetch tool, so the run used web search only (1 to 2 searches a row, capped at 3).

## Results

- 9 keep, 1 kill. Confidence: 5 high, 4 medium, 1 low.
- Every row came back with 1 to 4 source URLs (23 in total), each with a stated fact.
- Failures: 0 on the final run. No row was unparseable or empty.

## Quality notes

- Strong where the company is large and covered by press: the unicorn and listed cases came back high confidence with revenue and valuation sources.
- Weaker on the borderline growth-stage cases: revenue figures come from estimate sites (Owler, Latka, Tracxn bands), and two keeps are explicitly "lift" cases below the USD 50M revenue bar. They need a human call, not an automatic keep.
- The kill case was reasoned from a revenue band that straddles the bar, so it is a judgement, not a clear miss.
- One company was described as Series B+ when its sources show a Series A; the reason line says borderline.
- No row wrote to Notion.
