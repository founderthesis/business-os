# Silently skipped steps: what happened, and one shared fix

Asked by the CTO (29 Oct, 14:20 JST). This is a proposal only: nothing is built.

## The limit on this read

This builder session has no list_events tool, so it can't read another session's transcript. What follows comes from three sources:
- each run's session record (get_session: length, context used, tokens, artifacts published);
- the live trigger prompts (list_triggers);
- the run records in Activities. Only Zoya writes one today; the other routines' run records (decision 419, R-runrec) aren't live yet.

So each cause below is inferred from that evidence, not quoted from the transcript. The CTO can confirm each one with list_events on the session ids in the table.

## The four runs

| Run | Session | Length | Context used | Output | What it skipped |
|---|---|---|---|---|---|
| Evals 09:25 | session_019pwcV1XoyBE1NY8xpQ99qS (Cowork environment) | 5 min 39 s | 324k of a **500k** window (autocompact at 384k) | 44k tokens | the skill's own page (5 pages built by its own generator); STEPS 2b and 2c |
| WhatsApp 13:45 | session_019pwcV1tWfP1vbWmH8qhSS6 | 1 min 33 s | 140k of 1M | 3.6k tokens | STEP 3d, STEP 4 |
| Calendar 13:35 | session_019pwcV14JkJ16z9ApownMie | 59 s | 176k of 1M | 5.3k tokens | the Drive and Gmail evidence checks |
| Inbox 14:02 | session_019pwcV1rYbMFDHAZtdwCfx3 | 2 min 54 s | 267k of 1M | 14k tokens | STEP 7b |

All four run on claude-sonnet-5-5, and so does every routine except dossiers, which runs on claude-opus-5-5.

## Why each was skipped

**Evals: size and the model's choice, not time.**
- The five artifacts were published at 00:26:44, 00:27:58, 00:28:57, 00:29:40 and 00:30:29: one every 45 to 75 seconds.
- A real ft-guest-eval run does 6 to 10 web searches, a Drive search for precall notes, and builds the skill's Step 6 page. That can't fit in a minute.
- So the run didn't follow the skill. It wrote five pages from its own template ("FT Eval: <name>"), about 9k output tokens each.
- It stopped at 00:30:58 with 324k of its 500k window used. That's close to the 384k point where autocompact starts.
- The prompt asks for up to 5 new evals, 8 backfills and 5 re-runs in one run, each a full skill run. That doesn't fit a 500k window. The model shortened the work it could do and dropped what it couldn't (2b, 2c), without saying so.

**WhatsApp: ambiguity, and the model's choice.**
- The run used 1.5 minutes and 14% of its context, so neither time nor size explains it.
- STEP 3d and STEP 4 sit after STEP 3, which runs "once a day, on the first run of the JST day". Both do say "every run, even when STEP 3 is skipped".
- My guess is that a 13:45 run skipped STEP 3 and treated everything under it as skipped too. Reading the transcript would confirm or refute that.

**Calendar: the model's choice.**
- The run took 59 seconds, with 5k output tokens.
- The evidence checks sit inside STEP 4's "a finished calendar slot is not proof ... Look for evidence first". That reads as part of a step, not a step of its own.
- With no ledger to fill in, the run could treat "nothing changed" as done.

**Inbox: position at the tail.**
- STEP 7b (guest form submissions) is the last step before the report, after STEP 7's RSVP archiving.
- The run used 3 minutes and 27% of its context.
- The run decided it was finished before reaching the tail. This is the same pattern as the sweep on 23 Oct ("the 23 Oct run skipped STEPS 3b to 5 and still reported success"), which got its own Completed/Partial line. The other prompts never did.

**The common thread:** no run had to account for each step. A skipped step left no trace, so skipping cost the model nothing. Time and size (evals aside) weren't the cause.

## The shared fix, folded into decision 419's run record

One STEP LEDGER block, worded the same in every routine. It's added where R-runrec adds the run record, about 650 bytes per prompt:

> STEP LEDGER (decision 419). Every step of this prompt is either every-run or conditional (its own condition says when). The run record's body lists each step on its own line: "<STEP>: ran (<count>)", "<STEP>: not due (<the condition that was false>)" or "<STEP>: skipped (<reason>)". A skipped every-run step makes the run Partial. "Too much", "for brevity", "time" or "size" is never a reason unless it names a measured bound: elapsed minutes from Bash `date -u` since the start (the routine's own limit), or a cap this prompt sets. A step nested under a once-a-day step still runs when its own text says every run. Before the last write, check the ledger against this prompt's step list; a missing line is a skipped step.

**Each prompt also gets one line listing its steps,** so the ledger can be checked mechanically. For example: inbox "STEPS: 1, 2, 3, 4, 5, 6, 6a, 6b, 6c, 6d, 6e, 7, 7b, 8". The calendar list names the evidence check as its own step, "4e EVIDENCE", so it can't hide inside another step.

**For evals, two more sentences** (the CTO's own wording, plus a per-run budget):

> Publish only the skill's own page: the page the ft-guest-eval (or show) skill's Step 6 builds in this run, from a Skill tool call made for that guest in this run. Never write your own page generator or template, and never publish a page you built yourself; a page published without its own Skill call is a defect, reported as such.
> Per run: at most 2 new evals, 2 backfills and 1 re-run (was 5, 8 and 5), so each gets a full skill run inside the 500k window. What's left stays due and goes first next run.

**The calendar also needs its own line:** "4e EVIDENCE: for every finished precall or recording in the window, the Drive search (Gemini notes) and the Gmail search, each logged in the ledger with what it found."

## Cost and constraints

- **Size:** about 650 to 900 bytes per prompt.
  - The calendar, WhatsApp, sweep, evals, dossiers and host boards all have room.
  - The inbox doesn't: the Cleanup-accepted d420 inbox is 3 bytes under the build limit. It needs a cut of about 700 bytes first. Candidates are the MAILBOX paragraph, folded into a short pointer once the batch is live, and the HOURLY paragraph, which repeats the run-record rule.
- **Model:** evals runs where dossiers does, in the Cowork environment. Dossiers runs on Opus. Moving evals to Opus too, with its larger window and better step-following, is a cost decision for Akshay. The per-run caps above are the cheap version.

## How to check it once deployed

- **Run records:** for three days, every record has a ledger line for every step in its prompt's list. A run with a "skipped" every-run step is Partial, never Completed.
- **Evals:** each published page has a Skill call before it in the transcript, roughly 3 to 6 minutes per eval.
- **The morning check:** reads the ledgers, not the scheduler's "succeeded".

## Order

1. R-runrec (run records for every routine) plus this ledger, in one build.
2. The evals budget and the "skill's own page" rule ride in the same build.
3. The inbox cut and ledger follow, after the d420 inbox has been pasted live.
