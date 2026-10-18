---
name: "ft-guest-eval"
description: "Evaluate an inbound Founder Thesis guest request (PR pitch or paid promotion request). Trigger on /ft-guest-eval or ft-guest-eval followed by a name, LinkedIn URL, company, pitch email, screenshot or backgrounder, or on \"evaluate this FT guest\", \"should I book this founder\", \"is this pitch worth taking\". Checks the ThePodium Business OS in Notion for past guests and open engagements first, pins down revenue and funding, maps the guest's career journey, scores Audience Fit and Sales Fit, picks a route (editorial tier, sponsored only, or decline), publishes a slim decision page, and creates or updates the Engagements record. Also re-runs after a pre-call when notes are supplied."
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

## Step 1: Notion check (always first, before any web research)

Run these against the anchors above. Match on name AND organisation, since names collide.

1. **People.** `SELECT url, Name, Role, "FT guest", Episodes, Engagements, Organisation, "Latest eval verdict", LinkedIn FROM "collection://e6c44319-..." WHERE Name LIKE ?` with `%<last name>%`, then pick the right person by first name and org.
2. **Engagements for that person on FT.** Rows where `Guest` contains the person's page ID and `Show` matches FT. Pull `Status`, `Outcome`, `Stage`, `Eval verdict`, `Decision`, `Tier`, `Migration batch`, `Episode`.
3. **Episodes.** If the person has an `Episodes` relation, fetch those episodes and check whether any belongs to the FT show.

**Past guest = auto-decline.** Treat the person as a past FT guest if any of these hold:

- People `FT guest` is checked
- They are linked to an FT episode
- An FT engagement has Status `Booked` or `Recorded`, Outcome `Done`, or a `Migration batch` starting with `episodes-`

As a backstop, run one web search: `"Founder Thesis" "<Guest Name>"`. A founderthesis.com, YouTube or Spotify episode link is also a match.

On a past-guest match: verdict = Decline, reason "Already a Founder Thesis guest" with the episode link. Skip research, publish nothing, go straight to Step 8 to log it, and reply in chat.

**Already in the pipeline.** If an open FT engagement exists (not past guest), note its Status and history. You will **update that record**, never create a second FT engagement for the same person. If it was previously declined, say so in the synthesis line and judge whether anything has changed.

## Step 2: Research

Aim for 8 to 12 targeted web searches. Spend them on the LinkedIn URL, metrics, the career journey and the industry explainer first. Stop when you can score confidently and teach the business to a layperson.

0. **LinkedIn URL (mandatory, never skip).** Find the guest's personal LinkedIn profile URL (`linkedin.com/in/...`). Check, in order: the pitch email or backgrounder, the Notion People `LinkedIn` field, then a web search `site:linkedin.com/in "<First Last>" <Company>`, then speaker bios and company leadership pages that link out to it. Confirm the profile matches by current role and company. If no profile can be found after these checks, record "LinkedIn not found" (never silently drop it). Also capture the company's LinkedIn page if easy.
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

## Step 6: Publish the decision page

Write the page as HTML in the scratchpad and publish it with the Artifact tool (icon "user" on first publish). Title: `FT Eval: <Guest Name>`. Keep it to the sections below, in this order. Anything else belongs in ft-host-dossier, which runs once the guest is booked.

1. **Verdict banner.** Verdict plus route, for example "STRONG CONSIDER · Editorial Tier 2" or "DECLINE · Sponsored only".
2. **Header.** Name, role and company, with the guest's **LinkedIn profile linked directly under the name** (a visible "LinkedIn" link, not just the name hyperlinked). If no profile was found, show "LinkedIn not found" in muted text there instead. Then a **one-line synthesis**: the arc plus the reason to book or pass. This line is the whole decision for a skimmer. If an engagement already existed, open it with that history ("Pitched in Jan, we declined; now Series B").
3. **Business metrics strip.** A row of labelled figures directly under the header: Revenue/ARR (with year; an exact figure, or the signal-based band with YoY direction), Total funding, Last round (stage, size, date, lead), Valuation, Team size. Swap a cell that would only say "Not disclosed" for a stronger signal when you have one, such as Profitability or Debt (open charges). Show "Not disclosed" in muted text only where nothing turned up, and give each figure its source in small text. Add one line under the strip saying what the numbers mean for the decision. This is the only home for these numbers.
4. **Two scorecards.** Audience Fit and Sales Fit. Each has a big score, a one-line summary and 2 to 3 bullets. Audience Fit names the closest past FT comparables and their views. Sales Fit names the pitch angle if 7+, or says "skip the pitch" if 4 or below.
5. **The business.** This section **teaches** Akshay the business. Write it for a smart generalist who knows nothing about this industry. The test: after reading it, he could explain the business to someone else and ask the guest an informed first question. A paragraph that only gestures ("India is building X from near zero", "a capital-heavy bet") fails the test. No separate blurb above it (the 40 to 50 word blurb goes to Notion only).

   Use these short labelled paragraphs, each 2 to 4 sentences, bold label first:
   - **What it actually is.** The product in plain, physical terms: what it is, what it does, and what it ends up inside or affects. Define jargon in the same sentence it appears ("glass substrate, the ultra-thin sheet that every LCD and OLED panel is built on").
   - **Who pays and how money moves.** The buyer, the pain they pay to remove, roughly what they pay, and how the company earns (per unit, subscription, take rate, project fee). Give margin and capex intensity in a phrase if known.
   - **The industry and who wins it.** Market size (with year), the 2 to 3 leaders and their rough share, and why it's hard to break in. Name 1 to 2 comparables inline, linked to their websites.
   - **Where this company sits.** Its scale versus the leaders, its wedge, and what's changed that gives it a shot. If there are several entities, give each one a sentence and flag which is the cash core and which is the bet.
   - **Is the model relevant?** Start this paragraph with that bolded question. Judge whether the model fits the moment: timing (regulation, budgets, platform shifts), whether the revenue model scales in this industry, and how funded the competition is. End on the bet the business rests on and whether there's evidence for it yet.

   Concrete beats abstract: one number or named example per paragraph where possible, each industry figure with its source and year inline in small text or brackets. Mark anything unverified "(uncertain)".

   **Simple-business exception.** For a business any reader already understands (a D2C brand, a restaurant chain, a staffing firm), collapse the first two paragraphs into one line and keep the rest short. Complex, technical or B2B-infrastructure businesses always get all five.
6. **Career journey.** A replica of the LinkedIn experience section, in chronological order (oldest first), so the depth of experience is visible at a glance. One row per role: the date range and duration on the left; the title and organisation in bold, plus one line on what the role was, on the right. Link every organisation name (employers, universities, the guest's own companies) to its website so Akshay can dig deeper; leave a name unlinked only if no site exists. Education goes in as rows in its place in the sequence. Mark unconfirmed dates "circa". End with a total line, for example "~22 years of work, ~1 as a founder".
7. **Key facts.** 3 to 6 bullets for what the metrics strip and career journey don't carry: marquee signals, named customers, regulatory clearances, recent milestones. Mark anything unverified "(couldn't verify)". Omit the section if nothing is left.
8. **Better guest available?** PR agencies pitch whoever is available, often a hired CEO when the founder owns the better story. Include this section only when all of these hold:
   - There's a named alternative at the same org who would plausibly score higher on Audience Fit.
   - They are still at the org, or still its public face. Never surface exited founders, retired chairmen or purely ceremonial figures.

   Open the box with a visible link to the alternative's LinkedIn profile ("<Name> on LinkedIn"), or "LinkedIn not found" in muted text. Then write 2 to 3 sentences: who they are, what story they own that the pitched guest doesn't, and the bookability reality. Be honest when the upgrade is marginal, and remember that a founder who is a poor speaker isn't automatically the better guest. When the pitched guest is the best option, omit the section entirely, with no placeholder line.
9. **Watch-outs.** Only if there are any. Diligence and interview risks, and any pitch claim that didn't survive checking.
10. **Links.** The guest's LinkedIn profile first (required; repeat it here even though it's in the header, or write "LinkedIn not found"), company site, company LinkedIn page if found, 1 to 3 substantive press links, the booking contact if PR-brokered, and the Notion engagement link (added after Step 8).

### Tightening pass (before publishing)

- **Pre-publish checks.** The header shows a LinkedIn link (or "LinkedIn not found"), and so does the Better guest box if it's on the page. The business section has all five labelled paragraphs for any non-simple business, and every piece of jargon in it is defined. If either fails, fix it before publishing.
- **One home per fact.** Revenue and funding live in the metrics strip, roles and dates in the career journey, the business and its model in The business (said once, not as a blurb plus an explainer), the why-book in the synthesis and scorecards, risks in Watch-outs. Delete second mentions.
- **Cut throat-clearing.** Remove "notably", "it's worth noting" and narration of your own process.
- **Per-sentence test.** Every sentence either states a fact the host lacks or makes a judgment the host needs. If it does neither, cut it. This cuts filler, never the teaching in The business: explaining what the product is and how the industry works counts as facts the host lacks.

### Page styling

The page body only, with no doctype, html, head or body tags (the Artifact tool wraps it). A system sans-serif stack, 800px max width, 16px side gutters on mobile. The scorecards and the metrics strip stack below 640px, and career journey rows stack date-over-role at phone width.

Define colours as tokens on `:root`, and redefine them under `@media (prefers-color-scheme: dark)` guarded by `:root:not([data-theme="light"])`, and again under `:root[data-theme="dark"]`. Give `body` an explicit background.

- Banner: Book immediately `#059669`, Strong consider `#0284c7`, Pre-call needed `#d97706`, Decline `#dc2626`, with white text
- Score colour by tier: 8+ `#059669`, 6 to 7 `#0284c7`, 4 to 5 `#d97706`, 3 or below `#dc2626`
- Better-guest box: left border `#7c3aed`
- Section titles in small uppercase with letter-spacing and a thin bottom border. Cards with an 8px radius and a subtle shadow. No emojis, no icons, no external scripts.

## Step 7: Pre-call re-run

When pre-call notes arrive for an existing "Pre-call needed" engagement:

- Re-score Audience Fit with the call evidence, especially any revenue figures the guest shared.
- Pick a final verdict (Book immediately, Strong consider or Decline) and route.
- Republish the same page URL from the engagement's `Eval link` (read it first), with a short "After the pre-call" line under the synthesis.
- Update the engagement in Step 8: Status `Precall done`, the new Eval verdict, and Next action.

## Step 8: Write to Notion

**Organisation.** Find it by name or domain. If none exists, create it with Name, Website, Domain, Type (Startup, Enterprise or Fund) and Source `Agent`.

**People.** If the guest has no People row, create one with Name, Role, LinkedIn, Organisation, Location, What they do (a short descriptor such as "Fintech, auto loans"), Source `Agent` and Captured (today). On every run, set `Latest eval verdict` (it has no "Evaluate after call" option, so use the closest match). Fill LinkedIn (with the profile URL from Step 2) and What they do only if they're empty. Never touch `Blurb` (founder-thesis-blurb owns it), `FT guest`, or the duplicate fields.

**PR contact.** If the pitch came through an agency, find or create the contact in People (tag `PR contact`) and their agency in Organisations (Type `PR agency`). Link the contact via `Via`.

**Engagement.** Update the existing FT engagement if there is one, otherwise create one.

- Name: `<Guest> @ <Company>, Founder Thesis`
- Show: the FT show page
- Direction: `Inbound`
- Guest, Organisation, Via: relations as above
- Eval verdict: the verdict. Use `Evaluate after call` only if the eval genuinely couldn't be completed without a call.
- Eval link: the published page URL
- Status: `Decision pending` on create. On update, change Status only if the current one is `New`, `Contacted` or `Interested` (or `Precall done` on a pre-call re-run). Never move a record backwards.
- Next action: one line naming the recommended route and step, for example "Offer sponsored feature via SGA" or "Book, Tier 1.5. Ask PR for founder's dates" or "Decline, already a guest (2023)"
- Tags: add `Big name` for Audience Fit 9+, and `Has podcast` if applicable
- Captured: today, on create only
- Source: `Agent`, on create only

**Leave these for Akshay:** Decision, Tier, Heat, Host verdict, Payment, Amount. The recommendation goes in Next action and on the page, not in these fields.

**Page body.** Append a dated block to the engagement page, so the history stacks up across runs:

```
### Eval, <YYYY-MM-DD>
Verdict: <verdict> · Route: <route>
Audience Fit <n>/10 · Sales Fit <n>/10
Revenue: <figure, signal-based band with YoY direction, or Not disclosed> · Funding: <figure or Not disclosed>
<40–50 word company blurb>
Eval page: <url>
```

If Sales Fit is 7 or above, add a line `PaaS angle: <one sentence>`. Do not create a PaaS engagement; Akshay decides that.

If any Notion write fails, finish the eval anyway and name the failed write in the chat reply.

## Chat reply

Exactly this shape, nothing more:

> Verdict: Strong consider · Editorial Tier 2. Audience Fit 7/10, Sales Fit 6/10. Revenue ₹42 Cr (FY25), raised $12M.
> Notion: created engagement (or "updated engagement, was We declined in Jan").

For a past guest:

> Decline. Already a Founder Thesis guest: <episode link>. Notion: logged.

## Voice rules for the page

- First person, blunt, opinionated
- No em-dashes. Use commas, parentheses or two sentences instead.
- Banned: exciting opportunity, great potential, amazing journey, powerhouse, thought leader, game-changing, passionate, world-class, leverage, unlock, robust, seamless
- Concrete numbers ("Series B, $42M led by Sequoia"). If a number is unknown, write "Unknown". Never guess.
- Flag uncertainty explicitly with "(uncertain)" or "(couldn't verify)". Never fabricate.
- Sentence case for section titles in the source text (CSS can uppercase them)