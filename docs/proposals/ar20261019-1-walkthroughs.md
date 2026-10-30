# AR-20261019-1: acceptance walkthroughs, v3 (traced against the corrected text, 19 Oct)

Traced against ar20261019-1-build.py (the patches ar20261019-1-on-live.patch and ar20261019-1-nurture-2026-10-19.patch) and the payload. These are traces, not runs. "Zoya" is the patched zoya prompt, "sweep" the patched daily sweep, "5a" the new Rules for Zoya section. v2 answered Codex's content review of 58a26f5. v3 answers Codex's "v2 content disposition, 0c0ceaa": the inbox's three-chase path and Zoya's after-send. Rows marked (v3) are new or changed; the rest stand as in v2.

## v3 correction 1: the inbox three-chase path takes exactly one branch

The inbox text now reads, in order: (a) a precall or recording on the calendar, as the event says, or an Akshay or Jaya decision or hold on this pursuit: change nothing; (b) already in nurture: Chase step 0 only; (c) an approved pursuit: move to nurture; (d) else Unresponsive. In v2, a row that failed the GUARD fell into "Else Status Unresponsive, Waiting on empty". The sweep's STEP 3 now uses the same four branches.

| # | Case | v2 (wrong) | v3 trace | Result |
|---|---|---|---|---|
| I1 (G1) | Three old unanswered chases, then the PR booked: a recording event is on the calendar, Status Booked, Call type Recording. A fourth team mail logs as a chase. | GUARD failed, so "Else": Unresponsive, Waiting on empty. | (a): the event is a recording. Status, Call type, Waiting on, Next action and Next date stay. | Unchanged, still Booked. |
| I1p (G1) | The same, but the event is a precall (Call type Precall). | Same erase. | (a): the event says precall, so it stays a precall. Nothing is relabelled a booked recording and no recording ask goes out. | Unchanged. |
| I2 (G2) | Precall done; Waiting on Akshay, "Ask Akshay: verdict after the precall"; three chases from before the precall. | Unresponsive, Waiting on empty: his verdict ask erased. | (a): a decision Akshay holds on this pursuit. | Unchanged, still on his list. |
| I3 (G4) | Sponsored offered; Akshay holds a counter-offer decision. | Unresponsive. | (a). | Unchanged. |
| I4 (G5) | No-show waiting on Akshay. | Unresponsive. | (a). | Unchanged; nothing sent until he decides. |
| I5 | B2S row with a dated host hold ("revisit 15 Nov"). | Unresponsive. | (a): a hold on this pursuit. | Unchanged; revisited on 15 Nov. |
| I6 | Row in nurture since 2 Nov 2026 (segment "Zoya: nurture ... (since 2 Nov 2026)"); three nurture mails have gone unanswered, so the inbox's count reaches 3. | Passed the GUARD, so nurture restarted: new start, Next date reset to 30 days. | (b): Chase step 0 only. Start, n, Next date and the segment stay. | The cadence carries on. |
| I7 | FT Booking, three unanswered chases, nothing on the calendar, no decision or hold. | Nurture. | (c): Status LT chase, Zoya added (others stay), Next date our last mail + 30 days, only the chase segment becomes "Zoya: nurture ...", Claude note "nurture started". | Into nurture. |
| I8 | A row that isn't an approved pursuit (no Tier 1, a lower eval, never at Precall requested, Sponsored offered, Booking or LT chase), three unanswered chases. | Unresponsive. | (d): its existing rule. | Unresponsive, as before. |

## v3 correction 2: Zoya's after-send has explicit branches and reconciles before any retry

In v2 the after-send kept the live "Waiting on Zoya; Next action "Zoya: <routine> step <n+1>"", which overwrote other owners and asks on every send. v3 replaces the whole sentence with AFTER SEND: check Sent and the thread first; one Activity per sent message with the provider's message id; Zoya added to Waiting on; only her own segment of Next action replaced; then the ordinary, nurture or nothing-sent branch.

| # | Case | Trace | Result |
|---|---|---|---|
| A1 (v3) | Nurture row: start 2 Nov 2026 (Claude note "nurture started (60 silent days on sponsored)"), segment "Zoya: nurture <PR>: sponsored feature (since 2 Nov 2026)". Mail sent 2 Nov, message m1. | Nurture branch: Activity "Zoya sent: nurture 1 to <PR>", Source ID m1. Chase step 0. Next date 2 Nov + 60 = 1 Jan 2027. The segment and its "(since 2 Nov 2026)" stay. | n = 1, next 1 Jan. |
| A2 (v3) | The same row, second real send on 1 Jan 2027, message m2. | Check first: no mail since the last nurture Activity, so it sends. Activity "Zoya sent: nurture 2 to <PR>", Source ID m2. Next date 1 Jan + 90 = 1 Apr 2027. Segment and start unchanged. | n = 2, next 1 Apr. The marker and the date progression survive both writes. |
| A3 (v3) | Sankalp Arora: Recorded; Next action "Akshay: invite to the FT Community \| Zoya: guest form step 1 on <D Mon>"; Waiting on Akshay, Zoya. Form step 1 sends. | Ordinary branch: Activity "Zoya sent: guest form step 1 to Sankalp", Chase step 1, Zoya added (already there), Akshay stays; only "Zoya: guest form step 1" becomes "Zoya: guest form step 2 on <D Mon>". | Akshay's community ask and his place in Waiting on stay. |
| A4 (v3) | Sankalp again: form step 2 sends a week later. | Same branch; the community segment is untouched a second time. | Two send-state writes, his ask intact. |
| A5 (v3) | Amit Patni: the same shape (an Akshay community ask plus a form chase). The daily cap is hit before his step. | Nothing sent: no Activity; Chase step, segments, Waiting on and n stay; only Next date moves to the next working day, with "deferred: daily cap" in the Claude note. | Nothing erased, nothing duplicated. |
| A6 (v3) | Patni's row on a run before his Next date. | Not due: nothing changes. | No-op. |
| A7 (v3) | Crash after the mail went, before any write. | Next run, check first: the mail is in Sent and on the thread with no Activity. It sends nothing and does the writes for that message, with its real message id. | One mail, one Activity. |
| A8 (v3) | The Activity was written, then the row update failed. | Retry only the write. If the run ends first, the next run finds the mail and its Activity: it sends nothing, adds no second Activity, and completes Chase step, Next date and the segment. | No resend, n right. |
| A9 (v3) | Two runs on the same day for a nurture row. | The second run's check finds a mail since the last nurture Activity: no send. | n advances once. |

## Codex finding 1: one coordinated contact per person, no mutual blocking

| # | Case | Trace | Sends |
|---|---|---|---|
| X1 (v2) | Sparsh: FT Booking due; B2S row held by Satish ("no invite, Salesblink or follow-up until re-approved", 18 Oct). | ONE PERSON, ONE ASK holds only for a recent mail, active Salesblink, or the same ask open elsewhere. The B2S row has none of those; it's a show hold, which stops only the B2S row. FT goes if due under its own rules. Nothing is ever sent for B2S, and no B2S ask rides on the FT mail. | FT only. |
| X2 (v2) | Same person: FT and un# rows both due today, both unanswered. | Two rows due the same day: the more urgent one sends (PR coordination before nurture). The other row gets "deferred: <FT row>, sent today, recheck <today+7>" and sends then. Neither blocks the other for good. | One today, one in 7 days. |
| X3 (v2) | Same person, Salesblink sequence active on B2S, FT nurture due. | Held: "deferred: Salesblink, active sequence, recheck <its next step or end>". When that date comes and the sequence is over or they replied, the hold no longer applies and nurture sends. n is unchanged by the deferral. | Later, once. |
| X4 (v2) | Person recorded for FT last year (Recorded); a new un# Precall requested row is due. | A Recorded or finished row elsewhere is context, never a reason to wait. The un# step goes; the mail may mention the past episode as context. | un# step. |
| X5 (v2) | Revival-marked row whose person had an FT mail 5 days ago. | Sweep 3r doesn't skip it. It starts nurture with Next date 14 days after that mail, noted "deferred: <row>". | Later. |
| X6 | A person said "please don't contact me" on any row. | A no-contact request stops every row of that person. | None anywhere. |

## Codex finding 2: nurture progress stored on the record and advancing once

How it's anchored: the start is the Claude note "nurture started" (or, for older LT rows, the first date at LT chase, else 20 Oct 2026). n = the count of "Zoya sent: nurture" Activities since the start. The next due date counts from the last actual nurture send. The after-send keeps the chase segment "Zoya: nurture <recipient>: <ask> (since <start>)".

| # | Case | Trace | Result |
|---|---|---|---|
| N1 (v2) | Silent sponsored lead: our last mail 1 Sep; staleness gate on 2 Nov (60 silent days). | GUARD passes (no booking, no decision). Nurture start 2 Nov; Next date = 1 Sep + 30 = 1 Oct, which is past, so it's due at the next follow-up run. Nurture 1 sends 2 Nov to the PR (routine 8 angle); n=1; Next date 2 Nov + 60 = 1 Jan. | One mail, then 1 Jan. |
| N2 (v2) | The same row on successive runs: 1 Jan (mail 2, then +90 to 1 Apr), 1 Apr (mail 3, then +120 to 30 Jul), 30 Jul (mail 4, then +120), and so on. | n comes from Activities, the anchor from the last send date. | 60, 90, 120, 120 ... |
| N3 (v2) | The same row, nurture start 2 Nov 2026; a mail due 10 Nov 2028. | The start is over 2 years old, so the next interval is 180 days. | Twice a year from then. |
| N4 (v2) | A row at LT chase since 1 Mar 2025 (Claude note), silent. | The start is the first LT chase date (1 Mar 2025). Its 2 years end on 1 Mar 2027; until then 120-day intervals, then 180. In v1 the trace wrongly said 180 straight away. | Counted from the real start. |
| N5 (v2) | Sweep: 3 unanswered chases on FT Booking, our last chase 10 Oct, no calendar event, no decision pending. | GUARD passes. LT chase, Zoya added, Next date 10 Oct + 30 = 9 Nov (the same anchor as Zoya), chase segment "Zoya: nurture <PR>: recording slot (since 19 Oct 2026)", Claude note "nurture started (3 chases unanswered, <dates>)". | Via Zoya on 9 Nov. |
| N6 (v3) | Crash after the nurture mail sent, before the after-send write. | Next run: AFTER SEND checks Sent and the thread first, finds the mail, completes the writes (one Activity, which makes n correct) and sends nothing. v2 relied on a check the prompt didn't state; v3 states it (A7, A8). | No duplicate; n right. |
| N7 (v2) | An early run (Next date in the future) and a cap-blocked run. | Not due: no change. Cap: nothing sent, so n and the anchor stay; only Next date moves, with the reason. | n not advanced. |
| N8 | They reply during nurture. | Back on the active routine or their date; that nurture spell ends. A later silence starts a new spell with a new start line. | As routine. |

## Codex finding 3: bookings and decision gates survive every move

| # | Case | Trace | Result |
|---|---|---|---|
| G1 (v3) | Three old unanswered chases, then the PR booked: a recording event is on the calendar. Sweep runs. | Branch (a): the event's kind (recording, or precall) decides; nothing on the row changes. The inbox path is I1 and I1p. | Unchanged. |
| G2 (v3) | Precall done, waiting on Akshay's verdict; three chases from before the precall. | Branch (a) in the sweep and the inbox (I2). Zoya's STEP 2 skips it too. | Unchanged, on his list. |
| G3 (v3) | Sankalp or Amit Patni: Recorded, "Akshay: invite to the FT Community" plus a guest form due. | Zoya's skip: the community add is an independent ask, so the form chase (routine 5) runs. AFTER SEND now replaces only her segment and adds Zoya to Waiting on (A3 to A5); v2's after-send still overwrote both. | Form chase goes; his ask stays. |
| G4 (v3) | Sponsored offered, Akshay holds a counter-offer decision. | Branch (a) everywhere (inbox: I3). | None. |
| G5 (v3) | No-show waiting on Akshay. | Branch (a) everywhere (inbox: I4). | None. |

## Earlier cases, still holding (from v1, re-traced)

| # | Case | Result under v2 |
|---|---|---|
| P1 | Beerud (FT Booking, PR Satv, last PR mail 7 Oct). | PR coordination: 5 working days after the last real exchange; the 15 Oct loop-in doesn't count, so it's due. Guest travel doesn't stop a check with Satv. The 9 Nov Next date is not a confirmed slot; cleanup reconciles it from the thread. |
| P2 | PR replies "hold till 15 Nov". | Their date wins. |
| P3 | 5 working days across a weekend and Diwali week (6 to 13 Nov). | Weekdays only, never Diwali week. |
| P4 | Our last message was a loop-in. | Doesn't count; counted from the real ask before it. |
| P5 | PR quiet 31 days. | The page's slower schedule, then nurture. |
| R1 | HBD Tier 1 outbound, never replied (Salesblink cold). | Not revived; stays with cold outreach. |
| R2 | FT Tier 1 inbound with a real past exchange, marked eligible by cleanup. | Sweep 3r starts nurture on cleanup's date; Zoya sends a contextual routine 7 mail. |
| R3 | Prior guest with a completed Episode. | Never revived as a booking; routine 9 only. |
| S1 | Genuine decline. | Close note once, stop; never re-pitched elsewhere. |
| S3 | "Ping me in March". | Their date. |
| S4 | Akshay parks. | Never followed up. |
| Z1 | Second run the same day. | No step twice; no second nurture start (the Claude note line exists); sweep 3r skips rows with "nurture started (revival". |
| C1 | Daily cap hit. | Deferred and reported; n unchanged. |

## Known limits for cleanup's review

- A Tier 1 decision that lives only in an eval page body (Beerud) isn't found by a database query; the named cases and source checks cover it. The structured Tier changes only on Akshay's own decision.
- "Approved pursuit" no longer includes Booked or Precall done (v2): a booked call and a decision waiting on Akshay are not chases.
- Inbox bytes (v3): 65,523 on the chain build (13 spare) and 65,460 on live (76 spare), against the 65,536 cap. The explicit branches cost 129 bytes over v2. The chain margin is thin; AR-2's own inbox trim issue is separate and unchanged.
- Order: the patches don't commute byte for byte on one line. This change and AR-8 both edit Zoya's REPORT line. With the inbox trim, the whole pending chain applies from after-release/ when nurture ships first (ar20261019-1-release.md); that order was replayed and gives prompts identical to the chain build. v2 claimed full commutation; for this one line that was wrong in v2 too.
- A row whose segments carry their own dates still has one Next date, which belongs to the routine that sets it. That is unchanged from live.
