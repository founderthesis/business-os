---
name: "pathfinders-guest-eval"
description: "Decide whether a person fits Pathfinders (\"Pathfinders by Divir Tiwari, Powered by FieldAssist\"), the founder-led podcast ThePodium produces for FieldAssist, hosted by Divir Tiwari. Trigger on \"pathfinders-guest-eval\" or \"/pathfinders-guest-eval\" followed by a name, company or LinkedIn URL, or on \"should Divir book X\", \"is X a Pathfinders guest\", \"evaluate this Pathfinders guest\", or a list of names from Divir to screen. Auto-declines past Pathfinders guests and anyone already booked; flags anyone tied to a FieldAssist competitor. Tests the guest against three lanes (Route-to-market operator, Consumer founder who scaled, Regional or global consumer leader) and the season 1 plan, scores Pathfinders Fit with the strongest lane as the anchor, and writes one skimmable Notion eval page inside the Engagement (scorecard, sector, market stack and comparables with infographics, go-deeper links) with a verdict of Book immediately, Strong consider or Decline."
---

# pathfinders-guest-eval: is this a Pathfinders guest?

Pathfinders is FieldAssist's podcast, hosted by its co-founder Divir Tiwari and produced by ThePodium (decision 626). Full name: "Pathfinders by Divir Tiwari, Powered by FieldAssist". It is founder-led: Divir's name and face lead, FieldAssist stays subtle.

The reader is **Akshay first, Divir second.** Divir picks his guests (decision 626). Most names come from Divir's own list; the eval helps Akshay and Divir order that list, spot the strongest six for season 1, and say no early to a name that won't make a good episode. Write for both: blunt, plain English, every uncertain fact flagged.

**This is a direct evaluation. There are no precalls for the eval.** The verdict stands on the research and the reply, if there is one. Thin evidence is not a reason to hedge.

## Who Pathfinders is for

The audience is the people FieldAssist sells to and learns from:
- **Sales and distribution leaders** at consumer brands: chief sales officers, heads of general trade, modern trade and quick commerce, distributor and channel heads.
- **FMCG and route-to-market leaders**: the people who decide how a brand reaches the shop counter.
- **Founders** of consumer businesses who built that reach themselves.

India first, then global: season 1 aims for a mix of India, Southeast Asia and US/Canada guests.

**The purpose, in order:** access to decision makers first, audience second, then thought leadership and FieldAssist's brand equity (the 23 Sep call and the SOW). A guest who is a senior decision maker at a consumer brand is worth more to the show than a bigger name with no stake in distribution.

**The season 1 plan.** Six long-form conversations with founders and leaders who built consumer businesses that scale. Each episode covers the playbook that worked, the operating system underneath it, how they kept one thing excellent while everything else grew, and the parts that didn't work. Recording window 25 Dec to 5 Jan; remote, or in FieldAssist's new Delhi NCR office studio. About an hour of conversation, 75 minutes blocked.

## The three lanes

A guest fits if they clear **at least one lane**. Name the lane on every eval.

### Lane 1: Route-to-market operator

Someone who built or ran sales and distribution at scale for a consumer brand: how many outlets, how many distributors, which channels, what changed when they took over.

The test: **can you name the distribution problem they solved, with a number?** Outlets reached, distributors added, a channel built from zero, a shift to quick commerce or modern trade they led. "Head of sales at a big FMCG company" alone isn't enough; the story is what they changed.

Shapes that usually qualify:
- CSO, sales director or head of distribution at an FMCG, food, beverage, personal care, home care, pharma OTC or consumer durables brand.
- A leader who rebuilt general trade, launched a distributor management system or took a brand into rural markets.
- A leader who moved a legacy brand into quick commerce, e-B2B or modern trade.

### Lane 2: Consumer founder who scaled

A founder or co-founder of a consumer brand (FMCG, food and beverage, D2C that went offline, consumer durables) who built real distribution: the brand is on shelves, not only online.

The test: **is the brand on shelves at scale, and did the founder build that reach?** Evidence: outlet count, offline share of revenue, distributor network, retail presence in several cities or countries.

It still has to be a **real business at real scale**: revenue, people, years. A pre-revenue idea or a single-city brand is not a season 1 guest.

### Lane 3: Regional or global consumer leader

A founder or senior leader (VP and above) at a consumer company in Southeast Asia, the US, Canada or another market outside India, who can tell Indian sales and distribution leaders how it's done there.

The test: **name one practice from their market that Indian route-to-market teams don't use yet.** For example: how they run van sales, retail execution, distributor economics, retail media or data-led beat planning. A big title with no transferable practice is weak in this lane.

### What runs across all three lanes

- **Operators, not advisors.** The guest has built or run the thing. Consultants, analysts, bankers and investors don't fit, unless they ran sales or distribution at a consumer company first.
- **Decision makers beat observers.** A sitting leader who decides how a brand goes to market scores higher than a retired one with the same story.
- **Open beats guarded.** Guests who give specifics, name people and admit what failed make the best episodes. Guarded guests make question-and-answer episodes.
- **The playbook thread.** Every episode has a "how it actually works" conversation in it: the operating system behind the growth. If you can't find one in the research, flag it in the held-back bullets.

## Inputs

Any of:
- a name, a company or a LinkedIn URL (usually from Divir's list);
- the same plus a reply from the guest;
- a list of names to screen (see "Screening a list").

1. Extract every name, company, URL and fact before searching.
2. If a reply exists, read it as evidence: their stance, what they want to talk about, what they asked for, and who actually wrote.
3. House answers (internal flags only, never on the page): about an hour of conversation, 75 minutes blocked; remote, or in person at FieldAssist's new Delhi NCR office studio; broad themes in advance, never a question list. The recording platform, the studio link and anything about seeing the episode before release are **to confirm with Akshay**: never promise them. Anything about FieldAssist's product or a commercial conversation: Divir handles it off air.

## Workflow

### Step 1: auto-decline checks (in order, stop at the first match)

**1a. Already a Pathfinders guest.** Recorded means Decline. Query Engagements (`collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5`) for the person's rows on Pathfinders (Show relation `41d19a301a7f810aad39f01621459709`) at Recorded or later. There is no roster yet (season 1 records 25 Dec to 5 Jan).

**1b. Already booked.** An Engagement on Pathfinders at Booking or Booked means the eval isn't needed. Say so and stop.

**Non-blocking checks (note, don't decline):**
- **FieldAssist competitor or customer.** The guest works for, founded, advises or invests in a sales force automation, distributor management or retail execution software company that competes with FieldAssist: internal flag, Divir decides. Which companies count is to confirm with Ankita; until then flag any SFA or DMS vendor. A FieldAssist customer is a plus for access, not a decline: note it.
- **Founder Thesis past guest:** the person's People row (FT guest ticked) or an FT Engagement at Recorded or later. Note it; the FT episode is a long-form source for Step 2.
- **Divir's own relationships.** If the name came from Divir's list, say so in the internal flags; the invite goes from Divir (a WhatsApp for close friends, the guest note for others).
- **Restrictions:** a no-contact note, a "## Standing" restriction or a hold on the person's rows. Note it and respect it.

### Step 2: research

Aim for **8 to 12 targeted searches**, at least three of them on the numbers. Stop when you can place the guest in a lane, or show they clear none.

1. **Who and what now.** LinkedIn (capture the URL), current role, founder or hired, and how long in the role. The company in one line.
2. **The numbers** (always, whichever lane):
   - company scale: revenue (RoC filings via Entrackr or TheKredible for Indian companies, the annual report if listed), outlets or retail reach, distributor count, countries;
   - funding and valuation for startups, market cap for listed companies;
   - headcount, and the size of the sales force where public;
   - founding year.
   Every number carries a date and a source, graded **(filing)** or **(press)**. A number you looked for and couldn't find stays off the page; note "not public" in the internal flags.
3. **Lane evidence.**
   - *Route-to-market operator:* the distribution problem they solved, with the number; the channels they own; interviews or talks where they explain it.
   - *Consumer founder:* the shelf reach, offline share, how the distribution network was built and by whom.
   - *Regional or global leader:* the market, the practice, a talk or article where they describe it, any India link.
4. **The playbook thread.** One to three verbatim lines with links where the guest explains how their sales or distribution system works.
5. **Openness.** At least one long-form appearance (podcast or long YouTube interview). Do they go deep, name people, admit failures?
6. **Sensitivities.** Search on purpose: layoffs, distributor disputes, channel conflict, a recall, regulatory action, a recent exit from the company.
7. **Better guest available.** If the person is a middle manager, is the founder or the sales head at the same company bookable?

Never guess a figure, quote, name or link. If it can't be stated with confidence, leave it out.

### Step 3: score Pathfinders Fit (1 to 10)

**Score each lane 0 to 10 on its own test, then take the strongest as the anchor.** A guest who clears two lanes strongly (both 7+) gets +1, to a maximum of 10. A lane the guest doesn't touch scores 0. Don't average the lanes.

**Lane bands:**

| Band | Route-to-market operator | Consumer founder who scaled | Regional or global leader |
|---|---|---|---|
| 9 to 10 | Ran distribution for a household brand and changed how it reaches the shop counter, with numbers | Built a household consumer brand's offline reach from zero | A leader at a category-defining consumer company known for a practice others copy |
| 7 to 8 | A senior sales or distribution leader at a large brand with a clear, documented story | A founder whose brand is on shelves at real scale in several markets | A senior leader with a clear, documented practice from their market |
| 5 to 6 | A sales leader with a modest or undocumented story | A founder with some offline reach, or mostly online | A leader whose practice is generic or undocumented |
| 0 to 4 | No distribution story | Online only, or not at scale | Not a senior leader, or no practice |

**Season-fit adjustments (apply after the anchor):**
- **+1 decision-maker access:** a sitting decision maker (CXO, sales head, founder) at a consumer brand FieldAssist sells to or could sell to. Maximum 10.
- **Season mix:** if season 1 already has two booked guests from the same region (India, Southeast Asia, US/Canada), note it in the held-back bullets. It isn't a cap.

**Caps (they apply to the final score, whatever the lane):**
- **Not an operator** (consultant, analyst, banker, investor, advisor): cap 5. Exception: someone who ran sales or distribution at a consumer company first.
- **Guarded or talking-points evidence** (clipped answers in long-form interviews, media only through comms): cap 6.
- **Executive of a large listed company whose remarks need comms or legal sign-off**: cap 6.
- **Live sensitive window** (layoffs under way, a dispute or regulatory action, a recent exit): cap 6. Name a realistic revisit date in the held-back bullets.
- **More of the same**: same lane, same category and same story as a recorded Pathfinders guest: cap 6.
- **Not consumer** (B2B software, services, finance) with no consumer distribution story: cap 4.

**Not caps (don't mark down for these):**
- Low public profile. Many of the best route-to-market leaders are unknown outside their industry.
- No India link, for a Lane 3 guest.
- A guest who said yes. A yes makes them easier to book, not a better guest.

### Step 4: verdict

| Verdict | When |
|---|---|
| **Book immediately** | Pathfinders Fit 8 or above, no red flags, a clear lane and an episode angle you can name |
| **Strong consider** | Pathfinders Fit 6 to 7, or 8+ with a red flag or an ask that needs a polite no |
| **Decline** | Pathfinders Fit 5 or below, no lane cleared, or an auto-decline from Step 1 |

Book immediately here means "recommend to Divir now". Divir still decides the guest (decision 626), and no recording time is proposed, created, moved or confirmed without Akshay's ok (decisions 446, 448).

For a Decline on someone Divir put on his list, add one held-back line on how Akshay can raise it with Divir. Don't draft the mail.

### Step 5: the eval page (Notion, decisions 610 to 612)

The eval is a Notion page **inside the guest's Engagement** (a child page of the Engagement row). Title: `Pathfinders eval: <Name> @ <Company> (<D Mon YYYY>)`. Page icon: 🟢 Book immediately, 🟠 Strong consider, 🔴 Decline. No claude.ai artifact and no Eval slot. Follow the layout of ft-guest-eval v2 Step 6 and its Infographics section; the model page is Jacob George @ Duroflex (Notion 41c19a301a7f81d985f1f39a48f423f6). An auto-decline from Step 1 gets no page.

**Positive page.** The page may reach Divir and FieldAssist. It carries **no contact details, fees or internal status.** Risks, gaps, sensitivities, guardedness, competitor ties and relationship notes drive the score but never appear on it. They go in the chat as "Held back from the page" bullets (at most three), and in one "Held back:" line under the callout on the Engagement body, which stays internal.

Write it to be skimmed: lead with the point, bullets over paragraphs, at most two columns side by side, detail in closed toggles, Notion-flavoured markdown (callout, columns, toggle, tables), never HTML. Sections, in this order:

**Decide (30 seconds)**
1. **Verdict callout** (green, orange or red background). Line 1, bold: the verdict and Pathfinders Fit `n/10`. Line 2: the lane and the reason to book, in one sentence. Line 3: "**Next:**" what goes to Divir or why not.
2. **Scorecard image**: Pathfinders Fit as a bar out of 10, the three lanes as bars (anchor lane highlighted, one line each; if two lanes cleared, say so), and four tiles (revenue or scale, retail reach or outlets, team or sales force size, founding year or listing status), each with its source year.
3. **Why this lane / Why it could miss** in two columns, three bullets each. Keep the "why it could miss" bullets positive and factual (the lane gap, not a sensitivity); real risks stay held back.

**Understand**
4. **## The business.** The category and its route to market first, then where the company sits.
   - **### The sector in 30 seconds**: 3 to 5 bullets (market size with year and source, who leads, how the category reaches the shop counter, what is shifting: quick commerce, e-B2B, modern trade, rural).
   - **### Where <Company> sits in the stack**: a stack image from manufacturer to distributor to retailer to shopper, with the company's layers and channels highlighted. Under it, 2 to 3 sentences on its moat and its bet.
   - **### Comparable companies**: a comparables image of 4 to 6 peers Divir would recognise (revenue, reach, growth, stage), the company highlighted. One bold "Read it this way:" line under it.
5. **Toggles, closed:** "📊 Numbers" (a table, one row per number with its date and grade, filing or press; leave out rows that aren't public), "🎯 Why this lane" (the evidence behind the anchor lane, with links), "🧭 The playbook" (how their sales or distribution system works, one to three verbatim lines with links; omit the toggle if there's nothing), "👤 Career" (five to eight rows, year and event, terse), and "🙋 Better guest available?" only when a named, bookable person at the same company would score higher.

**Prepare**
6. **## Themes to cover**: five to seven bullets. Each is a bold title naming a moment or decision ("the year we cut half our distributors", never "distribution strategy"), plus one line. At least one theme is the playbook that worked and one is what didn't work. Include one theme on keeping one thing excellent while everything else grew. For Lane 3, at least one theme is the practice from their market and how it would land in India.
7. **## 🔗 Go deeper**, in two columns, every item a link: the guest (LinkedIn, or a LinkedIn people-search link for "<name> <company>" if none found; the best long-form interview; talks and podcasts), the company (site, company LinkedIn, Tracxn, 2 to 4 substantive news pieces labelled with outlet), the lane evidence (the best source for it), and comparables on Tracxn. End with one grey line naming the data sources and the date pulled.

**Infographics.** Three images: scorecard, stack and comparables. In Claude Code, build each as a small HTML card (Inter font, white background, 900px wide, orange highlight #f0a020 for the company), render it to PNG with Playwright at deviceScaleFactor 2, clipped to the content height, and look at the PNG before using it. Upload each with Notion's create-file-upload, POST the file to the returned URL, and place it with `![alt text](file-upload://<id>)`. Every number in an image is in the research with its source, and each image carries a one-line source note. Where images can't be made, use Notion tables and say so in the chat.

**The Engagement body.** Keep it short: one callout (same colour as the verdict) with the verdict, Pathfinders Fit and anchor lane on line 1 and the next step on line 2, then the "Held back:" line, then the eval page as a child page, then the pitch in one line. Set Eval link to the eval page's URL, plus Eval verdict and Eval date. On a re-run, update the eval page and the callout in place; never start a second eval page.

### Step 6: tightening pass (mandatory)

A first draft is always 30 to 40% too long. Re-read once as an editor whose only job is to cut.
- **Each fact lives in one section.** Business description in The business; numbers in Numbers; dates in Career; lane evidence in Why this lane; how the system works in The playbook; why book in the callout and scorecard.
- **Career is a spine:** year plus event, no numbers, no adjectives.
- **Cut throat-clearing:** "notably", "it's worth noting", "interestingly".
- **The test for every sentence:** it states a fact the reader doesn't have, or makes a call they need. Otherwise cut it.

### Step 7: report in chat

```
Verdict: Strong consider. Pathfinders Fit 7/10.
Lane: Route-to-market operator (7), Consumer founder (0), Regional or global (4).
Eval page: <Notion link>
Held back from the page:
- <up to three bullets>
```

When this runs inside an engagement chat, it writes Eval link (the Notion eval page), Eval verdict, Eval date and the short Engagement body above; workflow fields (Status, Next action, Waiting on) go through the chat's Row change Activity. The callout's line 1 carries the anchor lane as `Lane: <name>`, so list building can sort by it.

## Screening a list

When Divir's list arrives (12 to 15 names, to land 6):
1. Run Step 1 on every name. Report the auto-declines in one line each.
2. For the rest, do a quick lane test: two or three searches each, enough to score the strongest lane.
3. Return a table: name, company, region, anchor lane, lane score, one-line reason, and "full eval" or "drop". Show the region mix of the top six.
4. Run the full eval (Steps 2 to 7) only on names with a lane score of 7 or more, at most 10 per run, and say how many are left.

Never create Engagements or People rows from this skill. New names go into Notion through `routines/add-guest-names.md`, which matches existing rows first.

## Voice (anything on the page)

- Plain, direct English for Akshay and Divir. "You" where natural.
- No em dashes. No "it's not X, it's Y". No padded lists of three.
- Banned: "exciting opportunity", "great potential", "amazing journey", "powerhouse", "thought leader", "game-changing", "passionate", "world-class", "genuinely", "delve", "leverage", "unlock", "robust", "seamless".
- Concrete numbers, graded and dated. No vanity signals (awards, lists, panels) unless they're the only signal.
- People moves framed forward ("becomes chairman", not "replaces co-founder").
- Never judge a past guest on the page.
- Never mention a price, a fee or FieldAssist's commercial terms.

## Keeping this skill current

The lanes come from the season 1 plan agreed with FieldAssist in November 2026 (decision 626). If an eval's verdict and Divir's call disagree three times in a row, flag it to Akshay: the lanes may have moved. Log any change Akshay makes as a row in the Notion Decisions database and update this file.
