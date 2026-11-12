---
name: ft-working-doc
description: 'Build the Founder Thesis copy doc for an episode in one pass: eight tabs in a fixed order (Overview, AD thought leadership, AD release post, Guest posts, Guest company posts, LI newsletter, Substack article, Fact-check), for every episode whatever its tier. Trigger on "/ft-doc", "run the working doc", "build the copy doc", "full episode pack", "everything for this episode", "the whole doc for this guest", or whenever an FT transcript is supplied with an open-ended ask for the episode''s copy. This is an ORCHESTRATOR: it invokes the individual FT skills and assembles their output into the copy doc. It does not duplicate their rules.'
---

# Founder Thesis — the copy doc, end to end

One transcript in, the episode's copy doc out: one Claude Doc, one tab per
output, built the same way for every episode. The standard was set by Ranjita on
9 Nov 2026 (decision 527, plan: https://claude.ai/artifact/GvMYdptw8P9KNxq8t7XKgT;
model doc: the Rohit Manglik @ InfoBay.AI copy doc).

**This skill conducts. It does not write the rules.** Each tab below comes from a
real skill, and that skill's own instructions govern its output. Load and run
them; never inline or paraphrase their rules here.

## Before starting

1. **Episode row** in the Notion Episodes database
   (collection://5d250752-6db8-4ab6-8467-c68f5838278a). Read:
   - the **Transcript file**: download it fresh and read all of it, never a preview.
     Timestamps are required for fact-check references; without them, say so and run the rest
   - the **Engagement**: guest restrictions, edit notes, anything marked
     unpublished, and every Activity whose Summary starts "Edit notes:". A cut
     segment never appears in any copy
   - the **Dossier link**, if it can be opened
2. **Read the FT Channel Rules page:**
   https://app.notion.com/p/3d219a301a7f813fa919fe4b6c48a72f
   It carries the current performance evidence and supersedes any skill it
   contradicts. Note the date of its last run in the Overview.
3. **Research** (decision 531): look the company up on Tracxn (funding, investors,
   revenue, headcount, competitors), and read the guest's and the company page's
   recent LinkedIn posts with Apify. Write both up in the Overview tab, with what
   each copy tab can use. Tracxn figures are cited "Source: Tracxn" (decision 532).
4. **Episode link**: use `[episode link]` until the episode is live.

## No checkpoints

Run every tab in one pass. Where a skill asks for a pick (a theme, a voice), take
the recommended option, say so in the Overview, and carry on. Ranjita reviews the
finished doc with comments; nothing waits on an answer mid-run.

## The tabs, in this order

| # | Tab | Skill | What it holds |
| --- | --- | --- | --- |
| 1 | Overview | none | Episode facts, the Tracxn and LinkedIn research, sources read, restrictions and edit notes applied, picks made in the run, open questions |
| 2 | AD thought leadership | `ft-episode-themes` for the ideas | A "Your posts" section left blank for Ranjita, then post ideas: each a riches-in-niches angle, an Indian comparison and transcript timestamps. Posts Akshay asks for later go below as drafts (`ft-linkedin-post`, host variant) |
| 3 | AD release post | `ft-linkedin-post` (release post variant) | Three short options to go out with the trailer |
| 4 | Guest posts | `ft-linkedin-post` (guest variant) | Type 1 repost captions A, B, C paired with release options 1 to 3, and D for any; Type 2 a standalone post with the trailer attached; instructions for the guest on each; alternates |
| 5 | Guest company posts | `ft-linkedin-post` (company variant) | The same two types for the company page, with instructions for the page admin |
| 6 | LI newsletter | `ft-episode-themes` for the ideas | A "Your deep dive" section left blank for Ranjita, then deep-dive ideas. When asked to draft, run `ft-newsletter` |
| 7 | Substack article | `ft-substack-article` | Ready to publish, with only the title left to pick |
| 8 | Fact-check | `fact-check` | Every claim in tabs 2 to 7, its transcript timestamp or source, and the verdict |

Run `ft-episode-themes` once and split its output: themes best suited to a
LinkedIn post become the post ideas in tab 2; themes best suited to 1,000+ words
become the deep-dive ideas in tab 6. There is **no Themes tab** and **no Decisions
log tab**: decisions go in the plan doc's log.

## Not in the copy doc

Everything for YouTube (decision 564, Akshay, 12 Nov): show notes and the YouTube
description with chapters, YouTube and Spotify titles, thumbnail copy. They live in
the episode's editing doc. Also not here: the cinematic title, the host intro,
shorts, the trailer edit, the cut list, lower thirds and editor notes. They run as
separate steps (decisions 501, 526, 527, 564), so this skill does not call
`ft-show-notes`, `ft-episode-titles`, `thumbnail-copy`, `ft-cinematic-title`, `ft-host-intro`,
`ft-lower-thirds`, `episode-tightener` or `shorts-finder`. Run them only when asked
directly.

## Writing rules every tab follows

- **Audience:** urban, Indian, white collar, ambitious hustlers inspired by Shark
  Tank who want to learn about business niches.
- **Riches in niches:** the guest and the company are the case study. Explain the
  tech and the model plainly, and compare with an Indian brand or model the reader
  knows.
- **Read like a person wrote it:** take a stand, lead with a thesis; Akshay's
  pieces are in the first person; nothing that reads as written for a search engine.
- **Guest quotes as pull quotes,** edited for grammar only.
- **Figures** come from the transcript or the dossier. Market context comes from
  named public sources. Tracxn figures may be used, each cited as "Source: Tracxn"
  (decision 532).
- **Links:** published content (posts, the newsletter, the Substack article) can
  link to any source with no approval needed (decision 529). Mail still uses only
  the approved short links. Internal Founder Thesis links come from the Episodes
  database's Substack field and sit inside sentences.
- **House style:** no em dashes, sentence-case headers, no "it's not X, it's Y",
  no "delve", "leverage", "unlock", "robust" or "seamless".

## Building the doc

- One Claude Doc, named "<Guest> @ <Company> – copy", one tab per row above, in
  that order. Share it as editable by anyone with the link; the link stays
  internal and never goes to a guest or PR contact.
- Put its link in the Episode's **Copywriting doc** field (decision 526). Change no
  other Episode field: never Status, Copy done, Planned release or tier.
- **Formatting:** headings bold and coloured, teal for sections and recommended
  picks, purple for drafts and alternates; a horizontal rule between posts; the
  recommended option marked ★.
- Embed the Substack article's timeline graphic in tab 7 and hand over the PNG.

## Hard rules

- **Never fabricate to fill a tab.** If the transcript does not support something,
  say so in the Overview and leave it out.
- **Never invent a number or a quote.** Every figure traces to the transcript, the
  dossier or a named source.
- **Publish nothing, send nothing.** This produces copy. A human ships it.
- If a stage's skill is unavailable, say which one and continue with the rest
  rather than substituting your own version of its rules.
