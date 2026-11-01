# Inbox split: capture and actions (CTO, 1 Nov 18:35 JST; the 20 Oct audit's structural fix)

**Why.** The single 65 KB inbox prompt runs on Sonnet in about 2 minutes. It skipped Your call and every business step for a day, and justified each skip with the previous run's report. Two smaller routines, each with one job and a hard first step, replace it.

**Source.** `split.py` builds everything from the live prompt, 65,227 / 3bb46f9332241e3b (`docs/proposals/inbox-msgid/cleanup/inbox.txt`). Blocks are copied verbatim and located by their opening words, with each location asserted. `map.txt` lists every block and where it went. Only the lines marked "new" in `split.py` are new text.

## Files (each built twice, byte-identical)

| Routine | File | Bytes / sha256 |
|---|---|---|
| Inbox capture (the existing trigger, re-pointed) | `capture.txt` | 33,088 / 3df35d3de429dc49 |
| Inbox actions, **v2** (recommended) | `actions-v2.txt` | 37,705 / 137b9c7083f7125b |
| Inbox actions, v1 (everything in the prompt) | `actions.txt` | 41,554 / 523500f34027655c |
| Daily sweep (takes STEP 7b) | `sweep.txt` | 38,113 / 1ae5ff08c2dbfb9d (on the accepted d420 sweep, 35,047 / 06c4120b2cd48ef1) |
| Text for the Controls page (v2 only) | `yourcall-sections.md` | 4,276 / 6c23f51241fe6621 |

**v2 versus v1.** v1 keeps YOUR CALL and WHATSAPP TO AKSHAY in the prompt, which puts it over 40 KB. v2 moves those two blocks, word for word, to the existing Controls page "Inbox and Your call rules" (3ff19a301a7f8148993ccea78fc66428) as sections 6 and 7, and the prompt points to them. If that page can't be read in full, the run does nothing and ends Failed. That page already holds the snooze, owner and recording-happened rules Your call uses. The CTO pastes `yourcall-sections.md` there before cutover.

## What each routine does

**Inbox capture** (hourly at :02, the existing trigger):
- It logs each ad@ mail once, keyed `msgid:`. The Message-ID is read every time, one at a time, and never skipped.
- It links each mail to its Engagement or Deal and its People, and sets Last activity.
- It creates rows only for new pitches, outbound invites and proposed alternatives (decision 424 applies).
- It sends only the loop-in (STEPS 6 to 6b), archives RSVPs (STEP 7) and files episode assets (STEP 7c, moved from 6d).
- It never handles Your call, decides anything or moves a Status.

New rules in capture:
- **Cursor, not precedent:** it reads only "read to" and "pending" from the newest capture record, and never another run's report.
- **TIME:** start and end come from `date`.
- **SELF-CHECK:** any Activity this run created without `msgid:` goes to Trash, and the run ends Failed. Each worked message gets one ledger line.
- **STEP 0, one-off:** up to 15 `allmail:` rows a run.
  - If a `msgid:` row exists, the `allmail:` row is folded into it, then trashed.
  - If none exists, the row is re-keyed and linked, with Captured set to today so actions works it.
  - If no Message-ID can be read, the row is left and counted.

  It stops once there are none; at the last count there were 98.

**Inbox actions** (new trigger, hourly at :25, after capture):
- **STEP 0 Your call:** it runs every run, first and in full, before any mail.
- **Then the captured mail:** the mail Activities captured since its own record's "worked to", oldest first, at most 25 a run. Each gets:
  - STEP 2b (Akshay's sent mail);
  - STEP 3's status rules;
  - STEP 4 (Deals) and STEP 5 (waiting on);
  - STEP 6c (decision mails queued for Zoya with "## Decision mail");
  - STEP 6d (admin asks) and STEP 6e (holds, cancels, before-release notes, Akshay's list).
- It never searches the mailbox in bulk: it reads one THREAD only where a step needs the chain.
- It sends only WHATSAPP TO AKSHAY. Every mail goes through Zoya, as before.
- Its record keeps a ledger: "your call: n handled", plus one line per worked Activity. A missing line means Partial.

## What moved where (nothing dropped)

The full list is in `map.txt`.

**Shared by both prompts, verbatim:**
- TEAM ROLES, ZOYA LIVE, CADENCES, KIND and AKSHAY'S LIST;
- HARD RULES, NEXT DATE AND WAITING ON;
- WRITES and the data sources.

**Capture only:**
- MAILBOX (full), LOOP-IN, CONTEXT CHECK, BOUNCES and HOUSE COPIES: the loop-in is its only send.
- PEOPLE MATCH.
- STEPS 1, 2, Gemini notes, MATCHING PEOPLE and forwarded mail.
- STEP 3's three creating bullets: pitch, outbound and different guest.
- Stakeholders.
- STEPS 6, 6a, 6b and 7, and 6d's asset filing (as 7c).

**Actions only:**
- WORDING and YOUR CALL (v2: on the Controls page).
- WHATSAPP TO AKSHAY (v2: on the Controls page).
- STEP 2b and STEP 3's thirteen status bullets.
- Waiting on and Chase step.
- STEPS 4, 5, 6c, 6d (admin) and 6e.

**To the daily sweep:** STEP 7b, guest form submissions, verbatim, in Part B. It reads the Guest forms database, not mail, so once a day is enough.

**Rewritten:**
- 6e's release-date aside now follows decision 427 (Zoya's standard "Next steps and release date" reply), which replaced 155.
- 6e's recording-logistics bullet keeps the hand-off "Zoya: recording logistics reply to <who>". The reply's contents are Zoya's rules.
- Actions' MAILBOX is the THREAD and draft-delete part only.

**Not carried into actions** (not dropped: capture keeps them):
- CONTEXT CHECK, BOUNCES and HOUSE COPIES: actions sends no mail.
- PEOPLE MATCH: actions creates no People.

## Cutover plan

1. **Review:** Cleanup reviews `capture.txt`, `actions-v2.txt` and `sweep.txt` (or `actions.txt`, if v1 is chosen).
2. **Controls page (v2):** the CTO pastes `yourcall-sections.md` as sections 6 and 7 of "Inbox and Your call rules", then reads it back.
3. **Capture:** Akshay pastes `capture.txt` into the existing inbox trigger (trig_0189eZvAD8x4357cfevgZ3No), still disabled. Read it back byte for byte.
4. **Actions:** after Akshay's yes, the CTO creates the actions trigger, hourly at :25, with Notion, MCP Emails, Google Calendar and Blueticks attached. Akshay pastes `actions-v2.txt`. Read it back.
5. **Sweep:** paste `sweep.txt` into the daily sweep (if the sweep has moved on since the accepted d420 build, rebuild `sweep_7b.py` on it first).
6. **Enable both, capture first.**
   - **Watch the first capture run.** Its records should show: `msgid:` keys only; ledger lines; the `allmail:` counts falling; "read to" advancing.
   - **Watch the first actions run.** Its record should show "your call: 9 handled" (or what's left), with one line per worked mail.
7. **Rollback:** disable both new prompts and paste back the old inbox, 65,227 / 3bb46f9332241e3b, which is kept here unchanged. The old trigger is the capture trigger, so rollback is one paste plus re-enabling it.

**Order matters:** actions only works mail that capture has logged. While the `allmail:` backlog drains, Your call still runs first every hour.
