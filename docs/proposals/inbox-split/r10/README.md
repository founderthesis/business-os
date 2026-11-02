# Capture r10 and actions r10: drain the old allmail: rows (CTO, 2 Nov 17:00 JST)

**Bases:**
- capture: the live r8h, `../r8h/capture.txt`, 41,418 / de8465b8;
- actions: r9e, `../r9/actions.txt`, 42,316 / ac763528, which is with Cleanup and not yet deployed.

**Build:** `patch.py`, every edit asserted once, built twice, byte-identical.

| File | Bytes / sha256 |
|---|---|
| `capture.txt` | 43,475 / 82004b7ce0da42d7 |
| `actions.txt` | 43,122 / 3e548c47562977b6 |

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

## r10c (replay10.json, r10b section: ready on correctness)

The four lows it named are applied:

| Item | Fix |
|---|---|
| N1 | STEP 0 starts no row more than 12 minutes after the run's start, so new mail keeps its window before STOP TIME |
| N2 | 0A's 5 minutes count from the end of STEP 0L, so a heavy link pass can't take 0A's window. 10 a run is the stated batch, and slow RAW rows can make it fewer, carried first to the next run. Raise the window if the drain should be faster: about 9 runs at 10 a run, up to about 15 if RAW-heavy |
| N3 | A re-keyed Meeting row also gets Source Gemini notes and its Link set to the Doc |
| N4 | No loop-in for a 0A row, here or in STEP 6's catch-up. The fold stamp applies whatever the kept row's age |

**Status:** written and replayed offline (r10b). These four one-phrase changes weren't replayed again. Ready for Cleanup. Deploy actions r10 with or after r9e.

## Capture r10d and actions r10b (Cleanup's verdict, `../cleanup/r10/verdict.md`; CTO 20:48 JST)

**Option A (blanket n/a) is not used.** Akshay wants missing business effects found, not skipped.

**B2, actions REPAIR against current state:**
- **What it checks:** each effect the recovered mail calls for (STEPS 2b to 6e, 443 and 444 included) is checked against the row's current state and today's threads. That means both inboxes, the newest Activities, Sent, Action keys, the calendar, and the row's Status, Waiting on, Next action and Next date.
- **Done or overtaken** by anything newer: "n/a (overtaken: <what>)", with no write.
- **Still missing:** applied, or handed over as a dated visible step ("Zoya: reply to <who>: <what> (asked <D Mon>)", or Akshay's list under 325).
- **What it never does:** resend, set a past Next date or call date, or write over a newer value.
- **The ledger:** one line per effect.
- **First runs:** only a recovered row is never given a full first run (S9).

**B1, deploy order (unchanged):** capture r10d needs this actions build live first or with it. Live r8e would give the recovered rows a full first run.

**B3:** r9e's 443 and 444, scoped to Akshay's words, are in this build and need Cleanup's review with it.

**Capture should-fix 1 to 7:**
1. STEP 0's own sentence: no row after 8 minutes from the end of 0A, nor after minute 12.
2. 0A starts no row after minute 10.
3. A strike counts at most once per JST day.
4. Any failure other than quota, rate-limit or 5xx is a strike, an id that no longer resolves included.
5. MSGID FIND as KEY defines it, with the People-overlap branch back.
6. STEP 6 never catches up a recovered row.
7. A Meeting row reads its mail for the Doc id first.

**Status:** written, replay pending.
