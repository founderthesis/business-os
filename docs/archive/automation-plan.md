# Automations

What runs, when, and what it is allowed to do. Built 5 Oct 2026 on Akshay's go-ahead (decisions 66 to 68). The prompts live in `routines/`; the routines in claude.ai hold a copy, so change both together.

## The routines

| Routine | Runs (JST) | Connectors | Prompt |
|---|---|---|---|
| Inbox to Business OS | 06:55, 14:55, 20:55 daily | Gmail, Notion | `routines/inbox.md` |
| FT guest evals | 07:20, 15:20, 21:20 daily | Notion, Gmail | `routines/evals.md` |
| Calendar sync | 09:35, 16:35, 22:35 daily | Google Calendar, Notion, Gmail | `routines/calendar.md` |
| Daily sweep | 13:10 Mon to Sat (09:40 IST) | Notion, Gmail | `routines/daily-sweep.md` |

Each run starts a fresh cloud session and ends with a short report; a push notification goes to Akshay when a run has something worth knowing.

**Setup still needed:** the routines were created without connectors, because this organisation does not allow attaching them from a session. Open each routine in the claude.ai routines page and add the connectors in the table. Until then each run stops at the first step and says the connector is missing.

## What each one does

**Inbox to Business OS.** Logs every real email as an Activity, creates People and Organisations, and moves Engagements and Deals on clear evidence, with a Claude note line on every change. Three actions beyond capture:
- New FT pitch (not a mass pitch, under 72 hours old, nobody from our side on it yet): replies "Thanks for your mail, adding Mamatha to coordinate" with Mamatha in Cc.
- Calendar RSVP mail (Accepted, Declined, Maybe) with no human reply: archived and marked read. A guest decline is noted on the Engagement.
- Akshay's decisions read from his mail (his reply on the eval mail, the PR thread, or a mail to Mamatha) and applied to the Engagement. No cards for them (decision 78).
- Guest form submissions (the Notion guest form, decision 69): matched to the guest's Engagement, People and Organisation gaps filled, PR emails added as Stakeholders, Status Form filled, Guest form in ticked on the Episode, an Activity logged, and the row flagged for Mamatha to send the likely release date. No match goes to Needs review and is counted in the daily sweep mail.

**FT guest evals.** Picks up new inbound FT Engagements the inbox created (no eval yet, captured in the last 7 days, at most 5 a run). Runs ft-guest-eval and writes Eval link and verdict. Book immediately goes to Booking, flagged "Mamatha: ask for recording slots"; anything else sits at Decision pending, flagged "Ask Akshay to approve". Mails the eval to Akshay and Mamatha so Akshay can reply with his call (decision 78). If Mamatha already sent one, it copies hers instead. FT only.

**Calendar sync.**
- Calendar to Notion: recordings and precalls on the ad@thepodium.in calendar set Next date, Call type and Call link; a recording moves the Engagement to Booked. A cancelled or declined event, or one that vanished, flags the row for Mamatha to rebook or close. Booked with no invite is flagged as a fix.
- Notion to calendar: a private entry, no guests, no notifications, for each recording and precall in the next 14 days. Recordings get a 30-minute prep block before the call; precalls get an entry at the same time as the call, marked free, so no time is blocked (decision 73). Title "Prep: Guest @ Company (FT recording)", the call link as location, and the eval, dossier, LinkedIn and Engagement links in the description. Moved and cancelled calls update or remove it.
- After a recording that was not cancelled: a thank-you draft in Gmail copied from the last one Akshay sent (same wording, with the Notion guest form link in place of the deleted short link, guest and PR in To, every Stakeholder and the usual team in Cc), a WhatsApp blurb from founder-thesis-blurb (not sent to Slack), and a flag "Ask Akshay to send the thank-you draft and post the blurb", with the blurb in the Engagement's page body. FT only for the draft and blurb. Recorded is set by the inbox once the thank-you goes out.

**Daily sweep** (was Queue upkeep). Moves any leftover Queue card onto its row, applies what Gmail already settles (Akshay's decisions, replies, three unanswered chases over 30 days -> Unresponsive), flags what has gone quiet or is missing, and mails Mamatha the count with the FT: Today link.

| Check | Flag (Next action) |
|---|---|
| Decision pending, no decision in Gmail, no Next date | Ask Akshay to approve: eval says <verdict> |
| Decision pending, eval Book immediately | Status Booking. Mamatha: ask for recording slots |
| Open row, no Next date, no activity in 14 days, nothing new in Gmail | Mamatha: quiet since <date>, chase or update the status |
| Recorded over 5 days, form not in | Mamatha: send the form reminder |
| Sponsored, booked or recorded, payment not started | Mamatha: send GST and invoice details |
| Booked with no date, booked guest with no email, guessed name on a booked row, no status, no guest | Fix: ... |
| Deal at Interested or later, or a Warm deal, untouched 14 days | Akshay: follow up or close |

Cold deals at New or Contacted are the outreach list and are never flagged.

## The worklist: FT: Today (decision 79)

The Queue is retired. Anything that needs a person is a flag on the row itself: **Next date = today** and **Next action = who does what**, starting with the person ("Mamatha: reply to Rhea with a slot", "Ask Akshay to approve: eval says Strong consider", "Fix: booked guest has no email"). The Engagements view **FT: Today** shows every FT row whose Next date is today or earlier (closed rows aside), oldest first, with **Last activity** (the newest logged mail, written by the routines) next to Next action.

- Mamatha clears the list by doing the step and moving Next date forward, or by replying by mail: when our side replies and the ball is in their court, the inbox routine moves Next date 4 days out and writes "Waiting on <who>".
- A Next date of today or earlier is an open flag. Routines never move it later unless the mail settles the ask.
- "Due" is a formula (Next date on or before today) that the view filters on, because the Notion API cannot save a relative date filter.
- The Queue database stays for history; nothing writes to it.

## Guardrails

- Mail goes only from ad@thepodium.in and only these: the pitch reply, eval links to Mamatha, the daily queue mail to Mamatha. Thank-you mails are drafts that Akshay sends.
- Send cap 100 a day across all routines, counted from Activities whose Summary starts "Agent sent". A runaway guard, not a quota.
- Never deletes rows, never changes schemas, never touches Credentials.
- Never sets Parked, Tier, Amount or Payment unless the mail is Akshay saying so.
- Calendar: only events carrying "bos-key:" in the description are ever created, changed or removed. Events with guests are never touched.
- Every change to an Engagement or Deal adds a dated line to Claude note.

## Next wave

| Trigger | Action |
|---|---|
| Booked, recording in 3 days | ft-host-dossier, Dossier link on the Engagement and in the prep entry |
| Recorded, form not in after 3 and 7 days | Reminder drafts on the thank-you thread |
| Auto eval for un#, Built to Share, Human by Design | Their own eval skills, once FT runs clean |
