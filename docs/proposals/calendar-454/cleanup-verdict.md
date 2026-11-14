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

## Addendum: decision 460 (AD Personal renamed AD Tasks; same page id)

- **Accepted as a pure text substitution.** Replace all 4 occurrences of "AD Personal" with "AD Tasks", and change nothing else.
- **Result:** 58,664 / a2ea9c6d5c2e4363, from 58,676 / a06a8b37.
  - Built as `s.replace("AD Personal", "AD Tasks")` on `calendar-454/calendar.txt`.
  - Deploy that, or a byte-identical build of it.
- **The page id is unchanged** (3fa19a301a7f81638e55d12684ccad16), so this doesn't change behaviour. New personal rows are just named "<Person>, AD Tasks".
- **Old rows already named "..., AD Personal"** keep their names. Nothing matches rows by that suffix, because matching is by the page id and the Show relation.
