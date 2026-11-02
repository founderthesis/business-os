# Capture r8 (CTO, 2 Nov 12:25 JST)

**Base:** the live r7, `../cleanup/r7/capture.txt`, 39,522 / 3f08b76e.
**Build:** `patch.py` makes three edits, each asserted once. Built twice, byte-identical.

| File | Bytes / sha256 |
|---|---|
| `capture.txt` | 39,990 / d6bd4cd861d4d98d |

| # | Change | Where |
|---|---|---|
| 1 | **LINK class in STEP 0:** mail rows (msgid: or adid:) with no People and no Engagement, created since 2026-11-01T03:00Z, Captured before today. They count toward STEP 1's cap (15, BACKLOG 25), not STEP 0's 15. Each is read by its key (adid: by UID) and linked as STEPS 2 and 3 do. A row it touches gets Captured today, as all of STEP 0 does, so it's tried at most once a day, and today's 14 rows are taken from tomorrow | STEP 0 |
| 2 | **allmail: rows that are ad@-only** (and not sent from ad@) re-key to adid:<UID> with no RAW. MSGID FIND and STEP 2's lookup still run first. An id outside All Mail is found there by from, subject and date | STEP 0 |
| 3 | **RAW returned inline** is written to a file, the whole value in order, 8,000 characters per appended heredoc. The decode strips newlines, so the chunk boundaries don't matter, and runs after each chunk. It stops once a complete id shows. The existing rule that a failure pends as mcp: and never stops the run is unchanged | MAILBOX RAW |

**Why "Captured before today" and not "regardless of Captured":** Notion can't filter on body text, and STEP 0 marks a row as tried by setting its Captured. Without that cut, a row that can't be linked would come back every run and use cap slots for nothing.
