# Search + AEO reference

Everything here is measured from Google Search Console for founderthesis.com,
not guessed. The whole reason the article follows a structure is that search is
~40% of the site's traffic and it's the growth lever.

## What people actually search (the query patterns)

Traffic comes from **founder and company name searches**, almost always with a
*fact modifier*. Real queries pulled from Search Console:

- `[founder name]` and `[founder] [company]`
- `[company] owner` · `[company] owner name` · `who is the owner of [company]`
- `[founder] net worth`
- `[company] revenue` · `[company] valuation` · `[company] business model`
- `[founder] wikipedia` · `[founder] family` · `[founder] iit delhi` (background)
- `[company] ceo` · `[company] ceo name`
- `[founder] story`

**Implication:** the answer-first fact block at the top of the article must
front-load exactly these — the owner's full name, net worth / wealth if known,
revenue, valuation, funding, business model, and background. If the reader
searched "who is the owner of Foxtale", the first two sentences should answer it.

## Title formula (measured)

Comparing the top 60 articles by non-email views against the rest:

| Feature | Winners | Rest |
| --- | --- | --- |
| Colon in title | 58% | 30% |
| Contains a number | 40% | 19% |
| Money figure (₹/$/crore) | 32% | 13% |
| Old `Title \| Company` format | 27% | 56% |

These features help, but the team's rule (Nov 2026) comes first: **under 10 words,
curiosity-led and true**, e.g. `The Billion-Dollar Niche Nobody in India Noticed`.
Use a colon, number or money figure where it fits naturally. The pipe format is the
single strongest predictor of a *low*-traffic article — avoid it.

Good: `Arjun Vaidya's ~₹144 Crore Exit: Revitalizing a 150-Year-Old Brand`
Bad: `Building the SUV of scooters | River`

## Subtitle = the Google snippet

Substack has no separate meta-description field. It uses the subtitle, or (if
blank) the first line of the body. So **always** write a subtitle: one sentence,
under 155 characters, with the company + a hard number + the outcome. Make
someone click.

## AEO — getting quoted by AI answer engines

Two halves:

- **Google AI Overviews** — FT already surfaces here well; nothing special needed
  beyond ranking on Google.
- **External LLMs (ChatGPT / Claude / Perplexity)** — FT is weak here. Substack
  blocks the technical levers (no llms.txt, no custom schema), so AEO lives
  entirely in how the article is written:
  - **Answer-first fact block** — clean, quotable factual opener.
  - **Entity clarity** — full name + company + role, stated and repeated.
  - **Editorial H2s that name the entities** — no search-phrase or question headings; the answer goes in each section's first sentence.
  - **Sources section** — outbound authoritative links make the page look like a
    corroborated reference, which is what these engines cite.
  - **Self-contained facts** — every figure in the text; LLMs don't watch embeds.

These aren't separate SEO chores — they're the same structure that also wins the
Google snippet and the human reader.
