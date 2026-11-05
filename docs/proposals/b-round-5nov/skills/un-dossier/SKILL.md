---
name: "un-dossier"
description: "Build the pre-interview prep pack for a guest going on un# (Unhashed), Sri Misra's crypto podcast. Trigger on \"un-dossier\" plus a guest name, LinkedIn URL, company or backgrounder. Two phases with a hard STOP for Grok research, then a dark host dossier published as a page (TradFi-accessible opener, journey timeline, wider-lens questions, Sri clip points, Word download) with a markdown copy Sri can mark up, and a link-only guest prep note carrying a conversation outline."
---

# un-dossier

Pre-interview prep for Sri Misra, host of un#. Four jobs, and the skill fails if it does any of them badly.

**Job one: find what Sri would otherwise find himself.** He said it directly on 27 May 2026, about the Goldfeder episode: "he has made some tweets which are very important ones and which is what I started with and there is no more reference in that Lord [Claude]... I just did my diligence of looking through the profiles. Secondly I knew about that other important thing which had happened, which was that their whole decision to freeze assets, we spent like 20 minutes discussing that. So don't relegate this to claude only." Those were the two best segments of that episode. Neither came from the brief.

**Job two: write questions he would actually ask.** A dossier full of sharp, clean, adversarial questions is a different host's dossier. Sri's questions look nothing like that, and the shape is documented below.

**Job three: make it a podcast, not a company profile.** Feedback on the Adrian Cachinero (Steakhouse) dossier, October 2026: every question was, one way or another, doing promotional work for the guest's company. A good episode spends real time on the industry, on ideas a smart outsider cares about, and on Sri's own views. Every theme now carries a wider-lens question about the sector, and Sri gets his own clip-ready points.

**Job four: open the door for the crypto-curious.** Every episode opens on a question that a listener from traditional finance, or with no DeFi background at all, can follow. The guest explains their job in TradFi terms before any DeFi vocabulary is used.

Read `claude/sri-interview-method-2026-09.md` in the project if it is available. It is the full evidence base from 44 transcripts. The rules below are the operative summary and are authoritative where they differ from anything else.

## Era warning

The transcript archive splits in two and the older half will mislead you.

The **Alpha Unhashed** era had the guest read their own bio, ran a founder toast with a real drink in every episode, and opened on a bare definitional question. All of that is gone.

The current **un#** era opens "[Name], welcome to Unhashed", records the bio separately as a VO, has no toast at all, and opens with an accessible question that sets up the present. Generate for this era. Never put a toast prompt in a dossier.

## Before anything: check for earlier work on this guest

Search past conversations and list existing artifacts for the guest's name before researching. A guest is often evaluated (un-guest-eval) and partly prepped weeks before recording, and there may be a pre-call, a locked date, PR constraints, or an earlier dossier and guest note already published.

- **Reuse existing artifact URLs.** If a dossier or guest note for this guest already exists, read it and republish to the same URL rather than creating a new link. A guest note link may already be with the guest's team.
- **Carry forward pre-call constraints and logistics** (recording slot, PR contact, topics they asked for, terms they asked to avoid).
- **Flag stale shared versions.** If an older dossier for the same guest is shared publicly with a wrong date or superseded framing, tell Akshay so he can unshare it.

## Inputs

Any of: guest name, LinkedIn URL, company or protocol name, a PR backgrounder, pre-call notes (often a Gemini-exported call between Akshay and the guest), a recording date.

Extract every name, URL, role, number and date before doing anything else. Pre-call notes are high value: they carry the guest's own current framing, which is usually broader than the web picture, plus confirmed logistics, candid admissions, and any constraints the guest's team set (for example, Steakhouse asked that banking terminology be kept off its products). Every question must respect those constraints.

## Outputs

Two published pages, one markdown file, and optionally a Google Doc. The documents have different readers and different jobs, so they ship differently.

1. **The host dossier, published as a page** with the Artifact tool. Dark theme, aarna teal on charcoal, jump links, and a prominent Word download button. The primary artefact.
2. `/mnt/user-data/outputs/un-dossier-<lastname>.md`: the same content in plain text. **This ships every time, without being asked.** Sri marks it up, cuts themes, reorders them and adds his own questions before recording, and a published page gives him nowhere to do that.
3. **The guest prep note, published as a page.** The link is the whole delivery, because it gets pasted into an email or a DM to the guest. No markdown copy.
4. **Optional: a Google Doc copy of the dossier** so that people who open a shared link without signing in to claude.ai can still download it as Word. Only with Akshay's go-ahead. See "Word download" below.

Send the markdown file with SendUserFile after writing it. Hand over the dossier link, then its markdown, then the guest note link.

**The markdown is a real conversion, not a dump.** Page furniture (nav, jump links, styling hooks, the download button) becomes headings, bold labels and lists. The reading order stays identical, and nothing that exists on the page goes missing from the file.

Both pages are private on publish. Say so once: Sri and the guest cannot open their links until Akshay shares each page from its Share menu.

**Every later edit updates all copies together.** When Akshay asks for a change, edit the page, the markdown and (where relevant) the guest note in the same pass, republish to the same URLs, resend the markdown, and say the Google Doc copy needs a refresh if one exists.

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
8. If recording is this week: a fresh sector-news search for something live the guest can react to, and the company's own blog or newsletter archive for the last 30 days

`web_fetch` two or three substantive pieces: the most recent long interview, the most recent thesis post, any live incident. Skip the company's own marketing pages, except to read a fresh announcement in full.

Then tell Akshay in a few bullets what the web pass found (who the guest is, what is live, dated incidents, any number that needs reconciling) before the Grok prompt, so he can see what Grok is meant to add.

## 1b. Emit the Grok prompt, then STOP

Grok has live X access and is materially better than Claude at recent-post mining, which is the exact gap this skill exists to close. Output this in a copyable code block, filled in. Pre-load it with what 1a found: name the products, incidents, conflicting figures and interviews you already have, so Grok confirms or corrects them instead of rediscovering them.

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
   measurement basis is undefined in public. Also: how the company makes
   money, as a mechanism and at what rate.

5. SECTOR NUMBERS. The current figures for the category this company sits in,
   as of this month: total market size, the comparable metric for the two or
   three nearest competitors, the going rate or fee or yield in this segment,
   and the direction of travel over the last year. I use these to frame
   questions, so they must be current and sourced. A stale sector number is
   worse than none.

6. DISAGREEMENTS. Where has this person publicly taken a position that others
   in the space dispute? Who disputes it and what is their argument? Include
   replies and quote-tweets against them, and the person's own reply, VERBATIM
   with a link.

7. THE UNANSWERED QUESTION. Business and product questions this person has
   been asked directly and has not answered cleanly, on X or on a podcast.
   Quote the question, name who asked it, link it, and say what the nearest
   thing to an answer was. Skip personal, political and lifestyle material,
   which I will not use.

8. RECENT LONG-FORM AND CAREER. Podcasts, panels, AMAs, Spaces in the last 6
   months. For each: date, where, and the two or three things they said there
   that they have not said elsewhere. Then their full career before this
   company, including roles outside finance or crypto, with years and a
   source for each (registry entries, press releases, their own account in
   interviews). Say which roles you could not verify.

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

**Grok output often arrives in parts.** If sections are missing (commonly 6 to 8), build from what arrived, fill the gaps from your own long-form reading, say which sections were missing, and fold the rest in when Akshay pastes it. When he supplies a verbatim quote and link later, replace any paraphrase with it.

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
- **Verify Grok's career claims independently.** Grok's career lists mix confirmed and unconfirmed roles. Confirm each role you use against a primary source (a press release, a registry entry, the guest's own words on a podcast). A surprising role you can confirm is gold (Adrian Cachinero ran a Swiss chocolate company, confirmed by a 2022 press release naming him CEO). A role you cannot confirm stays out
- **Characterise third-party allegations as theirs.** When a theme rests on a critic's reading of an incident (OAK Research on Steakhouse and Resolv), attribute it in the text and in the question, and state what the company's own position was

## Dossier structure

**Header.** Guest, company, role, recording date and time in JST, SGT and the guest's local zone, X handles for the guest and the company.

**Word download button.** Prominent, at the top right of the sticky header. Spec below.

**Background block, at the TOP.** Two prose paragraphs, moved here at Sri's explicit request in June 2026. Never bury it at the end.
- *Guest in brief*, 70 to 90 words: career arc, prior ventures, and the bet they made
- *The firm*, 70 to 90 words as its own paragraph: what it is, where it runs from, scale, backers, and what has moved recently

**Write this block plainer than the rest of the dossier.** It is orientation, and Sri reads it in about fifteen seconds. Short declarative sentences. Plain verbs.

- **No registration numbers, CNPJs, filing IDs or legal entity names** unless one of them is load-bearing for a theme. Comoros incorporation matters. "KAST Tech, Reg No. 16223" does not
- **No sourcing hedges inside the sentence.** "Live in 170 countries" beats "live across 170 countries by its current product pages". Put the uncertainty in the theme where it does work, or leave it out
- **Attribute company claims once, plainly.** "KAST says it has over a million users" does the job that "Company figures: over one million users, stated at the Series A and unchanged in comms since" does badly
- **No stacked appositives.** If a sentence has three commas doing the work of three clauses, split it

**The journey.** Directly after the background block, with its own jump link. One chronological timeline that combines the guest and the organisation. Spec below.

**The angle.** One paragraph. The single sharpest reason this conversation matters now, ideally a tension, ending on the most current hook.

**Pre-call callout**, only if a pre-call actually happened. A short highlighted block capturing the guest's own framing, which themes absorbed it, any constraints their team set, and confirmed logistics. This is the guest's own words, not comms-team intel.

**How to use this.** One line saying the first question is the TradFi-accessible opener and stays first even if a breaking theme is pulled forward. One line explaining the Wider lens questions and the Your point boxes. Then the numbered theme index as jump links, and the one-line arc note.

**Themes, 5 to 7.** Spec below.

**The close.** One horizon question. Spec below.

**Comprehension checks.** Five to eight, as a compact block.

**Note and links.** One caution if there is a real one. Compact links, no narration. The bio does not repeat here.

**Intro VO.** Final section.

## The journey timeline

Sri asked for a chronological view of the guest and the organisation together, so he sees how one shaped the other before reading the themes.

- **15 to 20 milestones**, oldest first, ending on the recording date
- **Each entry carries:** a date (as precise as the evidence allows), a tag (Guest, Firm, Both, or Sector), one line of what happened, and a source link wherever one exists
- **Cover both lines:** the guest's career before the company (including non-crypto and non-finance roles you have confirmed), where the guest's path meets the company's, the company's founding and pivots, distribution deals, product launches, incidents, the regulatory moments that matter to it, and anything from the last 30 days
- **Be honest about imprecise dates.** "Early career" or "2020 to 2021" beats a guessed year. Where a guest held two roles at once, write the overlap rather than forcing a false sequence
- **Sector entries** only where an outside event changed the company's situation (a regulator's statement, a sector-wide exploit). Two or three at most
- **Styling:** a vertical line with dots; guest entries in coral, firm entries in teal, sector entries in grey, Both as a hollow dot. Grid of date, tag, text on desktop, collapsing to one column on a phone
- **Markdown:** a bullet list, `**Date · Tag.** Text (link)`

## The opening question: accessible first

Every episode opens on a question a TradFi listener, or someone with no DeFi background, can follow. This is now the rule, set by Akshay in October 2026. The guest explains what they actually do in terms that listener already uses, before any DeFi vocabulary.

- **Theme 1 carries it,** and its title names the job in plain words ("What a risk curator actually does")
- **Shape:** "[Name], welcome to Unhashed." Then picture a specific listener from traditional finance, name the jobs they already know (fund manager, credit committee, ratings agency, transfer agent, exchange, custodian, whichever are nearest), put them in front of the product the way they would actually meet it (an app button, a fund, a payment), give one checked number for scale, and ask what the guest's job is in that listener's language
- **The crystallisation for Theme 1 is in TradFi terms** ("you're the credit committee and the investment mandate rolled into one, written in code")
- **One press line asks for the nearest TradFi job title**
- **The first comprehension check restates the job as a TradFi analogy**
- **Respect pre-call constraints.** If the guest's team asked to avoid certain terms (Steakhouse: no banking terms for its products), choose analogies that don't use them
- Only then does the dossier move to the definitional or vocabulary question ("what is a vault") and on into the present

## Theme spec

Each theme is self-contained and carries these parts, in this order.

**1. A specific title.** The guest's own phrase where there is a good one. "Reserve's honest secret" passes. "Tokenomics" fails. The test: could this title belong to any other guest in the category? If yes, rewrite it.

**2. Context, with the thing that powers it.** The post, stat, event or decision, with its date and an inline link. Mandatory. A theme with no grounding is the "no real context" failure Sri named. Verbatim quotes go in quote blocks with date and link.

**3. One crystallisation.** See below. This is the most under-used device in past dossiers and the highest-yield one.

**4. Two or three questions, written in his grammar.** Single asks, not stacks.

**5. A press ladder.** One or two short reframes to deploy if the first answer goes vague. Sri presses twice at most and his second press is always short and reframed rather than repeated.

**6. A wider-lens question.** After the press ladder, separated visually. One question that takes the conversation off the guest's company and onto the industry, the market, history, or the listener's world. It must still be answerable by this guest from experience. Tests: would it work if the guest's company did not exist? Would a smart outsider want the answer even if they never use the product? If the answer to either is no, rewrite it. Examples from the Steakhouse dossier: who in the ETF and mutual fund world loses first when vaults do the same job in code; whether banks' next fight is with vaults rather than stablecoins; whether DeFi becomes a back end for the big apps and whether that is a win for the ethos; the one failure the industry keeps repeating across four exploits; whether onchain collateral pushes stock markets toward trading around the clock; which jurisdiction is getting it most right.

**7. Optional: a Your point box.** See below. Four to six themes per dossier carry one.

Order the themes in a logical arc and number them. The default arc runs accessible opener, then thesis, then live proof, then why it holds, then why it might not, then frontier, then backstory. **Treat it as a default you may break,** except that the accessible opener always comes first. When the guest does not fit the arc, break it and say why in one line under the theme index. An arbitrary pile drew the "the flow seems a bit random" critique; a forced arc produces a dumb dossier.

**At least two themes must come from the case FOR the company**, built off section 2 of the Grok pass. The live-proof and why-it-holds slots are not filler. A dossier where every theme is a challenge has turned Sri into a prosecutor.

**And no more than half the questions may be about the company's own products and numbers.** The wider-lens questions, Sri's points, the thesis theme and the close carry the rest. A dossier where every question promotes the guest's company is the failure Akshay named in October 2026.

Flag the **spine** (the sharpest tension) and any **breaking** theme. Place breaking where it fits the arc, not forced to the front. The tag lets Sri bring it forward, after the accessible opener, if the guest arrives talking about it.

Each idea appears in exactly one theme.

## Your point boxes: Sri's clip moments

Sri should make his own points on tape, so the episode yields clips of him, not only of the guest. Give him four to six short takes, each 20 to 30 seconds spoken (roughly 50 to 90 words), each in the theme where it lands naturally.

- **Built only from positions Sri has already taken.** Search the project transcripts (`project_search`) for his stated views before writing any. His documented positions include: vaults becoming the core of the whole asset management industry (and aarnâ building around vaults before ERC-4626 existed); the roughly $300bn stablecoin pool as a new capital market; tokenization only making sense when it fixes a specific problem ("just tokenizing for the sake of tokenizing really doesn't make sense"); regulators moving from lumping crypto, stablecoins and tokenization together to treating them separately; regulation that should be borderless; a large tokenized shift that users won't even notice; India's inward remittance market and access to Indian credit, where the guest gives a real hook. Never put a view in his mouth that he has not expressed. A forecast that is his own (for example a trillions figure from an earlier episode) stays framed as his view
- **Write each as standalone speech.** First person, contractions, one idea, opening on the claim and ending on a line that could close a clip. It must make sense cut out of the episode, with no reference to "what you just said"
- **Prioritise tokenization, vaults, stablecoins and regulation,** the topics the clips channel and aarnâ's positioning need most
- **Where an aarnâ hook is real, use it** (Indian credit reaching global investors, agentic treasury) as a shared engineering problem, never a pitch
- **Label it "Your point · clip"** in a coral-bordered box on the page and "**Your point (clip).**" in the markdown. A line under How to use this says to deliver it before or after the guest's answer, wherever it lands
- **These are exempt from Gate two's subtraction pass** in the same way as the questions: they are written to be spoken

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

**Write one per theme.** Make it a real, committed, falsifiable model of the business, not a hedge. A crystallisation the guest can only agree with is wasted. State the model positively: "the token is a claim on a share sitting in a structure somewhere", never "the token isn't the share, it's a claim".

Launch phrases: "if I were to rephrase what you said" / "if I were to kind of deconstruct that" / "Got it, so it's basically" / "correct me if I'm wrong" / "Is that how one should understand it?"

## Comprehension checks

Roughly one turn in three is him compressing a long answer into one sentence and handing it back. It is what he does instead of interrupting, and he improvises all of it live. Pre-drafting these is the single most useful thing the prep can hand him.

> "And this is basically multi sig."
> "So it's like the on-chain Swift basically."
> "So just to be clear for everybody, it's not a primary issuance. There's already a secondary. It's a digital reflection or a tokenization of an existing."
> "And the cross-chain bridges, are they like the new mixers?"
> "So we are introducing the whole element of trust here into what's supposed to be all trustless architecture. And the trust is residing where?"

**Ship a dedicated block of five to eight**, one line each, one per concept in this episode that a wider audience will not follow. The first one restates the guest's job as a TradFi analogy. He told a guest why he does it: "the audience is not only DeFi, it's wider."

## Pushback register

He challenges the architecture and the market logic. He does not challenge the person.

**Concede first, then counter.** "Yeah, no, very true. But at the same time, I also feel..."

**Attribute the objection.** "purists in the space" / "naysayers of the space have always been saying" / "I get asked this every time by any TradFi participant" / "crypto bros"

**Credit the guest's own values before landing it.**

> "Is there a risk of platforms like yours becoming gatekeepers for DeFi when DeFi was supposed to be completely accessible, permissionlessly for everybody? And as somebody who also passionately believes in the ethos of crypto, how do you balance this?"

**Never run a gotcha about the guest's own incident.** He said why, off-record: "you're running a centralized exchange, so I didn't want to go too much deeper into that."

But he is not avoiding controversy. He spent 20 minutes with Goldfeder on the Kelp DAO freeze and raised the same incident again with Sam at Spark. **The difference is he asks it as a systems and decision question, not a character accusation.** This is the model:

> "how difficult was the decision more recently... walk us through that whole decision making system and where you stand on this whole requirement for recourse. And secondly, as somebody who comes with the old foundation of decentralized systems, how do you balance this in the very core architecture?"

So: take the ugly thing, and ask what it reveals about how the system should be designed. "Is my money still mine" is an accusation. "What does custody actually mean in a business that takes stablecoin balances, and where did you land on it" is the same territory, and he will actually ask it. The Steakhouse version: the guest was named a protocol's risk manager days before that protocol was exploited, so the question became how a firm keeps assessing a protocol separate from curating against it, framed as the ratings-agency problem arriving in DeFi.

**Use the guest's own admissions as the strongest material.** When a guest has conceded a weakness on the record (Adrian: "I'm not satisfied by this because it's not cryptographically enforced"), build the question on it. It is fair, it is in his own words, and it produces better tape than any outside critique.

**Supply ammunition for the second press.** He presses withheld facts well and folds on contested opinions immediately, announcing the retreat out loud ("I'll let that pass"). The only thing that reliably gets him a second push on an opinion is an on-record contradiction from the guest's own past words. Section 7 of the Grok pass is built to find these. Put one in the press ladder.

## What to route toward

His standing obsessions, in order of how reliably he gets there regardless of subject. **Check the finished dossier against this list.** If a guest touches one of these and no theme covers it, that is a miss. These are also the natural home for the wider-lens questions and the Your point boxes.

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

Never Theme 1. The on-ramp is the accessible opener, not a biography question.

His origin questions are corporate and numeric: "how did you land up at GSR", "what was the AUM at that point in time", "when did you get orange-pilled". Across 44 transcripts there is one personal-life question. **Do not write:** the hardest month, the low point, what kept you up at night, childhood, family, mentors.

Give the backstory theme a callback line to the opening question. He does this out loud: "that's why that was my opening question when we started out."

**Where the guest's path genuinely parallels Sri's, use it.** Sri built and ran Milk Mantra, a dairy business, for more than a decade before aarnâ. A guest who ran a manufacturing or consumer business (Adrian ran a Swiss chocolate company) gives Sri a peer-to-peer line: two operators comparing what a factory floor teaches about margins and risk. Only where the parallel is real.

## The close

One question. Always a horizon with a number attached.

> "Jim, what would a successful tokenized capital market look like to you in 2030?"
> "what would be your three-year projection around what sky issuance will be at? Where do you see your TVL? Just paint that picture."
> "Let's take a one and a half year from now and a three year horizon. What's your take on the TVL?"

Put it in the dossier as its own short section after the last theme, not buried inside one. Where possible, frame the horizon around the sector (stablecoins, curated vaults, tokenized assets) as well as the guest's company.

## Gate two: the polish pass, before anything ships

Run this over the finished dossier body and the guest note. It is the `post-polish` craft applied to prose nobody will edit again, and it is a subtraction pass: nothing here adds a word.

**The disposition:** a grammatically correct sentence carrying true information can still be cut. Polish is weight-checking, not error-finding. Connective tissue is where AI writing shows, so when in doubt about a transition, cut it.

**Flag and rewrite every instance of these.**

- **Negative parallelism.** "The question is not whether X. It is whether Y." / "Business was not a roadmap item, it was a leak." / "That's for the listener, not a challenge." / "the token isn't the share, it's a claim". Banned outright, and it is the tell that survives longest because it reads as insight. It hides in crystallisations and in the guest note as well as in prose. Make the positive claim and stop. Run a text search for "isn't", "is not", "not a", "rather than" and "not just" before shipping and check each hit
- **Self-import.** "This is the thing I find genuinely interesting rather than the thing Twitter found interesting" / "what most people miss" / "a rare thing about". The observation should carry itself
- **Telegraphed contrast.** "But here's the thing", "Here's where it gets interesting", "The plot twist is". A good contrast happens without announcement
- **Connective tissue.** "What I find more interesting is", "This is where", "It is worth pausing on", "Let's turn to"
- **Borrowed clichés.** "Said the quiet part out loud", "the elephant in the room", "moving the goalposts". They read as borrowed because they are
- **Restating what was just shown.** "That is the tension this theme is built on", after the tension has been demonstrated
- **Three fragments doing one job.** Stacked short fragments all expressing the same idea. Keep the best one
- **Hedges before a real claim.** "While X is true, Y matters more" should just be the Y claim
- **Precious closing clauses.** "where the callback lands hardest", "which is the whole point". Stop at the fact
- **Throat-clearing first words.** A paragraph opening on "Now," "So," "Well," "Frankly"
- **Em-dashes.** Zero, anywhere. Search for them

**Then the subtraction sweep.** Sentence by sentence: is this claim made elsewhere, is it setting up a sentence that stands alone without it, is it connective tissue between two sentences that could sit next to each other. Cuts compound, so the second sweep finds what the first one's new rhythm exposed.

**What this pass does not touch.** Sri's own verbatim quotes, the guest's verbatim quotes, the questions written in his grammar, and the Your point boxes. His questions are deliberately long and full of "sort of", and tightening them into clean prose is the exact failure this skill exists to prevent. Polish the dossier's own writing: context paragraphs, the angle, the background block, the journey lines, crystallisations, notes, and the guest note. (Crystallisations get the negative-parallelism check even though they are in his voice.)

## Voice rules for the dossier body

- Internal-tool voice. Direct and blunt. This is Sri's read, not PR
- **No em-dashes.** Commas, parentheses, or two short sentences
- **Banned:** exciting opportunity, great potential, amazing journey, powerhouse, thought leader, game-changing, passionate, world-class, trailblazing, pioneering, revolutionary, disruptive, deep dive, unpack, delve, leverage, unlock, robust, seamless
- Concrete numbers everywhere. If a number is unknown, write "Unknown". Never guess
- No coaching notes under questions. No "why this lands". Sri cut them as noise
- Posts live inside the theme they power. No standalone recent-posts list
- Do not recycle the company's marketing language
- Sentence case for every heading

---

# The host dossier page

Published with the Artifact tool. **Load the `artifact-design` skill before writing it**, and write page content only: no doctype, html, head or body tags, since the tool wraps the file in its own skeleton. Put the `<title>` and `<style>` at the top.

Title it as a name, two to four words, identifiable in a gallery of other artifacts. "Raagulan Pathy dossier" works. "Host dossier" does not.

This page commits to a single dark theme by design, which the artifact contract allows as long as every colour is painted explicitly and nothing is left to inherit from the host ground. Define the full palette on bare `:root`, set `color-scheme: dark`, and give `body` an explicit background. A sticky header uses `top: env(safe-area-inset-top, 0px)`, never `0`, with a fixed `body::before` band painting the inset.

Inline all CSS. Google Fonts is the only external stylesheet host; JSZip from cdnjs is the only external script.

Dark theme, aarna palette.

```
--bg:#0E1010  --surface:#171A1A  --raised:#1F2423  --rule:#2C3030
--ink:#E8EAEA  --ink-soft:#B5BCBC  --ink-mute:#7F8888
--teal:#1FBFB0  --teal-deep:#0FA095  --teal-glow:#6FE5D8
--coral:#C97A4B  --on-teal:#06201D
```

Fonts: Manrope for body and UI, Newsreader for the angle, theme titles and pull quotes, JetBrains Mono for numbers, dates and tags. Load from Google Fonts with a system fallback stack.

Layout:
- Sticky header with the guest name, the recording time, the Word download button at the right, and a jump-link row: Background, Journey, Angle, theme numbers, Close, Checks, VO
- Background block and the journey timeline at the top, then the angle set in Newsreader at a larger size
- Each theme as a card on `--surface` with a teal left border. Breaking themes take `--coral` instead. Spine gets a teal filled tag
- Context paragraph in `--ink-soft`, quotes in a bordered block with the date and link in mono
- Crystallisation in its own dashed-teal box, labelled, so Sri can find it fast
- Questions numbered, press ladder indented under them in `--ink-mute`
- Wider lens below the press ladder, separated by a dashed rule, labelled in coral mono
- Your point box: coral left border on `--raised`, set in Newsreader, labelled "Your point · clip"
- Comprehension-check block styled as a compact list, since he scans it mid-recording
- Max width 860px, generous line height, and it must read on a phone, because that is where Sri reads it. Side gutter with the `max(16px, env(safe-area-inset-*))` padding pair
- Theme cards and section headings get `scroll-margin-top` clear of the sticky header (about 130px with the button row), or the jump links land under it

## Word download

Akshay asked for a prominent button at the top that downloads the dossier as a Word file. Build it in, every time.

**In-page build, for signed-in viewers.** Declare `capabilities: {downloads: true}` on the first publish (load `artifact-capabilities` first). Load JSZip 3.10.1 from cdnjs. A page script walks the dossier DOM and writes a real .docx (document.xml, styles.xml, relationships for every external link), then calls `(await claude.use("downloads")).save({filename, data: blob})`. Because it reads the live page, the Word file always matches the latest publish.

- Map page parts to named Word styles: Title, Heading 1 for section headings, Heading 2 with a teal top rule for theme titles, Angle, Quote and Cite with a teal left border, a shaded dashed box for Crystallisation, a coral-bordered box for Your point, Wider lens with a dashed top rule, numbered List Item for questions, indented Press lines with a bold "Press:" label, the timeline as list items with a bold date and a coloured tag. Skip the header, nav, scripts and SVG
- Only `http(s)` hrefs become hyperlinks; in-page `#anchors` become plain text
- Keep spaces around links: trim only the leading whitespace of a paragraph's first run
- Handle rejections: `declined` (cancelled), `rate_limited` (a prompt is open), anything else as unavailable
- **Test before publishing:** run the builder headlessly (jsdom with `runScripts: 'outside-only'`, JSZip's `nodebuffer`), open the result with python-docx, and render a page through LibreOffice to check it looks right

**Fallback, for anyone without the save prompt** (typically people opening a shared link without signing in to claude.ai). Artifacts cannot host a .docx file, and page-made download links are blocked, so the file has to live elsewhere.

- **Ask Akshay first** before writing to his Google Drive. With his go-ahead, convert the dossier into clean semantic HTML (headings, paragraphs, lists, blockquotes, inline styles only, attribute-stripping applied only inside tags so it never eats words like "release" or "identical") and upload it with the Drive `create_file` tool as `text/html`, which converts it to a Google Doc. Read it back once to confirm the conversion
- Point a hidden fallback link in the header at `https://docs.google.com/document/d/<id>/export?format=docx`, opening in a new tab. When `claude.use("downloads")` resolves `null`, hide the button and show the link
- **The connector cannot set "Anyone with the link".** Tell Akshay the one step: open the Doc, Share, General access, Anyone with the link, Viewer
- The Doc does not update itself. Say so, and refresh it whenever the dossier changes
- If Akshay declines Drive, send him the .docx with SendUserFile and leave the button as signed-in only

## The markdown file

Write it every time, alongside the page. It carries identical content in the same order, and it is the copy Sri works on: he cuts themes, reorders them, strikes questions and writes his own in. Markdown is the only format that lets him do that.

So it has to survive editing. Plain headings and bold labels, no HTML left in, no styling hooks, nothing that breaks when he deletes the paragraph above it. Jump links become a plain numbered index, the journey becomes a bullet list, the crystallisation box becomes a bold **Crystallisation.** label, the press ladder becomes an indented sub-list under its question, the wider-lens question a bold **Wider lens.** paragraph, and Sri's points a bold **Your point (clip).** paragraph. The download button has no markdown equivalent and is left out.

---

# The guest prep note

A published page, and the link is the whole delivery. It goes out once the guest has shown interest, before or after the date is locked, so it carries two jobs at once: tell them what to expect, and quietly confirm they want to do it.

Akshay's voice, founder to founder. Warm, specific, logistics-clear. Written to the guest, never about them.

This is **not** the sell document. The `guest-note` skill does that job, with reach figures and a case for coming on. This one assumes interest already exists, so it makes no audience claims and never argues for the show.

## How it ships

Build a self-contained HTML page and publish it with the Artifact tool. Akshay gets a link he can paste into an email or a DM, and the guest can reopen it or forward it to whoever handles their calendar. **Load the `artifact-design` skill before writing the page.** If a guest note for this guest already exists, republish to its URL.

No markdown copy for this one. Nobody edits it, and a file sitting in a folder just becomes a stale second version of a page that can be updated in place. **Whenever the dossier's themes or opener change, update the outline here in the same pass.**

Light theme, the aarna palette the host dossier inverts:

```
--bg:#FAFAF6  --paper:#FFFFFF  --rule:#E4E2DA
--ink:#0E1010  --ink-soft:#2C3030  --ink-mute:#6B7474
--teal:#0FA095  --teal-deep:#0E7F76
```

Unlike the host dossier, this page renders in the guest's own theme, so give it the full three-state treatment: light tokens on bare `:root`, a dark set under `@media (prefers-color-scheme: dark)` guarded as `:root:not([data-theme="light"])`, and the same tokens again under `:root[data-theme="dark"]`.

Newsreader for the page title and section headings, Manrope for body. Quiet and readable, closer to a letter than a deck.

Title it for the guest, not for the system. "[First name] on un# with Sri Misra" works. "Guest prep note" does not.

No email furniture. No "Hey [Name]," opening and no "Best, Akshay" sign-off. It ends on one warm line and a byline.

## What goes on the page, in order

**1. A one-line frame.** What un# is, in the guest's terms, and that the audience runs from DeFi natives to people from traditional finance. Never "Sri Misra's show on aarna Protocol", which reads as though the show is about the company. Sri has been explicit that the podcast is delinked from aarna.

**2. Who Sri is, and why that matters.** Two or three sentences. Second-time founder, built and sold Milk Mantra after more than a decade, now building aarna Protocol and launching a regulated tokenization platform for Indian financial assets. This is what makes it a peer conversation rather than a press interview, and it is the thing most likely to make a founder say yes.

**3. Recent guests, chosen for this guest.** Three or four names from the **current** roster, not whoever appears first in the archive. Pick for relevance, and where a name connects directly to the guest's own history, lead with it. Never a guest older than about six months.

**4. The conversation outline.** The section below. This is the part guests actually read.

**5. Format and logistics.**
- The locked date and time, in bold, in the guest's local zone and Singapore time, once the date is confirmed
- Riverside, link sent ahead, quick A/V check at the top
- 90 minutes held, roughly 60 minutes published
- **Sri records the introduction separately**, so the conversation starts cold with a welcome. Say this. Guests are visibly thrown when it happens unannounced
- Headphones help, a light in front of them matters more than anything behind, and a window behind them works against both
- If anything is off the table, tell us before we record

**6. Where it goes afterwards.** YouTube, Spotify and the other podcast platforms, the newsletter, and clips on LinkedIn. Name the channels. No subscriber or view numbers.

**7. The close.** One line looking forward to it. A byline, not a signature block.

## The conversation outline

Broad strokes only (Akshay, 5 Nov): 3 to 5 broad themes, one short line each, no running order, no sequence notes, no questions. Draw them from the dossier's themes, then strip out everything rehearsable.

**Rules:**

- **No question marks anywhere in this section.** If a line could be answered, rewrite it as territory. "How Reserve's economics actually work" is territory. "Whether the yield is sustainable" is a question in disguise and will be prepped against
- Where the dossier's spine rests on something contested, **name the territory neutrally and do not hide it**. "What a curator's role should be when a protocol engages it as a risk manager" is fair warning without being an ambush, and it matches how Sri will ask. A guest who is surprised on tape makes worse tape
- Name the industry-level territory too (where the sector is heading, regulation across jurisdictions), so the guest knows it isn't only about their company
- If the guest or their team asked for a topic, it appears in the outline so they can see it is covered
- Never mention edit rights, review or approval, in any form (Akshay, 5 Nov).

## Voice rules for the guest note

- Contractions throughout. This is a person writing to a person
- No em-dashes
- Say the agile thing **once**
- No hype about the show and no adjectives doing work that facts should do
- Specifics over reassurance. "90 minutes held, roughly 60 published" beats "it won't take long"
- Gate two applies here too, and harder. This page is read by someone outside the company

---

# The intro VO

Final section of the dossier, page and markdown both. Titled "Intro VO (record after the conversation)".

Pre-interview mode: the recording has not happened, so the tease is topic territory, not quotes.

**Five variations at 55 to 75 words**, each labelled with its hook angle, plus a one-line recommended pick with the reason. Where the guest's backstory has a surprising turn you have confirmed (a chocolate CEO running a DeFi risk desk), one variation can lead on it.

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
- **Don't start from scratch when earlier work exists.** Search past conversations and artifacts for the guest first, and republish to existing URLs
- **Don't open on DeFi vocabulary.** The first question is the TradFi-accessible one, every episode
- **Don't write a dossier that only promotes the guest's company.** Every theme carries a wider-lens question, and no more than half the questions are about the company's products and numbers
- **Don't forget Sri's own voice.** Four to six Your point boxes, built only from positions he has already taken
- **Don't skip the journey timeline.** Guest and firm on one chronological line, after the background block
- **Don't ship the dossier without the Word download button**, and don't write to Akshay's Drive without asking
- **Don't write clean journalist questions.** Sharp, short, single-clause and adversarial is the wrong host. Preamble plus his own number plus the ask
- **Don't open Theme 1 on backstory.** Backstory goes at 70 to 85%
- **Don't write an emotional origin question.** No hardest month, no low point, no childhood
- **Don't accuse the guest.** Take the controversy and ask the systems question underneath it
- **Don't ship a dossier with no comprehension checks.** One turn in three is this move
- **Don't ship a theme with no crystallisation.** His highest-yield device
- **Don't format a paraphrase as a quote.** Verbatim only inside quote marks, with date and link
- **Don't use an unverified career role.** Grok's career lists need independent confirmation
- **Don't confuse incidents across time.** Date every incident, and when there are several, list them with dates and flag the most recent
- **Don't file by source type.** No standalone Signals or recent-posts section. Every post lives in the theme it powers
- **Don't repeat an idea across themes.** Once, where it lands hardest
- **Don't write a theme that would work for any guest in the category.** "Tokenomics" is a category, "Why ARB holders see $0 of $26M ARR" is a theme
- **Don't generate a toast prompt.** That ritual ended with the Alpha Unhashed era
- **Don't ask about valuation, cap table, burn, runway, raise size or headcount.** He asks how a business makes money as a mechanism, never the number
- **Don't ask about hiring, team or culture.** He never does
- **Don't add an India angle by default.** Only with a real hook
- **Don't break a pre-call constraint.** If the guest's team asked to avoid certain terms or topics, every question, crystallisation and the guest note honour it
- **Don't build a PR-intel section.** Sri cut it. A pre-call callout from the guest's own words is different and is allowed
- **Don't surface a confidence-flag legend or a verify-list.** Keep the no-fabrication discipline, note real uncertainty inline in a phrase, and leave the scaffolding out
- **Don't stack questions.** Single asks, follow-ups in the press ladder
- **Don't ship either page as a loose file.** Both get published and handed over as links
- **Don't ship the dossier without its markdown file**, and keep the markdown, page and guest note in step on every edit
- **Don't put a question in the guest outline.** Territory only, no question marks
- **Don't use stale guest names as social proof.** Current roster, picked for relevance
- **Don't put reach numbers in the guest note.** Numbers belong to `guest-note`
- **Don't build the dossier only from the adversarial half of the research.** Two themes minimum come from section 2 of the Grok pass
- **Don't ship without the polish pass.** Negative parallelism in particular survives every other review, including inside crystallisations and the guest note
- **Don't load the background block with filing detail.** Sri reads that block in fifteen seconds
- **Don't polish the questions or Sri's points.** They are written to be spoken

## The bar

Sri's own fear about his show, stated 6 March 2026, is the standard the dossier has to clear:

> "is it boring content? I might be finding it very exciting to talk to someone else who is in the same boat as me and going into stuff which we both enjoy talking about. So we are both happy but the audience is not. Those are all lost opportunities then."

A dossier that only helps two insiders enjoy themselves has failed. So has one that only advertises the guest's company. Every theme should be something a smart outsider, including one who has never touched DeFi, would want to hear the answer to.