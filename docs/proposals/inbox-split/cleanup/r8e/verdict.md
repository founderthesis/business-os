# Cleanup verdict: r8e (6ae4a87), 2 Nov ~13:35 JST

Changed cases only, as asked.

**Accepted. No blocker, so deploy as built:**
- capture: `r8e/capture.txt`, **40,447 / c0abafcd8755c77b**;
- actions: `r8e/actions.txt`, **39,935 / 1d483cbdc43a58ba**.

Two should-fix items are follow-ups, not reasons to hold.

## Rebuild

`r8e/patch.py r8/capture.txt r7/actions-v2.txt <out>`, run twice, reproduces both files byte for byte.
- The inputs are Main's r8d (`r8/capture.txt`, 5ef8b937, built on the live r7 at 3f08b76e) and the live actions r7 (c80b1cee).
- The patch makes 3 edits and asserts each one. No em-dashes are added, and both files are under the cap.

## Cases

| Case | Result | Deciding text |
|---|---|---|
| Same-day unlinked mail | OK, by design | LINK takes rows "Captured before today or created before 2026-11-02T03:00Z". Today's later mail is linked when it's captured, or by LINK the next day. LINK runs through 2026-11-05. |
| The 13 stranded rows | OK | The second branch takes them once. The "link:" line plus Captured today take them out of the query afterwards. Rows that end "internal" or linked gain People or an Engagement, so they fall out of "no People and no Engagement" too. |
| Done but unmatched mail (Team Nxt, 40c19a30...fd22) | OK | LINK links the row and puts its id on "stamped:". Actions' REPAIR then takes "a stamped row with a "link:" line after its last "actions: done"". It reads the thread in both inboxes, the newest Activities, Sent and Action keys first. Its new "actions: done" ends the repair, so it can't loop. |
| One RAW failure, then a good message | OK, unchanged | A RAW failure "pends and the run goes on". |
| Repeat pitch | OK, with should-fix 1 | "except STEP 3's repeat-pitch bullet, applied in full". |
| An existing row that has moved on | OK | "found rows keep Status, Waiting on, Next action and later decisions". REPAIR "never undo a newer Your call, Status or decision". |
| Identity and dedupe on a repeat | OK | LINK goes "by key". A new Person or Engagement needs "verified identity", and STEP 3's 424 rules apply. Old rows still fold before any re-key. |
| No resend of the five sponsored offers (22:40 JST, 1 Nov) | OK | They're "Zoya sent:" Email out rows, which LINK excludes ("not an Email out whose Summary starts "Zoya""). REPAIR adds "never resend what went", and Zoya's action keys still dedupe her sends. |

## Should-fix (follow-ups)

1. **A stale repeat pitch can reach Akshay's list.**
   - The repeat-pitch bullet, applied in full to an old message, can put a pitch on his list that he has already answered. Team Nxt's 31 Oct cold ask had Akshay's replies on 31 Oct and 1 Nov.
   - It's noise on his decision inbox (decision 325), not a wrong action.
   - **Fix:** apply the bullet only if no mail from our side on that thread is newer than the pitch.
2. **A crash after linking can lose a repair.**
   - LINK links the row first and lists its id on "stamped:" after. A crash between the two leaves the row linked but never repaired, because REPAIR needs a stamped row.
   - Rare.
   - **Fix:** write the id to "stamped:" first, then link and add the "link:" line, as the earlier stamp rule (V2) does.

Nothing deployed by Cleanup.
