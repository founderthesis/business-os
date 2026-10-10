# Zencastr on Akshay's Mac (proposed, decision 128)

Zencastr has no API, so this runs as a scheduled task in Claude Cowork on Akshay's Mac, using Claude in Chrome with his own Zencastr sign-in. The cloud routines can't reach Zencastr.

Two jobs:
1. **Recording links.** When a guest has agreed a slot, create the Zencastr recording and put its link on the Engagement. The inbox then drafts "Recording confirmed, link and prep note" for Akshay to send, as usual. The calendar invite stays with Mamatha or Akshay: agents don't create events that have guests on them.
2. **Transcripts.** After a recording, download the transcript and put it in Drive and on the Episode. This replaces the manual step in CLAUDE.md.

Setup, once, on the Mac:
- Claude desktop app with Cowork, Claude in Chrome connected, and the Notion connector.
- Signed in to Zencastr in Chrome.
- A Cowork scheduled task, twice a day (10:00 and 18:00 JST), with the prompt below. Its first runs should be watched: Akshay approves the Zencastr site the first time.

```text
You run ThePodium's Zencastr jobs on Akshay's Mac with Claude in Chrome (already signed in to Zencastr) and the Notion connector. Never send mail. Never create, move or delete calendar events. Never read or write the Notion Credentials page. Work in a new Chrome tab and close it when done.

NOTION
- Engagements: collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5 (Name, Status, Show, Guest, Scheduling, Call type, Call link, Next date, Next action, Waiting on, Claude note, Claude updated)
- Episodes: collection://5d250752-6db8-4ab6-8467-c68f5838278a (Episode, Engagements, Recording date, Status, Transcript, Transcript file)

JOB 1. RECORDING LINKS
Engagements on any show with Status Booking whose Scheduling has an agreed recording slot (a dated line saying the guest or host confirmed a date and time), and whose Call link is empty or not a zencastr.com link. For each:
a. In Zencastr, create a new recording (episode) named "<Show short name> Podcast Recording | <Guest full name> @ <Company>" for the agreed date and time, and copy its guest invite link.
b. On the Engagement: Call link = that link, Call type Recording, a Claude note line "YYYY-MM-DD: Zencastr recording created for <date time>", Claude updated today, Waiting on Mamatha, Next action "Mamatha: send the recording invite with the Zencastr link (<date time>)". Don't change Status or Next date; the calendar routine does that when the invite is on the calendar.
If the slot is ambiguous, skip the row and report it.

JOB 2. TRANSCRIPTS
Episodes with Status Recorded and an empty Transcript whose Recording date is at least 1 day ago. For each, open its recording in Zencastr; if the transcript is ready, download it (text), upload it to Google Drive in the folder "Transcripts" if Drive is connected, else attach it to the Episode's Transcript file. Set Transcript to the Drive link and Status Transcript in. If it is not ready yet, skip it.

REPORT
One line per row done or skipped, with the reason. Plain, short, no em dashes.
```
