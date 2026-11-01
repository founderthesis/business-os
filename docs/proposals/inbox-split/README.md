# Inbox split: capture and actions (CTO, 1 Nov 18:35 JST; the 20 Oct audit's structural fix)

**Why.** The single 65 KB inbox prompt runs on Sonnet in about 2 minutes. It skipped Your call and every business step for a day, and justified each skip with the previous run's report. Two smaller routines, each with one job and a hard first step, replace it.

**Source.** `split.py` builds everything from the live prompt, 65,227 / 3bb46f9332241e3b (`docs/proposals/inbox-msgid/cleanup/inbox.txt`). Blocks are copied verbatim and located by their opening words, with each location asserted. `map.txt` lists every block and where it went. Only the lines marked "new" in `split.py` are new text.

## Files (round 4; each built twice, byte-identical)

| Routine | File | Bytes / sha256 |
|---|---|---|
| Inbox capture (the existing trigger, re-pointed) | `capture.txt` | 35,819 / 787edd7ac6b8db54 |
| Inbox actions, **v2** (recommended) | `actions-v2.txt` | 39,304 / 10fd6e2a05c2e0ac |
| Inbox actions, v1 (everything in the prompt) | `actions.txt` | 45,703 / 6eff3115e8d58983 (over 40 KB: not for deploy) |
| Daily sweep (takes STEP 7b and PEOPLE MATCH) | `sweep.txt` | 39,131 / 6783dd01e396e5ab (on the accepted d420 sweep, 35,047 / 06c4120b2cd48ef1) |
| Text for the Controls page (v2 only) | `yourcall-sections.md` | 7,326 / a28b43da3b0aac36 |

**v2 versus v1.** v1 keeps everything in the prompt, which puts it over 40 KB. v2 moves three blocks, word for word, to the existing Controls page "Inbox and Your call rules" (3ff19a301a7f8148993ccea78fc66428): YOUR CALL (section 6), WHATSAPP TO AKSHAY (section 7) and STEP 6e's bucket B reply types (section 8). The page text ends with the line "END OF INBOX ACTIONS SECTIONS 6-8". A read without the three headings and that line counts as not full: the run does nothing and ends Failed. That page already holds the snooze, owner and recording-happened rules Your call uses. The CTO pastes `yourcall-sections.md` there before cutover.

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
- **STOP TIME:** no new message after :20.
- **SELF-CHECK:** of the Activities this run created (its ledger ids, never another routine's), any without `msgid:` goes to Trash, and the run ends Failed. Each worked message gets one ledger line.
- **Its rows are marked:** every mail Activity it creates, re-keys or links ends with the body line "capture: <run id>". A loop-in ends "actions: n/a (loop-in)" instead.
- **STEP 0, one-off:** up to 15 old rows a run. First `allmail:` rows, then the old inbox's unlinked `msgid:` mail rows (created since 29 Oct, Captured before 2 Nov, no Engagement and no Deal). Within each, oldest Captured first.
  - `allmail:` with a `msgid:` row: the links are copied over and read back, its relations cleared and checked, then it goes to Trash (decision 416).
  - `allmail:` with none: re-keyed to `msgid:` and linked.
  - `allmail:` with no Message-ID: the body line "allmail: no Message-ID <date>", left.
  - Unlinked `msgid:`: linked as STEPS 2 and 3 do.
  - Every row it touches gets Captured today. A row it leaves goes to the back of the queue, and actions finds the rows it re-keys or links.

  It stops once there are none; at the last count there were 83 `allmail:` rows and 84 unlinked rows.

**Inbox actions** (new trigger, hourly at :25, after capture):
- **STEP 0 Your call:** it runs every run, first and in full, before any mail.
- **Then the captured mail:** the mail Activities created at or after W minus 2 minutes, where W is the "worked to" of the newest actions record other than this run's that has one. Rows Captured since the day before W's date are added (capture's STEP 0 rows; they never move W). Oldest first, at most 25 a run, none started after :35.
  - Only capture's rows ("capture:" line), plus the old inbox's rows from before actions' first record (not Zoya's sends).
  - Skipped: anything already "actions: done" or "actions: stuck". A loop-in is closed as n/a.
  - Each worked row gets "actions: done <run id>". One it can't finish gets "actions: try <n>"; at 3 it's "actions: stuck <why>", goes in the report for Akshay, and stops holding W.
  - It does nothing if the previous actions record is still Started and under 60 minutes old.

  Each worked row gets:
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

**Not carried into actions** (not dropped: capture keeps them): CONTEXT CHECK, BOUNCES and HOUSE COPIES, because actions sends no mail. PEOPLE MATCH and the decision 424 attach rules are in both, because actions' STEP 4 can create People and Deals.

## Cutover plan

1. **Review:** Cleanup reviews `capture.txt`, `actions-v2.txt`, `yourcall-sections.md` and `sweep.txt`.
2. **Controls page (v2):** the CTO pastes `yourcall-sections.md` as sections 6 to 8 of "Inbox and Your call rules", ending with its END line, then reads it back.
3. **Capture:** Akshay pastes `capture.txt` into the existing inbox trigger (trig_0189eZvAD8x4357cfevgZ3No), still disabled. Read it back byte for byte.
4. **Actions:** after Akshay's yes, the CTO creates the actions trigger, hourly at :25, with Notion, MCP Emails, Google Calendar and Blueticks attached. Akshay pastes `actions-v2.txt`. Read it back.
5. **Sweep:** paste `sweep.txt` into the daily sweep (if the sweep has moved on since the accepted d420 build, rebuild `sweep_7b.py` on it first).
6. **Enable both, capture first.**
   - **Watch the first capture run.** Its records should show: `msgid:` keys only; ledger lines; the `allmail:` counts falling; "read to" advancing.
   - **Watch the first actions run.** Its record should show "your call: 9 handled" (or what's left), with one line per worked mail.
7. **Rollback:** disable both new prompts and paste back the old inbox, 65,227 / 3bb46f9332241e3b, which is kept here unchanged. The old trigger is the capture trigger, so rollback is one paste plus re-enabling it.

**Order matters:** actions only works mail that capture has logged. While the `allmail:` backlog drains, Your call still runs first every hour.

## Round 2 (replaySPLIT.json)

The first replay passed completeness and seven of eight cases. A1 failed. Fixes:

| Defect | Problem | Fix |
|---|---|---|
| D1 | Actions' cursor used Captured, a date field, so mail captured later the same day would be skipped | Its cursor is now the Activity's created time ("worked to", never past an unfinished one). Re-keyed allmail: rows are flagged "actions: due" in the body, and the flag becomes "actions: done <date>" when worked |
| D10 | Mail captured after the failures began fell outside actions' first window | The first run takes everything created since 29 Oct, 25 a run |
| D2 | STEP 2b's scope said "logged this run" | It now reads "among the mail Activities you work" |
| D3 | Capture's hard rules forbade its own Trash steps | They make an exception for STEP 0's and the SELF-CHECK's Trash steps (decision 416) |
| D4 | Some decision work stayed in capture, or had no home | Capture's intro hands Your call, decisions and the actions-only steps to actions, except the status moves its own creating bullets make. Actions gains decision 162's ok/no answer |
| D5 | Actions creates People and Deals without the matching rules | PEOPLE MATCH and the full STEP 3 head (decision 424) are back in actions |
| D6 | The sweep's 7b creates People without PEOPLE MATCH | The sweep gets PEOPLE MATCH with 7b |
| D7 | Capture's Activity didn't carry what edit notes need | Capture logs edit notes with the "Edit notes: <guest>" Summary and every requested change in the body. Filing and the reply stay with actions |
| D8 | "Can't read the Controls page" was ambiguous | Actions then skips STEP 0 and every mail step, and ends Failed |
| D9 | Stale cross-references could pull a run into the other routine's job | Each intro scopes them: capture leaves the actions-only references, and in actions "mail" means the worked Activities. Actions' MAILBOX allows a one-person or one-thread search, never a window |

**Size.** actions-v2 is now 39,710 B, under 40 KB but not by much. If more room is wanted, STEP 6e's bucket B detail (about 2 KB of reply types) can move to Rules for Zoya, where the replies are decided.


## Round 3 (Cleanup's verdict on round 2, `cleanup-verdict.md`)

| Item | Fix |
|---|---|
| B1 | W is the "worked to" of the newest actions record other than this run's that has one. worked to = the later of W and the newest closed cursor row, never past an open one; a run that closes none carries W |
| B2 | No body flag. Capture's STEP 0 sets Captured today; actions also takes rows Captured since the day before W's date, outside the cursor, so W never moves backward |
| B3 | Cursor rows are created at or after W minus 2 minutes. Every worked row gets "actions: done <run id>", and done rows are skipped |
| B4 | "actions: try <n>"; at 3, "actions: stuck <why>", reported for Akshay, and it no longer holds W |
| B5 | Capture marks loop-ins "actions: n/a (loop-in)"; actions closes any Summary ending "Zoya loop-in" as n/a, before STEP 2b or 5 can see it |
| B6 | The page ends "END OF INBOX ACTIONS SECTIONS 6-8"; actions needs the three headings and that line, or ends Failed |
| B7 | Actions' MAILBOX carries the gmail: to msgid: remap sentence |
| B8 | Actions never creates a mail Activity. Sponsored no: "leave it for capture, name it in the report". Edit notes: update capture's Activity, never a second one |
| B9 | A row STEP 0 leaves gets "allmail: no Message-ID <date>" and Captured today, so it goes to the back. The fold clears and checks relations before Trash |
| B10 | STEP 0 also links the old inbox's unlinked `msgid:` rows; actions doesn't take them until then |
| S1 | Actions works only capture's rows and the old inbox's pre-cutover rows (not "Zoya sent" ones). The old inbox also skipped any mail Zoya had logged first, so this keeps its behaviour |
| S2 | Capture: no new message after :20. Actions: none after :35, and nothing if the previous record is still Started and under 60 minutes old |
| S3 | 6c's cap of 15 counts mail only; Your call decisions are never capped |
| S4 | The WhatsApp to Akshay is logged first, keyed "wa-akshay:<row id>:<the Your call text's first 40 characters>"; a key already logged means it went. A failed send renames the row and clears the key. The prompt says the page never overrides this |
| S5 | SELF-CHECK covers only this run's ledger ids |
| S6 | The sweep gets the WRITES line with 7b |
| S7 | Recording logistics keeps "never questions, data asks or the dossier; skip any part a team member already answered on the thread" |
| S8 | "No partial work." is back in actions' TOOLS |
| S9 | Report "W to worked to"; actions' ZOYA LIVE "you queue, Zoya sends"; capture's ZOYA LIVE without WhatsApp; this README now matches STEP 0 |

**Room.** v2 needed about 1.7 KB for these fixes. It came from moving 6e's bucket B reply types (2.7 KB) to the Controls page as section 8, and from three lines actions doesn't need:
- OUTSIDE MAIL becomes QUIET HOURS for invite cancels, because actions sends no outside mail;
- personal mail (capture never logs it);
- LAST ACTIVITY (actions logs no mail).

v1 now has no use, so it isn't for deploy.

**Cutover additions.** The CTO pastes all of `yourcall-sections.md` (sections 6 to 8 and the end line) and reads it back. STEP 0's dates assume the old inbox stays off; if it runs again on or after 2 Nov, move "Captured before 2026-11-02" to the cutover date.

## Rounds 3b to 3d (offline replays `replay3.json`, `replay3b.json`, `replay3c.json`, `replay3d.json`)

The round 3 replay passed every B and S case but found new defects in the joins. Each one was fixed and replayed again:

| Defect | Fix |
|---|---|
| D1 SELF-CHECK trashed Gemini notes rows | It checks only Email in, Email out and Draft rows |
| D2, D2b Zoya's rows worked by actions | Actions works only rows with capture's "capture:" line. STEP 0 checks each old row in ad@ by Message-ID: not there means Zoya's, no line |
| D3, D3b The first run replayed mail the old inbox had worked | No W means W = 1 Nov 12:00 JST, when the old inbox began skipping steps. Old rows reach actions only once STEP 0 stamps them (created since then, or unlinked since 29 Oct) |
| D4 A repeat pitch could knock Akshay's "pitched again" ask off | Actions closes that pitch as n/a, and his ask stays |
| D5 Dead allmail: rows starved the unlinked rows | STEP 0 takes up to 8 rows per class |
| D6 The WhatsApp was logged twice | One row, logged before the send |
| D7 The overlap guard sat on the hourly gap | 45 minutes, and the skipped run writes a No-op record |
| D8 Gemini notes were never worked | Actions takes Gemini notes Meeting rows, which capture stamps. A missing THREAD is never a try |
| D9, D9b ad@ mail Zoya logged first was never worked | Capture's STEPS 1 and 2 add the "capture:" line to such a row, once. This is new: the old inbox skipped that mail |
| Stale text | HARD RULES name each routine's own mail actions (Calendar, Blueticks); 7c points to STEP 2; STEP 0's cap wording is fixed |

**Precondition:** deploy capture on or after 2 Nov JST. Round 4 defines today as the JST date in both prompts, so 2 Nov 00:00 JST is safe; without that, it would be 09:00 JST.

## Round 4 (Cleanup's verdict on round 3, `cleanup-verdict-round3.md`)

| Item | Fix |
|---|---|
| R1 Zoya's sends worked by actions | Capture's exception stamps only Kind Email in rows created since 1 Nov 12:00 JST, never a "Zoya sent" row. STEP 0 adds nothing to a "Zoya sent" row. Actions closes "Zoya sent" rows as n/a |
| R2 Capture's first run re-stamped the old inbox's rows | CURSOR and STEP 1 read the newest run:inbox-capture: record, else run:inbox: (the old inbox). Stamps are bounded by the 1 Nov 12:00 JST cut |
| R3 A crashing row froze actions | "actions: try <n> <run id>" is written before a row is started. A row with 3 tries goes stuck |
| R4 "Today" had no time zone | TIME in both prompts: today and every date written or compared are the JST date (`TZ=Asia/Tokyo date +%F`) |
| Overlap | The guard is 90 minutes, and actions starts no mail after :35 (Your call runs in full) |
| WhatsApp | Logged "Zoya sending:", renamed after the send; a "sending" row is checked in Blueticks before any resend |
| Dead allmail: rows | At the third "no Message-ID" line the row is re-keyed "allmail-unread:<same id>" and reported once |
| Captured provenance | Before STEP 0 changes Captured, it writes "first captured <old date>" in the body |
| STEP 0 slot | STEP 0 starts no row after :10 |
| Captured window | Actions' Captured branch takes only rows created before 2 Nov |
| Folded rows | Stamped only if created since 1 Nov 12:00 JST |
| Loop-ins in a thread | Never count as our side replying |
| Late stamps (replay4 A1, replacing a 2-hour hold) | Capture lists each id its STEP 1 exception stamps on its record's "stamped: <ids>" line. Actions takes the ids on that line in capture records created since W minus 2 hours, so a row stamped after W passed it is still worked |
| Akshay's mail Zoya logged first (replay4 R1b) | The exception covers Email in and Email out, never an Email out whose Summary starts "Zoya" |
| Outage tries (replay4 R3b) | A run ending Failed on a connector error removes its own try lines, so healthy rows don't go stuck |

**Section 8 wording.** Five of its six bullets are byte-exact from the live prompt. Recording logistics carries the two S7 sentences added in round 3.
