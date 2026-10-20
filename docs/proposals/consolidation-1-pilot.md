# Consolidation 1 pilot: sponsored obligations as Kind Task rows (Main 2, 21 Oct)

Builds on docs/proposals/consolidation-1-sponsored-pilot.md (58ef515) under the CTO's design principles (CTO state page, decision 357). For cleanup review. Main deploys the prompt edits. Main 2 is the only Engagements writer for the migration. Nothing here is deployed or migrated yet.

## Failure it prevents, what it removes, what it adds

- **Prevents:** sponsored chases that no routine can pick because the free text has the wrong shape (about 22 of 86 rows on 20 Oct), and deferrals that move a booked call date.
- **Adds:** one select on Engagements, **Obligation** (Sponsored chase, Sponsored next steps, Payment reminder, Payment confirmation), pending the CTO's yes. Plus 10 Kind Task rows and one Zoya paragraph (OBLIGATIONS).
- **Removes (after the pilot passes):** routine 1's Next-date-on-Engagement selector, STEP 1b's Engagement-level steps, and the Next action segment surgery for these obligations. The rollout deletes them in the same week.
- **How we'll know:** the three proofs below, on real runs.

## Prompt edits (docs/proposals/consolidation-1-build.py)

The script checks each base by the sha256 of its prompt block, applies every edit exactly once, and prints the new sizes.

| Routine | Base (live 20 Oct) | After | Edit |
|---|---|---|---|
| Zoya | 49,048 B / 487ebbf6feef8db7 | 51,447 B / 4813ec927f97ba77 (14,089 spare) | YOUR QUEUE: obligation rows are follow-ups, never queue steps. STEP 1b: payment and next-steps work happens on the row. New OBLIGATIONS paragraph before STEP 2. Routine 1: select open Sponsored chase rows, plus Engagements at Sponsored offered with no open chase row (the old path, until rollout). |
| Daily sweep | 35,943 B / b0888b6624e6848f | 36,036 B / b5f4823d67cf56a5 | "Quiet" check: an Engagement with an open obligation row is not quiet because its Next date is empty. |

- **Unchanged:** inbox, calendar, evals, WhatsApp. Evals and calendar already skip Kind Task rows (decision 329). The inbox still writes the Engagement on replies and offers; the obligation row is Zoya's alone.
- **Composition:** the sweep edit touches one sentence of the "Quiet" bullet. Main's prepared sweep STEP 4b (4f28ef4) should not touch that sentence; Main to confirm when composing.

## Model (OBLIGATIONS paragraph, summarised)

- **One row per obligation:** Kind Task, Obligation set, For engagement the guest's Engagement, Source ID "obl:<obligation>:<engagement page id>". The Source ID is the dedupe key only, never a selector.
- **Selection** uses Kind, Obligation, Task state (not Done or On hold) and Next date due. Never Next action text.
- **While a row is open,** Zoya never writes the Engagement's Next date, Chase step or Next action for that obligation. The Engagement's Next date is its booked call only. Status and Payment stay on the Engagement.
- **Same send rules:** every STEP 2 rule applies to the row as if it were the Engagement: GUARD, NURTURE, ONE PERSON, ONE ASK, STALENESS GATE, LIMITS and holds. A hold moves only the row's Next date.
- **Replies and declines:**
  - A reply sets the row to Awaiting someone else.
  - A decline, a no-contact request, or Akshay's decline or park closes every open obligation row of that Engagement in the same run.
  - A declined chase never closes a payment row unless the decline covers it.

## The 10 pilot rows

Exported read-only on 20 Oct, 22:45 JST, to the scratchpad. Planned by migration/c1_plan.py.

| # | Engagement | Show | Obligation row | Row Next date | Hard case |
|---|---|---|---|---|---|
| 1 | Nidhi Shukla @ Girl Rising | FT | Sponsored chase (awaiting Sharon) | the day after the precall | booked precall 5 Nov stays on the Engagement (proof 1) |
| 2 | Sanjiv Bajaj @ BajajCapital | FT | Sponsored chase, step 2 | 26 Oct | Call type Precall: Engagement Next date kept only if the calendar shows a future precall (proof 1) |
| 3 | Sinduri Reddy @ Premia Academy | FT | Sponsored next steps (GST and billing) | 22 Oct | sponsored yes, Payment Not started |
| 4 | Sunith Reddy @ Beforest | FT | Sponsored next steps (billing, precall) | 23 Oct | yes next steps; payment rows only once an invoice exists |
| 5 | Rishwin Devaya @ Riverside Coffee | FT | Sponsored chase, step 3 (both segments) | 27 Oct | two segments, one obligation; proof 2 (Rerun eval) |
| 6 | Ayush Jhawar @ Genefied | FT | Sponsored chase | 25 Oct | PR Dilreen shared with row 7 |
| 7 | Subodh Bhardwaj @ Navaratna | FT | Sponsored chase | 25 Oct | same PR, offer sent 18 Oct (recent send) |
| 8 | Pratiqk Jaani @ Dhrasti Method | FT | Sponsored chase, step 3 owed | 20 Oct | overdue step plus a waiting segment |
| 9 | Andrey Fedorov @ STON.fi | un# | Sponsored chase, step 1 owed | 20 Oct | un# |
| 10 | Matthew Shaw @ OpenWorld | un# | Sponsored chase | 25 Oct | un#, recent send, sibling row (decision 324) |

- **Conservation check:** every one of the 13 Next action segments lands on exactly one Task row (10 rows); 0 stay on the Engagements.
- **After migration, each Engagement has:** Next action empty, Waiting on empty, Chase step empty, and Next date equal to its booked call or empty. Each planned "## Next sponsored mail" moves to the row's page body.
- **Gaps, stated plainly:**
  - No live row has a booked recording with an open payment step. Proof 1 uses booked precalls instead.
  - No sponsored row is snoozed today, so that case isn't in the pilot.
- **Row 4 note:** Sunith's Status is Sponsored offered but the plan reads as a yes. The migration leaves Status alone and puts the next-steps work on the row. Akshay or Zoya settles the Status from the thread.

## Migration procedure (one writer, Main 2)

1. **Re-export** the 10 rows immediately before writing. Stop any row whose Next action or Next date changed since the plan.
2. **Check the calendar** (read only) for rows 1 and 2: is there a future precall event? That decides whether the Engagement keeps its Next date.
3. **Create** the 10 Task rows in one call, then read them back.
4. **Update** the 10 Engagements: Next action, Waiting on, Chase step and Next date per the plan; the moved body sections are replaced by "Planned mail moved to <row>". Read them back.
5. **Re-export** and run c1_plan.py's check against the after state. Any segment not found exactly once rolls that row back. The rollback sets the Task row Done with "rolled back" and restores the Engagement from the export. Nothing is deleted.

Order: Main deploys the Zoya and sweep edits first, then the migration runs. If the migration ran first, Zoya would keep reading the old Engagement fields and the moved steps would go unread.

## The three proofs (on real runs)

1. **A deferral can't move a call date.**
   - On rows 1 and 2, snapshot the Engagement's Next date, Call type and Call link before two Zoya runs and after them. They must be identical.
   - Only the obligation row's Next date and Claude note may change.
2. **An eval can't erase an obligation.**
   - Tick Rerun eval on row 5.
   - After the evals run, the Task row must be unchanged and still linked.
3. **A retry can't duplicate a send.** Pilot evidence is narrower than the proposal's:
   - What the pilot checks: Zoya's existing Sent check before any resend still holds on the row, so the next run finds the mail and writes one Activity.
   - Not in this pilot: the canonical Message-ID upsert. Plain reads don't return the header. Gmail RAW and MCP Emails "original" do, at one extra call per send. It's the next change, sequenced with the inbox's Activity dedupe.

## Rollout (all sponsored rows, after the pilot is accepted)

- **The same planner and procedure,** in batches of 25 with a check after each.
- **One more Zoya sentence:** every in-scope Engagement at Sponsored offered with no open Sponsored chase row gets one, from its thread. That way new offers the inbox makes enter the new model without an inbox change. The inbox has 212 bytes to spare, so this matters.
- **Then delete the old path:** routine 1's Engagement-level selector and the "Zoya: sponsored step" prefix handling in YOUR QUEUE.
