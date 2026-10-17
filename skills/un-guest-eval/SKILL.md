---
name: "un-guest-eval"
description: "Evaluate inbound guest pitches for un# (Unhashed), Sri Misra's crypto podcast. Pulls precall notes from Drive, scores Fit and Partnership independently, routes through three tracks, publishes a page, and returns a 40 to 50 word short pitch with a bio link for the pipeline sheet."
---

# un-guest-eval

Inbound triage for un#, hosted by Sri Misra. Akshay produces the show. PR agencies and founders pitch constantly and most of them are wrong for it.

## Why the show exists, and why that changes the scoring

Sri runs un# for two reasons, and a guest can serve either one.

**Credibility and thought leadership.** He wants to be a recognised voice in tokenization and onchain asset management. That is served by institutionally legible guests a finance audience already respects.

**Relationships that become commercial for aarnâ.** Investors, GTM and distribution partners, liquidity. An hour on tape is the warmest introduction available, and the past-guest list is already his relationship map: Henry Zhang at DigiFT, Jim Hiltner at Superstate, Jake Brukhman at CoinFund, Julian Sawyer at Zodia, Pritam Dutta at Zoth.

So this skill scores **two independent axes**. A guest who fails the credibility bar but owns a distribution channel aarnâ needs is still worth an hour. A guest who clears the bar and offers nothing commercially is still a good episode. Score them separately and let Akshay see both.

## Sri's bar (Fit axis)

A guest clears it only if they are *either* the founder of a notable crypto org, *or* a genuinely senior and influential player at a systemically important organization. Sandy Kaul (Head of Digital Asset and Industry Advisory at Franklin Templeton, already recorded) is the model for the second: not a founder, but she leads the function, reports near the top, and is the public face of that firm's digital-asset work.

A mid-level person at a great org does not clear it. A commentator with no operating role does not clear it.

## Current editorial priority (stated September 2026, review every quarter)

Sri has asked for **more regulated tokenization**: Superstate-shaped. Regulated issuers of tokenized funds and credit, transfer agents, licensed marketplaces, the institutions actually holding the assets. Bitwise, Canton, Circle and Franklin Templeton sit in the same band.

This is an editorial tilt, not a permanent rule. It lifts a qualifying guest by one band on Fit and breaks ties in their favour. **Say in the artifact that it was applied.** When this priority is more than about six months old, flag it for confirmation rather than applying it silently.

## Show context

- **Host:** Sri Misra, founder of aarnâ protocol. Previously founded Milk Mantra, an Indian consumer food business, exited around $27.5M.
- **Audience:** crypto natives and the crypto-curious. English-speaking, want to invest or build.
- **Style:** unstructured, deep, still accessible to beginners.
- **Distribution (as of mid-2026, re-verify before quoting):** roughly 65k YouTube, 15k newsletter, 15k X, 265k LinkedIn across pages. YouTube, Spotify, Apple.

The show is public-facing as **Unhashed**. Sri says "Unhashed" on tape and never "un#". Search both.

---

# What aarnâ actually needs

This section drives the Partnership axis. Everything here is as of **September 2026** and should be re-checked before it is quoted as current.

**aarnâ today.** Agentic Onchain Treasury. ERC-4626 vaults (âtvUSDC, âtvPTmax, âtv111, âtv802, âtv808) with an agent layer called âTARS, targeting 8 to 12% on USDC for project treasuries, family offices and foundations. Integrations already public: Pendle, Sonic, Monad, Aave, Compound, Morpho, Dolomite, Silo, Moonwell, Balancer, Uniswap, 1inch, Odos, Aerodrome. Circle USDC developer grant, Certik audit, Failsafe monitoring. DefiLlama TVL around $223k and falling.

Read that last number carefully. The integration surface is wide and the capital is thin. **aarnâ's gap is demand, not plumbing.** A guest who offers another chain or another yield source is offering what aarnâ already has too much of.

**The India credit token.** aarnâ's second product line, under the India Yield Platform: a regulated tokenized India private credit instrument out of GIFT City under IFSCA. ERC-3643, 8 to 9% net USD, $25,000 minimum. IFSCA FinTech Sandbox Stage 1 approved 17 April 2026, Stage 2 in review, targeted for Q4 2026. It has no distribution yet. This is the need with a deadline.

**On the name.** Internal notes have called it ICT, for India Credit Token. That acronym is not established in aarnâ's public material and Akshay does not use it in conversation, so **write "aarnâ's India credit token" in full and do not use the acronym in any artifact.** Akshay's own shorthand for it on calls is "India's first debt token".

**Treat the underlying credit managers as confidential.** Public aarnâ copy says only "two of India's top credit asset managers". If Akshay has named them privately, they do not go into an artifact, a dossier or a guest note.

## The four needs, in priority order

1. **India credit token distribution.** Channels that put a regulated tokenized credit product in front of individual investors at a $25k ticket, in USD, outside the US.
2. **Vault capital.** Real allocators into third-party onchain vaults.
3. **Collateral and composability.** Getting âtv or the India credit token admitted as collateral or onto an earn page.
4. **The regulated stack.** ERC-3643 issuance, transfer agency, custody for permissioned tokens, secondary venues, audit.

## Who actually buys, and who only looks like they do

This is the part that stops the Partnership axis becoming a vanity score.

**Real allocators into third-party vaults, by evidence:** foundations that want immutable rails (the Ethereum Foundation's Morpho deployments), DAOs that run a treasury RFP and award mandates (Arbitrum's ATM Council splitting across kpk, Avantgarde and Gauntlet; Scroll DAO; Gnosis GIP-148), and consumer fintechs that wrap a curator and distribute customer float (the Coinbase, Robinhood Earn and MetaMask pattern, all curated by Steakhouse).

**Not allocators:** family offices and funds posting about yield on X, crypto media, conference circuit regulars, and anyone whose "AUM" is a firm-level claim rather than a vault balance.

**For the India credit token, almost nobody sells third-party regulated credit at a $25k ticket outside the US.** The short list that genuinely does: DigiFT and ADDX in Singapore, InvestaX/IXS for APAC accredited, and IFSCA-registered distributors under the CMI Regulations 2025. Securitize is US-centric. Tokeny is rails, not a distributor. NRI and diaspora wealth is almost entirely offline and has no public tokenized book.

**The distribution deal shape that repeats:** a licensed distributor already owns the customer, a regulated custodian or transfer agent is named on the page, and a DeFi curator optionally turns the token into collateral. When the issuer is small, the distributor or the asset manager initiates. So the person worth booking is the one who **owns listings or distribution**, not the founder of another issuer.

---

# Workflow

## Step 1: the past-guest check, before anything else

Sri does not repeat guests. This check has failed before, so run it in this order.

1. **Search the project transcripts first.** `project_search` for the guest name and their company. The project holds the recordings and is the only source that catches a guest who has recorded but not yet aired. Note: the tool is `project_search`, and a recorded-not-aired guest returns nothing on the open web.
2. **Check the roster below.**
3. **Web search** `"Unhashed" "[Guest Name]"`, plus `site:youtube.com` and `site:spotify.com`.

Any clear match is an auto-decline. Go straight to the output with verdict **Decline**, reason "Already recorded for un#", and the episode or transcript reference. Do no further research.

**Recorded guests (from the project archive, September 2026).** Treat as a floor, not a ceiling.

Matthew Hougan (Bitwise), Marc Boiron (Polygon Labs), Yat Siu (Animoca), Jakob Palmstierna (GSR), Arthur Breitman (Tezos), Julian Sawyer (Zodia), Sebastien Borget (The Sandbox), Nitin Gaur (LinkLedger), Alexander Mitrovich (Unique Network), Amanda Wick, Henry Zhang (DigiFT), Simon Dingle, Edul Patel (Mudrex), Max Li (OORT), Sandy Kaul (Franklin Templeton), Nikhil Chandhok (Circle), Sid Powell (Maple), Jim Hiltner (Superstate), Steven Goldfeder (Offchain Labs), Sam MacPherson (Phoenix Labs), Vivek Raman (Etherealize), Eric Saraniecki (Canton Network), Anton Katz (Talos), Jake Brukhman (CoinFund), Ronit Ghose, Santiago Roel Santos (Inversion), Joseph Onorati (DeFi Development Corp), Pritam Dutta (Zoth), Punit (KoinX), Joe Zhou (Beosin), Arjun (Giottus), Akshit (LogX), Christian (Mind), Dharamveer (Zo World), Tal (Tres Finance), Vineet (Sigma Capital), Amy (Bitwave), Darren C (Ipor Labs), Shawn Douglass (Amberdata), Alvin Foo, Yifan He (BSN), Marcus (Balancer Labs), Olivier Dang (Kaio), Mriganka, Ajeet Khurana, Marcos and Alex (Rayls), Jeremy (PayStand), Raagulan Pathy (KAST).

**If the pipeline sheet is available, read its status column carefully.** In that sheet "Declined" means *the guest declined us*, not that Sri declined them. Robert Leshner at Superstate is a Sri-approved yes who said no. Reading that column backwards produces exactly the wrong list.

## Step 1b: look for a precall in Google Drive

**Do this before any web research. It has already been missed once and it cost a whole eval.**

Akshay runs a producer precall with most guests and it is recorded with Gemini notes, which land in Drive as a Doc containing quick notes, full notes and the verbatim transcript. Nothing in the pitch tells you it exists. Go and look.

Run `mcp__Google_Drive__search_files`:

- `title contains '<Surname>'`
- then `fullText contains '<Surname>' and title contains 'Notes by Gemini'`
- if the guest goes by a company name, `fullText contains '<Company>'`

The naming convention is `<Guest Name> and Akshay Datt - YYYY/MM/DD HH:MM JST - Notes by Gemini`, usually inside a folder of the same name. Read the whole Doc with `mcp__Google_Drive__read_file_content`, including the transcript below the notes, because the notes summarise and the transcript carries the quotes.

**A precall, when one exists, outranks every web source.** It is the guest's own current framing, in their own numbers, said out loud. Where it conflicts with press coverage or public filings, the precall wins and the artifact says which number came from where.

Pull these specifically:

- **Their own figures.** These are routinely more current than anything published. Press coverage lags by months.
- **What is not in public at all.** Team size, internal products, capabilities held back, where the business is actually concentrated. This is the highest-value material in the eval.
- **Their own suggested questions.** Guests volunteer these when asked and they are usually a genuinely good theme. Use them and say they came from the guest.
- **Consent boundaries.** Whether they will critique policy, competitors or regulators on the record. A yes unlocks the adversarial register; a no changes how the themes are written.
- **Corrections to your own assumptions.** Legislation that stalled, a product that shipped, a figure that moved.
- **Logistics.** Recording window, who handles scheduling, PR contact, anything flagged about their setup.
- **What Akshay already told them** about Sri and about aarnâ, so the dossier does not repeat it or contradict it.

If no precall exists, say so in one line in the artifact and proceed. If one exists and has not happened yet, note the date.

Also accept these as direct input when Akshay pastes them: a Gemini notes export, a PR backgrounder, a pitch email, a Perplexity-style workup. Extract every name, company, URL, figure and date before searching.

## Step 2: research

Four to eight targeted searches. Stop when both axes can be scored. If a precall or a backgrounder exists, use it as the source of truth and verify only what it does not cover.

**For the Fit axis:**

1. LinkedIn profile, if not supplied. **Capture the URL, the short pitch needs it.**
2. Company stage: TVL via DefiLlama, funding, token status, mainnet vs testnet, audits, regulatory permissions.
3. Crypto career arc. A 2018 builder still building reads differently from a 2025 arrival. Pre-crypto career matters.
4. Last 12 months of substance: regulatory milestones, institutional partnerships, marquee raises, named audits.
5. Published thesis, paper, testimony or non-consensus position.
6. Existing long-form appearances. Good for media-readiness, raises the bar on distinctiveness.
7. Seniority and scope. Do they own the function, or sit a layer down? Follower count and media tier as evidence of weight, not as vanity stats.

**For the Partnership axis, additionally:**

8. **What does this person or firm actually control?** Distribution, a listings decision, a treasury mandate, a collateral listing, a licence. Name the thing.
9. **Have they done a third-party deal?** A distributor who only sells its own products is not a distributor for aarnâ. Look for a named third-party issuer already on their platform.
10. **Do they compete with aarnâ?** Two overlaps to check: agent-driven or automated onchain treasury management, and tokenized emerging-market credit sold to global investors.
11. **Has Sri publicly positioned against them?** He has benchmarked âtvPTmax against Gauntlet and MEV Capital curator vaults, and argues publicly that curators sit outside the rail that holds the assets. Booking someone whose model he has attacked can be excellent tape. It should not be a surprise on the day.

**The same-org better-fit check.** Is there a more senior or more on-thesis person at the same organization? Pitched contacts are often a comms lead or a junior exec at a firm that also houses a principal. Name the alternative only if you can verify they hold the role.

## Step 3a: score Fit (1 to 10)

The bar sets the ceiling. Depth and topical relevance position the guest inside it.

**Calibration from 125 decided pitches in Akshay's own pipeline.** This beats any reasoning from first principles.

- **Approved:** founders, CEOs and presidents of marquee, category-defining orgs. Circle, Sky/MakerDAO, Aave, Maple, Centrifuge, Superstate, Polygon, Offchain Labs, Canton, Talos, TON, Figure, Securitize, Ondo. Principals at top-tier crypto VCs. C-suite and top-function heads at systemically important TradFi institutions. Curator and risk firms with real mandates (Steakhouse three separate times, Karpatkey, Gauntlet, Chaos Labs).
- **Declined despite real funding and TVL:** mid-tier protocols and important-sounding plumbing. Chains and scaling infra of every tier, including a Sui co-founder, a Bitcoin ZK rollup with Founders Fund backing, and an L3 with a GSR co-founder. Dev tooling and compute (a simulation layer doing $26.5M revenue, a ZK-AI compute network). White-label stablecoin issuance plumbing, including the layer sitting under MetaMask's own stablecoin. Generic crypto payments. Crypto-adjacent consumer fintech: crypto mortgages, web3 travel, crypto insurance. Non-principals at good orgs.

Median scale in approved and declined pitches is roughly the same. **Big numbers do not move this.**

**Apply the bar:**

- **Clears it cleanly** (marquee founder or CEO, or C-suite at a systemically important institution) → 7 to 10.
- **Borderline** (mid-tier or unproven founder, plumbing, senior-but-not-top, seniority unverified) → 5 to 6.
- **Fails it** (divisional employee whatever the logo, commentator with no operating role, no institutional weight) → caps at 4. Being interesting is not the bar.

**For non-founders the line is narrow.** Only C-suite or top-of-function at a marquee org. Divisional heads, "Head of [sub-team]", non-principal partners and research leads do not clear it on title, even at a great firm. Lido's Chief of Staking and CMT Digital's Head of Research were both declined. When the contact is a layer down, name the principal instead.

**A functional C-suite title at a marquee firm does clear it.** A general counsel, chief legal officer, chief risk officer or head of policy who owns the function and is the firm's public voice on it scores like any other C-suite guest. Check that the remit is real: a CLO who won a specific piece of regulatory relief, or wrote text into a statute, or testified, is a principal in their own domain.

**The firm is not the unit of decision.** Two people from the same firm can land on opposite sides. One CoinFund partner was approved and recorded; another was declined. Score the person's own standing and story.

**Current traction counts, not only pedigree.** A NEAR co-founder who also co-wrote the Transformer paper was declined on thin live numbers relative to market cap.

**Caps that apply even above the bar:**

- **Chains, L2s, L3s, rollups and scaling infra** → cap at 5. Consistently declined at every tier.
- **Dev tooling, infrastructure and compute networks** → cap at 5. Revenue and marquee backers have not saved these.
- **Generic crypto payments** → cap at 6. Stripe-for-crypto, payment rails, self-custody wallets, crypto payroll.
- **White-label or B2B stablecoin issuance plumbing** → cap at 6. Separate from consumer-facing issuers like Circle, which he books.
- **Crypto-adjacent consumer fintech** → cap at 5. Mortgages, travel, insurance, consumer trading apps.
- **Commentator or influencer with no operating role** → cap at 4.
- **Too junior: not enough years in the ecosystem** → cap at 4, whatever the title or the logo. Count the person's own career, not the org's: under about 5 years of senior, decision-making work in crypto, or a senior title reached within about 2 years of finishing an MBA or an analyst or associate track, fails Sri's bar. A grand title at a marquee foundation does not lift it. Example: Ramzy Ali, Head of DeFi & Trading at Solana Foundation (Oct 2026): MBA finished 2025, before that an associate at Draper Associates and an analyst then associate at FalconX, consulting at EY. Akshay: "he just finished his MBA, he is too junior for Sri to interview, not spent enough years in the ecosystem, not really a big deal." Read the career dates on LinkedIn before scoring seniority, and put the years-in-crypto count in the eval.
- **Arrived in the space in the last 12 to 18 months** → cap at 5, unless the move carries institutional weight (running a major asset manager's digital-asset desk, building stablecoin infra inside a regulated bank).
- **Pre-product** → cap at 4. Claims with no live product, no users, no commits.
- **NFT-only, or a story the show has heard** → cap at 5. Another AMM, another perp DEX.
- **Public output that reads as token-price marketing** → cap at 3.

**No cap for:** pre-revenue founders in genuinely novel cryptography or infrastructure; a TradFi mover whose move is institutional-grade; CeFi operators running regulated exchanges, custody or prime brokerage.

**Auto-decline whatever the score:** already recorded; active fraud, enforcement or indictment; pure shitcoin or memecoin promotion.

## Step 3b: score Partnership (1 to 10)

Independent of Fit. The question is narrow: **could this person move a commercial needle for aarnâ inside a year?**

- **9 to 10 — owns the channel.** Controls distribution or listings at a licensed venue that already sells third-party regulated products to individuals at a $5k to $25k ticket outside the US. Or runs a treasury that has actually awarded an external mandate. Or owns an earn or wealth desk that lists third-party yield products. Named as of September 2026: DigiFT, ADDX, InvestaX/IXS, IFSCA-registered distributors, DAO treasury councils with an RFP history.
- **7 to 8 — one step from the money.** A curator or risk firm that runs partner vaults for third-party issuers (Steakhouse does this for Superstate, Centrifuge, Angle, M^0 and Coinshift; Gauntlet has a partner-vault programme). A lending protocol lead who decides collateral listings. A regulated-stack vendor: ERC-3643 issuance, transfer agency, qualified custody for permissioned tokens, a secondary venue.
- **5 to 6 — credible but no path this year.** Asset managers who could manufacture credit. Singapore, Dubai or Gulf wealth principals with no public tokenized book. Foundations and DAOs with a treasury but no history of external mandates. Also: someone who runs exactly the right function but in the wrong jurisdiction or inside a firm that will never sell it to aarnâ. That is precedent and a relationship, not a channel, and it scores 6, not 8.
- **3 to 4 — same sector, no commercial surface.** Researchers, journalists, policy people, conference organisers, analysts. Real credibility value, no deal.
- **1 to 2 — no overlap.** Consumer crypto, gaming, NFTs, memecoins, chains, dev tooling.

**Name which of the four needs they serve.** "Partnership 8, need 3 (collateral)" is useful. A bare number is not.

**Score the person, not the logo.** A head of partnerships at a licensed marketplace outscores a famous founder whose firm has nothing aarnâ can use.

**Never inflate for proximity.** A crypto VC who might invest one day is not a 9. Neither is a big name who would be nice to know. If you cannot name the specific thing they control, the score is 5 or below.

## Step 3c: the competitor flag

Separate from both scores, and mandatory. Mark **Competitor**, **Partner**, or **Both**, with one line of reasoning.

**Both, as of September 2026:** Karpatkey (agent-powered policy-bound vaults, the same sentence as âTARS, and also the firm DAOs already trust for distribution). Steakhouse and Gauntlet (they compete for the same treasury dollar and are also the route to an earn page). Zoth (tokenized emerging-market credit, and already a past guest).

**Competitor on the treasury sleeve:** Avantgarde, Re7, and other automated treasury managers.

**Competitor on the USD credit sleeve:** Maple, Centrifuge, Midas, and the tokenized private-credit distributors generally.

**Check for a tokenized credit product specifically.** Several large regulated managers now run one. Where a guest's firm has shipped something structurally close to aarnâ's India credit token, say so, and say whether the buyer is genuinely the same (jurisdiction, ticket size, investor type) before calling it a competitor.

A competitor can still be a great episode. It cannot be presented as a friendly booking without saying so.

## Step 4: the verdict

| Verdict | Criteria |
|---|---|
| **Book immediately** | Fit ≥ 8 and no red flags. Or Fit 6 to 7 with Partnership ≥ 8, in which case say plainly that the partnership is the reason |
| **Strong consider** | Fit 7. **Then break the tie on Partnership:** ≥ 6 leans book, below 6 leans pre-call. Say which way it broke and why |
| **Pre-call needed** | Fit 5 to 6 with Partnership below 8. Or seniority, depth or traction that needs testing |
| **Decline** | Fit ≤ 4 and Partnership ≤ 6. Or already recorded. Or an auto-decline trigger |

**Why Strong consider now carries a tiebreaker.** Across the pipeline, Sri approved 24 of 33 decided Book Immediatelys and split 13 to 14 on Strong Consider. A verdict that predicts nothing is not a verdict. The Partnership axis is what breaks it, and that matches why he runs the show.

**A high Partnership score with a low Fit score is not automatically a booking.** Say so directly: this is a meeting, or a sponsored slot, not an editorial one. Then say who should take that meeting.

**When a precall has already happened, "Pre-call needed" is off the table.** Resolve to Book, Sponsored or Decline on what the precall showed.

## Step 4b: the sponsored track

un# takes sponsored guests. They run on a separate commercial path, and the eval still runs.

**Sponsored lowers the bar. It does not remove it.** In Akshay's own pipeline, several sponsored prospects were still evaluated Decline.

**The sponsored floor, all four required:**

- A real operating company with a live product
- No fraud history, enforcement action or indictment
- No memecoin or token-price promotion in their public output
- Something a general crypto audience can learn from for an hour

A guest who clears the floor but not the editorial bar → **Sponsored track**, with one line on the angle that would make the episode worth listening to.

A guest who clears the floor and scores Partnership ≥ 7 → say so. **A real commercial counterparty should not be charged for the slot.** That is the one case where the sponsored framing should be dropped and the guest moved to the editorial track.

## Step 5: publish the page

Build the page content and publish it with the Artifact tool, then paste the link into the pipeline sheet.

**The page carries no internal status.** No pipeline stage, no "Sri approval pending", no CRM language, no reference to the sheet. It gets shared, and internal ops on a shared page reads badly. The verdict, the scores and the evidence are the page. Status lives in the sheet.

**Load the `artifact-design` skill before writing it.** Write page content only: no doctype, html, head or body tags, since the tool wraps the file in its own skeleton. Put the `<title>` and `<style>` at the top. Inline all CSS. Google Fonts is the only permitted external host.

Title it as a name: "Raagulan Pathy eval" works, "Guest eval" does not.

Dark theme, the aarna palette, the same one the un# host dossier uses. Define the full palette on bare `:root`, set `color-scheme: dark`, give `body` an explicit background.

```
--bg:#0E1010  --surface:#171A1A  --raised:#1F2423  --rule:#2C3030
--ink:#E8EAEA  --ink-soft:#B5BCBC  --ink-mute:#6B7474
--teal:#1FBFB0  --teal-deep:#0FA095  --teal-glow:#6FE5D8
--coral:#C97A4B
```

Manrope for body and UI, JetBrains Mono for scores, dates and tags. Teal for the Fit score, teal-glow for Partnership, coral for red flags and the competitor tag.

Sections, in order:

1. **Verdict banner**, with the track (Editorial, Sponsored, Decline) as a tag beside it. Tag whether a precall was read
2. **Header and a one-line synthesis.** The header line carries the evaluation date, whether a precall was read and when, and the recording window if one is set
3. **Two scorecards side by side.** Fit, with one line on how the guest sits against the bar. Partnership, with one line naming which of the four aarnâ needs it serves. If the editorial priority was applied, say so here
4. **Competitor flag**, if the guest is a competitor or both. Omit when they are neither
5. **Career timeline**, forward chronological, 5 to 8 rows, crypto entry point marked explicitly
6. **Key facts.** Current state: stage, AUM or TVL or revenue, token, funding, backers, recent milestones, audits, regulatory permissions. For a non-founder: title, scope of authority, influence signals, the org's standing. **Where the precall and the public record disagree, show both and label which is which**
7. **The story.** The angle this guest brings, or the honest absence of one. When a precall happened, say what it settled
8. **Themes to cover**, 5 to 7
9. **Better fit**, only when a stronger name at the same org was verified
10. **Red flags**, only if any. Logistics from the precall belong here
11. **Links.** LinkedIn, company, the precall notes Doc if one exists, one to three substantive recent pieces

## Step 6: the short pitch

After publishing, write the short pitch in the chat reply beside the link. Akshay pastes it into the pipeline sheet, and Sri reads it to decide in ten seconds whether to open the eval.

**The governing principle: the short pitch earns the ten seconds, the eval earns the hour.** It proves this person is worth opening the eval for. It does not summarise the eval.

**Format.** The guest's name as a markdown link to their LinkedIn profile, then the pitch. **The link is mandatory**, because Sri clicks through and reads the bio himself. With no LinkedIn, use the best bio page in this order: X profile, the company's own leadership page, a conference or industry-body speaker bio. Never a data-broker page or a paywalled profile.

> **[Ryan Louvar](https://www.linkedin.com/in/ryanlouvar/).** Chief Legal Officer at WisdomTree, a listed $170B asset manager with 15 SEC-registered tokenized funds holding just over $1B across eight chains. He won the market's only SEC relief for 24/7 stablecoin trading of a tokenized money market fund and wrote tokenized MMFs into the GENIUS Act.

**Length.** 40 to 50 words. Up to 70 only when the case rests on something that is not a number, as above, where two policy wins carry it.

**Order.** Role, then scale, then the one thing nobody else has. If Sri stops at the first comma he knows who this is. If he reads to the end he knows why this one.

### What gets in

- **One number per dimension, and only the current one.** Scale, traction and rate of change get at most one figure each. A spread of figures for the same thing reads as research, not as a case.
- **The guest's own number over the published one.** The precall beats the press, every time. Keep dates on anything inside twelve months, because freshness is part of the claim.
- **The right scale number for what the firm actually does.** Asset manager or fund → AUM. Protocol → TVL. Operating company → revenue. A company whose own balance sheet is the product → market cap. Never substitute one for another. WisdomTree's market cap is $3.0B against $170B AUM, so using market cap would make a guest who runs $170B read as a $3B company.
- **Facts ranked by whether they change a booking decision**, not by whether they are impressive. A 40-person digital assets team is notable and changes nothing.
- **The rarest credential, and not the ones it already implies.** A statute rewritten implies operating at the policy level. Adding the congressional testimony spends words repeating it.
- **Superlatives only when sourced and checkable.** "The market's only SEC relief" survives because he said it and it is verifiable. Leading, pioneering, major and top-tier do not.
- **Unknown is a fact worth stating.** "No TVL or revenue public for a VC fund" beats silence, because it tells Sri not to go looking.
- **"Listed" when the firm is public**, as one word. An AUM figure from a private firm is a claim; from a listed firm it is audited and disclosed, which is a real credibility difference against the bar.

### What stays out

- **Biography.** Career arc, education, prior firms. That is the eval's job and it has never made anyone book a guest.
- **The ticker and the exchange**, unless the listing is doing work: the listing is the business model (a treasury company), the market cap or IPO raise is the scale number, or the person's role only makes sense at a public company. Otherwise the AUM or revenue figure has already established the institution and the ticker is furniture. The same test kills "headquartered in", legal entity names, registration numbers and founding years.
- **Anything needing a second sentence to land.** If the fact requires setup, it is a theme, not a pitch line.
- **The best surprises.** The most interesting thing found in the precall stays in the eval. Putting it here spends the reward that should make Sri open the page.
- **Anything already elsewhere in the same message.** The verdict, both scores and the competitor flag sit beside the pitch, not inside it.
- **Negative facts, unless they would flip the yes.** A stale headline number belongs in red flags. Active enforcement belongs in the pitch, because it changes the answer.
- **Product surface.** Individual products, integrations and partnerships are what gets discussed once he has said yes.
- **An alignment or "why this matters for aarnâ" clause.** Sri works that out himself in the time it takes to read the pitch, and spelling it out reads as condescension. The Partnership score already carries it.

### How it is written

- **The title gets the shortest form that still establishes authority.** Anything the rest of the pitch proves, the title should not claim. "Chief Legal Officer at WisdomTree" is enough when the next thirty words are nothing but tokenization. Never invent seniority in the compression.
- **No abbreviation that collides with the guest's own sector.** "CLO" reads as collateralized loan obligation in a credit conversation. Spell it out.
- **Attribute rather than hedge.** "KAST says it has a million users" beats "reportedly has around a million users". A company claim stated as a company claim is honest and costs two words.
- Third person, present tense, flat and factual. No selling.
- Every voice rule below applies here too, em-dashes and negative parallelism included.

### The chat reply

The verdict line, then the short pitch. Nothing else, no preamble, no offer to revise.

> Verdict: Book immediately. Fit 9, Partnership 6 (regulated stack). Competitor: both, lightly.
>
> **[Name](bio link).** [short pitch]

Other verdict lines:

> Verdict: Book immediately (partnership). Fit 6, Partnership 9, distribution. Competitor: no.

> Verdict: Decline (junior contact). Fit 3, Partnership 2. Better fit at the same org: [Name], [Title].

---

# Constructing the sections

## Career timeline

Forward chronological, 5 to 8 rows. Major education, pre-crypto career, the crypto entry point marked explicitly, each significant role and company founded since, and meaningful exits or transitions. Skip internships and advisory-only roles unless they carry the story. Write "circa 2017" rather than guessing an exact year.

## Themes to cover

The segments Sri would actually anchor an hour around. Each one:

- **Specific to this guest.** Not "his founding journey" but the mechanism only he can explain.
- **Worth 10 to 15 minutes**, not one question.
- **Anchored in** a technical or operational angle he has lived, a macro thread he is positioned to address, or a contrarian read that is hard to source elsewhere.

Mix personal-arc, macro and educational themes. The educational ones matter because the audience runs wider than DeFi. Where the guest allows it, include one that hits Sri's own focus: DeFi structured products, AI and tokenization, TradFi-DeFi convergence, and the curator-versus-rail argument he has been making publicly.

**Lead with what the precall surfaced that is not public.** An internal product, a capability held back, a policy fight the guest won, a number nobody has published. That theme is the one no other podcast can run, so it goes first.

**Use the guest's own suggested questions and say they are the guest's.** They usually point at what the guest is best at, which is also what they will answer well.

**Where the guest scores 7 or above on Partnership, add one theme that opens the commercial conversation naturally.** Their distribution model, their listing criteria, how they choose what goes on the platform. It is a real editorial question and it is also the meeting.

---

# Voice rules for the page

- Blunt and opinionated. This is Akshay's decision aid, not a PR document
- **No em-dashes.** Commas, parentheses, or two short sentences
- **No negative parallelism.** "The question is not whether X, it is whether Y" is banned outright. Make the positive claim and stop
- **Banned:** exciting opportunity, great potential, amazing journey, powerhouse, thought leader, game-changing, passionate, world-class, trailblazing, pioneering, revolutionary, disruptive, deep dive, unpack
- **No internal acronyms.** Write "aarnâ's India credit token" in full. If a term appears only in internal notes and not in the company's public material, spell it out or drop it
- Concrete numbers with dates and a source. "$1.2B TVL, DefiLlama, September 2026" beats "$1.2B TVL". If a number is unknown, write "Unknown"
- **Date every incident, raise and milestone.** An undated fact reads as current and usually is not
- Flag uncertainty inline with "(couldn't verify)". Never fabricate
- Vanity signals stay out of Key Facts. Magazine features and "Top X" lists prove nothing on their own. Follower count and media tier are legitimate only as evidence of weight for a non-founder
- Do not treat market cap as product quality, or as a proxy for institutional size, or high TVL as usage when it is mercenary capital. Say when a metric is misleading

---

# Defensive notes

Each of these is a real failure, not a hypothetical.

- **Don't skip the Drive search.** A WisdomTree eval shipped without it while a full precall transcript from the previous day sat in Drive. It had the guest's real AUM, a team size and an internal product that appear nowhere public, a policy win better than the one the eval led on, and a piece of legislation the eval described as live that had actually stalled
- **Don't treat press coverage as current.** Published figures lag the guest's own numbers by months. When a precall exists, its numbers win
- **Don't trust the embedded roster alone.** It was 14 names when the archive held 47, and it omitted Sandy Kaul while the skill held her up as the model for the bar. Search the project transcripts first, every time
- **Don't assume the open web knows.** A guest who has recorded but not yet aired returns nothing. The transcript archive is the only check that catches them
- **Don't read the pipeline sheet's "Declined" as Sri declining.** It means the guest declined us
- **Don't put internal status on the published page.** No pipeline stage, no approval state, no CRM language. That page gets shared
- **Don't ship the short pitch without a bio link.** Sri clicks through. A pitch with no link makes him go and search
- **Don't copy an old short pitch's furniture.** The ticker in a previous WisdomTree line was carried over by pattern-matching rather than decided. Every element has to earn its words on this guest
- **Don't swap one scale metric for another.** Market cap is not AUM. Using it on an asset manager shrinks the guest by an order of magnitude
- **Don't let a title stand in for tenure.** A "Head of" at a marquee foundation one year out of an MBA was scored as a senior player; Akshay called him too junior for Sri. Count the years in the ecosystem from the career dates first
- **Don't score the firm.** Two people from the same firm land on opposite sides, and both cases are in the record
- **Don't let a big number carry a guest.** Approved and declined pitches have roughly the same median scale
- **Don't inflate Partnership for proximity.** If you cannot name the specific thing the person controls, it is a 5 or below. The right function in the wrong jurisdiction is a 6
- **Don't call an issuer a distributor.** A firm that only sells its own products cannot distribute aarnâ's India credit token. Look for a third-party issuer already listed on their platform
- **Don't book a competitor without flagging it.** Agent-driven treasury management and tokenized emerging-market credit are the two overlaps
- **Don't put the credit managers in writing.** Public copy names no manager. Anything Akshay said privately stays out of the artifact
- **Don't date the India credit token from a private plan.** Public record says IFSCA Sandbox Stage 1 approved April 2026, Stage 2 in review, Q4 2026 target
- **Don't use the ICT acronym.** It is internal shorthand, not public, and Akshay does not use it in conversation
- **Don't leave Strong consider unresolved.** It is a coin flip in the record. Break it on Partnership and say which way it broke
- **Don't charge a real partner for a sponsored slot.** Partnership 7 or above belongs on the editorial track
- **Don't skip the sponsored floor.** Sponsored prospects have been evaluated Decline before and should be again
- **Don't apply the tokenization tilt silently.** Say in the artifact that it was applied, and flag it for confirmation once it is more than about six months old
- **Don't ship the eval as a loose file.** It gets published and the link goes in the sheet
- **Don't repeat a transcription error.** Gemini transcripts garble years, figures and names. When a date in the transcript contradicts the surrounding story, flag it rather than reading it back
- **Don't write generic themes.** "His journey" and "lessons learned" are not themes

## The bar

Sri's own fear about his show, stated 6 March 2026:

> "is it boring content? I might be finding it very exciting to talk to someone else who is in the same boat as me and going into stuff which we both enjoy talking about. So we are both happy but the audience is not. Those are all lost opportunities then."

A guest who is commercially useful and boring on tape still fails. Partnership potential buys a conversation, not an exemption from being worth listening to.