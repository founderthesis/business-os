---
name: ft-episode-titles
description: >-
  Write the YouTube title for a Founder Thesis episode. Trigger on
  "/ft-titles", "FT titles", "YouTube title", "episode titles", "title
  options", "what should we call this episode", or whenever an FT transcript
  is supplied and the ask is for the title the episode is published under.
  Produces 8 search-shaped options with entity coverage and a recommendation,
  NOT a long list across psychological trigger styles - that approach was
  tested against the channel's own click-through data and found to do
  nothing. The title's job here is search and entity coverage; the thumbnail
  earns the click and is handled by thumbnail-copy.
---

# Founder Thesis — episode titles

## Read this before writing anything

The title is **not** the click lever. This was tested properly against the channel's own history: fifteen title features, measured against click-through after fitting out reach and publish date so that neither could masquerade as a title effect. Nothing cleared the bar. Colons, numbers, superlatives, "India", length, question forms, the `(Company)` construction — all flat. The strongest was a "How" opener at +12% on 27 episodes, which is inside the noise.

**What this means in practice:** the previous approach of generating 18-20 titles across six psychological trigger styles was expensive machinery aimed at a lever that barely moves. It is retired. Do not reproduce it.

**The thumbnail earns the click. The title earns the search.** YouTube search is 13.6% of the channel's views, and search is also the entire Substack strategy. So write the title as a search asset carrying the entities someone would actually type, and let `thumbnail-copy` carry the claim.

Current evidence lives on the FT Channel Rules page and supersedes this section: https://app.notion.com/p/3d219a301a7f813fa919fe4b6c48a72f

## Inputs

- **Transcript** (required)
- **Selected theme** (optional) from `ft-episode-themes`
- **Thumbnail copy** (optional) — if it exists, the title must not repeat it

## Output

Standalone use: **8 titles.** For each, note which entities it carries and what search intent it serves. Then recommend one and say why.

Inside the editing doc: no standalone list. Write one title per thumbnail the editor picked (thumbnail-copy step 2), in the table `# | Picked thumbnail | YouTube title | Chars | Keyword it targets`. All title rules here still apply (guest and company, no number not in the transcript, do not repeat the thumbnail copy), with the length band tightened to 60 to 70 characters.

Every title must carry as many of these as fit naturally:

- **Guest name** — people search founders by name
- **Company name** — the highest-intent term for this episode
- **Category or sector term** — "D2C", "fintech", "semiconductor", "quick commerce"
- **The specific number**, where there is a real one

## Title rules

1. **50 to 70 characters** including spaces. This is the band that survives on mobile and desktop.
2. **Do not open with the guest's name.** Lead with the idea, the tension, or the outcome; the name goes after a separator.
3. **Every title carries at least one high-intent search term** — guest, company, or sector.
4. **No em dashes.** Colons, commas, or simple dashes.
5. **No curiosity gap that the episode does not close.** A title that oversells produces a viewer who leaves at ninety seconds, which costs watch time — the metric that actually drives distribution.
6. **Do not repeat the thumbnail copy.** They are read together. If the thumbnail carries the claim, the title carries the entities and the specifics.
7. **Vary the structure.** Do not ship eight titles in the same shape, but do not manufacture variety for its own sake either.

## Spread across search intents, not trigger styles

Cover the different ways someone arrives at this episode:

- **Company search** — they know the company and want the founder's account
- **Founder search** — they know the name
- **Sector search** — they are researching the category, not this company
- **Problem search** — they have the problem the guest solved
- **Outcome search** — they want the number or the milestone

That is a coverage checklist, not a quota. Four intents served well beats eight served thinly.

## Hard rules

- **Every number in a title appears in the transcript.** Never round up, never borrow.
- The **$10M / ~₹80cr bar** applies: no sub-threshold figure headlines a title.
- **Accurate but generous.** FT hosted these founders. The title should be one they would find fair.
