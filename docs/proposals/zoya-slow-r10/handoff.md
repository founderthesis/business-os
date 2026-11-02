# Zoya SLOW r10c and FAST: for Cleanup and the CTO (2 Nov)

| File | Bytes / sha256 | Where |
|---|---|---|
| SLOW work file | 66,305 / a081b882f1ea108b | `routines/zoya/release/zoya-slow-work.txt` at commit 0ba169369480144c63e22e1114485551b6a9ece4 |
| FAST prompt | 44,075 / c17029efa4ab2fb2 | `zoya-one.txt` here, pinned to 0ba1693 |

**How it's built:**
- Built on a worktree at f70901f, with `../zoya-rules-read/build_one.patch` already in this folder's `build_one.patch`.
- Command: `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 0ba169369480144c63e22e1114485551b6a9ece4`. Built twice, byte-identical.
- Build from f70901f's parts, not the branch head. The branch head's parts carry the undeployed next-action edits and give a different SLOW file.

## Deploy, in this order (the CTO)

1. **Move the pin first:** push refs/heads/zoya-slow-pin to 0ba169369480144c63e22e1114485551b6a9ece4, then read it back. FAST checks the file's sha256 at that commit. If FAST goes live before the pin moves, every SLOW run ends Partial "slow work file unavailable".
2. **Paste FAST:** paste `zoya-one.txt` into the Zoya trigger and byte-compare it. Its only change from the deployed build b (775b9ed8) is the pin and hash, the Built to Share and Human by Design host wording, and "if any".
3. **Watch the first SLOW run** (10:38 or 16:38 on a weekday). Its record should show:
   - "eligible <n>:" with keys;
   - one outcome line per item;
   - "elapsed <n> min";
   - "carryover:" with keys;
   - a stop reason that is the cap, 40 minutes or a tool error, never "stopped early" without a reason.

## What changes

**Shared with FAST (now in the SLOW file's own text too):**
- Sri stays in Cc when he wrote on the thread, and so do Satish and Arjun on their shows; each is added back if missing.
- PRE-SEND CHECKS, with "if any" for a mail with no thread.
- GUEST EXAMPLES.
- BOOKING LINKS, with the "works" exception.

**SLOW BATCH (Akshay; CTO evidence: 16:38 sent 3 of about 100 in about 7 minutes and stopped by choice):**
- **The eligible list:** first, query every eligible item, each with its key: STEP 2 items due today or overdue, and snoozes due on or before today (keyed "snooze:<row id>:<date>"). Write "eligible <n>:" with one key per line.
- **Order:** carryover from the newest earlier record with SLOW work first, then SLOW ORDER's groups, oldest due first within each.
- **How much:** work up to the per-run cap on Cadences (40, shared with FAST's sends in the run). No cadence change.
- **When it may stop:** only on the per-run or daily cap, the 40 minutes, or a tool error, named. Stopping sooner is Partial "stopped early: <why>", a defect.
- **The record:** one line per item ("sent | returned to Akshay | held | blocked | deferred"), "elapsed <n> min", and "carryover:" with one key per line.
- **LIMITS:** a hold now defers only that one item and never stops the run. This was a likely cause of the early stops.

## Replay (`replay.json`)

r10b passed the build, the diffs and most cases. r10c fixes D1 to D4, D7 and D9, and the quick re-check of r10c is pending.

Left as low:
- **D5:** check 2's list doesn't repeat the host add-back. SENDING does it.
- **D6:** no self-check before the record's last write.
- **D11:** builds from the branch head differ, so build from f70901f.
