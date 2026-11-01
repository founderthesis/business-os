# Capture r6 (CTO, 2 Nov 01:40 JST: the split is live; r6 before the 09:02 JST run)

**Base:** the live capture r5, 36,666 / 405a30d3 (`../cto-r5/capture.txt`, commit 9e57cd2).
**Build:** `patch.py` applies seven asserted edits; everything else stays byte-identical. Built twice, byte-identical.

| File | Bytes / sha256 |
|---|---|
| `capture.txt` | 37,601 / bd937363f8e8e5fa |

Actions (39,354 / 19701651) and the sweep (6783dd01) are unchanged.

| # | Change | Where |
|---|---|---|
| 1 | **STEP 0 duplicate** (108855, 108860). Before re-keying an `allmail:` row, STEP 0 runs STEP 2's full lookup (IN on its ids, LIKE on the Message-ID's part before @, Zoya's rows included). Any hit other than the row itself: fold into it, never re-key | STEP 0 |
| 2a | **Work to the cap or STOP TIME**, whichever comes first. Ending earlier while due messages remain is Partial, "stopped early", listed as a defect | STOP TIME |
| 2b | **Batched reads:** bodies are read with `read_batch`, up to 20 a call, `body_max_chars` 2000. Action `read` runs only where a step needs the full body | STEP 1 |
| 2c | **Stakeholders:** the full `get_thread` sweep runs only for a new pitch, a new thread, or an address not yet in People. Otherwise it checks only the message's own From, To and Cc | Also on every Engagement |
| 2d | **Message-IDs:** when a later message's References or In-Reply-To names a Message-ID, it's confirmed with `query HEADER Message-ID` and that message's RAW fetch is skipped. Otherwise there's one `original` call per message, with the Bash recipe | STEP 2 IDENTITY |
| 2f | **Stop times count from the run's start** (CTO addendum): no new message more than 18 minutes after it, measured with `date -u`, and STEP 0 starts no row more than 8 minutes after it. A run fired by hand, or in another slot, gets the same window. The cron stays at :02 | STOP TIME, STEP 0 |
| 2e | **BACKLOG:** with more than 15 due at the start, the cap is 25 and STEP 0's rows count toward it | STEP 1, STEP 0 |

CONTEXT CHECK's `get_thread` before a loop-in is unchanged: it guards a send.
