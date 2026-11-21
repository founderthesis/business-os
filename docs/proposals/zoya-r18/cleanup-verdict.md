# Cleanup verdict: Zoya r18 (513d32c, 98a9c36), 4 Nov ~15:55 JST

This covers the SLOW file, the SLOW task and the hourly prompt for the 17:08 run.

**Accepted. No blocker.** The stopgap rule isn't needed.

| File | Bytes / sha256 |
|---|---|
| SLOW file at 513d32cb0a754dc381a4092dcb9d43f5732225c8 | 81,459 / a3335c1abd10b006 |
| SLOW task `zoya-slow.txt` | 12,985 / 3378858b38b24c0b |
| Hourly `zoya-one.txt` | 54,773 / 1a437c41c7a74d43 |

`zoya-episodes.txt` (45,279 / 3547a1dc) is a **new task, not reviewed here.** It needs its own review before it's enabled.

## Rebuild

- A worktree at f70901f with `zoya-r18/build_one.patch`, then `build_one.py ... 513d32c`, twice. All four files are byte-identical to the repo, and the SLOW file equals `git show 513d32c:...`.
- There are no em-dashes.
- The live pin is b732cb3, and 513d32c descends from it.

## The CTO's four must-haves (SLOW file line numbers)

1. **Bare loop-in (line 64).** The text reads: "Nothing else (CTO, 4 Nov, clarifying decision 421): no chase, offer, sponsored ask or reminder of ours and no restated ask; a chase goes from your own inbox after the loop-in, as its own action."
2. **Recipients asserted in code (line 145, PRE-SEND 2/).**
   - To and Cc are "built ... before the draft and checked in a Bash python step, never by eye":
     - To isn't empty;
     - ad@ and every team address are never in To;
     - every intended outside address is in To or Cc.
   - "a failed assert: send nothing, the action blocked 'recipients: <what failed>'".
   - The loop-in path (line 64) is "always the draft way, never email_compose reply's own addressing ... draft update to set To and Cc, read it back, draft send", with "ad@thepodium.in never in To or Cc".
3. **Selection order (line 83):**
   1. recording logistics within 7 days;
   2. "payments, invoices and billing (every STEP 1b step ...) and dated commitments";
   3. STEP 0 items, edit notes, internal tasks and snoozes;
   4. follow-ups.
4. **Every category gets an outcome, and writes are checked in code.**
   - Line 84: "one line per work category ... checked <n> | not due | blocked <why>; <owner> | unfinished <why>", for STEP 0a to 0g, 1b, edit notes, internal tasks, snoozes, follow-ups and nurture.
   - A completed line carries "act: ... note: <row id> <date> key: ...", from a read-back.
   - Line 85: the python "checks each completed line's act:, note: and key: (a loop-in's key matches ^loopin:<Message-ID>$ ...; a miss: that item is unfinished)", plus "category missing" means Partial.

## My r16 blockers: closed (line 54)

- **B1:** a file only from Mamatha, matched to a recording whose date has passed, "never a precall's". Decision 374's test runs "Before attaching anything", and "never replace" an existing file.
- **B2:** the key `transcript-file:<Message-ID>:<file name>`, done when the Episode's sha matches.
- **B3 (hourly line 80):** the exact old-to-new zencastr URL swap, "nothing else touched", with "done" tested per guest and event.
- **Also in:** the 14:01 addendum's UTF-8 bodies, and the "AD Tasks" rename.

## Should-fix (low)

- **The note: evidence is self-reported.** The python checks that act:, note: and key: are present and well-formed, but it can't fetch Notion. So "note:" is the model's own read-back. That's still a real improvement, and it catches a missing line, but it isn't proof. Spot-check the first 17:08 completed items against their rows.
- **A leftover phrase.** The loop-in line still says idempotency "only on the call that sends (email_compose or draft send)". Drop "email_compose" so nothing invites the old path.
- **CTO decision rows:** log two of them, the 421 clarification and the 445 replace-on-correction rule.
- **Ranjita still appears** in the Rules for Zoya wording (calendar 454c and sweep 3i are now fixed, per 4c33f11).

## Deploy order for 17:08

1. Move the pin to 513d32c and read back a3335c1a.
2. Paste the SLOW task (3378858b) and byte-compare it.
3. Paste the hourly prompt (1a437c41) in the same window, because it shares the loop-in and recipient fixes.

Nothing deployed by Cleanup.
