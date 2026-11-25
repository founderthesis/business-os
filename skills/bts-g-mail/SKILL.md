---
name: bts-g-mail
description: "Draft the full Built to Share guest-invite outreach: a LinkedIn message set (connection note plus InMail/DM) AND the cold-invite email, each with four follow-ups, in locked house wording, tailored to the guest. Built to Share is hosted by Satish Mugulavalli (Founder, Hissa Fund), about the people decisions that make or break startups: building teams, leadership, and how founders share ownership. Trigger whenever a founder name, company, or LinkedIn URL is supplied with intent to invite them onto Built to Share, e.g. 'BTS G Mail', '/btsgmail', 'BTS invite for [name]', 'cold email [founder] for Satish podcast', 'LinkedIn message for [founder]', or a pasted founder name in a B2S outreach context. Researches the guest team/leadership/ownership story, judges BTS fit, then outputs a compact workup, the LinkedIn messages, and the email sequence in house wording, no em dashes, wait-days on follow-ups. The INVITE sequence, not the prep pack (bts-host-dossier)."
---

# BTS G Mail

Turn a founder name into a ready-to-send Built to Share cold guest-invite pack. **Both channels
ship by default:** a LinkedIn message set (connection note plus InMail/DM) and the email sequence
(initial plus four follow-ups), in the locked house wording, with only one tailored angle line (and
a couple of name slots) changing per guest. The initial is deliberately short, because founders have
no time to read a long invite.

LinkedIn is the primary outreach channel for BTS, so it leads the output. Email follows. Do not
make Akshay ask for the second channel; give him both unless he names one.

This skill is for GUEST invitations to Built to Share, the podcast hosted by **Satish
Mugulavalli** (Founder and Managing Partner, Hissa Fund). The show is about the people decisions
that make or break startups: building teams, leadership, and how founders share ownership. It is
not the host prep pack (that is `bts-host-dossier`) and not the BD service pitch (`bd-eval` /
`pitch-builder`).

---

## Inputs

- **Founder name** (required). A LinkedIn URL alone also works; the name comes off the profile.
- **Company name** (optional). If not given, establish it in Step 1 research rather than asking.

Only ask a question back if the founder is genuinely ambiguous (two well-known people share the
name). Otherwise research and proceed.

### Channel selection

Default output is **both channels**: LinkedIn messages first, then the email sequence. Narrow only
if Akshay explicitly names one, e.g. "just the LinkedIn message" or "email only".

### Current-role check (mandatory)

Founder titles go stale, and a stale title makes the outreach read as lazy. Confirm in Step 1 what
the founder is doing **now**, not what their LinkedIn headline or Akshay's input line says. If they
have exited, stepped back, or moved to a new vehicle, name the old company as the story and the new
one as the present, and flag the staleness in Notes. Never assert a present-tense role you have not
verified.

---

## Step 1 - Research (fast, verified only)

Run web_search to establish these. Do not invent, approximate, or round up any number, name, or
link.

1. **The team / leadership / ownership story.** Find the one concrete thing this founder did in
   *building or rewarding a team* that fits the show: scaling headcount, an unusual hiring or culture
   call, a leadership philosophy, distribution or ops built on people not just product, an ESOP /
   buyback / employee-wealth move. You need this to understand the guest and pick the sharpest angle,
   but it does NOT go into the email as a recap. The founder lived it and already knows it. Use it to
   choose the one angle line you would explore with them (same discipline as Satish's own posts -
   ownership surfaces as the answer, never the headline, and never restate what the guest already
   knows).
2. **Company in 2 lines + a scale marker.** What they do, plainly, plus one relevant scale number
   for a *talent* show (headcount, funding stage, offices, users) with year and source. Flag if
   soft. Never recite this back to the guest inside the email; it is context for Satish and the
   Built to Share team.
3. **LinkedIn URLs** for the guest and the company. LinkedIn is the primary outreach channel for
   BTS, so these matter. Only give a URL you actually found. If the company page URL is uncertain,
   give the likely handle and flag "confirm before use."

House rules (always): verified figures, names, and links only; guests are never called clients; no
em dashes anywhere in the output.

---

## Step 2 - Compact workup

Before the emails, output this short block (keep it tight):

- **[Company], in 2 lines** - what they do, plainly. Context for Satish and the team, never recited
  to the guest.
- **Scale marker** - the headcount / funding / users figure, year, source, and a flag if it is soft.
- **LinkedIn** - guest URL and company URL (flag the company one if unconfirmed).
- **BTS-fit note** - one short paragraph. Name the angle line you will use and say whether the
  team / leadership / ownership story is strong (clear org-building narrative) or thin (mostly
  product / tech with no people story). If it is thin, say so and offer the best angle you can rather
  than forcing an ownership line that is not there. If the guest is a direct cap-table / equity-admin
  competitor of Hissa (Carta, Ledgy, Pulley, AngelList, Qapita), flag it here before drafting.

---

## Step 3 - The LinkedIn messages (ships first)

LinkedIn is the primary BTS channel, so output this block before the emails. Same angle, same house
wording, adapted to how LinkedIn actually reads.

### The three adaptations from email

1. **Greeting collapses into the block.** LinkedIn reads as chat, not letterhead. No standalone
   "Hi [First name]," line hanging above white space in the short messages.
2. **Follow-ups compress to a single paragraph each.** Same words, same order, one block.
3. **The connection note is a stripped rewrite,** not a truncation of the DM. It has to survive a
   300-character cap and still carry the show, the host, the format, and the ask.

### Hard character limits (measure, do not eyeball)

| Surface | Limit | Note |
|---|---|---|
| Connection request note | 300 | 200 on some free accounts. Flag if the sending seat is not Premium. |
| InMail subject | 200 | The house subject line fits easily. |
| InMail / DM body | 1900 | Ample. Do not use the room as an excuse to pad. |
| Message to an existing connection | ~8000 | Still send the short version. |

Run a real character count on the connection note before output. Do not estimate. If it is over,
cut words, never the ask.

### Template

CONNECTION REQUEST NOTE *(use if not already connected, keep under 300 characters INCLUDING the signoff)*

Hi [First name], I'd love to have you on Built to Share, a podcast hosted by Satish Mugulavalli (founder, Hissa Fund) on winning the war for talent. Past guests include unicorn and listed company founders. 60 mins, unscripted, remote. Happy to share details via mail. Open to it? Regards, Akshay Datt

---

INMAIL / DM
Sub: We want to interview you! (Built to Share podcast)

Hi [First name],

I'd love to have you on Built to Share, a show about how founders build teams and share ownership with the people who build alongside them.

It's hosted by Satish Mugulavalli (founder, Hissa Fund). [TAILORED ANGLE]

60-minute unscripted conversation, recorded remotely in a 90-minute slot. 230k+ community, past guests include founders of CarDekho, Cashify, and Fibe. More at built2share.in/note

Open to it?

Regards,
Akshay Datt

---

LINKEDIN FOLLOWUP 1 *(send 3 days after the DM)*

Hi [First name], just bumping this up in case it got buried. Here's our guest note with everything about the show and what the conversation looks like: built2share.in/note. If it's easier, I'm happy to coordinate with someone on your team to find a slot. Regards, Akshay Datt

---

LINKEDIN FOLLOWUP 2 *(send 5 days after Follow-up 1)*

Hi [First name],

We recently published our conversation with [MATCHED GUEST], who [personalised one-liner]. You might enjoy how they think about it: [VERIFIED EPISODE LINK]

We'd still love to have your story on the show. Let me know how we can make that happen.

Regards,
Akshay Datt

---

LINKEDIN FOLLOWUP 3 *(send 7 days after Follow-up 2)*

Hi [First name], confession: we keep publishing founders on how they build and reward their teams, and I still haven't managed to get the [Company] story on the show. It's starting to feel personal. Let's fix it? Regards, Akshay Datt

---

LINKEDIN FOLLOWUP 4 *(send 7 days after Follow-up 3)*

Hi [First name], last nudge from me. No worries at all if the timing's off, the invite stays open whenever it suits you. Would genuinely love to have the [Company] story on Built to Share whenever you're ready. Regards, Akshay Datt

The same Follow-up 2 roster rule applies here as in email: pick from `references/published-episodes.md`,
never invent, verify the link. Use the same matched episode across both channels for a given guest.

---

## Step 4 - The email sequence

Output the five emails exactly as templated below. Only the **[TAILORED ANGLE]** line and the
name / company / link slots change per guest. Everything else is fixed house wording - do not
paraphrase it. The initial email is deliberately short: a busy founder scans it in seconds, so
never pad it back out.

Formatting rules for this block:
- No em dashes. Use a spaced hyphen ( - ) or a comma. Keep the spaced hyphens the template uses.
- Put a single horizontal rule (`---`) after the INITIAL email and between every follow-up.
- Label every follow-up with its wait time on the same line as its heading, e.g.
  **FOLLOWUP 1** *(send 3 days after the initial)*.
- Use the guest's first name in every greeting. Use the company name in the last-nudge lines.

### Wait-day cadence (fixed)

- INITIAL - Day 0
- FOLLOWUP 1 - 3 days after the initial
- FOLLOWUP 2 - 5 days after Follow-up 1
- FOLLOWUP 3 - 7 days after Follow-up 2
- FOLLOWUP 4 - 7 days after Follow-up 3

### The angle (the only tailored line in the initial)

- One line, two at the very most. The founder is busy and already knows their own story, so do not
  recap what they built or narrate their achievement back to them. Restating their own biography is
  the single biggest way these emails go wrong.
- Name their company (or companies) as a light anchor, then go straight to the angle you would
  explore: their leadership lens, how they built the team, or how they think about ownership.
- Ownership can be the angle, the show is about it. Grounded and plain. No flattery, no hype, no
  "masterclass", no em dashes.
- Verified only. Do not invent a company, a metric, or a claim.
- Gold-standard shape: "We'd get into your leadership lens across [Company A] and [Company B], and
  how you think about who gets to own a piece of what they build."

### Template (reproduce verbatim except the [TAILORED ANGLE] line and the name/company/link slots)

The initial is deliberately short, four or five sentences. Do not add the full host bio or the full
guest list to the default send; those live in the optional credibility expansion in Notes, used only
when a colder or more skeptical guest needs extra proof.

INITIAL
Sub: We want to interview you! (Built to Share podcast)

Hi [First name],

I'd love to have you on Built to Share, a show about how founders build teams and share ownership with the people who build alongside them.

It's hosted by Satish Mugulavalli (founder, Hissa Fund). [TAILORED ANGLE]

60-minute unscripted conversation, recorded remotely in a 90-minute slot. 230k+ community, past guests include founders of CarDekho, Cashify, and Fibe. More at built2share.in/note

Open to it?

Regards,
Chaandini

---

FOLLOWUP 1 *(send 3 days after the initial)*

Hi [First name],

Just bumping this up in case it got buried. If it's easier, I'm happy to coordinate with someone on
your team to find a slot.

Regards,
Chaandini

---

FOLLOWUP 2 *(send 5 days after Follow-up 1)*

Hi [First name],

We recently published our conversation with [MATCHED GUEST], who [personalised one-liner tying their people / leadership story to why THIS guest would care] - you might enjoy how they think about building and holding a team together: [VERIFIED EPISODE LINK]

We'd still love to have your story on the show. Let me know how we can make that happen.

Regards,
Chaandini

> Follow-up 2 is now auto-personalised. Do NOT leave the three slots blank and do NOT
> guess. Open `references/published-episodes.md`, run its selection logic against the
> outreach guest's sector, and fill in the matched guest, a one-liner personalised to
> the outreach guest (not a generic episode recap), and the web-verified link. Then, in
> Notes, state which episode you picked and why it matches, so Akshay can swap it if he
> prefers another.

---

FOLLOWUP 3 *(send 7 days after Follow-up 2)*

Hi [First name],

Confession: we keep publishing founders on how they build and reward their teams, and I still
haven't managed to get the [Company] story on the show. It's starting to feel personal. Let's fix it?

Regards,
Chaandini

---

FOLLOWUP 4 *(send 7 days after Follow-up 3)*

Hi [First name],

Last nudge from me. No worries at all if the timing's off right now, the invite stays open whenever
it suits you.

Would genuinely love to have the [Company] story on Built to Share whenever you're ready.

Regards,
Chaandini

---

## Step 5 - Notes (only real flags)

After the emails, add a short Notes list only where there is a genuine call to make. Do not pad it.
Common ones:

1. **Follow-up 2 episode drop (auto-personalised, verified only)** - Follow-up 2 now selects the
   best-fitting *published Built to Share* episode from `references/published-episodes.md`, matched to
   the outreach guest's sector and story shape. State in Notes which episode you picked and why it
   fits, and give the matched guest name, the personalised one-liner, and the verified link so Akshay
   can approve or swap it. Rules that still hold: only episodes on the roster, never invent an episode
   or a link, web-verify the exact link before it ships, and never reuse a Founder Thesis episode as
   BTS proof (note some guests, e.g. Ravi Saxena, appear on both shows - use the BTS link only). If no
   roster episode is a real domain match, pick the strongest general org-building one and say so, or
   offer to cut Follow-up 2 to a plain nudge rather than force a weak fit.
2. **Thin ownership story** - if the guest's team / ownership narrative is weak, say so and let the
   angle lean on their strongest people or scaling angle instead of a forced equity line.
3. **Competitor guard** - if the guest is a direct Hissa / cap-table competitor (Carta, Ledgy, Pulley,
   AngelList, Qapita), flag before sending.
4. **Warm-intro variant** - if this is not fully cold (Satish or the team has a prior thread), open
   with the leaner "As discussed, I'm sharing a quick overview of the podcast..." line in place of
   "I'd love to have you on Built to Share...". Default stays the cold open above.
5. **Optional credibility expansion** - the default initial is short on purpose. For a colder or
   more skeptical guest who needs more proof, offer to add the fuller block back in: the host bio
   ("Satish has spent 20+ years as a serial entrepreneur, 4 years as a Venture Partner at YourNest
   VC analyzing 1,200+ startups, and is the founder of Hissa Fund") and the full guest list
   (CarDekho, Fibe, Cashify, Mudrex, Arya.ai). Only on request; never the default.
6. **Even-leaner option** - if the single social-proof line ("230k+ community, past guests...") is
   still too much, offer to drop it entirely and let the initial run four sentences.
7. **Stale role** - if the founder has exited or moved on since their LinkedIn headline was written,
   flag it. Name the old company as the story, the new one as the present. A present-tense role you
   have not verified is a hard error, not a rounding issue.
8. **LinkedIn seat** - if the connection note runs close to 300 characters, flag that free accounts
   cap at 200 so Mamatha knows whether the note needs a further cut on her seat.
9. **Reachability read** - one line on whether LinkedIn or email is the better first touch for this
   guest (LinkedIn-heavy and media-active founders favour the DM; quieter operators favour email).

---

## What good output looks like (worked example: Kunal Bahl, Snapdeal / Titan Capital)

Tailored angle line used (gold-standard shape):
"It's hosted by Satish Mugulavalli (founder, Hissa Fund). We'd get into your leadership lens across
Snapdeal and Titan Capital, and how you think about who gets to own a piece of what they build."

That is the bar. Note what it does NOT do: it never re-tells Kunal the Snapdeal comeback, never
recaps a metric, never flatters. It names the companies as a light anchor and goes straight to the
angle. A founder reads it in seconds and knows exactly what the conversation would be about. Every
fixed line around it matches the short template exactly.

Counter-example (the trap to avoid): "Steering Snapdeal from the brink back to profitability is one
of the hardest team stories in Indian tech..." That narrates his own biography back at him. He
lived it. Cut it.

---

## Hard rules recap

- Ship **both channels by default**: LinkedIn messages first, then the email sequence. Narrow only
  if Akshay explicitly asks for one.
- Measure the connection note with a real character count against the 300 cap, INCLUDING the
  "Regards, Akshay Datt" signoff. Never estimate. If a long first name pushes it over, cut wording,
  never the signoff or the ask.
- Signoffs are split by channel: every LINKEDIN message (connection note, InMail/DM, and all four
  LinkedIn follow-ups) ends with "Regards, Akshay Datt", and every EMAIL (initial and all four
  follow-ups) ends with "Regards, Chaandini". Own line in the InMail and emails; inline at the end
  of the short LinkedIn messages. Never mix the two names across channels.
- Verify the founder's current role before writing. Never assert a stale present-tense title.
- No em dashes anywhere.
- The initial email stays short (four or five sentences). Never pad it with the full host bio or
  full guest list; those are an optional expansion, not the default.
- One horizontal rule after the initial email, and one between every follow-up.
- Every follow-up carries its wait-days on the heading line.
- Only the tailored angle line and the name / company / link slots are tailored; all other wording
  is verbatim template.
- Never recap or narrate the guest's own story back at them. They already know what they built.
  Name the angle, not the biography.
- Verified figures, names, and links only. No invented numbers, guest names, or episode links.
- Follow-up 2 is auto-personalised from `references/published-episodes.md`: pick the closest published
  Built to Share episode to the outreach guest's sector, output the matched guest, a personalised
  one-liner, and the web-verified link, and note the pick in Notes. Never a blank slot, never invented,
  never a Founder Thesis episode passed off as BTS.
- Guests are never called clients.
