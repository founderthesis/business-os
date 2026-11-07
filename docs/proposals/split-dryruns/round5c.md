# Round 5c: the scan window after a long lock outage (27 Oct, about 01:40 JST)

Two independent offline runs, A and B. Nothing was sent, written or pushed.

**Inputs:**
- Prompt: zoya-one 5ffcec2b6c1baf54.
- SLOW work file: 85d532e8d94c3c6a (9770ee8, pinned to d0216f5).
- Scenarios: round5c/scenarios.json (ded3600de71d3292).

| Scenario | A | B | Outcome both runs gave |
|---|---|---|---|
| I3, crash while holding the lock, 31-hour outage | PASS | PASS | The scan reaches back to 26 Oct 10:38, the earliest run that took the lock since the last Completed one; 23 Skipped records don't count. It finds the 26 Oct 10:41 send, the one candidate. Logged once, not resent. 1 Activity |
| SKIP, lock held | PASS | PASS | Reads only git, the run id and the Activities data source; one write, the Skipped record; the reply stays due |

**Scenario error (mine):** the added inbound and sent mail were dated 27 Oct, while the narrative says 26 Oct. Both runs followed the narrative. Run B notes that with the mismatched dates, a send dated before its inbound would have no candidate. This is a test-data fault, not prompt behaviour: a reply can't predate the mail it answers.

**Wording fixed after this round (prompt only):** RUN RECORD said "Right after LOCK (and in its step 3), one Activity ... Started", against LOCK step 3's "created once (never Started first)". Both runs settled it by step 3. It now reads "Once you hold the lock, one Activity". That changes the prompt only: zoya-one 40,240 / 06c1f070ab2dae89, same pin, and the SLOW work file is unchanged. It is wording only, so Cleanup decides whether SKIP is re-run.

**Noted, unchanged:**
- **Only a Completed record closes the scan window**, so a No-op run doesn't. That is a wider scan, which is safe.
- **A run that took the lock but crashed before its Started record** is invisible to the window. The 24-hour floor still applies, and the runbook's reconcile step covers the rest.
- **A recovered revenue mail missing Jaya and Sarika** is reported, never resent.
