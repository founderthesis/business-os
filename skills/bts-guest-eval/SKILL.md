---
name: "bts-guest-eval"
description: "Decide whether a founder fits Built to Share (B2S), Satish Mugulavalli's Hissa podcast, under the guest profile Satish set in October 2026. Trigger on \"bts-guest-eval\" or \"/bts-guest-eval\" followed by a name, company or LinkedIn URL (with or without the guest's reply), or on \"should Satish book X\", \"is X a B2S guest\", \"evaluate this B2S guest\", \"X replied to the B2S invite\", or a list of names to screen for Built to Share. Works for a prospect before outreach and for a guest who replied. Auto-declines past B2S guests, anyone linked to Qapita or another Hissa competitor, and anyone already booked. Tests the guest against Satish's three lanes (Outlier business model or ownership structure, Discovery name, Global unicorn founder), scores Satish Fit with the strongest lane as the anchor, and publishes one decision page with a verdict of Book immediately, Strong consider or Decline."
---

# bts-guest-eval: is this a Satish guest?

Built to Share is the Hissa podcast, hosted by Satish Mugulavalli. In October 2026 Satish changed the guest profile, and every approval he gave before 18 Oct 2026 was rescinded (decision 328). This skill encodes the new profile. Use it to rebuild the list from scratch and to judge anyone who replies.

The reader is **Akshay first, Satish second.** Akshay curates every guest (decision 326): he reads the eval and decides whether the name goes on Satish's board. Satish then decides on his board. Write for both: blunt, plain English, every uncertain fact flagged.

**This is a direct evaluation. Built to Share does not do pre-calls.** The verdict stands on the research and the reply, if there is one. Thin evidence is not a reason to hedge.

## What Satish wants now (October 2026)

A guest fits if they clear **at least one of three lanes**. The lanes are different reasons to book, so a guest needs only one. Name the lane on every eval.

### Lane 1: Outlier (business model or ownership structure)

A founder whose company works in a way almost nobody else's does, either in **how it makes money** or in **who owns it and who shares in it**.

- **AppsForBharat** (Prashant Sachan, Sri Mandir): devotional tech. A large consumer business built on faith and ritual, a category most investors wouldn't touch. That's the business-model outlier.
- **Jaipur Rugs** (Nand Kishore Chaudhary): built on a community of rural weavers, with impact at the core of the model. That's the ownership-structure outlier.

Both have already recorded. They're the benchmark, not targets.

The test: **can you say in one sentence what is unusual, and why the obvious version of this business doesn't work that way?** If the sentence is "a D2C brand, but in a new category", it isn't an outlier. The unusual part has to be structural.

Shapes that usually qualify:
- Cooperative, community-owned or employee-owned companies; profit or equity shared with suppliers, artisans, farmers, drivers or frontline workers.
- Founders who gave away or locked up ownership on purpose (trusts, steward ownership, a foundation holding the company).
- Businesses in categories the market treats as unbackable (faith, rural crafts, death care, caste-blind matchmaking, prison labour, sanitation), built to real scale.
- A family business that changed its ownership model in a way other families talk about.

It still has to be a **real business at real scale**: revenue, people, years. An NGO, a small social project or a pre-revenue idea is not an outlier guest, however unusual.

### Lane 2: Discovery name

A founder so well known that **their episode gets Built to Share discovered**. People search for them, share their clips and follow them.

- **Sanjeev Bikhchandani** (Info Edge, Naukri)
- **Jaydeep Barman** (Rebel Foods)

The test: **would a typical Indian startup or business audience recognise the name without the company attached?** Evidence, in order of weight:
1. A founder of a household name (listed, or a widely used consumer brand) who people quote.
2. Their own reach: LinkedIn and X followers, YouTube views on their past interviews, mainstream (not trade) press.
3. Likely to share the episode: they post about their own appearances.

This lane is about **business fame.** A founder who is famous for business fits. A TV personality, film star or influencer whose fame has nothing to do with building a company does not, because the conversation goes nowhere Hissa can use.

Note: Sanjeev Bikhchandani and Jaydeep Barman are Akshay's own relationships (decision 327). For anyone in that group, the invite comes from Akshay, never from cold outreach.

### Lane 3: Global unicorn founder

A **founder or co-founder of a company valued at USD 1 billion or more** (now, or at its peak with the company still operating), based outside India, who can teach Indian founders a global best practice.

The test: **name one practice this founder is known for that Indian startups don't do yet.** For example: how they share equity, set pay, hire senior people, build remote teams or run culture at scale. A founder with a unicorn but no transferable practice is weak in this lane. The practice is the episode.

What counts:
- **Founder or co-founder only.** A CEO hired in later, a CXO or a VP doesn't clear this lane.
- **Valuation from a priced round, an IPO or a sale**, with the source and date. Use the peak if the company is still operating and the peak is public. A unicorn that collapsed or shut down doesn't count.
- **An India link is a plus, not a requirement.**

Indian unicorn founders aren't Lane 3. They qualify through Lane 1 or Lane 2, or not at all.

### What runs across all three lanes

- **Operators, not investors.** The guest has built and run a company. VCs, angels, consultants, bankers, lawyers and HR leaders don't fit any lane. (The one exception: a famous VC who founded a company first can still be a Lane 2 name.)
- **Founders beat professional managers.** If the person is a hired CEO, check whether the founder is still there and bookable (see "Better guest available").
- **Open beats guarded.** Satish's review of Season 1 (June 2026) still holds: guests who volunteered specifics and named people made the best episodes, and guarded guests made question-and-answer episodes. This doesn't decide the lane, but it moves the score.
- **The people and ownership thread.** Built to Share is the Hissa show, so every episode still has a people or ownership conversation in it: who they hired, who they gave a stake to, how they kept people. Lane 1 guests have it built in. For Lanes 2 and 3, find it in the research and build the themes on it. If you can't find any, flag it in the held-back bullets. It isn't a cap.

## Inputs

Any of:
- a name, a company or a LinkedIn URL (a prospect, before any outreach);
- the same plus the guest's reply email (a guest who answered our outreach);
- a list of names to screen (run the auto-decline checks and the lane test on each, then a full eval only for those that clear a lane; see "Screening a list").

1. Extract every name, company, URL and fact before searching.
2. If a reply exists, read it as evidence: their stance (yes, conditional, later, redirect, no), what they want to talk about, what they asked for, and who actually wrote (the guest, an EA or comms). A long personal reply with a story in it is the best openness signal you'll get.
3. House answers to common asks (internal flags only, never on the page): no episode review or edit rights; broad themes in advance, never a question list; recording is remote on Riverside; length and format: "(confirm current format with Akshay)". Anything about Hissa's fund or platform: Satish handles it off air.

## Workflow

### Step 1: auto-decline checks (in order, stop at the first match)

**1a. Already a Built to Share guest.** Recorded means Decline, published or not. Check by person and by company.

Roster, 19 Oct 2026 (Engagements, Show = Built to Share, Recorded or later):

| Guest | Company |
|---|---|
| Ajeya Motaganahalli | Pure Storage (Everpure India) |
| Ujjwal Jain | Share.Market / WealthDesk (PhonePe) |
| Ravi Saxena | Wonderchef |
| Ashish Goyal | Fibe |
| Visham Sikand | 1Buy.ai |
| Vinay Kumar | Arya.ai |
| Anurag Jain | CarDekho |
| Vishal Bali | Asia Healthcare Holdings |
| Edul Patel | Mudrex |
| Nand Kishore Chaudhary | Jaipur Rugs |
| Atul Shinghal | Scripbox |
| Ankit Mehta | ideaForge |
| Pravin Agarwala | BetterPlace |
| Ashok Hariharan | IDfy |
| Nakul Kumar | Cashify |
| Ravi Bhushan | BrightCHAMPS |
| Prashant Sachan | AppsForBharat |
| Saurabh Garg | (none; recorded, not to be published) |

The roster lags. Refresh it every run: query Engagements (`collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5`) for the person's rows on Built to Share (Show relation `3ed19a301a7f819e8f45de04a7c9d025`), and search the web for `"Built to Share" "<Name>"`. Apple Podcasts is the most reliable episode list.

A different person from a company already featured is not an auto-decline. It's a More of the same cap (Step 3).

**1b. Linked to Qapita or another Hissa competitor.** Qapita is Hissa's direct rival; ESOP Direct is a Qapita company. Also Carta, Ledgy, Pulley, AngelList, Incentiv and other cap-table, equity-management or ESOP-liquidity platforms.
- Decline if the guest is, or was in the last few years, a founder, employee, board member, investor or formal advisor of any of them.
- Decline if the guest's company is a **publicly named Qapita or ESOP Direct customer** (logo, case study, testimonial, press release).
- A named customer of the others is not a decline; put it in the internal flags.

**1c. Already booked.** An Engagement on Built to Share at Booking or Booked means the eval isn't needed (Guy Tytunovich @ CHEQ is booked as of 19 Oct). Say so and stop.

**Non-blocking checks (note, don't decline):**
- **Founder Thesis past guest:** the person's People row (FT guest ticked) or an FT Engagement at Recorded or later. A past FT guest gets a personal invite from Akshay, never Salesblink (decision 326), and the FT episode is a long-form source for Step 2.
- **Akshay's relationships** (decision 327): Aneesh Reddy, Jaydeep Barman, Sanjeev Bikhchandani, Vinay Singhal. They stay with Akshay.
- **Satish's own links:** his investments (Ultraviolette, STAGE), Hissa investors (Mukesh Bansal), Hissa Fund deals (Miko), YourNest portfolio companies, anything touching Verismo or Revvx. These need his eye: internal flag.
- **A pre-18 Oct "Host approval Yes"** on the row means nothing now (decision 328). Never write "already approved".
- **Restrictions:** a no-contact note, a "## Standing" restriction or a hold on the person's rows. Note it and respect it.

### Step 2: research

Aim for **8 to 12 targeted searches**, at least three of them on the numbers. Stop when you can place the guest in a lane, or show they clear none.

1. **Who and what now.** LinkedIn (capture the URL), current role, founder or hired. The company in one line.
2. **The numbers** (always, whichever lane):
   - funding: total raised, last round (size, date, lead), valuation and its source;
   - scale: revenue (RoC filings via Entrackr or TheKredible for Indian companies, the annual report or DRHP if listed), users or customers, and **headcount**;
   - IPO status (DRHP filed, listed, withdrawn) and market cap if listed;
   - founding year.
   Every number carries a date and a source, graded **(filing)** or **(press)**. A number you looked for and couldn't find stays off the page; note "not public" in the internal flags.
3. **Lane evidence.** Search for the lane you think fits, and test the other two quickly:
   - *Outlier:* the model itself. How it makes money, who owns it, who shares in it, why competitors don't do it. Look for the founder explaining it in their own words.
   - *Discovery:* follower counts (LinkedIn, X, YouTube) with the date, mainstream press in the last 12 months, views on their two biggest past interviews, whether they share their own appearances.
   - *Global unicorn:* the valuation event (round, IPO or sale) with date and source; the practice they're known for (a blog post, a handbook, a talk, a widely cited policy); any India link (team, market, Indian-origin founder).
4. **The people and ownership thread.** ESOP breadth, buybacks, secondaries, employee wealth at IPO, stated views on hiring, pay and equity. For Indian companies, the DRHP's employee stock option section is filing-grade. One to three verbatim lines with links if they exist.
5. **Openness.** At least one long-form appearance (podcast or long YouTube interview). Do they go deep, name people, admit failures? Or repeat the same polished anecdotes everywhere?
6. **Sensitivities.** Search on purpose: layoffs, down round, IPO delayed or withdrawn, ESOP dispute, co-founder exit, regulatory action, litigation.
7. **Better guest available.** If the person is a hired CEO, a CXO or a divisional head, is the founder still there and bookable?

Never guess a figure, quote, name or link. If it can't be stated with confidence, leave it out.

### Step 3: score Satish Fit (1 to 10)

**Score each lane 0 to 10 on its own test, then take the strongest as the anchor.** A guest who clears two lanes strongly (both 7+) gets +1, to a maximum of 10. A lane the guest doesn't touch scores 0. Don't average the lanes.

**Lane bands:**

| Band | Outlier | Discovery name | Global unicorn |
|---|---|---|---|
| 9 to 10 | The structure is the story and it's at scale (Jaipur Rugs, AppsForBharat shape) | A household business name (Bikhchandani shape) | A founder of a category-defining company known for a practice others copy |
| 7 to 8 | Clearly unusual and at real scale; the one-sentence test passes easily | Widely known in Indian startup circles, big personal reach | A unicorn founder with a clear, documented practice |
| 5 to 6 | Unusual in one respect, or modest scale | Known in their sector, modest personal reach | A unicorn founder whose practice is generic or undocumented |
| 0 to 4 | A normal business with a new twist | Not widely known | Not a founder, not a unicorn, or no practice |

**Caps (they apply to the final score, whatever the lane):**
- **Not an operator** (VC, angel, HR leader, consultant, banker, lawyer, advisor): cap 5. Exception: a Lane 2 name who founded a company first.
- **Hired CEO or executive, not a founder**: cap 6 for Lanes 1 and 2; Lane 3 doesn't apply (it's founders only).
- **Guarded or talking-points evidence** (clipped answers in long-form interviews, media only through comms): cap 6.
- **Executive of a large listed company whose remarks need comms or legal sign-off**: cap 6.
- **Live sensitive window** (DRHP quiet period, IPO withdrawn or delayed, layoffs under way, a dispute or regulatory action): cap 6. Name a realistic revisit date in the held-back bullets.
- **More of the same**: same lane and same shape as a recorded guest (another devotional-tech founder after AppsForBharat; another artisan-community company after Jaipur Rugs; a second person from a featured company): cap 6. Compare only against recorded guests.
- **Fame without business** (a celebrity famous for something other than building a company): cap 4.

**Not caps (don't mark down for these):**
- No India link, for a Lane 3 founder.
- Low public profile, for a Lane 1 founder. Outliers are often unknown.
- No ESOP programme, for any lane. It's a theme gap, not a fit gap.
- A guest who said yes. A yes makes them easier to book, not a better guest.

### Step 4: verdict

| Verdict | When |
|---|---|
| **Book immediately** | Satish Fit 8 or above, no red flags, a clear lane and an episode angle you can name |
| **Strong consider** | Satish Fit 6 to 7, or 8+ with a red flag or an ask that needs a polite no |
| **Decline** | Satish Fit 5 or below, no lane cleared, or an auto-decline from Step 1 |

Book immediately here means "put this on Satish's board now". Akshay still decides the board (decision 326) and Satish still decides the guest.

For a Decline on someone who said yes, add one held-back line on how to close it gracefully. Don't draft the mail.

### Step 5: the page

Publish one self-contained HTML page with the Artifact tool. Title: `B2S guest eval: <Name>`. Icon: `microphone`. When the Artifact tool hits its daily limit, republish into a Free Eval slot. Host-show evals are public by default (decision 121), so the page carries **no contact details, PR names, fees or internal status.** Follow the Artifact tool's page rules: colour tokens on `:root` with a dark-mode set, an explicit body background, a phone-width layout with no horizontal scroll, scripts only from the allowed CDNs (none are needed).

The page runs in three acts.

**Decide (30 seconds)**
1. **Verdict banner**: the verdict and Satish Fit `n/10`.
2. **Header**: name, role and company, LinkedIn link, and a one-line synthesis that names the lane and the reason to book.
3. **Lane card**: the three lanes, each with its score and one line. The anchor lane is highlighted. If two lanes cleared, say so.

**Understand**
4. **The business**: the industry structure first, then where the company sits, one or two comparables Satish would recognise, and one line on the thesis. For a Lane 1 guest, this section explains the unusual model in plain terms.
5. **Numbers**: a table, one row per number with its date and its grade (filing or press). Funding, valuation, revenue, headcount, users or customers, IPO status, founding year. Leave out rows that aren't public.
6. **Why this lane**: the evidence behind the anchor lane. For Lane 1, the one-sentence outlier test and how the model works. For Lane 2, reach numbers with dates. For Lane 3, the valuation event and the practice, with a link to where they've described it.
7. **People and ownership**: what they've done (ESOP breadth, buybacks, employee wealth, hiring stories) and one to three verbatim lines with links. Omit the section if there's nothing; never write a line about what's missing.
8. **Career timeline**: five to eight rows, year and event, terse.
9. **Better guest available?**: only when a named, bookable founder at the same company would score higher.

**Prepare**
10. **Themes to cover**: five to seven segments. Each is a bold title naming a moment or decision ("the weaver who became a shareholder", never "ESOP design"), plus one line, ending on the soft way into the people or ownership angle. For Lane 3, at least one theme is the global practice and how it would land in India. Include one theme where the guest agrees or clashes with something Satish has said publicly, if the research found one.
11. **Links**: LinkedIn, company site, one to three substantive press links, the best long-form interview, and the best source for the lane evidence.

**Positive page.** The page may reach Satish and travel further. Risks, gaps, sensitivities, guardedness, competitor ties and relationship notes drive the score but never appear on it. They go in the chat as "Held back from the page" bullets (at most three).

### Step 6: tightening pass (mandatory)

A first draft is always 30 to 40% too long. Re-read once as an editor whose only job is to cut.
- **Each fact lives in one section.** Business description in The business; numbers in Numbers; dates in the timeline; lane evidence in Why this lane; equity facts in People and ownership; why book in the synthesis and lane card.
- **The timeline is a spine:** year plus event, no numbers, no adjectives.
- **Cut throat-clearing:** "notably", "it's worth noting", "interestingly".
- **The test for every sentence:** it states a fact the reader doesn't have, or makes a call they need. Otherwise cut it.

### Step 7: report in chat

```
Verdict: Strong consider. Satish Fit 7/10.
Lane: Global unicorn (7), Discovery (4), Outlier (0).
<the page link>
Held back from the page:
- <up to three bullets>
```

When this runs inside the evals routine, the routine writes the Engagement (Eval link, Eval verdict, the "## Eval (YYYY-MM-DD)" and "## Guest Context" sections, Next action). Also add the anchor lane to the page body's eval section as a line, `Lane: <name>`, so list building can sort by it.

## Screening a list

When given more than one name to judge (list building after decision 328):
1. Run Step 1 on every name. Report the auto-declines in one line each.
2. For the rest, do a quick lane test: two or three searches each, enough to score the strongest lane.
3. Return a table: name, company, anchor lane, lane score, one-line reason, and "full eval" or "drop".
4. Run the full eval (Steps 2 to 7) only on names with a lane score of 7 or more, at most 10 per run, and say how many are left.

Never create Engagements or People rows from this skill. New names go into Notion through `routines/add-guest-names.md`, which matches existing rows first.

## Voice (anything on the page)

- Plain, direct English for Akshay and Satish. "You" where natural.
- No em dashes. No "it's not X, it's Y". No padded lists of three.
- Banned: "exciting opportunity", "great potential", "amazing journey", "powerhouse", "thought leader", "game-changing", "passionate", "world-class", "genuinely", "delve", "leverage", "unlock", "robust", "seamless".
- Concrete numbers, graded and dated. No vanity signals (awards, lists, panels) unless they're the only signal.
- People moves framed forward ("becomes chairman", not "replaces co-founder").
- Never judge a past guest on the page.

## Keeping this skill current

Satish's lanes were set in October 2026. If an eval's verdict and Satish's call on his board disagree three times in a row, flag it to Akshay: the lanes may have moved. Log any change Akshay makes to the lanes in `docs/decisions.md` and update this file.
