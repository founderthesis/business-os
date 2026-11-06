# PaaS move: 33 Deals to Engagements (dry run)

Main, 6 Nov. Akshay approved on 6 Nov, 5/nov page item 7: "Start the movement, put template approval in my queue - both can happen in parallel". Scope is the CTO's: the PaaS page (40f19a301a7f81f2a5c0dba97ed29d14) and the item 7 comment.

This is read-only. Nothing was written to Notion. The CTO runs the write after Cleanup's review.

## Files

- `migration/paas_move.py`: the re-runnable script. `plan` builds the CSV and the plan from snapshots; `verify` checks a read-back.
- `dry-run.md` (and `dry-run.csv` locally; .gitignore keeps CSVs out): all 35 Deals with Warm or Slow, or Stage Parked, each with its mapping and include flag.
- `plan.json`: one op per moved row: the Engagement to create, its page body, the Activities to relink, and the Deal's Next action. Run with a placeholder Show id (all zeros), it comes out at sha256 721dc6f2b9eac806. Built twice, byte-identical.
- The snapshots are under `data/paas/` (git-ignored, since they hold people's names and Notion ids):
  1. **Deals:** `SELECT url, Company, Stage, "Warm or cold", Heat, Result, "Waiting on", "Next action", "date:Next date:start" AS next_date, "Proposal link", "Pitch note", Amount, "Budget read", "Last activity", Contacts, Organisation, Activities, "From engagement", "Source ID", Tags, "Chase step" FROM <Deals> WHERE "Warm or cold" IN ('Warm','Slow') OR Stage='Parked'`, saved as JSON.
  2. **People:** `SELECT url, Name, Tags FROM <People> WHERE url IN (<every Contacts url>)`.

## Counts (6 Nov)

- **Read:** 35. **Move:** 33. **Stay:** 2, DuploCloud and Latent AI, both Parked but Cold outreach.
- **By stage:**
  - In conversation: 7
  - Proposal sent: 10
  - New or Contacted, warm: 5
  - Parked: 7
  - Unresponsive: 2
  - Won: 2
- **Activities to relink:** 67. Each Activity gets the new Engagement added and keeps its Deal.
- **Problems:** 2. Codewave and Meanwhile have no Organisation on the Deal, so their Engagement goes without one too.

The rule is "Warm or cold is Warm or Slow, any Stage". It gives exactly the 33 in the CTO's 5 Nov count. The CTO's wording ("not Cold outreach New, Contacted or Unresponsive") would also take the two Parked Cold outreach rows, making 35. I left those two out to match the 33. Say if they should move.

## Status mapping (Engagements has no deal ladder)

| Deal Stage | Engagement Status | Why |
|---|---|---|
| New | New | |
| Contacted | Contacted | |
| Interested | Interested | none today |
| In conversation | Interested | the nearest "talking, no proposal yet" |
| Proposal sent | Decision pending | waiting on their decision |
| Parked | Parked | |
| Unresponsive | Unresponsive | |
| Won | Booked | signed and in delivery |
| Declined | They declined | none in the 33 |

The Deal Stage is kept in the page body, so nothing is lost.

## Each moved row

- **Name:** "<main contact> @ <Company>, PaaS".
- **Show:** PaaS. **Kind:** empty. **Direction:** empty, since "Outbound at New" would take Akshay off the row.
- **Status:** as mapped above.
- **Waiting on and Next action:** the Deal's own Next action and Waiting on (Mamatha dropped). An open row with neither gets "Akshay: next step for <company>? (moved from Deals 6 Nov)" and Akshay. Decision 496: there are no PaaS templates to wait for, and follow-ups surface as reminders on Akshay's list.
- **Next date:** the Deal's own.
- **Guest:** the first Contact who isn't tagged PR contact. **Stakeholders:** the other Contacts.
- **Organisation** and **Amount:** carried from the Deal.
- **Provenance:** Source Agent, Source ID "deal:<deal page id>", Captured today, Migration batch "paas-move-2026-11-06".
- **Claude note:** one line with the Stage-to-Status move and the Deal's Next action.
- **Page body:** "## PaaS deal (moved ...)" with the Deal link, Stage, Heat, Result, Proposal link, Pitch note, Budget read, Last activity, the Deal's Next action, its Source ID and the Chase step. Engagements has no Proposal link field; per low admin, I haven't added one.
- **The Deal row:** Next action becomes "Moved to Engagements <link>". Nothing else on it changes and nothing is deleted.

## Write steps for the CTO (one writer)

1. Create the Show "PaaS" (like AD Tasks), then re-run `plan` with its page id. Only `show_id` changes.
2. Per op:
   - First look for an Engagement with that Source ID. If one exists, reuse it; never create a second.
   - Create the row, then write its page body.
   - Add the Engagement to each listed Activity.
   - Set the Deal's Next action with the new row's link.
3. Read every row back into the JSON shape `verify` documents, then run `python3 migration/paas_move.py verify plan.json readback.json`. It must report 0 problems.
4. Reconcile: Engagements on Show PaaS = 33, and Deals whose Next action starts "Moved to Engagements" = 33.

## Before the write: a PaaS guard in the other routines

Every guest routine reads Engagements and will treat these 33 as podcast guests, for example:
- the sweep's Decision pending step (STEP 2) and its gone-quiet flags;
- inbox actions' chase and close rules;
- calendar's booking steps;
- capture linking mail to them as pitches.

Zoya is gated in r22. Nothing stops the others. I recommend one line in each, deployed before the move: "Rows on Show PaaS are production-service rows: no guest step, no eval, no chase, no status change by guest rules; mail on them is logged and anything it asks goes to Akshay's list." I haven't built it, because it's outside the ask. I can do it in one round on request.

## Rows to look at (none block the move)

- **Field Assist (Won):** a live client with 27 Activities and four open waits in its Next action (Divir's branding contact, Ashmita's payment date, the setup-fee invoice, the signed agreement). The single "Akshay:" segment replaces them, and the waits survive only in the Claude note and page body. Consider keeping those four segments on this one row.
- **Clairva.ai (Won):** content licensing, not production. Moving it to PaaS as Booked may not be right. Keep it in Deals or move it? Akshay's call.
- **Cygnet.One:** the Deal's contact is Niraj Hutheesing, the FT guest, but the PaaS conversation is with Kesha Shah, who isn't in Contacts. The Guest should probably be Kesha (People row not checked).
- **CapConnect:** Ankita Saha is tagged PR contact, so she stays a Stakeholder; Shauraya Bhutani is the Guest.
- **Entrust Family Office** and others with "From engagement": the FT guest row stays as it is. The PaaS row is a separate pursuit on a separate show, so one person can have both.
