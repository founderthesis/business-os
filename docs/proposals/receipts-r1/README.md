# Run receipts on four routines (CTO, 3 Nov; Akshay: "ran", "completed business work" and "independently verified" stay separate)

**Inputs:** the live prompts, read back on 3 Nov with get_trigger (read-only), in `live/`. Each matches its last repo build.

**Build:** `patch.py` (`python3 patch.py live <out>`), every edit asserted once, built twice, byte-identical. The outputs are in `build/`.

| Routine | Trigger | Live | New |
|---|---|---|---|
| Calendar sync | trig_01Voiz5YsK2SnVf2STF8PoSH | 57,968 / f6d140196f3b75b4 | 60,052 / b1080b69814d8566 |
| Founder Thesis guest evals | trig_01R1yHgEztVEo832zMwUugBr | 14,795 / 1d87f124107a06c6 | 16,531 / cf15ed48886e8710 |
| WhatsApp to Business OS | trig_01MnmJYorWrd61K7b5BCqXr1 | 26,336 / ca8009c24aaeda15 | 28,430 / afcac744347f02f9 |
| Daily sweep | trig_01MdfUFg2qrebDWgiHwncgnd | 39,131 / 6783dd01e396e5ab | 40,914 / e5d2f31ba96fd37b |

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

## r1b (replay.json)

The replay confirmed every audited failure now ends Partial with a named skip. It also confirmed the diffs, sizes and deployment stamps, and found no behaviour change beyond receipts. Fixes:

| Item | Fix |
|---|---|
| Calendar: STEP 4b missing from the list | Added |
| Calendar: blank old markers still counted | STEP 1b's skip test counts a marker only when its page body has a "run <run id>" line. The blank 3 Nov 08 marker no longer counts, so that window is audited again |
| WhatsApp: overnight runs ending Partial | A post the prompt holds for quiet hours or its own timing is n/a, never a skip |
| Sweep: a same-day rerun lost the earlier lines | Reusing today's record keeps its earlier lines and adds this run's below "rerun <run id>" |
| Sweep: no Failed wording | The final Summary is STEP 7's first line, or "Sweep <A|B> <D Mon>: Failed: <why>" |

**For the CTO, sweep 3h b:** Mail issues has no Live date, so 3h b can't run and every Part B run will be Partial, naming it. Recommendation: add a Live date (date) field to Mail issues in the same deploy, rather than relabelling the step n/a, so Partial keeps its meaning.

**Lows left as listed in replay.json:**
- Failed and Partial overlap in wording.
- Step caps can read as "a sample".
- No-op is undefined.
- The good-morning check searches "Run <routine>", which doesn't match the sweep's "Sweep <A|B>" summary. Update CLAUDE.md's check, or search both.
- The "from what I know" tag is caught only if the run admits the 3g check wasn't made.

**Status:** written and replayed. Quick check of r1b pending. Nothing is deployed; the CTO deploys after Cleanup.
