---
name: "bts-host-dossier"
description: "Produce a two-file host dossier pack for a guest on Built to Share, the podcast hosted by Satish Mugulavalli. Trigger whenever Akshay types \"bts-host-dossier\" followed by a guest name, LinkedIn URL, or PR backgrounder. Also trigger on \"Built to Share dossier for [guest]\", \"host dossier for Satish\", \"make the BTS dossier\", or when Akshay pastes a backgrounder for an Ownership Collective episode. Single continuous run with no handoff and no stop: Claude does the research itself via web_search and web_fetch, covering recent moves, verbatim founder quotes, sensitivities, and comp/ESOP benchmarks, then gap-fills and produces two HTML files — a host dossier and a ~500-word peer-voiced guest prep note. A starting point for Satish's unraveling, not a script or research study. The guest's story leads (chronological journey), industry data is the bridge, angles follow as stations, and a clickable Sources section lets Satish validate every figure. Zero direct number-extraction questions. Ends by logging the Dossier link on the guest's Engagement in the Business OS (Notion)."
---

# bts-host-dossier — Built to Share Host Dossier Pack

A pre-interview prep workflow for **Satish Mugulavalli**, host of *Built to Share*. The current season is **The Ownership Collective** — episodes on how Indian founders build teams and design ownership.

## What this dossier is for

**The job is narrow:** surface basic research about the guest and his company, then suggest discussion areas and specific questions Satish can use. That's it.

Satish's own description of how he prepares (from the Saurabh Gupta recording): *"I didn't look at your LinkedIn profile until 7am... I didn't want to have some questions running in my mind. I spent 20 minutes on your LinkedIn. If I know this much about a person, it will serve as a starting point for me. And as I'm walking through the conversation, can I unravel bits and bits and pieces?"*

The dossier is Satish's *starting point for unraveling*. It is NOT a research study, an interrogation playbook, a prepared script, a comprehensive biography, or a position document.

**Three operating principles drawn from project call transcripts:**

1. **Light prep, by design.** Satish keeps preparation deliberately light to preserve organic discovery during the recording. The dossier should be substantive but not exhaustive — enough to ground Satish, not enough to make him feel scripted.

2. **Story arc over topic coverage.** Saurabh Gupta's structural feedback to Satish was direct: *"I do not think it was a structured conversation that was told like a story. Typically in my head it's a story that goes from A to B to C to D."* v3 takes this literally: § 01 IS the story, and § 03 Interview Angles walks the same chronology as stations — industry frame folded in → the bet → the hard moment → ownership → forward lens.

3. **Specific questions, not generic ones.** Also from Saurabh's feedback: *"If you give a specific question to people, they will give a specific answer. Specific questions is something Sean VP does very well in MFM."* Every follow-up in the dossier should be specific — anchored in a named fact, person, moment, or industry benchmark.

Plus the April 2026 feedback session locked in **indirect benchmarking** for sensitive topics: *"Direct questions are ineffective. The strategy should shift to an indirect approach, possibly using reports from hiring companies or industry benchmarks from sources like Native to frame generalized questions about trends rather than focusing solely on the guest's specific company."*

## Inputs

One or more of:
- Guest name (`bts-host-dossier Ashok Hariharan`)
- LinkedIn URL
- Company name
- Optional: a PR-supplied backgrounder or any research Akshay already has (PDF, pasted text, document attached to the project)
- Optional: the specific Ownership Collective slot (e.g. "patient compounding", "competing with Big Tech for AI talent", "IPO journey")
- Optional: recording date

A backgrounder is a bonus, never a requirement. A guest name alone is a complete input — the run does its own research from there.

Extract every name, role, company, recent round, and concrete data point before doing anything else. If a backgrounder is already attached, mine it first, then treat its claims as prep-grade until a search confirms them — don't duplicate work in Stage 1, and don't inherit its errors either.

## Outputs

**Two files**, generated at the end of the run, after the research is done:

1. **Host Dossier (HTML)** — `/mnt/user-data/outputs/<lastname>_dossier.html` — The five-section dossier Satish reads before recording. Warm editorial aesthetic. The guest's **story leads** (chronological journey); industry data is the bridge; angles follow the journey; a clickable Sources section closes it.
2. **Guest Prep Note (HTML)** — `/mnt/user-data/outputs/<lastname>_guest_prep.html` — ~500 words. Send-ready letter from Satish to the guest. Peer-to-peer founder-to-founder voice. No production scaffolding visible.

Then call `present_files` with both paths, dossier first.

## The workflow — one continuous run

Claude does the research itself. There is no external research step, no prompt to hand off, no waiting. Akshay supplies a name; the same turn ends with two files presented.

Four stages, all in one run: **research → gap-fill → generate → log in Notion**. Don't rush the research to reach the artifacts faster. The dossier is only ever as good as the search pass behind it, and there is no second pair of eyes on the research now.

### Stage 1 — Core research pass

Run 10-14 targeted web searches. Start here and adapt to the guest:

1. `"<Guest Name>" <Company>` — confirm the role is CURRENT, find recent press
2. `<Company> funding 2025 OR 2026` — latest round, valuation, lead investor
3. `<Company> ESOP OR secondary OR buyback` — any public equity events
4. `<Guest Name> interview OR podcast` — existing long-form he has done
5. `<Company> Glassdoor OR attrition OR layoffs` — workforce signals
6. `<Company> revenue OR profitable OR DRHP OR IPO` — financial stage
7. `<Guest Name> hiring OR team OR culture` — public people decisions
8. `<Guest Name> co-founder OR leadership team OR CXO hire` — the bench around him
9. `<Company> Entrackr OR RoC filing FY25 FY26` — filing-grade financials
10. `<Category> compensation report India 2026` — comp benchmarks
11. `<Category> ESOP pool DRHP` — comparable-stage pool sizes
12. `<Company> lawsuit OR controversy OR resignation OR down round` — sensitivities

Then the four jobs the old Deep Research handoff used to carry. These are now Claude's own work, and the dossier is visibly thin without them. **Do not skip them.**

**(a) Verbatim philosophy quotes.** Fetch the 2-3 longest-form interviews the guest has given and pull actual sentences in his own words about people, hiring, hard calls, or ownership. These feed the § 01 "words to catch and play back" row and the § 05 quotes group. Keep every verbatim short and sourced; paraphrase everywhere else.

**(b) Named-report benchmarks.** § 02 needs 4-6 benchmarks that each carry a report name, a publisher, and a year — not a floating industry figure. Search the publishers directly: Native, Aon, Mercer, EY, Deloitte, Longhouse, RedSeer, plus DRHPs of listed comparables. If a benchmark won't resolve to a nameable, linkable source, drop it rather than round it into vagueness.

**(c) Sensitivities.** What has the guest publicly dodged, declined to answer, or been asked in a way that visibly landed badly? Co-founder exits, down rounds, layoffs, regulatory action, a delayed IPO, a secondary priced below the last mark. This is the raw material for § 04, and it only surfaces if you search for it on purpose.

**(d) Filing cross-reference.** For ESOP pool sizing and revenue: RoC-sourced and DRHP figures are filing-grade, press estimates are prep-grade. Track which one you have for every number — § 05 has to flag it.

Use `web_fetch` on 4-6 substantive pieces: the most recent long-form founder interview, the latest funding press release, any people or HR coverage, the DRHP or filing summary if one exists. Skip company marketing pages.

Then check the project knowledge base via `project_knowledge_search` for:
- Past dossiers in the project that may indicate format updates
- Any pre-call notes or producer briefings on this guest
- Project call transcripts if the guest is mentioned

**Indian-source notes.** Entrackr plus an RoC qualifier is the filing-grade path. TheKredible often reports the standalone entity rather than consolidated — flag it when used. Moneycontrol and ET mobile URLs frequently block the fetcher; fall back to Business Standard, Inc42, YourStory, BusinessToday.

### Stage 2 — Gap-fill

Read Stage 1 back against the section spec and find what's missing. The usual gaps:

- Specific named hires the guest is publicly associated with (for the "land here" notes)
- Quotes from interviews that could anchor a benchmark opener
- Comparable-stage ESOP pool sizes (DRHPs are the best source)
- Exact wording of the Companies Act or regulatory change affecting his category
- Glassdoor patterns specific to the company (extract themes, never paste reviews verbatim)
- Recurring public phrases the guest uses — for the § 01 "words to catch and play back" row

Run 3-6 more targeted searches on the highest-leverage gaps. Don't over-search: if two honest attempts at a figure fail, it is unknown, and the dossier says so.

**Coverage gate — check before generating anything.** If any line here is still empty, that's a research problem, not a writing problem. Go back to searching.

- [ ] Current role verified as of this month, not inherited from an older profile
- [ ] At least 4 § 02 benchmarks with named, linkable sources
- [ ] At least 2 verbatim guest quotes, each with a working source link
- [ ] The ownership arc — at least one concrete public data point, or an explicit "no public signal"
- [ ] At least one genuinely delicate thread for § 04
- [ ] Every § 05 link opened and confirmed to resolve

Where a gate item genuinely can't be filled after honest searching, keep the section and state plainly what is unknown. Never invent a figure, a report name, or a URL to close a gate.

### Stage 3 — Generate the two outputs

Order of generation:

1. Build the **research synthesis** internally — merge Stage 1 findings, Stage 2 gap-fill, and any supplied backgrounder, deduplicating. This is the single source of truth for both artifacts.
2. Generate the **Host Dossier** using `references/dossier-template.html` as the visual base, filling in content per `references/dossier-structure.md`. Read the structure file BEFORE writing.
3. Generate the **Guest Prep Note** using `references/guest-prep-template.html`.
4. Run the **pre-delivery checks** below.
5. Call `present_files` with both paths in order: dossier first, guest prep second.
6. Close with 2-3 lines in chat naming where the research ran thin and which figures Akshay may want to double-check before this reaches Satish. Short, plain, no report formatting.

### Stage 4: Log the dossier in the Business OS (Notion)

The team works from Notion, so the dossier has to be findable on the guest's Engagement without anyone pasting links by hand. Run this after the dossier and guest note ship.

1. **Find the Engagement.** Engagements data source `collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5`, Built to Share rows only (`Show LIKE '%3ed19a301a7f819e8f45de04a7c9d025%'`). Find the guest in People (`collection://e6c44319-7f81-4da6-8b80-8441a4875d7a`) by LinkedIn first, then exact name, then match `Guest LIKE '%<people page id>%'`. If there is no match, or more than one open Engagement could be it, do not guess and do not create one: say so in the chat reply.
2. **The link.** Use the shareable link to the dossier: the published page URL if it was published, otherwise this chat's URL if you have it. If there is no link you can give, leave Dossier link alone and say "add the dossier link by hand" in the reply.
3. **Write.** `Dossier link` = the link. Add one line at the top of `Claude note`: `YYYY-MM-DD: Satish's dossier and guest prep note ready (<link>)`, keeping existing lines below it. `Claude updated` = today. Do not change Status, Next action, Tier, Payment or anything else: the team sends the guest note and moves the status.
4. **Reply.** End the chat reply with one line: `Notion: Dossier link added to <Engagement name>` (or what failed). A failed Notion write never blocks shipping the dossier.

The calendar routine copies the Dossier link into Akshay's private prep entry on its next run.

## Section structure (in order of appearance) — v3, story-first

1. **§ 01 — The Journey** — leads the document. An at-a-glance card (frame · signature stats · words to play back · soft landings), then the chronological team-and-ownership story (5-8 era-labelled beats). This folds in what used to be Episode Positioning, The Guest, and The Company.
2. **§ 02 — Industry Context** — the talent-market benchmarks, demoted to a bridge after the story. Data grid with **clickable sources** (~180 words).
3. **§ 03 — Interview Angles** — 4-7 journey-shaped stations, each anchored to a moment in the build. THE ANGLE box = a conversational opener in the host's voice (not a script). Ownership surfaces in a middle station as the answer.
4. **§ 04 — Tread Carefully** — one light callout for the single most delicate thread + the soft way in. Replaces the old reframe table.
5. **§ 05 — Sources** — every figure and quote with a **clickable, verified link**, grouped (benchmarks / company figures / quotes), filing-grade vs prep-grade flagged.

Full spec in `references/dossier-structure.md`. The One-Pager and separate Quick-Stats row are gone — their live-use content lives in the § 01 at-a-glance card.

## Voice rules — Host Dossier

These apply to the dossier body. The dossier is internal to Satish. Confident, editorial, peer-respect tone.

- **Warm editorial newspaper aesthetic.** Playfair Display headings, DM Sans body, DM Mono labels. Accent #C8371A (warm rust).
- **Em-dashes are FINE.** This is *not* the un#/aarna voice. Built to Share editorial copy uses em-dashes naturally.
- **Concrete numbers wherever possible.** If a number is unknown, say "unknown" or "reported range" — don't fabricate.
- **No badges, flags, or "verified / unverified" tags on individual claims.** If something is too shaky to state cleanly, leave it out.
- **No production-meta language visible to Satish.** No "Stage 1A", "Stage 2 · the cheat sheet", "Framework" tags, "Working Draft" — these were stripped in the validated final version of the Ashok dossier. Section labels read just `§ 0X — [Section Name]`.
- **No Stage 0 / Pre-Brief Intake block.** Production-team concerns don't go in the document Satish reads.
- **No Distribution Brief section.** Clip targets and LinkedIn hooks belong with the content team.

## Voice rules — Guest Prep Note

Different audience — the guest, not Satish. First-person voice from Satish. ~500 words target.

- **Peer-to-peer founder-to-founder.** Satish is a fellow builder (operator + VC + ESOP infrastructure), not a journalist.
- **No "deep and real" framing.** Banned. The April 2026 review locked this in.
- **No promises of edit rights or final approval** over the episode.
- **Never promise to share the edited or full episode with the guest.** We don't send full episodes to guests. The only after-recording promise: once the episode is live, we send the link along with a set of clips for the guest and their team.
- **Recording platform is Riverside.** The format bullet says a remote recording on Riverside, about 90 minutes, edited to around an hour. The older Built to Share Guest Note PDF in the project still says Zencastr; don't copy that.
- **No specific questions in the note.** Broad topic territory only.
- **Bulleted "How the conversation will run".** Five bullets covering format / style / theme / what Satish will lean on / what he's most interested in. **Do NOT include a "pre-call" bullet** — pre-call coordination happens offline if at all; never promised in the formal note.
- **One pull quote.** A single italic Playfair line that signals tone.
- **End with a P.S.** inviting the guest to reply if anything sits wrong (a sensitive topic, a name they'd rather we not raise) — framed as "much rather hear it in advance than discover it on the recording", without promising a pre-call.

## Framework discipline (non-negotiable)

Read `references/discipline.md` before generating the dossier. The headline rules:

1. **Principle 1 — ESOPs are the answer, not the question.** No station title or heading in § 03 names ESOPs, equity, or ownership — they describe the *people challenge*. (The § 01 story may narrate the ownership arc in prose; the ban is on question/station titles.)
2. **Principle 2 — Lead with the story; data is the bridge.** § 01 The Journey leads. § 02 Industry Context follows it. If you open with a benchmark grid instead of the guest's story, you've reversed v3 — restart.
3. **Principle 3 — Direct number-extraction questions get dodged.** Every number-relevant angle leans on a § 02 benchmark — but written in the host's conversational voice (THE ANGLE box), not as a paragraph he reads aloud.
4. **Principle 4 — Angles, not scripts; specific, not generic.** Stations follow the build chronologically; every follow-up names a fact, person, moment, or benchmark. The angles are starting points to circle in his own words.
5. **Principle 5 — Sources must resolve.** Every figure and quote gets a clickable link in § 05, verified to work. Filing-grade vs prep-grade flagged. No faked URLs.

## Pre-delivery checks

Run this before calling `present_files`. If any line fails, fix before shipping.

### Required (non-negotiable)
- [ ] § 01 The Journey LEADS — at-a-glance card + chronological story, before § 02
- [ ] The story is team-and-ownership, not CV pacing (no school→jobs→founding march)
- [ ] At-a-glance card has exactly four rows: frame / shape-of-him stats / words to play back / soft landings
- [ ] § 02 Industry Context follows the story; data grid has 4-6 named benchmarks, each with a CLICKABLE source
- [ ] § 03 has 4-7 stations in chronological order, each with THE ANGLE + 2-3 specific follow-ups + land-here
- [ ] No station title or § 03 heading mentions ESOPs, equity, or ownership
- [ ] THE ANGLE boxes read in the host's conversational voice, not as benchmark paragraphs to read aloud
- [ ] Every number-relevant angle leans on a § 02 benchmark; none ask for a number directly
- [ ] Ownership surfaces in a middle station as the guest's answer; that station's land-here is marked THE clip
- [ ] § 04 Tread Carefully is ONE light callout (single delicate thread + soft way in), not a table
- [ ] § 05 Sources present, grouped (benchmarks / company figures / quotes), every link VERIFIED to resolve
- [ ] Filing-grade (RoC/DRHP) vs prep-grade (press) flagged in § 05; no faked URLs (say "verify live" if unlinkable)
- [ ] No Stage breadcrumbs / Distribution Brief / Cross-Episode Patterns; section labels read just `§ 0X — [Name]`
- [ ] Guest Prep Note prose is between 480 and 580 words
- [ ] Guest Prep Note doesn't use "deep" or pair "deep" / "real" in interrogation framing
- [ ] Guest Prep Note doesn't promise edit rights or final approval
- [ ] Guest Prep Note doesn't promise to share the edited or full episode; the only post-recording promise is the live link plus clips
- [ ] Guest Prep Note format bullet names Riverside (never Zencastr)
- [ ] Dossier link written to the guest's Built to Share Engagement in Notion, or the reply says why not (Stage 4)

### Optional enhancements (use when applicable, delete the scaffold when not)
- [ ] **Timely Hook** — included if a fresh event drives the conversation; deleted if no current angle. Don't force.
- [ ] **Extra journey beats** — add 2-3 beyond the 5 scaffolded when the build has more distinct phases (cap ~8).
- [ ] **Extra interview stations** — add 1-2 beyond the 5 scaffolded (cap at 7) for builds with more phases; drop to 4 for a simpler arc.
- [ ] **Arc subtitle** — used under sections where the structural logic isn't self-evident.

See `references/dossier-structure.md` "Optional enhancement components" for the use/skip rules per component.

## Defensive notes — what NOT to do

- **Don't thin out the research now that nobody else is doing it.** The old workflow leaned on an external Deep Research pass for quotes, named-report benchmarks, and sensitivities. That work didn't disappear, it moved here. Six lazy searches and a confident tone produce a dossier that reads fine and collapses the moment Satish tries to use a number in the room.
- **Don't stop mid-run to ask permission to continue researching.** The run is continuous by design. Ask only if the input is genuinely ambiguous — two founders with the same name, or a company that can't be identified.
- **Don't let the story become a CV.** Story-first does NOT mean "X grew up in Y, studied at Z, then joined W." The Journey is a team-and-ownership story — people decisions, hard moments, how ownership surfaced. If a beat is about a degree or a product feature for its own sake, cut it.
- **Don't include themes that would work for any guest in the category.** "Talent retention" is a category. "Holding the team through eight years at ₹11 Cr revenue" is a theme. Specificity is the test.
- **Don't reintroduce Cross-Episode Patterns.** This was tried in an earlier version and pulled. The dossier is a starting point for Satish's unraveling, not a research study. If a useful cross-episode insight emerges, it can go in the LinkedIn distribution work — not in the dossier.
- **Don't fabricate Glassdoor or attrition numbers.** If the data isn't in the research, say "reportedly mixed" or "signal unclear".
- **Don't ship an unverified Sources link.** § 05 exists so Satish can validate data at source — a 404 defeats the point. Verify each link; if it won't resolve or the platform blocks linking, say "verify live" instead of faking a URL.
- **Don't put specific questions in the Guest Prep Note.** Territory only. The show's edge is the guest's reactions being in the moment.
- **Don't lift logistics from the old Guest Note PDF.** It says Zencastr and promises a prep call. Riverside is the platform, and neither a pre-call nor an edited-episode preview goes in the note.
- **Don't write the Guest Prep Note as a manifesto.** Treat it like a real founder-to-founder note, not a positioning document.
- **Don't write THE ANGLE as a script.** "You've just rebuilt the top of the house..." in his voice is right. A 60-word benchmark paragraph he'd read aloud like a journalist is wrong — that's the exact register the show avoids. Reference the data; sound like Satish.

## Reference files

Read each one immediately before the matching task:

- `references/discipline.md` — the principles + banned-phrasing list + v3 checklist (read before generating the dossier)
- `references/dossier-structure.md` — section-by-section spec (read before generating the dossier)
- `references/dossier-template.html` — visual styling base for the host dossier (v3 structure: at-a-glance, journey, stations, sources)
- `references/guest-prep-template.html` — visual styling base for the guest prep note