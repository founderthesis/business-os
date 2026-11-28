# Cleanup verdict: Zoya r16 (7169c68, SLOW file 8a3f733; decisions 456 and the 445 follow-up), 4 Nov ~09:20 JST

**Not accepted. Three blockers.** Stay on r15c. Each fix is short, and the replay is in `cleanup/replay-cleanup.json`.

## Rebuild

- A worktree at f70901f with `zoya-r16/build_one.patch`, then `build_one.py ... 8a3f733`, twice. All three files are byte-identical to the repo:

| File | Bytes / sha256 |
|---|---|
| zoya-one | 53,588 / e49b4170b842b5c3 |
| zoya-slow | 12,515 / 728358a1d8c8464e |
| SLOW file | 78,719 / 274cd09057943c0b (= `git show 8a3f733:...`) |

- There are no em-dashes, and 8a3f733 descends from b732cb3.

## The diff against r15c

- **FAST:** line 80 changes (the correction clause, and the link add after a hand send), plus the version.
- **SLOW task:** only the pin, the hash and the version.
- **SLOW file:** line 54 (INTERNAL TASKS a and c, and the 376 line) and line 66 (the WhatsApp example).

Three changes have no decision behind them:
- correction-wins replacement of the invite link (445 says "an add, never a move");
- "or anyone tagged Team" (456 names Mamatha);
- unbounded follow-ups to Mamatha.

## Blockers

**B1. A file is attached to the Episode before it's tested** (SLOW file line 54, c).
- The order is "Else attach the .txt to the Episode's Transcript file ... then write '## Transcript'" and only after that "(3) ... decision 374's test".
- So any file from "Mamatha (or anyone tagged Team)" that's matched by guest name gets filed as the transcript, and can replace a real one. Examples: Sarika's edit notes, Jaya's invoice, or a precall Meet transcript Akshay forwards.
- **Worse:** a precall transcript passes 374 (both voices, 20+ minutes). So Booked flips to Recorded and the thank-you is drafted before the recording happens.
- **Fix:** the transcript comes from Mamatha only; the recording's date is past (not a precall); the 374 test runs **before** attaching; and an existing Transcript file is never replaced. A mismatch goes to Akshay's list.

**B2. A transcript found outside the selection has no key or done marker.**
- Line 54 c files a transcript that "reaches your inbox from Mamatha ... on any thread ... none: file it on the Episode all the same". But SELECT FIRST (line 82) builds the batch "from metadata only", so that file gets no item, key or outcome.
- A model that reads the inbox anyway has no marker telling it the file is done, so it re-attaches and rewrites "## Transcript" every SLOW run.
- **Fix:** key the item as `transcript-file:<Message-ID>:<file name>` from its logged Activity. It's done when the Episode's "## Transcript" sha matches.

**B3. The recording-link correction rule contradicts the invite rules** (FAST lines 80 and 107).
- "her correction wins: the invite and Call link take the new link" conflicts with "location the link if empty", "never move, remove or change anything else" and "Call link to the link if empty".
- Either the wrong room stays on the invite (Sameet's failure again), or the model improvises edits to an event with guests.
- Also, a hand-sent old link with no Activity isn't "already done" for the new link, so the Else branch sends a second mail.
- **Fix:**
  - state the exact replacement: the old zencastr.app.link URL in location, description and Call link becomes the new one, notificationLevel ALL, nothing else touched;
  - test "already done" per guest and event, not per link;
  - log the replace-on-correction rule as a decision row, since 445 says add-only.

## Should-fix

1. **Look on the Episode before asking.** LOOK BEFORE ASKING never checks the Episode, so Saket's transcript, already filed, gets asked for again.
2. **Exclude `transcript:` rows from step b,** so Ranjita isn't chased before step a takes the row back.
3. **Bound the follow-up to Mamatha.** "one follow-up ... and Next date 2 working days on again" never ends. Make it one follow-up, then Akshay's list.
4. **Report an event you can't edit once,** not every hour.
5. **Retire "Ranjita" from transcript requests before deploy:** the Rules for Zoya wording, calendar 4f and sweep 3i still say "ask Ranjita".

## What holds

- No new team WhatsApp. The team-hours gate (line 66) is intact, so the 08:08 run still sends none.
- LOCK, RULES LOAD, the caps, PRE-SEND and the Z1 and Z2 quote rules are unchanged.
- The zencastr link appears only in that guest's mail and invite.

Nothing deployed by Cleanup.

## Addendum: decision 460

The rebuild after the blockers should also replace the 2 occurrences of "AD Personal" in the SLOW file with "AD Tasks": the scope line, and the routine 4 line. It's wording only, with the same page id. FAST and the SLOW task have none.

## Addendum: the first live SLOW run, 4 Nov 14:01 JST

The record is 40e19a301a7f817bbf32d3db8cb7a599. All five defects are present in the live r15c SLOW file (b732cb3), and r16 doesn't fix any of them. Fold them into Main's r16 rebuild, alongside B1 to B3.

**1. The loop-in reply went to ad@ alone (Taj Agra). Main's fix.**
- **The text:** the loop-in path says "email_compose action reply on the latest message from the person you address (a reply goes to its sender)". On a thread where Akshay wrote last, the model picked his message, so reply's default put ad@ in To.
- **Fix:** every loop-in goes the draft way the other branch already uses: draft action reply, draft update to set To and Cc from the PRE-SEND recipients, read back, draft send. Never send through email_compose reply's own default. Shared text: FAST and SLOW.

**2. The batch skipped STEP 0, payments, edit notes and internal tasks. Main's fix.**
- **The text:** line 83's classes are "(1) imminent recording logistics; (2) payments ...; (3) commitments with a promised date, today's owner mail and the Monday scorecard; (4) the oldest eligible follow-ups, then any other item".
- Feedback (0b), vendor forms (0d), edit notes and internal tasks sit in "any other", behind every follow-up. That's the starvation I flagged as L1 on r15b. Payments were class 2 but still weren't reached, so check how they were selected: a 1b payment item may not be keyed as eligible at all.
- **Fix:** make class 3 "STEP 0 (owner mail, feedback, vendor forms), STEP 1b payments not yet in (2), edit notes, internal team tasks, promised dates, the scorecard", before (4) follow-ups.

**3. The outcome check passed with writes missing. Main's fix.**
- 4 completed rows had no Claude note line, and two loop-ins used non-standard idempotency keys. The python counts outcome lines but can't see Notion.
- **Fix:**
  - A "completed" line must carry `act:<Activity id>` and `note:<row id> <YYYY-MM-DD>` from a read-back of the row (its top Claude note line dated today).
  - A send's `key:` must be printed on the line, and the python checks it against `^loopin:<Message-ID>$`, or the action-key form for Zoya mail.
  - A completed line missing any of these counts as unfinished.

**4. "FAST reserve missing on Cadences".** Not a file defect.
- Line 84 already defaults: "no reserve on Cadences: SLOW stops 30 short of the daily cap and the report says 'FAST reserve missing on Cadences'". So 150 less 30 is 120, exactly as built.
- **Fix:** add the reserve line to Cadences (the CTO). The file needs no change.

**5. The loop-in carried a sponsored chase from ad@. I agree with the CTO's reading.**
- Decision 421's "Optionally the ask in a few words" means restating their open ask. It never means a chase of our own offer from Akshay's address, which breaks the 15 Oct rule ("I need to protect my dignity": Zoya sends every follow-up).
- **Fix, in the shared LOOP-IN text** (FAST, SLOW and capture's loop-in):

  > Optionally their open ask in a few words; never our chase, offer or reminder: a chase goes from your own inbox after the loop-in, as its own action

- Log it as a one-line clarification of 421 in decisions.md.

**Minor: the ✨ in Cremica's plain text came out as mojibake. Main's fix.**
- Likely the plain-text body went through a Bash heredoc or echo.
- **Fix:** pass both bodies straight in the tool arguments as UTF-8, never through Bash. The read-back checks that the plain text ends "best,\nZoya ✨".

Nothing deployed by Cleanup.
