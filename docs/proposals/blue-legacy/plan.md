# Blue legacy transfer: Phase A plan

Status: proposal, 9 Nov 2026. Phase A was read-only: nothing was written to Blue or Notion. Extract in `data/blue_legacy/` (git-ignored), analysis in `migration/blue_legacy_phase_a.py` (re-runnable). Batch for every Phase B write: `blue-legacy-2026-11-09`.

Before anything else: this transfer reopens two closed decisions. Decision 28 (30 Sep) says "From Blue, copy field data only. Videos, photos and other heavy files are dropped", and decision 344 (19 Oct) retired the Blue backfill. Phase B needs Akshay to confirm he has reopened both, and the override goes in `docs/decisions.md`.

## What Blue holds today

Counts are measured on 9 Nov unless marked [E]. Blue grew since the 30 Sep audit: FT 155 to 161, Hissa 16 to 18.

| Workspace | Live records | Missing from Notion by key | Fields with values | Fields with no Notion home yet | Comments (records) | Docs | Form submissions | Files |
|---|---|---|---|---|---|---|---|---|
| FT & Spotlight | 161 | 3 | 53 | 25 | 23 in feed; 6 readable (6) | 7 | 136 | 1,164 |
| un# (Blue name "alpha un#") | 48 | 0 | 49 | 24 | 50 in feed; 29 readable (14) | 4 | 0 | 454 |
| Hissa / Built to Share | 18 | 2 | 33 | 9 | 0 | 1 | 0 | 29 |
| FastCode / Human by Design | 4 | 0 | 24 | 4 | 0 | 1 | 0 | 6 |
| Episodes Inventory | 500 | 10 | 32 | 13 | 4 in feed; 1 on a live card | 2 | 0 | 420 |
| Inner Journeys (archived) | 24 | archive page | not exported | | 0 | 2 | 0 | 120 |
| Prompts (archived) | 5 | archive page | 17 prompt fields | | 0 | 0 | 0 | 0 |
| Vanshika Projects (archived) | 110 | archive page | not read | | 0 | 0 | 0 | 0 |
| Vanshika (archived) | 4 | archive page | not read | | 0 | 0 | 0 | 0 |
| **Total** | **874** | **15** | | | **35 readable on live cards** | **17** | **136** | **2,193** |

How the match was made. Every Blue guest card the 2 Oct migration touched carries Source ID `Blue <record id>` on its Engagement (227 rows) and, for cards that became new Episodes, on the Episode (106 rows). Record ids are mixed (old cuid and new hex), so the key is the raw id. Inventory cards have no Source ID in Notion; they match on YouTube video id (396) or Spotify episode id (94). Name match was used only to fill the report column in `data/blue_legacy/not_in_notion.csv`.

The 15 missing by key:
- FT 3: Wysa (Published), Sorin Investments (Recorded), GyanDhan (Slotted). All three have a Notion Episode by name, created by later routines without a Blue Source ID.
- Built to Share 2: Prashant Sachan (Ready to Publish, name match exists on both FT and Built to Share Episodes) and Saurabh Garg (Recorded, no Episode; a People row exists).
- Episodes Inventory 10: 9 have a single name match in Notion; 1 (Arpit Chabbra @ IOTfy, In Progress) has none, while a People row spelled Chhabra exists.

Form submissions. 136 FT cards were created by the "Thank you for recording!" form (Created By empty and the form footer in the description). 133 of them already have an Engagement in Notion and 132 Episodes have Guest form in ticked. None of the 136 exists as a Guest forms row (that table has 8 rows, all new since 7 Oct). Fields on the form: guest name, company, guest email, designation, company LinkedIn (130 with a value), guest LinkedIn (136), hi-res photo (142 cards), logo (77), recording date (127), PR emails 1 to 4 (149, 112, 61, 28), Google Ads choice (67; 11 said yes to INR 5k or 10k).

Comments. The activity feed counts 77 comments; 41 sit on internal cards that no longer exist (Quote Card Deadlines, Vanshika To Do, Updates, Feedback on Christian, Bugs, and untitled deleted cards) and cannot be read. 35 are readable on 20 live guest cards (6 FT, 29 un#), 1 of them empty, so 34 move. Content: schedule notes, pre-call recording and transcript links, intro reel copy, edit notes ("needs some cuts"). The 1 on an inventory card was not read.

Docs (17). FT: FT Editing Process, FT Release Process 2024, Spotlight Release Process 2024, Working Doc Template, Competitors 2024, FT 10K ad, Home. un#: AU Editing, Dossier Process, Scope of work, Home. Inventory: Rework Old Episodes, Home. Built to Share: Home. Human by Design: Home. Inner Journeys: IJ Ad Prompt, Home.

Archived workspaces and whose work they are:
- Inner Journeys: ThePodium's former show hosted by Divakar Vijayasarathy (24 guest cards, Proposed to Published). Its guests became People on 2 Oct.
- Prompts: ThePodium's LLM repurposing prompts for FT, un# and Inner Journeys (5 cards). Superseded by `skills/`.
- Vanshika Projects: ThePodium work. Slug "thumbnail"; the 110 cards are named after FT and un# guests and sit in "Uploaded on Blue", so it was the thumbnail design queue.
- Vanshika: ThePodium work. 4 cards: B2S Launch, Vinay B2S Episode, Iron Pillar, Human in the Loop Launch.

## Gap list and where each value goes

Default rule: never overwrite a non-empty Notion value. A Blue value that differs goes to `data/blue_conflicts.csv`.

Already mapped to an existing property. These Blue values have a Notion property, and the counts are the empty Notion cells Phase B fills:
- Episodes: Amazon Music 650 (489 inventory, 106 FT, 40 un#, 15 B2S), Copywriting doc 177, Short link 157, LinkedIn 140 (FT LI announcement, un# Sri's LI post), YouTube 3, Spotify 2, Apple 4, Substack 3, Transcript file 3 (every other episode already has a transcript file or link from the October backfill).
- Engagements: Dossier link 6; Stakeholders, 9 PR links to People rows that already exist.
- People (the guest row on the Engagement): Email 137, Role 104, LinkedIn 31.
- Organisations: Website, from un#, B2S, HBD and inventory cards where the org row has none.

No home yet. Each of these needs a new property, a page body section, a Guest forms row or the manifest:

| Blue field (workspaces) | Records with a value | Value type | Goes to |
|---|---|---|---|
| Company LinkedIn (FT, un#, B2S, HBD) | 130, 34, 11, 2 | url | New property: Organisations.LinkedIn (url) |
| Hi-res photo, logo (FT form) | 142, 77 | image files | Guest forms row: Photo, Logo |
| Thumbnails, quote cards, episode-out-now, deep dive, infographics, guest pic (FT, un#, B2S, HBD, inventory) | about 1,000 files on 300+ cards [E] | image or pdf files | New property: Episodes.Assets (file) |
| Dossier PDFs, LinkedIn PDFs in "Source data" (un#, B2S) | 8 | pdf | Episodes.Assets |
| Intro reel, shorts and reels (FT, un#) | 40, 16 | mp4 | Video manifest; one body line naming the file |
| Audio file (FT, un#) | 9, 4 | audio | Drive folder linked from the Episode body |
| Episode title, show notes, thumbnail copy, LinkedIn release copy (FT) | 12, 18, 6, 16 | text | Episode body, "Copy from Blue" |
| Unlisted video (FT) | 34 | url | Episode body, "Links from Blue" |
| LinkedIn newsletter (FT, inventory) | 55, 11 | url | Episode body, "Links from Blue" |
| Pocket Casts, creators.spotify, Opus, guest assets, Sri's X post (un#) | 10, 30, 2, 1, 28 | url | Episode body, "Links from Blue" |
| Episode number (un#, B2S) | 32, 2 | number | Episode body |
| Guest X (un#) | 34 | url | Guest People body, "Links from Blue" |
| Company X (un#) | 28 | url | Organisation body |
| Google Ads choice (FT form) | 67 | select | Engagement body line (the upsell stays dropped, decision 30) |
| Blue start and due dates (FT, un#, B2S, inventory) | 148, 34, 11, 14 | date | Episode body; meaning unconfirmed (audit question 1) |
| Tags beyond tiers (Clips published, Shorts published, TBD?, Paid, Audio, Video, Substack Pending, reupload yt, Deep Dive) | 137 FT, 499 inventory | multi-select | Tiers to Episodes.Tags (Tier 1, Tier 2, Tier 3 Spotlight, Sponsored); the rest to the body |
| List, completed, completed at, assignees, created at | all | status and dates | Episode body, one "Blue record" line |
| Themes (inventory) | 493 | multi-select, 90 options | The 9 sector values to Episodes.Sector where empty; the rest to the body |
| YouTube cleanup flag, Re-Publish checklist (inventory) | 418, 116 | checkbox, checklist | Episode body |
| FT and un# Production and QC checklists | 120, 47, 17 B2S | checklist | Not moved: duplicated by an automation, 0 ticked (audit). The one exception is the inventory Re-Publish checklist above |

Comments go in as Activities, not page body lines. They are dated facts with an author, and the house rule is that facts are logged once as Activities with their source. Kind Note, Source Migration, Date from the comment id's timestamp, linked to the Episode and the Engagement, Source ID `blue:<record id>:comment:<comment id>`.

Docs go in as Notion pages: one archive parent page, "Blue archive", with one child page per non-empty doc. The release and editing docs are also the input for the Templates work the audit flagged.

Form submissions go in as Guest forms rows, one per submission. Merge status is Merged and the Engagement relation is set, because the routine already merged these guests on 2 Oct. Each row keeps its photo and logo, which matches decision 69: the raw submission stays as a row. Blue's submission date goes in Merge note, because Submitted is a created-time property.

Archived workspaces: one archive page each under "Blue archive". Inner Journeys gets a table of 24 cards. Prompts gets 5 prompt texts. Vanshika Projects gets a list of 110 design cards. Vanshika gets 4 cards. Files on archived cards are not attached; the 15 Inner Journeys videos are in the manifest.

## Provenance on every write

- New rows: Source = Migration, Source ID = `blue:<record id>` (comments `blue:<record id>:comment:<id>`, docs `blue:doc:<doc id>`), Migration batch = `blue-legacy-2026-11-09`, Captured = write date.
- Existing rows: provenance fields are left as they are. The 2 Oct batch keeps its `Blue <id>` Source ID. Each filled value is listed on one line in the page body, "From Blue (blue-legacy-2026-11-09): filled X, Y".
- Conflicts: 94 rows in `data/blue_conflicts.csv`: People Role 32, Episodes YouTube 30, Episodes Spotify 13, People LinkedIn 12, People Email 4, Episodes Substack 3. The 30 YouTube and most Spotify ones are inventory cards whose episode was re-uploaded ("reupload yt" tag), so Notion holds the newer link. Nothing in the file is written.
- PR contacts. Of the 355 distinct PR and other-contact addresses on Blue cards, 354 already have a People row (exact match on Email or Other emails); the last one is a typo of an address that does. New People: 0. Stakeholder links to add: 9. No PR or EA person becomes an Engagement of their own (decision 424).
- Guests. 134 of 188 Blue guest addresses match no People row by email. The guest's People row is already linked on the Engagement with Email empty in 137 cases (the gap fill above), so these create no new rows; any left over after that fill go to the review CSV, not a new row. The 2 guests behind the unmatched Blue cards also exist in People by exact name; linking them waits for a yes on open question 3.

## Files

| Workspace | Images | PDF | Text (transcripts, docx) | Video (mp4) | Other | Total | Size |
|---|---|---|---|---|---|---|---|
| FT & Spotlight | 874 | 15 | 181 | 76 | 18 | 1,164 | 10.03 GB video; about 2.2 GB images [E] |
| un# | 299 | 11 | 64 | 62 | 18 | 454 | 8.96 GB video; about 0.5 GB images [E] |
| Episodes Inventory | 337 | 5 | 75 | 0 | 3 | 420 | about 0.1 GB [E] |
| Built to Share | 7 | 1 | 21 | 0 | 0 | 29 | 96 MB |
| Human by Design | 2 | 0 | 4 | 0 | 0 | 6 | 7 MB |
| Inner Journeys | 79 | 0 | 15 | 15 | 11 | 120 | 1.45 GB video |
| **Total** | **1,598** | **32** | **360** | **153** | **50** | **2,193** | **20.4 GB video; about 3 GB other [E]** |

Upload limit assumed: 20 MiB per file. That is the Notion MCP single-part upload; a URL import allows 50 MiB on paid plans but needs a public URL. A sample of 63 FT images had a mean of 2.5 MB, a median of 0.13 MB, and 3 over 20 MB. Expect about 50 to 60 files over the limit [E], mostly guest photos plus one 58 MB Built to Share logo. Each goes into a Drive folder per Episode, and the folder is linked from the Episode body.

What moves:
- Attached in Notion: photos and logos from form submissions go on the Guest forms rows (about 260 files). Thumbnails, quote cards, guest pics and PDFs go to Episodes.Assets (about 1,000 [E]). The 3 missing transcripts go to Episodes.Transcript file. The other 357 transcripts duplicate files already attached in October and are skipped.
- Drive: files over 20 MiB and the 13 audio files.
- Manifest only: 138 mp4 in the live workspaces (18.98 GB) plus 15 in Inner Journeys (1.45 GB). `data/blue_video_manifest.csv` has 153 rows: workspace, record id, record title, file id, filename, size in bytes. 41 rows have no record id: the file sits on a comment or a card attachment, or its name repeats.
- Duplicates: many files were uploaded twice under the same name and size. Phase B uploads each name and size pair once per card.

## New Notion properties

Six properties on four databases. Each is filled at once and read by people or routines:
1. Episodes: Assets (file). Thumbnails, quote cards and guest pics, all in one place for the editors.
2. Organisations: LinkedIn (url). 177 values, and the Guest forms table already asks for it.
3. Guest forms: Source (select: Form, Migration). Separates the 136 historical rows from live submissions.
4. Guest forms: Source ID (text).
5. Guest forms: Migration batch (text).
6. Activities: Migration batch (text). Activities has Source and Source ID but no batch.

Not proposed, because they would not earn their place: People.X, Episodes.Episode number, Episodes.Other links. Those values go in page bodies.

## Write order and size

One Notion writer, sequential, read-back after each step, counts reconciled against `data/blue_legacy/inventory.json`.

| Step | What | Notion calls (est.) |
|---|---|---|
| 0 | Akshay confirms the decision 28 and 344 override; Blue admin export of files, or a Mac download run | 0 |
| 1 | Add the 6 properties | 4 |
| 2 | Blue archive page, 12 to 17 doc pages, 4 archived-workspace pages (re-read 16 docs and 4 prompts from Blue first; see limits) | 25 |
| 3 | Rows for the 15 missing records once open question 3 is answered (most get a Source ID set on the name match; at most 2 new Episodes) | 20 |
| 4 | Episode property fills, about 720 Episodes | 720 |
| 5 | Episode body "From Blue" sections, about 720 | 720 |
| 6 | People gap fills (Email, Role, LinkedIn) on about 200 guests | 200 |
| 7 | Organisation LinkedIn and Website, about 180 | 180 |
| 8 | Engagements: 6 dossiers, 9 stakeholder links, 67 Google Ads body lines | 80 |
| 9 | Activities for 34 comments, batched | 3 |
| 10 | Guest forms rows, 136, batched 20 per call | 7 |
| 11 | File uploads: about 1,260 files, an upload call plus a POST each | 2,520 |
| 12 | Attach uploads to Guest forms rows and Episodes.Assets | 400 |
| 13 | Drive folders for about 70 oversized or audio files, linked from the Episode | 70 |
| | **Total** | **about 4,950** |

Time: at 10 to 15 seconds per sequential write, steps 1 to 10 (about 1,960 calls) take 6 to 8 hours of run time. Steps 11 to 13 (about 3,000 calls) take 9 to 12 hours, once the files are local. Blue cannot hand over binaries through the MCP. If an admin export with files exists, add a few hours to fetch and sort it. If not, a Mac run with Claude in Chrome downloading about 1,300 non-video files takes another 10 to 15 hours. Realistic total: two working days for data and Activities, plus two to three for files.

## Risks

- Blue keeps changing. FT gained 6 cards since the audit, and 2 Built to Share cards were created in October. Phase B re-exports first and diffs against this extract.
- Blue export rate limit: about one record export every 4 to 5 minutes, and archived workspaces refuse export.
- Name-only matches: 13 of the 15 missing cards match by name only. Writing to them without a key risks merging a repeat guest's two episodes (decision 108: Tushar's file was named after another company). They wait for a yes.
- File-to-card mapping uses file names from the export. Duplicate names (INTRO_VERTI.mp4 appears 9 times) and commas inside names make about 3% ambiguous [E]. Ambiguous files go to a review CSV, never guessed.
- Guest photos are personal data. They sit in the Guest forms table, which has no row-level security, so anyone with Notion access to that table sees them.
- Volume: about 4,950 writes is far above any recent batch. Run in steps with a drift check between them, and never in parallel with the inbox routine's writes to the same rows.

## Open questions for the CTO

1. Has Akshay reopened decision 28 (field data only, heavy files dropped) and decision 344 (Blue backfill retired)? Phase B is blocked without it.
2. Files: does the Blue plan allow an admin full export with attachments? The MCP account is MEMBER level and returns metadata only. If not, is a Mac download run acceptable, and who triggers it?
3. The 15 cards missing by key: may Phase B set the Blue Source ID on the 13 single name matches (Wysa, Sorin, GyanDhan, Prashant Sachan on Built to Share, 9 inventory cards)? And create Episodes for Saurabh Garg (Built to Share, Recorded) and Arpit Chhabra (inventory)?
4. Blue due date on 148 FT cards: release date or leftover? If it is the planned release, it fills Planned release instead of a body line.
5. Assets: one Episodes.Assets property, or a Drive folder link per Episode as the audit proposed? Notion attachments are searchable and visible to the team. Drive costs nothing per file.
6. The 94 conflicts: does Notion win everywhere (proposed), or should the 32 Role differences be reviewed? Blue holds the designation the guest typed on the form, which is often more exact.
7. Vanshika Projects: is a title list enough? Its cards hold no files or docs.
8. Is Inner Journeys still worth an archive page, given its guests are already People?

## Tool limits hit in Phase A

- Blue MCP cannot download file binaries. get-file and list-files return metadata only, and list-files does not say which card a file belongs to. Card mapping comes from file names in the record CSV export.
- The Blue record export (CSV) is rate limited (several "too often" refusals) and refuses archived workspaces. Archived cards were read with list-records and get-record.
- Blue comments have no timestamps in the API. Dates come from the comment id. 41 comments sit on deleted cards and cannot be read.
- Not saved locally, to be re-read in Phase B (20 small Blue reads): 16 of the 17 docs (only FT Editing Process was saved), 4 of the 5 prompt cards, and the 110 Vanshika Projects titles.
- Notion SQL returns at most 100 rows per call, and People has 8,447 rows, so people dedupe ran as targeted queries (all Blue addresses in one parameter) instead of a full snapshot.
- Notion upload: 20 MiB per file (single-part MCP upload); 50 MiB by public URL on paid plans.
