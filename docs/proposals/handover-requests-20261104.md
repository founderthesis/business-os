# Handover requests for Akshay (decision 459), from Main, 4 Nov

These are the open asks for Akshay from today's builds. Under decision 459 the CTO creates each as one Engagements row (Kind Task, Waiting on Akshay, Task state Handed over, Source ID below). This session writes no Notion rows. Each one below gives what the row needs: why, the steps, and any text to paste.

## 1. cto:2026-11-04:skills-458-upload

**Why:** decision 458 adds an Apify socials step to eight skills, and the step only runs once the skills are uploaded and the connector is on the tasks.

**Next action:** "Akshay: upload the 8 patched skills and add the Apify connector to the evals and dossier tasks. Steps: <row link>"

**Steps:**
1. Get the eight patched SKILL.md files: ft-guest-eval, un-guest-eval, bts-guest-eval, hbd-guest-eval, ft-host-dossier, un-dossier, bts-host-dossier and hbd-host-dossier.
   - **CTO:** build them first with `python3 docs/proposals/skills-458/build.py <installed skills dir> <out>`, and attach the eight files to the row. They aren't in the repo, because one carries contact details.
   - **Check:** the hashes should match `docs/proposals/skills-458/handoff.md`.
2. Upload each in claude.ai Settings, Skills, replacing the current version.
3. Add the Apify connector to the "Founder Thesis guest evals" task and to the "Host dossiers and prep notes" task (trig_01WfLf8Zx9c34fSzfrTeUY5M).
4. Write "done" in Your call.

## 2. cto:2026-11-04:dossier-notion-log

**Why:** the repo copies of un-dossier, bts-host-dossier and hbd-host-dossier have a last step, "Log the dossier in the Business OS (Notion)", which writes the Dossier link on the guest's Engagement. The installed copies don't have it. So dossiers made with those three skills may never reach the Engagement row, and the calendar's prep events and Zoya's 453 themes reply both read from it.

**Next action:** "Akshay: should the un#, BTS and HBD dossier skills log the Dossier link on the Engagement, like ft-host-dossier does? Steps: <row link>"

**Steps:**
1. Write yes or no in Your call.
2. If yes, Main adds the step to the three item 1 patches before you upload them, so you upload once.

## 3. cto:2026-11-04:themes-client-shows

**Why:** decision 453's themes reply (Zoya sends the prep note's themes when the guest side asks) runs on Founder Thesis only for now. On un#, Built to Share and Human by Design, the request goes to Akshay's list, because the themes would otherwise reach the guest unseen by Akshay or the host.

**Next action:** "Akshay: should Zoya also send prep-note themes on un#, BTS and HBD, or keep those for you? Steps: <row link>"

**Steps:** write "all shows" or "FT only" in Your call.

## 4. cto:2026-11-04:cadences-slow

**Why:** the Zoya SLOW task reads three things from Cadences that aren't confirmed to be there:
- **A FAST reserve:** without one, SLOW stops 30 sends short of the daily cap of 150.
- **Team hours for team WhatsApp:** without them, the fallback is 09:00 to 20:00 IST. So only the 17:08 JST run (13:38 IST) sends team WhatsApp; the 08:08 and 11:08 runs send none.
- **The Diwali pause line:** it starts Fri 6 Nov. SLOW now holds chases only, and release mails, payments and owner mail still go on their dates.

**Next action:** "Akshay: confirm the FAST reserve, team WhatsApp hours and the Diwali line on Cadences. Steps: <row link>"

**Steps:**
1. On Cadences, add a line such as:

   ```
   FAST reserve: 30 sends a day (SLOW stops at the daily cap less this)
   Team WhatsApp hours: 09:00 to 20:00 IST, weekdays
   ```
   Change the numbers to what you want.
2. Check that the Diwali line says the pause dates, and that it holds chases only: follow-ups, nurture, revival. Release mails, invites, payments and team steps still go.
3. Write "done" in Your call.

## 5. cto:2026-11-04:transcripts-stuck

**Why:** a read-only check on 4 Nov found two transcripts no routine will ask for:
- Spyne (Sanjay Varnwal, 23 Jul): no transcript row exists. It's older than every routine's window.
- Entrust Family Office (23 Oct): its row is On hold.

**Next action:** "Akshay: ask Mamatha for the Spyne transcript, and say whether Entrust's should still be chased. Steps: <row link>"

**Steps:**
1. **Spyne:** write "create" in Your call, and the CTO makes a transcript row that Zoya asks Mamatha about. Or write "skip" if the episode isn't going ahead.
2. **Entrust:** write "reopen" to put its row back to Handed over, which makes Zoya ask Mamatha. Or write "leave".

## For the CTO, not Akshay

- **Rules for Zoya, "Transcript requests":** name Mamatha (decision 456).
- **Capture's 07:02 JST run on 4 Nov:**
  - Read its "pending:" line and the 0A line: do the 11 pends from 23:03 clear by HEAD?
  - Are Eshna Malhotra's two pitches (All Mail 109182 and 109183) logged?
  - Send me the error lines if not, and they go into capture r13b.
- **Ready for Cleanup:**
  - Zoya r16 (`docs/proposals/zoya-r16/`);
  - capture r13 (`docs/proposals/inbox-split/capture-r13/`);
  - calendar 454 (`docs/proposals/calendar-454/`).
