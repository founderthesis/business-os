---
name: "un-dossier"
description: "Build the pre-interview prep pack for a guest going on un# (Unhashed), Sri Misra's crypto podcast. Trigger on \"un-dossier\" plus a guest name, LinkedIn URL, company or backgrounder. Two phases with a hard STOP for Grok research, then a dark host dossier published as a page with a markdown copy Sri can mark up, and a link-only guest prep note carrying a conversation outline. Ends by logging the Dossier link on the guest's Engagement in the Business OS (Notion)."
---

# un-dossier

Pre-interview prep for Sri Misra, host of un#. Two jobs, and the skill fails if it does either badly.

**Job one: find what Sri would otherwise find himself.** He said it directly on 27 May 2026, about the Goldfeder episode: "he has made some tweets which are very important ones and which is what I started with and there is no more reference in that Lord [Claude]... I just did my diligence of looking through the profiles. Secondly I knew about that other important thing which had happened, which was that their whole decision to freeze assets, we spent like 20 minutes discussing that. So don't relegate this to claude only." Those were the two best segments of that episode. Neither came from the brief.

**Job two: write questions he would actually ask.** A dossier full of sharp, clean, adversarial questions is a different host's dossier. Sri's questions look nothing like that, and the shape is documented below.

Read `claude/sri-interview-method-2026-09.md` in the project if it is available. It is the full evidence base from 44 transcripts. The rules below are the operative summary and are authoritative where they differ from anything else.

## Era warning

The transcript archive splits in two and the older half will mislead you.

The **older** episodes, from before the show was un#, had the guest read their own bio, ran a founder toast with a real drink in every episode, and opened on a bare definitional question. All of that is gone.

The current **un#** era opens "[Name], welcome to Unhashed", records the bio separately as a VO, has no toast at all, and opens on the present: breaking news, the guest's own recent statement, or a demystify-this ask. Generate for this era. Never put a toast prompt in a dossier.

## Inputs

Any of: guest name, LinkedIn URL, company or protocol name, a PR backgrounder, pre-call notes (often a Gemini-exported call between Akshay and the guest), a recording date.

Extract every name, URL, role, number and date before doing anything else. Pre-call notes are high value: they carry the guest's own current framing, which is usually broader than the web picture, plus confirmed logistics and candid admissions.

## Outputs

Two published pages and one markdown file. The two documents have different readers and different jobs, so they ship differently.

1. **The host dossier, published as a page** with the Artifact tool. Dark theme, aarna teal on charcoal, jump links. The primary artefact.
2. `/mnt/user-data/outputs/un-dossier-<lastname>.md`: the same content in plain text. **This ships every time, without being asked.** Sri marks it up, cuts themes, reorders them and adds his own questions before recording, and a published page gives him nowhere to do that.
3. **The guest prep note, published as a page.** The link is the whole delivery, because it gets pasted into an email or a DM to the guest. No markdown copy: a second file in a folder only creates a version that drifts out of sync with the page.

The markdown file delivers itself when written with Write or Edit. Do not call a separate present tool. Hand over the dossier link, then its markdown, then the guest note link, then log the dossier in Notion (last section below).

**The markdown is a real conversion, not a dump.** Page furniture (nav, jump links, styling hooks) becomes headings, bold labels and lists. The reading order stays identical, and nothing that exists on the page goes missing from the file.

Both pages are private on publish. Say so once: Sri and the guest cannot open their links until Akshay shares each page from its Share menu.

---

# Phase 1: research

Two parallel jobs. Never skip either.

## 1a. Web search, immediately

Do not wait for Grok. Run these:

1. `"<Guest>" <Company>` for role and recent press
2. `"<Guest>" linkedin` for the profile if not supplied
3. `<Company> funding OR raise OR valuation` for current scale
4. `<Company> "2026"` for the recent quarter and recent moves
5. `<Guest> podcast OR interview` for existing long-form, and what he has already said elsewhere
6. `<Company> hack OR exploit OR freeze OR lawsuit OR controversy` for the incident sweep, and **date every hit**
7. A search on the guest's own public thesis or signature phrase
8. If recording is this week: a fresh sector-news search for something live the guest can react to

`web_fetch` two or three substantive pieces: the most recent long interview, the most recent thesis post, any live incident. Skip the company's own marketing pages.

## 1b. Emit the Grok prompt, then STOP

Grok has live X access and is materially better than Claude at recent-post mining, which is the exact gap this skill exists to close. Output this in a copyable code block, filled in:

```
Deep research on [GUEST FULL NAME], [ROLE] at [COMPANY]. X handle [@HANDLE].
I am preparing interview questions for a recording on [DATE]. I need what a
profile-scroll would surface and a press summary would not. The conversation
is a peer-to-peer founder conversation, not a prosecution, so I need the
evidence for what is working as seriously as the evidence against.

1. RECENT POSTS. Everything [@HANDLE] has posted or quote-tweeted in the last
   60 days that states a position, announces something, picks a fight, or puts
   a number in public. Give me the VERBATIM text of each, the date, and the
   link. Prioritise: posts that contradict something they said earlier; posts
   where they argue with a named person; posts with a metric in them. Do not
   summarise. I need their exact words.
   On coverage: a from:handle search usually returns a capped sample rather
   than the full timeline. Supplement it with topic searches on the company
   and product names, and TELL ME what your coverage actually was and what
   you may have missed. Extend past 60 days wherever a named incident,
   reversal or announcement sits just outside the window, and label anything
   you pull from outside it.

2. WHAT IS ACTUALLY WORKING. The case FOR this company, in evidence rather
   than marketing. What have they shipped in the last 12 months that landed?
   What do customers, partners or competitors say is genuinely good? Which
   metric is growing and on what basis? What did they get right early that
   others missed? If a respected person in the sector has praised them
   publicly, quote it with a date. I need this to build the parts of the
   conversation that are not a challenge.

3. LIVE INCIDENTS. Anything that has happened TO the company or that the
   company has had to DECIDE in the last 6 months: an exploit, a freeze, a
   depeg, a governance vote, an outage, a rug by a partner, a regulatory
   action, a public dispute, a product pulled, a term-of-service rewrite.
   For each: what happened, the exact date, what the company chose to do, who
   made the call, and who publicly criticised it. Separate anything older than
   12 months into its own list and label it clearly, so I do not confuse an
   old incident with the current one.

4. THEIR OWN NUMBERS. Every figure this person has stated publicly in the last
   12 months about their company: TVL, volume, users, revenue, AUM, valuation.
   Give date and source for each. Flag any figure that CHANGED between two
   statements, and quote both. Also flag any figure that has NOT changed when
   it should have, for example a headline number repeated unchanged for
   months alongside claims of fast growth. Say plainly where a figure's
   measurement basis is undefined in public.

5. SECTOR NUMBERS. The current figures for the category this company sits in,
   as of this month: total market size, the comparable metric for the two or
   three nearest competitors, the going rate or fee or yield in this segment,
   and the direction of travel over the last year. I use these to frame
   questions, so they must be current and sourced. A stale sector number is
   worse than none.

6. DISAGREEMENTS. Where has this person publicly taken a position that others
   in the space dispute? Who disputes it and what is their argument? Include
   replies and quote-tweets against them.

7. THE UNANSWERED QUESTION. Business and product questions this person has
   been asked directly and has not answered cleanly, on X or on a podcast.
   Quote the question, name who asked it, link it, and say what the nearest
   thing to an answer was. Skip personal, political and lifestyle material,
   which I will not use.

8. RECENT LONG-FORM. Podcasts, panels, AMAs, Spaces in the last 6 months. For
   each: date, where, and the two or three things they said there that they
   have not said elsewhere.

Rules: date-stamp everything. Link everything. Quote verbatim rather than
paraphrasing, and never format a paraphrase as a quotation. If you cannot
verify something, say so rather than asserting it. If I have named a specific
figure, quote or event in this prompt and you cannot find it, say so
explicitly and do not assume I am right. Distinguish the company's own claims
from independently reported facts.
```

Then close with exactly this line and stop:

> **Run this in Grok with Deep Research, paste the output back here, and I'll generate the prep files. STOPPING for Grok research.**

Generate nothing else. If Akshay comes back with "just generate it" or something that is clearly not Grok output, proceed but write "(no Grok pass, recent-post signals may be incomplete)" into the dossier header.

---

# Phase 2: build

## Gate one: fact-check every premise before writing a single question

Sri builds questions on premises and gets corrected on tape roughly once per episode. Three of five transcripts in one sample contained at least one. "you build on polygon CDKs" met "No, actually we build on the Ethereum." That is a question wasted and a small credibility hit.

Before any theme is written:

- Every number gets a source and a date. If two sources disagree, say so in the dossier text rather than picking one
- Every claim about what the company does gets checked against a primary source, not a press summary
- Anything you cannot verify either gets left out or gets hedged inside the sentence ("reported at", "he has put it as high as")
- **A quote block contains verbatim text only.** If you are summarising, write it as prose. A paraphrase formatted as a quote is a fabrication, and it is worse here than usual because Sri will read it out
- **A figure nobody can source gets dropped, not hedged.** If the Grok pass reports that a number cannot be found, it does not go in the dossier in any form, and no theme is built on it. This has already happened once: a Pathy dossier built a whole theme on a "$12B annualized volume" post that does not appear to exist, while the company's own comms had been repeating $5B unchanged for six months. The unchanged number was the better question. When a claimed figure evaporates, look at what the surviving numbers actually say

## Dossier structure

**Header.** Guest, company, role, recording date, X handle.

**Background block, at the TOP.** Two prose paragraphs, moved here at Sri's explicit request in June 2026. Never bury it at the end.
- *Guest in brief*, 70 to 90 words: career arc, prior ventures, and the bet they made
- *The firm*, 70 to 90 words as its own paragraph: what it is, where it runs from, scale, backers, and what has moved recently

**Write this block plainer than the rest of the dossier.** It is orientation, and Sri reads it in about fifteen seconds. Short declarative sentences. Plain verbs.

- **No registration numbers, CNPJs, filing IDs or legal entity names** unless one of them is load-bearing for a theme. Comoros incorporation matters. "KAST Tech, Reg No. 16223" does not
- **No sourcing hedges inside the sentence.** "Live in 170 countries" beats "live across 170 countries by its current product pages". Put the uncertainty in the theme where it does work, or leave it out
- **Attribute company claims once, plainly.** "KAST says it has over a million users" does the job that "Company figures: over one million users, stated at the Series A and unchanged in comms since" does badly
- **No stacked appositives.** If a sentence has three commas doing the work of three clauses, split it

**The angle.** One paragraph. The single sharpest reason this conversation matters now, ideally a tension, ending on the most current hook.

**Pre-call callout**, only if a pre-call actually happened. A short highlighted block capturing the guest's own framing, which themes absorbed it, and confirmed logistics. This is the guest's own words, not comms-team intel.

**How to use this.** One line, then the numbered theme index as jump links.

**Themes, 5 to 7.** Spec below.

**The close.** One horizon question. Spec below.

**Note and links.** One caution if there is a real one. Compact links, no narration. The bio does not repeat here.

**Intro VO.** Final section.

## Theme spec

Each theme is self-contained and carries five parts, in this order.

**1. A specific title.** The guest's own phrase where there is a good one. "Reserve's honest secret" passes. "Tokenomics" fails. The test: could this title belong to any other guest in the category? If yes, rewrite it.

**2. Context, with the thing that powers it.** The post, stat, event or decision, with its date and an inline link. Mandatory. A theme with no grounding is the "no real context" failure Sri named.

**3. One crystallisation.** See below. This is the most under-used device in past dossiers and the highest-yield one.

**4. Two or three questions, written in his grammar.** Single asks, not stacks.

**5. A press ladder.** One or two short reframes to deploy if the first answer goes vague. Sri presses twice at most and his second press is always short and reframed rather than repeated.

Order the themes in a logical arc and number them. The default arc runs credibility, then thesis, then live proof, then why it holds, then why it might not, then frontier, then zoom-out. **Treat it as a default you may break.** When the guest does not fit it, break it and say why in one line under the theme index. A regulator, a protocol founder and a sector analyst do not share one shape. An arbitrary pile drew the "the flow seems a bit random" critique; a forced arc produces a dumb dossier. Order it deliberately and defend the order.

**At least two themes must come from the case FOR the company**, built off section 2 of the Grok pass. The live-proof and why-it-holds slots are not filler. A dossier where every theme is a challenge has turned Sri into a prosecutor, which is the same failure as writing journalist questions, wearing different clothes.

Flag the **spine** (the sharpest tension) and any **breaking** theme. Place breaking where it fits the arc, not forced to the front. The tag lets Sri open cold on it if he wants.

Each idea appears in exactly one theme.

---

# Sri's question grammar

This is the section that decides whether the dossier is usable. Past dossiers failed here, not on research.

## The shape

His questions are **bimodal**. Either under 20 words, or 60 to 190 words with the interrogative in the last clause. There is almost nothing in between. A clean 25-word single-clause question is off-voice, however sharp it is.

The long form carries, in order: his own read on the situation, at least one number he supplies himself, then the ask.

> "There's a BCG Ripple report at nineteen, Ark Invest is saying eleven, Cities at five to six, McKinsey at two to four, and today we're at thirty-four billion. So you can see the wide divergence in this. And what's your thinking?"

> "in terms of the whole ecosystem, there's around, I think 11 billion circulation. If you take DAI, 4 billion, along with 7 billion of USDS. Roughly around three and a half goes through Sparks allocation. Who are the other two?"

**Write the preamble.** Do not write a bare question and assume he will build the runway. Supplying the runway, with a checked number in it, is most of the value. Section 5 of the Grok pass exists to feed exactly this, so use those figures rather than reaching for whatever is nearest.

## The crystallisation, built to be corrected

His highest-yield device. He states his own model of the thing and hands it over. Guests reject it about half the time, and the rejection is the good tape.

> "So Spark is the whole full stack asset management or capital allocation layer over the sky ecosystem as one of the major hubs. Is that how one should understand it?"

> "if I were to take a step back and draw an analogy, you're building the aladin of digital assets." The guest's reply: "That one I did hear before. We're not."

> "in New York parlance, do you refer to them as subnets? Is that how one should understand that?" The guest's reply: "No, I don't think that's quite right."

**Write one per theme.** Make it a real, committed, falsifiable model of the business, not a hedge. A crystallisation the guest can only agree with is wasted.

Launch phrases: "if I were to rephrase what you said" / "if I were to kind of deconstruct that" / "Got it, so it's basically" / "correct me if I'm wrong" / "Is that how one should understand it?"

## Comprehension checks

Roughly one turn in three is him compressing a long answer into one sentence and handing it back. It is what he does instead of interrupting, and he improvises all of it live. Pre-drafting these is the single most useful thing the prep can hand him.

> "And this is basically multi sig."
> "So it's like the on-chain Swift basically."
> "So just to be clear for everybody, it's not a primary issuance. There's already a secondary. It's a digital reflection or a tokenization of an existing."
> "And the cross-chain bridges, are they like the new mixers?"
> "So we are introducing the whole element of trust here into what's supposed to be all trustless architecture. And the trust is residing where?"

**Ship a dedicated block of five to eight**, one line each, one per concept in this episode that a wider audience will not follow. He told a guest why he does it: "the audience is not only DeFi, it's wider."

## Pushback register

He challenges the architecture and the market logic. He does not challenge the person.

**Concede first, then counter.** "Yeah, no, very true. But at the same time, I also feel..."

**Attribute the objection.** "purists in the space" / "naysayers of the space have always been saying" / "I get asked this every time by any TradFi participant" / "crypto bros"

**Credit the guest's own values before landing it.**

> "Is there a risk of platforms like yours becoming gatekeepers for DeFi when DeFi was supposed to be completely accessible, permissionlessly for everybody? And as somebody who also passionately believes in the ethos of crypto, how do you balance this?"

**Never run a gotcha about the guest's own incident.** He said why, off-record: "you're running a centralized exchange, so I didn't want to go too much deeper into that."

But he is not avoiding controversy. He spent 20 minutes with Goldfeder on the Kelp DAO freeze and raised the same incident again with Sam at Spark. **The difference is he asks it as a systems and decision question, not a character accusation.** This is the model:

> "how difficult was the decision more recently... walk us through that whole decision making system and where you stand on this whole requirement for recourse. And secondly, as somebody who comes with the old foundation of decentralized systems, how do you balance this in the very core architecture?"

So: take the ugly thing, and ask what it reveals about how the system should be designed. "Is my money still mine" is an accusation. "What does custody actually mean in a business that takes stablecoin balances, and where did you land on it" is the same territory, and he will actually ask it.

**Supply ammunition for the second press.** He presses withheld facts well and folds on contested opinions immediately, announcing the retreat out loud ("I'll let that pass"). The only thing that reliably gets him a second push on an opinion is an on-record contradiction from the guest's own past words. Section 7 of the Grok pass is built to find these. Put one in the press ladder.

## What to route toward

His standing obsessions, in order of how reliably he gets there regardless of subject. **Check the finished dossier against this list.** If a guest touches one of these and no theme covers it, that is a miss.

1. **Liquidity**: fragmentation, depth, slippage, price impact. He raises it at a tax company and at a security company
2. **Tokenization, and what it actually fixes**: never "is it real", always which problem. "Just tokenizing for the sake of tokenizing really doesn't make sense"
3. **Decentralisation purity against the institutional turn**: his most reliable source of genuine tension
4. **Institutional adoption mechanics**: what specifically is blocking them, who moved first
5. **Regulation as a constraint on builders**: what it prevents you from doing. He holds an original position that regulation itself should be borderless
6. **Composability and collateral**: can this be posted as collateral, looped, borrowed against
7. **The $300bn stablecoin pool as the new capital market**: same number, same framing, in at least five episodes. If the guest touches stablecoins at all, this belongs in the dossier
8. **The reverse flow**: which direction does traffic move, TradFi onto chain or crypto into wrappers
9. **Vaults as the future of asset management**: his personal thesis, inserted whether or not the guest raised it
10. **Timelines**: at least one "when" question with a number demanded

**One forced mechanic question per dossier.** He turns abstractions into a worked case and it is distinctive:

> "can I as a holder of a particular vault token be able to collateralize that on any lending platform, take a USDC loan against that and be able to use it for a leverage loop strategy?"

**One aarna insertion point.** He names aarna Protocol in nearly every episode, framed as a shared engineering problem rather than a plug. Give him the hook: where does this guest's problem overlap with what aarna is building.

**India is conditional.** It appears constantly but mostly as his *own* pre-roll positioning, not as a question. Generate an India or emerging-markets question only when the guest has a real surface for it: remittances, capital controls, emerging-market credit, dollar access. When there is one it is strong, and he has a line he reuses: "India has the largest inward remittance market in the world." When there is no hook, leave it out.

## Backstory placement

Late. 70 to 85% of the runway. Measured arrivals: Sam 43:13 of 51 minutes, Vivek 49:10, Yat 54:42, Alexander 50:51 of 68. In two episodes it never arrives.

Never Theme 1. The on-ramp is a demystify question, not a biography question.

His origin questions are corporate and numeric: "how did you land up at GSR", "what was the AUM at that point in time", "when did you get orange-pilled". Across 44 transcripts there is one personal-life question. **Do not write:** the hardest month, the low point, what kept you up at night, childhood, family, mentors.

Give the backstory theme a callback line to the opening question. He does this out loud: "that's why that was my opening question when we started out."

## The close

One question. Always a horizon with a number attached.

> "Jim, what would a successful tokenized capital market look like to you in 2030?"
> "what would be your three-year projection around what sky issuance will be at? Where do you see your TVL? Just paint that picture."
> "Let's take a one and a half year from now and a three year horizon. What's your take on the TVL?"

Put it in the dossier as its own short section after the last theme, not buried inside one.

## Gate two: the polish pass, before anything ships

Run this over the finished dossier body. It is the `post-polish` craft applied to prose nobody will edit again, and it is a subtraction pass: nothing here adds a word.

**The disposition:** a grammatically correct sentence carrying true information can still be cut. Polish is weight-checking, not error-finding. Connective tissue is where AI writing shows, so when in doubt about a transition, cut it.

**Flag and rewrite every instance of these.**

- **Negative parallelism.** "The question is not whether X. It is whether Y." / "Business was not a roadmap item, it was a leak." Banned outright, and it is the tell that survives longest because it reads as insight. Make the positive claim and stop
- **Self-import.** "This is the thing I find genuinely interesting rather than the thing Twitter found interesting" / "what most people miss" / "a rare thing about". The observation should carry itself
- **Telegraphed contrast.** "But here's the thing", "Here's where it gets interesting", "The plot twist is". A good contrast happens without announcement
- **Connective tissue.** "What I find more interesting is", "This is where", "It is worth pausing on", "Let's turn to"
- **Borrowed clichés.** "Said the quiet part out loud", "the elephant in the room", "moving the goalposts". They read as borrowed because they are
- **Restating what was just shown.** "That is the tension this theme is built on", after the tension has been demonstrated
- **Three fragments doing one job.** Stacked short fragments all expressing the same idea. Keep the best one
- **Hedges before a real claim.** "While X is true, Y matters more" should just be the Y claim
- **Precious closing clauses.** "where the callback lands hardest", "which is the whole point". Stop at the fact
- **Throat-clearing first words.** A paragraph opening on "Now," "So," "Well," "Frankly"

**Then the subtraction sweep.** Sentence by sentence: is this claim made elsewhere, is it setting up a sentence that stands alone without it, is it connective tissue between two sentences that could sit next to each other. Cuts compound, so the second sweep finds what the first one's new rhythm exposed.

**What this pass does not touch.** Sri's own verbatim quotes, the guest's verbatim quotes, and the questions written in his grammar. His questions are deliberately long and full of "sort of", and tightening them into clean prose is the exact failure this skill exists to prevent. Polish the dossier's own writing: context paragraphs, the angle, the background block, crystallisations, notes.

## Voice rules for the dossier body

- Internal-tool voice. Direct and blunt. This is Sri's read, not PR
- **No em-dashes.** Commas, parentheses, or two short sentences
- **Banned:** exciting opportunity, great potential, amazing journey, powerhouse, thought leader, game-changing, passionate, world-class, trailblazing, pioneering, revolutionary, disruptive, deep dive, unpack
- Concrete numbers everywhere. If a number is unknown, write "Unknown". Never guess
- No coaching notes under questions. No "why this lands". Sri cut them as noise
- Posts live inside the theme they power. No standalone recent-posts list
- Do not recycle the company's marketing language

---

# The host dossier page

Published with the Artifact tool. **Load the `artifact-design` skill before writing it**, and write page content only: no doctype, html, head or body tags, since the tool wraps the file in its own skeleton. Put the `<title>` and `<style>` at the top.

Title it as a name, two to four words, identifiable in a gallery of other artifacts. "Raagulan Pathy dossier" works. "Host dossier" does not.

This page commits to a single dark theme by design, which the artifact contract allows as long as every colour is painted explicitly and nothing is left to inherit from the host ground. Define the full palette on bare `:root`, set `color-scheme: dark`, and give `body` an explicit background. A sticky header uses `top: env(safe-area-inset-top, 0px)`, never `0`.

Inline all CSS. Google Fonts is the only external host the page may use.

Dark theme, aarna palette.

```
--bg:#0E1010  --surface:#171A1A  --raised:#1F2423  --rule:#2C3030
--ink:#E8EAEA  --ink-soft:#B5BCBC  --ink-mute:#6B7474
--teal:#1FBFB0  --teal-deep:#0FA095  --teal-glow:#6FE5D8
--coral:#C97A4B
```

Fonts: Manrope for body and UI, Newsreader for the angle and pull quotes, JetBrains Mono for numbers, dates and tags. Load from Google Fonts with a system fallback stack.

Layout:
- Sticky header with the guest name and a numbered theme index as jump links
- Background block and angle at the top, angle set in Newsreader at a larger size
- Each theme as a card on `--surface` with a teal left border. Breaking themes take `--coral` instead. Spine gets a teal filled tag
- Context paragraph in `--ink-soft`, quotes in a bordered block with the date and link in mono
- Crystallisation in its own visually distinct box, labelled, so Sri can find it fast
- Comprehension-check block styled as a compact list, since he scans it mid-recording
- Questions numbered, press ladder indented under them in `--ink-mute`
- Max width 860px, generous line height, and it must read on a phone, because that is where Sri reads it
- Theme cards get `scroll-margin-top` clear of the sticky header, or the jump links land under it

## The markdown file

Write it every time, alongside the page. It carries identical content in the same order, and it is the copy Sri works on: he cuts themes, reorders them, strikes questions and writes his own in. Markdown is the only format that lets him do that.

So it has to survive editing. Plain headings and bold labels, no HTML left in, no styling hooks, nothing that breaks when he deletes the paragraph above it. Jump links become a plain numbered index, the crystallisation box becomes a bold **Crystallisation.** label, the press ladder becomes an indented sub-list under its question.

---

# The guest prep note

A published page, and the link is the whole delivery. It goes out once the guest has shown interest but before the date is locked, so it carries two jobs at once: tell them what to expect, and quietly confirm they want to do it.

Akshay's voice, founder to founder. Warm, specific, logistics-clear. Written to the guest, never about them.

This is **not** the sell document. The `guest-note` skill does that job, with reach figures and a case for coming on. This one assumes interest already exists, so it makes no audience claims and never argues for the show.

## How it ships

Build a self-contained HTML page and publish it with the Artifact tool. Akshay gets a link he can paste into an email or a DM, and the guest can reopen it or forward it to whoever handles their calendar. **Load the `artifact-design` skill before writing the page.**

No markdown copy for this one. Nobody edits it, and a file sitting in a folder just becomes a stale second version of a page that can be updated in place.

Light theme, the aarna palette the host dossier inverts:

```
--bg:#FAFAF6  --paper:#FFFFFF  --rule:#E4E2DA
--ink:#0E1010  --ink-soft:#2C3030  --ink-mute:#6B7474
--teal:#0FA095  --teal-deep:#0E7F76
```

Unlike the host dossier, this page renders in the guest's own theme, so give it the full three-state treatment: light tokens on bare `:root`, a dark set under `@media (prefers-color-scheme: dark)` guarded as `:root:not([data-theme="light"])`, and the same tokens again under `:root[data-theme="dark"]`.

Newsreader for the page title and section headings, Manrope for body. Quiet and readable, closer to a letter than a deck.

Title it for the guest, not for the system. "un# with Sri Misra" works. "Guest prep note" does not.

No email furniture. No "Hey [Name]," opening and no "Best, Akshay" sign-off. It ends on one warm line and a byline.

## What goes on the page, in order

**1. A one-line frame.** What un# is, in the guest's terms. Never "Sri Misra's show on aarna Protocol", which reads as though the show is about the company. Sri has been explicit that the podcast is delinked from aarna.

**2. Who Sri is, and why that matters.** Two or three sentences. Second-time founder, built and sold Milk Mantra after more than a decade, now building aarna Protocol and launching a regulated tokenization platform for Indian financial assets. This is what makes it a peer conversation rather than a press interview, and it is the thing most likely to make a founder say yes. The old version left it out entirely.

**3. Recent guests, chosen for this guest.** Three or four names from the **current** roster, not whoever appears first in the archive. Pick for relevance: a guest talking stablecoins should see the stablecoin and payments names. Where a name connects directly to the guest's own history, lead with it. Use the same names the dossier's own research surfaced, and never a guest older than about six months.

**4. The conversation outline.** The section below. This is the part guests actually read.

**5. Format and logistics.**
- Riverside, link sent ahead, quick A/V check at the top
- 90 minutes held, roughly 60 minutes published
- **Sri records the introduction separately**, so the conversation starts cold with a welcome. Say this. Guests are visibly thrown when it happens unannounced
- Headphones help, and a window behind them does not
- No edit rights and no review before publishing. One sentence, stated plainly. Do not justify it, do not explain what it protects, do not apologise

**6. Where it goes afterwards.** YouTube, Spotify and the other podcast platforms, the newsletter, and clips on LinkedIn. Name the channels. No subscriber or view numbers, since this is a prep note and numbers belong to the sell document. A guest deciding how much effort to put in wants to know where it lands.

**7. The close.** One line looking forward to it. A byline, not a signature block.

## The conversation outline

The addition that matters most, and the thing the previous version had no version of. Six topic bullets is a list. An outline gives the guest the shape of the hour.

Build it from the dossier's own themes, in the order the dossier puts them, then strip out everything rehearsable. Six to eight lines, one line each. Because the hour genuinely is a sequence, a timeline treatment with phase markers is honest here rather than decorative.

**Rules:**

- **No question marks anywhere in this section.** If a line could be answered, rewrite it as territory. "How Reserve's economics actually work" is territory. "Whether the yield is sustainable" is a question in disguise and will be prepped against
- **Say that it opens on the present**, on where the company is right now, rather than on their career. This is true and it surprises people
- **Say that their own story comes later**, past the middle. Guests arrive ready to lead with the origin story and are thrown when it does not come. Telling them is useful and it is a real differentiator
- **Say that Sri will restate things in plainer terms as they go**, because the audience runs wider than DeFi. It reads as courtesy and it stops guests treating a comprehension check as a challenge
- **Say that it closes on a forward view with numbers attached**, so they can decide in advance whether they want to commit to one on tape
- Where the dossier's spine rests on something contested, **name the territory neutrally and do not hide it**. "The custody conversation from July, and what account structure should look like for a business holding stablecoin balances" is fair warning without being an ambush, and it matches how Sri will actually ask. A guest who is surprised on tape makes worse tape
- If the guest asked for a topic, it appears in the outline so they can see it is covered

## Voice rules for the guest note

- Contractions throughout. This is a person writing to a person
- No em-dashes
- Say the agile thing **once**. The old version promised the same flexibility three separate times
- No hype about the show and no adjectives doing work that facts should do
- Specifics over reassurance. "90 minutes held, roughly 60 published" beats "it won't take long"
- Gate two applies here too, and harder. This page is read by someone outside the company

---

# The intro VO

Final section of the dossier, page and markdown both. Titled "Intro VO (record after the conversation)".

Pre-interview mode: the recording has not happened, so the tease is topic territory, not quotes.

**Five variations at 55 to 75 words**, each labelled with its hook angle, plus a one-line recommended pick with the reason.

Structure, in this order: macro context first, then the guest, then the tease. It does not open with the guest.

**Closing line is fixed:** "Let's find out more on Unhashed." or "Let's look into this with [Guest Name] on Unhashed." The show name lands in the closing slot. He says "Unhashed" on tape, never "un#".

**Also ship one bio card**, which is the short form he actually records in take sessions. One sentence, the formula is `[Name] is [credential], the [role] of [company], [plain-English decode of what it does]. And now, he's building [current thing].`

> "Joseph Onorati is a crypto OG and is the founder of DeFi Development Corp, a US listed digital asset treasury company or a DAT that invests in Solana."
> "Arthur Breitman is the co-founder of Tezos, known for on-chain governance and energy-efficient staking. And now, he's building Etherlink."

**Accuracy gate on the decode clause.** In one recorded VO session Sri killed three drafts purely on technical precision: "But the other one is not correct" / "This is not technically correct" / "This is not correct also, this is not what they are doing. They are not doing that." The one-line description of what the company does must be exactly right. Check it against a primary source, not a press release headline.

No em-dashes, no markdown, no unexplained jargon. This is read aloud.

---

# Defensive notes

Each of these is a real failure, not a hypothetical.

- **Don't skip Phase 1b.** Even with good web results, the Grok prompt and the stop are mandatory. Skipping it is the failure this skill exists to fix
- **Don't write clean journalist questions.** Sharp, short, single-clause and adversarial is the wrong host. Preamble plus his own number plus the ask
- **Don't open Theme 1 on backstory.** It is the single most common structural error. Backstory goes at 70 to 85%
- **Don't write an emotional origin question.** No hardest month, no low point, no childhood
- **Don't accuse the guest.** Take the controversy and ask the systems question underneath it
- **Don't ship a dossier with no comprehension checks.** One turn in three is this move
- **Don't ship a theme with no crystallisation.** His highest-yield device
- **Don't format a paraphrase as a quote.** Verbatim only inside quote marks, with date and link
- **Don't confuse incidents across time.** The original Goldfeder dossier put a 2023 governance episode where the 2026 incident belonged. Date every incident, and when there are several, list them with dates and flag the most recent
- **Don't file by source type.** No standalone Signals or recent-posts section. Every post lives in the theme it powers
- **Don't repeat an idea across themes.** Once, where it lands hardest
- **Don't write a theme that would work for any guest in the category.** "Tokenomics" is a category, "Why ARB holders see $0 of $26M ARR" is a theme
- **Don't generate a toast prompt.** That ritual ended with the older episodes
- **Don't ask about valuation, cap table, burn, runway, raise size or headcount.** He asks how a business makes money as a mechanism, never the number
- **Don't ask about hiring, team or culture.** He never does
- **Don't add an India angle by default.** Only with a real hook
- **Don't build a PR-intel section.** Sri cut it. A pre-call callout from the guest's own words is different and is allowed
- **Don't surface a confidence-flag legend or a verify-list.** Keep the no-fabrication discipline, note real uncertainty inline in a phrase, and leave the scaffolding out
- **Don't stack questions.** He does this himself, loses half of them, and has to re-ask twenty minutes later. Single asks, follow-ups in the press ladder
- **Don't ship either page as a loose file.** Both the host dossier and the guest note get published and handed over as links. An HTML file in a folder is not shareable, and the guest note in particular is the only artefact the guest sees, so it is a first impression of how the show is run
- **Don't ship the dossier without its markdown file.** Sri edits before he records, and a published page gives him nowhere to do it. The guest note is the opposite case: link only, because nobody edits it and a second copy just goes stale
- **Don't put a question in the guest outline.** Territory only, no question marks. A guest who can rehearse an answer gives a worse one
- **Don't use stale guest names as social proof.** Pull them from the current roster, pick for relevance to this guest, and drop anything older than about six months
- **Don't put reach numbers in the guest note.** This is a prep note. Numbers belong to `guest-note`, which is the document that wins the booking
- **Don't build the dossier only from the adversarial half of the research.** Two themes minimum come from section 2 of the Grok pass. A dossier where every theme is a challenge is the wrong host again, in different clothes
- **Don't ship without the polish pass.** Gate two is not optional and it is not a formatting check. Negative parallelism in particular survives every other review because it reads like insight
- **Don't load the background block with filing detail.** Registration numbers, CNPJs and entity names belong in the theme that needs them, or nowhere. Sri reads that block in fifteen seconds
- **Don't polish the questions.** They are supposed to be long, hedged and full of "sort of". Gate two applies to the dossier's own prose only

## Last step: log the dossier in the Business OS (Notion)

The team works from Notion, so the dossier has to be findable on the guest's Engagement without anyone pasting links by hand. Run this after the dossier and guest note ship.

1. **Find the Engagement.** Engagements data source `collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5`, un# rows only (`Show LIKE '%3ed19a301a7f8111b5e4d46002a7afe1%'`). Find the guest in People (`collection://e6c44319-7f81-4da6-8b80-8441a4875d7a`) by LinkedIn first, then exact name, then match `Guest LIKE '%<people page id>%'`. If there is no match, or more than one open Engagement could be it, do not guess and do not create one: say so in the chat reply.
2. **The link.** Use the shareable link to the dossier: the published page URL if it was published, otherwise this chat's URL if you have it. If there is no link you can give, leave Dossier link alone and say "add the dossier link by hand" in the reply.
3. **Write.** `Dossier link` = the link. Add one line at the top of `Claude note`: `YYYY-MM-DD: Sri's dossier and guest prep note ready (<link>)`, keeping existing lines below it. `Claude updated` = today. Do not change Status, Next action, Tier, Payment or anything else: the team sends the guest note and moves the status.
4. **Reply.** End the chat reply with one line: `Notion: Dossier link added to <Engagement name>` (or what failed). A failed Notion write never blocks shipping the dossier.

The calendar routine copies the Dossier link into Akshay's private prep entry on its next run.

## The bar

Sri's own fear about his show, stated 6 March 2026, is the standard the dossier has to clear:

> "is it boring content? I might be finding it very exciting to talk to someone else who is in the same boat as me and going into stuff which we both enjoy talking about. So we are both happy but the audience is not. Those are all lost opportunities then."

A dossier that only helps two insiders enjoy themselves has failed. Every theme should be something a smart outsider would want to hear the answer to.