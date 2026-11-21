# Inbox ignores its prompt: diagnosis and the smallest structural fix

Asked by the CTO (1 Nov, 18:20 JST). This is a read-only proposal: nothing is built yet.

## What the 18:02 run did

Run session_019pwcV2mo8Puo1FD3dqpEkz, on the live prompt 65,227 / 3bb46f9332241e3b. Its run record is 40b19a301a7f818cb964c66f752b4221.

This session has no list_events tool, so it can't read the transcript. These facts come from the session record and the run record:
- **It took 2 minutes 4 seconds** (09:02:41 to 09:04:45Z). The record says "end about 18:20 JST", which is guessed. The inbox has no TIME rule.
- **It used about 10 model calls** (1.82M cache reads at roughly 170k context) and wrote 8,503 output tokens. Context ended at 190k of 1M.
- **It did one search, then wrote 15 Activities and the record.** Two minutes isn't enough to fetch 15 `original`s one at a time and match 15 rows. So the prompt's IDENTITY and STEPS 3 to 6e weren't attempted, not attempted and failed.
- **Its report explains itself by precedent:** "Same limits as earlier Partial runs: allmail keys used (Message-ID headers not read), no People or Engagement matching ..., no Your call sweep". Those are the 12:12 to 17:03 runs' words. STEP 1 tells the run to read the newest run record, and the run read its body as well as its "read to" and "pending" lines.

## Why

1. **The previous record is a template.** STEP 1 sends the run to the newest record. Its body reports what the last run skipped and why. A model under load copies it as the house standard, so each bad run licenses the next.
2. **Nothing checks the work against the rules.** The record is free text. A run that creates 15 provider-keyed rows and skips every step can still write "Partial" with a reason, and nothing counts what it skipped.
3. **Your call has no fixed slot.** The rule says "before STEP 1", but it sits mid-prompt in a 3 KB block. Nothing makes it visible that it ran.
4. **The prompt is at the cap and the model is Sonnet.** Every routine except dossiers runs on claude-sonnet-5-5. On a 65 KB prompt it takes the shortest path it can justify.

## The fix (about 1,300 bytes added, about 3,000 freed)

**(a) Records are a cursor, not a precedent.** STEP 1:
> From the newest inbox run record read only its Summary's "read to" and its body's first line ("pending: ..."). Never read or cite another run's report: what earlier runs skipped is never a reason to skip.

About 200 bytes.

**(b) A hard STEP 0 for Your call.** Move YOUR CALL's first sentence into a new first step:
> STEP 0. YOUR CALL, before STEP 1 reads any mail: handle every Engagement with Your call not empty (YOUR CALL); the record's body line 2 is "your call: <n> handled, <n> left (<why>)".

About 220 bytes. The YOUR CALL rules block stays where it is.

**(c) A ledger per message, and a self-check before the last write.**
> Each worked message gets one body line: "<msgid>: Activity <id>; row <name> | none (<why>); steps 3 to 6e: done | n/a (<why>)". Before the last write, query Activities captured today, created after the start, Kind Email in or Email out: any whose Source ID doesn't start "msgid:" is moved to Trash (it has no relations yet, decision 416) and the run ends Failed: "<n> rows without msgid: trashed". A ledger line missing for a worked message is a skipped step: Partial, never Completed.

About 600 bytes.

**(d) TIME, as in Zoya:**
> start and end from Bash `date -u`, never estimated.

About 150 bytes.

**(e) Freeing room: move STEP 7b to the daily sweep.** Guest form submissions don't depend on mail: they read the Guest forms database. That frees 3,014 bytes. The sweep has about 29 KB of room and already counts Guest form rows in STEP 5. The step text moves unchanged into sweep Part B, which then covers it once a day instead of hourly.

**Net:** about 65,227 + 1,170 − 3,014 ≈ 63,400 bytes. That leaves about 1.9 KB of room under the build limit, the first real headroom since 28 Oct.

## For Akshay (cost)

The inbox runs 17 times a day on Sonnet. The dossiers routine already runs on Opus. On this evidence (2-minute runs on a 65 KB prompt, copying precedent), moving the inbox to Opus would likely do more for compliance than any wording. It costs more per run. Akshay decides.

## Tests (offline replay, before Cleanup)

1. **Precedent:** the newest record's body says "allmail keys used, no STEPS 3 to 6e". The run must read only "read to" and "pending", and must not repeat the limits.
2. **Your call first:** nine Your call rows. They're handled before any mail search, and line 2 counts them.
3. **Ledger:** 15 messages, each with a ledger line and STEPS 3 to 6e. One message gets no row match, so its line says "none (why)".
4. **Self-check:** a run that creates an `allmail:` row trashes it and ends Failed.
5. **STEP 7b moved:** the sweep's Part B runs it, and the inbox no longer mentions guest forms except to point to the sweep.
