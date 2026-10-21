# Post-recording v2 (decision 374), parts 2 and 3: prepared patches

Spec: docs/proposals/post-recording-v2.md (33ca972). Main 2, 21 Oct. Prepared, not reviewed, not deployed, nothing sent. Part 1 (the thank-you wording) is not touched; it waits on Akshay's ok of the template.

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
| Calendar | 52,992 / d036faaf20ef74cb | 51,913 (-1,079) | 177ab5721d3ecd9e | 13,623 |
| Mac transcripts (local) | 16,743 file | 23,930 file, prompt 20,490 | n/a | 45,046 |

Sweep and WhatsApp are unchanged. If Main's deployed Cut 1 differs from these base hashes, the build stops; rebase it on what is live.

## Part 2: everyone on a guest's threads is a Stakeholder

- **Inbox STEP 3, THREAD PEOPLE.** On every thread matched to an Engagement, each address in From, To or Cc is checked. Team addresses and role or no-reply inboxes are skipped. Every other address is found in People (Email, Other emails) or created, with Source ID "gmail:<thread id>". It's then linked: the guest's own address goes on the Guest row, anyone else in Stakeholders unless already Via. Links are never removed. Each new link gets one Claude note line, with no address in it.
- **Zoya STEP 1a.** The same capture for the threads she reads.
- **Zoya SENDING.** Guest-facing mail, release mails included, has Cc = Stakeholders + Via + every outside address on the Engagement's threads and invites. That's minus the To, anyone who asked to be dropped, and bounced addresses. A new address is added to People first.
- **Calendar, GUEST-FACING CC.** The same union for every guest-facing mail or draft it writes: the day-before note, a reschedule, the client thank-you. STEP 3b's client draft Cc and STEP 4d's Cc now point to it.
- **Mac 6b.** The FT thank-you uses the same union and creates any missing Person first.

## Part 3: the transcript decides

**Calendar STEP 4a.**
- **Founder Thesis, Built to Share and Human by Design:**
  - Once the event has ended and nothing says it was cancelled or moved, a2 creates the Episode at once with Status "Awaiting transcript".
  - One Claude note line is added. Status, Call type, Waiting on and Next action stay as they are.
  - The Drive audio check (20 MB of .mp3) is gone.
  - 24 hours after the slot, if the Episode is still "Awaiting transcript" or the Mac wrote "not recorded (transcript", Akshay gets "cancelled or no-show?" once (decision 236). The guest is never chased.
- **un#** keeps the 2-hour rule (its studio has no transcript export).

**Calendar a2.** A new Episode is created as "Awaiting transcript" (un#: Recorded).

**Calendar STEP 4c.** It no longer drafts the FT thank-you: the Mac task does. The FT Community row creation moved here from 4a, so it still runs once the row is Recorded. The "drafted one Akshay has since sent" clean-up and the community ask are unchanged.

**Mac transcripts:** docs/proposals/post-recording-v2-mac-transcripts.md, a proposed replacement for routines/mac/transcripts.md.
- **Schedule:** hourly at :45, 10:45 to 22:45 JST. The work list starts with every "Awaiting transcript" Episode.
- **4c. Recorded?** The guest and the host each have 10 or more speaker lines, the last timestamp is 20:00 or more, and the existing identity and coverage checks pass. If not: no attachment, one Claude note line "not recorded (transcript <mm> min, speakers ...)", and a report line. The calendar asks Akshay at 24 hours. Once he answers, the open job closes.
- **6. Recorded.** Booked becomes Recorded. Call type Recording is cleared. The Claude note gets "recorded <YYYY-MM-DD> (transcript, <mm> min) (Mac)", which matches the calendar's skip pattern "recorded <that date> (". Status never moves backward. The Episode goes to "Transcript in" in step 5.
- **6b. FT thank-you draft:**
  - Gmail create_draft in ad@, with the .txt attached in the same call.
  - Wording, subject and To are moved verbatim from the calendar's 4c. Cc follows part 2. Never sent.
  - Read back, then: Activity "Zoya drafted: FT thank-you for <guest>" with its Draft ID, so the calendar and THANKS logic keep working; Akshay added to Waiting on; Next action "... transcript attached".
  - Dedupe: an existing Activity, a sent thank-you, or a draft with that subject means nothing is created. An unclear create_draft result is checked with list_drafts before any retry.
  - Fallback: Akshay set Recorded himself while the transcript failed 4c. The draft is created without the file, and THANKS attaches it later.
- **Sender policy:** it may create this one draft, nothing else. It never sends, deletes or forwards. The draft-attach gate (step 0) still covers only THANKS.

## Replays

**R1. Matthew Spacie @ Magic Bus, 20 Oct 14:30 JST recording** (Engagement 3f019a301a7f81bd9ed6c7020bf96f3d).
What happened: the guest's long Zencastr track never reached Drive (about 3 MB of test takes). So the old Drive check never set Recorded, no thank-you was drafted, and the row was still Booked 17 hours later. Gemini notes record audio trouble, and the call moved to the recording link.

Under v2:
1. **Calendar run after the slot ends (~16:35 JST, 20 Oct).** The event ended and wasn't cancelled. a2 finds no keyed Episode and creates "Matthew Spacie @ Magic Bus - Founder Thesis", Status "Awaiting transcript", Source ID "cal:<event id>". Claude note "2026-10-20: 20 Oct recording ended, Episode awaiting transcript". Status stays Booked, and the Drive audio isn't looked at.
2. **Mac, the next hourly run after Zencastr finishes.** Zencastr has the 20 Oct recording with Matthew. Two outcomes:
   - (a) The transcript has both speakers, 20 minutes or more, covering the recording:
     - The Episode gets the file and "Transcript in".
     - Booked becomes Recorded and Call type is cleared, with the note "recorded 2026-10-20 (transcript, <mm> min) (Mac)".
     - 6b drafts "Next Steps | Matthew Spacie @ Magic Bus <> Founder Thesis" as a reply on the latest thread. To: Matthew and the Via. Cc: Yugesh Arora, Archana Mukherjee and Vijayalakshmi Bhat (Stakeholders since the 21 Oct data fix), any other outside address on the 39-message thread (added to People first), and Zoya. Transcript attached.
     - Akshay gets "send the thank-you draft to Matthew (...; transcript attached)".
   - (b) The guest track is lost, so the transcript is Akshay-only:
     - 4c fails (one speaker), with the note "20 Oct recording not recorded (transcript <mm> min, speakers Akshay)".
     - At 24 hours (~14:30 JST, 21 Oct) the calendar puts "Akshay: Matthew's 20 Oct recording: cancelled or no-show?" first in Next action.
     - Akshay knows it happened and sets Recorded. 6b's fallback drafts the thank-you without the file. The calendar's 4c adds the community ask and the blurb step looks for a transcript.
   - In both cases the Cc carries the PR people that were missing on the real draft. That was the cause of decision 374's part 2.
3. **Before v2 is live:** a thank-you draft for Matthew already existed on 21 Oct (the one Akshay reviewed). 6b's dedupe means v2 creates no second draft once deployed, because its subject matches in ad@ Drafts, or its Activity if one was logged.

**R2. No-show (synthetic: an FT guest who never joins a 16:00 JST slot).**
1. **Calendar after the slot:** the Episode is created "Awaiting transcript". The row stays Booked.
2. **Mac:** either Zencastr has no finished recording ("waiting for Zencastr", nothing written), or it has only Akshay's track for a few minutes. Then 4c fails and the note reads "not recorded (transcript 4 min, speakers Akshay)". No file is attached, no Recorded, no draft.
3. **Calendar at 24 hours:** "Akshay: <guest>'s <D Mon> recording: cancelled or no-show?" goes on his list once. No mail goes to the guest or PR (decision 236: no-shows go to Akshay first; Zoya sends the note after he decides).
4. **Akshay answers no-show:** the Mac closes the open job and reports it once. The Episode stays as a record until Akshay sets it to Not releasing.

**R3. Retry safety.**
- A Mac run that creates the draft but dies before logging: the next run finds it by subject on the thread (6b a or c) and logs it, creating nothing.
- A calendar run that repeats after a2: it finds the keyed Episode and writes nothing.

## Deploy (Main, after Cleanup accepts and Cut 1 is live and read back)

1. **Notion:** add the Status option "Awaiting transcript" to Episodes (collection://5d250752-6db8-4ab6-8467-c68f5838278a) before the calendar prompt goes live. No other schema change.
2. **Cloud:** rebuild on the live bases. Push the inbox, Zoya and calendar one at a time, and read back bytes, hash, cron and model.
3. **Mac:** Akshay pastes the new prompt into the desktop app's "Mac transcripts" task, sets it hourly from 10:45 to 22:45 JST, and adds the Gmail create_draft grant ("allow once" until a real draft is seen). Then copy the proposal over routines/mac/transcripts.md and update routines/mac/README.md (schedule and writes).
4. **Order:** the Mac prompt goes in first, so Episodes the new calendar creates are picked up straight away. Until it's in, "Awaiting transcript" Episodes simply wait, and the 24-hour ask covers them.
5. **Records:** developer page change log and routine pages (calendar, Mac transcripts).

## Not in this package

- Part 1 (the template), until Akshay approves the wording.
- STEP 4e (Episode recovery) still accepts a Zencastr audio folder as evidence for days with several recordings. That's left as it is.
