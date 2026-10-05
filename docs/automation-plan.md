# Automation plan

Proposal, 5 Oct 2026. Builds on Akshay's "Inbox parser routine: handover" (5 Oct) and `routines/inbox.md`. Nothing here is switched on until Akshay approves the open questions at the end.

## What exists today

| Routine | Schedule | State |
|---|---|---|
| Inbox to Business OS (trig_01Q1P1B58ZQeQaeNfsqDMzUm) | 06:57 and 20:57 JST | Scheduled, but no connectors attached, so every run stops at step 0 |
| B2S sheet to Notion daily sync | daily | Running, has Gmail, Notion, Calendar, Drive |
| FT Newsjack daily scan | daily | Running |

Two inbox designs exist and disagree in two places. This plan merges them into one.

| Point | Handover routine | routines/inbox.md (this repo) | Plan |
|---|---|---|---|
| Status rules | Detailed table: chase ladder, LT chase on timing reasons, last-chance chasers go to Akshay | Simpler ladder | Use the handover's rules |
| Parked | Akshay only: he is no longer interested. LT chase = revisit later | Parked = revisit on Next date | Use the handover's meaning (needs a yes) |
| Queue | Cards with a Choice picked in the "Akshay: decide" tab; the agent would apply the choice | Board; Akshay clicks the Engagement and changes Status himself; the agent closes the card | Use the board (Akshay asked for it on 5 Oct). The agent closes a card once the Engagement moves or his reply shows in the thread |
| Cards for | Akshay, Mamatha, Chaandini | Akshay only, for evals and direct questions | Akshay for decisions; Mamatha for "needs human" facts; Chaandini for unclear deals |

## The four automations

All run as Claude routines in the cloud with the Gmail, Notion and Google Calendar connectors attached. Polling is the trigger: there is no push from Gmail, so "when a pitch arrives" means "on the next run", at most an hour later.

### 1. Inbox to Notion (hourly, 09:00 to 21:00 IST)

One run, in this order:
1. Log every real email as an Activity (Gmail message id, so nothing is logged twice).
2. Create People and Organisations, deduped, Source Agent.
3. Move Engagements and Deals on clear evidence, with a Claude note line on every change (handover status table).
4. Queue cards only for real decisions: an eval to decide, a direct question to Akshay, a last-chance chase, a timing reason (LT chase or Park). One card per thread, linked to the Engagement or Deal, title led by the guest.
5. Close cards whose Engagement has moved or where Akshay has replied.
6. Pitch trigger, below.

### 2. New pitch trigger (inside run 1, plus an eval routine)

When a new inbound guest pitch arrives:

| Step | What happens | Approval |
|---|---|---|
| a | Person, PR contact, Organisation and Engagement created (Status New, Direction Inbound, Show detected) | Automatic |
| b | Reply on the thread: "Thanks for your mail, adding Mamatha to coordinate", Mamatha in Cc, from ad@thepodium.in | Standing approval (decision 56). Only when Mamatha is not already on the thread. First week as Gmail drafts, then live |
| c | Guest eval runs with the show's skill (ft-guest-eval, un-guest-eval, bts-guest-eval, hbd-guest-eval) | Automatic |
| d | Eval link and Eval verdict written to the Engagement, Status Decision pending | Automatic |
| e | Queue card for Akshay: "<Guest @ Company>: eval says <verdict>, your call" with the eval link | Automatic |

The eval runs as its own routine ("Guest evals", hourly at :30) that picks up Engagements with Status New and no Eval link. That keeps the inbox run fast and means a failed eval never blocks logging. Mass pitches (the pitch names another show) get an Activity only, no eval. Mamatha no longer writes evals by hand; she gets the routed thread and sees the verdict on the Engagement.

### 3. Calendar to Notion (inside run 1)

Read the ad@thepodium.in calendar from 2 days back to 30 days ahead and match events to Engagements by attendee email, then guest name.

| Calendar shows | Notion does |
|---|---|
| Recording event with the guest | Booked, Next date = recording date |
| Precall event | Precall requested stays, Next date = precall date |
| Event cancelled, or guest declined | Next action "Recording cancelled: rebook or close", card for Mamatha (the Vicky Dodani case) |
| Recording date passed, not cancelled | Recorded, with a Claude note (Mamatha can correct) |
| Booked in Notion, no event on the calendar | Card for Mamatha: "Booked but no invite" |

### 4. Notion to Calendar (daily, 07:00 JST)

- For every Booked recording, a private entry on a separate "Podium prep" calendar, 30 minutes before: guest, company, show, and links to the dossier, eval, LinkedIn and Engagement. Allowed without asking (CLAUDE.md: private entries on Akshay's prep calendar).
- Never creates, moves or edits an event that has guests on it. Recording invites stay with Mamatha. If Notion and the calendar disagree, the calendar wins and the Engagement is corrected.

## Next wave (after the first four run clean for a week)

| Trigger | Action | Approval |
|---|---|---|
| Booked, recording in 3 days | Run ft-host-dossier, put the Dossier link on the Engagement and in the prep entry | Automatic |
| Recorded | Thank-you mail to the guest, cc every Stakeholder, with the FT form link | Standing approval for the template (CLAUDE.md) |
| Recorded, form not filled | Reminders at +3 and +7 days until Form filled | Same template approval |
| Person tagged "Add to WhatsApp" | founder-thesis-blurb skill, blurb saved on the Person and sent to Akshay | Automatic |

## Guardrails (all routines)

- Email goes only from ad@thepodium.in, only the approved templates, with a daily send cap of 20. A switch on the Business OS home page (Sending: ON or OFF) stops all sending at once.
- Never deletes rows, never changes schemas, never touches Credentials or Templates.
- Never sets Parked, Tier, Decision, Amount or Payment; never edits a calendar event with guests.
- If a connector is missing, the run stops and reports; no partial work.
- Every run ends with a short report and a push notification.

## Setup work

1. Rewrite the Inbox to Business OS prompt as the merged version and attach Gmail, Notion and Google Calendar. Connectors can only be attached when a routine is created from here, so the routine is recreated with the same name and schedule; the old one is deleted once the new one has run cleanly.
2. Create the Guest evals routine and the Notion to Calendar routine.
3. Create the "Podium prep" calendar.
4. Fix the data the handover found: the 46 Parked rows re-sorted into LT chase or Parked (a list for Akshay), three rows set to Parked on 5 Oct by the review moved to LT chase (Flourish Ventures, Nikita Kumawat, Ankit Utreja), the Pavan Kavad duplicate.
5. One supervised test run of each routine, read together, before the schedules go live.

## Open questions for Akshay

1. Parked = "no longer interested, Akshay only" and LT chase = "revisit later": adopt?
2. Inbox runs hourly 09:00 to 21:00 IST (13 runs a day) or twice a day?
3. Pitch reply: drafts for the first week, then live?
4. Auto-eval every new pitch on all four shows, or Founder Thesis only to start?
5. Set Recorded automatically once the calendar date passes?
