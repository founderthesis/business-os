# Zoya r13: decision 449, SLOW becomes its own task (3 Nov)

Built on r12d (recording links, 445 to 448 included) with `build_one.patch`, applied to `routines/zoya/build_one.py` at f70901f in a worktree, plus two new parts: slowtask-intro and slowtask-load.

**Command:** `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin ab107654e5af4db90c085f3545fe3d5cbfa891ae`. Built twice, byte-identical, no em dashes.

| File | Task | Bytes / sha256 |
|---|---|---|
| `zoya-one.txt` | A: Zoya, hourly :38 (the current trigger) | 50,675 / 99b244b6569a40b8 |
| `zoya-slow.txt` | B: **new** Zoya SLOW task, 11:08 and 17:08 JST, Mon to Fri | 11,027 / 42863ae7f3f52237 |
| `zoya-slow-work.txt` | The pinned SLOW file B loads | 70,737 / aa59b79a1784f959, at ab10765 |

## Why B loads a pinned file

The SLOW file alone is 70.7k, over the 65,536-byte cap, so it can't be inlined. It stays pinned, and B is small: intro, TOOLS, LOCK, RUN RECORD, SLOW FILE and HARD RULES. The shared text the CTO listed (RULES LOAD with the follow-ups page and its routine pages required, ACTIONS, SENDING, LIMITS) is in the file, from the same `build_one.py` parts, so there's still one source. B's prompt can't skip the file:
- **Order:** it loads it right after the run record, before any other read.
- **Check:** the sha must match; then it reads it in python, in 20,000-character slices, to the end, and logs "slow file: <read> of <total> characters, sha <16>".
- **Fails closed:** a short read sends nothing and ends Failed, "slow file not loaded".
- **Excuses:** size, row counts and a guessed time never count as reasons to stop. Only the measured minute 22, a cap or a tool error does. The 16:38 run's excuse ("not enough of the run to read the slow-work file... 100+ rows") is named in that rule.

B's HARD RULES and LOCK are the same text as FAST's. Its run records are "Run zoya-slow ...", Source ID run:zoya-slow:<run id>, and its LOCK-skip record is "Run zoya-slow <start> JST: Skipped: lock held by ...". The Activities data source id is in B, because the run record is written before the file is loaded.

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

1. **Move the pin** to ab107654e5af4db90c085f3545fe3d5cbfa891ae and read the file's sha256 back (aa59b79a).
2. **Notion edits:** the r12d list (Rules for Zoya, Client show mails, Controls section 8, the Recording link toggle, the zencastr link clause).
3. **Paste A** into the hourly Zoya trigger and byte-compare.
4. **Create B:** cron `CRON_TZ=Asia/Tokyo 8 11,17 * * 1-5`, on the same environment, repo and model as the Zoya task (Sonnet, per 449). Byte-compare its prompt.
5. Paste actions r11b and capture r12b with the rest of the r12d set.

## Risks to confirm

- **The lock overlap.** A 10:38 or 16:38 FAST run that's still working at :08 holds the lock. B then writes "Skipped: lock held" and that slot does no SLOW work. FAST stops starting rows at 25 minutes, so it usually ends by about :05 to :10. Check its measured durations after the first runs. If skips happen, B could retry the lock fetch for up to 5 minutes before skipping. That's not built: the ask was "skip on held".
- **STEP 0 items are in the batch.** Feedback, bounces, vendor forms, owner mail and the scorecard now count toward the 15 by age, class 5. Fixed-date ones (the Monday scorecard, owner mail) aren't a class of their own. Say if they should run outside the batch.
- **Deferred outcomes.** The CTO listed only "deferred (cap)". r13 adds "minute 22" and "tool error" as reasons, so every stop has an outcome.

**Status:** built. Replay pending. Nothing is deployed, and the pin ref hasn't moved.
