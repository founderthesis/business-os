# AR-20261019-1: acceptance walkthroughs, v2 (traced against the corrected text, 19 Oct)

Traced against ar20261019-1-build.py (the patches ar20261019-1-on-live.patch and ar20261019-1-nurture-2026-10-19.patch) and the payload. These are traces, not runs. "Zoya" is the patched zoya prompt, "sweep" the patched daily sweep, "5a" the new Rules for Zoya section. v2 answers Codex's content review of 58a26f5; rows marked (v2) are new or changed.

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
| N6 (v2) | Crash after the nurture mail sent, before the after-send write. | Next run: SENDING checks Sent and the thread first, finds the mail, logs it (Activity, which makes n correct) and sends nothing. | No duplicate; n right. |
| N7 (v2) | An early run (Next date in the future) and a cap-blocked run. | Not due: no change. Cap: nothing sent, so n and the anchor stay; only Next date moves, with the reason. | n not advanced. |
| N8 | They reply during nurture. | Back on the active routine or their date; that nurture spell ends. A later silence starts a new spell with a new start line. | As routine. |

## Codex finding 3: bookings and decision gates survive every move

| # | Case | Trace | Result |
|---|---|---|---|
| G1 (v2) | Three old unanswered chases, then the PR booked: a recording event is on the calendar. Sweep runs. | GUARD: a recording on the calendar stops that chase; Status stays (Booked); no nurture move, no new booking ask. Booked is not in the approved-pursuit list anyway. | Unchanged. |
| G2 (v2) | Precall done, waiting on Akshay's verdict; three chases from before the precall. | GUARD: a decision Akshay holds on this pursuit leaves the row as it is. Precall done isn't a chase. Zoya's STEP 2 skips it too. | Unchanged, on his list. |
| G3 (v2) | Sankalp or Amit Patni: Recorded, "Akshay: invite to the FT Community" plus a guest form due. | Zoya's skip: the community add is an independent ask, not a decision on this pursuit, so the form chase (routine 5) runs. Any later nurture move would replace only the chase segment; Akshay's community ask and his place in Waiting on stay. | Form chase goes; his ask stays. |
| G4 | Sponsored offered, Akshay holds a counter-offer decision. | A decision on this pursuit, so it's skipped and no nurture move happens. | None. |
| G5 | No-show waiting on Akshay. | A decision gate, so nothing is sent. | None. |

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
- The inbox's three-chase text grows 125 bytes over v1 (chain build 65,394; on live 65,331). AR-2's own inbox trim issue is separate and unchanged.
