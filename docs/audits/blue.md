# Blue audit (ThePodium)

Audit date: 30 Sep 2026. Read-only: nothing was created, moved, edited, commented or re-configured. Method: Blue MCP (list/count/get tools, workspace activity feeds, per-record action history), plus read-only SQL against the Notion Episode Inventory (collection 6e563350) for the cross-check.

Legend: **[M]** = measured over all rows or all objects. **[E]** = estimated from a sample, a name-match heuristic, or inference. Timestamps come from Blue object IDs (cuid IDs embed their creation time), because the field-history tool is not authorised for the audit account.

Scope limits: the MCP account has MEMBER access (not admin). Full record reads were expensive (automations have stacked 80 to 140 duplicate checklist items on many records), so field fill rates rest on 11 full record reads plus 5 action-history timelines, not 50+. Treat all fill rates as [E] with n stated.

---

## 1. Summary

- **Blue holds 723 live records in 5 workspaces, plus 143 in 4 archived workspaces (866 total)** [M]. 500 of the 723 are the Episodes Inventory back-catalogue, which is dormant since Oct 2025 and fully covered by the Notion Episode Inventory. Only about 223 records reflect current production (FT & Spotlight 155, un# 48, Hissa/B2S 16, FastCode/HBD 4) [M].
- **Only FT & Spotlight uses Blue as a real pipeline.** 28 FT/SL episodes are in flight right now (Hold 3, Recorded 14, Slotted 6, Doc Ready 3, Video QC 2) [M]. un# has 1 in flight; B2S and HBD records are mostly created directly in "Published" as an after-the-fact register [M from activity feed].
- **The guest form is the one thing Blue does that nothing else does.** "Thank you for recording!" has received 129 submissions since Oct 2024 (about 5 a month, 12 in Sep 2026) [M]. Each submission creates the FT/SL record in "Recorded" and carries the hi-res guest photo, logos, designation, LinkedIn links and up to 4 PR contact emails. It must be replaced before switch-off.
- **Checklists are noise, not tracking.** A "list changed, create checklist" automation with no list filter re-adds the 33-item "Production and QC" checklist on every move, so FT records carry 99 to 143 items. Across 6 fully read FT records: 484 checklist items, 0 ticked [E, n=6]. The EI "Re-Publish Checklist" (4 items) is the only checklist that was actually used [M: 110 EI records marked done].
- **Content fields are dead; link fields are alive.** Episode Title, Show Notes, Thumbnail Copy and LinkedIn Release copy were empty on 6 of 6 FT records [E]. Final copy lives in the Google working doc. What Blue reliably holds is guest identity, the working doc link, dossier link, transcript file and platform URLs after release [E, n=11].
- **Asset FILE fields were used in early 2025 and abandoned by late 2025.** 138 mp4 files (about 19 GB [E]) were uploaded Jan to Oct 2025 and none since [M]. Thumbnail/reel/quote-card FILE fields were 0 of 6 on recent FT records [E]. Guest hi-res photos, logos and transcripts are still uploaded every week [M].
- **Blue vs Notion Episode Inventory:** the 500 Blue EI records are all in Notion (0 genuinely missing after checking 6 name-match misses by guest name) [M+E]. Blue-only: 10 published FT/SL episodes from 2026 (Drivn, Bluehill VC, ADA AI, Inventus, Vyome, TeamLease, Eggoz, SilverX Fund, The Guild, Sudama Devi Foundation), the Pant Project (live, still in Video QC), the 28 in-flight FT/SL records, and every un#, B2S and HBD record (68) [E].
- **Stage data lags reality.** The Pant Project sits in Video QC with live YouTube, Spotify, Apple and Substack links; an un# "Published" record has no YouTube link [E, spot checks]. Lists are moved late or not at all, so time-in-stage in Blue is a weak signal.

---

## 2. Workspace inventory

| Workspace | Records | Lists (records) [M] | Done [M] | Fields | Tags | Automations (active) | Forms | Docs | Files [M] | Last real activity |
|---|---|---|---|---|---|---|---|---|---|---|
| FT & Spotlight | 155 | Hold 3, Recorded 14, Slotted 6, Doc Ready 3, Video QC 2, Published 65, Shorts In Progress 10, Archived 52, Newsletter Pending 0 | 18 | 39 | 10 | 5 (4) | 1 (guest) | 7 | 1,143 | 28 Sep 2026 |
| Episodes Inventory | 500 | In Progress 167, Published 216, With Priya 7, Akshay Review 0, Publishing WIP 110 | 110 | 19 | 11 | 2 (2) | 0 | 2 | 420 | Oct/Nov 2025 |
| un# | 48 | Recorded 0, Slotted 0, Doc Ready 0, Video QC 1, Published 35, Medium in progress 12 | 5 | 37 | 5 | 7 (5) | 1 (internal) | 4 | 455 | 25 Sep 2026 |
| Hissa Podcast (B2S) | 16 | Recorded 1, Slotted 0, Doc Ready 0, Edting/ QC 0, Ready to Publish 0, Published 6, Newsletter Published 9 | 4 | 36 | 1 | 8 (6) | 0 | 1 | 24 | Sep 2026 |
| FastCode Podcast (HBD) | 4 | Recorded 0, Slotted 0, Doc Ready 1, Video QC 0, Published 3, NL 0 | 0 | 18 | 0 | 0 | 0 | 1 | 6 | Sep 2026 |
| **Active total** | **723** | | **137** | | | **22 (17)** | **2** | **15** | **2,048** | |
| Archived workspaces | 143 | Vanshika Projects 110, Inner Journeys 24, Prompts 5, Vanshika 4 | | | | | | | not listed | |

Other objects [M]: 0 dashboards, 0 reports, 0 webhooks, 0 Blue-archived records (the "Archived" list is used instead). 140 of 155 FT records have a due date [M]; meaning not verified (see open questions).

Tag usage [M]:
- FT & Spotlight: FT 101, SL (Spotlight) 24, Clips published 13, Shorts published 11, FT Tier 2 10, TBD? 3, Paid 1; Schedule, Duplicate, ON HOLD FROM GUEST unused in current records. Records in Recorded carry no show tag yet (14 of 14); the FT/SL tag is added later. Spotlight is a tag, not a workspace.
- Episodes Inventory: FT 396, Audio 276, Substack Pending 185, Video 148, Tier 2 133, Spotlight 103, reupload yt 77, Tier 1 70, Deep Dive 9, bug 4.
- un#: Dossiered, Tier 2, "to be recorded", "Zencastr & Calendar Invite Shared", un# (a handful each). Hissa: one tag. FastCode: none.

Activity volume [M] (workspace feeds): FT 344 events Oct 2024 to Sep 2026 (129 form submissions, 37 creates, 37 deletes, 23 comments); EI 662 (407 of them the Dec 2024 bulk load, near-silent since Nov 2025); un# 221 (50 comments, low in 2026); Hissa 50 since Nov 2025; FastCode 36 since Jan 2026.

---

## 3. Lifecycle and stages

**Canonical lifecycle encoded by the lists** (FT, un#, B2S and HBD all use the same spine) [M]:

`Recorded -> Slotted -> Doc Ready -> Editing / Video QC -> (Ready to Publish) -> Published -> post-publish tail -> Archived`

| Stage | Meaning (from process docs and automations) | Trigger in Blue |
|---|---|---|
| Hold | Recorded but parked (guest asked to hold, or not releasing) | manual |
| Recorded | Guest form received; record exists with guest identity and assets | form submission (FT); manual elsewhere |
| Slotted | Release slot assigned | email automation (FT, un#), checklist (un#) |
| Doc Ready | Transcript in, working doc and editing doc done | email automation (FT, un#) |
| Video QC / Edting/ QC | Edited cut uploaded unlisted, QC by Sarika/Akshay, sent to guest | FT creates "Assets for release" checklist |
| Ready to Publish | only in B2S; unused | none |
| Published | Live on YouTube + Zencastr feed (Spotify/Apple/Amazon), Substack post, LI post | un# creates post-publish checklist |
| Shorts In Progress (FT), Medium in progress (un#), Newsletter Published / NL (B2S, HBD) | post-publish tail: clips, shorts, deep dive, Medium/Substack newsletter | manual |
| Archived (FT) | all promotion done ("Move to Archived" is the last step of the Spotlight release doc) | manual |

The Episodes Inventory runs a different, back-catalogue rework loop: `In Progress -> With Priya -> Akshay Review (emails Akshay) -> Publishing WIP (ticked = done) / Published`. Its goal was to refresh YouTube title/thumbnail/description, publish a Substack SEO article and a LinkedIn deep dive for old episodes. Notion's Episode Inventory "Queue status" now covers the same job.

Lists that existed and were deleted [M, activity feed]: un# "Proposed", "To Be Scheduled", "In progress" (a pre-recording pipeline once lived in Blue); Hissa "Scheduled". Pre-recording booking is no longer in Blue anywhere.

**Time in stage** [E, 5 timelines, decoded from action IDs]:

| Record | Timeline | Elapsed |
|---|---|---|
| HBD, Simon Jagers | transcript 27 Mar; Doc Ready 30 Mar; Video QC 3 Apr; Published 15 Apr 2026 | 19 days transcript to live (3 / 4 / 12 days per stage) |
| B2S, Visham Sikand | transcript 21 Apr; Published and newsletter 29 Apr 2026 | 8 days |
| FT, The Pant Project | recorded 21 May; form (photo) 26 Jun; first stage move 8 Jul; transcript 18 Sep; YouTube link 28 Sep 2026 | about 4 months record to live; still shown as Video QC |
| FT, Netcore Cloud | form 2 Apr; stage moves 4 May, 5 Jun, 22 Jun 2026 | about 2.5 to 3 months form to live |
| EI rework, Lead School | With Priya 23 Aug; working doc and Akshay Review 23 Sep; back and forth 24/25 Sep; Publishing WIP 1 Oct; done 5 Oct 2025 | 6 weeks, of which review loop 1 week |

Read: FT/SL has a long, variable queue between Recorded and Doc Ready (slotting backlog), then 2 to 3 weeks from doc to live. Smaller shows move in 1 to 3 weeks. Blue does not show where FT episodes wait because nobody moves the cards on time.

---

## 4. Fields (used vs dead)

Sample: 6 FT (Recorded 1, Video QC 1, Published 3, Archived 1), 2 EI, 2 un#, 1 B2S full reads [E]; plus FastCode action history.

**FT & Spotlight (39 fields)**

| Field group | Fill | Verdict |
|---|---|---|
| Guest Name, Guest Organisation Name, Guest Email, Formal Designation (form, required) | 6/6 | Used |
| PR/Comms email 1 / 2 / 3 / 4 | 6/6, 5/6, 2/6, 2/6 | 1-2 used; 3-4 rare |
| Hi Res Image, Org LinkedIn, Guest LinkedIn (form, required) | 5/6 each (pre-form 2024 record lacks them) | Used |
| Upload the Logo(s) (form, optional, added Aug 2025) | 4/4 post-Aug-2025 | Used |
| Date of recording | 4/6 | Used, patchy |
| Google Ads spend select (INR 5k / 10k / No thanks) | 2/6 (one "INR 10k") | Rare; commercial signal |
| Link to working doc, Dossier, Training Data (transcript .txt) | 4/5, 3/5, 4/5 of post-2025 records | Used |
| YouTube, Spotify, Apple, Amazon, podm.in short link, Substack page, LI Announcement | 4/4 live records | Used (post-publish) |
| LinkedIn Newsletter | 3/4 live | Used |
| Episode Title, Show Notes, Thumbnail Copy, LinkedIn Release post copy | 0/6 | Dead (copy lives in the working doc) |
| Unlisted Video, Uncut version | 0/6 | Dead |
| FILE: YT / Spotify / Substack / Episode Out Now / Deep Dive thumbnails, Intro Reel, Quote Cards, Audio File | 0/6 | Dead since late 2025 (used in early 2025, see files) |

**Episodes Inventory (19 fields):** Guest Name, Org Name, Guest LinkedIn, Org Website, YouTube/Spotify/Amazon/Apple links, YouTube Cleanup checkbox, Themes (multi-select with 90 options) filled 2/2; Substack Link 1/2; Transcript and Working Doc filled only on records that went through rework; Shorts, Quote Cards, 3 thumbnail FILE fields, LI Newsletter 0/2 [E].

**un# (37 fields):** 2025 record (Punit @ KoinX) had almost everything filled, including thumbnail files, reel mp4, Opus project, creators.spotify link, Pocket Casts, episode number, carousel PDF. 2026 record (Nikhil @ Circle) has only guest identity, guest pic, working doc, dossier, source transcripts, Sri's LI announcement; every platform link is empty although the list says Published [E, n=2]. Gemini Chat / Claude Project / ChatGPT link fields (added Nov 2025) and Link to Guest Assets: 0/2. Pattern: platform links moved out of Blue during 2025.

**Hissa/B2S (36 fields, cloned from un#):** identity, working doc, dossier (a Claude chat link), transcript, YouTube, Spotify, Apple, short link, newsletter link filled; thumbnails, guest pic, episode title, thumbnail copy, Satish's LI/X announcement empty [E, n=1]. One field is literally named "http://www.cashify.in" (used as Company Website).

**FastCode/HBD (18 fields):** "Dossier" exists twice. Action history shows identity, dossier, working doc, transcript, short link (fscd.ai) being set [M for one record].

**Cross-workspace dead or duplicate fields [E]:** all FILE thumbnail/reel/quote-card fields, all copy fields, Unlisted/Uncut links, Audio File, Gemini/Claude/ChatGPT links, Pocket Casts, creators.spotify, Opus project, duplicate Dossier, misnamed website field.

---

## 5. Checklists, forms, automations, files

**Checklists** [E unless marked]
- FT: template "Production and QC" (33 items: draft cuts, working doc, clips/shorts ideation, VO script, main edits, intro horizontal/vertical, thumbnails, reviews, LI posts, deep dive, uploads to YT/Spotify/Insta, corrections) plus "Assets for release" (11 items: final on YT and Zencastr, 3 thumbnails, intro reels, 3 reels, quote cards, episode-out-now, deep dive thumbnail). 6 records: 484 items, 0 ticked; 3 to 4 copies of the same checklist per record.
- un#: "Production And QC" (2 items), "Ranjita Post Publishing" (3 items: post on X, repost LI, email guest). 5 items, 0 ticked (n=1).
- B2S: "Production and QC" (36) + "Pre-Release" (15) three times over; 81 items, 0 ticked (n=1). Pre-Release items still reference "Sri" and "aarna" (copied from un#).
- EI: "Re-Publish Checklist" (4 items: YT thumbnail+description+title, LI deep-dive newsletter, Substack thumbnail+SEO article, Zencastr thumbnail+show notes). Actually ticked; 110 EI records done [M].
- Conclusion: people use lists, links and Slack/WhatsApp, not checklists. The 30+ item checklist is a good inventory of deliverables but a bad task list.

**Forms**
- "Thank you for recording!" (FT & Spotlight, active) [M]. Lands in list "Recorded"; record body says "created using the following form". 13 fields: Guest Name*, Organisation Brand Name*, Guest Email*, Designation*, Organisation LinkedIn*, Guest LinkedIn*, Hi-res image(s)* ("full torso visible"), Logo(s), Date of recording, PR/Comms emails 1 to 4 ("people who should be updated about the release status"). (* required.) 129 submissions Oct 2024 to Sep 2026, monthly range 1 to 12 [M]. Used for both FT and Spotlight guests; un#, B2S and HBD have no guest form, their records are keyed in by staff.
- "Internal" (un#, active): 2 fields (guest name, title), no target list, 0 submissions in the feed [M]. Dead.

**Automations** [M]: 22 total, 17 active, 0 in FastCode. Only three action types: CREATE_CHECKLIST, SEND_EMAIL, ADD_ASSIGNEE (the assignee ones are disabled).
- FT: any list change -> create checklist (the duplicate-checklist bug, created Dec 2025); Slotted -> email; Doc Ready -> email; Video QC -> "Assets for release" checklist.
- EI: With Priya -> Re-Publish checklist; Akshay Review -> email to Akshay.
- un#: Slotted -> email + checklists (three overlapping rules); Doc Ready -> email + checklist; Published -> checklist.
- Hissa: record created -> checklist; list changes -> emails to internal staff and checklists; list triggers show blank because they were cloned from un#. Emails fire on moves even when records are created after release [M, Visham record].
- No automation emails guests; guest release mails are manual (per the release docs).

**Documents** [M]: FT Release Process 2024, Spotlight Release Process 2024, FT Editing Process (with full-episode and clips QC checklist), Working Doc Template (sections: title, show notes, epi-out-now teaser, Akshay's LI post; embedded quote cards, editing doc with thumbnail copy, cuts, intro sound bytes, explainer text, clips, reels; guest promo copies; SEO post; deep dive), Competitors 2024, FT 10K ad (not read); EI Rework Old Episodes; un# Scope of work (deliverables per team and asset list), AU Editing, Dossier Process; plus 5 workspace Home pages (not read). These are the best source for Templates.

**Files** [M counts by extension, sizes E]
- FT & Spotlight 1,143: 172 txt (165 named transcript), about 860 images (jpg/jpeg/png: guest hi-res photos, company logos, 77 logo-named, a few thumbnails), 76 mp4 (intro horizontal/vertical, reels, full-episode R1/R2 cuts; 25 to 360 MB each, about 10 GB [E]; uploaded 16 Jan to 28 Oct 2025), 14 pdf.
- Episodes Inventory 420: 75 transcripts, 335 png (rework thumbnails), 5 pdf, 0 video.
- un# 455: 64 transcripts, 283 images, 62 mp4 (about 9 GB [E]; Jan to Jun 2025), 11 pdf (dossiers, carousels).
- Hissa 24 (mostly transcripts, 3 guest photos, one 58 MB logo); FastCode 6.
- Guest hi-res photos can be large (several 15 to 36 MB originals). Some uploads are duplicated (same file twice).

---

## 6. Migration mapping (Blue -> target design)

| Blue object | Target | How |
|---|---|---|
| FT & Spotlight records (155), un# (48), Hissa (16), FastCode (4) | **Episodes** (one row each) | Title "Guest @ Company"; Show from workspace plus FT/SL tag; Stage from list (map Hold, Recorded, Slotted, Doc Ready, Video QC, Published, post-publish tail, Archived to a single Status); Recording date; Tier from "FT Tier 2"/"Tier 1/2" tags. Match existing Notion rows first (Episode Inventory already has 582 FT/SL rows); create new rows for the 10 Blue-only 2026 FT/SL releases, 28 in-flight FT/SL, and all 68 un#/B2S/HBD. |
| Episodes Inventory records (500) | **Episodes** (already present) | Do not import rows. Optionally backfill Themes and Tier tags onto matching Notion rows; the rework status is superseded by Notion "Queue status". |
| Platform URLs: YouTube, Spotify, Apple, Amazon, Pocket Casts, short link (podm.in, unhashed.co, built2share.in, fscd.ai), Substack/newsletter, LI newsletter, LI/X announcement | **Episodes** link fields | Keep as a small fixed set: YouTube, Spotify, Apple, Substack/Newsletter, Short link, Host LI post. Put rarer ones (Amazon, Pocket Casts, X post, Opus, creators.spotify) in one "Other links" field or drop. |
| Working doc link, Dossier link | **Episodes** | During migration keep as links; going forward the Episode page body is the working doc and the dossier becomes a child page or file. |
| Episode Title, Show Notes, Thumbnail Copy, LI Release copy | **Episodes** "Final" fields | Blue has nothing to migrate (0/6). Fill from the Google working docs, not from Blue. |
| Transcript .txt (Training Data / Source data / Transcript fields) | Drive, linked from **Episodes** | Copy files; store Drive link (or Notion file) on the Episode. |
| Guest hi-res photo, logos, thumbnails, reels, quote cards (FILE fields) | Drive folder per episode, linked as asset fields on **Episodes** | Copy files; one "Assets folder" link per episode is enough. |
| Guest Name, Designation/Title, Guest LinkedIn, Guest X, Guest Email, Guest Pic | **People** (guest) | Dedupe against Members Master List; link to Episode. |
| Organisation name, Org LinkedIn, Org website, Org X, logo | **People** company fields (or a later Organisations table) | Target design has no Organisations table; keep company text + LinkedIn + website on the guest and the Engagement. |
| PR/Comms emails 1 to 4, "Other Email IDs" | **People** (role: PR contact) linked to the guest's **Engagement** | They are the release-notification list. Keep in Notion only, never in git. |
| Google Ads spend choice, "Paid" tag, "ON HOLD FROM GUEST" tag, Hold list | **Engagements** | Commercial and guest-relationship state belongs to the engagement, not the episode. |
| Form submissions, comments (23 FT, 50 un#), automation emails | **Activities** | Do not import history; new system logs form submissions and release emails as Activities. |
| "Production and QC" and "Assets for release" checklists | **Tasks** (a handful per episode, auto-created) + **Templates** | Collapse 33+11 items into about 6 tasks: Working doc and titles; Edit and QC main episode; Thumbnails and graphics; Clips and shorts; Publish and distribute; Promote (host post, guest mail, newsletter/deep dive). Keep the full item list as a reference checklist inside the Template, not as tasks. Do not migrate existing checklist items (0% ticked). |
| Process docs (FT/Spotlight release, FT editing + QC checklist, Working Doc Template, AU editing, AU scope of work, dossier process, rework old episodes) | **Templates** | Rewrite into the Episode page template and per-show release templates. |
| Workspaces (FT & Spotlight, un#, Hissa, FastCode) and host-specific fields (Sri's / Satish's announcements) | **Shows** | One Show row each (FT, Spotlight, un#, B2S, HBD) holding host, short-link domain, feed and channel URLs. |

**Drop:** duplicate checklists and the any-list-change checklist rule; all dead fields listed in section 4; "Newsletter Pending", "Ready to Publish", "Akshay Review" (empty) lists; un# "Internal" form; tags Schedule, Duplicate, TBD?, bug; the Episodes Inventory workspace after a final export; the 4 archived workspaces after a one-time export.

---

## 7. Switch-off prerequisites

1. **Guest post-recording form replaced and live.** Same fields (identity, designation, LinkedIn x2, hi-res photo upload, logo upload, PR contacts, recording date), creating or updating the Episode + People + Engagement in Notion and dropping files into the episode's Drive folder. Update every place the Blue form link is sent (guest thank-you emails and templates). Extend it to un#, B2S and HBD, which today have no form.
2. **In-flight episodes moved.** 28 FT/SL (Hold 3, Recorded 14, Slotted 6, Doc Ready 3, Video QC 2), 10 FT Shorts In Progress, 1 un# Video QC, 12 un# Medium in progress, 1 B2S Recorded, 1 HBD Doc Ready [M], with their working doc, dossier and transcript links.
3. **Files copied to Drive and linked.** Priority: guest hi-res photos and logos for in-flight and 2026 episodes, and all transcripts (about 335 .txt [M]). Then the 138 mp4 files (about 19 GB [E]) if the edited cuts are not already on Drive or Zencastr. Blue offers no binary download through the MCP, so this needs a Blue export or manual download by an admin.
4. **Blue-only episodes recorded in Notion.** The 10 published FT/SL 2026 episodes, the Pant Project, and all 68 un#/B2S/HBD episodes with their platform links.
5. **Notification emails replaced.** Slotted and Doc Ready (FT, un#), Akshay Review (EI), Hissa list-change emails: decide which survive as Notion automations or Slack messages.
6. **Templates written** from the process docs (section 5) so the release steps are not lost.
7. **Admin export and check.** An admin account should confirm there are no workspaces hidden from the audit account, and take a full export (records, comments, files) of all 9 workspaces, including the 143 records in archived workspaces, before the subscription ends.
8. **One-week parallel run** (per architecture plan) with at least one form submission and one release going end to end in Notion.

---

## 8. Open questions

1. What does the due date on 140 of 155 FT records mean: planned release date, slot date, or leftover? If it is the release date it should become the Episode "Release date".
2. Is the Google Ads upsell (INR 5k / 10k question on the guest form) still offered? If yes it is an Engagement or revenue field; if not, drop it from the new form.
3. What do "FT Tier 2" (FT), "Tier 1/2" (EI) and "Paid" mean operationally: guest priority, promotion budget, or paid placement?
4. Do shorts/clips need their own tracking (FT "Shorts In Progress", "Clips published"/"Shorts published" tags), or is one Promote task per episode enough?
5. un# "Medium in progress" (12): is Medium still a channel? B2S/HBD "Newsletter Published": is the newsletter a separate milestone worth a status?
6. Where do edited video masters live today (Drive, Zencastr, editor's machine)? This decides whether the 138 Blue mp4s must be kept.
7. Should B2S and HBD production be tracked from Recorded in Notion, given Blue is only used after release for them today?
8. Contents of the archived workspaces (Vanshika Projects 110 records, Inner Journeys 24): keep, export only, or discard?
9. PR contact emails from the form: should they live on People (role PR) or only on the Engagement, and who is allowed to see them?
