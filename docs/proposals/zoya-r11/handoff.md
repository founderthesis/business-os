# Zoya r11: rules loaded to the end before any send, and Cleanup's SLOW should-fix (3 Nov)

| File | Bytes / sha256 | Where |
|---|---|---|
| SLOW work file | 67,837 / 2cf5b7156ce80240 | `routines/zoya/release/zoya-slow-work.txt` at commit 63fcf669014fe5c4eeff64c7fedbe6d1c85d926c |
| FAST prompt | 44,839 / 264f69fc3ae384c2 | `zoya-one.txt` here, pinned to 63fcf66 |

**How it's built:**
- On a worktree at f70901f with this folder's `build_one.patch`, which carries everything since the rules-read patch.
- Command: `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 63fcf669014fe5c4eeff64c7fedbe6d1c85d926c`. Built twice, byte-identical.
- **What changed against the live FAST** (44,075 / a6109709): only the edits below, the pin and hash, and the version string.

## The bug (Auditor finding 1, CX-20261103T0800)

The 07:38 run read about 21k of the wording page's 62k characters. It then sent 3 mails, saying "the templates were in the first slice". The 23:38 run blocked correctly on an incomplete read, so the rule was being applied unevenly.

## What changes (FAST and SLOW, shared text)

- **RULES LOAD** replaces "read each page in full". Every required page is read in full every run. A fetch saved to a file is read to its end in Bash or python, slice after slice, never stopped at the part a step needs. Then the run logs "<page>: <read> of <total> characters", both counts taken from the file itself. A page whose read is short of its total is not loaded.
- **PRE-SEND check 1** reads that state. Any required page short or unread means no send that uses wording or rules, with no "the part I need was loaded" exception. Each such action is blocked and named in the report as "rules not loaded: <page> <read> of <total>".
- **Required pages:** the list isn't narrowed.
- **The morning's 3 mails:** nothing resends them. ACTIONS' key and Sent check are unchanged.

## Cleanup's SLOW should-fix (from `../zoya-slow-r10/next-slow-build.md`)

1. Carryover goes first within STEP 2, after STEP 0, 1b and team work. A carried key not in this run's eligible list is dropped.
2. "A tool error" means a call that fails after one retry. It stops only the work that needs that tool, and a failed PRE-SEND check blocks that item only.
3. The read-back exclusion now names the Built to Share and Human by Design host alongside Sri, unless they wrote on the thread.
4. FAST's LIMITS says "Everything FAST work sends", so it never relaxes SLOW sends.
5. Snooze key: "snooze:<row id>:<YYYY-MM-DD>:<segment n>".
6. The watch of the first SLOW run is the CTO's, not a build item.

## Deploy (the CTO), in this order

1. Move refs/heads/zoya-slow-pin to 63fcf669014fe5c4eeff64c7fedbe6d1c85d926c and read the file's sha256 back.
2. Paste `zoya-one.txt` into the Zoya trigger and byte-compare it.
3. The next run's record has one "<page>: <read> of <total> characters" line per required page. A short page blocks its sends.

## r11b (replay.json)

The first replay passed the CTO's required case: a 21k-of-62k read blocks every send and nothing goes. It also passed the no-resend case. Fixes for what it found:

| Defect | Fix |
|---|---|
| D1, high: a fully blocked run read as Completed | A short page ends the run Partial, "rules not loaded: <page> <read> of <total>", whatever RUN RECORD says of blocked actions. It writes nothing for the actions that page governs |
| D2, D5: SLOW-only pages | The follow-ups page and the routine pages it links are SLOW work's only. FAST sends never wait on them, and SLOW sends do |
| D3: inline fetches | A fetch shown inline in full is loaded, with read = total = its length |
| D4: counts that could never match | A saved file is loaded in python as one string (its text field when it's JSON) and printed in slices of at most 20,000 characters, in order, to the end. Total is the string's length, and read is the end of the last slice shown in full |
| D6 | Snooze key: "snooze:<row id>:<YYYY-MM-DD>:<the first 20 characters of its ask>" |
| D7 | A dropped carryover key is logged as "dropped: <key> (not eligible)" |
| D8 | The page counts go in the run record |
| D9: pin precondition | The pin is still at 8bf34ea. Move it to 63fcf669014fe5c4eeff64c7fedbe6d1c85d926c before FAST goes live (deploy step 1) |

**Also in SLOW:** the line listing "Rules for Zoya: follow-ups", which the live SLOW file never had.

**Status:** written. Re-replay pending.
