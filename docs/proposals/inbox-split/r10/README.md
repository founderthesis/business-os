# Capture r10 and actions r10: drain the old allmail: rows (CTO, 2 Nov 17:00 JST)

**Bases:**
- capture: the live r8h, `../r8h/capture.txt`, 41,418 / de8465b8;
- actions: r9e, `../r9/actions.txt`, 42,316 / ac763528, which is with Cleanup and not yet deployed.

**Build:** `patch.py`, every edit asserted once, built twice, byte-identical.

| File | Bytes / sha256 |
|---|---|
| `capture.txt` | 43,212 / 24570e4b06bbbed5 |
| `actions.txt` | 42,394 / bbaa4262caa35cb8 |

## Capture

A new **STEP 0A**, after STEP 0L, with its own SQL: `allmail:` rows ordered by Captured, then Date, 10 a run (stated). It works all 10 before STEP 0, never skipped as too heavy, each by the cheapest path:
1. Read it by its MCP Emails id: UID, From, To, Cc, date.
2. MSGID FIND by Date within 2 minutes against msgid: rows (Zoya's included), HEADER-confirmed: fold.
3. Ad@-only and not sent from ad@: `adid:<UID>`, STEP 2's lookup, then fold or re-key.
4. Only then RAW (sent from ad@, or Zoya on it, with no match), through its file.

If RAW fails, the row gets "allmail: no Message-ID <date> <the error>" and goes to the back of the queue by Captured. At the third such line it becomes `allmail-unread:` and is reported once. The next row always goes on.

**What each recovered row gets:** a re-keyed or linked row gets the "capture:" line and "link: <run id> recovered", and its own page id goes on the record's "stamped:" line.

**The record:** one line per row ("<allmail id>: re-keyed <key> | folded into <row> | linked <row> | pended <reason>"), then "allmail left: <n>" after the batch, so the drain shows run by run.

**Other changes:**
- STEP 0's own allmail: class is removed, since those rows are STEP 0A's, so none is taken twice.
- STEP 0A's rows don't count toward STEP 1's cap, and STOP TIME holds.

**Throughput:** 90 rows at 10 a run is about 9 hourly runs, through the existing schedule, with no hand runs.

## Actions

**REPAIR condition:** a stamped row with a "link:" line and no "actions: done" after it gets REPAIR. So a recovered row is only checked for effects not yet performed, never replayed from scratch and never resent.

Deploy actions r10 together with, or after, r9e.

## r10b (replay10.json)

| Defect | Fix |
|---|---|
| D1: Gemini Meeting rows | Path 0/: a Kind Meeting row's key is the Doc id, with no RAW |
| D2: folds didn't stamp the kept row | A fold stamps the row it keeps for REPAIR, unless that row is Zoya's own or already has "actions: done". This covers Akshay's 29 to 30 Oct sent mail that Zoya logged |
| D3: rows taken twice | Every row 0A touches gets Captured today, with a "first captured" line |
| D4: time | 0A starts no row after 5 minutes, and STEP 0's 8 minutes count from the end of 0A |
| D5 | REPAIR skips a row with "actions: stuck" after its link line |
| D6 | A quota, rate-limit or 5xx error is no strike. The record says "allmail left: <n>, unread: <n>" |
| D7 | A REPAIR row is never given a full first run |
| Loop-ins | 0A sends none: their 72 hours have passed |

**Status:** written. Re-replay pending.
