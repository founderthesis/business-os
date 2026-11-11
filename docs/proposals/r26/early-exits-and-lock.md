# r26: the 11 Nov early exits and the SLOW/hourly lock clash (diagnose and propose, nothing built)

Main, 11 Nov, for the CTO's ask after r25's first live runs. Read-only: nothing built or deployed, no Notion write.

## What I could read

This session still has no tool that reads a routine run's events, so I couldn't open either transcript. I read:
- the session records (get_session) for both runs;
- the runs' own records in Activities (the hourly's and SLOW's);
- the live prompts as built in r25.

| Run | Length | Context at end | Output tokens | Its own record |
|---|---|---|---|---|
| Zoya hourly 19:39 (cse_019pwcV1tQUNiwR8oU6Bgox4) | 8 min (10:38:52 to 10:47:55 UTC) | 434,911 of 1,000,000 | 40,237 | "Failed (early exit at minute 8)" |
| WhatsApp 20:48 (cse_019pwcV2PbeFtMUDnyiU33m7) | 2 min (11:46:14 to 11:48:17 UTC) | 161,827 | 6,472 | none (WhatsApp writes no run record) |
| Zoya SLOW 20:08 | started 20:17, stopped at minute 22, ended 20:41 | | | "Partial (minute 22)" |

## 1. Why the two runs stop early

**The status check works; it just doesn't stop anything.** The hourly's own record says it honestly:
- "step 0r: unfinished (not reached ...)", "step 1: unfinished (not reached ...)", "step 1-72h: unfinished (not reached)";
- the python check printed Failed (early exit at minute 8).

So STATUS IN CODE did its job: it labelled the exit. But it runs only at the end, when the run has already decided to stop, and nothing sends the run back.

**What made it decide to stop** (likely, not proven without the transcript):
- **Size:** the hourly loads Rules for Zoya (65,737 chars) and the wording page (63,445) in full, then the mail. By minute 8 it held 435k tokens of context. That's the same shape as the calendar exits (heavy reads, then a short report).
- **Wording:** TIME already says "size or context never ends a run early", so the wording isn't missing. It's a rule the model weighs and loses to its own sense that the run is big. Another sentence of the same kind won't hold either.

WhatsApp is the same pattern. In 2 minutes it pulled 160k tokens, ran STEP 0, 1, 2 and 2b, and skipped 0d, 0w, 3, 3d and 4. Its own order puts 0w third, so it didn't follow its list. WhatsApp has no run record, so I can't see its step lines.

**Proposed fix: turn the end check into a gate,** in the hourly and in WhatsApp. One sentence each:

> GATE: run the STATUS IN CODE check before your last write; while it prints Failed and `date -u` shows under 25 minutes since the start, write nothing final: go back to the first step it names, work it, and check again.

This is the one change that doesn't rely on the model agreeing the run is too big. The code names the unreached step, and the rule makes the next action "go and do it", not "write the report".
- **Hourly:** about 230 bytes. It's at 62,951 (r25), so it needs about 190 bytes of cuts. Candidates are description-only parentheticals (the NOTION DATA field lists, two worked examples in HARD).
- **WhatsApp:** about 230 bytes, no cut needed (39,065).
- **WhatsApp run record:** I'd also give WhatsApp the run record the others have ("Run whatsapp <start> JST: <status>" plus its step lines), about 400 bytes. Without it, an early exit only shows in the session.
- **Calendar:** the same gate belongs in calendar-early-exit.md's proposal.

**Lighter reads would cut the pressure behind it.** This is a separate and bigger change, so I'd leave it out of r26's first cut. The hourly reloading 129k chars of Notion rules every hour is most of its context. A read-once cache would halve the hourly's context, keyed on each page's last-edited time and stored in the run record of the previous run. But it changes RULES LOAD, which Cleanup has guarded since r21.

## 2. SLOW holding the lock past :38

**What happened:**
1. SLOW's 20:08 trigger started at 20:17, 9 minutes late, from the scheduler.
2. It worked its measured 22 minutes and stopped at 20:39.
3. It wrote its record and freed the lock at 20:41.
4. The 20:38 hourly found the lock held and wrote "Skipped: lock held by cse_019pwcV3YPW9Zmf33DfoZSbW".

With seven SLOW runs a day (decision 546), any start more than about 8 minutes late will do this again.

**Option A: SLOW ends by :30 JST at the latest (recommended).**
- SLOW BATCH's stop becomes "measured minute 22 or :30 JST of the hour it started in, whichever comes first".
- A :30 stop is written as the stop line "stop: :30 JST at <date -u>", and the python check accepts it like minute 22 (Partial, with carryover).
- That leaves 8 minutes for the record and the lock release before the :38 hourly.
- **Cost:** a late SLOW run does less, and its carryover goes to the next of the seven runs. About 150 bytes in the SLOW file and 40 in the SLOW task's status check. Pin moves.

**Option B: the hourly waits for the lock.**
- Finding the lock held by a zoya-slow run, the hourly re-reads it every 60 seconds for up to 6 minutes (Bash sleep 60, then the same read) before it writes Skipped.
- **Cost:** about 180 bytes in the hourly, which then needs more cuts. The hourly's own 25 minutes then start late, and it never forces or takes over the lock.

**Recommendation: A.** It fixes the cause and needs no hourly bytes. B on top is cheap insurance, but it pushes the hourly's end toward the next SLOW start, and it needs hourly cuts.

## For the CTO

1. Say yes to the gate (hourly plus WhatsApp), with or without WhatsApp's run record, and to A, B or both. I build them as r26 on the r25 builds, with cuts, both builds, sizes and sha256s for Cleanup.
2. If you can open the two sessions in the web UI, their last few events would confirm the trigger. The model's own words just before the report would show whether it was size, time or a misread of the step list. The gate holds either way.
