# Episode context pilot

Status, 5 Nov: built and dry-run, not generated. This session has no `ANTHROPIC_API_KEY`, so the batch was never sent. The 10 Markdown dumps land here once a session with the key runs the two commands below.

## The 10 episodes

| # | Episode | Show | Released | Episode id |
|---|---|---|---|---|
| 1 | Anand Jain @ CleverTap - Founder Thesis - V2 | Founder Thesis | 10 Jan 2025 | 3ed19a301a7f8184b716df56bd9ff620 |
| 2 | Ajay Singhania @ Epack Durable - Founder Thesis | Founder Thesis | 4 Mar 2025 | 3ed19a301a7f81ccaf0dfab1bc09a205 |
| 3 | Amit Gupta @ Yulu - Founder Thesis - V2 | Founder Thesis | 13 Jun 2025 | 3ed19a301a7f8185bbe6dda356973a9e |
| 4 | Prithwi Singh @ Khetika - Founder Thesis | Founder Thesis | 6 Jan 2026 | 3ed19a301a7f8153a115c5886bd8898f |
| 5 | Manish Sabharwal @ TeamLease Services - Founder Thesis | Founder Thesis | 21 Sep 2026 | 3ed19a301a7f81de9ad3d191709a7607 |
| 6 | Dhruv Toshniwal @ The Pant Project - Founder Thesis | Founder Thesis | 28 Sep 2026 | 3ed19a301a7f812c916fe07ce98c61b4 |
| 7 | Gaurav Mishra @ Proshort - Founder Thesis | Founder Thesis | 13 Oct 2026 | 3ed19a301a7f81529fe2d0ace6c3a588 |
| 8 | Sandy Kaul @ Franklin Templeton - un# | un# | published | 3ed19a301a7f81a9bd24de0da97e36c6 |
| 9 | Raagulan Pathy @ KAST - un# | un# | recorded 25 Sep 2026 | 3ed19a301a7f8194ad73fa1c526c1380 |
| 10 | Nand Kishore Chaudhary @ Jaipur Rugs - Built to Share | Built to Share | recorded 1 Oct 2026 | 3ed19a301a7f8166b9bbc00aeb83d890 |

All 10 transcripts were read from the Episode's Transcript file attachment (713 KB of text in total).

## To finish the pilot

1. Download each Transcript file into `data/episode_context/transcripts/` and write `data/episode_context/manifest.json` (format in the script's docstring). Notion's signed file links expire in 5 minutes, so fetch and download one page at a time.
2. `python migration/episode_context.py submit` sends one Sonnet 5.5 batch with the shared instructions cached.
3. `python migration/episode_context.py collect` waits for the batch, then writes JSON and Markdown to `data/episode_context/out/` and tokens and cost to `usage.csv`.
4. Copy the 10 `.md` files here.

## What to know before the full run

- 526 of the 621 Founder Thesis episodes keep their transcript only as a Transcript URL on ft-transcripts.vercel.app. This environment's network policy blocks that host. The full run needs it allowed, or it has to run somewhere that can reach it.
- These are raw recording transcripts, so timestamps are recording time, not the published episode's timeline.
