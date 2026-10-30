# Architecture audit: claims checked against source, 20 Oct 2026

The audit text itself was not available to this session. Its named claims (Evals prompt drift, schedules and models, retired-tool references, and the Beerud, CHEQ and Mohan cases) were checked directly.

**Sources:**
- Read directly by Main: the coordination page, the AR-3 calendar run metadata, and the three case rows after repair.
- Read by two read-only workers this session (their outputs are in the session scratchpad):
  - the routine inventory (list_triggers, live prompts hashed against the repo);
  - the case evidence (Notion, both mailboxes, the calendar).
- Inferred: marked where it appears.

## Routines (read directly from the scheduler by a worker)

| Routine | Schedule (JST) | Model | Live bytes / sha256[:16] | Matches repo |
|---|---|---|---|---|
| Inbox | 0 0,8,16,21 | sonnet-5-5 | 64,936 / b3f1e632a6a5a40a | yes |
| Host boards | 15 0,8,16,21 | sonnet-5-5 | 8,474 / 5819ccf7528ca16f | yes |
| Evals | 25 0,8,16,21 | sonnet-5-5 | 15,154 / e7530dfcfe1973fc | no (see below) |
| Zoya | 30 0,8,16,21 | sonnet-5-5 | 43,704 / 7f71e2302f155d6f | yes |
| Calendar | 35 8,16,22 | sonnet-5-5 | 54,862 / cd50072ab657736a | yes |
| WhatsApp | 45 * | sonnet-5-5 | 22,647 / d4c9986b750e9cbd | yes (privacy placeholders aside) |
| Daily sweep | 10 13 weekdays | sonnet-5-5 | 35,063 / f0bf956ef3253898 | yes |
| Dossiers | 50 6 daily | sonnet-5-5 | 5,487 / 68e94cb7d30ca645 | yes (trailing newline) |
| Community | 47 9 Saturdays | sonnet-5-5 | 4,168 / b521543d14266866 | yes |

- FT Newsjack is disabled (it was on claude-sonnet-5).
- All recurring last runs show SUCCEEDED. That is the scheduler status, not proof the work got done: the 08:35 calendar run "succeeded" during a Notion outage and wrote nothing.
- AR-6's hourly schedules are not installed.

## Evals drift (confirmed)

- **Live:** routines/cowork-evals.md at 74c038f (17 Oct), byte for byte.
- **Intended reviewed version:** docs/proposals/evals-prompt-2026-10-19.txt (14,779 B / 6432ff8b5c869992, commit 8745eea). docs/install-2026-10-19.md says to deploy it after cleanup accepts it. No cleanup acceptance is recorded, so it is not deployed.
- **The delta** (evals-live-vs-reviewed-2026-10-20.diff, 4 hunks):
  1. Gmail read-only.
  2. TEMPLATES removed; NO MAIL, WORK FIELDS and the Kind Task skip added.
  3. Mamatha mail steps b and f removed (including the old 100-send cap; decision 317 says 150), with step c gaining decisions 324, 326 and 328.
  4. Step references and the report line follow.
- **Risk while it stays live** (inferred): an eval run can mail by the retired Mamatha path, and doesn't skip Kind Task rows.
  - Mitigation in force: the UN# ON ZOYA override cancels the Mamatha steps on client shows. On FT the path is dormant (no Mamatha steps in use).

## Retired tools in live prompts

- **Live instructions:** "(Salesblink)" for cold outreach in inbox, calendar, sweep and Zoya, and Zoya's Salesblink hold in ONE PERSON, ONE ASK. AR-6 removes both and is prepared, not installed.
- **Dead or cancelled text:** Evals step f (Mamatha), inbox and calendar "Mamatha:" steps on client shows (overridden).
- **Read-only or forbid mentions** (harmless): Queue, make_eval.py, "Agent:", Blue Source IDs, FT: Today.
- **Not found:** Newsjack, podm.in/founders, the Tasks database.
- **Connectors still attached:** Salesblink and Blue on Evals and Dossiers (an owner UI step).

## Cases

| Case | Audit claim holds? | What the evidence shows | Repaired 20 Oct (Main) | Still open |
|---|---|---|---|---|
| Beerud Sheth, FT | yes | Next date 9 Nov with no source. The 7 Oct note set 21 Oct; three sibling rows carry 9 Nov, from an unlogged writer (inferred). The 12 Oct "Fix: no email" lead was overwritten. No duplicate sends. | Next date to 20 Oct (PR check due under the 5-working-day cadence), with a note | Fill People email and LinkedIn from the 23 Sep invite; Tier (Akshay's "tier 1", left blank deliberately); trace the 9 Nov writer |
| Guy Tytunovich (CHEQ), B2S | yes | Notion, the host board and the calendar say 20 Oct 19:00 JST. Mail moved it to 3 Nov, then a tentative 24 Nov. Guy declined the 20 Oct invite. Routines correctly left invites alone. The eval says "booked 20 Oct" (stale, nothing erased). Eval link empty. | Same-day decision put on Akshay's list: cancel or keep the 19:00 recording and Satish's 18:30 prep invite. "Guy (host)" corrected | Akshay's calendar decision before 18:30 JST; Next date once 24 Nov is confirmed; publish the eval page |
| Mohan Lakhamraju, FT | yes | The snooze was written to Next action (2 Nov) but Next date stayed 19 Oct. "Precall done" is wrong: on 20 Aug Akshay joined late and apologised. No Activities linked. No sends. | Next date to 2 Nov, with a note | Log the 20 Aug and 16 Oct facts as Activities; correct the precall status (Akshay's facts, not inferred) |
| Nupoor Mohan, FT | minor | Next action says 19 Oct, Next date 21 Oct (held under the 7-day rule) | none needed | none |

**Root causes these show** (consolidation 1 targets them):
- Several writers share one Next date and Next action.
- The snooze path wrote text without the date. AR-20261020-1 rev 2 fixes that path.
- Writers that don't log their changes.
