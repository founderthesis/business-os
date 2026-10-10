# Zencastr on Akshay's Mac (proposed, decision 128)

Zencastr has no API, so this runs as a scheduled task in the Claude desktop app on Akshay's Mac, using Claude in Chrome with his own Zencastr sign-in. The cloud routines can't reach Zencastr.

One job: **recording links.** When a Founder Thesis guest has agreed a slot, create the Zencastr recording and put its link on the Engagement. The calendar invite stays with Mamatha: agents don't create events that have guests on them. Only FT records on Zencastr (un# uses the unhashed studio, B2S Riverside), so other shows are left alone.

Transcripts are a separate nightly task already specced in `transcripts-after-recording.md` (decision 85). Set that one up too; don't merge the two.

## Handover

The prompts are self-contained: a new Mac chat or scheduled task needs nothing else. Keep them apart from the chat that is running the one-off backfill (`transcripts-backfill.md`, `transcripts-blue-youtube.md`): let that finish, then set up the two scheduled tasks fresh. Each task needs the Notion connector and Claude in Chrome; the transcript task also needs Google Calendar. On the first run, watch it and choose "always allow" for Notion and for zencastr.com in Chrome.

Setup, once, on the Mac:
- Claude desktop app, Claude in Chrome connected, and the Notion connector.
- Signed in to Zencastr in Chrome.
- A scheduled task in the Claude desktop app, twice a day (10:00 and 18:00 JST), with the prompt below. Its first runs should be watched: Akshay approves the Zencastr site the first time.

```text
You create Zencastr recording links for ThePodium's Founder Thesis podcast on Akshay's Mac with Claude in Chrome (already signed in to Zencastr) and the Notion connector. Never send mail. Never create, move or delete calendar events. Never read or write the Notion Credentials page. Work in a new Chrome tab and close it when done.

NOTION
- Engagements: collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5 (Name, Status, Show, Guest, Scheduling, Call type, Call link, Next date, Next action, Waiting on, Claude note, Claude updated)

Founder Thesis Engagements (Show page 3ed19a301a7f817c9367e0d88afc5776) with Status Booking whose Scheduling has an agreed recording slot (a dated line saying the guest or host confirmed a date and time), and whose Call link is empty or not a zencastr.com link. For each:
a. In Zencastr, create a new recording (episode) named "FT Podcast Recording | <Guest full name> @ <Company>" for the agreed date and time, and copy its guest invite link.
b. On the Engagement: Call link = that link, Call type Recording, a Claude note line "YYYY-MM-DD: Zencastr recording created for <date time>", Claude updated today, Waiting on Mamatha, Next action "Mamatha: send the recording invite with the Zencastr link (<date time>)". Don't change Status or Next date; the calendar routine does that when the invite is on the calendar.
If the slot is ambiguous, skip the row and report it.

REPORT
One line per row done or skipped, with the reason. Plain, short, no em dashes.
```
