---
name: notion-business-os
description: Update ThePodium Business OS in Notion from any chat. Trigger when a message starts with "update in notion business OS" or "update in Notion", or asks to change a guest's status, next date, next action, eval, dossier, PR contact or organisation, or to log that something happened with a guest (recorded, form filled, precall done, declined, parked). Finds the right Engagement and People rows, makes the change, and leaves a dated note so the team can see who changed what.
---

# Update the Business OS in Notion

The Business OS is ThePodium's single record of every guest conversation. Mamatha works it every day; the team's Google Sheets are retired (decision 71 and Akshay on 6 Oct). This skill lets her, or anyone on the team, say in plain words what happened and have Claude make the change correctly.

## Where things live

| Table | Data source | What one row is |
|---|---|---|
| Engagements | collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5 | one guest conversation for one show (person + organisation + show) |
| People | collection://e6c44319-7f81-4da6-8b80-8441a4875d7a | one human, ever: guest, PR person, EA, colleague |
| Organisations | collection://c43c280a-3b37-4821-96ef-dab688a53aea | one company |
| Shows | collection://ebca6861-4d71-4555-a6ec-6ed76cc0c733 | Founder Thesis 3ed19a301a7f817c9367e0d88afc5776, alpha un# 3ed19a301a7f8111b5e4d46002a7afe1, Built to Share 3ed19a301a7f819e8f45de04a7c9d025, Human by Design 3ed19a301a7f815585e7e6c8accaab23 |
| Queue | collection://af59132c-92cb-4e87-85f0-266bd07309c4 | a card on Mamatha's worklist |

Fetch a data source once before writing to it, to get exact property names. Never open the Credentials page.

## Status, in journey order

New (a name we noted, nothing done) · Contacted · Interested · Decision pending (waiting on Akshay; for alpha un#, Akshay gets Sri's call) · Precall requested · Precall done · Sponsored offered · Booking (chasing a recording slot) · Booked (recording on the calendar) · Recorded · Form filled (all done).

Off the ladder: LT chase (still want them, revisit on Next date) · Parked (Akshay has lost interest; stop following up, no formal no; Akshay only) · They declined · We declined · Unresponsive.

Direction: Inbound = they pitched us (usually via PR). Outbound = we reached out first. A cold lead stays Outbound even after they reply.

## Rules when changing a row

1. Find the Engagement by guest name and show (search Name, or the Guest's People row). If two rows could match, ask which one; never guess.
2. Next date is the date of the next follow-up, not the date of the last one. When a follow-up is done, set Next date to when you will chase next.
3. Never move Status backward on the ladder unless the person asks for it in so many words. Never set Parked, Tier, Amount or Payment unless the message is Akshay's decision.
4. Add one line at the top of Claude note: "YYYY-MM-DD <who>: <what changed and why>", keep older lines below it, and set Claude updated to today.
5. New person (a PR contact, an EA): search People first by email, then name + company. Create only if not found, with Source Manual, Captured today, and the Organisation. Add them to the Engagement's Stakeholders (PR) or Via (who brought the guest). Never store a person only in a note.
6. New guest: create the People row, the Organisation if missing, then the Engagement named "<Guest> @ <Company>, <Show>", Status, Direction, Show, Guest, Organisation, Source Manual, Captured today.
7. Never delete rows. To get rid of a duplicate, rename it "DELETE: <name>" and tell Akshay.
8. Do not write email addresses or phone numbers into notes or page text; they go in the Email and Phone fields of People only.
9. When done, reply with one line per row changed: the row name, what changed, and the link.

## Examples

- "update in notion business OS: Anmol Madan recorded today, thank-you sent, chase the form on Monday" → Status Recorded, Next date next Monday, Next action "Chase the guest form", Claude note line.
- "Supriya not replying after three follow-ups, try again 25 Oct" → Next date 2026-10-25, Next action "Fourth follow-up", status unchanged.
- "Deepan at Vita: PR no longer represents him, we are talking to Daniel directly for the precall" → Direction stays as is, add Daniel as a Stakeholder, Next action "Precall via Daniel".
- "Lupin: park it" from Akshay → Status Parked. From anyone else → ask Akshay first.
