---
name: "ft-guest-eval"
description: "Evaluate an inbound Founder Thesis guest request (PR pitch or paid promotion request). Trigger on /ft-guest-eval or ft-guest-eval followed by a name, LinkedIn URL, company, pitch email, screenshot or backgrounder, or on \"evaluate this FT guest\", \"should I book this founder\", \"is this pitch worth taking\". Checks the ThePodium Business OS in Notion for past guests and open engagements first, pins down revenue and funding, maps the guest's career journey, scores Audience Fit and Sales Fit, picks a route (editorial tier, sponsored only, or decline), writes a skimmable eval page inside the Engagement in Notion (verdict, scorecard, sector, market stack and comparables, with infographics and go-deeper links), and creates or updates the Engagements record. Also re-runs after a pre-call when notes are supplied."
---

# ft-guest-eval

Founder Thesis gets a steady stream of inbound guest requests. Most come through PR agencies, and many end up as **sponsored features** (the paid slot, same format and distribution as any episode). This skill answers three questions fast:

1. Has this person already been on FT, or is there already a live engagement for them?
2. Is this an editorial booking, a sponsored-only slot, or a pass?
3. Is there a production-service sale here?

It then logs the result in the Notion **ThePodium Business OS**, so the pipeline stays the single source of truth.

The output is Akshay's internal decision aid. Blunt, opinionated, short.

## Notion anchors (use these exact IDs, never search by database name)

| What | ID |
|---|---|
| Engagements data source | `collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5` |
| People data source | `collection://e6c44319-7f81-4da6-8b80-8441a4875d7a` |
| Organisations data source | `collection://c43c280a-3b37-4821-96ef-dab688a53aea` |
| Episodes data source | `collection://5d250752-6db8-4ab6-8467-c68f5838278a` |
| Founder Thesis show page (the `Show` relation value) | `https://app.notion.com/p/3ed19a301a7f817c9367e0d88afc5776` |
| FT Channel Rules page | `3d219a301a7f813fa919fe4b6c48a72f` |
| Sponsored features page (reach numbers, what's included) | `3ea19a301a7f8109ac3ed03e82c9a9c0` |

The Engagements schema changes as the Business OS evolves. Fetch the data source once per run and write only properties that exist; skip any field below that's missing and mention it in the chat reply.

Relation columns are stored as JSON arrays of `https://app.notion.com/<id>` URLs, so match the show with `Show LIKE '%3ed19a301a7f817c9367e0d88afc5776%'`. If a query errors on a column name, re-fetch the data source schema and rewrite the query. Never guess column names.

## Input

Anything: a name, LinkedIn URL, company, pasted or screenshotted pitch email, backgrounder PDF, or a mix. Re-read screenshots and attachments before searching the web. Note whether the request mentions payment or a sponsored feature, and who brokered it (agency, contact name, email, phone).

**Pre-call re-run.** If the input includes pre-call notes or a transcript for someone who already has an FT engagement with Eval verdict "Pre-call needed", skip to Step 7 and re-score with the call evidence.

## Step 1: History check (always first, before any web research)

Find every past interaction with this person and their company before judging anything. Names are spelled many ways ("Shashwath T R", "Shashwath TR", "T.R.Shashwath"), so never rely on one name search.

1. **People, three ways.** (a) LinkedIn: once you have the guest's `linkedin.com/in/...` URL (Step 2.0 can run first for this), match People `LinkedIn` on the profile slug. (b) Name: search each name token separately (first name, last name, and the last name with spaces and dots removed), `WHERE Name LIKE ?` per token, then pick by organisation. (c) Company: People whose Organisation or Role names the company. Several rows for the same person: use them all, and flag the extras with Match status "Possible duplicate" and Duplicate of the row that has the episode (never merge or delete).
2. **FT guests directory** (collection://b460a8fa-1531-49e5-82f9-133478e2278d): match on LinkedIn, then on Company, then on name tokens.
3. **Engagements** on any show for any of those People rows or the company: Status, Tier, Eval verdict, Migration batch, Episode, Claude note.
4. **Episodes**: any FT episode linked to them, or whose title names the person or the company.
5. **Mail** (Gmail on ad@thepodium.in and MCP Emails on zoya@myunnati.com, read only): search the full name, the name tokens and the company. Note every thread: the PR or agency, past pitches, a thank-you ("Next Steps |" or "Thank you for coming on"), a decline, a sponsored offer, a promise of dates.
6. **Calls**: Drive for Gemini notes ("<Guest> and Akshay Datt ... Notes by Gemini") and the Zencastr folder for a recording under their name; the Engagement's page body for precall notes.

Write what you found as a short **"History with us"** block at the top of the decision page and the Engagement eval: each interaction with its date, channel and outcome (pitched by X on D Mon; precall D Mon; recorded D Mon, episode link; declined; sponsored offered). "None found" only after all six checks.

**Past guest = auto-decline.** Treat the person as a past FT guest if any of these hold:

- People `FT guest` is checked on any of their People rows
- They are linked to an FT episode, or the FT guests directory lists them (LinkedIn, company or name match)
- A thank-you mail or a Zencastr recording exists for them
- An FT engagement has Status `Booked` or `Recorded`, Outcome `Done`, or a `Migration batch` starting with `episodes-`

As a backstop, run one web search: `"Founder Thesis" "<Guest Name>"`. A founderthesis.com, YouTube or Spotify episode link is also a match.

On a past-guest match: verdict = Decline, reason "Already a Founder Thesis guest" with the episode link. Skip research, publish nothing, go straight to Step 8 to log it, and reply in chat.

**Already in the pipeline.** If an open FT engagement exists (not past guest), note its Status and history. You will **update that record**, never create a second FT engagement for the same person. If it was previously declined, say so in the synthesis line and judge whether anything has changed.

## Step 2: Research

Aim for 8 to 12 targeted web searches. Spend them on the LinkedIn URL, metrics, the career journey and the industry explainer first. Stop when you can score confidently and teach the business to a layperson.

0. **LinkedIn URL (mandatory, never skip).** Find the guest's personal LinkedIn profile URL (`linkedin.com/in/...`). Check, in order: the pitch email or backgrounder, the Notion People `LinkedIn` field, then Reach (Reach_MCP scrape_search, account 374, URL `https://www.linkedin.com/search/results/people/?keywords=<First Last> <Company>` URL-encoded, count 3; it finds most profiles in one call and costs one unit per result from the 50-a-day quota, so search by name plus company, never name alone), then a web search `site:linkedin.com/in "<First Last>" <Company>`, then speaker bios and company leadership pages that link out to it. Confirm the profile matches by current role and company. If no profile can be found after these checks, record "LinkedIn not found" (never silently drop it). Also capture the company's LinkedIn page if easy.
1. **Business metrics (the most important research, often decides the call).** Chase each of these until you have a number or have exhausted the sources:
   - Revenue or ARR, with the year. For Indian private companies, check Tofler, Entrackr, Inc42 and The Kredible (they report MCA/ROC filings); for others, Crunchbase, Tracxn, PitchBook snippets, press and founder interviews.
   - **No exact revenue? Collect revenue signals, never stop at "Not disclosed".** Revenue matters most to Akshay, so work down this ladder and report everything you find:
     - **Tofler company page** (fetch it directly, not just the search snippet). Even without Pro it shows the operating revenue band (for example ₹10–25 Cr), the filing year, YoY change in revenue, EBITDA and net profit, margin ratios, debt-to-equity and borrowings growth.
     - **Zauba or MCA charges.** Open secured loans (lender, amount, date) are a scale and health proxy: who lends tells you about credit quality (bank versus NBFC), and big recent charges usually mean capex. Also note authorised and paid-up capital and the last balance sheet filed.
     - **Headcount.** LinkedIn company size, AmbitionBox, Glassdoor, careers pages. Use industry revenue-per-employee to sanity-check the band.
     - **Other proxies.** IndiaMART or TradeIndia turnover bands, GST turnover bands, D&B listings, export or import records, government tender wins, named enterprise customers, number of sites or labs, and revenue the founder has said in interviews.
     When two sources conflict (Tofler sometimes shows two bands), report both and say which you trust.
   - Total funding raised, last round (size, stage, date, lead investor), and valuation if reported.
   - Profitability or burn if reported, team size, and named customers.
   Record the source and year next to every number. Direction matters as much as size: flag revenue decline, losses or rising debt. When a metric truly isn't public after the ladder above, write "Not disclosed", list the signals you checked, and say in one line what its absence suggests (for example "no round found on Crunchbase, Tracxn or press: likely bootstrapped or pre-funding").
2. **Career journey.** Rebuild the guest's LinkedIn experience section: every role with title, organisation, start and end dates, and duration, plus education with years. Capture each organisation's website URL so it can be linked. Use LinkedIn search snippets, speaker bios, company About pages, alumni pages, press profiles and podcast intros. Where a date can't be confirmed, write "circa" or "dates unconfirmed". This is how Akshay judges depth of experience, so don't skip roles.
3. Substantive signals only: YC, top-tier leads, regulatory clearances, named enterprise logos, gated government programmes. Ignore vanity press, "Top 30 under 30" lists and conference panels.
4. Recent press, last 12 months.
5. Whether they already host their own show (for the Sales Fit tag only). Don't research past podcast appearances, talks or long interviews: Akshay doesn't score guests on their media track record, so never list its absence as a gap or watch-out.
6. **Org leadership scan.** Search for the founder, co-founder, executive chairman or group CEO, in case the pitched person is a hired CEO or divisional head and someone more interesting is bookable. If you find a plausible better guest, find their personal LinkedIn profile URL too, using the same method as step 0.
7. **The business in its industry (budget 2 to 4 searches; this feeds the teaching section, so don't skimp).** Research until you could explain the business to a friend over coffee without notes. Collect:
   - **The product in physical or plain terms.** What the thing actually is and does, and where it ends up (what it's a component of, what end product or decision it touches). Define every piece of jargon you'll need.
   - **Who pays, and why.** The named buyer types (or named customers), the pain they're paying to remove, and roughly what they pay (price per unit, contract size, take rate).
   - **The value chain.** Who sits upstream (suppliers, inputs) and downstream (customers, end users), and where the margin pools sit.
   - **Industry size and who wins it.** Market size with year and source, the leaders and their approximate share, and why incumbents are hard to dislodge (capex, IP, certification, switching costs, network effects).
   - **The company's position.** Its scale versus the leaders, its edge or wedge, and what's new or changing that gives it a shot.
   - **Unit economics.** How money is made per unit or per customer, gross margin range for this kind of business, and capex or working-capital intensity.
   - **Model test.** Does the revenue model (SaaS, services, transaction fees, hardware margin) scale in this industry, is there a tailwind or headwind right now (regulation, budgets, platform shifts), and how well funded are the competitors?
   - 1 to 2 comparable companies a generalist would recognise, with their websites.
   Record a source next to every industry number.

If a backgrounder is attached, treat it as the source of truth, but verify any time-sensitive claim (funding round, CEO change) with one fresh search.

## Step 3: Calibrate against the channel

Before scoring, pull evidence from FT's own history:

- **Comparable past episodes.** Query Episodes for FT episodes in the same `Sector` (or with a similar business, found by title), with `YouTube views`. Pick the 2 to 3 closest comparables and note their views. This anchors Audience Fit and tests for a repeat story: if FT already has several near-identical episodes, apply the soft drag in Step 4.
- **Channel rules.** Fetch the FT Channel Rules page and apply any rule about guest types, sectors or profiles that perform or underperform. Cite the rule in one bullet if it moves the score.

## Step 4: Score

### Audience Fit (1 to 10)

One composite score across three angles. Strength in any one can carry the score if the others aren't negative.

- **Founder profile.** Substantive signals, personal brand, recognisability to an Indian founder and operator audience.
- **Business scale.** Revenue (exact figure or signal-based band), funding, valuation, team size, logos, footprint. Weigh this heavily: the metrics block from Step 2 often decides the verdict. Falling revenue, losses or heavy debt pull the score down. No revenue signal at all and no funding is a strong drag unless the topic or the founder's arc is exceptional.
- **Topical relevance.** Hard-to-source domain expertise: deep tech, semis, defence, drones, AI infra, robotics, climate hardware, novel finance, drug discovery.

**Never score on media presence.** A guest with no podcasts, talks or long interviews on record loses nothing for it.

**Caps (apply even if other angles are strong):**

- 20-something founder with under ~3 years of significant operating tenure: cap 5 (Akshay's experience with very young founders hasn't been good; a 28-year-old with a 7-year scaling record gets no cap)
- Professional CEO of a large corporate, not a founder: cap 6 (exception: a rare institutional voice, judged case by case)
- Pre-revenue founder in a generic domain (another SaaS, D2C or marketplace): cap 4

**Soft drag, not a cap:** a story FT has clearly done before (per the Step 3 comparables) pulls the score down by a point or so. Name the comparables and let it weigh, but it never sets a ceiling.

**Lift for VC fund GPs:** a GP or managing partner of a VC fund gets +1 to 2. They're ecosystem door openers: founder intros, co-investor and LP networks, and portfolio founders as future guests. Give the full +2 to an established fund with a track record, +1 to a first-time or sub-$25M fund.

**No cap for:** B2C or D2C with real scale (Series B+, ~$10M+ revenue or strong brand), or very early founders in niche technical domains.

**Reference points** (from the sponsored features page): IPO'd and unicorn founders such as Dinesh Agarwal, Sanjeev Bikhchandani, Amit Jain and Bhavin Turakhia sit at 9 to 10. A Series A B2B SaaS founder with a familiar story sits around 4 to 5. Use the Step 3 comparables to place everyone in between.

### Sales Fit (1 to 10)

Would Akshay sell them his podcast-production service? The ICP is VCs, B2B startups and software-services firms that sell to senior decision-makers.

- Up: clear B2B, VC or services orientation; Series A+ or ~$3M+ ARR; the founder is the public face; already active on LinkedIn; sells to enterprise.
- Down: pure consumer brand; listed company with a big comms team; too small to pay an agency; a corporate CEO for whom podcasting won't be a procurement line.
- **Paid-request signal.** Someone requesting or accepting a sponsored feature has already shown budget and an appetite for long-form media. Add 1 to 2 points if the profile is otherwise in the ICP.
- **Already hosts a podcast.** Tag it "Has podcast". It lowers the need but opens a production-as-a-service pitch.

Sales Fit never moves the verdict. It decides whether a sale gets flagged.

## Step 5: Verdict and route

The verdict is driven by Audience Fit. The **route** says what kind of slot it is.

| Verdict | Criteria | Route |
|---|---|---|
| Book immediately | Audience Fit 8+, no red flags, distinctive story | Editorial, Tier 1 or 1.5 |
| Strong consider | Audience Fit 6 to 7, or 8+ with minor flags | Editorial, Tier 1.5 or 2 |
| Pre-call needed | Audience Fit 5 to 6 with open doubts about scale or depth that a call can settle; professional CEOs needing vetting | Editorial Tier 2 or Spotlight (Tier 3) pending the call, or Sponsored |
| Decline | Audience Fit 4 or below, a past guest, or clearly not the FT audience | **Sponsored only** if the guest wouldn't embarrass the show, otherwise a flat decline |

**The sponsored-only bar.** For a paid slot, the question isn't "is this a great episode". It's three checks:

1. Is the business real and verifiable?
2. Is there enough business substance to fill a 60 to 90 minute conversation?
3. Would an FT viewer feel misled?

A sponsored guest fails on any red flag of fraud, regulatory trouble, unverifiable claims or a business that doesn't exist yet. Spell out which check failed if you recommend a flat decline.

If the request is explicitly paid already, still score Audience Fit honestly. A paying guest who would have earned an editorial slot anyway is worth knowing about: it means the pricing conversation has leverage, or the guest deserves a better tier.

## Step 6: Write the eval page in Notion

The eval is a Notion page **inside the guest's Engagement** (a child page of the Engagement row; do Step 8's Engagement write first if the row doesn't exist yet). Title: `Eval: <Guest> @ <Company> (<D Mon YYYY>)`. Page icon: 🟢 Book immediately, 🟠 Strong consider, 🟡 Pre-call needed, 🔴 Decline. No claude.ai artifact: the page lives in Notion, so the artifact cap never blocks an eval. The model page is Jacob George @ Duroflex (18 Nov 2026), page 41c19a301a7f81d985f1f39a48f423f6.

Write it to be skimmed. Akshay should get the decision from the first screen, and go deeper only where he wants to. Rules that hold everywhere on the page:
- Lead with the point. A line that needs more than one breath to read aloud is too long.
- Bullets over paragraphs. Bold the one fact a skimmer must not miss in each bullet.
- At most two columns side by side (Akshay, 9 Oct).
- Detail goes in closed toggles, never in the main flow.
- No em dashes. Use Notion-flavoured markdown (callout, columns, toggle, tables), never HTML.

Sections, in this order:

**Page layout, Akshay 23 Nov (this wins over the section list below; model page: Eval: Vaibhav Pandey @ Instawork, 41e19a301a7f81518bc9cd92f62747fd).** (1) Lead with a short company TLDR: what the company is, who pays and how big it is, before any verdict ("Need to get a TLDR of the co first before I see the verdict"). (2) Then the verdict callout, then the scorecard as a table at full page width (`<table fit-page-width="true">`), never an image. (3) No infographics at all: no scorecard, stack or comparables images; the stack and comparables stay as tables. (4) Never write a bare "you replied": quote Akshay's actual reply in the callout, with its date. The rest of the order stays as listed; the sector-in-30-seconds part stays inside The business.

1. **Verdict callout** (colour to match the verdict: green, orange, yellow or red background). Line 1, bold: verdict and route ("Strong consider · Editorial Tier 2, only if he'll share numbers"). Line 2: the arc and the reason to book or pass, in one sentence. Line 3: "**Your call:**" the decision Akshay must make, in one line. If an engagement already existed, say that history here ("Pitched in Jan, we declined; now Series B").
2. **Scorecard image** (see Infographics). Verdict, Audience Fit and Sales Fit as bars out of 10, each with a one-line reason, and four tiles: Revenue (with year and YoY), Profit or burn, Funding (last round, lead, date), and the one status that matters most (IPO, valuation, team size). Each tile shows its source year. If no image can be made, use a 2-column table with the same content.
3. **Why yes / Why not** in two columns, three bullets each. Audience Fit's comparables (past FT guests and their views) and Sales Fit's pitch angle or "skip the pitch" belong here.
4. **## The business.** It teaches Akshay the business: after reading it he could explain it to someone else and ask an informed first question. Define every piece of jargon where it first appears. One number or named example per bullet; mark anything unverified "(uncertain)".
   - **What it is** and **Who pays**: one short paragraph each (the product in plain terms; the buyer, what they pay, how the company earns, margin or capex in a phrase).
   - **### The sector in 30 seconds**: 3 to 5 bullets. Market size with year and source, how organised it is, who leads, why it's hard or easy to enter, and what is shifting now.
   - **### Where <Company> sits in the stack**: a stack image (see Infographics) running from inputs to end customer, with the company's layers highlighted and labelled (core, the bet, where the money goes). Under it, 2 to 3 sentences: its moat and its bet.
   - **### Comparable companies**: a comparables image of 4 to 6 named peers (revenue bar, growth, profit, stage), the company highlighted, each row labelled with its fiscal year. Pull peers and figures from Tracxn (competitors of the company, then the named leaders). Under it, one bold "Read it this way:" line saying what the comparison means for the decision.
   - For a simple business (a D2C brand, a restaurant chain), keep What it is and Who pays to one line each, but always keep the sector, stack and comparables.
5. **Toggles, closed:** "👤 Career" (chronological, oldest first, one bullet per role with dates, title, organisation and one line on the role; a total line at the end; "circa" for unconfirmed dates), "📊 Key numbers" (a revenue-by-year table, then rounds, valuation and filings), "🚩 Watch-outs" (diligence and interview risks, and pitch claims that didn't survive checking; include past history with us here), and "🙋 Better guest available?" only when Step 5's conditions for one hold.
6. **## 🔗 Go deeper**, in two columns, every item a link Akshay can click:
   - **The guest:** LinkedIn profile (if not found, write "no profile found" and give a LinkedIn people-search link for "<name> <company>"), 1 to 3 interviews, talks or podcasts he has done, and any news about him.
   - **The company:** website, company LinkedIn, Tracxn page, and 2 to 4 substantive news pieces (funding, IPO, strategy, results), each labelled with what it is and the outlet.
   - **Past FT episodes in this category:** the YouTube links of the comparable FT guests from Audience Fit, with views (from the Episodes database).
   - **Comparables on Tracxn:** each peer's Tracxn page.
   - **Booking:** the PR contact and a link to the pitch Activity.
   End the page with one grey line naming the data sources and the date they were pulled.

### Infographics

Three images per eval: scorecard, stack and comparables. In Claude Code, build each as a small HTML card (Inter font, white background, 900px wide, orange highlight #f0a020 for the company, green #2e7d5b and red #b42318 for good and bad), render it to PNG with Playwright at deviceScaleFactor 2, clipped to the content height, and look at the PNG before using it. Upload each with Notion's create-file-upload, POST the file to the returned URL, and place it with `![alt text](file-upload://<id>)`. Every number in an image must also be in the eval's research with its source, and the image carries a one-line source note. Where images can't be made (no browser), use Notion tables and a callout instead and say so in the chat reply.

### Tightening pass (before writing the page)

- **Checks.** The Go deeper section has a LinkedIn link or a LinkedIn search link. The business section has the sector, stack and comparables. Every jargon word is defined. Fix any miss before writing.
- **One home per fact.** Figures live in the scorecard and Key numbers, roles in Career, the business in The business, risks in Watch-outs. Delete second mentions.
- **Cut throat-clearing.** Remove "notably", "it's worth noting" and narration of your own process.
- **Per-sentence test.** Every line either states a fact the host lacks or makes a judgment the host needs. If it does neither, cut it. Teaching the business counts as facts the host lacks.

## Step 7: Pre-call re-run

When pre-call notes arrive for an existing "Pre-call needed" engagement:

- Re-score Audience Fit with the call evidence, especially any revenue figures the guest shared.
- Pick a final verdict (Book immediately, Strong consider or Decline) and route.
- Update the same Notion eval page from the engagement's `Eval link` (read it first): rewrite the verdict callout and scorecard, and add an "After the pre-call" line under the callout. Never start a second eval page.
- Update the engagement in Step 8: Status `Precall done`, the new Eval verdict, and Next action.

## Step 8: Write to Notion

**Organisation.** Find it by name or domain. If none exists, create it with Name, Website, Domain, Type (Startup, Enterprise or Fund) and Source `Agent`.

**People.** If the guest has no People row, create one with Name, Role, LinkedIn, Organisation, Location, What they do (a short descriptor such as "Fintech, auto loans"), Source `Agent` and Captured (today). On every run, set `Latest eval verdict` (it has no "Evaluate after call" option, so use the closest match). Fill LinkedIn (with the profile URL from Step 2) and What they do only if they're empty. Never touch `Blurb` (the ft-community-blurb chat owns it), `FT guest`, or the duplicate fields.

**PR contact.** If the pitch came through an agency, find or create the contact in People (tag `PR contact`) and their agency in Organisations (Type `PR agency`). Link the contact via `Via`.

**Engagement.** Update the existing FT engagement if there is one, otherwise create one.

- Name: `<Guest> @ <Company>, Founder Thesis`
- Show: the FT show page
- Direction: `Inbound`
- Guest, Organisation, Via: relations as above
- Eval verdict: the verdict. Use `Evaluate after call` only if the eval genuinely couldn't be completed without a call.
- Eval link: the Notion eval page's URL
- Status: `Decision pending` on create. On update, change Status only if the current one is `New`, `Contacted` or `Interested` (or `Precall done` on a pre-call re-run). Never move a record backwards.
- Next action: one line naming the recommended route and step, for example "Offer sponsored feature via SGA" or "Book, Tier 1.5. Ask PR for founder's dates" or "Decline, already a guest (2023)"
- Tags: add `Big name` for Audience Fit 9+, and `Has podcast` if applicable
- Captured: today, on create only
- Source: `Agent`, on create only

**Leave these for Akshay:** Decision, Tier, Heat, Host verdict, Payment, Amount. The recommendation goes in Next action and on the page, not in these fields.

**Page body.** Keep the Engagement page short. At the top, one callout (same colour as the verdict): verdict and route with both scores on line 1, the next step on line 2. Under it, the eval page as a child page, then the pitch in one line (who pitched, when, what they said). On a re-run, update the callout in place; the eval page keeps the history.

If Sales Fit is 7 or above, add a line `PaaS angle: <one sentence>`. Do not create a PaaS engagement; Akshay decides that.

If any Notion write fails, finish the eval anyway and name the failed write in the chat reply.

## Chat reply

Exactly this shape, nothing more:

> Verdict: Strong consider · Editorial Tier 2. Audience Fit 7/10, Sales Fit 6/10. Revenue ₹42 Cr (FY25), raised $12M.
> Eval page: <Notion link>. Notion: created engagement (or "updated engagement, was We declined in Jan").

For a past guest:

> Decline. Already a Founder Thesis guest: <episode link>. Notion: logged.

## Voice rules for the page

- First person, blunt, opinionated
- No em-dashes. Use commas, parentheses or two sentences instead.
- Banned: exciting opportunity, great potential, amazing journey, powerhouse, thought leader, game-changing, passionate, world-class, leverage, unlock, robust, seamless
- Concrete numbers ("Series B, $42M led by Sequoia"). If a number is unknown, write "Unknown". Never guess.
- Flag uncertainty explicitly with "(uncertain)" or "(couldn't verify)". Never fabricate.
- Sentence case for section titles in the source text (CSS can uppercase them)