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
  editor to choose from, plus at most 3 motion visualisations that can stand
  alone as a short or clip, then a curated recommended list below it (no
  basic-English terms, 90 seconds between explainers, nothing in cuts).
---

# Founder Thesis — lower thirds and B-roll

The editor needs a list, in order, of every moment where a viewer would be lost without help, and what to put on screen at that moment, then a short recommended list of what should actually go on screen.

**Assume a mature audience that knows basic business words** (revenue, profit, startup, investor, funding). Leave only those out. Every other technical term, acronym, finance or industry term, insider phrase, brand, company, fund, product and named person gets a row. The editor picks what goes on screen; this skill's job is a complete list.

## Inputs

- **Transcript with timestamps** (required). Without timestamps this skill cannot do its job — ask for them.

## Output format

Two parts, in this order: the full table, then the recommended list below it.

### Part 1: the full table

One table, ordered by timestamp:

| Timestamp | Term / phrase | Lower third text or B-roll |
|---|---|---|

- **Timestamp** — precise, where the term is *first* used
- **Term / phrase** — the specific jargon, acronym, brand, or person
- **Lower third text or B-roll** — either a short plain-English definition, or the visual to cut to

Each cell in the third column starts with a type word:

- `LT:` a one-line plain-English definition, under 15 words
- `Visual:` the logo or photo for a brand, company, fund, product or person
- `VIZ:` a motion visualisation. At most 3 per episode, only where the moment can stand alone as a short or clip. Name that short or clip in the cell. No other data, text or motion graphics. A VIZ shows a flow that needs motion to be understood: money or ownership moving through steps, a clock or sequence, a before-and-after mechanism, or a screen recording such as a scroll of the company's own website (for example its fund list, to show how many funds it runs). Never a static fact dressed up as motion: a donut of where assets sit, a counter, a number card or a dot grid is too simple. Choose for gravitas: educational, never promotional (hide prices, yields and sales lines in any screen recording).

**Leave out housekeeping cuts entirely.** A housekeeping cut is a segment that is clearly coming out: technical issues (a frozen call, "can you hear me", reconnecting), mic and camera checks, talk before or after the recording, breaks, retakes and restarts of the same question, and anything said off the record. Take them from the cut list's "Pre-roll / housekeeping" entries (episode-tightener), plus any segment that matches this list. No row for any term that appears only inside one. If the term comes up again later, give it its row at that later first use.

Mark with † any row whose timestamp falls inside any other cut proposed in the cut list (an editorial call the editor may overrule).

### Part 2: the recommended list

Below the full table, under the heading "Recommended list", a second table of what should actually go on screen, picked from Part 1 and ordered by time: `# | Time (raw / rough cut) | Type | Term | On-screen text or brief`. Then a short "Left out, by rule" list naming what was dropped under each rule, so the editor can overrule. Curate by these rules (Akshay, 26 Nov):

- **No basic English.** Leave out any term a general reader already understands from plain English, even if it is finance vocabulary: broker-dealer, sandbox, bank fragility, mutual fund, yield, harmonization and the like. Keep true jargon, acronyms, named laws and regulators.
- **At least 90 seconds between explainers,** start to start, measured on the final cut (after the proposed cuts come out, so two items either side of a cut count as close). A VIZ counts from its end. Name supers are not explainers; hold them alone for the first 90 seconds. When two compete, keep the one with more weight and fold the other into a VIZ caption, or place an LT at a later mention of the same term.
- **Nothing inside a cut:** no item inside a housekeeping cut or any proposed cut.
- **Visualisations by the Part 1 VIZ rule:** flows that need motion, screen recordings, gravitas. Drop every simple one.

## Completeness check

Before you hand over, scan the transcript once more for acronyms (any run of capitals), numbers with units, and proper nouns. Every one that is not a basic business word must have a row at its first use outside housekeeping cuts. Expect well over 50 rows for a long episode (Mandar, 106 min raw: 151). Part 1 ignores spacing; Part 2 applies it.

## Hard rules

- **Never invent a definition.** If you are not certain what a term means in this context, flag it for the editor rather than guessing.
- **No em dashes.**
- Plain language. If the definition needs its own definition, rewrite it.
- Do not annotate the whole transcript. Only what a viewer would actually stumble on.

## Lessons
- 2026-11-26: "things which are clearly cut like housekeeping cuts should not be included in lowerthird" (Ranjita, via the Episode copywriter chat; Cleanup clear, decision 682).
- 2026-11-26: "I need a recommended list below the full list": no basic English ("broker dealer, sandbox, bank fragility - these are basic english terms"), no two explainers within 90 seconds, nothing in the housekeeping cuts, and visualisations that "need motion to demonstrate", like "the website scroll of their funds", with "gravitas in our selection of visualisation - educational rather than promotional", never "very simple ones" such as a two-thirds-of-AUM split (Akshay, in the Ryan Louvar copy doc chat; Part 2 and the VIZ rule added).
