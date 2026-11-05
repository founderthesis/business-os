# Cleanup verdict: B round (5 Nov feedback B1 to B15)

Cleanup session, 5 Nov 2026, about 21:30 JST. Read-only. Nothing deployed, no Notion write, no mail.

## Verdict: accepted, with one condition on the Zoya hourly (C1)

Every build was reproduced twice from its live base, byte-identical, and each matches the hand-off and the committed copy.

| Routine | Live base, how proven | Build | Bytes / sha256 |
|---|---|---|---|
| Zoya hourly | r19 ee8f1966 (pin 95c4e79 live) | zoya-r21/zoya-one.txt | 57,877 / 69a0c4bfa6cb9693 (with C1: 58,053 / 187b4f54ec26e056) |
| Zoya SLOW task | r19 8c8765db | zoya-r21/zoya-slow.txt | 14,416 / a81e3bc6752c9a33 |
| Zoya SLOW file | pin 201f730 | zoya-slow-work.txt | 85,088 / 9d74718b043345e3 |
| Zoya episodes (not live) | r19 | zoya-r21/zoya-episodes.txt | 47,566 / 185326a27ef23a28 |
| Calendar sync | e4b39d67, then precall-409 | calendar.txt | 61,195 / 9dc4babe6294cf18 |
| Daily sweep | 76b49956, then precall-409 | sweep.txt | 43,938 / 4ef8998fad2ced33 |
| WhatsApp | 8628f42a, then precall-409 | whatsapp.txt | 27,410 / 174d931773dd6cc0 |
| Inbox capture | 40e787a2 (live prompt saved to file and byte-compared) | capture.txt | 49,196 / 72c4d81afaefb68e |
| Inbox actions | 07832eb6 (inbox-split/r11/actions.txt) | actions.txt | 46,501 / 459e40411924cddd |
| Host dossiers | 98875d4e (base rebuilt by reversing the 5 edits) | dossiers.txt | 6,401 / 28a2d9b739dafac7 |

How each base was proven:
- **Zoya:** build_one.patch on a clean f70901f tree, then build_one.py at 201f730.
- **Calendar, sweep, WhatsApp:** precall-409 then b-round patch.py.
- **Capture:** the live prompt is r13c byte for byte.
- **Actions:** live came back inline. It was last updated 3 Nov, at the r11b deploy, and I compared it by content.
- **Dossiers:** reversing the 5 edits gives 5,942 / 98875d4e, the hash patch.py asserts. That matches the live text I read: the 466 sentence, "at most 3 per run", and no update since 4 Nov 07:48Z.

No em dash was added anywhere.

## The checks the CTO named

- **B2, no compose reply:** holds in every build. No email_compose action reply is left in any Zoya variant, calendar, capture, actions, sweep or WhatsApp. email_compose survives only for a new mail and the sweep's billing forward. Every reply (Zoya, the calendar's day-before note, capture's loop-in) follows the same five steps:
  1. draft reply
  2. draft update To and Cc
  3. draft_read
  4. a python assert on draft_read's actual To and Cc
  5. draft send

  A failed assert deletes the draft.
- **B10, no Meet on recordings:** INVITES gives a precall a Meet and a recording none. STEP 0r removes a Meet from a recording invite, including the "link already there" case. **C1 (condition):** 0r never says it can't touch a precall. It edits "that recording event", matched through a Booked row. A Booked row that also has a precall or prelim on the calendar could lose the wrong invite's Meet, which is a change to an event with guests. The fix is one replacement in zoya-one.txt:
  - Replace: `Then the link add on that recording event:`
  - With: `Then the link add on that recording event (the guest's recording invite only, the event the row's Call type Recording and Next date point to; never a precall or prelim invite, whose Meet stays, Akshay, 5 Nov, item 13):`
  - Result: **58,053 / 187b4f54ec26e056**, reproduced twice. It occurs once, and the other three Zoya files don't contain the string. Put it into r21_edits.py, or deploy this exact file.
- **B11, thank-you:**
  - Calendar 4c drafts a standalone new mail, never a reply, with one Akshay segment ("send the thank-you ... and add <guest> to the FT Community WhatsApp").
  - The patron paragraph is out for Sponsored, and the PR paragraph only appears when a PR or comms person is on To (Via is always on To).
  - The 4f transcript row on FT and SLOW (4b) carry the transcript, and (4b) keeps quiet hours.
  - **Timing for the Gulab test:** 4c runs "in the first run after Recorded", and Recorded needs STEP 4's evidence. Gulab records at 21:00 JST on 6 Nov, so the draft can't appear before the 07:35 JST calendar run on 7 Nov, and only once the Zencastr audio is in Drive. That's expected behaviour, not a failure.
- **B12, Next action size:** Zoya and actions write segments of about 120 characters, with the detail in the Claude note. Sweep 3a3 trims existing rows. It keeps who, the step and its date, puts the cut words first in a dated Claude note line, and never changes the ask, owner, key or Waiting on. Nothing Akshay still owes is dropped: "Write ok, not ok" leaves, but the step itself stays. The scheduling and 448 templates keep the recommended step in the segment, so his "ok" still approves the step on the row.
- **B14, community asks:** no community segment is written anywhere:
  - calendar 4a, 4b and 4c.2;
  - sweep 3k;
  - WhatsApp e0 and 3a(1).

  The sweep's one-time cleanup moves old asks onto the FT Community To invite list, changes no other Membership value, and keeps the thank-you segment.
- **PR guard:** it's in sweep 3g, sweep 3k and the calendar's Guests line. A person People tags PR contact, or the row has as Via or Stakeholder, is never the guest, whatever the title says.
- **Decision 409:** carried. No "precall:<event id>" key is left in any build. The exemption line now reads "(transcript:) ... precall promises go on the guest's own row (decision 409)" in calendar, sweep, WhatsApp, capture, actions, the SLOW file and episodes.

## Not carried: my r20 items (please put them in r22)

r21 is built on r19, and none of these is in it:
- **L1:** a Failed record on the no-repo path.
- **L2:** re-read the record's Summary before RELEASE.
- **Note-check fixes:**
  - (a) SQL never counts as a full read;
  - (b) an exact new == line + old assert, plus a re-fetch;
  - (c) chk: on every note: outcome line.
- **The hourly's status checked in code,** so a self-chosen skip is Failed, not Partial.
- **Counting sends by Message-ID,** never by Sent item.

r21 doesn't make any of these worse than live r19. But the 11:08 run showed the note rule being bypassed, and the hourly keeps leaving steps. They're the next round's first items, so they don't get lost a second time. r20 (decision 467, C1 open) gets rebased onto r21 as planned.

## Should-fix (not blocking)

- **S1. Form link in the thank-you.** W3 puts podm.in/thank-you only in the PR paragraph. A guest with no PR gets no form link until the form chaser, while 4c then sets "Waiting on <guest>: guest form". Either add a one-line form ask for the no-PR case, or accept the chaser. That's Akshay's wording call. Raise it with the "review" question the hand-off already flags.
- **S2. B7.** The Akshay step for a blocked delete is right (Zoya can't delete events). It only works once the CTO's item 1 is done: a permission mode, or an allow override for delete_event on Calendar sync and Inbox actions. Until then every cancelled call becomes an Akshay step.
- **S3. Known items to log on the Build board,** so they aren't lost:
  - calendar moving Booked back to Booking;
  - 4a setting both Invited and To invite;
  - 4d's "attach the transcript".

## Deploy order

As the hand-off says: calendar, capture, Zoya (pin 201f730, hourly with C1, SLOW task), then sweep, actions, WhatsApp, dossiers. Read each back byte for byte against the sizes above. W8 (Gulab's Meet) comes before his 6 Nov recording, and W3's toggles before the first 4c and (4b) runs.
