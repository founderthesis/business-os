# AR-20261019-1: Notion payload for nurture and revival (exact before and after)

These go onto Rules for Zoya (3f719a301a7f81a09de3ee3ad6ad98a3) and five routine pages. They are live controls: Zoya reads them every run. Nothing here is applied until cleanup accepts it. It is applied together with the prompt change (Zoya, daily sweep, inbox), never one without the other. Two equivalent patch files carry that change: ar20261019-1-on-live.patch, built on today's live prompts, and ar20261019-1-nurture-2026-10-19.patch, built on the end of the pending chain. Both come from ar20261019-1-build.py. The routine prompts end up identical in either order, with one textual catch: this change and AR-8 both edit Zoya's REPORT line. If nurture ships first, AR-8 applies from ar8-run-reporting-after-nurture.patch (the same AR-8 change, rebased; checked to give byte-identical prompts).

No mail wording changes. Nurture and revival mails use the live angles of routines 7 and 8, adapted to the thread under decision 152. The close-out mails stop being sent; none is re-worded, so decision 238 needs no new test.

## A. Rules for Zoya

### A1. New section, inserted after section 5's routine page links and before "## 6. WhatsApp"
After (new):
> ## 5a. Nurture and revival (AR-20261019-1, Akshay, 19 Oct)
> **Controls.** Zoya, the daily sweep and the inbox carry these rules; this section is the master copy. Silence never ends a relationship: Zoya keeps in touch for years until there's a clear no, slowing down when nobody answers and speeding up when someone does.
> **Approved pursuit:** a row at Precall requested, Sponsored offered, Booking or LT chase, or with Tier 1, or one Akshay asked to nurture. A booked call and a decision waiting on Akshay are not chases.
> **Guard, before any move to nurture (every routine):** re-read the row, its calendar and its thread, then take exactly one branch.
> - **Preserve and stop.** A precall or recording on the calendar, a decision Akshay or Jaya holds on this pursuit (a verdict after a precall, a price, an offer, a no-show), or a dated host or show hold. Nothing on the row changes: Status, Call type, Waiting on, Next action and Next date stay. A precall stays a precall; it's never relabelled a booked recording.
> - **Already in nurture.** Nothing restarts; a chase count only resets Chase step to 0.
> - **Approved pursuit.** It moves to nurture (below).
> - **Anything else.** The routine's own closing rule, as before (three unanswered chases: Unresponsive).
> - In every branch, only the chase part of Next action can change. Other asks, their owners and independent obligations stay.
>
> | Situation | Next mail |
> |---|---|
> | A PR team is coordinating a precall or recording that isn't booked, and their side wrote in the last 30 days | 5 working days after the last real ask or exchange (a loop-in, a thanks or an out-of-office doesn't count). Weekdays only, never Diwali week. Their requested hold or date wins. |
> | Within a routine's schedule | The routine page's dates. |
> | The routine has run out (last step, span over, 60 silent days on a sponsored offer, our last mail a close-out, or 3 unanswered chases) | Nurture mail 1: 30 days after our last mail on the thread. |
> | After nurture mail n is sent | Mail n+1 is due 60 days after mail 1, 90 days after mail 2, then 120 days after each, and 180 days once the nurture start is 2 years old. |
> | They reply, give a date, or there's a real new opening (verified news, an episode on their topic) | Back on the active routine, or on their date; that nurture spell ends. |
>
> **Nurture state comes from what happened, not a typed counter:**
> - The start is the Claude note line "nurture started (\<why\>)". For a row already at LT chase before 20 Oct 2026, it's the date it first went to LT chase, else 20 Oct 2026.
> - n is the number of "Zoya sent: nurture" Activities since the start.
> - Only a send moves n or the date the next interval counts from. A run that sends nothing (the cap, a deferral, a failure) changes only Next date, with a reason.
>
> **What nurture looks like on the row:**
> - Status LT chase, Zoya added to Waiting on, Chase step 0.
> - Next date = the next contact.
> - The chase part of Next action reads "Zoya: nurture \<recipient\>: \<the open ask\> (since \<D Mon YYYY\>)".
> - So every row reads as one of: scheduled (Waiting on Zoya with a Next date), held (a hold with a revisit date), blocked (Parked, or no contact), needs a decision (Waiting on Akshay for this pursuit), inactive (Unresponsive, or never-contacted outbound), or done (Recorded onward).
>
> **After a send:**
> - **Check first.** A mail counts as sent once it's in Sent or on the thread. Before any send or retry, Zoya looks there. If she finds one, she sends nothing and completes whatever of the writes below is missing, never a second Activity for the same message. If writing the row fails, only the write is retried, never the mail.
> - **Every send:** one Email out Activity with the provider's sent message id, Last activity, Zoya added to Waiting on (other owners stay), and only her own part of Next action replaced.
> - **Ordinary step:** Activity "Zoya sent: \<routine\> step \<n\> to \<name\>", Chase step n, Next date the next step's date.
> - **Nurture mail:** Activity "Zoya sent: nurture \<n\> to \<name\>", Chase step 0, Next date the send date plus the interval for n. The nurture part of Next action keeps its "(since \<start\>)".
> - **Nothing sent:** not due changes nothing. A cap, deferral or failed send moves only Next date, with the reason.
>
> **The mails.** Routine 7's angles (routine 8's for sponsored rows, to whoever owns the thread), adapted to the thread. Each gives one clear next step and a true reason to write, never invents news or urgency, and never repeats an angle to the same person. The close-out mails are not sent: sponsored 14, precall A14, B8 and C4.
>
> **Stops, which send nothing:**
> - a clear decline (They declined, with the close note);
> - a no-contact request from that person, anywhere ("## Standing", Claude note, Your call or the thread; Status Parked). It stops every row of that person.
> - Akshay's decline or park;
> - a no-show waiting on Akshay;
> - a dated host or show hold (wherever it's written). It stops only that show's row, revisit on its date.
>
> An old Unresponsive label or our own close-out mail is not a decline. A show hold is never worked round through another show. A declined offer is never re-pitched through another show, contact or channel.
> **One person, one ask.** Before a mail, Zoya reads the recipient's other rows on every show. She holds this mail only for:
> - a mail to them from any row in the last 7 days (14 for nurture or revival);
> - an active Salesblink sequence to them (rechecked at its next step or end);
> - the same ask already open on another row.
>
> When two rows are due for the same person on the same day, the more urgent one goes (booked-call logistics, then PR coordination, then an active routine, then nurture). The other waits 7 days after that send. A Recorded or finished row elsewhere is context, never a reason to wait. Every hold writes a recheck Next date and the reason ("deferred: \<row\>, \<why\>, recheck \<D Mon\>") and never changes n.
> **Revival of Tier 1 conversations, inbound or outbound:**
> - **Who:** owner-approved Tier 1 rows closed by silence (Unresponsive, or LT chase gone quiet). Akshay's own decision is what makes a row Tier 1, never a model's suggestion.
> - **Gate:** cleanup source-checks each candidate and marks eligible ones in the Claude note: "revival checked \<date\> (cleanup): eligible, \<reason\>".
> - **Start:** the daily sweep starts nurture on each marked row (at most 5 a day). If the person was written to in the last 14 days, it starts after that, noted as a deferral.
> - **Never revived:** declines, parks, no-contact or held rows. Targets who never wrote back stay with their cold-outreach owner. A guest who already recorded gets routine 9, not their old booking ask.
>
> **Caps.** At most 10 nurture and revival mails a Zoya run, inside the 150-a-day cap and the one-mail-per-person-per-7-days rule.

### A2. Section 5 table, row "1. Sponsored offers"
| Column | Before | After |
|---|---|---|
| Mails and span | `14 mails over 6 months: weekly for 3, then every 2 weeks. Silent leads close after 60 days` | `14 mails over 6 months: weekly for 3, then every 2 weeks. Silent leads move to nurture after 60 days (section 5a)` |
| Stops or ends | `A decline stops it. "Give us time" doesn't. 60 days with no reply from their side: Unresponsive (a reply restarts the 60 days). No restart of old offers (decision 230)` | `A decline stops it. "Give us time" doesn't. 60 days with no reply from their side: nurture (section 5a), never Unresponsive on silence. No fresh restart of old offers (decision 230)` |

### A3. Section 5 table, row "2. Precall requested", Stops or ends
Before: `Call booked or a reply. After the last mail: Unresponsive (others with a strong eval go to long-term chase)`
After: `Call booked or a reply. While a PR team is coordinating, every 5 working days (section 5a). After the last mail: nurture (section 5a)`

### A4. Section 5 table, row "3. Recording slot", Stops or ends
Before: `Recording on the calendar or a reply. Unresponsive only after 2 years`
After: `Recording on the calendar or a reply. While a PR team is coordinating, every 5 working days (section 5a). Never Unresponsive on silence`

### A5. Section 5 table, row "7. Long-term chase"
| Column | Before | After |
|---|---|---|
| Mails and span | `Every 90 days for 2 years: a milestone, recent guests, or congrats on their news` | `Long-term chase and nurture (section 5a): a milestone, recent guests, or congrats on their news, for years` |
| Stops or ends | `A reply gets a proper follow-up. Silent for 2 years: Unresponsive` | `A reply gets a proper follow-up. Only a stop in section 5a ends it` |

### A6. Section 5 table, row "8. Sponsored revival", Stops or ends
Before: `"Stop" or a second no. PR-routed leads never`
After: `"Stop" or a second no. PR-routed leads: nurture while silent (section 5a), nothing after a no`

### A7. Section 5, "For every routine", first bullet
Before: `**Staleness gate before any follow-up** (decision 230). Read the whole thread. Close the row instead of mailing when the routine's span is over, a sponsored lead has been silent from their side for 60 days or more, or our last mail was a close-out. A closed sponsored thread never gets a fresh restart.`
After: `**Staleness gate before any follow-up** (decisions 230, AR-20261019-1). Read the whole thread. When the routine's span is over, a sponsored lead has been silent from their side for 60 days or more, or our last mail was a close-out, the row moves to nurture (section 5a) instead of getting the routine's next mail. Silence never closes a row. A sponsored thread never gets a fresh restart.`

### A8. Section 2, Limits, second bullet
Before: `At most one mail per person per 7 days, whichever routines they're in; the more urgent one wins.`
After: `At most one mail per person per 7 days, whichever routines and whichever shows they're in; the more urgent one wins (section 5a).`

### A9. Section 7, "Never followed up", second item
Before: `Organic Unresponsive (45): stays closed.`
After: `Organic Unresponsive (45): stays closed, unless it is a Tier 1 conversation cleanup has checked for revival (section 5a).`

### A10. Section 7, last bullet
Before: `**Three unanswered chases never go to Akshay** (decision 118). Each routine's last step closes the row or moves it to the long-term chase.`
After: `**Three unanswered chases never go to Akshay** (decision 118). Each routine's last step moves the row to nurture (section 5a); only a section 5a stop ends it.`

## B. Routine pages

### B1. 1. Sponsored offers (3fa19a301a7f81b0a80dc0c75102b60e)
Before: `- **Closes as Unresponsive:** 60 days with no reply from their side, counted from the offer or their last reply. A reply restarts the 60 days, so a lead who wrote in month 5 stays open past month 6 until 60 silent days pass. A closed lead is never restarted with a fresh mail (decision 230).`
After: `- **Moves to nurture (Rules for Zoya section 5a):** 60 days with no reply from their side, counted from the offer or their last reply, or the schedule ends. A reply restarts the 60 days. Nurture continues for years until a clear no; it never restarts the offer from mail 1 (decision 230).`

Before: `A lead that never replies closes on day 60, after mail 5. Mails 6 to 14 go only to leads who wrote back in the last 60 days. Before every mail, Zoya runs the staleness gate: 60+ days silent from their side, the 6 months over, or our last mail a close-out means she closes the row instead of mailing (decision 230).`
After: `A lead that never replies moves to nurture on day 60, after mail 5. Mails 6 to 13 go only to leads who wrote back in the last 60 days. Mail 14 is not sent; the row moves to nurture instead. Before every mail, Zoya runs the staleness gate: 60+ days silent from their side, the 6 months over, or our last mail a close-out means the row moves to nurture instead of getting this schedule's next mail.`

### B2. 2. Precall requested (3fa19a301a7f8197be92d74c8f8e0660)
Before: `- **Ends:** after the last mail with no reply. Tier 1 and 1.5 become Unresponsive. Others: Strong consider or better moves to long-term chase (routine 7); anything lower becomes Unresponsive (decision 118).`
After: `- **While a PR team is coordinating** (their side wrote in the last 30 days and the call isn't booked): the next mail goes 5 working days after the last real ask or exchange, unless they asked for a hold (Rules for Zoya section 5a). After 30 quiet days the schedule below takes over.
- **Ends:** the close-the-loop and close-out mails (A14, B8, C4) are not sent. After the mail before them, the row moves to nurture (Rules for Zoya section 5a) until a clear no.`

### B3. 3. Recording slot (3fa19a301a7f814086fdd272fb6f6b86)
Before: `- **Ends:** 2 years after our first slot request with no reply, the row becomes Unresponsive.`
After: `- **While a PR team is coordinating** (their side wrote in the last 30 days and nothing is booked): the next mail goes 5 working days after the last real ask or exchange, unless they asked for a hold (Rules for Zoya section 5a). After 30 quiet days the schedule above takes over.
- **Ends:** never on silence alone. After mail 6, routine 7 and nurture continue until a clear no (Rules for Zoya section 5a).`

### B4. 7. Long-term chase (3fa19a301a7f8151b310e102839d630f)
Before: `- **Cadence:** one check-in every 90 days, 8 in all over 2 years.`
After: `- **Cadence:** one check-in every 90 days. Rows moved here by nurture follow Rules for Zoya section 5a (30, 60 and 90 days, then every 120, then every 180 after 2 years).`

Before: `- **Ends:** 2 years after the row first went to LT chase with no reply, it becomes Unresponsive.`
After: `- **Ends:** only on a stop in Rules for Zoya section 5a (a clear no, a no-contact request, Akshay's decline or park, a dated hold). Silence alone never ends it.`

### B5. 8. Sponsored revival (3fa19a301a7f81008e72f23ebc526327)
Before: `PR-routed leads (300 rows) get routine 1 and nothing after it.`
After: `PR-routed leads get routine 1, then nurture while silent (Rules for Zoya section 5a). After a no, nothing.`

## C. Developer page

Add one Change log line to the Zoya, Daily sweep and Inbox routine pages: "19 Oct (AR-20261019-1): silence moves rows to dated nurture instead of closing them; 5-working-day PR coordination; one ask per person across shows; cleanup-gated Tier 1 revival."
