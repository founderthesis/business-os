# B round (5 Nov feedback, B1 to B15): hand-off to Cleanup and the CTO

Main, 5 Nov. Source: docs/feedback/2026-11-05-5nov-page.md (8c7ad98). Nothing is deployed. Nothing was written to Notion and no mail was sent. Every build was run twice and came out byte-identical. Two offline replays ran (replay/zoya.md, replay/others.md), and every defect they found that a prompt can fix is fixed in these builds.

## Builds

| Routine | Base (live) | Build | Bytes / sha256 |
|---|---|---|---|
| Zoya hourly | r19 ee8f1966 | zoya-r21/zoya-one.txt | 57,877 / 69a0c4bfa6cb9693 |
| Zoya SLOW task | r19 8c8765db | zoya-r21/zoya-slow.txt (pin 201f730) | 14,416 / a81e3bc6752c9a33 |
| Zoya SLOW file | r19 c4fd78d6 | routines/zoya/release/zoya-slow-work.txt at 201f730 | 85,088 / 9d74718b043345e3 |
| Zoya episodes | r19 3fa79d6f | zoya-r21/zoya-episodes.txt | 47,566 / 185326a27ef23a28 |
| Calendar sync | e4b39d67, then precall-409 (27d7bdf6) | b-round-5nov/calendar.txt | 61,195 / 9dc4babe6294cf18 |
| Daily sweep | 76b49956, then precall-409 (191497f3) | sweep.txt | 43,938 / 4ef8998fad2ced33 |
| WhatsApp | 8628f42a, then precall-409 (b8b7c312) | whatsapp.txt | 27,410 / 174d931773dd6cc0 |
| Inbox capture | r13c 40e787a2 | capture.txt | 49,196 / 72c4d81afaefb68e |
| Inbox actions | r11b 07832eb6 | actions.txt | 46,501 / 459e40411924cddd |
| Host dossiers | 98875d4e | dossiers.txt | 6,401 / 28a2d9b739dafac7 |

How to build:
- **Zoya:** apply `zoya-r21/build_one.patch` at f70901f. It adds `routines/zoya/r21_edits.py`, the r21 edit list applied after the variant edits. Then run `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 201f730a2a19b1a604bc1b5e7efbdaa29781e35c`.
- **The rest:** run `python3 docs/proposals/precall-409/patch.py <cal|sweep|wa> <live> <tmp>`, then `python3 docs/proposals/b-round-5nov/patch.py <cal|sweep|wa|cap|act|dos> <tmp or live> <out>`.

Every edit is asserted exactly once and the patch adds no em dash. The sweep's one em dash was already in the live prompt.

r21 is built on r19, which is live, not on r20. r20 (decision 467) still waits on Cleanup's C1 and gets rebased onto r21 when it's rebuilt. The branch's release file now holds r21. r20's SLOW file stays at 08c214a.

## CTO changes folded in (5 Nov, about 17:40 JST)

1. **Dossiers:** at most 5 a run, up from 3 (Akshay: "make it upto 5 dossiers a run").
2. **B1:** no un# skill zip. Akshay updated un-dossier himself on claude.ai and closed item 1. The prompt-side PREP NOTE RULES change stays. The ft, bts and hbd zips are small and stay here for the CTO to offer him.
3. **B11:** this isn't done until it's proven on a real recording. The first ones after deploy are the test: Gulab, 6 Nov 21:00 JST, and Bharat, 7 Nov 13:30 JST.
4. **PR guard:** sweep 3g, sweep 3k and calendar a2 never treat a person as the guest or a co-guest when People tags them PR contact or the row has them as Via or Stakeholder, whatever an event or episode title says. Mitali Ahuja is Col. Sai Shankar's PR.
5. **B8:** Akshay agreed it as proposed (themes, not questions).

## What each item became

- **B1:** the dossier routine's prep note rules now say 3 to 5 themes, one line each, no running order, no questions, and "Never mention edit rights, review or approval, in any form". Booked FT notes are rewritten once ("prep note v3"). Skill zips for ft, bts and hbd are in skills/*.zip, built by skills/patch_skills.py from the synced copies; un# has none (see above).
- **B2:** NO COMPOSE REPLY is a HARD rule in Zoya, and SENDING, the loop-in and ACTIONS now name the draft send. Calendar MAIL FORMAT replies the draft way in Zoya's inbox, with a python assert on draft_read's actual To and Cc. Capture's loop-in goes the same way; that one is beyond the list but is the same hazard.
- **B3:** BOOKING LINKS reads "you can pick any slot available on this link: podm.in/30min", and the PLAIN ENGLISH "works" exception is gone. Page edits are in notion-writeouts.md, W1.
- **B4:** wording page only (W2).
- **B5:** calendar 3b never uses an invitation thread. To is the guest's People Email, else the guest's address on the invite, which is also written to People.
- **B6:** capture STEP 6 and 6b skip the loop-in when Zoya is already on To or Cc, and write the note "loop-in skipped: Zoya already on the pitch".
- **B7:**
  - A blocked delete still does the row part.
  - The row gets "Akshay: delete the <D Mon> invite for <guest> (blocked: <error>)", and STEPS 2, 3, 3b and 4 skip that event while the segment is on.
  - The run adds a report line until the event is gone.
  - **This deviates from B7's "Zoya: delete":** Zoya's HARD rules forbid her deleting events, so a Zoya step would sit undone forever.
- **B8:**
  - A themes or questions ask before a recording is Zoya's on every show, even inside a reply to Akshay's own mail; only the scheduling part goes to him.
  - No prep note yet: one holding line, merged with any other holding reply, and the reply action stays open.
  - The dossier routine builds that row's prep note first, whatever its date.
  - Inbox actions queues the same step.
  - The Rules for Zoya text is W5.
- **B9:**
  - STAKEHOLDERS FIRST opens THREADING. A new company-side person joins Stakeholders.
  - A person from a different agency becomes Via, and the old Via moves to Stakeholders with a "Via changed" note line.
  - The row name follows the change.
  - The Nutrifresh row fix is W6.
- **B10:** a recording invite gets no Meet; its recording link is the location and the first description line. STEP 0r removes a Meet from a recording invite, including one that already has the link. Gulab Patil's 6 Nov invite needs a manual fix now (W8).
- **B11:**
  - Calendar 4c drafts Akshay's new text on the recording day as a standalone new mail, with the one segment "Akshay: send the thank-you to <guest> (draft ready) and add <guest> to the FT Community WhatsApp".
  - On FT, the 4f transcript row reads "...then send it to <guest> on the thank-you thread".
  - SLOW (4b) sends it once the thank-you has gone, using a new toggle, "Transcript for review" (W3, needs Akshay's ok).
  - SLOW's own thank-you draft step uses the same segment.
- **B12:**
  - NEXT ACTION SIZE (about 120 characters a segment, detail in the Claude note, no "Write ok, not ok") is in Zoya and inbox actions. The writers' templates are shortened: 446, 444, 448, brand, held-for-review, and capture's replacement proposal.
  - Sweep STEP 3a3 trims open rows, longest first, 30 a run.
  - **Not built:** moving action keys out of Next action. Engagements has no "Action keys" field (decision 438), so this needs a schema decision first.
- **B13:** wording page only (W4), with the bar from Akshay's Chandrayee mail.
- **B14:** calendar 4a and 4c.2, sweep 3k, and WhatsApp e0 and 3a(1) write no community segments. The sweep cleans up the old ones without touching other Membership values, and keeps the thank-you segment.
- **B15:**
  - Cleanup's precall-409 edits are applied first for calendar, sweep and WhatsApp.
  - The same exemption line is fixed in capture, actions, the Zoya SLOW file and episodes, which the 409 set didn't cover; they now say Mamatha, per decision 456.
  - WhatsApp also gets Cleanup's carry-overs (AD Tasks, Mamatha).
  - The 9 open precall Task rows remain the CTO's.

## For the CTO

1. **B7 permission.** The Calendar sync task (trig_01Voiz5YsK2SnVf2STF8PoSH) has no permission mode set and no tool policy override, so Google Calendar delete_event hits a permission prompt that nobody answers. Either set the task's permission mode to auto, as the Host dossiers task has, or add an allow override for Google-Calendar delete_event on its connector. Inbox actions (trig_012HbtmVKHUDeFZnFyooSgL3) cancels invites in 6e, so it needs the same. update_trigger here can't set either.
2. **Notion write-outs:** W1 to W8 in notion-writeouts.md. The urgent one is W8, Gulab's Meet, before his 6 Nov recording.
3. **Deploy order** (after Cleanup):
   - calendar first, since every precall makes new Task rows until 409 is live;
   - then capture (B6, B2);
   - then the Zoya pin plus the hourly and SLOW prompts;
   - then sweep, actions, WhatsApp and dossiers.
   - Zoya (4b) only sends once W3's toggle exists; until then it reports "wording missing".
4. **Skills.** Offer Akshay ft-host-dossier.zip, bts-host-dossier.zip and hbd-host-dossier.zip, which change only the "never mention edit rights, review or approval" line and FT's theme count. un# has no zip, so his own edit stands.
5. **Decisions for the Notion ledger,** at the next free numbers:
   - No email_compose action reply, from any inbox or routine; replies go the draft way with an assert on the draft's actual recipients (B2).
   - The day-before note is never sent on a calendar-invitation thread; the guest's address can come from the invite (B5).
   - No loop-in when Zoya is already on the pitch's To or Cc (B6).
   - A blocked calendar delete does the row part and goes to Akshay as one step until the event is gone (B7; note the deviation above).
   - Recording invites carry no Google Meet; precalls do (B10).
   - The FT Community ask lives only on the To invite list; no Engagement segments (B14).
   - Next action segments are about 120 characters, detail in the Claude note, and the sweep trims them (B12, part of decision 438).
   - Slot wording is "you can pick any slot available on this link: <link>" (B3).
   - Guest form ask wording (B4).
   - New FT post-recording mail, standalone, drafted on the recording day; Zoya sends the transcript afterwards (B11).
   - "Why not organic" reply for Founder Thesis (B13).
   - Themes on request are Zoya's on every show, carved out of decision 448 (B8).
   - Stakeholders are updated from each inbound, and Via changes across agencies (B9).
   - Prep notes carry 3 to 5 broad themes and never mention edit rights, review or approval (B1).

## Known, not in this round

These are from the replay's lower-priority list, all already in the live prompts:
- Calendar moves Booked back to Booking against "never move Status backward".
- Calendar 4a sets both Invited and To invite for the same note.
- 4d (client shows) still says "attach the transcript".
- Rows drafted before this build keep their old thank-you segment until Akshay sends.
