# Tasks on Akshay's Mac

Two scheduled tasks run on the Mac, in the Claude desktop app (Scheduled tasks). Install and cut over with docs/install-2026-10-19.md. They exist because Zencastr and Riverside have no API. Each prompt file is self-contained and paste-ready, with its own setup block.

| Task | File | When (JST) | Connectors | Chrome sites | Writes |
|---|---|---|---|---|---|
| Mac transcripts | transcripts.md | daily 10:45 and 22:45 | Notion, Google Drive, Gmail, MCP Emails (ad@ inbox), Google Calendar | zencastr.com, riverside.fm | Episode Transcript file, Status and "## Transcript" lines, the .txt on Akshay's thank-you draft (never sent), Engagement Claude note and one Next action phrase |
| Zencastr links | zencastr-mac.md | daily 09:52 and 17:52 | Notion, Google Calendar (read) | zencastr.com | Engagement Recording link (Call link if empty), Call type, its own Next action segment, Claude note |

Blue is retired (AR-20261019-6, 19 Oct): the one-off Blue and YouTube backfill prompt is gone from this folder (git history keeps it) and the paused Mac task "Blue transcripts backfill (one-time, after maintenance)" is to be deleted. Missing transcripts are recovered from Zencastr, Riverside, mail and Drive only.

Retired: routines/retired/mac-transcripts-v1.md (8 Oct nightly prompt, replaced by transcripts.md) and transcripts-backfill.md.

Not Mac tasks, despite the name: "Founder Thesis guest evals" (routines/cowork-evals.md) and "Host dossiers and prep notes" (routines/cowork-dossiers.md) were created from Cowork but run as cloud scheduled tasks on claude.ai (trig_01R1yHgEztVEo832zMwUugBr and trig_01WfLf8Zx9c34fSzfrTeUY5M, cloud sessions, all account connectors). The cloud can read their live prompts; for those two the whole file is the prompt.

Mac task prompts are local to the Mac, so the cloud can't read what is deployed. It checks outcomes instead: Episode Transcript file and its hash, the Drive copy, the .txt on the thank-you draft, the Recording link on the Engagement and on the invite, and the "(Mac)" lines (decision 334).
