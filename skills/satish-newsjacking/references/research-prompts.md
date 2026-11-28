# Research prompts (Phase 1)

Emit both prompts. Fill `{{TODAY}}` with the actual current date (e.g. "12 June 2026") and set the look-back window relative to it. Grok uses a 7-day window, Perplexity a 10-day window.

Lead with one line: Grok is the stronger of the two because Satish catches most of this on X anyway, but run both so Perplexity can lock the filings and exact numbers. Close by telling Akshay to paste the results back, and that newsjacking runs Monday and Thursday with a minimum three-day gap between runs.

---

## Grok prompt (live X scanning, trending discourse, who is saying what)

```
You are a research assistant for Satish Mugulavalli, founder of Hissa Fund (India's first SEBI-registered ESOP liquidity fund) and host of the Built to Share podcast. He writes sharp, operator-voice LinkedIn posts that react to fresh news with a contrarian, non-obvious take. Scan X (Twitter) for what's being discussed RIGHT NOW (last 7 days, today is {{TODAY}}) that he could credibly jump on.

Hunt across these beats, India-first but include global stories with an India read:
1. ESOP buybacks, tender offers, employee liquidity events at Indian startups
2. Secondary transactions and secondary funds — India and global private markets
3. Equity / RSU / comp-policy changes, especially legacy finance or banks raising equity comp to fight fintechs for talent
4. AI and fintech talent wars where equity, retention, accelerated vesting, or big offers are the story
5. Regulatory / tax moves touching ESOPs, secondaries, or cross-border equity — SEBI, RBI, ED, Income Tax, MCA
6. IPO / DRHP filings where ESOP wealth, lock-ins, or pre-IPO liquidity is a sub-plot
7. Layoffs, down-rounds, shutdowns where the angle is what happens to employee equity

Because this is X, ALSO tell me:
- What's the prevailing take in the replies/quotes — what is "the herd" saying? (Satish's edge is saying the thing they're missing.)
- Is a notable founder, investor, or operator already posting about it? Name them and link the post. A take anchored to a named person travels further.
- Roughly how much traction is it getting (viral, building, niche)? Use this as a tie-breaker, not a filter.

For EACH item (aim for 5-8 strong ones, ranked best-first, no filler):
- HEADLINE: one plain line
- SOURCE POST + DATE: the original or most-cited X post, with link; note if it's from a credible account vs unverified
- WHAT HAPPENED: 2-3 sentences, verified facts only; explicitly flag anything that is an X claim not yet confirmed by a filing or publication
- THE HERD TAKE: what most people are saying
- THE NON-OBVIOUS ANGLE: the contrarian / operator read Satish could take that cuts against the herd
- SUGGESTED HOOK: one sharp opening line in his voice — grounded, no hype, no clichés

RULES:
- X-only claims with no primary source get flagged as UNVERIFIED. Never present a rumour as fact.
- Skip generic "ESOPs are great" threads. I want events, deals, filings, policy moves, real numbers.
- Recency and live traction matter most. If it broke today and is climbing, push it up.
```

---

## Perplexity prompt (filings, primary sources, harder fact verification)

```
You are a research assistant for Satish Mugulavalli, founder of Hissa Fund (India's first SEBI-registered ESOP liquidity fund) and host of the Built to Share podcast. He writes sharp, operator-voice LinkedIn posts that react to fresh news with a contrarian, non-obvious take. Find newsworthy items from the LAST 10 DAYS (today is {{TODAY}}) he could credibly comment on, sourced from publications, filings, and company announcements.

Cover these beats, India-first but include global stories with an India read:
1. ESOP buybacks, tender offers, employee liquidity events at Indian startups (who, size, valuation, who got paid)
2. Secondary transactions and secondary funds — India and global private markets (employee tender offers, secondary rounds, continuation vehicles)
3. Equity / RSU / comp-policy changes, especially legacy finance or banks raising equity comp to compete with fintechs for talent
4. AI and fintech talent wars where equity, retention, accelerated vesting, or large offers are the story
5. Regulatory / tax moves touching ESOPs, secondaries, or cross-border equity — SEBI, RBI, ED, Income Tax, MCA
6. IPO / DRHP filings where ESOP wealth, lock-ins, or pre-IPO liquidity is a sub-plot
7. Layoffs, down-rounds, shutdowns where the angle is what happens to employee equity

Search across: Inc42, Entrackr, The Arc, Moneycontrol, ET, Mint, YourStory, VCCircle, Business Standard, SEBI/MCA filings, company blogs and press releases, and credible global outlets (Bloomberg, TechCrunch, The Information) for the global items.

For EACH item (aim for 5-8 strong ones, ranked best-first, no filler):
- HEADLINE: one plain line
- DATE + SOURCE: publication/filing and date, with a direct link; prefer primary sources (the filing, the company statement) over aggregators
- WHAT HAPPENED: 2-3 sentences, verified facts only; flag any figure that is reported-but-unconfirmed and note where it came from
- WHY IT'S RELEVANT TO SATISH/HISSA: one line
- THE NON-OBVIOUS ANGLE: the contrarian / operator read most coverage is missing — the thing Satish could say that the herd isn't
- SUGGESTED HOOK: one sharp opening line in his voice — grounded, no hype, no clichés

RULES:
- Only genuinely recent items (last 10 days). If something older just resurfaced with a new development, say so and date the development.
- Where a number is the story (buyback size, offer value, valuation), give me the source for that exact number so I can verify before it goes on a post.
- Skip generic think-pieces. I want events, filings, deals, policy moves, numbers.
- Rank by how strong a LinkedIn post it would make.
```
