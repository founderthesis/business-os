# Architecture

Version 1, 30 Sep 2026. Plain-language version: https://claude.ai/artifact/L8TPLZUSa3rLfXwaHjwYqa

## Goals

1. **Remember people.** One record per human across every sheet, show and inbox. "Have we ever spoken to this person?" answered in one search.
2. **Queue decisions.** Pitches and precalls reach Akshay already researched. He taps, the reply goes.
3. **Free up Mamatha.** Intake, research, chasing and status updates run themselves, so she manages relationships instead of routing information.
4. **Team self-serve.** Everyone sees what they own today.
5. **Make the content.** Skills write the episode pack into Notion and learn from what gets used.
6. **Record the inbox.** Every email is logged on the person and the conversation it belongs to.

Scope: owned shows, BD, client production. Ghostwriting later.

## Layers

```
SOURCES      Gmail · Calendar · Gemini notes · Zencastr · Sheets · Blue · Guest form · WhatsApp (pasted)
   │
1 CAPTURE    everything becomes an Activity (append-only, with source)
   │
2 RESOLVE    match to a Person: LinkedIn, then email, then domain, then name + company
   │         unsure → Queue for a human; never auto-merge
   │
3 MEMORY     People ── Organisations
                │
             Engagements ── Shows
                │
             Episodes (page body = working doc) ── Tasks
             Templates · Credentials (walled off)
   │
4 AGENTS     intake + eval · inbox sorter · chase · prep docs · content pack · skill learning · morning brief
   │         write only to the Queue, then act on approval
   │
5 SURFACES   Notion views · private prep calendar (dashboard dropped, decision 61)
             team "my work today" · episode working doc · host portal · client portal
```

## Tables (10)

| Table | One row is | Key contents |
|---|---|---|
| People | a human; the master network list | name, LinkedIn, email, phone, location (from LinkedIn), organisation, role, blurb, research history (evals, dossiers, prep notes), tags (guest, prospect, sponsor, PR contact, host), FT guest, Substack article, in WhatsApp group |
| Organisations | a company, fund or agency | domain, type, client status, people |
| Engagements | one pursuit with a person or organisation | type (guest outbound, guest inbound, BD, sponsor, partner, client), show, stage, outcome, whose move, next action and date, eval verdict, host approval (hosts answer on their host board, decision 185), commercial terms, via (PR contact, a Person), stakeholders (everyone else on the thread, all copied on guest emails) |
| Shows | a podcast | host, owned or client, active, templates, default price (Spotlight is FT Tier 3, not a show) |
| Episodes | an episode | show, guest(s), tier, recording and publish dates, transcript, links, Final fields (title, cinematic title, thumbnail copy, intro VO, show notes, LinkedIn post, trailer copy); page body is the working doc every skill writes into |
| Tasks | a unit of work with an owner | episode or engagement, owner, due, status; a handful per episode, auto-created |
| Activities | something that happened | person, engagement, date, source (email, call, meeting, form, WhatsApp), summary, link |
| Queue | something waiting for a human | type (decision, heads-up, reminder, action), related records, recommendation, prepared email or calendar change, status, decided by, decided at |
| Templates | an email that can be sent | show, purpose, body, version, approved (a template edit resets approval) |
| Credentials | a login | walled off; no routine reads it |

Engagements carry one Status ladder for the guest journey (New to Form filled, plus LT chase, Parked, They declined, We declined, Unresponsive); see docs/statuses.md. After Booked, production state lives on the Episode. Commercial pursuits (PaaS, sponsors, partners) live in Deals with their own Stage.

Field-by-field spec: `docs/schema.md`.

## The inbox

Dropped for now (decisions 61, 62): the sorting dashboard and the Decision Desk. Akshay reads all his own mail. The inbox agent only records: one Activity per email, and the Engagement or Deal moved to match. Decision surfaces get another try later with a different approach.

## Triggers

| When | What happens | Human part |
|---|---|---|
| Any email arrives | Logged as an Activity; Engagement or Deal updated | None |
| Pitch arrives | Eval skill runs; research saved on the Person; decision card | Tap an answer |
| Precall booked | Prep entry on private calendar with eval link and a reminder to switch on the Meet transcript | One click in the call |
| Precall ends | Gemini notes read, eval re-runs, recommendation card | Record / Don't / Another call |
| Recording ends | Tier card; Claude in Chrome opens the Zencastr link from the invite and downloads the transcript | Pick the tier; Mac must be on |
| Transcript saved | Thank-you with transcript + PR form request sends (standing approval); content pack stage A writes into the Episode page | None |
| Theme picked | Content pack stage B (titles, show notes, LinkedIn, trailer copy, Substack) | Pick the theme |
| Recording in 3 days | Dossier made if missing, linked on the private prep entry | None |
| Follow-up due | Reminder in brief; templated chase sent or queued | WhatsApp: chase, then paste the chat in |
| Monthly | Each skill reviewed against Finals vs its options; change proposed | Approve the edit |

Private prep calendar: a separate calendar only Akshay sees. Agents never write into an event that has guests on it.

## Content pack and learning

- Stage A (on transcript): themes, cinematic titles, lower thirds, soundbite bank, cut list, host intro.
- Stage B (on theme pick): YouTube titles, thumbnail copy, show notes, LinkedIn set, trailer copy, Substack article.
- Claude runs automatically. Gemini or ChatGPT options can be pasted into the same page, tagged by model.
- Skills flag risks as checklist items on the Episode (verify ASR at a timestamp, confirm a fact). The episode cannot be marked Ready while one is open.
- Learning signals: which option became the Final, how much it was edited, how the episode performed. Monthly, each skill gets a proposed rule change for Akshay to approve. Skill sources are versioned in `skills/`.

## Runtime

| Piece | Runs on |
|---|---|
| Storage and screens | Notion |
| Skill work, email, calendar | Scheduled Claude routines with Notion, Gmail, Calendar, Drive connectors |
| Zencastr transcript download | Claude in Chrome on Akshay's Mac |
| Migration, identity resolution | Python in `migration/`, re-runnable |
| Rules, prompts, skill versions | This repo |

Google Workspace access. Claude reaches Gmail, Calendar, Drive, Docs and Sheets through the connectors Akshay approved with ad@thepodium.in. In the Workspace admin console these are third-party connections, managed under Security, Access and data control, API controls, app access control. Claude must stay Trusted or Unrestricted there: Limited or Blocked cuts every routine off from mail, calendar and Drive at once. The admin page "Agents, Agent access management" is only for Google's own Gemini agents and does not govern Claude (checked 15 Oct 2026; no Gemini agents in use).

## Build order

1. Audits (done or running; see `docs/audits/`)
2. Clean People: all sources into one list, enriched with location, blurb, research; duplicates reviewed by a human
3. Capture: Gmail and Calendar into Activities
4. Dashboard: inbox sorting, eval on intake, send after approval, mark read
5. Content pack into Episode pages, with learning
6. Team views and morning brief
7. Host and client portals
8. One-week parallel run, then retire the sheets and Blue
