# Inbox: cap the backlog, never refuse it

Asked by the CTO (30 Oct, 08:20 JST). On 30 Oct the 08:03 run (cse_019pwcV3NZujFpfkBXLVK8fZ) found about 40 messages since 11:30Z. It called that "larger than one run can capture" and logged none, so "read to" stayed at 12:00Z, and every later run would do the same.

## The fix (`patch.py`, on the live inbox 65,336 / 403f49ac840dc31b)

**STEP 1:**
- Work the window's messages oldest received first, at most 15 not yet logged per run. A run that hits the cap ends Partial.
- The rest wait for the next run. They're not pending: pending stays for messages that failed.
- "A backlog never means working none."
- Re-reads in the 30-minute overlap that are already logged don't count toward the 15, so the overlap can't use up the cap.

**RUN RECORD is unchanged.** "read to" already means the newest received time up to which every message was logged or skipped as noise, never past a pending one. So a capped run moves it to its last message worked, and the next run starts 30 minutes before that. The WRITES and IDENTITY rules are unchanged.

**Room:** three explanatory parentheticals removed, and the unclear-create note shortened. No rule changed.

| File | Bytes / sha256 |
|---|---|
| `inbox.txt` | 65,325 / e6cf4db2bc37918b |

Built twice, byte-identical; 11 bytes under the build limit.

## Replay (`replayCAP.json`, offline): the CTO's window, 40 messages from 11:30Z

| Case | What it checks | Result |
|---|---|---|
| C1 | Run 1 works the oldest 15, moves read to to the 15th, leaves 25 unlisted, ends Partial | PASS |
| C2 | Run 2 re-reads the overlap, which doesn't count toward the cap, then works the next 15 | FAILED in the first build, which counted re-reads toward the cap. Fixed by "not yet logged" (this build) |
| C3 | Run 3 works the last 10 plus 2 new, reaches the newest, ends Completed | PASS |
| C4 | A failed write goes on pending and holds read to behind it, as intended; the next run retries it, and the cap still makes progress | PASS once C2 is fixed |
| C5 | A run with no messages is a No-op | PASS |
| C6 | A pitch not yet reached gets its loop-in in the run that works it, inside STEP 6's 72 hours | PASS |

The fixed build hasn't been re-replayed. The change is the two words C2 named.

**Known cost:** behind a long pending message, each run re-reads a growing span. That costs calls but never stops progress, and "pending since" is reported after 24 hours.
