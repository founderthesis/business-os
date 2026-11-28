# Zoya r14: decision 450, Zoya SLOW on Opus with durable outcomes (3 Nov)

This replaces r13b. It's the r13b structure, with SLOW BATCH rewritten to the decision 450 spec. Apply `build_one.patch` to `routines/zoya/build_one.py` at f70901f, which adds two new parts, slowtask-intro and slowtask-load.

**Command:** `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 2f607f0b30dbc0688feef8f16e4859c9796a8f23`. Built twice, byte-identical, no em dashes.

| File | Task | Bytes / sha256 |
|---|---|---|
| `zoya-one.txt` | A: hourly Zoya (trig_01UPT8LDrBDL5JQqW91Awgbo), FAST only, Sonnet | 50,822 / 677aa3473026e9ef |
| `zoya-slow.txt` | B: **new** "Zoya SLOW", `CRON_TZ=Asia/Tokyo 8 8,11,17 * * 1-5`, Opus | 11,238 / 20cce0904095ec86 |
| `zoya-slow-work.txt` | The pinned SLOW file B loads | 74,785 / 68ec0805f5393c2d (74,781 characters), at 2f607f0 |
| r14 (replaced, `replay.json`) | | B 11,276 / 05466170; file 73,243 / 26b60e7c at 9d1bda1; A unchanged |

## What 450 changes from r13b

- **Runs:** three a day on weekdays, 08:08, 11:08 and 17:08 JST.
- **SELECT FIRST:**
  - Every SLOW obligation due today or overdue is its own item, keyed as ACTIONS says. Two obligations on one row are two items and two outcomes.
  - The bounce scan runs first, outside the batch.
  - The run selects up to 30 items, in order: (1) recording logistics within 7 days, (2) payments, invoices and billing, (3) dated commitments, plus today's owner mail and the Monday scorecard, (4) the oldest eligible follow-ups, then anything else.
  - Carryover goes first within its class.
  - "eligible <n>, oldest <key> due <date>" and "selected: <key>, ..." are saved to the record before any send.
- **Chunks of 10:** after each chunk, the run appends "chunk <n>: <key>=<outcome>, ...". Each outcome is one of:
  - completed <msgid or match>
  - overtaken <what>
  - held <rule> (<what>), recheck <D Mon>
  - blocked <the missing fact or the decision someone else holds>; <next owner>
  - unfinished (<cap | minute 22 | tool error>)
  
  Time, size or the number due is never a hold, a block or a reason. A follow-up inside the Diwali pause is held "Diwali". The caps stay on Cadences (40 a run, and 150 a day shared with FAST, counted from today's Activities).
- **Timing:** no new chunk starts after minute 22 (`date -u`). A run still holding the lock at :38 is fine: FAST skips, as LOCK says. The lock is never taken over.
- **OUTCOME CHECK IN CODE:** a Bash python step diffs the selected keys against the chunk-line outcome keys. Any key with no outcome becomes unfinished and goes to "carryover: ...".
- **Status:**
  - Completed: every key ended completed, overtaken, held or blocked.
  - Partial: some keys are unfinished, all from a cap, minute 22 or a tool error; the reason is named. A RULES LOAD failure is also Partial.
  - Failed: any key is unfinished with none of those reasons, "early exit at minute <n>, <k> of <selected> unfinished". It's never Completed.
  - No-op: eligible is 0.
- **First record lines:** "eligible <n>, oldest <key> due <date>, selected <n>, completed <n>, overtaken <n>, held <n>, blocked <n>, unfinished <n>, remaining eligible <n>, elapsed <n> min". Then a usage line (input, cache read, cache write, output, cost), or "usage: unknown".
- **Kept from r13b:**
  - B loads the file in full, one slice per Bash call with END lines, against a known total.
  - Class 1 never sends FAST's prep note, recording link or day-before note.
  - Carryover comes from the newest record with "selected:".
  - Owner mail and scorecard keys, and the batch-over-due-list fixes.
  - A is FAST-only, with every r12d behaviour.
- **Naming:** the spec's "RECONCILE IN CODE" is named "OUTCOME CHECK IN CODE", because the build refuses the old RECONCILE word (it belonged to the retired lease design).

## Cutover (after Cleanup accepts; see the open question below)

1. Move the pin to 2f607f0b30dbc0688feef8f16e4859c9796a8f23 and read the file's sha256 back (68ec0805).
2. Create B **disabled**: same environment and repo as the hourly task, connectors MCPEmail, Notion, Gmail, Google-Calendar and bluetick. Then update_trigger with the model claude-opus-5-5. Read back the model, cron, connectors and prompt sha (20cce0904095ec86).
3. Fire B by hand once, in a window clear of :38: a dry check that the repo clones, the lock is taken and released, and the connectors load. It does real work within every limit.
4. Paste A into trig_01UPT8LDrBDL5JQqW91Awgbo, and byte-compare it (677aa3473026e9ef).
5. Enable B, then read both back. Record any slot where neither task does SLOW, or both do.
6. The r12d set (actions r11b, capture r12b, and the Notion edits) goes with this window.

**Handover gap to watch:** today's 16:38 hourly run (r12d) still does SLOW, so 17:08 under B would double up only if B is enabled before then. B's first natural run is Wed 08:08. The 07:38 FAST run can hold the lock at 08:08, which would make B skip that slot.

## r14b: replay fixes (`replay.json`: not ready, D1, D2, D3 and D5 must-fix)

| Defect | What it was | The fix |
|---|---|---|
| D1 (high) | The code check split lines on ", " and "=", but outcomes contain ", " and Message-IDs contain "=" | One "S<nn> <key>" line per selected item. Each chunk is a "chunk <n>:" line followed by "S<nn> <outcome>" lines, numbers only. Python reads the record body verbatim through a quoted heredoc. Carryover lines are "S<nn> <key>" |
| D2 (high) | B's RUN RECORD statuses contradicted SLOW BATCH 4/: a stop at minute 22 or a cap read as Failed, and a RULES LOAD failure as Completed | B's status is the one the code check prints. Also Failed: a SLOW FILE failure, or a stop before SLOW BATCH selects |
| D3 | 450 says the daily cap keeps room for FAST, but nothing did | SLOW stops at the daily cap less the FAST reserve on Cadences. With no reserve on Cadences, it stops 30 short and the report says "FAST reserve missing on Cadences". **Akshay or the CTO sets the reserve on Cadences** |
| D4 | The counts and the status were still the model's own words | The same python computes the counts, the first line and the status from `date -u`. "unfinished (minute 22)" under 22 measured minutes, or a tool error with no error text, counts as no reason. Output is copied, never rewritten |
| D5 (dated: the pause starts Fri 6 Nov) | The Diwali hold caught every follow-up, including release mails | Only chases are held (routines 1 to 5, 7 and 8, nurture, revival, PR coordination), recheck the first weekday after. Release mails, invite confirmations, payments, billing, team steps, owner mail and the scorecard go on their dates unless Cadences names them. **Check this against the Cadences Diwali line** |
| D6 | Payment reminders had no key form, so reminder 2 could match reminder 1 | Payment reminders get their own key, "<row>:team:seq-pay<n>-<reminder n>:<due>". Owner-mail items sent on their own get "ownermail:<date>:<row>" |
| D7 | 449 wording was left in the report and AFTER SEND | Both now use the 450 outcome words |

A is unchanged (677aa347). B and the file changed, so the pin is now 2f607f0. Built twice, byte-identical, no em dashes. A short re-replay of the fixes is running (`replay-b.json`).

**Status:** waiting on the re-replay, then Cleanup. Nothing is deployed, and the pin ref hasn't moved.
