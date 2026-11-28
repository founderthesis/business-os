---
name: ft-g-mail
description: "Draft the Founder Thesis cold guest-invite email plus its four follow-ups for a specific guest, in Akshay's locked template wording, tailored to the guest and their company. Trigger whenever Akshay gives a founder name and a company name with intent to invite them onto Founder Thesis, e.g. \"FT G Mail\", \"/ftgmail\", \"FT invite for [name] at [company]\", \"draft the guest invite for [name]\", \"cold email [founder] for the podcast\", or just pastes a founder name + company in a Founder Thesis outreach context. Also fires on \"tailor the FT invite for X\", \"write the guest emails for Y\". Researches latest revenue and LinkedIn, judges the FT-first / India-connection fit, then outputs a compact workup and the full five-email sequence with the exact house wording, no em dashes, a horizontal rule between the initial email and the follow-ups, and wait-days on every follow-up."
---

# FT G Mail

Turn a founder name + company name into a ready-to-send Founder Thesis cold guest-invite
sequence: the initial email plus four follow-ups, in the locked house wording, with only two
lines tailored per guest.

This skill is for GUEST invitations to the Founder Thesis podcast. It is not the BD service
pitch (that is `bd-eval` / `pitch-builder`).

---

## Inputs

- **Founder name** (required)
- **Company name** (required)

If only one is given, ask for the other in one line, then proceed.

---

## Step 1 - Research (fast, verified only)

Run web_search to establish three things. Do not invent, approximate, or round up any number.

1. **Latest revenue.** Find the clearest figure (self-reported ARR beats aggregator estimates).
   Note the year and source. If sources conflict or only soft estimates exist, say so plainly
   and label it an estimate. Never put a revenue number inside the emails - it is for Akshay's
   context only.
2. **LinkedIn URLs** for the guest and the company. Only give a URL you actually found. If the
   company page URL is uncertain, give the likely handle and flag "confirm before use."
3. **India connection.** Determine whether the guest is genuinely India-connected (India-based,
   Indian ecosystem, Indian-VC backed) or only India-origin (e.g. IIT alum who built entirely
   abroad). This drives the note in Step 3, not the email wording.

House rules (always): verified figures only; guests are never called clients; no em dashes
anywhere in the output.

---

## Step 2 - Compact workup

Before the emails, output this short block (keep it tight):

- **[Company], in 2 lines** - what they do, plainly. Never recite this back to the guest inside
  the email; it is context for Akshay.
- **Latest revenue** - the figure, year, source, and a flag if it is soft. State it is kept out
  of the email.
- **LinkedIn** - guest URL and company URL (flag the company one if unconfirmed).
- **FT-first / India note** - one short paragraph. If the guest is genuinely India-connected,
  say the template's Indian-ecosystem marquee line lands cleanly. If they are only India-origin
  (US/other-based), flag that the marquee line is the weak point and offer the reframe from the
  Notes section. If the service angle is worth a line (strong B2B-SaaS service ICP vs.
  already-huge personal brand), add it in one sentence.

---

## Step 3 - The email sequence

Output the five emails exactly as templated below. Only the two **[TAILORED]** lines change per
guest. Everything else is fixed wording - do not paraphrase it.

Formatting rules for this block:
- No em dashes. Use a spaced hyphen ( - ) or a comma. The template already uses spaced hyphens;
  keep them.
- Put a single horizontal rule (`---`) after the INITIAL email and all followup mails (horizontal line between all followup mails).
- Label every follow-up with its wait time on the same line as its heading, e.g.
  **FOLLOWUP 1** *(send 3 days after the initial)*.
- Use the guest's first name in the greeting. Use the company name in the last-nudge line.

### Wait-day cadence (fixed)

- INITIAL - Day 0
- FOLLOWUP 1 - 3 days after the initial
- FOLLOWUP 2 - 5 days after Follow-up 1
- FOLLOWUP 3 - 7 days after Follow-up 2
- FOLLOWUP 4 - 7 days after Follow-up 3

### Template (reproduce verbatim except the two [TAILORED] lines)

INITIAL
Sub: We want to interview you! (Founder Thesis podcast)

Hi [First name],

[TAILORED HOOK] - Hook rules: two lines max, no exaggeration/flattery/hype, never restate what a busy founder already knows, plain and genuine. It must never state anything the guest already knows about. keep in mind that they dont have time to ready long hooked mails
Then a short bridge like "That's exactly
the kind of story our audience wants to hear."

You'll be in good company on the Founder Thesis podcast (500+ episodes published since 2020).

We've built a serious audience of startup enthusiasts (280k followers on LinkedIn, 1mn+ views on
our YouTube channel) and have interviewed the who's who of the Indian startup ecosystem (Sanjeev
Bhikchandani, Manish Sabharwal, Amit Jain and many more incredible founders).

It's a 2-hour conversation, completely unscripted, recorded remotely.

Interested?

---

FOLLOWUP 1 *(send 3 days after the initial)*

Hi [First name],

Just bumping this up in case you missed it… feel free to loop in someone from your team whom I can
coordinate with for this!

FOLLOWUP 2 *(send 5 days after Follow-up 1)*

Hi [First name],

We just released an episode featuring Manish Sabharwal who built Team Lease into a Rs. 24bn listed
company over 2 decades - you might enjoy that episode: podm.in/manish

We continue to remain keen to feature you on the podcast - let me know how we can make that happen!

FOLLOWUP 3 *(send 7 days after Follow-up 2)*

Hi [First name],

I regret to inform you that we just crossed 1.5 mn views on our YouTube channel - and we’ve still not featured your story😭
Let’s fix this?

keep these exact words

FOLLOWUP 4 *(send 7 days after Follow-up 3)*

Hi [First name],

Last nudge from me. No worries at all if the timing's off right now, the invite stays open whenever
it suits you.

Would genuinely love to have the [Company] story on the show whenever you're ready.

---

## Step 4 - Notes (only real flags)

After the emails, add a short Notes list only where there is a genuine call to make. Do not pad it.
Common ones:

1. **India framing reframe** - if the guest is only India-origin, offer this alternative marquee
   line (use only if true, and prefer naming a real AI / deep-tech / global founder from the FT
   roster if one exists - never invent a name):
   *"…and have interviewed 500+ founders across the startup world, from Sanjeev Bhikchandani to a
   deep bench of AI and deep-tech builders."*
2. **Follow-up 2 episode swap** - the Manish Sabharwal episode is a staffing-industry drop. If the
   guest is in a very different domain, tell Akshay it is a mild mismatch and offer to swap the link
   for a more relevant published FT episode if he has one. Keep the real link (podm.in/manish) as the
   default; never invent an episode or link.
3. **Views-number consistency** - the initial says "1mn+" and Follow-up 3 says "1.5mn". That growth
   is the intended running gag and only works if the emails go out days apart. If they will go out
   close together, flag that Akshay should make them match.
4. **Service angle** - one line only, if useful: whether this is a strong production-service prospect
   for later (dead-center B2B-SaaS ICP) or a weaker service fit (founder already has a huge personal
   brand), and that FT-first earns the relationship first either way.

---

## What good output looks like (worked example: Vijay Chittoor, Blueshift)

Hook line used: "Big fan of what you've built at Blueshift - you were doing serious AI in marketing
years before it became the thing every company claims to do."

Views-gag line used: "Mildly embarrassing update: we just crossed 1.5 mn views on YouTube doing none
of the audience personalization you've spent a decade perfecting - and we still haven't got you on the
show."

That is the bar: the two tailored lines feel written by a person who actually knows the guest's work,
and every fixed line matches the template exactly.

---

## Hard rules recap

- No em dashes anywhere.
- One horizontal rule, placed after the initial email, before the follow-ups.
- Every follow-up carries its wait-days.
- Only the hook line and the views-gag line are tailored; all other wording is verbatim template.
- Never state anything the guest already knows about themselves or their company.
- Verified figures only. No invented numbers, no invented guest names, no invented episode links.
- Guests are never called clients.