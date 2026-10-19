# AR-20261019-1: acceptance walkthroughs (traced against the patch and payload, 19 Oct)

These are traced against docs/proposals/ar20261019-1-nurture-2026-10-19.patch and the payload, not run. "Zoya" means the patched routines/zoya.md, "sweep" the patched daily-sweep, "5a" the new Rules for Zoya section.

| # | Case | Trace | Sends |
|---|---|---|---|
| N1 | Silent sponsored lead, day 61 (PR-routed). | Staleness gate: 60 silent days. Moved to nurture: LT chase, Waiting on Zoya, Next date +30 days, "Zoya: nurture <PR>: sponsored feature (last contact, nurture 1)". Routine 7 picks it on that date with routine 8's angles, to the PR. | Nothing today; nurture mail 1 in 30 days. |
| N2 | Tier 1 precall, after mail 13 (day 300), still silent. | A14 "Close the loop" is not sent. Last step leads to nurture; 30/60/90, then every 120 days, then every 180 after 2 years. | No "last note" mail. |
| N3 | Tier 2 precall, sequence C ends. | C4 close-out is not sent. It's an approved pursuit (Precall requested), so it moves to nurture. | Slow nurture. |
| N4 | LT chase row 2 years in, silent. | Routine 7 "Ends" is now only on a 5a stop. Cadence goes to every 180 days. | Twice a year. |
| N5 | Sweep: 3 unanswered chases on an FT Booking row. | Approved pursuit: LT chase, Waiting on Zoya (no longer Guest or PR), Next date +30, nurture step. | Via Zoya, in 30 days. |
| N6 | Sweep: 3 unanswered chases on a never-approved inbound pitch (eval Decline, no Tier). | Not an approved pursuit, so Unresponsive as before. | None. |
| P1 | Beerud (FT Booking, PR Satv, last PR mail 7 Oct "busy a couple of weeks"). | PR coordination active (PR wrote within 30 days, not booked): next mail 5 working days after the last real exchange. The 15 Oct loop-in doesn't count, so it's due now. Guest travel doesn't stop a check with the PR. The 9 Nov Next date is not a confirmed slot; cleanup reconciles the field from the thread. | A check with Satv, once cleanup confirms the thread. |
| P2 | PR replies "hold till 15 Nov". | Their date wins: Next date 15 Nov, hold noted. | None until 15 Nov. |
| P3 | 5 working days across a weekend and Diwali week. | Weekdays only, never Diwali week. | Pushed past the week. |
| P4 | Our last message was an internal loop-in. | Loop-ins and thanks don't count as the last real ask. Counted from the ask before. | As per the rule. |
| P5 | PR silent 31 days. | PR coordination ends; the page's slower schedule takes over, then nurture. | Slower. |
| X1 | Sparsh: FT Booking plus B2S held by Satish ("no invite, Salesblink or follow-up until re-approved", 18 Oct). | One person, one ask: the B2S hold is a Standing hold on that row and never activates through FT. The FT row checks the other rows: B2S has no open ask (held), so FT may proceed if due, under its own rules. | FT only, if due; B2S nothing. |
| X2 | Same person: FT row due and a B2S Salesblink sequence active. | Is in a Salesblink sequence, so wait; Next date moves past it. | None. |
| X3 | Same person, FT mail 3 days ago, un# nurture due today. | Another row wrote in the last 14 days (nurture), so wait. | None. |
| R1 | HBD Tier 1 outbound, Unresponsive, never replied (Salesblink cold). | Revival needs cleanup's "eligible" line; a target who never wrote back stays with cold outreach. Not revived. | None. |
| R2 | FT Tier 1 inbound, closed Unresponsive by silence, real past exchange; cleanup marks eligible. | Sweep 3r re-reads Standing and other rows, then moves it to nurture with cleanup's reason and date (at most 5 a day). Zoya sends a contextual routine 7 mail. | One revival mail on cleanup's date. |
| R3 | Prior guest with a completed Episode, Tier 1. | Never revived as a booking; routine 9 only. | None from revival. |
| S1 | Genuine decline ("not interested"). | They declined, close note once, stop. Never re-pitched through another show. | Close note only. |
| S2 | "Please don't contact me again." | Standing "no contact", Parked. All rows for that person stop. | None. |
| S3 | Requested later revisit ("ping me in March"). | Their date wins: Next date in March, nurture resumes then. | None till March. |
| S4 | Akshay parks the row. | Parked, never followed up (section 7). | None. |
| S5 | No-show waiting on Akshay. | A decision on this pursuit by Akshay blocks it; no rebook mail until he answers. | None. |
| O1 | Sankalp or Amit Patni: Recorded, Waiting on Akshay for the community add, guest form due. | Zoya's new skip rule: Akshay's community add is an independent ask, so the form chase still goes (AR-2's separate-obligation contract). | Form chase. |
| O2 | Waiting on Akshay for a sponsored counter-offer. | A decision on this pursuit, so skipped. | None. |
| Z1 | Second run the same day. | Steps are never sent twice (Chase step and thread dates). Nurture moves are already done. Sweep 3r skips rows with "revival started". | None new. |
| Z2 | Crash after the move to nurture, before the report. | The row state is on the row; the next run reads it and carries on. | No duplicate. |
| C1 | Cap: 150 a day reached. | Nurture and revival mails count in the cap and the 10-a-run limit; the rest wait, reported. | Deferred. |

## Known limits for cleanup's review

- The Engagements SQL can't read eval page bodies, so a Tier 1 that lives only in an eval (Beerud) isn't found by query. The named cases (Beerud, Aravind) and source checks cover it; the structured Tier stays as Akshay set it.
- "Approved pursuit" includes every Precall requested and Booking row. That's Akshay's earlier approval of a precall or booking, not a new one.
- The inbox gets only the shorter three-chase text (65,269 B). Nurture execution is Zoya's; state moves are the sweep's.
