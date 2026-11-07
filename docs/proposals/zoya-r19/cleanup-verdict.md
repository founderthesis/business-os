# Cleanup verdict: Zoya r19 (Claude note writes), plus the 18:38 lock gap

Cleanup session, 4 Nov 2026, about 20:55 JST. Read-only. Nothing deployed.

## Verdict: r19 accepted for the 08:08 JST repin

Reproduced twice, byte-identical, each equal to the proposal copy. I applied docs/proposals/zoya-r19/build_one.patch alone to a worktree at f70901f6, then ran build_one.py refs/heads/zoya-slow-pin 95c4e79667baeb2d276211dcef0241cc3b15c971. None of the four files contains an em dash.

| File | Bytes | sha256 (first 16) |
|---|---|---|
| zoya-slow-work.txt (pin 95c4e79) | 82,109 (82,105 characters) | c4fd78d6828640fb |
| zoya-slow.txt (SLOW task) | 13,451 | 8c8765db87178fa5 |
| zoya-one.txt (hourly) | 55,192 | ee8f196655999a7a |
| zoya-episodes.txt (not live, not reviewed) | 45,698 | 3fa79d6fd1f8f0e2 |

Diff against r18 contains only what the handoff names:
- The CLAUDE NOTE WRITES HARD rule is the same text in all three prompts: hourly line 103, SLOW file line 149 and the SLOW task's HARD RULES (episodes line 87).
- SLOW task: SLOW FILE now runs "after the run record's Started write is confirmed (never before it)". The pin sha is 95c4e796..., the hash prefix c4fd78d6828640fb and the total 82,105 characters, all matching the file. The deployment reference is b96e947c724f.
- SLOW file 3/: chunks run "in S-number order, never one out of order". Held, blocked and overtaken lines carry note:<row id> <date> from a read-back.
- SLOW file 4/: the python checks note: on all four terminal outcomes.

Repin order is unchanged: move zoya-slow-pin to 95c4e79, paste the SLOW task (8c8765db) and the hourly (ee8f1966), then read all three back.

## Should-fix (next round, r20 or later; none blocks the repin)

- N1. Check the text exactly, not just its length. "New length at least old plus new line" passes a rewrite that keeps or grows the length, for example an older line edited and padded. Make the python assert new == new_line + separator + old.
- N2. Check what Notion stored, not just the local string. The python checks the string the run built. A truncation or escape change on the write side passes. Fetched notes carry `<br />` separators and backslash escapes (Ryan Louvar's row has `20\\:30`), so writing one back can shift the count either way. After the write, re-fetch in the same mode and assert the old note is still the stored note's tail. That also replaces 3/'s "top line dated today" read-back.
- N3. Say how "note check failed" counts. 4/ accepts only cap, minute 22 and tool error as reasons, so one note check failure makes the whole run Failed. That may be wanted (it's loud), but say so, or add it to the allowed reasons as Partial.

## The 18:38 JST hourly run (CTO finding)

The zoya-lock log confirms it: 08:43:32Z (17:38 run, released), then 10:38:48Z (19:38 run, held). Nothing at 09:38Z.

The hourly prompt live now is byte-identical to r18 (get_trigger saved it to a file: 54,773 / 1a437c41c7a74d43). It was updated 07:45:12Z, before 18:38.

In r18, one path ends a run before LOCK without a record, by design: "no repo: end at once and report 'no repo, lock not checked'". That report is only the session's final message. No Activity is written. Every other pre-lock failure (fetch fails, lock held, lock taken) goes through LOCK 3, which writes the Skipped record. A run that never started (the scheduler fired, but the container or session failed before the prompt ran) also leaves nothing.

I can't list trigger-fired sessions from here, so I can't tell which of the two it was. Check the scheduler's run history for 09:38Z. If a session exists, its final message says "no repo" or it has an error.

- L1. On the no-repo path (hourly and SLOW), write the record anyway: Summary "Run <routine> <start> JST: Failed: no repo, lock not checked". The run id comes from printenv, or the syn- id. This is safe: without a lock nothing else runs, and a record is only an Activity. The morning check then sees it.

## The record left at "Started" with a complete body (10:40 run)

That run released the lock (its free: commit is in the log), so it believed its last write was done. Either the last write updated the body but not the Summary, or the Summary update failed silently.

- L2. Before RELEASE, re-fetch the record and assert in python that the Summary no longer ends "Started" and starts with the status line 4/ printed. On a miss, retry the Summary write once, then add "record status write failed" to the body. Applies to hourly and SLOW.
