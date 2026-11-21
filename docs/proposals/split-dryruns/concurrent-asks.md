# Concurrent asks on one row (replay 3, concurrency test), 26 Oct

Read-only replay on build split26c (FAST 34,091 / c1b292450f738a01, SLOW 63,710 / b34422106ee6f517), 26 Oct 12:20 JST. Nothing sent or written.

Row: Akshat Khandelwal @ NuFlower and GoEarnest (3f019a301a7f81ef81a4c4780c92fee2). The row is real; the decision action is hypothetical. On 2 Nov a Your call decision and the routine 1 step 1 follow-up are both due.

Keys differ:
- FAST: `...:decision:call-<id>:2026-11-02T<time>+09:00`
- SLOW: `...:followup:seq-1-1:2026-11-02T00:00:00+09:00`

**Verdict: FAIL.**
1. SLOW can't act on a row whose follow-up has no Zoya segment (e.g. "Waiting on Jheel: reply to the commercials"). FAST keys only Zoya segments, and SLOW acts only on keyed ones. This deadlocks routines 1 to 8 on every row waiting on PR.
2. FAST has no rule that Next date is the earliest open segment date.
3. Re-read-then-write isn't atomic: a long SLOW run can overwrite FAST's write. Nothing checks after the write.
4. Real data: segment 2 is dated "original due 2026-10-29", not "on <D Mon>", so DATED SEGMENTS can't see it.
