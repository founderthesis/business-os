# Mac workers: walkthroughs for repeat runs and partial recovery (19 Oct 2026)

Desk checks of routines/mac/transcripts.md and routines/mac/zencastr-mac.md, traced against the prompt text. The cloud can't run Mac tasks, so these are traced rather than executed. The live readbacks that were possible from the cloud are at the end.

## Zencastr links

| # | Situation | What the prompt does | Duplicates? |
|---|---|---|---|
| Z1 | Hitarth Dadia, Booked, Next date 29 Oct 10:30 UTC, event "Podcast Recording \| Hitarth Dadia" 19:30 to 21:30 JST, accepted; the 8 Sep event is his old precall. | Step 1 takes the slot from the recording event (19:30 JST), not the precall. 2b finds no room, creates one. 2c writes the Recording link and reads it back. 2d removes only "Akshay: build the Mac routine ..." and keeps "Recording on 29 Oct". | One room |
| Z2 | The same run again, an hour later. | Recording link is a zencastr link, so step 2 skips the row. Step 3 checks the invite. | None |
| Z3 | The run stopped after creating the room, before writing Notion. | The next run's 2b finds the room by the guest's name, with nothing recorded, and reuses it. | One room |
| Z4 | The guest moved the booking between 2b and 2c. | 2c sees the event start changed, writes nothing, reports with the room name. The next run reuses the room and sets its time if Zencastr allows. | One room |
| Z5 | The link was written at 09:52; the calendar run at 16:35 adds it to the invite. | The 17:52 run's step 3 finds the link in the invite, adds "invite carries the Recording link", and compares start, end and attendees with the 2c line. | n/a |
| Z6 | The invite still lacks the link after a calendar run, recording 10 days out. | Step 3 reports "invite still without the link" every run until it's there. It never edits the event. | n/a |
| Z7 | The calendar run added a different link. | Reports "invite has another link"; changes nothing. | n/a |
| Z8 | Next action also holds "Zoya: send the prep note". | 2d keeps it; Waiting on is never touched. | n/a |

## Mac transcripts

| # | Situation | What the prompt does | Duplicates? |
|---|---|---|---|
| T1 | Recording ended 21:30; Zencastr still processing at 22:45. | 3b1 waits ("waiting for Zencastr"); all three jobs stay open. 10:45 retries. | n/a |
| T2 | Transcript ready, 61 min; the recording page says 62:10. | Coverage passes (within 5 min). FILE, then COPY. THANKS: the calendar run wrote the draft at 22:35, so it's attached and read back. | n/a |
| T3 | The run stopped after notion-create-attachment, before setting Transcript file. | Transcript file is still empty, so the next run attaches again. The first upload was never placed and expires. | One file on the Episode |
| T4 | The run stopped after Transcript file was set, before the readback or COPY. | 3a downloads the Episode's own file, then 5's readback and COPY run. FILE is never uploaded twice because 5 re-fetches first. | None |
| T5 | Transcript file filled, Drive copy present, no draft yet (Akshay deleted it, or the calendar run hasn't written it). | The work list still holds the Episode, because THANKS is open. 7b: "waiting for thank-you draft". Each run retries; after 21 days it reports "no thank-you draft after 21 days". | n/a |
| T6 | The run stopped after the MCP Emails draft update, before the readback. | The next run's 7c finds FILE NAME on the draft with the same bytes and marks THANKS done. The snapshot is lost, so preservation of that one draft isn't re-proved; the probe (step 0) already proved the method. | One attachment |
| T7 | Akshay edited the draft's wording and added a PDF. | 7d snapshots the edited body and the PDF. The update passes only the attachment. 7e checks body, recipients, thread and the PDF are unchanged. | n/a |
| T8 | Akshay already attached a transcript himself. | 7c: done, no change. | None |
| T9 | Akshay sent the thank-you without the transcript. | 7a: "thank-you sent without transcript", reported once. Nothing sent or drafted. | No mail |
| T10 | Two matching drafts. | 7b touches neither and reports both. | n/a |
| T11 | The readback finds the subject or thread changed. | Pauses THANKS everywhere ("draft attach paused") and reports. Akshay checks that draft. | n/a |
| T12 | A returning guest; Drive has a copy dated six months ago. | 4a/6: another date is another recording, so a new copy is made with this date. | n/a |
| T13 | A file in Downloads matches on first name only. | 3b4 needs full name and date, so it's not a source. 4a: "unidentified". | n/a |
| T14 | un# studio recording; no duration anywhere. | 4b: "coverage unverified", not attached, retried and reported. | n/a |
| T15 | A thank-you thread with an unread reply from the guest. | Only Gmail and MCP Emails reads; Chrome never opens Gmail; read state is untouched. | n/a |

## Readbacks done from the cloud, 19 Oct

- **Calendar writer:** Saket Saurabh's 30 Oct invite carries "Recording link: zencastr.app.link/sfDPoAXzh6b" and the location, written by the calendar run on 17 Oct. The zcal description, the 11:00 to 13:00 JST time and the three attendees were kept.
- **Hitarth Dadia, rechecked:** the recording event is Thu 29 Oct, 19:30 to 21:30 JST, accepted. The Engagement is Booked, Next date 29 Oct 10:30 UTC, and Recording link is empty. The 8 Sep event was the precall.
- **Notion file:**
  - Sankalp Arora's 15 Oct Episode file, downloaded from Transcript file: 58,211 bytes, sha256 161a2e2f4818bea3, the same as the Episode's provenance line. It ends at 59:41 ("we are just at one hour mark. Let me stop").
  - The Drive audio estimate from the same recording folder is 3,584 to 3,585 seconds (59:45) from both the .wav and the .mp3.
- **Gmail draft attachment: not verified from the cloud.**
  - A test draft was made from ad@ to ad@ on an internal thread. The Gmail connector's draft read does not list existing attachments, and its update_draft drops attachments it isn't given again, so it is not used.
  - MCP Emails did see the test draft's attachment and its In-Reply-To.
  - The next step, editing the test draft, was refused by this session's safety check, so it was not tried another way. The test draft was deleted, and Drafts is empty again.
  - The first Mac run's step 0 runs this same test, with Akshay watching, before any real draft is touched.
