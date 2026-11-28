# Cleanup verdict: inbox split round 2 (d6243c5), 1 Nov

**Not accepted.** There are 10 blocking defects and 9 should-fix, all wording fixes Main can make in one round. Nothing is deployed. The split itself is sound: nothing is dropped or reworded without saying so. The defects are in the new joins between capture, actions and Zoya.

## 1. Rebuilt twice: bytes and hashes match

| File | Bytes / sha256 |
|---|---|
| capture.txt | 33,626 / c2054076f189667a |
| actions-v2.txt | 39,710 / 54f7b98bb5a7e506 |
| actions.txt (v1) | 43,545 / 05b3596c1ba66e7f |
| yourcall-sections.md | 4,276 / 6c23f51241fe6621 |
| step7b.txt | 3,734 / 6ae42bbf26586cbf |
| map.txt | 2,613 / ad0ceadc8b0dfc8f |
| sweep.txt (on d420 `deploy/sweep.txt`, 06c4120b) | 38,837 / e7716b9e2d0346f2 |

**Source.** I read the live inbox trigger back at 10:2xZ: 65,227 / 3bb46f9332241e3b, now disabled. That is the input `split.py` asserts.

## 2. Completeness (`cleanup/completeness.json`)

**The check.** Every source sentence and line was tested verbatim against the outputs.
- 25 source units are missing from v2 (25 from v1). Each one is a marked rewrite in `split.py` or the README, or the STEP 7b move. None is unexplained.
- All 93 new units in v2 (86 in v1) come from `split.py`'s NEW constants or its replacements.
- YOUR CALL and WHATSAPP TO AKSHAY are byte-exact in `yourcall-sections.md`.
- STEP 7b is byte-exact in step7b.txt and in the sweep.
- Em-dashes: none added. The sweep's one is pre-existing.

**But rules didn't follow the text that needs them.** These are defects B7 and B8 below, and S7 and S8.

## Blocking

**B1. The actions cursor resets to 29 Oct every run.**
- Actions takes mail "created after the newest record's 'worked to' (none yet: created since 2026-10-29)".
- But RUN RECORD writes this run's own "Started" record before any other write. The newest record is therefore always the run's own, which has no worked to. A Failed, No-op or crashed run leaves the same gap.
- Capture gets this right: "the newest inbox run record that has one".
- **Fix:** "the newest actions record other than this run's that has a worked to".

**B2. The "actions: due" flag can't be queried, and it pulls the cursor backward.**
- The flag is a page-body line, and a Notion data-source query can't filter on body text. So the re-keyed `allmail:` rows are never selected.
- When one is found, its old created time plus "oldest first" and "never past one you didn't finish" drags worked to backward.
- **Fix:** capture's STEP 0 sets Captured to today, as the README already says. Actions takes "Captured on or after the worked-to date, body without 'actions: done'". Worked to never moves backward: flagged rows are worked outside the cursor.

**B3. Mail created in the same minute is lost, and nothing marks a mail done.**
- Notion's created time is rounded to the minute, and "created after" is strict. An Activity that capture or Zoya creates in the same minute as the last one worked is skipped.
- Only re-keyed rows get a done mark, so a re-read can work a mail twice.
- **Fix:** take mail "at or after worked to minus 2 minutes", and write "actions: done <run id>" on every Activity worked. Skip any that already carries that line.

**B4. One stuck Activity freezes the actions cursor.**
- "'worked to' never passes a mail you didn't finish". This is the same failure mode as the `mcp:` pending fix in the msgid rev.
- One unreadable thread holds the cursor, and the 24 rows behind it are re-worked every hour.
- **Fix:** after 3 runs, mark it "actions: stuck <reason>", report it, and let the cursor pass.

**B5. Capture's loop-ins read as Akshay's replies.**
- The loop-in is logged as Kind Email out. Actions' STEP 2b (Akshay's sent mail) and STEP 5 ("our side replied, ball in their court") treat it as his reply.
- On a repeat pitch, that takes Akshay off "Akshay: <guest> pitched again".
- In the single prompt, the loop-in was logged after STEP 2b had run, so this didn't happen.
- **Fix:** actions skips Activities whose Summary ends "Zoya loop-in", or capture marks their body "actions: n/a (loop-in)".

**B6. The fail-closed check can't tell a partial read of the Controls page.**
- "Page not readable in full ... end Failed" has nothing to check against. A truncated fetch, or a section 6 or 7 that someone edited, reads as complete.
- **Fix:** end section 7 with "END OF INBOX ACTIONS SECTIONS 6-7". Actions requires both headings ("## 6. Your call", "## 7.") and that line, or it ends Failed. A sha in the line would be better still.

**B7. Actions creates Deals with the old key.**
- STEP 4 still writes Source ID "gmail:<thread id>".
- The MAILBOX remap that makes it "msgid:<the first message's Message-ID>" went to capture only.
- **Fix:** copy that one remap sentence into actions' MAILBOX.

**B8. Actions can create Activities outside IDENTITY.**
- The sponsored-no bullet says "(one found but not logged: log it with its message id)". Actions has no IDENTITY or RAW rule, so this reopens the non-`msgid:` rows.
- The edit-notes bullet still says "Log the Activity with Summary starting 'Edit notes: <guest>'", which makes a second Activity. Capture already logs it (D7).
- **Fix:** in actions, "a mail not logged yet: leave it for capture and note it". Make edit notes "update the captured Activity".

**B9. STEP 0 stalls on rows it can't read.**
- STEP 0 takes "up to 15 ... oldest Date first", and a row with "No Message-ID: leave it and count it" stays the oldest.
- Rows that can't be read, or heavy rows waiting behind the 2-a-run limit, come back first every run. 15 of them stop STEP 0 completely.
- **Fix:** a row it leaves gets the body line "allmail: no Message-ID <date>", and STEP 0 takes unmarked rows first.
- The fold also needs decision 416's check: after copying links, clear the `allmail:` row's remaining relations and confirm none are left, then Trash it.

**B10. The 84 unlinked `msgid:` mail rows have no owner.**
- Main's read-only reconciliation (664d922; the CTO calls it Cleanup's, but it isn't) counted 83 `allmail:` rows (98 at the README's last count) and 84 Email Activities since 29 Oct with no Engagement and no Deal (its class D).
- STEP 0 covers only `allmail:` rows. Actions works whatever it's given, but never links an Activity that came in unlinked, and capture links only at create time.
- So those 84 rows reach actions' first run with nothing to act on, and its status rules do nothing.
- **Fix:** extend STEP 0 to "msgid: Email Activities since 29 Oct with no Engagement and no Deal: link as STEPS 2 and 3 do, Captured today", or name the one-off reconciliation as their owner before cutover.

## Should-fix

**S1. Zoya's own mail.** Zoya logs her sends and her inbox mail as `msgid:` Email Activities. Actions works them at :25, before her :38 run. 6e can cancel a hold, or bucket C can put Akshay on the list, for mail she owns. **Fix:** skip Activities whose author or Summary is Zoya's, unless the old inbox handled them (state which).

**S2. Overlap guards.** There's no lock and no stop time.
- **Fix:** capture starts no new message after :20. Actions starts no new mail after :35. Actions does nothing if the previous actions record is still "Started" and under 60 minutes old.
- Otherwise two overlapping runs can each send the WhatsApp to Akshay, and read-then-write-back of Waiting on can lose an update.

**S3. Your call is capped by 6c.** STEP 0's ok's go through 6c's "At most 15 per run". That contradicts "first and in full". **Fix:** exempt Your call, or have the record say "left (6c cap)".

**S4. A WhatsApp resend.** The WhatsApp to Akshay goes out before Your call is cleared or anything is logged, so a failure in between resends it next hour. **Fix:** log first, or key it by row and the Your call text.

**S5. SELF-CHECK isn't scoped to capture's own rows.** It queries every Email Activity created after the start, so a row from Zoya or a chat session without `msgid:` gets trashed and the run ends Failed. **Fix:** "created by this run (the ids in its ledger)".

**S6. The sweep has no WRITES rule.** No create names its data source parent; this was already true of the accepted d420 sweep. The moved 7b now creates People rows and Form Activities there, which is the 29 Oct parentless-create bug. **Fix:** copy the WRITES line in with 7b.

**S7. Recording logistics.** The 6e rewrite drops "Never send questions, data asks or the dossier.", "Skip any part a team member already answered on the thread." and the PREP NOTE tips, on the ground that Rules for Zoya covers them. The repo Zoya prompt only says "recording logistics". **Fix:** confirm on the Notion page before cutover, or keep the two sentences.

**S8.** Actions' TOOLS line lost "No partial work.". **Fix:** restore it.

**S9. Stale text.**
- Actions' STEP 8 says "window by Captured time", but the cursor is created time.
- Actions' ZOYA LIVE says "capture-only".
- Capture's ZOYA LIVE still lists "and WHATSAPP TO AKSHAY".
- The README says "Captured set to today", but STEP 0 writes a body line instead. B2's fix makes the README right.

## What passes

- Actions' STEP 0 is "every run, first and in full", and only 6c's cap (S3) shortens it.
- Capture never touches Your call ("You never handle Your call").
- Capture's cursor survived intact: read to, pending, `mcp:` never holding it, 2 heavy reads a run, a cap of 15, and "cursor, not precedent".
- PEOPLE MATCH and decision 424 are in every routine that creates People or Engagements.
- Never-mark-read is in both routines.

## Recommendation

- **v2 over v1**, once B6 is in.
- **Round 3:** B1 to B10 plus S1 to S9. Then replay B1 to B5, B9 and S2 before cutover.
- **Until then:** the live inbox stays disabled, as it is now. The rollback build, 65,227 / 3bb46f9332241e3b, is unchanged.
