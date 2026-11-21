# Zoya r13: decision 449, SLOW becomes its own task (3 Nov)

Built on r12d (recording links, 445 to 448 included) with `build_one.patch`, applied to `routines/zoya/build_one.py` at f70901f in a worktree, plus two new parts: slowtask-intro and slowtask-load.

**Command:** `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin ba3e8aa2a637bc56737fe6c4b875521f54fd2c4e`. Built twice, byte-identical, no em dashes.

| File | Task | Bytes / sha256 |
|---|---|---|
| `zoya-one.txt` | A: Zoya, hourly :38 (the current trigger) | 50,809 / ca541881f4a059ea |
| `zoya-slow.txt` | B: **new** Zoya SLOW task, 11:08 and 17:08 JST, Mon to Fri | 11,260 / 3f9f2e22ee7ce129 |
| `zoya-slow-work.txt` | The pinned SLOW file B loads | 72,411 / 3a612b90498c8e81 (72,407 characters), at ba3e8aa |
| r13 (replaced, `replay.json`) | | A 50,675 / 99b244b6; B 11,027 / 42863ae7; file 70,737 / aa59b79a at ab10765 |

## Why B loads a pinned file

The SLOW file alone is 72.4k, over the 65,536-byte cap, so it can't be inlined. It stays pinned, and B is small: intro, TOOLS, LOCK, RUN RECORD, SLOW FILE and HARD RULES. The shared text the CTO listed (RULES LOAD with the follow-ups page and its routine pages required, ACTIONS, SENDING, LIMITS) is in the file, from the same `build_one.py` parts, so there's still one source. B's prompt can't skip the file:
- **Order:** it loads it right after the run record, before any other read.
- **Check:** the sha must match; then it reads it in python, in 20,000-character slices, to the end, and logs "slow file: <read> of <total> characters, sha <16>".
- **Fails closed:** a short read sends nothing and ends Failed, "slow file not loaded".
- **Excuses:** size, row counts and a guessed time never count as reasons to stop. Only the measured minute 22, a cap or a tool error does. The 16:38 run's excuse ("not enough of the run to read the slow-work file... 100+ rows") is named in that rule.

B's LOCK is FAST's (only the Skipped summary differs), and its HARD RULES are the SLOW file's. Its run records are "Run zoya-slow ...", Source ID run:zoya-slow:<run id>, and its LOCK-skip record is "Run zoya-slow <start> JST: Skipped: lock held by ...". The Activities data source id is in B, because the run record is written before the file is loaded.

## A: FAST-only

- The SLOW WORK pointer is gone, and the intro says no run of this task does SLOW work. FAST no longer depends on the pin.
- Everything in r12d's FAST stays: STEP 0r, 446, 447 and 448.
- The queue line now says "leave them to the Zoya SLOW task".
- **Shared:** ACTIONS' Sent reconcile now counts both tasks' run records (run:zoya: and run:zoya-slow:) as runs that took the lock.

## The SLOW file: SLOW ORDER and SLOW BATCH (decision 449)

- **Time:** before each item, check `date -u`. No new item starts after minute 22, measured, so the lock is free before :38. Nothing else ends the work early.
- **1/ Eligible:** every SLOW action due today or overdue, with its key, due date and row, logged as "eligible:".
- **2/ Selected:** a fixed batch of 15, in this order:
  1. recording logistics within 7 days (prep note, recording link, day-before note);
  2. payments, invoices and billing asks;
  3. commitments with a promised date;
  4. sponsored revenue follow-ups;
  5. the oldest due.
  
  Carryover keys from the newest run:zoya-slow: record go first within their class; a key that's no longer eligible is dropped and logged. Logged as "selected:".
- **3/ Outcomes:** each item gets one line: "sent <Message-ID> | completed by match | held <why> | blocked <why; next owner> | deferred (cap | minute 22 | tool error)". A hold or a one-group limit (nurture's 10, the per-person gap) is that item's held line and never stops the batch. The daily cap is shared with the hourly task, counted as today (JST).
- **4/ End:**
  - Every selected item with no sent, completed, held or blocked line goes under "carryover:" and stays due.
  - Items without an outcome before minute 22, with no tool error or cap: Failed, "early exit at minute <n>, <k> of <selected> without outcome", and they're carried over anyway.
  - A cap or minute 22 with items deferred: Partial. Everything settled: Completed.
- **First lines of the record:** "eligible <n>, oldest due <date> (<row>), selected <n>, outcomes <counts>, remaining <n>", then the "slow file:" and RULES LOAD lines.
- The SLOW REPORT follows these lines. The old 40-minute rule, the 2 Nov batch, and "after the FAST report" are gone.

## Deploy (CTO; atomic, A first)

1. **Move the pin** to ba3e8aa2a637bc56737fe6c4b875521f54fd2c4e and read the file's sha256 back (3a612b90).
2. **Notion edits:** the r12d list (Rules for Zoya, Client show mails, Controls section 8, the Recording link toggle, the zencastr link clause).
3. **Paste A** into the hourly Zoya trigger and byte-compare.
4. **Create B:** cron `CRON_TZ=Asia/Tokyo 8 11,17 * * 1-5`, on the same environment, repo and model as the Zoya task (Sonnet, per 449). Byte-compare its prompt.
5. Paste actions r11b and capture r12b with the rest of the r12d set.

## Risks to confirm

- **The lock overlap.** A 10:38 or 16:38 FAST run that's still working at :08 holds the lock. B then writes "Skipped: lock held" and that slot does no SLOW work. FAST stops starting rows at 25 minutes, so it usually ends by about :05 to :10. Check its measured durations after the first runs. If skips happen, B could retry the lock fetch for up to 5 minutes before skipping. That's not built: the ask was "skip on held".
- **STEP 0 items are in the batch.** Feedback, bounces, vendor forms, owner mail and the scorecard now count toward the 15 by age, class 5. Fixed-date ones (the Monday scorecard, owner mail) aren't a class of their own. Say if they should run outside the batch.
- **Deferred outcomes.** The CTO listed only "deferred (cap)". r13 adds "minute 22" and "tool error" as reasons, so every stop has an outcome.

## r13b: replay fixes (`replay.json`)

The r13 replay failed. Its 6 must-fixes and 4 minor fixes are all applied, using its exact old and new text:

| Defect | What it was | The fix |
|---|---|---|
| D1 (high) | Batch class 1 named the prep note, recording link and day-before note, but those are FAST-only mails | Class 1 is now SLOW items for a precall or recording in the next 7 days, plus release mails 1 and 2. The FAST-only mails are never selected here; one that's due goes in the report |
| D2 (high) | Carryover came from the newest SLOW record, even a Skipped one, a file failure or a crash | Carryover now comes from the newest record that has a "selected:" line. A record stuck at Started gives its selected keys that have no outcome. "eligible:" and "selected:" are written to this run's record before any item is worked |
| D4 (high) | "held <why>" and "blocked <why>" took any text, so a run could quit early and still end Completed | A held line names a real hold and a recheck date. A blocked line names a missing fact or someone else's decision, plus the next owner. A deferral names the cap, minute 22, or the tool and its error. Time, size, context or the number due never counts as an outcome |
| D5 | STEP 2 ("every due row ends the run...") and LIMITS (the due list until empty, its own order) contradicted the batch | Both now point to the selected batch and SLOW BATCH's order. An unselected row just stays due |
| D6 | STEP 0 items had no keys, so carryover couldn't match them, and owner mail and the scorecard could starve | Keys are defined for feedback, vendor forms, edit notes, owner mail and the scorecard. Today's owner mail and the Monday scorecard are class 3. The bounce scan runs first, outside the batch |
| D7 | A model could print all the slices in one call, get output saved to a file, and still log a full read | One slice per Bash call, each ending with an "END <offset> OF <length>" line; a cut or saved output gets printed again. B states the total, 72,407 characters. **The same per-call rule is now in the shared RULES LOAD, so A changes too** |
| D3 | r12d's elapsed line had been dropped | "elapsed <n> min" is back in the first line |
| D8 | The file said it's read "right after LOCK" | It's read right after the prompt's SLOW FILE load |
| D9 | The end status was undefined for some cases | Eligible 0 is No-op. A cap, minute 22, a tool error or a RULES LOAD failure is Partial |
| D10 | This hand-off misdescribed B's HARD RULES | Corrected above |

Built twice, byte-identical, with no em dashes. All three files changed, and the pin is now ba3e8aa. These fixes haven't been replayed again, because they're the replay's own exact text.

**Risks no text fixes:**
- A FAST run still going at :08 makes B skip that slot.
- A run that dies holding the lock blocks both tasks until the runbook frees it.
- Sonnet's context load (the 72k file plus every rules page) hasn't been measured. Record tokens on the first runs, as decision 449 asks.

**Status:** ready for Cleanup with the r12d set. Ship A and B together, A first. Nothing is deployed, and the pin ref hasn't moved.
