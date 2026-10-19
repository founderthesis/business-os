# Table spec

Draft 3, 30 Sep 2026. For review with Akshay before anything is created in Notion.

How to read it. **Fill** says who fills a field:
- **Auto**: an agent or formula fills it. Nobody types.
- **Migrate**: filled once from old data, then kept up by agents.
- **Human**: someone types or picks it. Every Human field has to earn its place.

Every table also carries three provenance fields, not repeated below: `Source` (where the row came from), `Source ID` (its ID there), `Captured` (date). Rows from the migration carry `Migration batch` too.

Twelve tables: People, Organisations, Engagements, Deals, Shows, Episodes, Tasks, Activities, Queue, Templates, Credentials, Guest forms.

**Tags everywhere.** People, Organisations, Engagements, Episodes and Tasks each have a `Tags` multi-select that anyone can add values to. Tags are how the team organises on the fly without asking for a new field. Agents read and set tags too (for example the tier after a recording). Fixed fields stay only where an automation needs exactly one value, such as Stage or Status.

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
| Blurb | text | Agent | Research profile, 2 to 3 neutral lines, any show (decision 342). The WhatsApp intro is WA-Blurb on FT Community (decision 331) |
| Research | page body | Auto | Every eval, dossier, prep note and call summary, newest first, each with date and link |
| Latest eval verdict | select | Auto | Book immediately / Strong consider / Pre-call needed / Decline |
| Tags | multi-select | Auto / Human | Starts with Guest, Prospect, Sponsor, PR contact, Host, Client, Team, Investor, US VC, No email, Name guessed, Role inbox; anyone can add more |
| FT guest | checkbox | Auto | True if linked to any published FT or Spotlight episode |
| Substack article | url | Migrate / Auto | Their founderthesis.com feature |
| Instagram | url | Form / Auto | For sending reels on release day |
| What they do | text | Migrate | Short descriptor from the master list |
| In WhatsApp group | checkbox | Migrate / Human | Akshay's 500+ founders and VCs group |
| Episodes | relation → Episodes | Auto | |
| Engagements | relation → Engagements | Auto | Everything we have pursued with them, any show |
| Last contact | date | Auto | Rolled up from Activities |
| Match status | select | Auto | Clean / Possible duplicate / Merged into another row. A human resolves duplicates |
| Duplicate of | relation → People | Auto | The other row of a possible duplicate pair, so the human sees both |
| Duplicate check | text | Auto | One line from the dedupe check (web lookup): same, different or unsure, and why |

Views: Network (FT guest or In WhatsApp group; the pitch asset), PR contacts, Needs review (possible duplicates).

## 2. Organisations

One row per company, fund or agency.

| Field | Type | Fill | Notes |
|---|---|---|---|
| Name | title | Migrate | |
| Domain | text | Auto | Used to match people and infer PR agencies |
| Type | select | Auto | Startup, Enterprise, Fund, PR agency, Client, Vendor |
| Website | url | Auto | |
| General email | email | Migrate / Auto | Role inbox (info@, hello@). Personal addresses go on People |
| People | relation → People | Auto | |
| Client | checkbox | Human | True for retainer clients |
| Engagements | relation → Engagements | Auto | |
| Instagram | url | Form / Auto | Company page, for reels on release day |
| Tags | multi-select | Auto / Human | Free |

PR agencies are recorded here for the first time. Today the agency is never written down; the migration infers it from the PR contact's email domain.

## 3. Engagements

One row per guest pursuit: a person and a show. Replaces every guest pipeline tab. The full status ladder, the sponsored payment track and the mapping from the old sheets are in `docs/statuses.md`.

| Field | Type | Fill | Notes |
|---|---|---|---|
| Name | title | Auto | "Person @ Company, Show" |
| Show | relation → Shows | Migrate / Auto | |
| Guest | relation → People | Migrate / Auto | The person being featured |
| Stakeholders | relation → People | Auto | PR agency people, comms, EAs. All copied on guest emails |
| Via | relation → People | Migrate / Auto | The PR contact who brought it in |
| Organisation | relation → Organisations | Auto | |
| Direction | select | Auto | Inbound (pitched to us), Outbound (we reached out) |
| Status | select | Auto / Human | New, Contacted, Interested, Decision pending, Send draft, Precall requested, Precall done, Sponsored offered, Booking, Booked, Recorded, Form filled, LT chase, Parked, They declined, We declined, Unresponsive |
| Tier | select | Human | Tier 1, Tier 1.5, Tier 2, Sponsored. Importance to us, or Sponsored when the guest pays (Payment and Amount apply). Set by Akshay (decision 74) |
| Call type | select | Auto | Precall, Recording, Planning call. What Next date is when it is a call |
| Call link | url | Auto | Zencastr, Riverside or Meet link of the next call, from the calendar |
| Eval verdict | select | Auto | Book immediately, Strong consider, Pre-call needed, Evaluate after call, Decline. Hidden by default |
| Eval link, Dossier link | url | Auto | |
| Host verdict | select | Auto / Human | Yes, No, Maybe, Not asked. un#, B2S and HBD only |
| Next action | text | Human / Auto | One line |
| Next date | date | Human / Auto | When someone next acts. Today or earlier = on the team's list (FT: Today). A booked call's date when nothing else is due (decision 79) |
| Next action | text | Human / Auto | Who does what, starting with the person: "Mamatha: ...", "Ask Akshay to ...", "Fix: ...", or "Waiting on <who>: ..." |
| Last activity | text | Auto | "<D Mon>, <summary>" of the newest logged mail or form. Written by the routines (decision 79) |
| Due | formula | Auto | "Due" when Next date is today or earlier. The FT: Today view filters on it |
| Chase step | number | Auto | 0 to 5 on the follow-up ladder |
| Payment | select | Human / Auto | Not started, GST received, Invoice 1 sent, Payment 1 received, Invoice 2 sent, Payment 2 received, Settled. Sponsored only |
| Amount | number | Human | Sponsored fee |
| Episode | relation → Episodes | Auto | Created at Booked |
| Activities, Queue items, Deals | relations | Auto | |
| Tags | multi-select | Auto / Human | Free |

Retired on 5 Oct 2026: Type, Stage, Outcome, Whose move, Heat, Pitch link, Rank, Paid. Commercial rows moved to Deals.

## 3b. Deals

One row per company we are selling podcast production to (PaaS). Later also show sponsors and partners.

| Field | Type | Fill | Notes |
|---|---|---|---|
| Company | title | Auto | |
| Organisation, Contacts | relations | Auto | |
| From engagement | relation → Engagements | Auto | The FT guest row it grew out of, if any |
| Warm or cold | select | Auto | Warm (via an FT guest, recording or intro), Cold outreach |
| Stage | select | Human / Auto | New, Contacted, Interested, In conversation, Proposal sent, Won, Parked, Declined, Unresponsive |
| Heat | select | Human | Hot, Warm, Cold |
| Proposal link | url | Human | Short link to the proposal (podm.in), the one we send |
| Pitch note | url | Auto | The full proposal page with pricing (artifact or Doc) |
| Guest note | url | Auto | Guest-facing note for the client show's prospective guests |
| Chat link | url | Auto | The Claude chat where the pitch was built |
| Fit rank | number | Migrate | Cold list ranking, 1 first |
| Budget read | text | Migrate | |
| Amount | number | Human | |
| Next action, Next date, Chase step | | | As Engagements |
| Tags | multi-select | | Has podcast, Priority A/B/C, No email |
| Activities, Queue items | relations | Auto | |

## 4. Shows

One row per show. The page body is the show's wiki: ad hoc notes, things to remember, how the host likes to work.

| Field | Type | Fill | Notes |
|---|---|---|---|
| Name | title | Human | Founder Thesis, un#, Built to Share, Human by Design, client shows. Spotlight is not a show; it is FT Tier 3 |
| Host | relation → People | Human | |
| Owned | select | Human | Owned, Client |
| Active | checkbox | Human | |
| Guest note | url | Human | The standard note sent to prospective guests |
| Recording guidelines | url | Human | Sent with every recording invite |
| YouTube | url | Human | FT also stores the Spotlight channel |
| Spotify | url | Human | |
| Apple Podcasts | url | Human | |
| Amazon Music | url | Human | |
| RSS | url | Human | FT also stores the Spotlight feed |
| Website | url | Human | e.g. founderthesis.com |
| Release cadence | text | Human | e.g. "weekly, Monday"; used by the release planner |
| Default sponsored price | text | Human | e.g. INR 50k + GST, or USD 600 outside India |
| Templates | relation → Templates | Auto | |
| Wiki | page body | Human | Free notes |

These are set once per show, so Human is fine here.

## 5. Episodes

One row per episode. Created automatically when a recording is booked. Absorbs Episode Inventory, Article Queue page bodies, and the Blue-only episodes (field data only).

| Field | Type | Fill | Notes |
|---|---|---|---|
| Episode | title | Auto | "Guest @ Company - Show", plus " - V2" for a repeat recording or " - Part N". Never the published title |
| YouTube title, Spotify title | text | Auto | Titles as published; they can change and can differ by platform |
| Show | relation → Shows | Auto | |
| Guests | relation → People | Auto | One or more. Two-guest episodes link both |
| Engagements | relation → Engagements | Auto | One per guest |
| Tags | multi-select | Auto / Human | Holds the tier (Tier 1, Tier 2, Tier 3 Spotlight), set by the one tap after recording. Tier 3 Spotlight publishes on the Spotlight channel and feed. Anything else the team wants: Two guests, Re-edit, Sponsored, Evergreen |
| Status | select | Auto | Scheduled, Recorded, Transcript in, Copy in progress, Editing, Ready, Published |
| Recording date | date | Auto | From the calendar |
| Planned release | date | Auto | Set by the release planner, approved on the dashboard |
| Actual release | date | Auto | From YouTube or the RSS feed |
| Slip (days) | formula | Auto | Actual minus planned |
| Transcript | file / url | Auto | Downloaded from Zencastr |
| Copy done | checkbox | Auto | True when every copy section in the working doc has a tick |
| Open checks | number | Auto | Unticked review flags from the skills (verify ASR, confirm a fact). Ready is blocked while above 0 |
| YouTube, Spotify, Substack, LinkedIn links | url | Auto | After release |
| Apple | url | Auto | After release |
| Sector | multi-select | Migrate / Auto | Fintech, SaaS, D2C, Marketplace, Deeptech, Edtech, Healthtech, Services, Gaming |
| Article state | select | Auto | None, Short, Drafted, Full: the founderthesis.com feature |
| Article priority | number | Migrate / Auto | Order the article agent works through |
| YouTube views | number | Auto | Lifetime, refreshed by a routine |
| Guest form in | checkbox | Auto | FT only. Photo, logo, designation, links and PR emails received. Other shows do not send the form |
| Tasks | relation → Tasks | Auto | |
| Priority | formula | Auto | 1 client, 2 Tier 1, 3 Tier 2, 4 Tier 3 Spotlight, 5 untiered. Sorts the release calendar and task due dates |
| Views 7d, Avg view duration, New viewers %, Browse %, External % | number / text | Auto | The numbers reviewed on the weekly release feedback call |
| Team feedback | text | Auto | Verdicts from the weekly call, parsed from the Gemini notes |

Episode tags also include Client (client episodes jump the queue) and Guest review (rendered frame sent to the guest before release; default for HBD).

No typed Final fields. The final version of every piece of copy is whatever is ticked in the working doc.

### The working doc (Episode page body)

Created with the Episode, empty sections ready. Skills fill it in two passes:

- **Stage A, when the transcript lands:** Themes, Cinematic titles, Host intro, Lower thirds, Soundbite bank, Cut list.
- **Stage B, when a theme is ticked:** YouTube titles, Thumbnail copy, Show notes, LinkedIn set, Trailer copy, Substack draft.

Every option is a checkbox line. The copywriter ticks the one to use and can edit its text in place. Options pasted from Gemini or ChatGPT go in the same section, tagged [Gemini] or [ChatGPT].

```
## YouTube titles
- [ ] How Venkat took Vyome from Delhi to Nasdaq
- [x] India makes the world's medicine and invents almost none of it
- [ ] [ChatGPT] The Chik shampoo CEO building a cancer drug
```

What the skills learn from, with nobody filling a form:
- which option was ticked and which were not, per skill and per show
- how much the ticked text was edited (the agent keeps a copy of what it generated)
- which model's option won
- later, how the episode performed

Review flags from the skills sit in a "Checks" section as checkboxes too.

## 6. Tasks

A handful per episode, created automatically. Owner comes from the task type.

| Field | Type | Fill | Notes |
|---|---|---|---|
| Task | title | Auto | |
| Episode | relation → Episodes | Auto | |
| Engagement | relation → Engagements | Auto | For non-episode work |
| Owner | select | Auto | From the task type (below) |
| Due | date | Auto | Counted back from Planned release |
| Status | select | Auto / Human | To do, Doing, Done. Copy tasks close themselves when the working doc is ticked |
| Tags | multi-select | Auto / Human | Free, e.g. Blocked, Urgent |

| When | Task | Owner | Due |
|---|---|---|---|
| Transcript in | Pick theme and final copy | Ranjita | Planned release minus 7 days |
| Transcript in | Edit episode (cut list and lower thirds linked) | Sarika | Planned release minus 5 days |
| Edit done | Shorts | Sarika | Planned release minus 2 days |
| Copy done | Thumbnail design | Sarika | Planned release minus 3 days |
| Ready | Release emails and posts | Ranjita | Release day |

The table of task types lives in `routines/tasks.md` so it can change without touching Notion.

### Release calendar

A calendar view of Episodes by Planned release, coloured by show. A release-planning task runs every other week in Cowork (or on demand): it looks at episodes in progress, each show's cadence and open slots, proposes Planned release dates for the coming month, and puts them on the dashboard for approval. Actual release fills itself, so slips show up on the calendar.

## 7. Activities

Something that happened, logged once. Only mail tied to a person or engagement is logged; noise is not.

| Field | Type | Fill | Notes |
|---|---|---|---|
| Summary | title | Auto | One line. The page body holds a 2 to 3 line summary of what was said and asked |
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
| Type | select | Auto | Ask Akshay, Follow up, Fix data (decision 67). Decision, Heads-up, Reminder, Action, Chase and Noise are history only |
| For | select | Auto | Akshay, Mamatha, Chaandini, Sarika, Ranjita |
| Recommendation | text | Auto | e.g. "Sponsored" pre-selected when the eval says Decline |
| Choice | select | Human | Sponsored, Precall, Book, Decline, Present to host, Approve, Edit first, Dismiss |
| Comment | text | Human | Optional |
| Prepared action | page body | Auto | The exact email (to, cc, subject, body) or calendar change that runs on approval |
| Related | relation → People, Engagements, Episodes | Auto | |
| Gmail thread | url | Auto | |
| Eval | url | Auto | Mamatha's guest eval link |
| LinkedIn | url | Auto | Of the person the decision is about, not the PR contact |
| Website | url | Auto | That person's company |
| Other link | url | Auto | The one other link needed to decide: notes Doc, deck, episode |
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
- Whatsapp Group Members (its members set the In WhatsApp group checkbox; new members are ticked on People after that), FT Newsjack Scout, Substack Posts Audit, both inbox triage snapshots, the starter templates, and the page titled "DELETE" (holds phone data; a human deletes it).
- Sheet columns that are data-verification flags or contact plans (listed in the sheets audit).

## Guest forms

One row per Founder Thesis guest form submission, made by the Notion form behind podm.in/thank-you (decision 69). Raw and append-only. The inbox routine merges it; photos and logos stay on the row and the Engagement links to it.

| Field | Type | Fill | Notes |
|---|---|---|---|
| Guest name | title | Form | As it should appear in the episode |
| Company | text | Form | |
| Designation | text | Form | On-screen title. Copied to People Role |
| Guest email | email | Form | Main match key |
| Guest LinkedIn, Company LinkedIn | url | Form | |
| Photo | files | Form | High-res guest photo |
| Logo | files | Form | |
| Guest Instagram, Company Instagram | url | Form | Optional. Copied to People and Organisations where empty |
| PR and comms emails | text | Form | Optional. Each becomes a PR contact Stakeholder |
| Filled by | text | Form | When a PR person or EA fills it in |
| Before release | text | Form | Optional. Anything to hold back; copied to the Engagement's Claude note |
| Submitted | created time | Auto | |
| Engagement | relation → Engagements | Auto | Two-way; the Engagement shows it as Guest form |
| Merge status | select | Auto | New, Merged, Needs review |
| Merge note | text | Auto | What the routine changed, or why it could not match |


### Your call (Engagements, added 12 Oct 2026, decision 157)
Text. Written by whoever the row is waiting on (Akshay, Chaandini, Mamatha, a host): their decision or instruction. The inbox routine acts on it at its next run, copies it word for word with the writer's name into Claude note, and clears it. Agents never write here; their state and proposals stay in Next action.
