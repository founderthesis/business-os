# Research Layers (Stage 1) — what Claude must return before drafting

Claude runs all five layers itself with `web_search` and `web_fetch`. There is no handoff. Layers 4 and 5 only surface if searched for on purpose, and Layer 1 is the one most often under-delivered.

**Standing rules for every layer:** every figure carries a date and a source with a working URL. Label each number filing-grade (MCA/RoC, DRHP, regulator, exchange), press-grade, or company-reported. Never reconcile two conflicting figures into one.

---

## Layer 1 — The industry (the decode layer)

Target: enough to **write § 01 as prose**, not enough to ask about it. The test is whether Akshay could explain this category to a friend after reading the dossier. Generic category description fails that test.

- **The chain.** What happens between the customer's action and fulfilment, who each participant is, and what the company does and does not own.
- **The money-flow stack.** On a single transaction or contract, every charge, who receives it, and the rate. Search fee schedules, charge sheets, exchange or platform pricing pages, regulator circulars. This is concrete and findable, and it is what makes § 01 land.
- **The real revenue pools.** Where operators in this category actually make money, with numbers. Almost never just the headline line item. Look for analyst or rating-agency estimates of revenue mix (CRISIL, ICRA, broker research), founder blog posts about their own economics, and listed comparables' segment disclosures. Note which pools are growing and which are dying.
- **What changed, in order, with dates.** Regulatory, technological or business-model shifts in the last 18-24 months, each named specifically, with the measured effect on volumes, revenue or participant counts.
- **Market size and structure.** India figures with the most-cited source named, concentration (what share the top players hold), and direction of travel.
- **3-5 named comparables** in the same segment with any public revenue or funding figures, and how their models differ. This becomes the benchmark table.

Useful query shapes: `how <industry> companies make money revenue mix India`, `<industry> charges breakdown per transaction`, `<regulator> circular <year> <industry> impact revenue`, `<industry> revenue contribution <segment> CRISIL OR ICRA`.

## Layer 2 — The company through numbers

Target: a reader should be able to argue about this business after the cheat sheet.

- Revenue for the last 2-3 financial years, with growth rate and source type. Say plainly when the latest FY is not yet filed.
- Profitability, EBITDA or burn, whatever is public.
- Full funding history: every round with year, amount, lead, valuation. **Peak valuation and most recent valuation stated separately with dates.** A peak reported as current is the single most common error.
- Business model mechanics: who pays, pricing, revenue mix, gross-margin structure if reported.
- The operating metrics that matter in this category, in absolute terms as well as growth multiples.
- Headcount now vs two years ago. These conflict often; label the source and flag rather than pick.
- Watch India-entity vs consolidated on Indian filings. TheKredible frequently reports standalone. Where a company runs two entities, get both and note which holds the licence.

## Layer 3 — The founder

- Career arc in brief: prior ventures with dated outcomes (exit value, shutdown, pivot). Note plainly if this is a first venture.
- 3-5 short verbatim quotes from recent interviews or posts that reveal thesis, assumptions or contrarian beliefs, each with a URL. These anchor the Act IV themes, and a dossier without them produces generic questions.
- Their own technical or product posts, which are often the best material for the mechanics act and show what they enjoy talking about.
- Claims they make about themselves or the company (rankings, "first in India", angel portfolio, growth rates), and whether an independent source confirms them. Unconfirmed goes to fact flags, never into the snapshot as fact.

## Layer 4 — Discrepancies and tensions

Search for these on purpose.

- Wherever two sources disagree on a number, carry **both** with both sources and dates.
- Figures still circulating that appear stale, especially a peak valuation reported as current.
- Numbers that measure different things being used interchangeably (downloads vs accounts vs active users).
- Anything the founder has publicly dodged, walked back or been visibly challenged on.
- Dated sensitivities: layoffs, down rounds, co-founder exits, regulatory trouble, failed pivots.
- **The low point for Act II.** If nothing negative is on the record, look for the silence: a long stretch with no coverage, no revenue, no announcements. Name the window and its length. A gap in the record is a finding, not a dead end.
- The single strongest bear case an informed skeptic would make, grounded in Layer 1 and 2 numbers. This is the raw material for the spine, and it should be phrased as a puzzle rather than a charge.

## Layer 5 — The archive (past appearances)

Feeds § 07 and prevents Akshay repeating a conversation that already exists.

- **Every prior podcast, long-form interview, conference session and founder-led product session, each with a working URL.** Run the search properly; one query is not enough. Try `<Name> podcast`, `<Name> interview`, `<Name> fireside OR keynote`, `<Company> founder YouTube`, and check the investor's content hub, since portfolio podcasts are common and rarely indexed well.
- For each: date, host, and what it actually covered. Flag ANI-wire-syndicated appearances and investor-hosted episodes, since those rooms are friendly and cover little.
- **Check the master guest spreadsheet** for a prior Founder Thesis appearance and state the result either way.
- Then form **the read**: how the guest interviews, and specifically **what nobody has asked them yet**. That gap is the argument for recording, and it usually points straight at Act II or Act IV.

---

## Coverage check before drafting

- [ ] Layer 1: the money-flow stack is concrete enough to tabulate; real revenue pools have numbers; dated shifts are named specifically; 3-5 comparables with figures
- [ ] Layer 1: you could write § 01 as prose right now without asking the guest anything
- [ ] Layer 2: 2-3 years of revenue, peak AND current valuation dated separately, source type on every number
- [ ] Layer 3: 3+ verbatim founder quotes with URLs, prior ventures dated, self-reported claims separated from verified
- [ ] Layer 4: at least one live discrepancy, one dated sensitivity or named silent window, and a bear case in one sentence
- [ ] Layer 5: every past appearance has a working URL; master sheet checked; the read written
- [ ] Any figure that failed two honest search attempts is marked unknown, not estimated
