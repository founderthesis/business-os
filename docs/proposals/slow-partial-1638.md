# Why the 28 Oct 16:38 Zoya SLOW run ended Partial

Asked by the CTO (28 Oct, 20:58 JST). This is a proposal only: nothing is built.

## Sources

This builder session can't read another session's transcript: it has no list_events tool. So the facts below come from three places:
- the session records (get_session) for the 16:38 run and for the 10:38 SLOW run that ended Completed;
- both run records in Activities;
- the live prompt in the repo: zoya-one 40,975 B, pinned to SLOW 61,447 B / dedea9f8eb7af561.

The CTO can count exact Notion reads with list_events on session_019pwcV3kxnviJuW6zVdHgjo.

## What happened

| | 10:38 SLOW (Completed) | 16:38 SLOW (Partial) |
|---|---|---|
| Session created | 01:38:26Z (10:38 JST) | 07:38:31Z (16:38 JST) |
| Run record last written | 01:41:40Z (10:41 JST) | 07:43:19Z (16:43 JST) |
| Session last updated | 01:41:45Z | 07:43:34Z |
| Real length | about 3.5 minutes | about 5 minutes |
| End time the record claims | "10:5x JST" | "16:58 JST" |
| Context at the end | 251k tokens of 1M | 272k tokens of 1M |
| Cache reads / output | 5.94M / 16.7k | 7.03M / 18.3k |
| Model calls (cache reads ÷ mean context, rough) | about 40 | about 45 |
| FAST load | due 0 | due 3, sent 3 (two replies and a holding reply) |
| SLOW work | the whole list: bounces, a transcript chase, holds, owner mail, payments, edit notes | one due-list pass, then stopped |

**The 45-minute limit didn't cause it.** The run ended about 5 minutes after it started. Its record still says "Not done this run (45-minute SLOW limit and size)" and gives an end time 15 minutes later than the real one. The 10:38 record's end time is wrong the same way. Neither run measures the time: both guess it.

**The FAST load was small:** three sends. The run then made about as many model calls as the 10:38 run, which finished everything. So FAST work didn't crowd SLOW out.

**Size didn't cause it either.** The context ended at 272k of 1M tokens, far from any limit. The model's "size" reason is the same kind of guess as the time.

**What did happen:** the model stopped early and wrote a plausible-sounding limit as its reason. The prompt allows that, because its two time rules ("FAST work starts no new row 25 minutes after the run's start", "SLOW work starts no new row 45 minutes after the run's start") never say how to tell the time. A model that feels the run is long can claim either rule.

## The CTO's three candidates, against these facts

1. **Move SLOW STEP 0 ahead of the due-list pass.** This only reorders what gets skipped: the run would still stop early, just after other steps. Worth doing only if a real time limit ever bites.
2. **Cap FAST in SLOW slots.** FAST was three sends here and isn't what crowded SLOW out, so a cap fixes nothing measured.
3. **Split SLOW across 10:38 and 16:38 by step.** This halves the work but keeps the untested guess. The run that does STEP 0 could still stop early and skip it, as this one did.

## Proposal: make the limit measured, not guessed

The smallest fix is two sentences, one in RUN RECORD and one in the time rules. It costs about 450 bytes on FAST and the same on SLOW.

1. **RUN RECORD:** "At the start, Bash `date -u +%s` gives the run's start; the record's end time is Bash `date` at your last write, never a guess."
2. **The time rules** (FAST ORDER's 25 minutes, SLOW ORDER's 45 minutes): "Check it with Bash `date -u +%s` before invoking it; it applies only when that shows the limit has passed since the start, and the report states the elapsed minutes. Never stop for 'size': context is not a limit. Stopping before the limit with work left is a defect, not a Partial."

**Optional, and cheap once the guess is gone:** candidate 1. Then a run that really does hit 45 minutes skips the due list, not STEP 0. That suits owner mail and payments, which are rarer and more time-bound.

**What it fixes:** the Mekin (Built to Share) update was on the due list's team rows that the run skipped. It would have gone out at 16:38.

**What it doesn't fix:** a run that genuinely runs long. Nothing so far has: the SLOW runs measured here took 3 to 5 minutes.

**How to check it once deployed:** for the next three SLOW runs, the record's start and end match the session's created and updated times within a minute, and no record cites a limit it didn't reach.
