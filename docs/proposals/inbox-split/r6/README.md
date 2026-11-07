# Capture r6 (CTO, 2 Nov 01:40 JST: the split is live; r6 before the 09:02 JST run)

**Base:** the live capture r5, 36,666 / 405a30d3 (`../cto-r5/capture.txt`, commit 9e57cd2).
**Build:** `patch.py` applies seven asserted edits; everything else stays byte-identical. Built twice, byte-identical.

| File | Bytes / sha256 |
|---|---|
| `capture.txt` | 37,954 / 9b55110e2cead4c2 |

Actions (39,354 / 19701651) and the sweep (6783dd01) are unchanged.

| # | Change | Where |
|---|---|---|
| 1 | **STEP 0 duplicate** (108855, 108860). Before re-keying an `allmail:` row, STEP 0 runs STEP 2's full lookup (IN on its ids, LIKE on the Message-ID's part before @, Zoya's rows included). Any hit other than the row itself: fold into it, never re-key | STEP 0 |
| 2a | **Work to the cap or STOP TIME**, whichever comes first. Ending earlier while due messages remain is Partial, "stopped early", listed as a defect | STOP TIME |
| 2b | **Batched reads:** bodies are read with `read_batch`, up to 20 a call, `body_max_chars` 2000. Action `read` runs only where a step needs the full body | STEP 1 |
| 2c | **Stakeholders:** the full `get_thread` sweep runs only for a new pitch, a new thread, or an address not yet in People. Otherwise it checks only the message's own From, To and Cc | Also on every Engagement |
| 2d | **Message-IDs:** when a later message's References or In-Reply-To names a Message-ID, it's confirmed with `query HEADER Message-ID` and that message's RAW fetch is skipped. Otherwise there's one `original` call per message, with the Bash recipe | STEP 2 IDENTITY |
| 2f | **Stop times count from the run's start** (CTO addendum): no new message more than 18 minutes after it, measured with `date -u`, and STEP 0 starts no row more than 8 minutes after it. A run fired by hand, or in another slot, gets the same window. The cron stays at :02 | STOP TIME, STEP 0 |
| 2e | **BACKLOG:** with more than 15 due at the start, the cap is 25. STEP 0 shares only the time window: its rows don't count toward the cap, because STEP 0 runs first and could otherwise take 15 of the 25 (replay R6-2) | STEP 1 |

CONTEXT CHECK's `get_thread` before a loop-in is unchanged: it guards a send.

## Replay fixes (r6b, `replay6.json`)

| Item | Fix |
|---|---|
| R6-1 | The HEADER confirm must return the same message, the same MCP Emails id; otherwise RAW. A References id can name a different message |
| R6-2 | BACKLOG: STEP 0's rows don't count toward the 25 (see 2e) |
| R6-3 | A truncated forward, pitch or edit notes is always read in full |
| R6-4 | OVERLAP: if another capture record is still Started and under 30 minutes old, the run writes No-op and stops |
| Nit | When several rows match, the fold goes into the row whose Source ID is exactly the msgid: key, else the oldest |

**Hand runs:** not between :35 and :50 (Zoya's :38 run), and not within 30 minutes of another capture run.
