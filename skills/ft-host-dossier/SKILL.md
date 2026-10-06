---
name: ft-host-dossier
description: 'Produce the Founder Thesis host dossier pack for Akshay Datt: an HTML dossier plus a ~500-word HTML guest prep note. Trigger on "ft-host- dossier", "/ft-host-dossier", "FT dossier for [guest]", "host dossier for [founder]", "prep me for [guest]", or a pre-call transcript/PR backgrounder upload. Single run: first checks Drive and Gmail for a pre-call transcript and PR mail chain, asking only if not found, then researches via web_search/web_fetch across five layers, drafts, copywriter pass, ships. Dark-mode HTML, sticky nav. Four acts: grounding, low point, mechanics, hard questions. Opens with a short business-in-the-stack explainer and a founder paragraph, not a chronological journey - a career timeline carries the dates. Snapshot and numbers cheat sheet sit after Themes, cheat sheet and sources collapsed into an appendix. Questions follow Akshay''s register per akshay-question-voice.md. Guest note never promises edit rights. Finishes by writing the Dossier link onto the guest''s Founder Thesis Engagement in the Business OS (Notion).'
---

# ft-host-dossier — Founder Thesis Host Dossier Pack

A pre-interview prep workflow for **Akshay Datt**, host of *Founder Thesis* (550+ episodes, The Podium). Guests are founders and operators, mostly India-connected. The show's promise: **learn how to analyse business strategy and tactics** through one founder's business.

## What this dossier is for

**The job is narrow:** give Akshay a one-sitting read that lets him run a hi-signal interview. He should finish it understanding the industry himself, knowing the numbers, and holding question clusters he can jump between. It is NOT a research study, a biography, or a script.

**Five operating principles:**

1. **Explain the business simply, in the context of the industry stack.** A short paragraph plus a simple stack diagram — what sits upstream, what sits downstream, which layer this company occupies. Not a five-part breakdown; that level of density is for the appendix or a specific theme, not the opening read.

2. **No chronological journey opener as prose.** The founder gets one brief paragraph (arc and stakes, not a CV), and the dates and detail live in a dedicated visual career timeline section right after it — including, where it's part of the tension, what happened to a past company after the founder left it.

3. **Dual audience, every theme.** A 20-year-old generalist must follow it AND a VC analyst must learn from it. Per theme: **101-level question → worked example → sharp pressure-test.**

4. **Curiosity, not cross-examination.** Akshay does not do gotcha interviews. Discrepancies are housekeeping notes, not the spine. The sharpest theme is a genuine puzzle the guest can argue, not an accusation he must survive.

5. **Verify before you print.** Stale valuations, funding totals and "bootstrapped forever" narratives are the most common inaccuracies. Where a founder's own statement conflicts with press, **flag the discrepancy, never average it.**

## Stage 0 — Find the pre-call materials yourself, before anything else

**Don't ask Akshay for this before you've looked.** Before starting research, search on your own:

1. **Google Drive** — search for the guest's name and company (e.g. `fullText contains '<Guest Name>' or fullText contains '<Company>'`) to find a Gemini pre-call transcript or planning-call notes. These typically outrank every other source on facts and agreed scope.
2. **Gmail** — search for the guest's name, company, and/or the PR agency if known, to find the mail chain that set up the recording (referral source, PR contact, recording date/time, any brief). This is where the meta-block details (referred by, PR contact) usually come from.

Only if both searches come up empty do you ask Akshay whether call notes or a mail chain exist and where to look. Don't skip straight to asking — a guest name alone is enough to go try Drive and Gmail first.

If you find a pre-call transcript, mine it fully: it outranks press and PR framing on facts, and it's also where you find the questions Akshay already asked this guest (a pre-call question that landed should usually be re-asked on the record) and any moment the guest visibly dodged (raw material for Act IV).

## Three things this skill exists to stop you re-litigating

All three were corrected by hand. They are hard requirements now.

### 1. The business explainer is short, prose, and simple — not the old five-part breakdown

The opening business section is a single short paragraph (roughly 80-120 words) plus a stack diagram, explaining where this company sits between what's upstream and what's downstream of it. If Akshay cannot answer "where does this business sit in its market" from that one paragraph and diagram, it has failed. It should NOT reproduce the old money-flow table, the market-pools bullet list, or the dated-shifts list inline — those went into the appendix or into individual themes, on purpose, because too much of that up front was the exact complaint that got this section rewritten.

### 2. Past appearances get inline clickable links

`Past appearances` lists every prior podcast, long-form interview or founder-led session, **each hyperlinked inline on the name**. A source that appears only in the Sources block is not enough. Also check the master guest sheet and state plainly whether they have been on Founder Thesis before.

Close the section with **the read**: how the guest interviews, which rooms were friendly, and what nobody has asked them yet. That last part is the argument for recording.

### 3. Every question is written in Akshay's register

**Read `references/akshay-question-voice.md` immediately before drafting themes. Not optional.** Questions drafted in neutral journalist-English get rewritten by hand every time.

Recalibrate against source material where available: the pre-call transcript found in Stage 0, and mine it for questions he has already asked this specific guest.

## Inputs

One or more of: guest name, LinkedIn URL, company name, a PR backgrounder or research export, a pre-call transcript (this outranks all secondary sources on facts and agreed scope), recording date, an angle Akshay has flagged.

A guest name alone is a complete input — go find the rest yourself (Stage 0, then research), don't wait for it to be handed to you.

Mine every upload FIRST, same as anything found via Stage 0's Drive/Gmail search. For `.docx`: copy to `/tmp/`, extract with `python-docx`, take paragraphs AND tables. Gemini and Zoom note files often ship as a summary doc plus a transcript doc; the transcript is the valuable one. Mislabeled PDFs that are really ZIPs: copy to `/tmp/x.zip`, unzip, read the numbered `.txt` files. PR framing often conflicts with what was agreed on the planning call; **defer to the planning-call transcript.**

## Outputs

1. **Host Dossier (HTML)** — `/mnt/user-data/outputs/<lastname>_ft_dossier.html` — **dark mode**: dark background, light text, one accent colour, a second accent for flags, sticky in-page nav, visual stat strip and career timeline. No light/white theme.
2. **Guest Prep Note (HTML)** — `/mnt/user-data/outputs/<lastname>_ft_guest_prep.html` — ~500 words, branded, warm, first-person Akshay. Base: `references/guest-prep-template.html`.

Then `present_files` with both, dossier first. Ship one dossier only; if a superseded format version sits in outputs, delete it.

## The workflow — one continuous run

Seven stages: **locate pre-call materials → research → gap-fill → draft → copywriter pass → ship → log in Notion**. No handoff, no waiting, no Deep Research prompt. Don't rush the research to reach the artifacts faster.

### Stage 0 — Locate pre-call materials (see above)

Search Drive and Gmail on your own first. Ask only if both come up empty.

### Stage 1 — Core research pass

Mine uploads and whatever Stage 0 found first. Then 12-16 targeted searches, adapted to the guest:

1. `"<Guest Name>" <Company>` — role, recent press
2. `<Company> FY26 revenue results financials` — adjust FY to latest
3. `<Company> funding valuation 2025 OR 2026` — round history, peak-vs-current gaps
4. `<Company> unit economics OR margins OR profitable` — the VC-analyst layer
5. `how <industry> companies make money revenue mix India` — feeds the business explainer
6. `<industry> regulation OR rule change India 2025 2026` — name the specific circular
7. `<industry> market size India stakeholders value chain`
8. `<Guest Name> podcast OR interview` — **run this properly, it feeds Past appearances and needs working URLs**
9. `<Company> competitors India` — the comparison set, with their numbers
10. `<Company> layoffs OR pivot OR down round OR co-founder exit OR controversy`
11. `<Legal entity name> Entrackr OR RoC filing FY25 FY26` — combine legal entity AND brand name
12. `<Guest Name> "we" OR thesis OR contrarian <Industry>` — verbatim quotes
13. `<Guest Name> prior venture exit OR acquired OR shut down`
14. For common company names: cross-reference Crunchbase, Tracxn, TheOrg, company site
15. If a founder left a prior company, search what happened to that company **after** they left — this is what makes the career timeline and Act II land

`web_fetch` 3-5 substantive pieces. Then `project_knowledge_search` for past dossiers and transcripts, and scan the master guest spreadsheet for prior appearances.

Then the five layers. Full spec in `references/research-layers.md`; read it before searching. Layers 4 and 5 only surface if searched for on purpose.

**Indian-source notes.** Entrackr plus an RoC qualifier is the filing-grade path. TheKredible often reports the standalone India entity rather than consolidated; flag it. Moneycontrol and ET mobile URLs frequently block the fetcher; fall back to Business Standard, Inc42, YourStory, BusinessToday. Company LinkedIn posts often carry numbers more current than press; label them company-reported.

### Stage 2 — Gap-fill (3-6 targeted searches)

Read Stage 1 back against the section spec. Typical gaps: a competitor's comparable number, a verbatim quote to anchor a provocation, the exact wording of a regulation, a working URL for a past appearance, what happened to a prior company after the founder's exit.

If two honest attempts at a figure fail, it is unknown, the dossier says so, and it becomes a ⚑ rather than an estimate.

### Stage 3 — Draft (internally)

Read `references/dossier-structure.md` for sections, then `references/akshay-question-voice.md` before writing any question. Both, every time.

### Stage 4 — Mandatory internal copywriter pass

Re-read as a copywriter serving a busy podcaster skimming on a phone 30 minutes before recording:

- **Skim test:** absorbable in 5 minutes. Headings and bold carry meaning.
- **Redundancy cut:** each fact appears ONCE, where it works hardest.
- **Voice check:** read every question aloud. Would Akshay say this sentence? If it reads like a Financial Times interviewer, rewrite it.
- **Flow check:** the sections read as one arc, not a pile. Business explainer → founder paragraph → timeline should read as three views of the same story, in increasing detail.
- **Word discipline:** each theme ≤75 words where the voice allows. His register is wordier than crisp written questions; when they conflict, **voice wins and the context line gets cut instead.**
- **AI-tell strip:** no "delve", "leverage", "robust", "seamless", "game-changing", "deep dive", no puffery, **no em-dashes anywhere**.

Only the post-pass version ships. One final dossier, never a before-and-after pair, never internal stage names in the output.

### Stage 5 — Guest note, checks, present

Generate from `references/guest-prep-template.html`, run the pre-delivery checklist, `present_files` dossier-first.

### Stage 6 — Log the dossier in the Business OS (Notion)

The team works from Notion, so the dossier has to be findable on the guest's Engagement without anyone pasting links by hand.

1. **Find the Engagement.** Engagements data source `collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5`, Founder Thesis rows only (`Show LIKE '%3ed19a301a7f817c9367e0d88afc5776%'`). Find the guest in People (`collection://e6c44319-7f81-4da6-8b80-8441a4875d7a`) by LinkedIn first, then exact name, then match `Guest LIKE '%<people page id>%'`. If there is no match, or more than one open Engagement could be it, do not guess and do not create one: say so in the chat reply.
2. **The link.** Use the shareable link to the dossier: the published artifact URL if the dossier was published, otherwise this chat's URL if you have it. If there is no link you can give, leave Dossier link alone and say "add the dossier link by hand" in the reply.
3. **Write.** `Dossier link` = the link. Add one line at the top of `Claude note`: `YYYY-MM-DD: host dossier and guest prep note ready (<link>)`, keeping existing lines below it. `Claude updated` = today. Do not change Status, Next action, Tier, Payment or anything else: the team sends the guest note and moves the status.
4. **Reply.** End the chat reply with one line: `Notion: Dossier link added to <Engagement name>` (or what failed). A failed Notion write never blocks shipping the dossier.

The calendar routine copies the Dossier link into Akshay's private prep entry on its next run.

## Dossier sections (full spec in references/dossier-structure.md)

Header (with LinkedIn link up top) · Sticky nav · **The business, simply** (short paragraph + stack diagram) · **The founder, briefly** (one paragraph) · **Career timeline** (visual, folds in company timelines) · **Themes in four acts** · Fact flags · Past appearances and how he interviews · **Snapshot** (stat strip + table, moved here) · **Appendix** (Numbers cheat sheet, Sources — collapsible)

**The four acts:**

- **Act I · Grounding** (2-3 themes) — category decode, the 101, who pays whom. The listener learns the industry before meeting the company.
- **Act II · The story, with a low point** (2-3 themes) — the leap, and the hardest stretch. Hunt for the low point deliberately. If the public record has none, the gap itself is the lead: find the period with no coverage, no revenue or no announcements and aim at it.
- **Act III · Mechanics** (3-4 themes) — model, unit economics, growth engine, tech, regulation.
- **Act IV · Hard questions** (2 themes) — genuine puzzles the guest can argue. Mark the sharpest `★ SPINE`. Mark anything from the last few days `⚡ BREAKING`.

Per theme: catchy specific heading, one context line carrying the fact that powers it, 2-4 questions in Akshay's register.

## Framework discipline (non-negotiable)

1. **The business explainer stays short.** One paragraph plus a stack diagram. If it's turning into a multi-part breakdown, cut it back — the detail belongs in the appendix or inside a theme, not up front.
2. **Both audiences, every theme.** 101 → worked example → pressure test.
3. **Numbers: ask plainly, or play back a published benchmark.** Both are his. Use the plain ask ("how do you make money", "what does revenue look like") for facts not in the public domain. Use benchmark playback ("Groww is making ₹19.8 an order, you charge ₹10, how does that work") where a comparable figure is published. What is banned is the analyst paraphrase of either.
4. **Flag, never average.** Conflicting figures get both numbers, both sources, and a ⚑.
5. **Specificity is the test.** Every question names a fact, number, year, person, competitor or benchmark.
6. **Sources must resolve.** Clickable, verified. Write "verify live" rather than faking a URL.
7. **Dark mode, always.** No light/white theme.

## Pre-delivery checks

- [ ] **Stage 0 run first: Drive and Gmail searched for pre-call notes and PR mail chain before asking Akshay for either**
- [ ] LinkedIn profile link visible near the top of the header, not buried in the meta block
- [ ] Sticky nav present and every anchor resolves
- [ ] Business section is one short paragraph + stack diagram, not a multi-part breakdown
- [ ] Founder paragraph is brief (100-150 words); career timeline carries the dates and folds in company timelines
- [ ] Timeline shows what happened to a prior company after the founder's exit, where that's part of the story
- [ ] Four acts present; Act II contains a low point or names the gap where one should be; spine marked
- [ ] **Every question read aloud against akshay-question-voice.md; no banned phrasings**
- [ ] At least one self-inserting hypothetical and one candidate-answer stack somewhere in the themes
- [ ] **Past appearances each hyperlinked inline, plus the read on how he interviews**
- [ ] Prior Founder Thesis appearance checked against the master sheet and stated
- [ ] Fact flags framed as housekeeping, not prosecution
- [ ] Snapshot (stat strip + table) placed after Themes/Fact flags/Past appearances, not before
- [ ] Numbers cheat sheet and Sources collapsed into an appendix at the bottom
- [ ] No em-dashes, no AI vocabulary, no repeated facts
- [ ] Guest note 480-550 words, first-person Akshay, no specific questions, no edit or approval promise
- [ ] Both files in `/mnt/user-data/outputs/`, presented dossier-first, no stale format version left behind
- [ ] Dark mode throughout, no light background
- [ ] Dossier link written to the guest's FT Engagement in Notion, or the reply says why not (Stage 6)

## Defensive notes — what NOT to do

- **Don't ask Akshay for pre-call notes or PR contact before searching Drive and Gmail yourself.**
- **Don't hand the research off, and don't stop to ask for it otherwise.** A guest name alone is complete input.
- **Don't rebuild the old five-part industry breakdown up front.** One paragraph, one diagram.
- **Don't write the founder's story as a chronological prose journey.** Brief paragraph, then the visual timeline.
- **Don't list past appearances without links.**
- **Don't draft questions before reading the voice file.** Neutral journalist-English gets rewritten every time.
- **Don't write prosecutorial questions.** "Defend that", "Why are they wrong", "What has to be true by FY28" are not his voice and not his interview.
- **Don't trust secondary-source valuations.** Peak figures get reported as current for years.
- **Don't present self-reported claims as verified.**
- **Don't average conflicting numbers.**
- **Don't ship two versions or leave a superseded file in outputs.**
- **Don't let themes go generic.** "Fundraising lessons" is a category; "raising at a $200m mark on a base that was zero eighteen months ago" is a theme.
- **Don't put specific questions, or any edit/approval language, in the guest note.**
- **Don't put the Snapshot or the numbers cheat sheet up front.** They go after Themes now.
- **Don't use a light background. Don't use em-dashes.**

## Reference files

Read each immediately before the matching task:

- `references/research-layers.md` — the five layers and what each must return (Stage 1)
- `references/dossier-structure.md` — section-by-section spec, dark mode, new section order (Stage 3)
- `references/akshay-question-voice.md` — **his register, verbatim patterns, banned phrasings (Stage 3, before any question)**
- `references/guest-prep-template.html` — visual base for the guest note (Stage 5)
