# Blue legacy transfer: Phase B result (9 Nov 2026)

Decision 533 (Akshay reopened decisions 28 and 344). Data only; no files moved. One Notion writer throughout. Every write was logged per operation in data/blue_legacy/write/applied/ (git-ignored). Builder: migration/blue_legacy_phase_b.py.

## What was written

| Step | Target | Planned | Applied | Skipped | Errors |
|---|---|---|---|---|---|
| 1 | Organisations: new LinkedIn (url) property | 1 | 1 | 0 | 0 |
| 2 | Organisations LinkedIn fills | 122 | 122 | 0 | 0 |
| 3 | People fills (Email 128, Role 100, LinkedIn 28) | 165 pages | 165 | 0 | 0 |
| 4 | Episodes fills (empty cells only) | 629 pages, 804 cells | 629 / 804 | 0 | 0 |
| 4 | New Episode (Saurabh Garg, Built to Share) | 1 | 1 | 0 | 0 |
| 5 | Engagements Dossier link fills | 6 | 6 | 0 | 0 |
| 6 | Guest forms created (133 Merged, 3 Needs review) | 136 | 136 | 0 | 0 |
| 7 | Activities from Blue comments | 34 | 34 | 0 | 0 |
| 8 | Blue legacy archive page plus 17 docs | 18 | 18 | 0 | 0 |
| 9 | Archive pages (Inner Journeys, Vanshika, Vanshika Projects, Prompts) | 4 | 4 | 0 | 0 |
| 10 | Provenance lines appended to page bodies | 931 | 931 | 0 | 0 |

Episodes cells by column: Amazon Music 458, Copywriting doc 177, LinkedIn 140, Sector 8, Short link 9, Apple 4, YouTube 3, Substack 3, Spotify 2.

## Reconciliation

- Episodes 691 to 692. For all nine filled columns, the pre-run non-empty count plus cells written equals the live count.
- Guest forms 8 to 144.
- Activities: 34 Blue-sourced rows, exact. The table total rose by 36 during the run because a live routine also wrote.
- 22 new pages under Business OS developer: the archive parent, 17 docs, 4 archive pages.
- Drift: no cell was non-empty at write time. 303 planned fills had been dropped in prep because the Amazon Music and Short link backfill had already filled them.

## Checks

- Read-back sample of 10 rows across Organisations, People, Episodes, the new Episode, Engagements, Guest forms and Activities: 10 pass.
- All 17 docs and 3 of 4 archive pages match the Blue source text exactly; Prompts differs in formatting only (bold shown as tags, curly quotes), no wording or ids.
- The Vanshika Projects (110 rows) and Inner Journeys (24 rows) tables were rebuilt so every row sits inside the table.

## Not done, on purpose

- Files: photos, logos, transcripts and PDFs (about 1,300) wait for the file route; 153 videos (20.4 GB) stay in Blue, listed in data/blue_video_manifest.csv.
- 94 conflicts: Notion kept its value (data/blue_conflicts.csv).
- Held for a yes: Source ID appends on 9 exact same-show name matches (05b), and a second Arpit Chhabra Episode (04b), since one already exists.
- Blue due date: not mapped to any field.

## Follow-ups

- Blue Home docs hold plaintext passwords and a phone number; none were copied. They should be rotated before Blue is switched off.
- Two Episode rows for Nikhil Barshikar (Imarticus) now share one Amazon Music link: likely a duplicate Episode.
- Private Drive backup of the git-ignored extract is waiting for Akshay's own ok.
