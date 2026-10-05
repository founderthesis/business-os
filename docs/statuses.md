# Statuses

One field, one ladder. Proposed 5 Oct 2026 after reading every status value in the FT Pipeline sheet (counts in `data/out/ft_pipeline_statuses.md`, not committed). Replaces the Stage + Outcome pair and the status columns listed at the end. Not applied in Notion until Akshay agrees.

## What the sheet actually tracks

The FT Pipeline sheet holds 1,009 guest rows across Inbound (673), P1 (209), Paid (13), FT Cold Lead (154) and VC Intros (34), plus 1,631 PaaS rows. Its "Status" columns mix three different things:

| It is really | Raw values (count) |
|---|---|
| Where the guest is on the journey | TBD 108, Precall Scheduled 2, To be Scheduled 14, Scheduled 13, Recorded 2, Form Filled 89, Paid-tab milestones (planning call, recording scheduled, released) |
| What Akshay decided | Sponsored 53, Paid 7, P1 62, P2 47, Add to outbound 13; and in the free-text route column: Sponsored 117, Preliminary call 87, Commercials shared 84, Akshay has to decide 19 |
| How it ended or stalled | Declined 288, Unresponsive 136, Chase 16, LT Chase 17, Maybe Later 4, Propsed Alt 11 |

The eval verdict lives in a fourth column (373 readable labels: Decline 160, Evaluate after call 107, Strong consider 80, Book immediately 26; another 96 are links or doc titles). PaaS tabs are 95 to 99 percent blank.

So the guest journey, as the team actually runs it, is: pitch in, eval, Akshay decides, then one of three paths (precall, sponsored offer, book), then recording, then the Episode takes over. Rows stall (chase, park) or end (decline, no response, dropped out) at any point.

## The new field: Status

One select on Engagements. Mamatha reads and sets this column and nothing else; the agent sets it where it can.

### Guest journey (Guest inbound, Guest outbound)

| Status | Means | Set by | What happens next |
|---|---|---|---|
| New | Pitch received, or target approved for outreach | Agent (inbox), Mamatha | Agent runs the guest eval |
| Evaluating | Eval requested or running | Agent | Eval lands on the Decision Desk |
| Decision pending | Eval done, Akshay has not decided | Agent | Card on the Decision Desk; nothing moves until a Choice |
| Precall | Precall offered, scheduled or done. Next date = the call | Agent on Choice = Precall, Mamatha | After the call, agent sets Decision pending again for the post-call verdict |
| Sponsored offer | Commercials shared, waiting on them | Agent on Choice = Sponsored, Mamatha | Chase ladder runs; a yes moves to Booking with Amount set |
| Booking | Yes to record, date not yet fixed | Agent on Choice = Book, Mamatha | Mamatha fixes the slot; for sponsored, invoice goes out (Paid = Invoiced) |
| Booked | Recording date set. Next date = recording | Mamatha, or agent from the calendar | Episode row created; dossier runs 2 days before |
| Recorded | Recording done | Agent from the calendar | Thank-you and PR form go out; form chasers run; Episode status carries production. This is the last active status |
| Parked | Not now, revisit on Next date | Mamatha, Akshay by comment | Reminder on Next date, then back to the right status |
| Declined | We said no, or they did | Agent on Choice = Decline, Mamatha | Closed |
| No response | Chase ladder exhausted | Agent | Closed; a reply reopens it |
| Dropped out | Agreed, then fell through, or a substitute guest was proposed | Mamatha | Closed; the substitute gets a New row |

"Done" is not a guest status. Released lives on the Episode (Status = Published). The engagement stops at Recorded.

### BD journey (PaaS, Sponsor, Partner, Client, Vendor)

Same field, the BD values stay as they are: New, Contacted, In conversation, Proposal sent, Agreed, then Parked, Declined, No response, Dropped out. Heat (Hot, Warm, Cold) stays for PaaS only.

### Reading it

- Open pipeline = Status is not Parked, Declined, No response or Dropped out, and not Recorded.
- Mamatha's work = open rows sorted by Next date. Next action says what.
- Anything with no Next date and an open status is a gap the agent flags.

## What this replaces

| Today | Becomes |
|---|---|
| Stage (Identified, Contacted, In conversation, Proposal sent, Agreed) | Status. Guests never used these names; BD keeps them |
| Outcome (Live, Done, Declined, No response, Dropped out) | Status. Live and Done move to the Episode; the three ended values stay |
| Whose move | Removed. No person tagging; each person owns a show or a list |
| Host verdict | Kept for un#, B2S and HBD only. Hidden on FT views |
| Paid-tab milestones (7 checkboxes) | Status (Precall, Booked, Recorded), Paid (Not due, Invoiced, Part paid, Paid), Amount, Episode Published |
| P1 / P2 | P1 = whatever active status the row is at. P2 = Parked |
| Sheet "Next action - AD" and route column | Decision (Sponsored, Precall, Book, Decline, Present to host), set from the Decision Desk |

Kept as they are: Decision (Akshay's call), Eval verdict (the agent's), Eval link, Dossier link, Next action, Next date, Chase step, Amount, Paid.

## Mapping the sheet into Status

| Raw (count) | Status | Also set |
|---|---|---|
| TBD (108), "Akshay has to decide" | Decision pending | |
| Precall Scheduled (2), route "Preliminary call" or "Asked for pre call" | Precall | Decision = Precall |
| Sponsored (53), route "Sponsored" or "Commercials shared" | Sponsored offer | Decision = Sponsored |
| Paid (7), Paid tab rows | Booking, Booked or Recorded by milestone | Decision = Sponsored, Amount, Paid |
| To be Scheduled (14) | Booking | Decision = Book |
| Scheduled (13) | Booked | Decision = Book, Next date = recording |
| Recorded (2), Form Filled (89) | Recorded | Episode row; Guest form in = true for Form Filled |
| P1 (62) on Inbound | Status from the matching P1 row; Decision pending if none | |
| P2 (47), Maybe Later (4), LT Chase (17), Later (1) | Parked | Next date from the sheet, else 90 days |
| Chase (16), Interested (4), warm (9), Emailed (5) | Stay at the status they were chasing from; Chase step from the follow-up column | |
| Add to outbound (13), Approved (154 cold leads), Cold (52) | New | Type = Guest outbound or PaaS |
| Declined (288), Reject (6) | Declined | |
| Unresponsive (136), Bounced (8) | No response | Bounced also tags the email invalid |
| Propsed Alt (11) | Dropped out | Substitute becomes a New row |

The eval column maps to Eval verdict where it is a label, and to Eval link where it is a URL. Doc titles (173 rows) get neither; the enrichment routine looks them up later.

## Open questions for Akshay

1. One Status field for guests and BD, or keep BD on its own Stage? One field is simpler to read; two keeps the BD board untouched.
2. Does "Decision pending" need to be visible to Mamatha, or should those rows sit only on the Decision Desk until decided?
3. Sponsored guests: does Booking wait for the first payment, as the Paid tab implies, or can the slot be fixed first?
