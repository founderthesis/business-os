---
name: notion-business-os
description: Update ThePodium Business OS in Notion from any chat, for anyone on the team. Trigger when a message starts with "update in notion business OS" or "update in Notion", or asks to change any guest, deal or person record (status, next date, next action, tier, parked, eval, dossier, PR contact, organisation, payment, amount), or to log that something happened (recorded, form filled, precall done, declined, parked, paid). Finds the right rows, makes the change, and leaves a dated note saying who asked for it.
---

# Update the Business OS in Notion

The Business OS is ThePodium's single record of every guest, deal and person. The team's Google Sheets and Blue are retired. Anyone on the team can change anything in it, either in Notion directly or by telling Claude in plain words. This skill is the second route: say what happened, and Claude finds the rows and makes the change.

## Where things live

| Table | Data source | What one row is |
|---|---|---|
| Engagements | collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5 | one guest conversation for one show (person + organisation + show) |
| People | collection://e6c44319-7f81-4da6-8b80-8441a4875d7a | one human, ever: guest, PR person, EA, colleague, prospect |
| Organisations | collection://c43c280a-3b37-4821-96ef-dab688a53aea | one company or fund |
| Deals | collection://1a981c5a-912a-4972-b3fc-8c9f2abb329a | one sales conversation for a branded podcast or retainer |
| Shows | collection://ebca6861-4d71-4555-a6ec-6ed76cc0c733 | Founder Thesis 3ed19a301a7f817c9367e0d88afc5776, un# 3ed19a301a7f8111b5e4d46002a7afe1, Built to Share 3ed19a301a7f819e8f45de04a7c9d025, Human by Design 3ed19a301a7f815585e7e6c8accaab23 |
| Activities | collection://290f715d-fd45-4203-ade6-3642c2326c6c | one email, call, form or note, logged once |

Fetch a data source once before writing to it, to get exact property names and select options. Never open the Credentials page.

## Engagement status, in journey order

New (a name we noted, nothing done) · Contacted · Interested · Decision pending (waiting on Akshay's call; for un#, Akshay takes it to Sri) · Precall requested · Precall done · Sponsored offered · Booking (chasing a recording slot) · Booked (recording on the calendar) · Recorded · Form filled (all done).

Off the ladder: LT chase (still want them, revisit on Next date) · Parked (lost interest, stop following up, no formal no) · They declined · We declined · Unresponsive.

Tier: Tier 1, Tier 1.5, Tier 2 (how much we want them), or Sponsored (the guest pays; Payment and Amount apply).

Direction: Inbound = they pitched us (usually via PR). Outbound = we reached out first. A cold lead stays Outbound even after they reply.

Deal stage: New, Contacted, Interested, In conversation, Proposal sent, Won, Parked, Declined, Unresponsive.

## Rules when changing a row

1. Do what the person asks. Anyone on the team can change any field, including Status, Tier, Parked, Payment and Amount.
2. Find the row by name and show (search Name, or the person's People row). If two rows could match, ask which one; never guess.
3. Next date is when someone next acts, not the date of the last contact. Today or earlier puts the row on the team's list (the FT: Today view). When a step is done, move Next date to when to chase next. To flag something for a person, set Next date to today and Next action to who does what, starting with the person ("Mamatha: send the precall invite", "Ask Akshay to approve: eval says Strong consider"). The Queue is retired: never write to it.
4. If a change moves Status backward on the ladder, or changes a price or commercial term on a Sponsored row or a Deal, make it and say so plainly in the reply so nobody is surprised.
5. On an Engagement, add one line at the top of Claude note: "YYYY-MM-DD <who asked>: <what changed and why>", keep older lines below it, and set Claude updated to today. Deals have no Claude note: put the same line in Next action when the change closes or parks the deal. Use the asker's first name. If you can't tell who is asking, ask once.
6. New person (a PR contact, an EA, a colleague): search People first by email, then name + company. Create only if not found, with Source Manual, Captured today, and the Organisation. Add them to the Engagement's Stakeholders (PR, comms, EA) or Via (who brought the guest). Never store a person only in a note.
7. New guest: create the People row, the Organisation if missing, then the Engagement named "<Guest> @ <Company>, <Show>", with Status, Direction, Show, Guest, Organisation, Source Manual, Captured today.
8. Never delete rows (the connector can't, and merges need a human). To get rid of a duplicate, rename it "DELETE: <name>" and tell the person to delete it in Notion.
9. Do not write email addresses or phone numbers into notes or page text. They go in the Email and Phone fields of People only.
10. When done, reply with one line per row changed: the row name, what changed, and the link.

## Examples

- "update in notion business OS: Anmol Madan recorded today, thank-you sent, chase the form on Monday" → Status Recorded, Next date next Monday, Next action "Mamatha: chase the guest form", Claude note line.
- "Supriya not replying after three follow-ups, try again 25 Oct" → Next date 2026-10-25, Next action "Mamatha: fourth follow-up", status unchanged.
- "Deepan at Vita: PR no longer represents him, we are talking to Daniel directly for the precall" → add Daniel as a Stakeholder, Next action "Precall via Daniel".
- "Lupin: park it" → Status Parked, Next action cleared, Claude note line naming who asked.
- "Rayls paid the first invoice" → Payment "Payment 1 received", Claude note line.
- "Acadly deal is parked" → Deal Stage Parked, Next action "2026-10-06 Akshay: parked".
