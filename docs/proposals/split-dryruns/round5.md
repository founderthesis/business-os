# Round 5: the one-writer build (27 Oct, about 01:10 JST)

Two independent offline runs, A and B. Nothing was sent, written or pushed.

**Inputs:**
- Prompt: zoya-one acc12bf038e76cf3.
- SLOW work file: 461f6c4e79bb98b3 (c1669fd, pinned to 2636857).
- Snapshot: 3537b3e5c7ca55de.
- Scenarios: round5/scenarios.json (fa17d02ac2a89d7c).

Outputs are in round5/.

| Scenario | A | B | Outcome both runs gave |
|---|---|---|---|
| C contact holds (10:38) | PASS | PASS | Ronit sent To Payal, Cc Akshay, Next date 3 Nov. Vijay held with a 7-day recheck. Amit and Devesh not due |
| D cap (10:38) | PASS | PASS | 40 sent, 5 left due unchanged; Partial |
| E several asks (11:38) | PASS | PASS | One mail: next steps plus the holding line for the crew-cost ask. That ask goes to Akshay beside its open reply segment |
| G sponsored yes (10:38) | PASS | PASS | One reply To Jheel, Cc Akshay, Jaya, Sarika; Next date 29 Oct |
| R1 thank-you (412) | PASS | PASS | Draft in ad@ as a new mail, To Riya, Cc Kabir, Neha and Zoya, no attachment, "(draft ready)". It doesn't wait on the Episode |
| R2 recording unclear (411) | PASS | PASS | One Akshay ask; a holding reply to the PR; no WhatsApp; Next date 27 Oct, not the recording date |
| R3 recipients (413) | PASS | PASS | To Sreya; Cc Akshay, Rajmohan, Santhosh, Mala; Mamatha and Zoya left out |
| I3 crash while holding the lock | PASS | PASS | 10:38 to 16:38 each write only "Skipped: lock held by ...". After the runbook's release, the 17:38 run finds the one candidate, logs it and the inbound, and doesn't resend. 1 Activity |
| I4 two candidates | PASS | PASS | Both actions held under one Akshay segment naming both mails; nothing logged or resent |
| SKIP lock held | PASS | PASS | Reads only git and the run id; one write, the "Skipped" run record; the reply stays due |

**Fixed in d-split26t:**
1. The Notion rules read said "before anything else", against LOCK's "before ANY other read". LOCK comes first now.
2. A skipped run's record is created once, as Skipped. It is no longer created as Started and then rewritten.
3. The 24-hour Sent scan would miss a crashed send once the lock had been held for more than a day. It now reaches back to the start of the latest run that didn't end Completed.
4. `@@VERSION@@` was left unfilled. build_one.py now stamps it, as build.py does.

**Noted, unchanged:**
- **No Status after a mailed sponsored yes:** blocked, a rule change for the CTO and Akshay.
- **The yes wording's precall line when a precall already happened:** the CONTEXT CHECK drops it.
- **A recovered revenue mail missing Jaya and Sarika:** recovery can't re-send. It is reported.
- **A held ask goes unanswered until Akshay settles it:** the cost of decision 414.
- **A lock outage skips the day's SLOW runs:** the follow-ups slip; nothing is lost.
- **Data:** Payal's two People rows (blocked), and Devesh's 9 Nov Next date in Diwali week.

These changes move the hashes, so SKIP, I3 and G are re-run twice on the new pin (round 5b).
