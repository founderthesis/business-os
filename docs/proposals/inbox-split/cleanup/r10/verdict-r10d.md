# Cleanup verdict: capture r10d and actions r10d (c80a282), 2 Nov ~22:55 JST

The replay is in `replay-r10d-cleanup.json`.

**Capture r10d: accepted.** `r10/capture.txt`, **43,475 / 82004b7ce0da42d7**.

**Actions r10d: accepted with three REPAIR guards added.** Deploy `cleanup/r10/actions-r10d-cleanup.txt`, **43,955 / 4ac5406dd5d25bbf**. That's r10d plus one inserted passage (`cleanup/r10/fix_r10d.py`), built twice, byte-identical, with no em-dashes.

The decision 443 and 444 changes (r9e, B3) are reviewed here: no blocker.

**Deploy order:**
1. Actions first (on its own it's safe with live capture r8h: no recovered rows exist yet, so REPAIR sits idle).
2. Then capture r10d.

Doing both in one window between runs is fine, as long as actions lands first.

## Rebuild

`r10/patch.py r8h/capture.txt r9/actions.txt <out>`, run twice, reproduces capture **43,475 / 82004b7ce0da42d7** and actions **43,621 / 97190a21b962a5fc** byte for byte. Neither has em-dashes.

## Blockers in actions r10d (fixed by the added passage)

**B1. The Status guard went missing.**
- r8e's REPAIR said "never undo a newer Your call, Status or decision". r10d keeps only "never write Waiting on, Next action or Next date over a value set after this mail".
- HARD RULES still let Status move "to ... a closed outcome".
- **Failure:** a recovered 29 Oct "we'll pass" closes a row Akshay re-opened to Booking on 31 Oct.

**B2. "Set after this mail" can't always be told.**
- Notion shows no edit time per field. A hand edit with no Claude note line looks undated, so stale mail would overwrite it.

**B3. Stale mail can cancel an invite.**
- REPAIR covers STEP 6e, which includes the invite cancel. A recovered "please cancel" from 29 Oct could cancel an event that has since been rebooked, and every attendee is told.
- Cancelling or moving an event with guests is ask-first under CLAUDE.md. Decision 398's exception is a current written cancel, not a 3-day-old one recovered later.

**The fix,** inserted after "as STEP 3 says." in REPAIR:

> A value whose set date can't be shown older than this mail counts as newer. Never change Status, Tier or Your call, or undo a decision, set after this mail (a closed outcome on a row moved since goes to Akshay's list instead). Never cancel an invite or delete a draft from a recovered mail (a cancel still due goes to Akshay's list).

## What holds

**Decisions 443 and 444 (r9e):**
- 443 is authorised: it's the fourth case added to decision 81.
- 444's "Recommend: ... ok, not ok" is a real decision, so it fits decision 325.
- 444's block clears through Your call, or through Akshay's own mail (STEP 2b).
- Neither adds a send path, and neither changes the cursor.

**REPAIR:**
- A call already booked, a decline overtaken since, and an open question handed over as a dated step all pass.
- No Next date or call date already past is ever set.
- There's no WhatsApp path from a recovered row.
- The 3-try limit stops any loop.

**Capture should-fix 1 to 7** are all in the text:
1. no STEP 0 row after "minute 12 of the run";
2. 0A "nor after minute 10";
3. "at most one per JST day";
4. "an id that no longer resolves included" counts as a strike;
5. "MSGID FIND as KEY defines it";
6. STEP 6 never catches up a "recovered" row;
7. a Meeting row reads its mail for the Doc id first.

## Should-fix (follow-ups)

1. **443 can queue slots after the question is settled.** It doesn't check whether our side already answered or whether a call is booked for that date, so "confirming our 4 Nov call" still queues a slots step. **Fix:** apply 443 only when no message from our side follows the request and no call with them is on the calendar for that date.
2. **443's Next date reaches further than Akshay agreed.** The prompt says "replacing any Next date but a calendar booking's"; decision 443 says "replacing any chase date". **Fix:** limit it to chase, nurture and hold dates.
3. **C1 gives decision 444 a Next date write** that STEP 3 and decision 81 don't allow. **Fix:** the Next date part is 443 only.
4. **C3's past-date step may lose its "Zoya: reply to <who>:" prefix** (decision 223). **Fix:** write the full segment in both places.
5. **"Their later reply" overtakes too easily.** **Fix:** "their later reply that answers, withdraws or restates it".
6. **444's block has no clear end.** **Fix:** it lasts "while that 'Akshay: <who> wrote again' segment stands". The HARD RULES re-open exception should also cover Akshay's own mail, not only "Akshay's ok".
7. **443 can stack two slot steps.** **Fix:** "never a second" slot step for the same person.
8. **REPAIR's try counter counts old tries.** **Fix:** count only tries after the last "link:" line.
9. **Recovered rows are found through the stamped: list.** **Fix:** find them by their own "link: <run id> recovered" line.
10. **The README** says "actions r10c goes live"; the build is r10d.

Nothing deployed by Cleanup.
