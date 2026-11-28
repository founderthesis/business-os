# Cleanup post-deploy check: Zoya SLOW live prompt, and dossier STEP 1 (decision 466)

Cleanup session, 4 Nov 2026, about 17:20 JST. Read-only: get_trigger on both tasks, one Notion query, get_session on the fired run. Nothing deployed, nothing sent.

## 1. Zoya SLOW live prompt (trig_015i1JzfyNDoYfrgTfbqDSXu)

Content match to docs/proposals/zoya-r18/zoya-slow.txt (12,985 bytes, sha256 3378858b38b24c0b). This is not a byte hash: get_trigger returned the prompt inline in JSON for this session too, so I checked by content.

- Same 31-line paragraph structure, same section order (PREFLIGHT, TOOLS, LOCK 1 to 4 and RELEASE, RUN RECORD, SLOW FILE, HARD RULES with all 14 bullets).
- Load-bearing values match: pin sha 513d32cb0a754dc381a4092dcb9d43f5732225c8, file hash prefix a3335c1abd10b006, total 81,455 characters, deployment reference "zoya-slow c5be6872d5d3", --force-with-lease on both pushes, no "+" refspec.
- updated_at 07:42:38Z (16:42 JST), after the pin move and before the 17:08 run. Model claude-opus-5-5, cron CRON_TZ=Asia/Tokyo 8 8,11,17 * * 1-5, enabled.

Verdict: live = r18 as far as an inline read can show. If someone needs a byte hash, the next SLOW run's record line "slow file: ... sha a3335c1abd10b006" proves the file, and a session whose get_trigger saves to a file can hash the prompt.

## 2. Dossier routine STEP 1 sentence (trig_01WfLf8Zx9c34fSzfrTeUY5M, decision 466)

The sentence matches decisions.md row 466. Accepted after the fact, with one watch item and two should-fixes.

What holds:
- Rebuilds once, no loop. STEP 2e writes "YYYY-MM-DD: dossier built (<skill>)" dated today, which ends the condition. On failure STEP 2f writes "dossier failed", so the row comes back next run. That's the existing retry for every show, capped at 3 rows per run.
- Scope is right: un# only, inside STEP 1's Booked, Recording, next-21-days filter. Two rows qualify today: Adrian Cachinero Vasiljevic (5 Nov 13:00Z) and Ryan Louvar (16 Nov).
- Same-link republish works. Ryan's republish landed on his existing Dossier link (claude.ai/artifact/2vudZbtfZegDQemp1gXCq6, run artifact updated 07:51Z). So the host's Podcast prep invite keeps working.
- Status, Next date, Waiting on and Next action stay untouched (2e). Nothing goes to guests. On un#, the prep note feeds the day-before mail, and Akshay sends that by hand from a draft.

Watch item (time-critical): Adrian records tomorrow, 5 Nov 22:00 JST. His row has no "dossier built" line dated 4 Nov or later, so he qualifies and should have gone first ("soonest recording first"). But the only dossier artifact the fired run (cse_019pwcV3nDxJ3YzztfYEBCzw) shows so far is Ryan's. The run was still RUNNING when I checked. CTO: when it ends, confirm Adrian's Claude note has "2026-11-04: dossier built (un-dossier)" and his Dossier link is still claude.ai/artifact/Lo8sC4Q46fkjXL6qE3TT5K. If it doesn't, the 06:50 JST run on 5 Nov picks him up, still before the recording. If that run fails too, it's a handover to Akshay under decision 459.

Also: Adrian's day-before draft (in Akshay's Drafts) already carries the old prep note. The rebuild rewrites the prep note page, not that draft. If the note changes, the calendar routine or Akshay has to refresh the draft before sending.

Should-fix (next edit of this prompt, not urgent):
- S1. Read before you republish. The Artifact tool refuses a publish to a URL the session hasn't read, and hands back the live version instead. An unattended run could treat that refusal as "publish failed", fall back to a new page and change the link. Add "read the current Dossier link first (Artifact action read), then publish with that url". Ryan's run shows it can work, but the fallback path is still open.
- S2. This is a one-off rule, so sunset it. Once both rows show a 4 Nov or later build, take the sentence out (any un# dossier built from now on is dated 4 Nov or later anyway). Otherwise it stays in the prompt as dead text. The Claude note can also lose lines in an overwrite (Adrian's 2 Nov line records exactly that), which would trigger one more rebuild. Harmless, but another reason to remove it.
