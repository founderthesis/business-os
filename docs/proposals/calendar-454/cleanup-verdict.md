# Cleanup verdict: calendar sync 454 (c02fe3f), 4 Nov ~09:00 JST

**Accepted. No blocker.** Deploy `calendar-454/calendar.txt`, **58,676 / a06a8b37924c60ad**, after byte-comparing the live prompt against f6d14019 as the handoff says.

## Rebuild

- `calendar-454/patch.py` on the live base, `d420/deploy/calendar-b1.txt` (57,968 / f6d140196f3b75b4, the B1 build Cleanup accepted), twice. It gives 58,676 / a06a8b37924c60ad, byte-identical, with no em-dashes.
- The only addresses in the file are ad@ and zoya@, which the committed prompts already carry.

## The changes

**454: prep event links.**
- Every run compares the private "Prep:" event's description with the row's Eval, Dossier, Prep note and LinkedIn links. It rewrites only the description, with Dossier and Prep note first, notificationLevel none.
- It's a private event with no guests, so this is an add, never a move.
- That's exactly why Sameet's 30 Oct event stayed stale.

**453: the day-before note.**
- With no recording link, the run drops the {call link} sentence and still sends or drafts the note. It never waits.
- The note stays a draft Akshay sends where his rules say so.

**445: Zencastr links.**
- zencastr.app.link counts as a Zencastr link in STEP 1, audit rule 4 and STEP 4e.
- Rule 4's no-link case is a Claude note only. Zoya's live STEP 0r (r15c) asks Mamatha and raises the 24-hour Akshay ask, so there's no duplicate ask.

## Should-fix (low)

"Compare every run" could rewrite the description when the same link is only formatted differently, say a trailing slash or tracking parameters. **Fix:** compare links with "?..." and a trailing "/" stripped.

Nothing deployed by Cleanup.
