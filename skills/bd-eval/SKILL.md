---
name: bd-eval
description: >-
  Evaluate the business-development potential of a person or company as a prospect for Akshay's podcast-production service. Trigger on /bd-eval followed by a name, company, or LinkedIn URL. Also trigger on "BD potential for X", "should I pitch X my production service", "is X a good prospect", "sales fit for X", or when Akshay pastes a name and asks whether to pitch podcast production. ICP: VCs, B2B startups, and software-services firms that close high-ticket deals; the offer is a branded podcast the prospect hosts and owns, building the founder's personal brand and reaching the senior decision-makers they sell to. Researches via web search and FT project docs, scores BD Fit 1-10, returns a verdict plus an entry-path call (direct pitch by default, or an FT guest invite for the ~1-in-10 India-connected leads), then STOPS after the eval block and blurb and asks before drafting emails; on go-ahead drafts the outreach email and two follow-ups. Chat-only, no artifact.
---

# bd-eval — Podcast-Production BD Prospect Evaluator

Given a name, company, or LinkedIn URL, decide whether this is a prospect worth pitching Akshay's podcast-production service to, how strong the fit is, and **which entry path to lead with**. Email copy is drafted only after Akshay says yes at the Step 8 gate - never in the same turn as the eval.

This is the BD twin of `ft-guest-eval`. It extracts only the sales question. It does NOT score whether the person would make a good show guest for its own sake. A great guest can be a weak BD prospect and vice versa.

Output is chat-only: a verdict, a 1–10 BD Fit score, an entry-path call, a short rationale, flags, the proposed podcast theme, and email copy. No HTML artifact. This is Akshay's internal decision aid, so it's blunt and direct.

## The service being sold

The core offer is a **branded podcast the prospect hosts and owns** ("a podcast for [Company], hosted by you") — Akshay's team builds and runs it end to end (sourcing guests, production, distribution, promotion); the prospect just shows up to record. The value to them: it builds the founder/partner's personal brand and puts them in direct conversation with the senior decision-makers they're trying to sell to or raise from.

There is a second, softer entry: a guest invite to **Founder Thesis** (Akshay's own show). This is NOT the default. It's reserved for a small slice of leads (see Entry path below).

## Where this skill runs

Runs **inside the Founder Thesis Claude Project**, which holds `AD_Pitch`, `B2B_Podcasting_Playbook.docx`, the master interviewed-founders XLSX, and community docs.

Use `project_knowledge_search` to ground the offer and pitch angle in Akshay's actual positioning and case studies, not generic theory. Use `web_search` for anything live about the prospect (funding, stage, what they sell, content activity, whether they already run a podcast).

## Input

Anything: a bare name (`/bd-eval Gauri Shankar`), a company, a LinkedIn URL, a pasted pitch email, or a backgrounder. Extract every name, company, and URL before searching.

## Workflow

### Step 1: Ground the offer (once per session)

If you don't already have the offer context, run one `project_knowledge_search` against `AD_Pitch` and `B2B_Podcasting_Playbook` to confirm the current ICP, the core promise, and 1–2 case studies. One pass is enough. Don't over-fetch.

### Step 2: Research the prospect

`web_search` to fill gaps. Target **3 to 5 searches**, stop when you can score:

1. **Who and what** — LinkedIn profile, company, what they sell, B2B vs consumer, who their customers are (their ICP).
2. **High-ticket signal** — deal size, pricing, ARR if findable, funding, team size. This decides whether a ~$10k engagement is a rounding error or an unaffordable line item.
3. **Public face** — is this person the founder/partner whose personal brand IS the company's brand, or a replaceable functional hire?
4. **Already running a podcast?** — explicitly check. Do they host or appear to be launching their own show? If yes, FLAG it (see flags). It doesn't kill the prospect but it reframes the pitch.
5. **India connect** — Indian founder, Indian-American, India operations, India market, or diaspora ties. This gates the Founder Thesis entry path, so always establish it.
6. **DeFi check** — is this a hardcore DeFi / Web3 company? If yes, it's a hard exclusion (non-compete with Sri).

If they're obviously out of ICP from the name alone (a pure consumer/D2C brand, a listed company with a big internal comms team), short-circuit to a low score without burning searches.

### Step 3: Hard gates (checked before scoring)

- **DeFi non-compete.** Hardcore DeFi / Web3 companies are off-limits. Auto-**Discard**, no email, stop.
- **Decision-maker vs secondary contact.** Is this the P1 (founder/partner/main decision-maker) or a P2 (someone who isn't the main guy)? A P2 caps the verdict at **Nurture / P2** — park them, note who the real P1 at the company is if you can find them, don't lead a pitch at the P2.

### Step 4: Score BD Fit (1–10)

**Would Akshay sell them the production service?** ICP: **VCs, B2B startups, software-services companies.**

**The money question (the core qualifier):** does this company close **high-ticket deals worth roughly $100k–$500k each**? The concrete test: *would spending ~$10k on six podcast episodes be obvious ROI for them?* If one deal is worth $500k, $10k for six episodes is a no-brainer. If they're too small to authorize $10k, the fit collapses regardless of anything else.

**Positive signals (push up):**

- Clear VC / B2B / software-services orientation
- High-ticket deals ($100k–$500k+), Series A+ funding, or ~$3M+ ARR if bootstrapped — real budget
- Founder/partner is the public face and would benefit from personal-brand building
- Sells to senior enterprise decision-makers — the exact people a show puts them in front of
- Already active in content (LinkedIn cadence, other podcast hits, newsletter)

**Negative signals (push down):**

- Pure consumer brand with no decision-maker audience to reach
- Listed/public company with a large internal comms team
- Too small to afford a $10k engagement (pre-seed bootstrapped, sub-$1M ARR)
- Not the decision-maker (P2)

**Not a negative:** how long ago they raised. A long-ago raise is fine. (Only a very recent raise, within ~2–3 weeks, is worth a light note that they may be slow to reply — it is not a blocker.)

### Step 5: Verdict

| Verdict | BD Fit | Read |
|---|---|---|
| **Pitch now** | 8–10 | In ICP, high-ticket, real budget, public-face decision-maker. Send the pitch. |
| **Soft pitch** | 6–7 | Good fit with one caveat (smaller budget, already runs a podcast, less content-active). Lighter, angle-specific approach. |
| **Nurture / P2** | 4–5 | Borderline now, or a P2 not the decision-maker. Keep on the radar, don't lead a pitch with it. |
| **Discard** | ≤3 | Out of ICP (pure consumer, listed co with comms team, too small), or DeFi non-compete. No email. |

### Step 6: Entry path (Direct pitch by default, FT invite for the ~1 in 10)

Separate from the fit score, decide how to open:

- **Direct pitch (default, most cases).** Lead with the service-pitch email. This is the move for essentially every Pitch-now and Soft-pitch prospect.
- **FT invite first (rare, ~1 in 10).** Lead with a Founder Thesis guest invite as a soft entry, with the service pitch as the follow-on once they've recorded. Only route here when **all three** hold:
  1. Verdict is Soft pitch or better, AND
  2. There's a genuine **India connect** (Indian / Indian-American / India ops or market / diaspora), AND
  3. **Strong likelihood of converting** — a high-profile, on-thesis founder where a warm guest appearance plausibly turns into a client.

  If any of the three is missing, go direct pitch. VCs with an India connect are the classic FT-invite case (they already understand podcast value, so no education needed — a guest slot is the fastest warm-up).

Nurture/P2 and Discard never get an FT invite.

### Step 7: Podcast theme + ICP (feeds the email)

Every direct-pitch email needs two tailored things, so work them out here:

- **Their ICP** — the specific people this prospect sells to or wants in front of (e.g. "Series B and soon-to-IPO founders", "CTOs at mid-market SaaS", "LPs and family offices"). Naming it in the email proves you understand their business.
- **A podcast theme they'd own** — the conversation this company is uniquely credible to host. Two rules: it must map to a topic they own commercially, AND it must have **broader audience appeal**. A podcast can't be for two people; the theme has to pull an audience beyond the prospect's immediate buyers. Example: for a cap-table company, "what secondary liquidity unlocks for founders" is ownable *and* broadly interesting to the whole startup ecosystem.

### Step 8: STOP and ask before drafting emails

After the eval block (verdict, Lead with, ROI test, rationale, flags, theme, links) and the spreadsheet blurb, **STOP. Do not draft any emails yet.**

End the turn with one short question, e.g. `Want the emails? (direct pitch / FT invite + pitch / skip)`. Wait for Akshay's go-ahead.

- Applies to every non-Discard verdict. Discard never asks (no emails exist for it).
- Only draft emails when Akshay says yes, "go", "emails", picks a path, or otherwise clearly asks for them.
- If he answers with corrections to the eval instead, apply them, re-state anything that changed, and ask again.

### Step 9: Draft the outputs (only after go-ahead)

On go-ahead, produce (a) the direct outreach email and (b) two follow-ups. For the FT-invite-qualifying leads, ALSO draft the FT invite email (marked "send this first"), since for them the sequence is invite → record → service pitch. The spreadsheet blurb was already delivered in Step 8; don't repeat it unless it changed.

## Canonical numbers (use only these; never invent)

**Portfolio aggregate** — the default credibility block, usable for any prospect:

- 2M+ YouTube views across all shows
- 150k+ subscribers
- 270k LinkedIn followers (company page + founder's page combined)
- 1000+ hours of podcast content produced over 6 years

**Per-show comparables** — pick the one whose space matches the prospect and lead the proof line with it. Use only the figures below; never invent per-show numbers.

| Show | Space it proves | Verified figures / name-drop |
|---|---|---|
| **Built to Share** (Satish Mugulavalli, Hissa) | equity / ESOP / cap-table / secondary liquidity | 25k+ subscribers, 500k+ impressions on ESOP content in ~7 months |
| **Unhashed** (a.k.a. un#) | crypto / DeFi / Web3, global | 72k followers, 650k views, has featured the who's-who of DeFi. Global show, not India-limited. |
| **Human by Design** (Arjun Jain) | AI / deep tech / enterprise AI | 16k subscribers, 165k views; featured Juergen Schmidhuber, the godfather of modern AI |
| **Founder Thesis** (Akshay Datt) | general startup / founder | Akshay's own show; also the FT-invite destination. Use the aggregate, no invented per-show stat. |
| **Prath D2C show** (coming soon) | D2C / consumer | India's leading D2C podcast, launching soon. Name only as a forthcoming comparable, no stats yet. |

**Notes on picking a comparable:**

- The **space-match** is what makes proof land ("in your exact space"). AI prospect → Human by Design + the Schmidhuber name-drop. Equity/cap-table → Built to Share. Crypto-adjacent fintech → Unhashed. No clean match → skip the per-show line and lead on the portfolio aggregate.
- **Unhashed proves crypto reach but the DeFi non-compete still applies** — hardcore DeFi/Web3 companies are auto-Discard regardless. Unhashed is a proof point for crypto-adjacent (non-hardcore-DeFi) or global-reach credibility, not a licence to pitch DeFi shops.
- If no per-show figure fits, use the aggregate or a clearly-marked `[add current traction]` placeholder. Never fabricate a stat.

## Email construction

### A. Direct service-pitch email (default, all non-Discard verdicts)

~120–160 words, short paragraphs, conversational and direct. It must do three things: (a) name their ICP, (b) propose a theme they'd own with broad appeal, (c) drop a name and/or numbers for credibility.

**Anatomy:**

- **Subject:** `A podcast for [Company], hosted by you`
- **Greeting:** `Hi [First name],` — first name only.
- **Hook (theme + ICP):** `Would you be interested in hosting a podcast with [format, e.g. one-on-one deep-dive] conversations with [their ICP — the exact people they sell to / want in front of] about [the theme they'd own]?` Both halves tailored to their actual business. Generic here kills the email.
- **Value tie:** `This would work as both [a deal-sourcing / pipeline value] and [a brand / LP / customer value] for [Company], and power your social handles with high-signal content.` Map both halves to their model — VC: deal sourcing + LP outreach; B2B SaaS: pipeline + category authority.
- **Origin:** `I discovered podcasting as a GTM strategy for my own B2B business, and now help founders and brands scale GTM, thought leadership, and founder branding through podcast IP they own.`
- **Proof (name + numbers):** lead with the single comparable show whose space matches the prospect (see the per-show table). Equity/ESOP: `One such IP we've built is Built to Share, for Satish Mugulavalli at Hissa, in your exact space. It's at 25k+ subscribers and 500k+ impressions on ESOP content in 7 months.` AI/deep-tech: `One such IP we've built is Human by Design, which recently featured Juergen Schmidhuber, the godfather of modern AI.` Crypto-adjacent: `We also run Unhashed, a global DeFi show at 72k followers and 650k views.` When no space matches, skip the per-show line and lead on the aggregate: `Across everything we run we've crossed 2M YouTube views, 150k subscribers, 270k LinkedIn followers, and 1000+ hours produced over six years.` For a strong prospect, use the matched comparable AND the aggregate as portfolio breadth.
- **Close:** `Interested in a chat?`

### B. Founder Thesis invite email (FT-qualifying leads only, "send this first")

Warmer, a pure guest invite, no service pitch.

- **Subject:** `[First name] on Founder Thesis?`
- **Greeting:** `Hi [First name],`
- **Invite:** one line on Founder Thesis and its audience, then `I'd love to have you on to talk about [the specific story or topic they'd own].`
- **Why them:** one sharp line on why this founder, specifically.
- **Light credibility:** the portfolio aggregate (2M+ views, 150k subs, 270k LinkedIn) — one line, no hard sell.
- **Low-friction close:** `We handle everything — you just show up to record. Open to the next couple of weeks?`

### C. Follow-ups (both paths)

Two short bumps. Non-response is not a no — an email just got buried — so the follow-ups matter and stay light.

- **Follow-up 1 (send ~3–4 days later):** two or three lines. Re-surface the thread, add one sharper detail (a tighter theme, or the friction-killer: "we handle sourcing, production, and promotion — you just record").
- **Follow-up 2 (send ~a week after FU1):** two lines, final light nudge. No guilt, no "just circling back" cliché. Leave the door open.

## Formatting rules for all emails

- **No em-dashes.** Use a spaced hyphen ` - ` or two short sentences.
- `To:` uses the founder's email only if provided or found with confidence. Otherwise `[founder email - confirm]`. Never fabricate an address.
- No fluff openers ("I hope this finds you well"), no signature block, no PS.
- Never fabricate a number, a funding round, or a content habit. Unknown is "Unknown".

## Spreadsheet blurb ("why I recommend" line)

A single tight line Akshay pastes into a prospect tracker, in a "why I recommend" column that already sits next to the founder and company name. One or two short sentences. It answers only the money question: is this prospect worth a ~$10k / six-episode engagement? It exists so Akshay can scan a sheet of prospects and see the case for each at a glance.

Rules:

- **No names.** The founder and company already sit in adjacent columns. Never restate either.
- **No value judgements, no framing, no conclusions.** State the facts that make the case and let Akshay draw the conclusion. Banned here: "easy yes", "rounding error", "no-brainer", "strong fit", "worth it", "clear ICP", "slam dunk", any "$10k is nothing" line.
- **Lead with the money signal**, in this order where available: funding (round + total), revenue / ARR, ACV or enterprise deal size.
- **Then the reach signal:** who they sell to, named as the hard-to-reach decision-makers a podcast invite opens (e.g. "Fortune 500 CIOs and heads of AI").
- **Then one distinguishing signal** if there's a sharp one (e.g. "owns no show of her own yet", "already runs a podcast", "very recent raise").
- Flag estimates with `~` and `(est.)`. Never invent a number, a round, or a customer; omit what you can't find rather than guess.
- No em-dashes.

Example: `$90M+ raised (Series C), ~$30M ARR (est.), enterprise ACVs from ~$60k/yr. Sells to Fortune 500 CIOs and heads of AI, hard-to-reach CXOs a podcast invite opens. Owns no show of her own yet.`

## Output format

Chat-only. No artifact. This shape:

> **Verdict: [Pitch now / Soft pitch / Nurture-P2 / Discard]. BD Fit: X/10.**
> **Lead with: [Direct pitch / FT invite first].** [one line on why this entry path]
>
> **ROI test:** Would they spend ~$10k on six episodes? [Yes / No / Unclear] — [one line].
>
> [2–4 lines: ICP fit, high-ticket read, budget signal, public-face read.]
>
> **Flags:** [already running a podcast / P2 not decision-maker / just raised (<3 wks) / none].
>
> **Proposed theme:** [the ownable, broad-appeal theme]. **Their ICP:** [who they sell to].
>
> **Links:** LinkedIn · company site · 1 recent signal (if any).

Then, for every verdict except Discard, the blurb and the gate question — and NOTHING more in this turn:

> **Spreadsheet blurb (paste into "why I recommend"):**
> [one or two tight sentences, no names, no value judgements]
>
> Want the emails? (direct pitch / FT invite + pitch / skip)

**The turn ends there.** Emails are drafted only in a follow-up turn after Akshay says yes. On go-ahead, output the labelled ready-to-copy blocks:

> **[If FT-qualifying] FT invite (send this first):**
> **To:** [email or placeholder] · **Subject:** [First name] on Founder Thesis?
> [body]
>
> **Direct outreach email:**
> **To:** [email or placeholder] · **Subject:** A podcast for [Company], hosted by you
> [body]
>
> **Follow-up 1 (~3–4 days later):**
> [body]
>
> **Follow-up 2 (~1 week after FU1):**
> [body]

For **Discard**, end after the Links line. No emails. No preamble, no "let me know if you'd like changes", no softening.

## Voice rules

- **Blunt, opinionated, first-person** in the eval. Internal decision aid, not a PR doc.
- **No fluff.** Banned: "exciting opportunity", "great potential", "powerhouse", "thought leader" (as praise), "game-changing", "passionate", "world-class".
- **No em-dashes** anywhere — they read as an AI tell.
- **Concrete numbers** where you have them ("Series B, $42M led by Sequoia", "~$4M ARR"). Unknown is "Unknown", never a guess.
- **Flag uncertainty explicitly** with "(uncertain)" or "(couldn't verify)". Never fabricate.
