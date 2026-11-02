# Cleanup verdict: capture and actions r10c (d0cd599, efeb028), 2 Nov ~18:45 JST

This covers the changed behaviour only. The replay is in `replay-cleanup.json`.

**Capture r10c:** accepted on correctness, **but it can't go live while actions is r8e** (B1).
**Actions r10:** not accepted (B2, B3).

**The fast, safe route for the 90 rows is option A below.**

## Rebuild

- `r10/patch.py` from capture r8h (de8465b8) and actions r9e (ac763528), run twice, gives:
  - capture.txt **43,349 / 21ef858303692477**;
  - actions.txt **42,394 / bbaa4262caa35cb8**.
- Both are byte-identical to the repo. The diffs hold only STEP 0A, STEP 0's class text and the REPAIR clause. There are no em-dashes.

## What holds

- **Selection:** a run takes no row twice and starves none, because every touched row gets Captured today and goes to the back.
- **Path order:** the cheapest path runs first, and the raw fetch only for mail sent from ad@ or with Zoya on it.
- **Folds** follow decision 416.
- **Loop-ins:** none for 0A rows.
- **Loops:** REPAIR's try counter caps it at 3 tries, so nothing loops.

## Blockers

**B1. Deploy order: capture r10 with live actions r8e replays old mail in full.**
- Live r8e takes "rows created before 2026-11-02 and Captured on or after the day before W's date". Its REPAIR only covers a row with a "link:" line *after its last "actions: done"*.
- The roughly 87 rows that 0A re-keys or keeps are old, get Captured today, and have no "actions: done". So r8e gives this 29 to 30 Oct mail a full first run, with none of REPAIR's checks. That means status moves, Zoya steps and asks on Akshay's list, all from mail that's 3 days old.
- **Capture r10 must not go live before an accepted actions r10.**

**B2. REPAIR on old mail can still write stale state.**
- The guard is "never undo a newer Your call, Status or decision". Waiting on, Next action, Next date and the calendar aren't covered.
- So a recovered 29 Oct mail can set "Waiting on X". r9e's decision 443 can queue Zoya slots for a past date, and decision 444 can put stale asks on Akshay's list (decision 325).
- **Fix:** for a recovered row older than its Engagement's newest Activity, write no state, no ask and no WhatsApp. Log the link only, ledger "nothing left (superseded)".

**B3. Actions r10 brings in r9e, which Cleanup hasn't reviewed.** Live actions is r8e. From the diff, r9e adds:
- decision 443: a call request gets "Zoya: reply to <who>: slots for <date>" and sets Next date, while Tier 1 or a same-day or next-day date goes to Akshay;
- decision 444: new inbound on a closed row puts an "Akshay: ... Recommend:" ask on his list and blocks Zoya's replies except the holding reply.

Neither touches the cursor or adds a send path, but both need their own review before actions r10 can ship.

## Option A: drain now with no business effects (recommended)

The 29 to 30 Oct mail has mostly been handled by hand and by Zoya since then. So recover the records without replaying their effects.
- Capture r10c, plus one change: every row STEP 0A re-keys or keeps also gets "actions: n/a (recovered <date>)".
  - Live r8e already closes rows marked "actions: n/a" without work.
  - Fold-stamping the kept row would also be dropped.
- That makes capture r10c safe with the live actions r8e, and the drain runs at 10 a run with links and People but no stale asks.
- Anything still truly open shows in the "allmail left" and "link:" report lines for a person to pick up.

## Should-fix (capture)

1. **STEP 0's 8 minutes.** STEP 0 still says "Start no row more than 8 minutes after the run's start", which contradicts 0A's "count from the end of 0A". Edit STEP 0's own sentence.
2. **Time for new mail.** 0L has no time limit, so 0L, 0A and STEP 0 up to minute 12 can leave STEP 1 little time before STOP TIME. New mail is delayed, not lost. **Fix:** 0A starts no row after minute 10.
3. **Strikes on a systemic error.** "at its third such line" with hourly runs retires a row within 3 hours. **Fix:** one strike per JST day.
4. **A row that never resolves.** A row whose MCP Emails id no longer resolves gets no strike, so it rotates forever and "allmail left" never reaches 0. **Fix:** any failure other than quota, rate-limit or 5xx counts as a strike.
5. **MSGID FIND.** "MSGID FIND by Date within 2 minutes" drops STEP 2's People-overlap branch. **Fix:** "MSGID FIND as STEP 2 defines it".
6. **"recovered" marker.** STEP 6's catch-up has no marker for a 0A row. **Fix:** a row with a "link: <run id> recovered" line is never caught up. Also limit actions' "never given a full first run" to recovered rows (S9 in the replay).
7. **Meeting rows.** Path 0/ should say to read the mail and look up the Doc id first.

Nothing deployed by Cleanup. If you choose option A, I can review the one-line change quickly.
