# Notion workspace audit (ThePodium)

Audit date: 30 Sep 2026. Read-only. Method: Notion MCP schema fetches, SQL counts over every row (so row counts and fill rates are over all rows, not samples, unless marked), cross-table SQL joins on normalised names and URLs, and spot reads of individual pages.

Legend: **[M]** = measured by query over all rows. **[E]** = estimated (sample, name-match heuristics, or inference). "Last active" = most recent row edit, taken from Notion search sorted by last edited.

Excluded on purpose: "ThePodium context brief for Claude", "Business OS" and its audit children, "CRM Build Plan" (earlier drafts). No credentials or password database was found in Notion; the only hits for those words were draft pages and one B2S row about a company named 1Password.

---

## 1. Summary

- **Notion holds about 20 databases, created almost entirely between 22 Aug and 30 Sep 2026.** Most are one-shot imports or agent run logs, not a system. Only two real relations exist (Members to Episode Inventory), and they are filled on 25 rows out of 682 and 582 [M], even though 514 episodes can be matched by YouTube URL [M].
- **People are spread across at least 7 tables with no shared key.** Members Master List (682), B2S live list (90) and archive (492), HBD Guest Outreach (113), US VC contacts (up to 3 per firm across 774 firms, about 2,000 named people), PaaS Leads (14), Vendor Pitches (3). Estimated distinct humans: about 3,300 [E]. Measured cross-table overlap is small (a few dozen), except that Whatsapp Group Members is a near-complete copy of the Members subset flagged "In WhatsApp Group" (479 of 505 exact name matches) [M].
- **No table has a guest blurb, a research history, or a location field for guests.** "What they do" averages 24 characters (max 83) [M], so it is a tag, not a blurb. Country exists only on B2S lists; City/State on US VC is the firm HQ. The closest thing to a written blurb is the "Fact sheet" section at the top of Article Queue page bodies.
- **Episodes exist only for Founder Thesis (460) and Spotlight (122)** [M]. There is no episode or guest table for un#, and no episode table for B2S or HBD. un# is absent from Notion.
- **The episode "working doc" pattern already exists, but in the wrong table.** Article Queue page bodies hold fact sheet, title options, subtitle, full article, tags, thumbnail prompt and infographic notes. Episode Inventory page bodies hold only the transcript file. 418 of 439 Article Queue rows match an Episode Inventory row by YouTube URL [M]; the two are parallel records for the same episodes.
- **Evals, pitch notes and dossiers live outside Notion.** Every guest eval link (42 of 61 triage rows) and every PaaS pitch note and chat link (14 of 14) points to claude.ai; PaaS guest notes (4) point to Google Docs [M]. There is no Eval or Dossier field anywhere else.
- **Most pipelines are unworked.** US VC: 774 of 774 "Not sent" [M]. B2S live: 82 of 90 "Not started" [M]. HBD: 99 of 113 have no status [M]. Episode Inventory "Queue status": 576 of 582 "Not started" [M]. Article Queue "Pipeline": 429 of 439 blank [M].
- **Privacy exposure is real.** Members holds phone numbers on 599 rows, and one "Source Note" holds a phone number [M]; a page marked "DELETE" still contains phone data in its body; the 28 Sep inbox triage snapshot stores 23 personal/family emails [M]; the WhatsApp members table sits under a page described as public-facing.

---

## 2. Inventory

| Database | Rows | Covers | Holds | Last active | Verdict |
|---|---|---|---|---|---|
| Members Master List | 682 [M] | FT (guests + WhatsApp community) | People | 27 Sep | Keep as People seed |
| Episode Inventory | 582 [M] | FT 460, Spotlight 122 | Episodes | 30 Sep | Keep as Episodes base |
| Article Queue | 439 [M] | FT, Spotlight | Content (working docs) | 30 Sep | Merge into Episodes (page body) |
| Substack Posts Audit | 424 [M] | FT Substack | Content analytics snapshot | 24 Aug | Retire (fold a few fields into Episodes) |
| Whatsapp Group Members | 505 [M] | FT community | People (duplicate) | 27 Sep | Retire (becomes a People view) |
| Built-2-Share guest list | 90 [M] | B2S | Pipeline (guest invites) | 28 Sep | Merge into Engagements |
| Built-2-Share guest list (archive) | 492 [M] | B2S | Pipeline (guest invites) | 23 Sep | Merge into Engagements |
| HBD Guest Outreach | 113 [M] | HBD | Pipeline (guest invites) | 23 Sep | Merge into Engagements |
| US VC Podcast Outreach | 774 [M] | Agency BD (PaaS) | Orgs + people + pipeline | 16 Sep | Split: Organisations, People, Engagements |
| Podcast-as-a-Service Leads | 14 [M] | Agency BD | Pipeline (clients) | 25 Sep | Merge into Engagements |
| Vendor Pitches | 3 [M] | FT | Inbound vendor intake (form) | 26 Sep | Keep form, route rows to Engagements |
| Newsjack Log | 130 [M] | FT Substack | Agent log | 30 Sep | Keep (agent log) |
| FT Newsjack Scout: Daily Scan Log | 3 [M] | FT | Agent log (one day) | 7 Sep | Retire (superseded by Newsjack Log) |
| Publishing Plan | 5 [M] | FT Substack | Agent decision log | 30 Sep | Merge into Queue / Activities |
| Inbox triage: unread primary (10 Sep) | 61 [M] | All shows | Email snapshot | 10 Sep | Retire (design input only) |
| Primary inbox triage: latest 100 (28 Sep) | 100 [M] | All + personal | Email snapshot | 28 Sep | Retire (privacy) |
| Meetings | 12 [M] | FT recordings, precalls, sales calls | Activities (AI meeting notes) | 30 Sep | Keep as Activities source |
| Projects / Tasks / Docs / My Tasks | 3 / 3 / few / few [M] | none | Notion starter template | 22 Aug | Retire |
| Page: "DELETE - Founder Thesis Master People List" | 16 child pages | FT | Old people page | 23 Sep | Retire (contains phone data) |

---

## 3. Per-database detail

Fill rates are over all rows [M] unless noted.

### 3.1 Members Master List (collection 3d719a30...9aff)
- Displayed as "Members Master List"; the parent database is titled "Notion_Master_List (2).csv", so it is a CSV import. Rows created 10 to 27 Sep. One view (Table, unfiltered). Inline database with no visible parent (private section).
- Properties: Name (title, 100%), Company (text, 681/682), Role (text, 258, of which 242 = "Founder"), What they do (text, 682; avg 24 chars), LinkedIn (url, 631 = 93%; 623 are /in/ profile URLs), Phone (text, 599 = 88%), Source Note (text, 503; raw WhatsApp scan text, one contains a phone number), In WhatsApp Group (checkbox, 505), Episode Published (checkbox, 511), Episode Title (514), Episode Link (url, 514), Transcript Link (url, 513; points to an external transcript host), Episodes (relation to Episode Inventory, **25**), rollups Article / YouTube / Zencastr (via the 25-row relation, so mostly empty).
- No Email, no Location, no Blurb, no research fields. Page bodies are blank on the rows opened.
- Dupes: 680 distinct names in 682 rows; 3 LinkedIn URLs appear twice (same person, two spellings) [M].
- Covers: FT guests (511 with a published episode) plus non-guest community members (about 170 [E]).

### 3.2 Episode Inventory (6e563350...1ff)
- 582 rows, all created 22 to 23 Aug (bulk build), still being edited (30 Sep). Views: Default, "Clips to delete".
- Show (select): Founder Thesis 460, Spotlight 122 [M]. No other shows.
- Fill: Guest 580, Company 581, YouTube URL 582, Spotify URL 533, Apple URL 293, Substack URL 433, Views 428, Theme 487, Article state 582 (Full 218, Short 215, None 149), Article words 582, Queue status 582 (Not started 576, Done 6), Transcript words 87, **Published date 1**, **Priority 0** (its description says Ranjita works highest first, but the numbers live in Article Queue), Zencastr transcript 0, Guest profile relation 25.
- Theme values used: Fintech 127, SaaS 72, D2C 65, Marketplace 59, Deeptech 56, Edtech 33, Healthtech 25, Services 20, Gaming 8, plus 20 multi-tag rows; 2 blank.
- Page body: transcript .txt attachment only (seen on sampled pages).
- Guests with 2 to 3 episodes: 29 names (legitimate repeat guests, not dupes). No duplicate YouTube URLs [M].

### 3.3 Article Queue (42a58339...de)
- 439 rows created 24 Aug. Views: Default, "idmap-temp", "Ready to draft", "TEMP guest empty" (two temp views left behind).
- Action: Expand stub 266, Write new 173. Pipeline: blank 429, Drafted 8, Published 2 [M]. Priority 193, Substack URL 271, Current words 268, Suggested internal links 242, Agent notes 8, Owner 0, Thumbnail 0, Published on 2, Scheduled for 0.
- **Page body is the content working doc** on drafted rows: Fact sheet (guest bio facts), Facts to verify, Title options, Subtitle, full Article, Sources, Tags, Thumbnail hook lines and image prompt, Infographics. Agent notes record what a human must still do.
- 418 of 439 match Episode Inventory by YouTube URL; 0 duplicate YouTube URLs [M].

### 3.4 Substack Posts Audit (126a7576...55)
- 424 rows, all created and last edited 24 Aug. Default views only (not inspected in detail).
- Per-post metrics: Views, Likes, Restacks, Open rate % (297), Words, Headings, Tags, Internal links (only 1 post has any), YT link (7), Spotify link, Subtitle, Money stat early, State (Stub 170, Medium 42, Full 212), Episode matched (367; 57 orphans).
- A frozen analysis snapshot. Its companion pages (Substack Audit Report, Article Writing Spec, Tags + AEO Strategy, FT Channel Rules, Subtitle drafts) are playbooks and belong under Templates/Docs.

### 3.5 Whatsapp Group Members (3d519a30...834)
- 505 rows, Name / Company (100%) / What they do (486). One view. Parent page: "Welcome to the Founder Thesis Community" (described in the DELETE page as the public-facing version).
- 479 of 505 names exactly match Members rows, and all 479 have In WhatsApp Group ticked; Members has exactly 505 ticked [M]. The remaining 26 are almost certainly spelling variants [E]. Pure duplicate.

### 3.6 Built-2-Share guest list (live, 40650bc2...bf) and archive (69e79920...338)
- Same schema: Founder @ Company (title, "Name @ Company"; LinkedIn is a hyperlink on the title text, not a field), Email, Category, Connect (AD / Satish / Cold), Country, Status, Next Follow-up, Satish Approved, AD Comment, Rank (formula).
- Live: 90 rows, created 15 to 26 Sep; 6 views (Default, Master list, Declined and unresponsive, Follow-up due, AD and Satish connects, By category board). Email 68, AD Comment 46 (e.g. "Proposed 26 Sep, pending Satish approval"), Satish Approved 45, Next Follow-up 1. Status: Not started 82, Unresponsive 4, Maybe later 2, Emailed/Started 1, Do not contact 1. Connect: Cold 74, AD 12, Satish 4. Country: India 79.
- Archive: 492 rows, all created 15 Sep in one import; last edit 23 Sep. Email 489, Next Follow-up 141, AD Comment 0. Status: Not started 358, Emailed/Started 90, Unresponsive 22, Declined 9, Do not contact 6, Maybe later 4, Chasing 3. Category: More of the Same 248, Outliers 139, IPO/Pre-IPO 37, Big Indian 28, Big Global 21, Recently IPOd 14. Country India 144, US 123, rest spread.
- **The archive holds most of the real B2S outreach history** (90 emailed, 40 closed out). Rows are merged by hand between the two ("Merged from duplicate 'Asrotalk' row (archived)").
- Title links: on the archive sample the link is a LinkedIn people-search URL, not a profile; on a live sample it is a real profile URL. Not queryable in SQL, so LinkedIn fill here is unknown.
- Overlap: 4 names in both B2S tables; 12 live and 22 archive names are in Members; **13 live B2S targets already have an FT episode** [M].

### 3.7 HBD Guest Outreach (b5711d4f...8f)
- 113 rows all created within 30 seconds on 23 Sep (import). One view. Name, Company (110), Email (112), Note (8), Next follow-up (61, dated 23 to 30 Sep), Status.
- Status: blank 99, Approved 6, Unresponsive 4, Maybe later 3, Chasing 1. **"Approved" is ambiguous**: notes read "Marked approved, Arjun declined" on several rows, so the field mixes host approval with guest response.
- Mostly academic AI researchers. 1 name overlaps Members [M].

### 3.8 US VC Podcast Outreach (df32dba9...8e)
- 774 firms created in 20 minutes on 13 Sep, enriched by 17 Sep (Enrichment Status Done 773, Skip 1). One view.
- Firm fields: Firm, Website, LinkedIn (753), City (772), State (773), Founded, Team Size, Portfolio Count, Investment Score, Sectors, Stages, Unicorns, IPOs, Recent Deals, Tracxn (774), Overview (774), Sources.
- Fit fields: Priority A 381 / B 300 / C 92, Budget Read High 652 / Medium 120 / Low 2, Has Podcast No 596 / Yes 115 / Dormant 63, Fit Rank (688), Fit Note (774), Budget Rationale, Pitch Line (773), Partners On Other Podcasts (326).
- People packed into columns: Contact 1 (774; email 594, LinkedIn 731), Contact 2 (662), Contact 3 (566), Other Contacts free text "name | title | email" (431 rows), Generic Email (507).
- Outreach Status: Not sent 774 [M]. Nothing sent yet.

### 3.9 Podcast-as-a-Service Leads (15bd76c9...17)
- 14 rows, created 14 to 22 Sep. One view. Company (title), Founder (14), Status, Hot or not, Owner (Akshay 7, blank 7), Next Action (14), Next Action AD (0), Last call (5), Last call details (7), Next follow-up (5), Follow-ups sent (4), Last checked (5, set by a daily agent run), Pitch note (14, claude.ai), Chat Link (14, claude.ai), Guest note (4, Google Docs), short link (14).
- Status used: Send Pitch 4, In discussion 3, Proposal sent 2, Lost 1, Renew 1, Later 1, blank 2. The option list mixes stages (Pitched, Proposal sent) with actions (Send Pitch, Renew) and parking (Later, Dormant). Hot or not: hot 6, warm 3, Lukewarm 2, cold 1 (inconsistent casing).
- Rows have child pages (Pitch note, Pitch note (priced), Guest note (options draft)) as well as external links, so the pitch doc lives in two places.

### 3.10 Vendor Pitches (d4ca5f98...3d)
- 3 rows (20 to 26 Sep). Has a public form view "Pitch to Us" plus "All pitches". Status unset on all 3. Stores contact name, email, phone/WhatsApp.

### 3.11 Newsjack Log (64415dd5...b1) and FT Newsjack Scout (dcafabd4...f2)
- Newsjack Log: 130 rows, detected 11 to 30 Sep across 8 run days; written by a daily agent. Status: Skipped weak hook 75, Skipped duplicate story 52, Skipped not chosen 2, Drafted 1. Guest 74, Score 67, Agent notes 130, Rank 0, YouTube 12, Substack 9. Option lists have drift: "Fraud" vs "Fraud / controversy", "IPO" vs "IPO / listing", "Layoffs / Shutdown" vs "Shutdown / layoffs", "<24h" vs "<24 hours". Freshness blank on 53.
- Scout: 3 rows, one day (7 Sep), all Not started. Superseded.

### 3.12 Publishing Plan (c76d2bb3...17)
- 5 rows, 14 to 30 Sep, one per agent morning run: Decision, Type (Newsjack / Inventory expand stub), Score, Runner-up, Rationale, weekly counters. All Status = Drafted. This is a decision log that should surface to Akshay.

### 3.13 Inbox triage snapshots
- 10 Sep (81f92b58...9f): 61 rows, one run. Tag: Follow-up/chaser 19, Scheduling 15, Guest eval 11, Sponsorship 10, others 6. Owner: Akshay 26, Waiting on them 20, Mamatha 13, Both 2. Status: Not started 61. Fields People, Context, Recommended response, Next action all 100%; Guest eval URL 42 (all claude.ai); Email IDs holds raw addresses.
- 28 Sep (83f8d978...29): 100 rows, messages from Apr 2025 to Sep 2026. Category: Personal/family 23, Guest pitch 22, Sponsored/partnership 18, Vendor 13, Alumni/event 9, Admin 6, Other 5, Misrouted 4. Decision: Unassessed 95. Triage status: Reference/stale 70, Private 24. 4 views including "Mamatha threads".
- Both are frozen snapshots with page bodies summarising each thread. Good evidence for Activities and Queue design; neither should become operating data.

### 3.14 Meetings (3c419a30...567)
- 12 rows, 22 Aug to 30 Sep. Notion AI meeting notes (summary, action items, transcript). Contents include FT recordings, precalls and PaaS sales calls. Project relation points at the starter-template Projects table. Attendees is a Notion person field (team only).

---

## 4. People data quality

| Field | Members (682) | B2S live (90) | B2S archive (492) | HBD (113) | US VC Contact 1 (774) | PaaS (14) |
|---|---|---|---|---|---|---|
| Name clean, split | Yes, single field | Packed in "Name @ Company" | Packed | Yes | Yes | Yes (Founder) |
| Email | **no field** | 68 (76%) | 489 (99%) | 112 (99%) | 594 (77%) | none |
| LinkedIn | 631 (93%) | title hyperlink, unmeasurable | title hyperlink, some are search URLs | none | 731 (94%) | none |
| Location | none | Country 100% | Country 100% | none | firm City/State only | none |
| Blurb / bio | "What they do" 2 to 5 words | AD Comment (46) | none | Note (8) | firm Overview, Fit Note | Last call details (7) |
| Phone | 599 (88%) | none | none | none | none | none |

All counts [M].

**Blurbs.** No table stores a guest blurb. Nearest substitutes: Members "What they do" (a sector tag), Article Queue "Fact sheet" in page bodies (only on the handful of drafted rows [E]: 8 Drafted + 2 Published), US VC "Overview" (firm-level). The FT blurb skill sends to Slack, not Notion.

**Research history / evals / dossiers.** Stored as links to claude.ai (triage Guest eval, PaaS Pitch note and Chat Link) or Google Docs (PaaS Guest note); PaaS child pages hold pitch drafts; Meetings hold precall notes. Nothing links any of these to a person record.

**Duplicates within tables [M].**
- Members: 1 repeated name (may be two people), 3 LinkedIn URLs used twice.
- Episode Inventory: 29 guests with 2 to 3 episodes (expected, not errors).
- B2S: live and archive share 4 names; at least one hand-merged duplicate noted in AD Comment.
- US VC, Article Queue, HBD: no exact duplicates found.

**Duplicates across tables (exact normalised-name match) [M].**
- Whatsapp Group Members vs Members: 479 of 505 (the other 26 likely variants [E]).
- Episode Inventory guests vs Members: 491 of 548 distinct guest names; 514 episodes by YouTube URL.
- B2S live vs Members: 12; vs Episode Inventory: 13. B2S archive vs Members: 22.
- HBD vs Members: 1. HBD vs B2S: 0.
- PaaS founders vs Members: 2 (4 by company). US VC Contact 1 vs Members: 1.
- Exact-name matching understates overlap (initials, "Dr", spelling). Real cross-table overlap is probably 1.5 to 2 times these figures [E].

**Estimated distinct people in Notion:** about 680 (Members) + 540 (B2S) + 110 (HBD) + 2,000 (VC contacts 1 to 3) + small tails = **about 3,300** [E], before counting "Other Contacts" lines and people named in triage text.

---

## 5. Mapping to the target tables

| Target | Source in Notion today | Notes |
|---|---|---|
| **People** | Members Master List (seed); contacts from US VC (Contact 1 to 3, Other Contacts); names from B2S live + archive, HBD, PaaS Founder, Vendor Contact Name | Split "Name @ Company". Location must be added (only B2S Country exists). Blurb: seed from "What they do" and Article Queue Fact sheets. Research history: attach claude.ai eval links and Meetings. Phone goes to a restricted field or Credentials, not the open People table. |
| **Organisations** | US VC firm fields (774); Company text on every table | No company table exists; Company is free text everywhere with variants ("Koo/ Vokal", "Eko" vs "Eko India"). |
| **Engagements** | B2S live + archive (guest invite), HBD (guest invite), PaaS Leads (BD prospect / client), US VC (BD prospect, all Identified), Vendor Pitches (inbound pitch), triage rows tagged Podcast pitch / Guest eval / Sponsorship (inbound pitch, sponsor) | Stage map: Not started / Identified = Identified; Emailed/Started, Pitched, Send Pitch, Sent = Contacted; Chasing, In discussion, Proposal sent, Meeting, Replied = In conversation; Booked, Won, Approved (host side) = Agreed. Outcome: Declined, Lost, Unresponsive, Do not contact, Maybe later, Later, Dormant, Bounced. HBD "Approved" needs splitting into host-approved vs guest-agreed. |
| **Shows** | Show select in Episode Inventory and Article Queue (FT, Spotlight only); B2S and HBD implied by table name | Need a real Shows table with FT, Spotlight(?), un#, B2S, HBD. |
| **Episodes** | Episode Inventory (582) + Article Queue (439) + Substack Posts Audit (metrics) | Merge on YouTube URL. Move Article Queue page body (working doc) into the episode page body. Final fields (title, subtitle, Substack URL, YouTube, Spotify, Apple, views, theme, article state) mostly exist in Episode Inventory. Published date is empty on 581 of 582. |
| **Tasks** | Only the starter-template Tasks (3 rows); in practice Agent notes "YOU NEED TO DO" text, PaaS Next Action, triage Next action | No real task table. |
| **Activities** | Meetings (12), inbox triage snapshots (161), Newsjack Log (130, agent runs), PaaS Last call / Last checked | Email, call and WhatsApp events are not logged per person anywhere. |
| **Queue** | Publishing Plan (agent decisions), Newsjack Log rows needing a call, triage "Decision needed", B2S "pending Satish approval" | Decisions for Akshay are scattered across 4 tables and free-text comments. |
| **Templates** | Substack Audit Report children (Article Writing Spec, Tags + AEO Strategy, FT Channel Rules, Subtitle drafts), Meetings "@Today" template, Vendor "Pitch to Us" form, "Founder Thesis: sponsored guest features" page, Routing Rules page | Mostly playbooks and specs, not reusable email/message templates. |
| **Credentials** | None found | Phone numbers in Members and the DELETE page are the only sensitive-contact store. |

---

## 6. Surprises and risks

1. **Relations are nearly empty.** The only relational link (Members to Episodes) is filled on 25 rows while 514 are matchable by URL. Every other link is by copied text (Guest, Company, YouTube URL).
2. **Two parallel episode tables.** Episode Inventory and Article Queue describe the same 400+ episodes as separate pages; the valuable working content is on the Article Queue side, the metadata on the Inventory side.
3. **Fields described but not populated.** Episode Inventory Priority (0 of 582, described as Ranjita's work order), Published date (1 of 582), Zencastr transcript (0), Article Queue Owner and Thumbnail (0), Newsjack Rank (0).
4. **B2S split into live and archive** with the real history in the archive; hand-merging is already happening. Risk of double outreach to the same founder.
5. **13 B2S targets already have FT episodes** and 1 HBD target is in Members, with nothing warning the person doing outreach.
6. **Option drift** in Newsjack Log, PaaS (mixed stage/action/parking statuses, inconsistent casing) and HBD (Approved meaning two things).
7. **Bulk imports with zero follow-through**: US VC 774 enriched, none sent; B2S live 82 not started; HBD 99 blank status.
8. **PII in the open**: phone numbers on 599 Members rows and in one Source Note; a "DELETE" page with phone data and 16 orphan person pages; raw email addresses in triage "Email IDs"; 23 personal/family emails in the 28 Sep snapshot; Vendor form collects phone numbers. The WhatsApp members table sits under a page described as public-facing (sharing state not verifiable via API).
9. **Starter template debris** (Projects, Tasks, Docs, My Tasks with "Website Redesign", "Mobile App Launch") and temp views ("idmap-temp", "TEMP guest empty") add noise for agents searching the workspace.
10. **Eval and dossier output never lands in Notion**; it lives in claude.ai chats/artifacts and Google Docs, so it is not searchable from a person record and may be lost if links break.
11. **Everything sits in one person's private section** (no ancestor paths or teamspace on the databases); team access depends on individual sharing.

---

## 7. Open questions for Akshay

1. Is **Spotlight** a show in its own right in the Shows table, or a format of Founder Thesis?
2. Where does **un#** guest and episode data live today (Sheets?), and should it come into Notion in the first cut?
3. Should the **B2S archive** be treated as the source of truth for outreach history, and can the live list be rebuilt as a view of Engagements?
4. For HBD, what does **"Approved"** mean: approved by Arjun to invite, or guest agreed? Same question for B2S "Satish Approved".
5. Are the **~170 non-guest community members** in Members people you want in People (with engagements), or only in a community view?
6. Should **phone numbers** stay in Notion at all? If yes, in which restricted table; if no, can they be removed from Members and the DELETE page?
7. Is the **US VC list** an active BD campaign, or a research asset to park? It is the single largest source of people (about 2,000).
8. Should **evals, dossiers and pitch notes** be saved into Notion (as page content or files on the person/engagement), rather than kept as claude.ai links?
9. Can the **two inbox triage snapshots**, the Scout log, Substack Posts Audit and the starter-template databases be archived once their fields are mapped?
10. Is the **Article Queue page body format** (fact sheet, titles, subtitle, article, tags, thumbnail) the template you want every episode's working doc to follow?
11. Who owns **Publishing Plan and Newsjack decisions** day to day: should agent picks go into Akshay's Queue, or straight to Ranjita?
12. Is **"What they do"** worth keeping as a short tag alongside a proper blurb, or should it be replaced?
