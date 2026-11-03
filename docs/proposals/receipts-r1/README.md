# Run receipts on four routines (CTO, 3 Nov; Akshay: "ran", "completed business work" and "independently verified" stay separate)

**Inputs:** the live prompts, read back on 3 Nov with get_trigger (read-only), in `live/`. Each matches its last repo build.

**Build:** `patch.py` (`python3 patch.py live <out>`), every edit asserted once, built twice, byte-identical. The outputs are in `build/`.

| Routine | Trigger | Live | New |
|---|---|---|---|
| Calendar sync | trig_01Voiz5YsK2SnVf2STF8PoSH | 57,968 / f6d140196f3b75b4 | 59,970 / 8503ea145e702df9 |
| Founder Thesis guest evals | trig_01R1yHgEztVEo832zMwUugBr | 14,795 / 1d87f124107a06c6 | 16,531 / cf15ed48886e8710 |
| WhatsApp to Business OS | trig_01MnmJYorWrd61K7b5BCqXr1 | 26,336 / ca8009c24aaeda15 | 28,350 / c5bb8b95d5ffc5e3 |
| Daily sweep | trig_01MdfUFg2qrebDWgiHwncgnd | 39,131 / 6783dd01e396e5ab | 40,789 / 31f1f5a025e17513 |

All four are under the cap.

## What each gets

**The same RUN RECORD block, from capture (decision 419):**
- the run id, fixed once;
- a "Started" record before any other Notion write, then a final status;
- in the body: "run <id>", "deployment <routine> <12-hex version>", start and end from `date -u`, one line per step ("STEP <n>: done <count> | skipped (<reason>) | n/a (<why>)"), counts, errors as the tool gave them, then the report;
- the routine's list of mandatory steps.

**Status rules:**
- Completed only when every mandatory step is done or n/a.
- A skipped, cut-short or "lighter pass" step (a sample, a light pass, checks not made) is Partial, whatever the reason.
- "done" means every item the step selects. A check not made is never written as done.

**Per routine:**
- **Calendar:**
  - Mandatory: STEPS 1, 1a, 2, 3, 3b, 4a, 4, 4f, 4e, 4c, 4d and 5, each with its per-item Notion and Drive checks.
  - STEP 1b runs once per window, or is "n/a (window <08|16|22> audited by <run id>)".
  - The audit marker "Calendar audit done: <date> <window> JST" now has the page body "run <run id>" and one line per finding (or "no findings"). A marker without them is never written.
- **Evals:** STEPS 1, 2, 2b, 2c and 3 every run. 2b and 2c run even when STEP 1 finds nothing.
- **WhatsApp:**
  - Mandatory: STEP 0 with 0a2, 0b, 0c and 0d, and STEPS 1, 2, 2b, 3d, 4 and 5.
  - STEP 3 on the first run of the JST day only; other runs record "n/a".
  - Every create names its parent data source and is fetched back. The record has "creates: <n> confirmed in their data source, <n> not", and one not confirmed makes the run Partial.
- **Sweep:**
  - Its existing report Activity ("sweep:<A|B>:<today>") becomes the run record, created or reused first as "Started"; its final Summary is STEP 7's first line.
  - Mandatory: every step of the run's part, with STEP 4 row by row.
  - A check that can't run is "skipped (<what is missing>)". For example, 3h b while Mail issues has no Live date. That makes Part B Partial until the field exists. This is deliberate, so it shows; the CTO decides whether to add the field.

## Not changed (out of this build's scope)

- **The sweep's verify-or-blank rule:** it tagged a guest "from what I know". That's a behaviour rule, not a receipt. Flagged for the next sweep change.

**Status:** written. Replay pending (`replay.json`). Nothing is deployed; the CTO deploys after Cleanup.
