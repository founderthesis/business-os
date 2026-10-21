# Post-recording v2 (decision 374), parts 2 and 3: prepared patches

Spec: docs/proposals/post-recording-v2.md (33ca972). Main 2, 21 Oct. Prepared, not reviewed, not deployed, nothing sent. The thank-you wording is not touched (Akshay approved the template on 21 Oct; it's on the wording page). The Mac side is the CTO's routines/mac/transcripts.md (fed74f0); this package is the cloud side that meets it.

## Build

The base is Cut 1 plus decision 373, built from the live prompts at 9ae734d (`routines/*.md` at that commit, between the "```text" fences, are byte-equal to live):

```
python3 docs/proposals/cut-1-build.py <live bases> <cut1>
python3 docs/proposals/cut-1-d373.py <cut1> <base>
python3 docs/proposals/post-recording-v2-build.py <base> <out>
```

The build checks each base's bytes and hash before editing, refuses an em dash, and refuses a calendar that still checks Drive audio.

| Prompt | Base (Cut 1 + 373) | v2 | Hash | Spare to 65,536 |
|---|---|---|---|---|
| Inbox | 56,942 / afc7176f665f1fe7 | 57,681 (+739) | 42c692dcd33da47b | 7,855 |
| Zoya | 49,590 / 3b7fe7ed689c06ae | 50,459 (+869) | f080df60fe1bc04f | 15,077 |
| Calendar | 52,992 / d036faaf20ef74cb | 52,075 (-917) | e9261408652a5737 | 13,461 |

Sweep and WhatsApp are unchanged. If Main's deployed Cut 1 differs from these base hashes, the build stops; rebase it on what is live.

## Part 2: everyone on a guest's threads is a Stakeholder

- **Inbox STEP 3, THREAD PEOPLE.** On every thread matched to an Engagement, each address in From, To or Cc is checked. Team addresses and role or no-reply inboxes are skipped. Every other address is found in People (Email, Other emails) or created, with Source ID "gmail:<thread id>". It's then linked: the guest's own address goes on the Guest row, anyone else in Stakeholders unless already Via. Links are never removed. Each new link gets one Claude note line, with no address in it.
- **Zoya STEP 1a.** The same capture for the threads she reads.
- **Zoya SENDING.** Guest-facing mail, release mails included, has Cc = Stakeholders + Via + every outside address on the Engagement's threads and invites. That's minus the To, anyone who asked to be dropped, and bounced addresses. A new address is added to People first.
- **Calendar, GUEST-FACING CC.** The same union for every guest-facing mail or draft it writes: the day-before note, a reschedule, the client thank-you. STEP 3b's client draft Cc and STEP 4d's Cc now point to it.
- **The Mac's FT thank-you** (CTO, 7g) already uses the same union.

## Part 3: the transcript decides (Founder Thesis)

**Calendar STEP 4a.**
- **Founder Thesis:**
  - Once the event has ended and nothing says it was cancelled or moved, a2 creates the Episode at once with Status "Awaiting transcript".
  - One Claude note line is added. Status, Call type, Waiting on and Next action stay as they are.
  - The Drive audio check (20 MB of .mp3) is gone.
- **Client shows** keep the 2-hour rule, unchanged.

**Who asks Akshay, so he gets one ask, not two:**
- **Mac 6d:** no Zencastr recording 24 hours after the slot.
- **Calendar:** two cases the Mac doesn't cover.
  - The Mac wrote "not counted as recorded" (one speaker, or under 20 minutes). At 24 hours the calendar asks.
  - The Episode is still "Awaiting transcript" at 48 hours with no ask about this recording in Next action (for example the Mac is off). The calendar asks then.
- Both use "Akshay: <guest>'s <D Mon> recording: cancelled or no-show?". The Mac's step 6 takes that ask out when the transcript confirms the recording.

**Calendar a2.** A new Episode is created as "Awaiting transcript" on Founder Thesis, else Recorded.

**Calendar STEP 4c.** It no longer drafts the FT thank-you: the Mac writes it (7g). The FT Community row creation moved here from 4a, so it still runs once the row is Recorded. The skip check ("Zoya drafted: FT thank-you" prefix, or a sent "Next Steps |" mail) and the "drafted one Akshay has since sent" clean-up match the Mac's Activity "Zoya drafted: FT thank-you for <guest> (transcript attached)" and its Next action "Akshay: send the thank-you draft to <guest first name> (in your Gmail Drafts, transcript attached)".

**What the two must agree on, checked against fed74f0:**

| Item | Calendar (this package) | Mac (CTO) |
|---|---|---|
| Episode Status at slot end | creates "Awaiting transcript" | works "Awaiting transcript" first, sets "Transcript in" |
| Confirmed recording | skips rows with "recorded <that date> (" | writes "recorded <D Mon> (transcript, ...) (Mac)" |
| Not recorded | asks at 24 h on "not counted as recorded" | writes "... not counted as recorded (Mac)", doesn't ask |
| No recording at all | asks only at 48 h, if no ask exists | asks at 24 h ("no Zencastr recording found") |
| Thank-you | never drafts on FT | drafts, Activity "Zoya drafted: FT thank-you ..." |

**For the CTO, one gap in the Mac prompt.** After 6c ("not counted as recorded", no THANKS), Akshay may know the call happened, for example when the guest track was lost, and set Recorded himself. Then nothing drafts the thank-you: the calendar no longer does, and the Mac skips THANKS for that Episode. Suggested fix in the Mac: if the Engagement is Recorded by Akshay after a 6c verdict, write the 7g draft without the attachment, with "attach the transcript" in Next action. I haven't changed the Mac file.

## Replays

**R1. Matthew Spacie @ Magic Bus, 20 Oct 14:30 JST recording** (Engagement 3f019a301a7f81bd9ed6c7020bf96f3d).
What happened: the guest's long Zencastr track never reached Drive (about 3 MB of test takes). So the old Drive check never set Recorded, no thank-you was drafted, and the row was still Booked 17 hours later. Gemini notes record audio trouble, and the call moved to the recording link.

Under v2:
1. **Calendar run after the slot ends (~16:35 JST, 20 Oct).** The event ended and wasn't cancelled. a2 finds no keyed Episode and creates "Matthew Spacie @ Magic Bus - Founder Thesis", Status "Awaiting transcript", Source ID "cal:<event id>". Claude note "2026-10-20: 20 Oct recording ended, Episode awaiting transcript". Status stays Booked, and the Drive audio isn't looked at.
2. **Mac, the next hourly run after Zencastr finishes.** Zencastr has the 20 Oct recording with Matthew. Two outcomes:
   - (a) The transcript has both speakers, 20 minutes or more, covering the recording:
     - The Episode gets the file and "Transcript in".
     - Booked becomes Recorded and Call type is cleared, with the note "recorded 20 Oct (transcript, <mm> min, 2 speakers) (Mac)".
     - The Mac's 7g drafts "Next Steps | Matthew Spacie @ Magic Bus <> Founder Thesis" as a reply on the latest thread. To: Matthew and the Via. Cc: Yugesh Arora, Archana Mukherjee and Vijayalakshmi Bhat (Stakeholders since the 21 Oct data fix), any other outside address on the 39-message thread (added to People first), and Zoya. Transcript attached.
     - Akshay gets "send the thank-you draft to Matthew (...; transcript attached)".
   - (b) The guest track is lost, so the transcript is Akshay-only:
     - The Mac's 6c writes "20 Oct recording: transcript <mm> min, Akshay, not counted as recorded (Mac)".
     - At 24 hours (~16:35 JST, 21 Oct) the calendar puts "Akshay: Matthew's 20 Oct recording: cancelled or no-show?" first in Next action.
     - Akshay knows it happened and sets Recorded. The calendar's 4c adds the community ask, and the blurb step looks for a transcript.
     - No thank-you draft is written. That's the gap flagged for the CTO above.
   - In both cases the Cc carries the PR people that were missing on the real draft. That was the cause of decision 374's part 2.
3. **Before v2 is live:** a thank-you draft for Matthew already existed on 21 Oct (the one Akshay reviewed). Once v2 is live, the Mac's step 7 finds the "Zoya drafted: FT thank-you" Activity if one was logged and attaches the file to that draft instead of writing a second one.

**R2. No-show (synthetic: an FT guest who never joins a 16:00 JST slot).**
1. **Calendar after the slot:** the Episode is created "Awaiting transcript". The row stays Booked.
2. **Mac:** either Zencastr has no recording for the slot, or it has only Akshay's track for a few minutes.
   - No recording: at 24 hours the Mac adds "Akshay: <guest>'s <D Mon> recording: no Zencastr recording found. Did it happen?" once. The calendar's 48-hour fallback sees that ask and adds nothing.
   - A short Akshay-only track: 6c writes "not counted as recorded", and at 24 hours the calendar adds "cancelled or no-show?" once.
3. Either way, no Recorded, no draft, and no mail to the guest or PR (decision 236: no-shows go to Akshay first; Zoya sends the note after he decides).

**R3. Retry safety.**
- A calendar run that repeats after a2: it finds the keyed Episode and writes nothing.

## Deploy (Main, after Cleanup accepts and Cut 1 is live and read back)

1. **Notion:** add the Status option "Awaiting transcript" to Episodes (collection://5d250752-6db8-4ab6-8467-c68f5838278a) before the calendar prompt goes live.
2. **Cloud:** rebuild on the live bases. Push the inbox, Zoya and calendar one at a time, and read back bytes, hash, cron and model.
3. **Order:** the CTO's Mac prompt goes in first (out of TEST MODE), so FT Episodes the new calendar creates are picked up straight away. Until it's in, "Awaiting transcript" Episodes wait, and the 48-hour fallback asks Akshay.
4. **Records:** developer page change log and the calendar's routine page.

## Not in this package

- The thank-you wording (approved, on the wording page) and the Mac prompt (the CTO's).
- STEP 4e (Episode recovery) still accepts a Zencastr audio folder as evidence for days with several recordings. That's left as it is.
