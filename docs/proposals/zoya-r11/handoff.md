# Zoya r11: rules loaded to the end before any send, and Cleanup's SLOW should-fix (3 Nov)

| File | Bytes / sha256 | Where |
|---|---|---|
| SLOW work file | 67,287 / b7f9f96f96aed90f | `routines/zoya/release/zoya-slow-work.txt` at commit 05a2c63b4ecdcd64ad5b6a7907c03b61659b9cc2 |
| FAST prompt | 44,354 / 5e958a83d0ab3530 | `zoya-one.txt` here, pinned to 05a2c63 |

**How it's built:**
- On a worktree at f70901f with this folder's `build_one.patch`, which carries everything since the rules-read patch.
- Command: `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 05a2c63b4ecdcd64ad5b6a7907c03b61659b9cc2`. Built twice, byte-identical.
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

1. Move refs/heads/zoya-slow-pin to 05a2c63b4ecdcd64ad5b6a7907c03b61659b9cc2 and read the file's sha256 back.
2. Paste `zoya-one.txt` into the Zoya trigger and byte-compare it.
3. The next run's record has one "<page>: <read> of <total> characters" line per required page. A short page blocks its sends.

**Status:** written. Replay pending (`replay.json`).
