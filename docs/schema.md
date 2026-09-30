# Table spec

Draft 1, 30 Sep 2026. For review with Akshay before anything is created in Notion.

How to read it. **Fill** says who fills a field:
- **Auto**: an agent or formula fills it. Nobody types.
- **Migrate**: filled once from old data, then kept up by agents.
- **Human**: someone types or picks it. Every Human field has to earn its place.

Every table also carries three provenance fields, not repeated below: `Source` (where the row came from), `Source ID` (its ID there), `Captured` (date). Rows from the migration carry `Migration batch` too.

Ten tables: People, Organisations, Engagements, Shows, Episodes, Tasks, Activities, Queue, Templates, Credentials.

---

## 1. People

One row per human, forever. This is the master network list: every FT guest, everyone in Akshay's founder and VC WhatsApp group, prospects, PR contacts, hosts, team. It replaces Members Master List, Whatsapp Group Members, the Drive "Founder_Thesis_Master_People_List" and the people inside every pipeline sheet.

| Field | Type | Fill | Notes |
|---|---|---|---|
| Name | title | Migrate | Cleaned: no "@ Company", no URLs |
| LinkedIn | url | Migrate / Auto | Primary identity key. Many sit as hidden hyperlinks in the sheets; the migration reads them |
| Email | email | Migrate / Auto | Best current address. Role inboxes (press@, ir@) never go here |
| Other emails | text | Auto | Older or alternate addresses, for matching |
| Phone | phone | Migrate | Kept, per Akshay |
| Organisation | relation → Organisations | Migrate / Auto | Current one |
| Role | text | Auto | Title at the organisation |
| Location | text | Auto | City, country from LinkedIn or the eval. Apollo fills the rest |
| Blurb | text | Auto | Latest blurb (Slack #ft-blurbs, host DMs, or generated). About 150 words |
| Research | page body | Auto | Every eval, dossier, prep note and call summary, newest first, each with date and link |
| Latest eval verdict | select | Auto | Book immediately / Strong consider / Pre-call needed / Decline |
| Tags | multi-select | Auto | Guest, Prospect, Sponsor, PR contact, Host, Client, Team, Investor |
| FT guest | checkbox | Auto | True if linked to any published FT or Spotlight episode |
| Substack article | url | Migrate / Auto | Their founderthesis.com feature |
| In WhatsApp group | checkbox | Migrate / Human | Akshay's 500+ founders and VCs group |
| Episodes | relation → Episodes | Auto | |
| Engagements | relation → Engagements | Auto | Everything we have pursued with them, any show |
| Last contact | date | Auto | Rolled up from Activities |
| Match status | select | Auto | Clean / Possible duplicate / Merged into another row. A human resolves duplicates |

Views: Network (FT guest or In WhatsApp group; the pitch asset), PR contacts, Needs review (possible duplicates).

## 2. Organisations

One row per company, fund or agency.

| Field | Type | Fill | Notes |
|---|---|---|---|
| Name | title | Migrate | |
| Domain | text | Auto | Used to match people and infer PR agencies |
| Type | select | Auto | Startup, Enterprise, Fund, PR agency, Client, Vendor |
| Website | url | Auto | |
| People | relation → People | Auto | |
| Client | checkbox | Human | True for retainer clients |
| Engagements | relation → Engagements | Auto | |

PR agencies are recorded here for the first time. Today the agency is never written down; the migration infers it from the PR contact's email domain.

## 3. Engagements

One row per pursuit: a person (or organisation) and a goal, usually on a show. Replaces every pipeline tab. Rows that were copied forward between sheet tabs (FT Inbound to P1, B2S N2 to N3, un# Pipeline v2 to CRM) collapse into one row; the latest status wins and the history goes into Activities.

| Field | Type | Fill | Notes |
|---|---|---|---|
| Name | title | Auto | "Person @ Company, Show" |
| Type | select | Auto | Guest outbound, Guest inbound, BD, Sponsor, Partner, Client |
| Show | relation → Shows | Migrate / Auto | The show it starts on. Spotlight episodes start as FT |
| Guest | relation → People | Migrate / Auto | The person being featured or pitched |
| Stakeholders | relation → People | Auto | Everyone else on the thread: PR agency people, company comms, EAs, interns. Filled from email participants. All are copied on guest emails |
| Via | relation → People | Migrate / Auto | The PR contact who brought it in, if any |
| Organisation | relation → Organisations | Auto | |
| Stage | select | Auto | Identified, Contacted, In conversation, Agreed |
| Outcome | select | Auto | Live, Done, Declined, No response, Dropped out |
| Whose move | select | Auto | Akshay, Mamatha, Chaandini, Sarika, Ranjita, Host, Them |
| Next action | text | Auto | One line |
| Next date | date | Auto | Drives chasing and reminders |
| Chase step | number | Auto | 0 to 5 on the follow-up ladder. A human "Stop chasing" sets Outcome |
| Eval verdict | select | Auto | Book immediately / Strong consider / Pre-call needed / Decline |
| Eval link | url | Auto | The eval page; also added to the person's Research |
| Host verdict | select | Auto / Human | Yes, No, Maybe, Not asked. From Sri Approval, "Arjun rejected" cells, host replies |
| Decision | select | Auto | Akshay's call: Sponsored, Precall, Book, Decline, Present to host |
| Commercial | select | Auto | Free guest, Sponsored, Paid, Client |
| Amount | number | Human | Only when money is agreed |
| Paid | select | Auto | Not due, Invoiced, Part paid, Paid |
| Episode | relation → Episodes | Auto | Created when Stage reaches Agreed and the recording is booked |
| Activities | relation → Activities | Auto | |

Status mapping from the sheets (74 raw values onto these fields) is in `docs/audits/sheets.md`.

## 4. Shows

| Field | Type | Fill | Notes |
|---|---|---|---|
| Name | title | Human | Founder Thesis, Spotlight, alpha un#, Built to Share, Human by Design, client shows |
| Host | relation → People | Human | |
| Owned | select | Human | Owned, Client |
| Parent show | relation → Shows | Human | Spotlight's parent is Founder Thesis |
| Active | checkbox | Human | |
| YouTube channel, RSS | url | Human | |
| Default sponsored price | text | Human | e.g. INR 50k + GST, or USD 600 outside India |
| Templates | relation → Templates | Auto | |

## 5. Episodes

One row per episode. The page body is the working doc: each skill writes its own section (themes, cinematic titles, lower thirds, soundbites, cut list, host intro, titles, thumbnail copy, show notes, LinkedIn set, trailer copy, Substack draft). Absorbs Episode Inventory, Article Queue page bodies, and the Blue-only episodes (field data only).

| Field | Type | Fill | Notes |
|---|---|---|---|
| Title | title | Auto | Working title until Final title is set |
| Show | relation → Shows | Auto | Where it publishes. Tier 3 FT publishes on Spotlight |
| Guests | relation → People | Auto | |
| Engagement | relation → Engagements | Auto | |
| Tier | select | Human | Tier 1 FT, Tier 2 FT, Tier 3 Spotlight. One tap after recording |
| Status | select | Auto | Scheduled, Recorded, Transcript in, Pack drafted, Editing, Ready, Published |
| Recording date | date | Auto | From the calendar |
| Publish date | date | Auto | |
| Transcript | file / url | Auto | Downloaded from Zencastr |
| Theme picked | text | Human | Starts content pack stage B |
| Final title | text | Human | What went live. Compared with the options for learning |
| Final cinematic title | text | Human | |
| Final thumbnail copy | text | Human | |
| Final intro VO | text | Human | |
| Final show notes | text | Human | |
| Final LinkedIn post | text | Human | |
| Final trailer copy | text | Human | |
| Open checks | number | Auto | Count of unticked review flags from the skills (verify ASR, confirm a fact). Ready is blocked while above 0 |
| YouTube, Spotify, Substack, LinkedIn links | url | Auto | After release |
| Guest form in | checkbox | Auto | Hi-res photo, logo, designation, links and PR emails received |
| Tasks | relation → Tasks | Auto | |

The Notion FT guest list that feeds the automated Substack articles keeps working. Either Episodes takes over as its source in one switch, or it stays live until then. Nothing is switched off before that is confirmed.

## 6. Tasks

A handful per episode, created automatically when Status changes. Blue's 33-item checklists had 0 of 484 items ticked, so this stays small.

| Field | Type | Fill | Notes |
|---|---|---|---|
| Task | title | Auto | Edit, Thumbnail, Shorts, Release emails, Substack, LinkedIn |
| Episode | relation → Episodes | Auto | |
| Engagement | relation → Engagements | Auto | For non-episode work |
| Owner | select | Auto | Team first names |
| Due | date | Auto | |
| Status | select | Human | To do, Doing, Done |

## 7. Activities

Something that happened, logged once. Only mail tied to a person or engagement is logged; noise is not.

| Field | Type | Fill | Notes |
|---|---|---|---|
| Summary | title | Auto | One line |
| Date | date | Auto | |
| Kind | select | Auto | Email in, Email out, Meeting, Call notes, Form, WhatsApp, Note |
| People | relation → People | Auto | Everyone involved |
| Engagement | relation → Engagements | Auto | |
| Episode | relation → Episodes | Auto | |
| Link | url | Auto | Gmail thread, Gemini doc, form entry |

## 8. Queue

Akshay's dashboard and the team's work queue. Every inbox email becomes one item; agents add their own suggestions too.

| Field | Type | Fill | Notes |
|---|---|---|---|
| Item | title | Auto | One line |
| Type | select | Auto | Decision, Heads-up, Reminder, Action, Noise |
| For | select | Auto | Akshay, Mamatha, Chaandini, Sarika, Ranjita |
| Recommendation | text | Auto | e.g. "Sponsored" pre-selected when the eval says Decline |
| Choice | select | Human | Sponsored, Precall, Book, Decline, Present to host, Approve, Edit first, Dismiss |
| Comment | text | Human | Optional |
| Prepared action | page body | Auto | The exact email (to, cc, subject, body) or calendar change that runs on approval |
| Related | relation → People, Engagements, Episodes | Auto | |
| Gmail thread | url | Auto | |
| Due | date | Auto | Reminders resurface on this date |
| Status | select | Auto | Waiting, Done, Failed |
| Marked read | checkbox | Auto | |
| Decided at | date | Auto | |

## 9. Templates

| Field | Type | Fill | Notes |
|---|---|---|---|
| Name | title | Human | |
| Show | relation → Shows | Human | |
| Purpose | select | Human | Thank-you, PR form request, Precall, Sponsored decline, Follow-up 1 to 5, Release, Reschedule, Decline, BD sequence |
| Body | page body | Human | With placeholders |
| Version | number | Auto | |
| Approved | checkbox | Human | A body edit clears it. Only approved templates send on their own |

## 10. Credentials

Walled off. No routine reads it. Fields: Service, Login, Notes, Last rotated.

---

## Not carried over

- Blue videos, photos and other heavy files.
- Whatsapp Group Members (becomes the In WhatsApp group checkbox), FT Newsjack Scout, Substack Posts Audit, both inbox triage snapshots, the starter templates, and the page titled "DELETE" (holds phone data; a human deletes it).
- Sheet columns that are data-verification flags or contact plans (listed in the sheets audit).
