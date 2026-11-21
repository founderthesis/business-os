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

Updated for Codex's three corrections (19 Oct). Earlier rows T1 to T15 still hold where not replaced here.

### Correction 1: the exact draft (7a to 7f)

| # | Case | Trace | Result |
|---|---|---|---|
| A1 | Returning guest across two shows: FT recording 2 Oct, un# recording 16 Oct. Both have Episodes and thank-you Activities. | 7a takes, for each Episode, only the Activity on that Engagement captured after that Episode's Recording date and linked to that Episode (or, if unlinked, captured before the later Episode's date). The un# Episode gets the "client thank-you" draft, the FT one the "FT thank-you" draft. | Each draft gets only its own Episode's file. |
| A2 | Shared PR address on two guests' threads. | No address or subject matching anywhere in 7: drafts come from the Activity's Draft ID and thread. | The other guest's draft is never touched. |
| A3 | Akshay edits the draft's HTML (bold, a link), and the plaintext stays the same. | 7d snapshots the edited HTML. 7e compares the HTML too (whitespace between tags ignored). If the update changed the HTML, it fails and pauses. | His formatting is checked, not only the plaintext. |
| A4 | The draft already has his PDF. | 7d hashes the PDF. 7e requires the same sha256 after. | The PDF's content is proven unchanged. |
| A5 | Two Activities, or two drafts on the thread. | 7a or 7c: ambiguous, touch none, "no linked thank-you draft" or both reported. | Waits; nothing guessed, no second thank-you. |
| A6 | Akshay sent a thank-you for this guest's earlier Episode, on another thread. | 7b looks only at the linked thread. Mail on other threads never counts. | Not marked sent. This Episode's own draft still gets its file. |
| A7 | The connector refuses the attachment-only update. | 7d: the draft is untouched, the limitation is reported, THANKS stays open, and 7f pauses THANKS. | No partial edit; Akshay sees why. |

### Correction 2: unfinished work carries on ("## Open Mac jobs")

| # | Case | Trace | Result |
|---|---|---|---|
| B1 | Day 29: FILE and COPY done, no thank-you draft yet. | The Episode's line reads "open: THANKS". 7a: "no linked thank-you draft". | Waits. |
| B2 | Day 31: the calendar run's draft appears (Activity with Draft ID). | 1b takes every Open Mac jobs line whatever its age. FILE and COPY are seen done from the Episode file and the Drive hash, not redone. 7 attaches; the line is removed. | THANKS resumes. No second upload or copy. |
| B3 | Zencastr still processing for two days. | 3b1 waits; the line says "open: FILE, COPY, THANKS". The fresh window covers it anyway, and the line covers it past day 30. | Retried until ready. |
| B4 | Crash after the line was written, mid-upload. | Next run: the line puts it in the work list; 5 re-fetches, sees Transcript file empty, uploads once. The unplaced earlier upload expires. | One file. |
| B5 | Akshay writes "cancel THANKS" on a line. | The worker leaves that job and reports it. Age never closes a job. | Only Akshay cancels. |

### Correction 3: no unverified or mismatched file goes anywhere

| # | Case | Trace | Result |
|---|---|---|---|
| C1 | The WAV is 44.1 kHz stereo and the MP3 is 192 kbps. | 4b reads the duration from the provider page, else from the media header (afinfo or ffprobe), never from size. | The duration is the file's own; nothing is assumed. |
| C2 | The transcript stops at 41:10 of a 62:00 recording. | 4b: "partial", not used, retried. | Not attached, copied or put on the draft. |
| C3 | The Drive copy has the right name and size but different text. | 6 compares sha256: "Drive copy differs", never overwritten, COPY open, reported. | The mismatch is caught. |
| C4 | The Episode's file doesn't match the sha256 in its "## Transcript" record. | 3a: no COPY, no THANKS for that Episode; line kept open; reported for Akshay. | Nothing known-mismatched spreads. |
| C5 | No duration anywhere (the un# studio, no Drive for desktop). | 4b: "coverage unverified", not attached, line open, reported. | Never certified complete. |
| C6 | The draft gains a file of the right name and size but different content. | 7e downloads it and compares its sha256 with the Episode file's: fail, pause. | Caught. |

## Readbacks done from the cloud, 19 Oct

- **Calendar writer:** Saket Saurabh's 30 Oct invite carries "Recording link: zencastr.app.link/sfDPoAXzh6b" and the location, written by the calendar run on 17 Oct. The zcal description, the 11:00 to 13:00 JST time and the three attendees were kept.
- **Hitarth Dadia, rechecked:** the recording event is Thu 29 Oct, 19:30 to 21:30 JST, accepted. The Engagement is Booked, Next date 29 Oct 10:30 UTC, and Recording link is empty. The 8 Sep event was the precall.
- **Notion file:**
  - Sankalp Arora's 15 Oct Episode file, downloaded from Transcript file: 58,211 bytes, sha256 161a2e2f4818bea3, the same as the Episode's provenance line. It ends at 59:41 ("we are just at one hour mark. Let me stop").
  - A file-size estimate from the same Drive folder (3,584 seconds, assuming 48 kHz mono WAV and 128 kbps MP3) happened to agree. Codex is right that the size proves no encoding, so the prompt no longer uses it.
- **Gmail draft attachment: not verified from the cloud.**
  - A test draft was made from ad@ to ad@ on an internal thread. The Gmail connector's draft read does not list existing attachments, and its update_draft drops attachments it isn't given again, so it is not used.
  - MCP Emails did see the test draft's attachment and its In-Reply-To.
  - The next step, editing the test draft, was refused by this session's safety check, so it was not tried another way. The test draft was deleted, and Drafts is empty again.
  - The worker no longer runs this test itself. Step 0 is a gate that opens only after a supervised probe Akshay explicitly authorises (docs/install-2026-10-19.md, "The draft-attach probe").
