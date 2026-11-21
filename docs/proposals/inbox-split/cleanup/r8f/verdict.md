# Cleanup post-deploy review: capture r8f (f2685d8), 2 Nov ~13:45 JST

**Accepted as live.** No blocker. The capture is `r8f/capture.txt`, **40,650 / b034a489dd5e97d5**.

## Rebuild

- `r8f/patch.py r8e/capture.txt <out>`, run twice, gives 40,650 / b034a489dd5e97d5, byte-identical to the repo file.
- It's one insertion after STEP 0's "Start no row more than 8 minutes after the run's start.". No em-dashes are added.

## Live read-back

- The Inbox capture trigger (trig_0189eZvAD8x4357cfevgZ3No) is enabled, cron `2 7-23` JST, and its prompt contains the r8f sentence where the build puts it.
- The tool returned the prompt inside JSON. I checked it by content, not by an exact byte hash, so a byte compare by the deployer is still worth doing.

## The sentence

"Work LINK rows first (no RAW). STEP 0 is never skipped or judged too heavy: a run that works none of it while rows are due is Partial, "STEP 0 skipped", a defect; a slow row only waits for the next run."

- **It targets the 13:19 failure directly.** The model skipped STEP 0 as "too heavy". Now that's named as a defect, and the run record shows it ("STEP 0 skipped"), which is what the good-morning check reads.
- **"Work LINK rows first (no RAW)" fits LINK.** LINK goes by key, and the 13 stranded rows are cheap. Putting them first means a slow allmail: row can't starve them.
- **It doesn't conflict with the existing limits.**
  - STEP 0 runs before STEP 1, so "Start no row more than 8 minutes after the run's start" still bounds it.
  - "a slow row only waits for the next run" agrees with that.
  - The per-class limit (up to 5 of each, 15 in all) is unchanged.
- **Should-fix (follow-up):** a row that is slow every run (a heavy allmail: original) stays oldest and is taken first in its class each run, so it can eat each run's 8-minute window.
  - The "allmail: no Message-ID" third-try rule doesn't cover a slow row that does finish.
  - **Fix:** a row that hit the 8-minute stop gets "step0: slow <date>" and goes to the back of its class.

## Operational note

- The capture run was fired by hand at 13:37:45 JST (04:37:45Z) and is still running. That's inside the "never by hand between :35 and :50" rule, because the overlap guard doesn't cover Zoya's :38 run.
- Worth checking its record and Zoya's 13:38 record for overlapping writes on the same rows.

Nothing deployed by Cleanup.
