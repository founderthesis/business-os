# Post-recording v2 (decision 374)

Akshay, 21 Oct, on Matthew Spacie's thank-you draft. Three fixes. Builds on Cut 1; do not start until Cut 1 is live and read back.

## 1. One thank-you template, patron always in (template awaits Akshay's ok)

Cause: the "FT thank-you, PR block variant" on the wording page has no patron paragraphs, and it brought back the release-date line decision 96 dropped. The calendar routine picks that variant whenever a PR person is on the thread, which is most guests.

Fix: one template, "FT thank-you after recording", with an optional PR block. The patron paragraphs are always in except for Sponsored guests. The PR variant is retired. Wording: see the CTO's chat proposal of 21 Oct; it goes on the wording page only after Akshay approves it.

## 2. Every person on a guest's threads is a Stakeholder

Cause: Yugesh Arora and Archana Mukherjee (PR) were in Cc on Matthew's 39-message thread since 29 Sep, but nothing ever turned mail Cc's into People. Decision 373 covers calendar invites only. The thank-you takes its Cc from Stakeholders, which was empty.

Fix, two parts:
- Inbox and Zoya STEP 1 (capture): every outside address in From, To or Cc of a thread matched to an Engagement is found in People (Email, Other emails) or created (Name from the display name, Organisation from the domain, Source Agent, Source ID "gmail:<thread id>"), then linked: guest's own address on the Guest row, everyone else in Stakeholders unless already Via. Team addresses and role inboxes never become Stakeholders.
- Every guest-facing composer (thank-you, day-before, reschedule, release mails): Cc is the union of Stakeholders, Via, and every outside address on the Engagement's threads and invites, minus anyone who asked to be dropped. A composer that finds an address not yet in People adds it before sending.

Data fix done 21 Oct: Yugesh Arora, Archana Mukherjee and Vijayalakshmi Bhat created and linked to Matthew's Engagement.

## 3. The transcript decides whether the recording happened

Today: the calendar run checks Zencastr audio size in Drive, sets Recorded, creates the Episode and drafts the thank-you; the Mac task (10:45 and 22:45 JST) later downloads the transcript and attaches it to the draft.

New chain, each step started by the one before:
1. Calendar (cloud): when a recording event has ended and was not cancelled, create its Episode at once with Status "Awaiting transcript" (keyed cal:<event id> as today). It no longer sets Recorded or drafts the thank-you. The Drive audio check is dropped.
2. Mac transcripts (Akshay's Mac, now hourly from 10:45 to 22:45 JST): picks up every Episode "Awaiting transcript", fetches the transcript from Zencastr or Riverside as today, then parses it. Recorded = the guest and the host both speak, the last timestamp is 20 minutes or more, and it covers the recording's duration (the existing coverage check). Then, in one pass:
   - Episode: Transcript file attached and read back (as today), Status "Transcript in".
   - Engagement: Status Recorded, Call type cleared, Claude note "recorded <date> (transcript, <mm> min)".
   - Thank-you: creates the draft in ad@thepodium.in with the transcript attached, from the approved template, To the guest and main PR, Cc per part 2. Akshay reviews and sends (decision 300 holds). Next action "Akshay: send the thank-you draft to <guest>".
   - A transcript under 20 minutes or with one speaker: not recorded. Claude note line and a report line; Akshay is asked only if no transcript exists 24 hours after the slot.
3. Calendar's later steps (WhatsApp blurb, Community ask, Episode recovery) key off Status Recorded as they do now, so they follow the transcript automatically.

Trigger, honestly: the calendar run can't start a task on the Mac. "Triggered" means the Episode row the calendar creates is the Mac task's work list, and the Mac task runs hourly, so the draft lands within about an hour of Zencastr finishing the transcript.

Notion link instead of attachment: not possible. Notion file links are signed and expire within about an hour, and Notion has no public link to a file on its own, only to a page. The transcript stays an attachment.

Permission change this needs: the Mac task today may only add a file to an existing draft (decisions 333, 334). Creating the thank-you draft in ad@thepodium.in is new. Akshay's 21 Oct instruction ("the transcript fetch should trigger the confirmation of recording and the composition of the mail") is the approval; it still never sends.

Client shows (un#, Built to Share, Human by Design): the same chain on Riverside; un# studio has no transcript export, so un# keeps the calendar rule (recorded 2 hours after the slot unless the thread says otherwise).

Akshay's one step: paste the new Mac prompt into the desktop app's "Mac transcripts" task and set it hourly.
