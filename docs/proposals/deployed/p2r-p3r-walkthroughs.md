# P2r/P3r final corrections: walkthroughs (18 Oct 2026)

These are walkthroughs of the text in `p2r-p3r-2026-10-18.patch`, not executions. The patch is not deployed. It waits for cleanup's review, and main deploys it after.

The patch applies to inbox, calendar, Zoya and daily sweep at repo 1beae15 (decisions 329 and 330).

## What changed against cleanup's review

| Cleanup asked | Now in the patch |
|---|---|
| Day-before Draft needs a route to sending | Akshay's ok on the approval ask is a Zoya step naming the exact draft id and event id (inbox YOUR CALL). Zoya STEP 0e2 sends that draft unchanged after rechecking the event, its time, the 3-hour window, holds and duplicates. |
| Day-before Draft needs an expiry | Calendar 3b expiry runs every run: the event started, moved or gone deletes the draft and drops both the ask and the step. Zoya 0e2 also refuses an expired or superseded draft. Neither ever sends later. |
| Close-note test | It has gone only if a message from our side since the no is the close note itself or Akshay's own substantive reply settling it. An acknowledgement, a loop-in or any other mail never counts. One found but not logged gets logged, and nothing is resent. |
| Repair scope (cleanup proposed 14 days) | Replaced at Akshay's instruction. Every unresolved failure stays eligible, whatever its age. Each run takes at most 10, oldest first, and re-reads each message to confirm it is a no. |
| Proposed mail | Set only when a matching Templates row exists. A wording-page mail has none, so it stays empty (Zoya 0e and inbox 6c e.). |
| Sweep line | The "Tier set but no draft" Fix waits 2 days while Zoya's decision-mail step is queued (P2r). |

Size: inbox 65,172 B, under the 65,536 cap. The space came from cutting 6c f. (drafts from before 12 Oct) and shortening the WhatsApp-to-Akshay wording, with its meaning unchanged.

## Cases

1. **Approved early.** FT recording on 21 Oct at 19:00 JST. Draft made 20 Oct 08:35. Akshay writes ok at 11:00.
   - The inbox queues "Zoya: send the approved day-before draft (<id>, event <id>)".
   - Zoya's next run: the event is unchanged and 30 hours out, with no hold and no earlier note. She sends that draft and logs it with the message id.
   - **Pass.**
2. **Approved too late.** Same, but ok arrives at 17:00 on 21 Oct.
   - Zoya at 17:30 finds it 1.5 hours to start, under 3, so she sends nothing and leaves the step.
   - After 19:00 the calendar expiry deletes the draft and drops both. It never sends.
   - **Pass.** The rule is strict: an ok inside 3 hours sends nothing.
3. **Moved after approval.** Ok given, then the recording moves to 23 Oct.
   - Zoya finds the start differs from the draft's time. She deletes it, drops the step and logs superseded.
   - The calendar makes a fresh draft for 23 Oct the day before, with a new ask.
   - **Pass.**
4. **Never approved.** The recording starts. Calendar expiry deletes the draft and drops the ask. **Pass.**
5. **Hold.** Ok given, then a no-show or reschedule question puts Akshay in Waiting on for this recording.
   - Zoya leaves the step and reports the hold.
   - If the time passes, expiry clears it.
   - **Pass.**
6. **Stale draft id.** The event moved and a new draft id exists, but Akshay's ok names the old one. Zoya treats it as superseded: deletes the old draft, sends nothing. **Pass.**
7. **Acknowledgement after a no.** Sponsored no, then our "thanks Priya" acknowledgement. The acknowledgement is not the close note, so the close note goes once and is logged with its message id. **Pass.**
8. **Akshay already answered by hand.** Sponsored no, then Akshay writes "understood, all the best, let's stay in touch". That is his substantive reply settling it.
   - No close note.
   - Status They declined; the chase is removed; the row is recorded.
   - **Pass.**
9. **Old failure.** A sponsored-no Activity from 2 Oct, with the row still at Sponsored offered.
   - Eligible. Zoya re-reads the message, confirms the no, and runs the branch.
   - With 25 such rows, 10 a run, oldest first: done in 3 runs, none dropped.
   - **Pass.**
10. **Unrelated ask on the row.** Sponsored no while Akshay holds "call Ananya" on the row.
    - Only the sponsored chase and the close-note step go.
    - "Akshay: call Ananya" and Akshay in Waiting on stay.
    - **Pass.**
11. **Close note can't go.** It fails on the daily cap.
    - Status They declined; Waiting on Zoya with "Zoya: send Akshay's sponsored close note to <name> (not sent: cap)".
    - Never logged as sent. No nurture mail.
    - **Pass.**
12. **Proposed mail.** An FT decline sent from the wording page leaves Proposed mail empty. A sponsored offer from the Templates row "Sponsored offer (FT)" sets it. **Pass.**
13. **Two decisions in a day.** Tier Sponsored at 10:00, then Your call "precall" at 15:00. The 10:00 section is retitled superseded; only the precall invite goes. **Pass.** This is unchanged from the reviewed text.
