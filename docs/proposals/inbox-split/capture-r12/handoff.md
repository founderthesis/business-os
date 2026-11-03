# Capture r12: order gate, measured stop, 0L and 0A count lines (CTO, 3 Nov ~14:30 JST)

| File | Bytes / sha256 |
|---|---|
| `capture.txt` (r12) | 45,137 / 64f8fc5bf40c9ec6 |
| Input: `../r11/capture.txt` (r11, should-fix included, assumed live) | 43,989 / 043dbe3ad8d0a858 |

**Build:** `python3 patch.py ../r11/capture.txt <out>` asserts the input hash 043dbe3a and each edit exactly once. Patched twice, byte-identical. No em dashes. The CTO should byte-compare the live capture against 043dbe3a before pasting.

## Why
The 14:02 run lasted 2.5 minutes. It wrote "STEP 0L, 0A, STEP 0: not worked this run, stop time" without ever running 0L's or 0A's SQL. STOP TIME is minute 18.

## The three edits, nothing else
1. **ORDER GATE**, before STEP 0L:
   - After the run record and OVERLAP's check, the first two Notion queries are 0L's SQL, then 0A's SQL. Both run before STEP 1's search or any other MCP Emails call.
   - Each query's row count goes on the record as the "due" figure of its line.
   - The run then works 0L's rows, then 0A's.
   - Searching mail first, or a record without either line, makes the run Failed, "order gate".
2. **MEASURED STOP**, in STOP TIME:
   - Any stop for time is read from `date -u` at that moment, and the record says "stopped at minute <n> of <limit>".
   - Rows of this run's 0L or 0A batch left unworked before a measured limit has passed make the run Failed, "0A skipped at minute <n>" (or 0L), never Partial.
3. **Record body**: the first lines are "0L: <n> due, <n> worked" and "0A: <n> due, <n> worked (REF <n>, RAW <n>, adid <n>, fold <n>)". The "stamped:" line follows; actions finds it by name, not position.

## One thing to confirm (CTO)
Item 2 as asked ("ending before minute 18 with 0L or 0A rows due and unworked is Failed") would also fail a run that obeyed 0A's own window: start no row more than 5 minutes after 0L ends, nor after minute 10. So r12 counts that window as a measured limit, and so is STOP TIME. Leaving rows only at one of those limits, measured and logged, isn't Failed. If you meant 0A's window to go, that's one more edit.

**Status:** built. Replay running. Nothing deployed.
