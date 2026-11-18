---
name: ft-lower-thirds
description: >-
  Build the lower-thirds and B-roll plan for a Founder Thesis video episode:
  every piece of jargon, acronym, brand, person or statistic that needs an
  on-screen explanation or visual. Trigger on "/ft-lowerthirds", "lower
  thirds", "b-roll plan", "explainer text", "notes for editor", "what needs
  a graphic", "jargon list", or whenever an FT transcript is supplied and the
  ask is for on-screen support rather than copy. Produces a complete
  timestamped table of every technical term, brand and named person, for the
  editor to choose from, plus at most 3 data visualisations that can stand
  alone as a short or clip.
---

# Founder Thesis — lower thirds and B-roll

The editor needs a list, in order, of every moment where a viewer would be lost without help, and what to put on screen at that moment.

**Assume a mature audience that knows basic business words** (revenue, profit, startup, investor, funding). Leave only those out. Every other technical term, acronym, finance or industry term, insider phrase, brand, company, fund, product and named person gets a row. The editor picks what goes on screen; this skill's job is a complete list.

## Inputs

- **Transcript with timestamps** (required). Without timestamps this skill cannot do its job — ask for them.

## Output format

One table, ordered by timestamp:

| Timestamp | Term / phrase | Lower third text or B-roll |
|---|---|---|

- **Timestamp** — precise, where the term is *first* used
- **Term / phrase** — the specific jargon, acronym, brand, or person
- **Lower third text or B-roll** — either a short plain-English definition, or the visual to cut to

Each cell in the third column starts with a type word:

- `LT:` a one-line plain-English definition, under 15 words
- `Visual:` the logo or photo for a brand, company, fund, product or person
- `VIZ:` a data visualisation. At most 3 per episode, only where the data moment can stand alone as a short or clip. Name that short or clip in the cell. No other data, text or motion graphics.

Mark with † any row whose timestamp falls inside a cut proposed in the cut list.

## Completeness check

Before you hand over, scan the transcript once more for acronyms (any run of capitals), numbers with units, and proper nouns. Every one that is not a basic business word must have a row at its first use. Expect well over 50 rows for a long episode (Mandar, 106 min raw: 151). Spacing, timing and the first-90-seconds call are the editor's, not this skill's.

## Hard rules

- **Never invent a definition.** If you are not certain what a term means in this context, flag it for the editor rather than guessing.
- **No em dashes.**
- Plain language. If the definition needs its own definition, rewrite it.
- Do not annotate the whole transcript. Only what a viewer would actually stumble on.
