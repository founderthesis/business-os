# Cleanup verdict: PaaS move dry run (33 Deals to Engagements)

Cleanup session, 6 Nov 2026, about 17:30 JST. Read-only: the README, dry-run.md, plan.json, migration/paas_move.py, and the r22 builds' PaaS text.

## Verdict: not yet. The plan is sound, but three things must be true before the write (C1 to C3)

**What holds:**
- **Selection:** "Warm or cold is Warm or Slow, any Stage" gives 33 of the 35 read. The 2 that stay (DuploCloud, Latent AI) are Parked and Cold outreach. That's right: Cold outreach Deals are the target list (decision 89), and leaving them gives the CTO's 33. Keep it 33.
- **Stage mapping:** right, with one caution. New, Contacted and Parked map to themselves, Unresponsive to Unresponsive, Declined to They declined, In conversation and Interested to Interested, and Proposal sent to Decision pending. The Deal Stage is kept in the page body, so nothing is lost. The caution: Won becoming Booked, and Proposal sent becoming Decision pending, are guest statuses that other routines act on. C1 covers that.
- **Idempotency:** each op looks up Source ID "deal:<id>" first and reuses a row it finds. A re-run can't create a second one.
- **Provenance:** Source Agent, Source ID, Captured and Migration batch are all set.
- **Plan file:** plan.json comes from the snapshot by script, with the Show id as a placeholder. The only change after the Show exists is show_id.

## C1 (blocker): the PaaS guard must be live in every routine that reads Engagements, before the write

Main's README names this risk and leaves it unbuilt. r22 has no guard outside Zoya, and live Zoya (r21) has no PaaS gate at all. Paths I traced in the live prompts:
- **Sweep STEP 2:** on a row at Decision pending it ensures "Ask Akshay to approve: eval says <verdict>". That hits all 10 Proposal-sent rows.
- **Sweep STEP 4 "Quiet":** this isn't limited by show. It flags "Zoya: quiet since <date>, chase or update the status" with Zoya in Waiting on on open rows (Contacted, Interested and the rest) with no Activity in 14 days. Live r21 Zoya would then work a "Zoya:" step on a PaaS row from her inbox. That's an unapproved send to a sales prospect.
- **Sweep STEP 4:**
  - "Booked, no date" flags Clairva.ai, Won with no Next date, as "Fix: Booked but no recording date".
  - "No contact" flags any Booked row whose guest has no email.
  - The Deals flag ("Akshay: <Stage>, untouched <n> days") keeps firing on the old Deals, so one pursuit sits in two places.
- **Inbox actions:**
  - STEP 3's guest rules move Status on new mail ("they reply yes": Interested, "decline": They declined).
  - STEP 4 still updates the moved Deals' Stage.
  - 6e queues "Zoya: <reply>" steps.
- **Capture and the evals task:** capture links new mail to these rows as guest mail. The Cowork evals task scans open rows for evals.

The fix is one line in each of sweep, inbox actions, capture, calendar and WhatsApp, plus the live Zoya (or deploy r22's gate first):
- "Engagements on Show PaaS are production-service rows: no guest step, eval, chase, status change or flag by guest rules; mail on them is logged and what it asks goes to Akshay's list."
- "A Deal whose Next action starts 'Moved to Engagements' is retired: never flag, update or link to it; use its Engagement."

Deploy those, or hold the write until the next round carries them.

## C2: the Activity relink must append, and verify must prove the old links survived

Each op lists the Activity ids that get the new Engagement. The Engagement relation is written whole, though, and several of these Activities already link a guest Engagement: Entrust (Rajmohan), Field Assist, Codewave, Cygnet.One. Writing only the new id would drop the old guest link. So:
- read each Activity's current Engagement list and write back old plus new;
- extend verify to compare against that before-snapshot, so every old link is still present.

Today verify checks only that the new id is there.

## C3: the migration segment names Zoya and puts 33 identical asks on Akshay's list

- **The text is now wrong.** "Akshay: PaaS row moved from Deals, Zoya waits for the PaaS templates (6 Nov)" names Zoya, but Akshay rejected the Zoya-voice templates and PaaS follow-ups now go from ad@ as him. r22's SLOW also treats this exact text as "no hold" and removes it on the first PaaS send.
- **It floods his queue.** Thirty-three copies of the same line on his list is a notification, not a decision (decision 325).

Recommended: each row's Next action becomes the Deal's own next step, cut to about 120 characters (B12), owner first ("Akshay: send the proposal reminder to Manu (27 Oct)"). The full text goes in the Claude note, as the plan already does. Rows with no step of his get Waiting on Guest or PR, or nothing for Parked and Unresponsive. The template approval stays on its one Task row (41019a301a7f810da25cc4145a7de33d). This also settles Field Assist: its four open waits become segments with their owners, not one generic line.

If the CTO keeps one generic segment, at least drop "Zoya" from it: "Akshay: PaaS row, follow-ups wait for your PaaS template ok (6 Nov)".

## Rows Main flagged (agree)

- **Clairva.ai:** content licensing, not production. Keep it in Deals, or move it as Booked with C1 live. Akshay's call.
- **Cygnet.One:** the Guest should be Kesha Shah, who runs the PaaS conversation, once her People row is checked. Niraj stays a Stakeholder.
- **CapConnect:** right as planned. The PR contact stays a Stakeholder.
- **Codewave and Meanwhile:** no Organisation. Fine, and listed in problems.

## PaaS in r22 (the CTO's flag on the ad@ exception)

r22 assumes Zoya's inbox in three places:
1. **PAAS:** "Every PaaS mail goes from your inbox on the company's existing thread", in both the hourly and the SLOW file.
2. **The GATE:** it waits on four named Zoya-voice toggles ("PaaS chase (no reply)", "Proposal questions", "Proposal call offer", "Monthly nurture").
3. **PAAS FOLLOW-UPS:** the whole ladder, sent by Zoya.

The gate keeps r22 safe today, since those toggles won't be approved. But if Akshay approves one-liners under any of those names, Zoya sends them from her inbox in her own voice, against his ruling.

Recommended for r22, which also saves bytes in the hourly, now about 1,140 under the cap: replace PAAS and PAAS FOLLOW-UPS with "PaaS rows: send nothing, ever; one Claude note line per inbound ('PaaS: <Message-ID> for Akshay'), and report it." Build the ad@ sender as its own change. Sending as Akshay from ad@ is a new exception to decision 420, so log it in the Decisions database first, and say whether it's a send or a draft he sends.
