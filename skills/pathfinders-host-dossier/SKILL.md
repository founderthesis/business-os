---
name: "pathfinders-host-dossier"
description: "Produce a two-file host dossier pack for a guest on Pathfinders (\"Pathfinders by Divir Tiwari, Powered by FieldAssist\"), the podcast hosted by Divir Tiwari. Trigger whenever Akshay types \"pathfinders-host-dossier\" followed by a guest name, LinkedIn URL, or backgrounder. Also trigger on \"Pathfinders dossier for [guest]\", \"host dossier for Divir\", \"make the Pathfinders dossier\". Single continuous run with no handoff and no stop: Claude does the research itself via web_search and web_fetch, covering recent moves, verbatim quotes, sensitivities, and sales and distribution benchmarks, then gap-fills and produces two HTML files: a host dossier and a ~500-word peer-voiced guest prep note. A starting point for Divir's conversation, not a script. The guest's story leads (chronological journey), industry data is the bridge, angles follow as stations, and a clickable Sources section lets Divir validate every figure. Zero direct number-extraction questions. Ends by logging the Dossier link on the guest's Engagement in the Business OS (Notion)."
---

# pathfinders-host-dossier: Pathfinders host dossier pack

A pre-interview prep workflow for **Divir Tiwari**, co-founder of FieldAssist and host of *Pathfinders* (full name "Pathfinders by Divir Tiwari, Powered by FieldAssist"). Season 1: long-form conversations with founders and leaders who built consumer businesses that scale, in India, Southeast Asia and beyond. Each episode covers the playbook that worked, the operating system underneath it, how they kept one thing excellent while everything else grew, and the parts that didn't work.

## What this dossier is for

**The job is narrow:** surface basic research about the guest and their company, then suggest discussion areas and specific questions Divir can use.

Divir is an operator, not a broadcaster. He has spent more than a decade on how consumer brands reach the shop counter, and he learned most of it from operators a few steps ahead of him. The dossier should let him talk to the guest as a peer who knows the trade: distributors, beats, outlets, general trade, modern trade, quick commerce, sales force productivity. It is his starting point, not a research study, a script or a biography.

**Three operating principles:**

1. **Light prep, by design.** Enough to ground Divir, not enough to make him sound scripted.
2. **Story arc over topic coverage.** A conversation that goes from A to B to C to D beats a list of topics. § 01 IS the story, and § 03 walks the same chronology as stations.
3. **Specific questions, not generic ones.** Every follow-up is anchored in a named fact, person, moment or benchmark. Specific questions get specific answers.

**Indirect benchmarking for sensitive numbers.** Guests dodge direct number questions (margins, distributor economics, attrition, sales force cost). Frame them through an industry benchmark ("most FMCG brands we see run X; where did you land?"), never "what is your margin?".

## Inputs

One or more of:
- Guest name (`pathfinders-host-dossier <Name>`)
- LinkedIn URL
- Company name
- Optional: a backgrounder, the guest's eval page on the Engagement, Divir's notes on why he invited them
- Optional: recording date and whether it is remote or in the FieldAssist studio

A guest name alone is a complete input. Extract every name, role, company and data point before doing anything else. If the Engagement has a Pathfinders eval page, mine it first, then treat its claims as prep-grade until a search confirms them.

## Outputs

> **Notion standard (decision 677, Akshay, 25 Nov 2026): this overrides the output format below.** The host dossier is a Notion page under the guest's Engagement, laid out exactly as docs/dossier-notion-layout.md says (model: the Akshay Bector FT dossier). Do not build or publish the dossier as HTML or an artifact. Everything below still governs research, content, voice, section substance and questions; only the format and delivery change. The guest prep note is unchanged.


**Two files**, generated at the end of the run, after the research is done:

1. **Host Dossier (HTML)**: `<lastname>_pathfinders_dossier.html`. The five-section dossier Divir reads before recording.
2. **Guest Prep Note (HTML)**: `<lastname>_pathfinders_guest_prep.html`. About 500 words. A send-ready note from Divir to the guest. Peer-to-peer, operator to operator. No production scaffolding visible.

Publish both as artifacts (dossier first) and give the links.

## The workflow: one continuous run

Four stages, all in one run: **research, gap-fill, generate, log in Notion**. Don't rush the research to reach the files faster.

### Stage 1: core research pass

Run 10 to 14 targeted web searches. Start here and adapt to the guest:

1. `"<Guest Name>" <Company>`: confirm the role is CURRENT, find recent press
2. `<Company> revenue OR FY25 OR FY26`: financial stage (Entrackr or RoC for Indian companies; the annual report if listed)
3. `<Company> distribution OR distributors OR outlets`: retail reach and how it was built
4. `<Company> general trade OR modern trade OR quick commerce`: the channel mix and how it is shifting
5. `<Guest Name> interview OR podcast`: existing long-form they have done
6. `<Guest Name> sales team OR sales force OR field force`: public people decisions in sales
7. `<Company> rural OR expansion OR new markets`: reach decisions
8. `<Company> funding OR acquisition OR IPO`: capital events
9. `<Category> India market size 2025 OR 2026`: category benchmark
10. `FMCG distribution report India 2026` or the guest's market equivalent: route-to-market benchmarks (NielsenIQ, Kantar, Bain, Redseer, McKinsey, EY, company annual reports)
11. `quick commerce share FMCG <year>`: channel shift benchmark
12. `<Company> layoffs OR dispute OR recall OR resignation`: sensitivities

Then the four jobs that make the dossier usable. **Do not skip them.**

**(a) Verbatim quotes.** Fetch the 2 or 3 longest-form interviews the guest has given and pull actual sentences in their own words about how they sell, how they built distribution, hard calls or the people around them. These feed the § 01 "words to catch and play back" row and the § 05 quotes group. Keep every verbatim short and sourced.

**(b) Named-report benchmarks.** § 02 needs 4 to 6 benchmarks, each with a report name, a publisher and a year. If a benchmark won't resolve to a nameable, linkable source, drop it.

**(c) Sensitivities.** What has the guest publicly dodged or been asked in a way that landed badly? Channel conflict, distributor disputes, layoffs, a recall, a failed launch, a market exit. This is the raw material for § 04; it only surfaces if you search for it on purpose.

**(d) Filing cross-reference.** RoC-sourced and annual-report figures are filing-grade; press estimates are prep-grade. Track which one you have for every number; § 05 flags it.

Use `web_fetch` on 4 to 6 substantive pieces: the most recent long-form interview, the latest results or funding release, any coverage of their sales or distribution system. Skip company marketing pages.

**Indian-source notes.** Entrackr plus an RoC qualifier is the filing-grade path. TheKredible often reports the standalone entity rather than consolidated: flag it when used. Moneycontrol and ET mobile URLs often block the fetcher; fall back to Business Standard, Inc42, YourStory, BusinessToday, Afaqs, exchange4media.

### Stage 2: gap-fill

Read Stage 1 back against the section spec and find what's missing. The usual gaps: specific named hires or partners, a quote that could anchor a benchmark opener, the guest's channel mix, recurring phrases for the § 01 "words to catch and play back" row. Run 3 to 6 more searches on the biggest gaps. If two honest attempts at a figure fail, it is unknown, and the dossier says so.

**Coverage gate: check before generating anything.**

- [ ] Current role verified as of this month
- [ ] At least 4 § 02 benchmarks with named, linkable sources
- [ ] At least 2 verbatim guest quotes, each with a working source link
- [ ] The playbook: at least one concrete public data point on how they sell or distribute, or an explicit "no public signal"
- [ ] At least one genuinely delicate thread for § 04
- [ ] Every § 05 link opened and confirmed to resolve

Never invent a figure, a report name or a URL to close a gate.

### Stage 3: generate the two outputs

1. Build the **research synthesis** internally: Stage 1, Stage 2 and any backgrounder, deduplicated. It is the single source of truth for both files.
2. Generate the **Host Dossier** per the section structure below.
3. Generate the **Guest Prep Note** per its voice rules.
4. Run the **pre-delivery checks**.
5. Publish both, dossier first.
6. Close with 2 or 3 lines in chat naming where the research ran thin and which figures Akshay may want to check before this reaches Divir.

### Stage 4: log the dossier in the Business OS (Notion)

1. **Find the Engagement.** Engagements data source `collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5`, Pathfinders rows only (`Show LIKE '%41d19a301a7f810aad39f01621459709%'`). Find the guest in People (`collection://e6c44319-7f81-4da6-8b80-8441a4875d7a`) by LinkedIn first, then exact name, then match `Guest LIKE '%<people page id>%'`. No match, or more than one open Engagement: don't guess and don't create one; say so in the reply.
2. **The link.** The published page URL. If there is no link you can give, leave Dossier link alone and say "add the dossier link by hand".
3. **Write.** `Dossier link` = the link. Inside an engagement chat, the Claude note line goes through the chat's Row change Activity, and the decision 617 sharing task for Akshay is created as the engagement chat seed says. Do not change Status, Next action, Waiting on or anything else.
4. **Reply.** End with one line: `Notion: Dossier link added to <Engagement name>` (or what failed). A failed Notion write never blocks shipping the dossier.

## Section structure (in order of appearance), story first

**§ 01 The Journey** (leads the document)
- **At-a-glance card**, exactly four rows:
  1. *Frame*: the episode in one line (the build, the playbook, the one thing they kept excellent).
  2. *Shape of them*: 3 or 4 signature stats (revenue, outlets or reach, years, team or sales force), each dated.
  3. *Words to catch and play back*: 2 or 3 phrases the guest uses, verbatim.
  4. *Soft landings*: 2 or 3 safe, warm openers if the conversation stalls.
- **The story**: 5 to 8 era-labelled beats, chronological, about building the business and its reach: the first customers or outlets, the first distributor, the channel bet, the hard moment, the system that made it scale, what's next. Not a CV: no school-to-jobs march.

**§ 02 Industry Context** (the bridge, about 180 words)
- A data grid of 4 to 6 named benchmarks on the guest's category and route to market (market size, channel mix, quick commerce share, distributor economics, sales force productivity), each with a **clickable source**.

**§ 03 Interview Angles**
- 4 to 7 stations in the order of the story. Each has:
  - a station title naming the moment ("The year the distributors walked", never "Distribution strategy");
  - **THE ANGLE**: a conversational opener in Divir's voice, peer to peer, one or two sentences;
  - 2 or 3 specific follow-ups, each naming a fact, person, moment or benchmark;
  - *land here*: what a great answer sounds like.
- The playbook surfaces in a middle station as the guest's answer; mark that station's land-here as THE clip.
- One station is about what didn't work.
- Every number-relevant angle leans on a § 02 benchmark; none asks for a number directly.

**§ 04 Tread Carefully**
- One light callout: the single most delicate thread, and the soft way in.

**§ 05 Sources**
- Every figure and quote with a **clickable, verified link**, grouped (benchmarks / company figures / quotes), filing-grade vs prep-grade flagged. If a link won't resolve, write "verify live" instead of faking a URL.

**Look and feel.** Clean editorial page: a serif for headings (Playfair Display), a sans for body (DM Sans), a mono for labels (DM Mono), white background, one accent colour. Section labels read just `§ 0X  <Name>`. No production meta: no stage breadcrumbs, no "working draft", no distribution brief, no clip plan.

## Voice rules: Host Dossier

- Internal to Divir. Confident, plain, peer respect.
- **No em dashes** anywhere.
- Concrete numbers wherever possible. Unknown means "unknown" or "reported range"; never fabricate.
- No badges or "verified / unverified" tags on individual claims. If something is too shaky to state cleanly, leave it out.
- Never mention FieldAssist's product, pricing or a sales pitch to the guest. The conversation is about the guest's playbook. If the guest is a FieldAssist customer, note it once in § 04 as context for Divir, never as an angle.

## Voice rules: Guest Prep Note

Different audience: the guest. First person from Divir. About 500 words.

- **Peer to peer, operator to operator.** Divir is a fellow builder who has spent a decade on route to market, not a journalist.
- **Facts about the show come only from the Pathfinders pitch sheet** on the Notion page "Client show mails" (decision 306). A line there marked "to confirm" never goes in the note.
- **Format bullet:** about an hour of conversation, with 75 minutes blocked; remote, or in person at FieldAssist's new studio in Delhi NCR. Don't name a recording platform or a link until the pitch sheet has one.
- **Never mention edit rights, review, approval or seeing the episode before release**, in any form (Akshay, 17 Nov, engagement chat seed).
- **No specific questions in the note.** Broad territory only.
- **Bulleted "How the conversation will run":** five bullets covering format, style, the theme, what Divir will lean on, and what he's most interested in. No pre-call bullet.
- **One pull quote**: a single italic line that sets the tone.
- **End with a P.S.** inviting the guest to reply if anything sits wrong (a topic or a name they'd rather we not raise), framed as "much rather hear it in advance than discover it on the recording", without promising a call.
- No "deep and real" framing. No prices or fees, ever.

## Pre-delivery checks

### Required
- [ ] § 01 The Journey LEADS: at-a-glance card plus chronological story, before § 02
- [ ] The story is about building the business and its reach, not a CV
- [ ] At-a-glance card has exactly four rows: frame / shape of them / words to play back / soft landings
- [ ] § 02 has 4 to 6 named benchmarks, each with a CLICKABLE source
- [ ] § 03 has 4 to 7 stations in chronological order, each with THE ANGLE, 2 or 3 specific follow-ups and land-here
- [ ] THE ANGLE boxes read in Divir's conversational voice, not as benchmark paragraphs
- [ ] No angle asks for a number directly
- [ ] The playbook surfaces in a middle station, marked THE clip; one station covers what didn't work
- [ ] § 04 is ONE light callout
- [ ] § 05 grouped, every link VERIFIED, filing-grade vs prep-grade flagged
- [ ] No em dashes in either file
- [ ] Guest Prep Note is 480 to 580 words
- [ ] Guest Prep Note uses only pitch-sheet facts, nothing marked "to confirm"
- [ ] Guest Prep Note never mentions edit rights, review, approval or a preview of the episode
- [ ] No price, fee or FieldAssist product pitch in either file
- [ ] Dossier link written to the guest's Pathfinders Engagement, or the reply says why not (Stage 4)

### Optional (use when it fits, drop otherwise)
- [ ] **Timely hook**: a fresh event that drives the conversation (results, a launch, a market entry). Don't force it.
- [ ] **Extra journey beats**: up to 8 when the build has more distinct phases.
- [ ] **Extra stations**: up to 7; drop to 4 for a simpler arc.

## Defensive notes

- **Don't thin out the research.** Six lazy searches and a confident tone make a dossier that collapses the moment Divir uses a number in the room.
- **Don't stop mid-run to ask permission.** Ask only if the input is genuinely ambiguous (two people with the same name, a company that can't be identified).
- **Don't include themes that would work for any guest.** "Distribution in Bharat" is a category. "Taking a ₹50 product to 2 lakh outlets without a single super-stockist" is a theme.
- **Don't fabricate outlet counts, distributor numbers or Glassdoor patterns.** If the data isn't in the research, say "signal unclear".
- **Don't ship an unverified Sources link.**
- **Don't write THE ANGLE as a script.** One or two sentences Divir would actually say to a peer.

## Apify step

The Built to Share dossier skill this was cloned from had no Apify research step on 19 Nov. When one lands in bts-host-dossier, port it here (decision 626).
