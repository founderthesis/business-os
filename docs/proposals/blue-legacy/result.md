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
- 04b, a second Arpit Chhabra Episode: not created (CTO, 9 Nov). One already exists: "Arpit Chhabra @ IoTfy - Founder Thesis".
- Blue due date: not mapped to any field.

## After the run (9 Nov, CTO answers)

- 05b applied: "; Blue <id>" appended to Source ID on 11 rows that are exact same-show name matches (9 Episodes and the 2 Engagements linked to them), read back.
- Credential check: none of the 17 docs, 4 archive pages, guest forms, Activities or body lines carries a password, login, key or phone number; the only hits are the notes saying Blue holds them and they were not copied. The git-ignored extract has none either.
- Two wrong Amazon Music fills found and cleared: Blue's Episodes Inventory cards for Twid (Amit Koshal) and Xpressbees (Amitava Saha) held the Imarticus and CleverTap episodes' links. Both cells were empty before this run, so they are empty again, with a note in each page body. A URL-vs-name check over all 458 Amazon Music fills found no others.
- The "probable duplicate" Imarticus Episode was not a duplicate: it was the Twid row with the wrong link. Nothing was folded or trashed.

## Follow-ups

- Blue Home docs hold plaintext passwords and a phone number; none were copied. They should be rotated before Blue is switched off.
- Twid and Xpressbees Episodes have no Amazon Music link; the right ones still need finding. The Xpressbees Copywriting doc came from the same card and is worth a glance.
- Private Drive backup of the git-ignored extract is waiting for Akshay's own ok.
