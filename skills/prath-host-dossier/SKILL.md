---
name: prath-host-dossier
description: >-
  Produce a two-file host dossier pack for a guest on the Prath
  podcast, the Indian D2C/consumer-founder show hosted by Piyush Goenka
  (co-founder, Prath Ventures). Trigger when Akshay types
  "prath-host-dossier" followed by a guest name, LinkedIn URL, brand,
  or backgrounder. Also trigger on "Prath dossier for [guest]", "host
  dossier for Piyush", "dossier for the Prath podcast", "prep Piyush
  for [founder]", or when Akshay pastes a backgrounder for a
  consumer-founder episode. Single continuous run, no handoff and no
  stop: Claude does the research itself via web_search and web_fetch
  across four layers (the brand build, category benchmarks, founder
  voice, tensions and sensitivities), then drafts, runs a copywriter
  pass, and ships both HTML files in the same turn. A starting point
  for Piyush's unraveling, not a script. The brand build leads, Indian
  category data is the bridge, angles follow as stations. No direct
  metric-extraction questions. No em-dashes.
---

# prath-host-dossier — Prath Podcast Host Dossier Pack

A pre-interview prep workflow for **Piyush Goenka**, co-founder of Prath Ventures (Mumbai consumer/D2C fund) and host of the Prath podcast. Guests are **Indian D2C and consumer founders**. The show is a founder build-story conversation, told through an investor's lens.

## What this dossier is for

**The job is narrow:** surface basic research about the founder and the brand, then suggest discussion areas and specific questions Piyush can use. That is it.

The dossier is Piyush's *starting point for unraveling the build*. It is NOT a research study, an interrogation playbook, a prepared script, a comprehensive biography, or a position document. Piyush has sat through 4,000+ founder meetings; he does not need a CV recited back to him. He needs the few specific threads worth pulling.

**Three operating principles:**

1. **Light prep, by design.** Enough to ground Piyush, not enough to make him feel scripted. Substantive but not exhaustive. Organic discovery during the recording is the point.

2. **The build is the story.** A consumer brand is a sequence of decisions: the wedge, the first SKU, the distribution bet, the hard quarter, the channel inflection. § 01 IS that story, in order. § 03 Interview Angles walks the same chronology as stations. If the dossier reads as "topics covered" rather than "a build told from A to B to C", restart.

3. **Specific questions, not generic ones.** Every follow-up is anchored in a named fact, person, number, moment, or category benchmark. "How do you think about retention" is a category. "You held DTC-only for three years while peers rushed to general trade. Why" is a question.

Plus a hard rule on sensitive numbers: **indirect benchmarking.** Founders dodge direct metric questions or give rehearsed answers. Frame the number through a § 02 category benchmark and let the founder volunteer the real figure by reacting to it.

## Inputs

One or more of:
- Guest name (`prath-host-dossier Ghazal Alagh`)
- LinkedIn URL
- Brand / company name
- A PR-supplied or AI-generated backgrounder (PDF, pasted text, document in the project). Optional, never required
- Optional: the show slot or theme (e.g. "category creation", "the road to profitability", "DTC to omnichannel")
- Optional: recording date

A guest name alone is a complete input. The run does its own research from there and ends with both files presented.

Extract every name, brand, round, channel, and concrete number before doing anything else. If a backgrounder is attached, mine it first, then search only for what it does not already cover.

## Outputs

**Two files**, generated at the end of the run, after the research is done:

1. **Host Dossier (HTML)** — `/mnt/user-data/outputs/<lastname>_prath_dossier.html` — The five-section dossier Piyush reads before recording. Restrained premium-consumer editorial aesthetic. The **brand build leads** (chronological journey); Indian category data is the bridge; angles follow the build; a clickable Sources section closes it.
2. **Guest Prep Note (HTML)** — `/mnt/user-data/outputs/<lastname>_prath_guest_prep.html` — ~450-550 words. Send-ready note from the Prath Podcast team to the founder, warm and professional, referring to Piyush in the third person. No production scaffolding visible.

Then call `present_files` with both paths, dossier first.

## The workflow — one continuous run

Claude does the research itself. There is no external research step, no prompt to hand off, no STOP, no waiting. Akshay supplies a name or a brand; the same turn ends with two files presented.

Five stages, all in one run: **research → gap-fill → draft → copywriter pass → ship**. Do not rush the research to reach the artifacts faster. The dossier is only ever as good as the search pass behind it, and there is no second pair of eyes on the research now. A thin § 02 Category Context and a generic § 03 are the two symptoms of a rushed Stage 1.

### Stage 1 — Core research pass

First mine any uploaded backgrounder or pre-call material. Then run 10-14 targeted searches. Start here and adapt to the guest and category:

1. `"<Guest Name>" <Brand>` — confirm role, find recent press
2. `<Brand> funding OR valuation 2025 OR 2026` — round history, lead investor, cap table signals. Hunt peak-vs-current valuation gaps
3. `<Brand> revenue OR GMV OR profitable OR EBITDA FY25 FY26` — financial stage and trajectory
4. `<Legal entity name> Entrackr OR RoC filing FY25 FY26` — filing-grade Indian financials. Combine legal entity AND brand name
5. `<Brand> distribution OR quick commerce OR general trade OR modern trade OR retail` — channel footprint and the mix shift
6. `<Guest Name> podcast OR interview` — existing long-form, for verbatim philosophy quotes
7. `<Category> market size India CAC repeat rate AOV report 2026` — the benchmark layer for § 02
8. `<Brand> competitors India` — the comparison set, with any public revenue or funding figures
9. `<Brand> recall OR layoffs OR down round OR controversy OR co-founder exit` — sensitivity sweep
10. `<Category> GST OR regulation OR rule change India 2025 2026` — name the specific rule, not the topic
11. Category-specific: a listed comparable's DRHP or annual report for margin structure (e.g. Nykaa, Honasa, Boat, Wow Skin, Bikaji), or the relevant industry report

`web_fetch` 3-5 substantive pieces: the most recent long-form founder interview, the latest funding or financials coverage, one category or channel report, a comparable's filing. Skip the brand's own marketing pages.

Then `project_knowledge_search` for past Prath dossiers (format updates), pre-call notes or producer briefings on this guest, and any project transcript that mentions the guest or the brand.

Then work the four research layers. **These are Claude's own work now, and the dossier is visibly thin without them. Do not skip them.** Full spec in `references/research-layers.md`. Read it before searching.

**Layer 1 — The brand build.** The wedge and the founding insight, the first SKU and its price point, the distribution sequence (DTC, marketplace, quick commerce, general trade, own retail) with dates, the hard quarter, the scale inflection. Named hires, advisors and investors attached to specific decisions. This is the raw material for § 01, and it is a decisions story, not a CV.

**Layer 2 — The category through numbers.** India category size and growth with the most-cited source named. The GT/MT/quick-commerce split for this category. CAC, AOV and repeat-rate benchmarks with the report and its date. Two or three comparable Indian brands with revenue, growth and margin where public, labelled filing-grade (MCA/RoC, DRHP, annual report) or prep-grade (press, estimated, self-reported). Every figure carries a date.

**Layer 3 — The founder's voice.** Prior ventures with dated outcomes. Then 3-5 short verbatim quotes from recent interviews or posts that reveal how the founder thinks about the category, the channel bet, or the brand. Each one linked. These anchor § 03 and the "words to play back" row, and a dossier without them produces generic stations. Also capture every claim the founder makes about the brand (category-first, largest, fastest, fully profitable) and whether an independent source confirms it.

**Layer 4 — Tensions and sensitivities.** The layer that only surfaces if searched for on purpose. Where two sources disagree on revenue, valuation or scale, carry both figures with both sources and dates. Never reconcile them into one number. Figures still circulating that look stale, especially a peak valuation reported as current. Anything the founder has publicly sidestepped or been challenged on. Dated sensitivities: a recall, a down round, a co-founder exit, margin pressure, a failed channel bet. This feeds § 04, and § 04 needs exactly one of these, chosen as the most delicate.

**Indian-source notes.** Entrackr plus an RoC qualifier is the filing-grade path. TheKredible often reports the standalone India entity rather than consolidated; flag it when used. Moneycontrol and ET mobile URLs frequently block the fetcher; fall back to Business Standard, Inc42, YourStory, BusinessToday, The Morning Context.

### Stage 2 — Gap-fill (3-5 targeted searches)

Read Stage 1 back against the section structure below and find what is missing. Typical gaps:

- The exact latest-FY revenue, or peak vs current valuation
- A named comparable's benchmark number for § 02
- A verbatim quote to anchor a station opener or the "words to play back" row
- Named hires, advisors or investors for the "land here" notes
- The exact wording of recent category news the brand is affected by (a quick-commerce shift, a GST change, an import rule)

Do not over-search. If two honest attempts at a figure fail, it is unknown, the dossier says so, and it never becomes an estimate.

### Stage 3 — Draft both files internally

Build the research synthesis first: merge Stage 1, Stage 2 and any provided backgrounder or pre-call notes, deduplicating. That synthesis is the single source of truth for both files. Then draft the Host Dossier per "Section structure" below, and the Guest Prep Note per its voice rules.

If `references/dossier-template.html` and `references/guest-prep-template.html` are present, use them as the visual base. If they are not, build to the visual system described below.

### Stage 4 — Mandatory internal copywriter pass (do NOT skip, do NOT show the pre-pass draft)

Re-read the dossier as a copywriter serving a busy investor who will skim it on a phone 30 minutes before recording:

- **Skim test:** the whole thing absorbs in 5 minutes. Headings and bold carry the meaning; prose is support.
- **Redundancy cut:** each fact appears ONCE, in the section where it works hardest. The at-a-glance card, the build story and the stations must not repeat each other.
- **Flow check:** § 01 reads as one build from A to B to C, and § 03 walks the same chronology. If it reads as "topics covered", restructure.
- **Specificity sweep:** any follow-up that would work for any consumer founder gets cut or anchored to a named fact.
- **AI-tell strip:** no "delve", "leverage", "unlock", "robust", "seamless", "game-changing", "deep dive", no puffery, **no em-dashes anywhere**.

Only the post-pass version ships. One final dossier, never a before-and-after pair, and never the internal stage names in the output.

### Stage 5 — Run checks and present

Run the pre-delivery checks below. Verify every § 05 link resolves. Then call `present_files` with both paths, dossier first.

## Visual system

Restrained premium-consumer editorial. Warm ivory ground (`#FBF8F3`), deep jade accent (`#1B5E4A`), near-black text (`#1A1A1A`), hairline rules in a warm grey. Spectral (or a serif fallback) for headings and pull quotes, Inter for body, IBM Plex Mono for the `§ 0X` labels and data-grid keys. Generous whitespace, one column, max width around 760px, no cards-on-cards. The at-a-glance card and the § 02 data grid are the only boxed elements; THE ANGLE boxes get a left jade rule rather than a full border. Self-contained HTML, fonts loaded from Google Fonts with a system fallback, no dark mode.

## Section structure (in order of appearance)

1. **§ 01 · The Build** — leads the document. An at-a-glance card (frame · signature numbers · words to play back · soft landings), then the chronological brand-build story in 5-8 era-labelled beats (the wedge / the insight → first product and pricing → the distribution bet → the hard moment → the channel or scale inflection → forward lens). People decisions and category bets, not a school-to-jobs march.
2. **§ 02 · Category Context** — the Indian consumer-market benchmarks, as a bridge after the story. Data grid with **clickable sources** (~180 words). Category size and growth, GT/MT/quick-commerce split, CAC/AOV/repeat benchmarks, comparable-brand revenue and margin. Indian comparators only (Zepto/Blinkit/Swiggy, Nykaa/Mamaearth/Boat, not DoorDash/Sephora).
3. **§ 03 · Interview Angles** — 4-7 journey-shaped stations, each anchored to a moment in the build. THE ANGLE box = a conversational opener in Piyush's voice (not a script). The transferable category lesson surfaces in a middle station as the founder's answer, not as an opening question.
4. **§ 04 · Tread Carefully** — one light callout for the single most delicate thread (down-round, recall, co-founder exit, margin pressure) + the soft way in.
5. **§ 05 · Sources** — every figure and quote with a **clickable, verified link**, grouped (category benchmarks / brand figures / quotes), filing-grade (DRHP/MCA) vs prep-grade (press) flagged.

## Voice rules — Host Dossier

The dossier is internal to Piyush. Calm, observational, investor-peer register. He is a fellow builder (Tano Capital, Safari Industries, 4,000 founder meetings), not a journalist.

- **Restrained premium-consumer editorial aesthetic.** Spectral serif headings, Inter body, IBM Plex Mono labels. Accent deep jade `#1B5E4A` on warm ivory.
- **No em-dashes anywhere.** This is Piyush's hard rule and it applies to the dossier too. Use commas, parentheses, or two short sentences. (This is the key divergence from a Built to Share dossier, which allows em-dashes.)
- **Concrete numbers wherever possible.** "₹140 Cr revenue, FY24, 60% from quick commerce". If a number is unknown, write "unknown" or "reported range". Never fabricate.
- **Indian anchoring.** Benchmarks and comparators are Indian-market. If you reach for a US comparator, find the Indian one.
- **No banned AI vocabulary** (delve, leverage, unlock, robust, seamless, etc.) and **no engagement-bait or puffery**. No "powerhouse", "thought leader", "game-changing", "deep dive".
- **No badges or "verified/unverified" tags on individual claims.** If something is too shaky to state cleanly, leave it out.
- **No production-meta language visible to Piyush.** Section labels read just `§ 0X · [Name]`. No "Stage 2", "Framework", "Working Draft".

## Voice rules — Guest Prep Note

Different audience: the founder, not Piyush. **Team voice** (the Prath Podcast team), referring to Piyush in the third person. This note is NOT first-person from Piyush. ~450-550 words.

- **Team voice, warm and professional.** The note comes from the show's team on Piyush's behalf. "We" run the conversation; Piyush is "he". Founder-respecting and specific, not a PR blast.
- **No specific questions.** Broad topic territory only. A founder in prep-mode kills the authenticity the show runs on.
- **Clips only.** We share clips from the conversation afterwards. **Never promise the full edited episode**, and never promise edit rights or final approval.
- **No em-dashes.** Same hard rule.
- **Bulleted "How the conversation will run".** Five bullets: format / style / theme / what Piyush will lean on / what he's most interested in. **No "pre-call" bullet** — pre-call coordination happens offline if at all, never promised in the note.
- **One pull quote.** A single italic Spectral line that captures Piyush's register (calm, aphoristic, Indian-consumer specific) and signals tone. It represents the host's approach; the note itself stays in the team's voice.
- **End with a P.S.** inviting the founder to flag anything sensitive in advance (a number they would rather not discuss, a name to avoid), framed in team voice as "we would much rather know now than have it come up on the recording", without promising a pre-call.

## Framework discipline (non-negotiable)

1. **Principle 1 — The category lesson is the destination, not the question.** No station title or § 03 heading names "the thesis", "the playbook for D2C", or "lessons for founders". Titles describe the founder's specific build decision. The transferable lesson emerges as the founder's answer in a middle station. (The § 01 story may narrate the arc in prose; the ban is on question/station titles.)
2. **Principle 2 — Lead with the build; data is the bridge.** § 01 The Build leads. § 02 Category Context follows it. If you open with a benchmark grid instead of the founder's build, you have reversed the structure. Restart.
3. **Principle 3 — Direct metric-extraction questions get dodged.** Every number-relevant angle leans on a § 02 benchmark, written in Piyush's conversational voice (THE ANGLE box), not as a paragraph he reads aloud. Never open with "what is your CAC / repeat rate / ARR".
4. **Principle 4 — Angles, not scripts; specific, not generic.** Stations follow the build chronologically. Every follow-up names a fact, person, moment, or benchmark. The angles are starting points to circle in his own words.
5. **Principle 5 — Sources must resolve.** Every figure and quote gets a clickable link in § 05, verified to work. Filing-grade (DRHP/MCA) vs prep-grade (press) flagged. No faked URLs; if a platform blocks linking, say "verify live".

## Pre-delivery checks

Run before `present_files`. If any line fails, fix before shipping.

### Required (non-negotiable)
- [ ] All four Stage 1 research layers worked (build, category numbers, founder voice, tensions), not a single sweep
- [ ] Every figure carries a date and a source, labelled filing-grade or prep-grade; nothing estimated to fill a hole
- [ ] Conflicting figures carried as both, never averaged into one
- [ ] At least 2 short verbatim founder quotes pulled from long-form, with links
- [ ] § 01 The Build LEADS: at-a-glance card + chronological build story, before § 02
- [ ] The story is build-and-decisions, not CV pacing (no school→jobs→founding march)
- [ ] At-a-glance card has four rows: frame / signature numbers / words to play back / soft landings
- [ ] § 02 Category Context follows the story; data grid has 4-6 named benchmarks, each with a CLICKABLE source
- [ ] All comparators and benchmarks are Indian-market, not US/global
- [ ] § 03 has 4-7 stations in chronological order, each with THE ANGLE + 2-3 specific follow-ups + land-here
- [ ] No station title or § 03 heading names the thesis, the D2C playbook, or "lessons"
- [ ] THE ANGLE boxes read in Piyush's conversational voice, not as benchmark paragraphs to read aloud
- [ ] Every number-relevant angle leans on a § 02 benchmark; none ask for a number directly
- [ ] The category lesson surfaces in a middle station as the founder's answer; that station's land-here is marked THE clip
- [ ] § 04 Tread Carefully is ONE light callout (single delicate thread + soft way in), not a table
- [ ] § 05 Sources present, grouped, every link VERIFIED to resolve; filing-grade vs prep-grade flagged; no faked URLs
- [ ] **NO EM-DASHES anywhere** in either file
- [ ] No banned AI vocabulary, no puffery, no engagement bait
- [ ] No production-meta breadcrumbs; section labels read just `§ 0X · [Name]`
- [ ] Guest Prep Note prose is between 450 and 550 words
- [ ] Guest Prep Note is in the team's voice (not first-person Piyush; Piyush referred to in third person)
- [ ] Guest Prep Note carries no specific questions, promises clips only (never the full edited episode), and no edit-rights/approval promise

### Optional enhancements (use when applicable, delete the scaffold when not)
- [ ] **Timely hook** — included only if a fresh event drives the conversation; deleted if no current angle
- [ ] **Extra build beats** — add 2-3 beyond the 5 scaffolded when the build has more phases (cap ~8)
- [ ] **Extra interview stations** — add 1-2 (cap at 7) for richer builds; drop to 4 for a simpler arc

## Defensive notes — what NOT to do

- **Don't rush the research to reach the artifacts.** There is no external research pass behind this dossier any more and no second pair of eyes on the facts. Work all four layers in Stage 1 before drafting. A thin § 02 and a generic § 03 both trace back to a hurried search pass.
- **Don't stop and ask.** No handoff, no research prompt, no waiting for a paste-back. A guest name is enough to run the whole thing end to end.
- **Don't let the build become a CV.** Build-first does NOT mean "grew up in X, studied at Y, joined Z, then founded W". The Build is a decisions story: the wedge, the pricing call, the distribution bet, the hard quarter, the channel inflection. If a beat is a degree or a feature for its own sake, cut it.
- **Don't ask for metrics directly.** "What is your repeat rate" gets a rehearsed answer. Frame it through a § 02 benchmark and let the founder react. This is Principle 3 and it is the most common failure mode.
- **Don't reach for US comparators.** Swiggy, not DoorDash. Nykaa, not Sephora. Mamaearth, not The Ordinary. The Indian anchor is the point.
- **Don't include themes that would work for any consumer founder.** "Building a brand" is a category. "Staying DTC-only for three years while the category rushed to quick commerce" is a theme. Specificity is the test.
- **Don't fabricate financials or CAC numbers.** If the data isn't in the research, write "reported range" or "signal unclear". Never invent a margin or a valuation.
- **Don't ship an unverified Sources link.** § 05 exists so Piyush can validate data at source. A 404 defeats the point. Verify each link; if it won't resolve, say "verify live".
- **Don't put specific questions in the Guest Prep Note.** Territory only.
- **Don't write the prep note in Piyush's first-person voice.** It comes from the show's team on his behalf. "We" run it; Piyush is "he".
- **Don't promise the full edited episode.** We share clips only. Never imply the founder gets the finished episode, edit rights, or approval.
- **Don't write the Guest Prep Note as a manifesto.** A real team-to-founder note, warm and professional, not a positioning document.
- **Don't write THE ANGLE as a script.** "You held DTC-only while everyone else rushed to the marketplaces. Walk me through that call." in his voice is right. A 60-word benchmark paragraph he reads aloud like a journalist is wrong.
- **Don't use a single em-dash, anywhere, in either file.** This is the rule the model will most easily break. Check twice.

## Reference files

Read each one immediately before the matching task:

- `references/research-layers.md` — the four research layers Claude works in Stage 1 (read before searching)
- `references/dossier-template.html` — visual styling base for the host dossier (at-a-glance, build, category grid, stations, sources). Optional; if it is not in the folder, build to the "Visual system" section above
- `references/guest-prep-template.html` — visual styling base for the guest prep note. Optional; same fallback
