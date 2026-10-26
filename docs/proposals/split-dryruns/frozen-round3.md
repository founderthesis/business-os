# Frozen round 3, lock tests and the 411 to 413 scenarios (26 Oct)

Two independent offline runs, A and B. Nothing was sent or written.

**Inputs:**
- Prompts: FAST 96c11beae7ec325b and SLOW a5b4ef40cfd85bb1, the build frozen at 8e64140.
- Snapshot: 3537b3e5c7ca55de.
- Migration: d837edb33231084f.
- Scenarios: round3/scenarios.json (0f0c685078a88035). D's offer date is now pinned to 13 Oct.

Both runs' outputs are in round3/.

| Scenario | A | B | Agree on outcome |
|---|---|---|---|
| C contact holds | PASS | PASS | Yes: Ronit sent, step 2 dated 2 Nov; Vijay held to 3 Nov; Amit and Devesh not due |
| G same minute, sponsored yes | PASS | FAIL | Yes: FAST holds by the tie-break and sends "Sponsored yes: next steps"; SLOW waits, then finds nothing due |
| H overlap | PASS | PASS | Yes: SLOW's 10:08 record holds at 10:38; FAST has nothing to write and ends No-op |
| D cap (offer date pinned) | PASS | PASS | Yes: 40 sent oldest first, 5 left due, Partial |
| E several asks | FAIL | FAIL | Yes: the fail is the same |
| L1 same-second acquire | PASS | PASS | Yes: FAST holds; SLOW only reads, then runs |
| L2 crashed holder | PASS | PASS | Yes: at 48 minutes held, so FAST waits 10 and ends Partial; at 68 minutes stale, so FAST runs |
| L3 wait/skip leaves work due | PASS | PASS | Yes: FAST writes only its run record; the reply stays due with Next date and owner unchanged |
| L4 FAST 10:38 still running at 10:50 | PASS | PASS | Yes: SLOW waits until FAST completes at 11:02, then runs; no row has two writers |
| R1 thank-you after the transcript (412) | PASS | PASS | Yes: a standalone new mail in ad@, To the guest, Cc the PR, stakeholders and house copies, no attachment, "(draft ready)" |
| R2 recording unclear (411) | PASS | PASS | Yes: Akshay's queue ask on the row; never the PR, never WhatsApp |
| R3 recipients (413) | PASS | PASS | Yes: To Sreya; Cc Akshay, Mamatha, Rajmohan, Santhosh, Mala |

The field-by-field match is by reading, not by string. The two runs wrote free text in different shapes, such as one row per D row or a range.

## Findings, all fixed in d-split26m

1. **E (both runs).** One inbound carried a sponsored yes and a crew-cost question. The yes got its answer. The crew-cost question went to Akshay with no acknowledgement, because "the real answer goes on it this run" cancelled the holding reply. Fix: the holding line rides inside the answer mail. The Akshay ask keeps its own reply segment beside his "Ask Akshay" one.
2. **G (run A).** "A message on a row that waits on Akshay" read literally sent the yes to Akshay, because he had an unrelated travel step on the row. Fix: it is the ask that waits on him, not the row.
3. **R3 (both).** The read-back named the inbound's To and Cc. That leaves out the sender and includes our own address. Fix: its From, To and Cc, less our own address.
4. **L1 (both).** A residual same-minute race. A run that read before the other's Started record existed would go ahead, and so would the other run by the tie-break. Fix: a second read 1 minute later, before the first row write.
5. **R1 (both).** No branch for a recording with no Episode yet. Fix: the row stays Doing with a note, and the next run retries once the calendar's STEP 4e creates the Episode. "The row" in c(4) now says the guest row.
6. **R2 (both).** A PR question about a recording whose status is open added a second Akshay ask for the same fact. Fix: it waits on his answer.
7. **R1, R2, E (both).** Next date was undefined when no open segment names a date. Fix: a segment's date is the date its text gives, else its key's, else the day it was written.
8. **D (both).** After a late step 1, step 2 was dated in the past (offer plus 14 days is today). The next run re-selected all 40 rows only to hold them. Fix: the next step is never dated before the first day the 7-day rule allows.

## Not fixed here, for the CTO

- **G (run B): no Status is named after a mailed sponsored yes.** Rules for Zoya page 1 says "the sequence stops (decision 227)", but neither the live prompt nor the build names a Status. If the row stays Sponsored offered, routine 1 can select it again on its Next date, and only the CONTEXT CHECK stops a chase after a yes. This is not new in the split. Booking would close it, but that is a rule change, so it is not decided here.
- **Lease timing.** SLOW can hold the lease until its run ends, up to 60 minutes. FAST waits only 10. So a reply can slip one FAST run, about an hour, when SLOW runs long. L3 shows the work stays due and nothing is lost. Correct, but slow.
- **A crashed run record stays Started.** It ages out of the lease at 60 minutes, but the good-morning check will show it as Started until a person or a later run marks it.

## Re-freeze

d-split26m changes behaviour, so the frozen hashes move:
- FAST 36,811 / 1b4cca2a0d0b284e.
- SLOW 63,845 / 94943a20df0745dd. That is 1,491 B under the cap less 200.

Built on Cleanup's d-split26l-fix (1303cea: never Mamatha; the read-back excludes Mamatha and, on un#, Sri). Both reproduce from 1303cea in a clean worktree. Cleanup's fix alone gave FAST 36,211 / f4a541d352980139 and SLOW 63,099 / 33ecf7c33c68d0ce; round 3 ran on 8e64140, so its R3 expected Mamatha kept. Round 3b expects her dropped. Inbox, calendar and sweep are unchanged.

Tests repeated on the new build: all twelve scenarios (round 3b). The lease text changed, so every run is affected.

Not repeated, because the parts they read did not change (ACTIONS' Sent check, MESSAGE IDENTITY): the crash A and crash B recoveries.
