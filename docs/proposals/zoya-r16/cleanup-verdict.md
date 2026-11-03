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
