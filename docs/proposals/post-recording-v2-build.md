# Post-recording v2 (decision 374), parts 2 and 3: prepared patches

Spec: docs/proposals/post-recording-v2.md (33ca972). Main 2, 21 Oct. Prepared, not reviewed, not deployed, nothing sent. The thank-you wording is not touched (Akshay approved the template on 21 Oct; it's on the wording page). The Mac side is the CTO's routines/mac/transcripts.md (fed74f0); this package is the cloud side that meets it.

## Build

Rebuilt 21 Oct ~19:00 JST on the live prompts: `routines/*.md` at 7eec76c, between the "```text" fences, which match live (Cut 1 and decision 375 are deployed). The build checks each base's bytes and hash before editing, refuses an em dash, and refuses a calendar that still checks Drive audio.

```
python3 docs/proposals/post-recording-v2-build.py <dir with the live prompts as trig_<id>.txt> <out dir>
```

| Prompt | Live base (7eec76c) | v2 | Hash | Spare to 65,536 |
|---|---|---|---|---|
| Inbox | 57,267 / f48898f4ac396bf0 | 58,006 (+739) | bf91c4368a9fba42 | 7,530 |
| Zoya | 50,247 / 2e05abc111942c9e | 51,116 (+869) | 319db320cdb1b3fe | 14,420 |
| Calendar | 52,992 / d036faaf20ef74cb | 52,142 (-850) | 4e46ceed7d112279 | 13,394 |

Sweep and WhatsApp are unchanged. If a live prompt changes before deploy, the build stops; rebase it on what is live.

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
- Both use "Akshay: <guest>'s <D Mon> recording: cancelled or no-show?", and only while Status is still Booked: STEP 4 selects Booked rows only, and the ask is never added once the row is Recorded. The Mac's step 6 takes that ask out when the transcript confirms the recording.

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

**The Matthew gap is closed on the Mac side (0fdecc1).** When Akshay sets Recorded himself, the Mac drafts the thank-you with the one-sided transcript, or without one after 24 hours.

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
     - The Mac (0fdecc1) then drafts the thank-you with the one-sided transcript. The calendar's ask doesn't come back, because the row is no longer Booked.
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

## Deploy (Main, after Cleanup accepts)

1. **First, gating everything:** Akshay installs the Mac prompt (routines/mac/transcripts.md, 0fdecc1) and passes the "TEST Matthew" run. Nothing below goes live before that test passes.
2. **Notion:** add the Status option "Awaiting transcript" to Episodes (collection://5d250752-6db8-4ab6-8467-c68f5838278a).
3. **Cloud:** rebuild on the live bases. Push the calendar, then the inbox, then Zoya, one at a time, and read back bytes, hash, cron and model.
4. **Records:** developer page change log and the calendar's routine page.

## Not in this package

- The thank-you wording (approved, on the wording page) and the Mac prompt (the CTO's).
- STEP 4e (Episode recovery) still accepts a Zencastr audio folder as evidence for days with several recordings. That's left as it is.
