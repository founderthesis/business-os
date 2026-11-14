# r27: SLOW done by :35 JST; N2 and the outcome check held to their words

Main, 12 Nov ~21:30 JST, for the CTO's 20:55 ask. Built on r26 (accepted at 7bc9461, pin 63d63ec). Not deployed, the pin ref isn't moved, nothing written to Notion.

## 1. SLOW and the hourly's lock

**Today's three Opus runs** (from their own records):

| Run | Start (date -u) | Chunk 2 began | Stop line | End | Elapsed | Hourly at :38 |
|---|---|---|---|---|---|---|
| 14:08 | 14:08:57 | minute 20 | 14:48:21 (minute 39.4) | 14:49 | 41 min | 14:38 skipped (lock held) |
| 17:10 | 17:10:02 | 17:30:13 (minute 20.2) | 17:38:39 (minute 28.6) | 17:41 | 30 min | 17:39 skipped |
| 20:12 | 20:12:09 | minute 15.8 | 20:34:16 (minute 22.1) | 20:35 | 23 min | 20:39 ran (No-op) |

**Why:**
- **The stop is only checked between chunks.** SLOW BATCH says "Stop only at minute 22 (no new chunk after it)", and the run checked the time only before a chunk. A chunk of 10 that starts at minute 20 runs to its end:
  - 14:08: chunk 2 took 19 minutes, about 1.9 a row, and the check came at minute 39.
  - 17:10: chunk 2 ran 8.4 minutes, and the check came at minute 28.
  - Both records still wrote "minute 22".
- **The budget counts from the start, not the clock.** A run firing 4 minutes late (20:12) uses its full 22 minutes to 20:34 and ends at 20:35. With the record and the release, that leaves 3 minutes before the hourly.

**The fix,** with the existing budget and carryover: no new gate, and LOCK and RELEASE untouched. "Minute 22" is redefined in one place, SLOW BATCH 3/:

> Stop only at minute 22 (the earlier of 22 minutes after the start and :28 JST of the hour you started in, checked with `date -u` before every item, never only between chunks; no new item after it)

The stop line's python check and the OUTCOME CHECK now refer to "minute 22 as 3/ defines it". That replaces "22 or more minutes after the start" and "under 22 minutes after the start, or while the measured elapsed is under 22".

**The arithmetic,** with the observed costs:
- **The longest row was about 1.9 minutes** (14:08's chunk 2). The last row starts no later than :28 and ends by about :30.
- **Last write to release:** 0.6 to 2.4 minutes (end minus stop line on the three runs), so the record and release finish by about :32 to :33.
- **That leaves 5 minutes before the hourly fires at :38,** and at least 2 before the :35 target.

The three runs replayed under the new rule:

| Run | Start | Stops at | Minutes of work | Release by |
|---|---|---|---|---|
| 14:08 | 14:08:57 | 14:28 (:28 comes first; minute 19.1) | 19 | about 14:33 |
| 17:10 | 17:10:02 | 17:28 (minute 18.0) | 18 | about 17:33 |
| 20:12 | 20:12:09 | 20:28 (minute 15.8) | 16 | about 20:33 |

**Cost:** 3 to 6 fewer minutes of work per run. At today's pace of 13 to 15 rows per run, that's about 3 rows, which go to carryover and lead the next run's selection. With seven runs a day, the backlog (60, then 19, then 3 eligible across today's runs) still clears.

**A run that starts after :28** (more than 20 minutes late) does no work, writes its record with carryover, and releases. That's the intent, because the hourly comes next.

## 2. N2 and the outcome check (20:12's deviations)

The 20:12 record said "N2 checks on S04 to S14 used a SQL read of the Claude note, not a page fetch" and "The code check ran on a condensed copy of this body with mail links unwrapped, not the verbatim fetch".

**Cut before add:**
- **N2** (HARD RULES, in all four prompts): "after the write re-fetch the row and assert" becomes "after the write read it again that way and assert". "That way" is the first read just described: a notion-fetch of the row, the note pasted verbatim into python, and "SQL results, a full column included, rows mode, a preview or any slice are never a read of the note". So the existing ban now covers the re-read too, with no new list.
- **The chk: marker** (SLOW BATCH 4/): the python now fails a chk: that doesn't end "fetch". The record's own S04 to S14 lines ended "sql", so a SQL re-read now leaves the item unfinished instead of passing.
- **OUTCOME CHECK input:** "give python its body verbatim in a quoted heredoc" now goes on: "the fetch's text exactly, never a condensed, unwrapped or retyped copy".

**Hourly:** the N2 wording reaches it too. Two cuts pay for it: "properties from its fetch" becomes "fields from its fetch", and "negotiation reply" becomes "negotiation" in an example list. The hourly is 62,992.

## Builds

Each was built twice, byte-identical, and rebuilt from a fresh worktree at f70901f with r27/zoya/build_one.patch. The SLOW file matches the pin commit. No em dash.

| Routine | Base (r26) | Build | Bytes / sha256 |
|---|---|---|---|
| Zoya SLOW file | 63d63ec (78332307) | routines/zoya/release/zoya-slow-work.txt at **582ad08** | 95,045 / ce4d0b3f22ec8daf |
| Zoya SLOW task | 4da2f146 | r27/zoya/zoya-slow.txt (pin 582ad08) | 15,652 / 856318d36558128d |
| Zoya hourly | b1b0b0ac | r27/zoya/zoya-one.txt | 62,992 / 839117217edc49ed |
| Zoya episodes (not live) | b796ea43 | r27/zoya/zoya-episodes.txt | 50,152 / 2a0c1bffce85c8c9 |

**How to build:** apply r27/zoya/build_one.patch at f70901f, then run `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 582ad08c0473dd56beb9ab794e5220f1acc72b1c`.

**Deploy (CTO):** pin 582ad08, then the SLOW task and the hourly.

## Not done

The CTO asked for this to be posted as a comment on the coordination thread. That's a Notion write on a relayed ask, which Main doesn't make. This file is the post, and the CTO or Cleanup can link it there.
