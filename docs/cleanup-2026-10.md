# Business OS cleanup: audit and proposal (16 Oct 2026)

Akshay's brief, 16 Oct: "a comprehensive audit on all decisions and routines: retire old decisions, routines, artefacts, Notion pages, clean things up: no duplications, single source of truth."

Status: **proposal, nothing built.** Akshay comments on the Notion copy (decision 220). Decisions 260 to 299 are reserved for what comes out of it. Every number below was measured on 16 Oct from the live scheduled tasks, Notion SQL counts and this repo.

## Part 1. Audit

### What actually runs

| Live task | When (JST) | Prompt | Repo file | Live = repo |
|---|---|---|---|---|
| Inbox to Business OS | 00:00, 08:00, 16:00, 21:00 | 65,481 B (55 B under the cap) | routines/inbox.md | yes |
| Founder Thesis guest evals (Cowork) | :25 after each inbox run | 14,129 B | routines/cowork-evals.md | yes |
| Zoya | :30 after each inbox run | 20,120 B | routines/zoya.md | yes |
| Calendar sync | 08:35, 16:35, 22:35 | 39,357 B | routines/calendar.md | yes |
| WhatsApp to Business OS | :45 after each inbox run | 11,769 B | routines/whatsapp.md | yes (ids redacted in repo) |
| Daily sweep | weekdays 13:10 | 39,063 B | routines/daily-sweep.md | yes |
| Host dossiers and prep notes (Cowork) | 06:50 | 5,487 B | routines/cowork-dossiers.md | yes |
| Salesblink sync | weekdays 09:10, 15:10 IST | 7,962 B | routines/salesblink-sync.md | yes |
| FT Community directory sync | Sat 09:47 | 4,168 B | routines/community-directory.md | yes (never run yet) |
| FT Newsjack daily archive scan | 11:30 | 7,731 B | none | predates the OS |

Disabled but still there: FT guest evals (old cloud, trig_01DbJZ), Dossiers (old cloud), B2S sheet to Notion sync, FT Article Queue. On Akshay's Mac: the transcript task.

**Repo routines/: 21 files, 9 live prompts.** The other 12: evals.md and dossiers.md (the disabled cloud versions, kept "in sync" by hand with the Cowork copies), community-invite-kit.md and un-eval-refresh.md (retired), cowork-tasks.md (setup notes, done), transcripts-backfill.md and transcripts-blue-youtube.md (one-off Mac runs), zencastr-mac.md (proposed), transcripts-after-recording.md (Mac task), add-guest-names.md (paste-in tool), feedback-call.md and tasks.md (specs, not routines; feedback-call still files "Queue items"), tools/make_eval.py (retired by CLAUDE.md).

### Where the bytes go in the four big prompts

| Prompt | Size | Shared rules repeated in it | Dead or one-off text | Work that isn't its job |
|---|---|---|---|---|
| Inbox | 65.5 KB | 8.5 KB | 2.6 KB: STEP 6f loop-in (runs once, 17 Oct), STEP 7c (fires the disabled old evals task), Mamatha backlog clause | 4.9 KB host boards (7d); ~21 KB of sending (6 to 6e, Your call, WhatsApp to Akshay) |
| Daily sweep | 39.1 KB | 9.2 KB | 9.5 KB: STEP 3f sponsored nurture (8.2 KB, which its own ZOYA LIVE line says to skip), STEP 1 Queue, 3c stub, Mamatha backlog | 1.6 KB template review (3e, 6b) |
| Calendar | 39.4 KB | 7.7 KB | Mamatha backlog clause | 6.5 KB of sending (day-before, thank-you, declined-invite, double booking) |
| Zoya | 20.1 KB | 4.2 KB | none | none |

About 30 KB of the same rules (who is in Cc, caps, bounces, context check, links, mail format, template modes, Waiting on and Next date) is copied across four prompts, worded slightly differently each time. The inbox prompt was changed 13 times in 36 hours.

### Why the inbox prompt is bloated

Measured, the cause is not "many exceptions". It is three structural habits:

1. **Override layers instead of rewrites.** When a rule changed, a paragraph was added at the top ("TEAM ROLES ... This overrides every mention of Mamatha below", "ZOYA LIVE ... whatever a read of Rules for Zoya returns") and the old steps were left in place. STEP 5 still routes Founder Thesis work to "Mamatha:" and a header says to read it as "Zoya:". Every rule change adds bytes and never removes any.
2. **The mail reader also sends mail.** Inbox captures mail, but it also sends nine kinds of mail (holding reply, Saurabh thanks, vendor redirect, repeat-pitch note, Akshay's decision mails, admin confirmations, asset receipts, edit-notes reply, sponsored close, acknowledgements, cancellations, loop-ins). Each send needs the whole sending rulebook, so the rulebook lives in inbox too.
3. **Jobs parked where there was room.** Host boards moved from the sweep into inbox (decision 187) because inbox runs more often. The one-off 17 Oct loop-in went in because inbox was the routine running that morning.

### Mail wording: two sources, and they disagree

- Templates database: 55 rows. Wording page ("Mail and WhatsApp wording", ~33k chars): every mail Zoya sends.
- Compared row by row: 29 identical, 12 differ only in sign-off or sender, **14 differ in wording**. 8 mails and 3 WhatsApps exist only on the wording page.
- Inbox, calendar, sweep and the evals task still read Templates; Zoya reads the wording page. Decision 98 (Templates holds the wording) is already marked superseded by 194 and 207. The prompts never moved.
- **Live hazard:** "Eval ready, in the pitch thread" and "Short-form and collab answer" are retired on the wording page but still Mode = Send in Templates.
- Examples of drift: the FT thank-you in Templates links the transcript, the wording page attaches it (decision 228). "Sponsored commercials (FT)" is first person signed Akshay in Templates, third person signed Zoya on the page. "Mamatha's daily list" still carries the dead FT: Today link.

### Sending rules: two regimes running at once

- **Links and format.** Calendar and Zoya send through MCP Emails with real links (decision 184). Inbox and sweep still send through the Gmail connector with links as broken-dot plain text (decision 135, which 184 replaced). The live inbox task has MCP Emails attached and doesn't use it.
- **Cc.** Mamatha is in Cc on every outside mail (decision 132), but she has **0** Founder Thesis rows. Zoya Cc scope, Akshay Cc and the revenue Cc (Jaya, Sarika) are each restated per prompt.
- **Akshay in Cc on Zoya's mail.** Calendar rules says "until 25 Oct (decision 205)", Rules for Zoya says "until he says stop (decision 229)".
- **The daily cap** is counted by matching "Zoya sent" or "Agent sent" in five prompts.

### Overlapping jobs

Four routines send mail and four set Waiting on and Next action for Founder Thesis rows:

| Concern | Inbox | Calendar | Sweep | Zoya |
|---|---|---|---|---|
| Sends mail from ad@ | 9 kinds | 3 kinds | Mamatha's list, Jaya forwards, template review | joining mails, closes |
| Sends from zoya@ | | double booking | | everything else |
| Sets "Zoya: <step>" | yes | yes | yes | yes |
| Closes rows on silence | 3-chase rule | | 3-chase rule, 60-day sponsored rule (dead) | staleness gate |
| Reads Gmail to settle rows | yes | | yes (60 rows a day) | yes |

There are three closing rules for one row, written three ways.

### Leftovers (measured)

- **Queue**: 72 rows, all Done, newest 6 Oct. Sweep STEP 1 still reads it; Engagements still has a "Queue items" relation.
- **Mamatha on FT**: 0 rows Waiting on Mamatha, 0 "Mamatha:" steps. The backlog clauses in inbox, sweep and calendar move nothing.
- **"Agent" naming**: 56 open FT rows still say "Agent: sponsored step" (4 of them at step R, dropped by decision 230). 182 Activities say "Agent sent", the last on 15 Oct. Five prompts match both prefixes.
- **Draft learning loop (decision 102)**: drafts, Edit size, Template modes, the Send draft status and the Friday template review. Zoya sends directly now, and Akshay's feedback reaches the wording page through the Mail issues database (23 rows). Two learning loops exist and only the second is fed.
- **Two decision inputs**: Your call (decision 157), plus instructions typed into Next action "until 26 Oct", plus Tier set by hand (decision 112).

### Notion

- Home page: cards for two databases that are in the trash (WhatsApp blurbs, Whatsapp Group Members). No card for the public Members directory or the Decisions database. The Templates card says "until Zoya's rules go live". The FT guests count says 566; it is 661.
- Under Rules for Zoya (a Controls page agents read every run): three dated snapshots (Routine audit 16 Oct, Mail feedback 15 Oct, Background). Calendar rules (Controls) carries a "Today's audit (15 Oct)" section.
- Zoya routine 6 holds a second, different copy of the release mails that are on the wording page.
- Dead databases with no card in section 5: Guest evals (66 rows), Tasks (3 rows, newest 5 Oct), Queue. Not yet migrated: HBD Guest Outreach (113), SEA VC Outreach (13), FT Guest Outreach (0).
- Root-level leftovers: "Business OS" (audits), the context brief, CRM Build Plan, two inbox-triage databases, a second "Tasks" template database, My Tasks, Docs, Projects, Substack Posts Audit.

### Repo docs

| File | Size | State |
|---|---|---|
| decisions.md | 113 KB | live, but the Notion Decisions database (237 rows) is now a second copy with its own status column |
| notion.md | 102 KB | a 238-line migration log; its "workspace map" lists the dropped dashboard and the Queue, and misses 10 databases |
| schema.md, statuses.md | 20 KB, 12 KB | drafts of 30 Sep and 5 Oct; Notion is the real schema |
| automation-plan.md | 7 KB | a list of routines, duplicated by the developer page |
| email-automation.md | 4 KB | the decision 102 plan |
| handoff.md, handoff-ft-email.md | 4 KB, 3 KB | handoffs of 8 and 9 Oct |
| mac-tasks.md | 1 KB | overlaps akshay-pending.md |
| architecture.md | 8 KB | version 1 of 30 Sep |
| migration-sources.md, audits/ | | history; keep |

### Decisions

237 rows: 176 In force, 57 Superseded, 3 Open, 1 row malformed (no. 99 lost its columns). On top of the 57, these are **in force on paper but replaced in practice**:

| No. | Says | Replaced by |
|---|---|---|
| 9 | Emails send once Akshay approves | standing sends (164, 207, 227) |
| 102 | Draft, learn, then send | Zoya and the Mail issues loop (194) |
| 112 | Akshay decides by setting Tier | Your call (157) |
| 134 | Status Send draft | drafts retired with 102 |
| 159 | Sponsored commercials template on Send | Zoya handles sponsored (227) |
| 164 | "Noted with thanks" sent by inbox | Zoya (207) |
| 167 | Mamatha off FT, outbound at New | 211 |
| 187 | Host boards sync from the inbox routine | proposal below |
| 205 (in Calendar rules) | Akshay in Cc until 25 Oct | 229 |
| 233 | Re-audit before the first 8am runs | done 16 Oct |

## Part 2. Target design

### One source of truth per concern

| Concern | Single source | Who edits it | Read by | Retired |
|---|---|---|---|---|
| Who gets which mail, when, from which address and voice | **Rules for Zoya** (Notion), widened to all agent mail | Akshay, and Zoya applying his feedback | the one sending routine | sending rules in inbox, calendar and sweep |
| The words of every mail and WhatsApp | **Mail and WhatsApp wording** (Notion): every mail, with a header line (sender, show, trigger, live or off) | same | the one sending routine | Templates database (to section 5); Zoya routine 6's copy of the release mails |
| Calendar rules | **Calendar rules** (Notion), snapshot section removed | Akshay | calendar | |
| Row rules: Waiting on, Next action, Next date, Claude note, Last activity, the status ladder, one closing rule | **Data rules** (Notion, today "Describes", becomes Controls) | developer, agreed with Akshay | every routine | NEXT DATE AND WAITING ON, FLAGGING, TEAM ROLES and three closing rules in four prompts |
| Plumbing: tool names, data source ids, inbox ids | **repo** routines/shared/, included into prompts by a build script | developer | compiled into every prompt | hand-copied NOTION blocks |
| Decisions | **docs/decisions.md** (agents write it, git keeps history); Notion Decisions database is a mirror regenerated from it | sessions | sessions, Akshay | status kept in two places |
| What runs, when | **Business OS developer** page, Routines | sessions | Akshay | automation-plan.md, cowork-tasks.md |
| What's pending on Akshay | docs/akshay-pending.md, mirrored on the developer page | sessions | Akshay | mac-tasks.md |

The split between Notion and repo is deliberate. Anything Akshay changes (who, when, wording, calendar rules) lives in Notion and is read at run time, so his edits take effect without a prompt push. Anything only a developer changes (ids, tool names, step logic) lives in the repo, gets compiled into the prompt, and is checked byte for byte when pushed.

### One job per routine

The core change: **capture, decide, act.** Capture routines write what happened and what's due. They never send. One routine sends everything.

| Routine | Job | Sends? | Target size | Now |
|---|---|---|---|---|
| Inbox | Mail to Activities, People, Engagements and Deals. Classifies each thread and writes the step due ("Zoya: holding reply", "Zoya: Akshay's Tier 1 mail"), never the mail | no | ~22 KB | 65.5 KB |
| Calendar | Calendar to Notion and back, prep entries, audit, did the call happen, blurb. Writes the thank-you, day-before and double-booking steps for Zoya | no | ~24 KB | 39.4 KB |
| WhatsApp | WhatsApp to Activities, FT Community, public directory mirror | to Akshay's own chat only | ~11 KB | 11.8 KB |
| **Zoya** (the outbox) | Sends every agent mail and team WhatsApp, in her voice from zoya@ or in Akshay's from ad@, as the rules and wording pages say. Handles Your call. | yes, the only one | ~28 KB | 20.1 KB |
| Daily sweep | Hygiene: settle rows from Gmail, one closing rule, quiet and missing flags, revenue safety net, FT guests list, billing forwards to Jaya | forwards only | ~16 KB | 39.1 KB |
| Host boards (new, split out of inbox) | un#, B2S, HBD boards both ways | no | ~5 KB | inside inbox |
| Evals, dossiers (Cowork) | unchanged; remove their Templates read | no | | |
| Salesblink, Community directory | unchanged; directory drops its copy of the mirror rules and does City only | no | | |

The inbox's holding reply goes out about 30 minutes later than today, at the next Zoya run, not inside the inbox run. That is the one behaviour cost of this design. It buys one sending path with one rulebook, one cap, one bounce check and one context check.

Zoya sending Akshay's own mails from ad@ is what a chief of staff does, and her prompt already does it for the joining mail and the sponsored close. The wording page marks which mails are Akshay's voice. Mail never introduces her, and she never writes in Akshay's voice except the mails marked his.

### What moves where

| From | To |
|---|---|
| Inbox STEPS 6, 6a, 6b, 6c, 6d, 6e (send parts), YOUR CALL, WHATSAPP TO AKSHAY | Zoya's queue steps; wording to the wording page |
| Inbox 7d host boards | new Host boards routine |
| Inbox 2b, sweep 3e and 6b, TEMPLATE MODES (draft learning) | retired; the Mail issues loop stays |
| Inbox 6f loop-in | removed after its 17 Oct run |
| Inbox 7c | removed (the Cowork evals task runs every 25 minutes past) |
| Calendar 3b day-before, 4c thank-you, 2 declined-invite, 1b double-booking sends | Zoya steps (calendar writes the step and the data, Zoya sends) |
| Sweep 3f sponsored nurture | deleted (Zoya routine 1 owns it) |
| Sweep STEP 1 Queue | deleted; Queue to section 5 |
| Sweep 6 Mamatha's list | Zoya, for the shows Mamatha still runs |
| Every TEAM ROLES, MAMATHA IN CC, ZOYA IN CC, ZOYA LIVE, BEFORE ANY SEND, LINKS, TEMPLATES block | Rules for Zoya (once) and Data rules (once) |
| "Agent sent" and "Agent:" matching | one rename upload (56 rows, 182 Activities), then "Zoya" only |
| Templates database | section 5 once the wording page holds every mail |

### Retire

- **Repo routines/**: move evals.md, dossiers.md, community-invite-kit.md, un-eval-refresh.md, cowork-tasks.md, transcripts-backfill.md, transcripts-blue-youtube.md and tools/make_eval.py to routines/retired/. Keep add-guest-names.md, transcripts-after-recording.md and zencastr-mac.md under routines/mac/ and routines/tools/. feedback-call.md and tasks.md move to docs/ as specs.
- **Repo docs/**: handoff.md, handoff-ft-email.md, automation-plan.md, email-automation.md, mac-tasks.md, schema.md and statuses.md to docs/archive/. notion.md becomes a one-page map (every database, id, purpose); its migration log moves to docs/archive/notion-migration-log.md.
- **Scheduled tasks**: delete the four disabled ones (old evals, old dossiers, B2S sheet sync, FT Article Queue). Ask Akshay about FT Newsjack, which runs outside the OS.
- **Notion, section 5**: Templates (after cutover), Queue, Guest evals, Tasks. Remove the two trashed-database cards. Move the three snapshots under Rules for Zoya and the "Today's audit" section of Calendar rules to an Archive page under Business OS developer.
- **Decisions**: mark the ten rows in the table above Superseded, fix row 99, one Notion AI upload.

### Pushback on earlier calls

1. **Mamatha in Cc on every mail (decision 132).** She has no Founder Thesis rows and is asked to do nothing with the mail. On FT this is noise in her inbox, plus a rule restated in every prompt. Proposal: drop her from FT and vendor mail; keep her on the shows she runs.
2. **Three ways to decide a guest** (Your call, typed Next action, Tier). Only Your call is unambiguous; the other two need the "is this text his or a sheet note?" guessing that takes 2 KB of inbox prompt. Proposal: from 26 Oct, Your call only. Tier stays a field and picks the template, but setting it no longer sends anything.
3. **Draft, learn, then send (decision 102).** It made sense when agents drafted and Akshay sent. Now Zoya sends, and Akshay's corrections go straight to the wording page. Proposal: retire the draft loop, the Send draft status and the Friday template review.
4. **Host boards in the inbox (decision 187).** It was the right call for frequency but the wrong place. Its own small routine runs just as often.
5. **Akshay in Cc on all of Zoya's mail (decision 229).** That's fine while he is checking her, but it needs an end date. Proposal: review on 30 Oct.

### How we get there (each step pushed, verified live = repo byte for byte, and announced to the other sessions)

1. **Safe now, no behaviour change:** Templates rows "Eval ready" and "Short-form and collab answer" to Mode Off. Delete the dead text: sweep 3f, sweep STEP 1, every Mamatha backlog clause, inbox 7c. Fix Calendar rules' Cc line. Archive the repo files and docs.
2. **Shared rules:** write Data rules (Controls) and widen Rules for Zoya to all agent mail. Build script and routines/shared/.
3. **Wording:** move the 14 differing and 12 sign-off-only Templates rows onto the wording page, each with a header line. Inbox, calendar, sweep and evals read the page. Templates to section 5.
4. **Zoya becomes the only sender:** her prompt takes the queue steps from inbox and calendar. Run it for one day with inbox still sending, comparing what each would send. Then cut inbox and calendar sending in the same push.
5. **Inbox rewrite** (target ~22 KB), host boards split out, sweep rewrite (~16 KB). un# goes live on the rewritten prompts, not the old ones.
6. **Rename "Agent"** to "Zoya" by upload. Then the home page, the developer page, and docs/decisions.md with the new decisions.

Agents can't delete Notion pages or rows. The deletions list for Akshay comes with step 6.
