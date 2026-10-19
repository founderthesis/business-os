# Tasks on Akshay's Mac

Two scheduled tasks run on the Mac, in the Claude desktop app (Scheduled tasks). Install and cut over with docs/install-2026-10-19.md. They exist because Zencastr and Riverside have no API and the cloud can't upload files to Notion. Each prompt file is self-contained and paste-ready, with its own setup block.

| Task | File | When (JST) | Connectors | Chrome sites | Writes |
|---|---|---|---|---|---|
| Mac transcripts | transcripts.md | daily 22:45 | Notion, Google Calendar, Google Drive, Gmail (read), MCP Emails | zencastr.com, riverside.fm, mail.google.com, app.notion.com | Episode Transcript file and Status, Drive copy, one "Transcript \| <guest>" mail into ad@ from Zoya, Engagement Claude note |
| Zencastr links | zencastr-mac.md | daily 09:52 and 17:52 | Notion, Google Calendar (read) | zencastr.com | Engagement Recording link (Call link if empty), Call type, its own Next action segment, Claude note |

One-off, not scheduled: transcripts-blue-youtube.md (part B, for Episodes with a YouTube link and no transcript anywhere).

Retired: routines/retired/mac-transcripts-v1.md (8 Oct nightly prompt, replaced by transcripts.md) and transcripts-backfill.md.

Not Mac tasks, despite the name: "Founder Thesis guest evals" (routines/cowork-evals.md) and "Host dossiers and prep notes" (routines/cowork-dossiers.md) were created from Cowork but run as cloud scheduled tasks on claude.ai (trig_01R1yHgEztVEo832zMwUugBr and trig_01WfLf8Zx9c34fSzfrTeUY5M, cloud sessions, all account connectors). The cloud can read their live prompts; for those two the whole file is the prompt.

Mac task prompts are local to the Mac, so the cloud can't read what is deployed. It checks outcomes instead: Episode Transcript file filled, the "Transcript |" mail in ad@, the Recording link on the Engagement, and the "(Mac)" Claude note lines.
