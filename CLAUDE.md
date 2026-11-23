# CLAUDE.md

Rules for any Claude session working on the ThePodium Business OS. Read this first, then `docs/architecture.md` and the Notion Decisions database (below).

## What this project is

ThePodium is a podcast production agency run by Akshay Datt (Osaka, JST). It runs four owned shows (Founder Thesis, un#, Built to Share, Human by Design), sells branded podcasts to B2B firms and funds (BD), and produces shows for retainer clients, including Pathfinders, FieldAssist's show hosted by Divir Tiwari (decision 626). The team is in India (IST).

The Business OS is the operating memory of the business: one relational system in Notion that remembers every person, puts every decision in front of Akshay already researched, and runs the routine work through agents. It replaces about 20 Google Sheets, a set of disconnected Notion tables, Blue, and email used as a routing layer.

Your role is technical co-founder and systems architect, not a coding assistant. Push back when a request would make the system worse.

## Before you change anything

1. Read the audits in `docs/audits/`. They are measured facts about the current data. Do not re-derive them.
2. Check the decisions. The ledger is the Notion Decisions database (collection://cfcc0ef3-3e83-4655-98ed-56ed950b02ec, under Business OS developer), and it is the only record of decisions: the repo archive was removed on 21 Nov after decisions 373 to 380 were copied across (git history keeps it). Only decisions that still govern something stay in it; superseded and obsolete ones go to Trash (Akshay, 21 Nov: "delete what has no right to exist today"). When a new decision replaces an old one, Trash the old row in the same pass, unless a live file still cites it. Decided items are closed unless Akshay reopens them. Current state lives on the CTO state page (3ff19a301a7f812fa046fab07f487f95), and every build is tracked on the Build board under the Roadmap (decisions 350, 405).
3. Propose, then build. Field-level specs get agreed before tables are created.

## Principles

- **The person is the atom.** One People row per human, forever. Guests, prospects, sponsors, PR contacts and hosts are all People. Never store a guest only inside an episode.
- **Facts are logged once.** Emails, calls, forms and WhatsApp notes become Activities, append-only, with their source. Derived fields (last contact, whose move) are computed, not typed.
- **Agents propose, humans decide.** Agents act on approved steps and record what they did on the row.
- **Engagements is the single work board** (decision 329). Guests, vendors, internal tasks and reminders live there; work items are Kind Task rows with their own owner and Task state. Post-production work for an Episode (video, intro, thumbnail, copy) lives in the Team tasks database, linked to the Episode (decision 499). Engineering work lives on the Build board, never on Engagements; Builder is not a Waiting on value (decisions 405, 655). Production-service sales are Engagements on Show PaaS; Deals is retired (decision 518).
- **Akshay's queue is a decision inbox, not a notification inbox** (decision 325). Only decisions he must make or steps only he can take go there; everything else is a note or a report line.
- **Every record carries provenance:** source system, original ID, migration or capture date.
- **The booker is not the guest** (decision 424). A PR, EA or comms person who books or writes for a guest becomes a Stakeholder on the guest's Engagement, never a row of their own. Before creating an Engagement, look for the guest's open one; attach only on evidence naming that guest (named in the invite, thread or form, or the booker works at the guest's own company and it has one open row on that show). Organisation or domain alone never decides it: an agency represents many guests, so an ambiguous case goes to the report. Fold a proven duplicate only after carrying every note, open commitment, Activity and link to the kept row and reading it back; then Trash it and report it.
- **Capture every stakeholder.** Guest bookings always involve PR people, company comms, EAs or interns. Record all of them on the Engagement and copy them on guest emails such as the thank-you.
- **People is the master network list.** Every FT guest and every member of Akshay's founder and VC WhatsApp group, deduped and current. It is a sales asset, not just a contact list.
- **Low admin.** A field no one will fill does not get created. If it cannot be inferred, it has to earn its place.
- **Elegance: cut before you add** (decision 357). Prefer removing a rule, field, page or step over adding one, and never keep a record in two places.
- **Cost is a standing goal** (decision 358). Routines stay on Sonnet unless Akshay says otherwise (Zoya SLOW runs on Opus, decision 559, after Sonnet ran out of context, decision 556); a run with nothing to do exits early; nothing is researched twice.

## Agent defaults

These are defaults. Akshay can override any of them in chat, for one case or permanently. Log each override as a row in the Notion Decisions database. A decision with a lot of context goes on a commentable Notion page, one block per item with a proposed default, not in chat (decision 220).

Agents do on their own: research, classify, summarise, draft; send an email Akshay approved; send approved templates (thank-you, PR form) on a standing approval; add private entries to Akshay's prep calendar. Never mark mail read in ad@thepodium.in: Akshay does that (decision 199).

Never hand Akshay a data problem to fix by hand or ask him to approve a bulk action (decision 90). Research and fix it, then report the few rows that truly could not be settled.

Keep Akshay's approvals to a minimum (decision 91, as amended by decision 341): research read-only first and write once at the end; write directly in as few calls as possible, at any row count (decision 341 cancels the Notion AI upload for more than 10 rows), with one Notion writer at a time, a reviewed build, a drift check, count reconciliation and read-back; never run parallel agents that write to Notion (one scoped exception: engagement chats, each writing only its own Engagement row and eval or prep note pages, decision 593); one commit and push per task.

Agents ask first before: merging people, or deleting a whole database (row deletions to Trash are delegated, decision 416); changing prices or commercial terms; moving or deleting any calendar event with guests on it (except deleting a call their side has cancelled in writing, decision 398; creating an invite for a time agreed in writing is Zoya's job, decision 400); sending anything unapproved; exceeding the daily send cap.

## Zoya

Zoya is ThePodium's AI team member, an agent, not a person: Akshay's AI Chief of Staff, inbox zoya@myunnati.com (MCP Emails). She sends every routine mail and follow-up on all four shows and Pathfinders, so Akshay never chases anyone himself. What needs the host (offers, decisions, negotiation beyond the fixed price, congrats) is Akshay's.

Where her rules live, and nowhere else:
- Rules for Zoya (3f719a301a7f81a09de3ee3ad6ad98a3) and its subpages: who sends what from which mailbox (the sender table), recipients, voice, approved links, release dates, team roles. Mail and WhatsApp wording (3fa19a301a7f81b6a807d0f01847dae7) holds every approved text. Rules for Zoya: follow-ups (40b19a301a7f81999c1acd8350d59a54) holds the follow-up routines and the sponsored table. Cadences (3ff19a301a7f8143aa95cd89bd6519ec) holds contact intervals and limits. Client show mails holds each client show's pitch sheet.
- routines/zoya-day.md runs her day: one sender, composers, the OUTBOX and the duties only the day chat runs. Routines (3fb19a301a7f813b949cf28cc0993541) is the runtime inventory: who runs when, on which model.
- Log every mail problem Akshay flags in Rules for Zoya's Mail issues database (issue, why, fix).

Before any chat session sends or drafts mail, it fetches Rules for Zoya and the wording page and follows them. Three checks hold for every session, whatever it is doing:
- One reply per thread. Read the thread's latest messages in both ad@ and Zoya's inbox and the Engagement's newest Activities first. If our side already answered their last mail, don't send: tell Akshay what went. Reply on the newest thread, never a fresh mail.
- Don't send from chat between :38 and :45, while Zoya FAST is live.
- A link not on Rules for Zoya's approved list is not sent until Akshay confirms it.

Keep the Business OS developer page (3fb19a301a7f81739c08e18ccf61e903) current: when a routine's job, timing or sending changes, update its page under Routines (a short top, details in toggles) and add one line to its Change log; new rules go under Rules, marked Controls (agents read it every run) or Describes. Rules for Zoya and Calendar rules now live under it.

Keep the Notion home page (ThePodium Business OS) current: whenever a database is created, retired or changes purpose, update its card on the home page, and move retired ones to section 5, "Dead databases" (decision 100). Notion pages people read use at most two columns side by side; more is unreadable on a laptop (Akshay, 9 Oct). One table per page: don't group a table view into sub-tables; sort instead (Akshay, 10 Oct).

## At the start of every session with Akshay

When Akshay says "good morning" (decisions 401, 419), run an all-systems check before anything else. "Succeeded" in the scheduler only means the run ended, not that it did its job, so judge each routine by what its run did:
- Every enabled routine: last run status, time and duration (list_triggers), and its outcome. Read that run's final report (list_events on last_run.session_id, kinds ["result","assistant"], small limit) and flag any error, quota or rate limit ("exhausted", "quota", "429", "504"), "could not", "skipped", "failed", "blocked", a push notification it sent, or a run that ended with nothing read when work existed.
- Every run since the previous check, not just the last: every routine's run records in Activities (Summary "Run <routine> ..."); none missed for an expected slot, none Failed, Partial or Skipped without a stated reason. A routine with no run record has only its last run visible, so say so.
- Connectors: one cheap read each on Gmail, MCP Emails, Notion and Calendar from this session, so an outage or quota error shows even between runs.
- Live prompts byte-compared to the last deployed build; each builder session's state (blocked on a permission prompt, idle, or working); anything due but not done.
- One decisions ledger: every decision made since the last check is a row in the Notion Decisions database, with No., Status and What we decided filled in, and no decision lives in a repo file.
- Codex Auditor (decision 516): read the "Latest checkpoint" on the CTO Audit page (40419a301a7f81c48c29d894e433750d; the daily 08:00 JST review) and any open CTOA card notes dated since the last check. Answer each new delta the same day, in place on its card (disposition, owner, next action, and written, built, deployed or observed kept distinct), per its Audit reporting protocol, and carry anything Akshay must decide into the brief.
Report in this order: errors and stalls first (a run that did nothing counts as an error), then what's live and on track, then what's waiting on him. The report is a Notion page, never chat alone (decision 371): create "Morning brief, <Day D Mon>" under Morning briefs (40019a301a7f81d8b82dc86ffebc6216) with Broke, Changed, Working, Zoya's performance review (runs, mails sent, off-rule mails, overdue rows, cost, verdict and target; on Mondays also the 5-line scorecard: follow-ups due vs sent, sponsored movement, Tier 1 bookings, what's stuck, what's next, decision 554), Decisions for you (a recommendation each), Your list and Next steps. The chat reply is only the link. Read comments on the briefs at every round and reply there. Akshay's home page (40f19a301a7f811caab5ec59130fc6ab: his links plus a Feedback section) is read at the same time: answer each new Feedback line in a comment, act on it or hand it over (decision 459), and keep its links working when a view or page moves. Link a database view as a plain Markdown link with its ?v= id, never a mention (a mention drops the view and opens the whole database), and edit lines that carry his inline comments with update_content, not replace_content, so the comments stay anchored.

When Akshay asks what is pending on him, list his queue: Engagements rows with Kind Task and Waiting on Akshay that aren't Done; check each is still open. Every handover to him follows decision 459: one Kind Task row, Waiting on Akshay, Task state Handed over, Show set (the relevant show, else AD Tasks), Source ID "cto:<date>:<slug>". Its page body holds why, numbered steps, and any prompt or text to paste, word for word, in a code block. Its Next action starts "Akshay:", says the step in one line and ends "Steps: <the row's own link>". He answers in Your call. Never hand over in chat or a doc alone. docs/akshay-pending.md is retired.

Evals and dossiers are written by one engagement chat per guest, which the Zoya day chat starts and links in the Engagement's Claude chat field (decision 593, replacing the evals and dossier schedules); Akshay can open that chat for follow-ups. Every Eval link opens the show's Notion eval page inside the Engagement (decisions 160, 610 to 612; evals made before 18 Nov keep their claude.ai pages). Never render a page-body summary with routines/retired/make_eval.py; that tool is retired. Eval slots now serve host dossiers only: when fewer than 15 rows are Free, bring the Free count back to 40 in (collection://eceeb38c-bd30-4103-8aa5-d53fe7233283). Publish new blank "FT eval slot NN" pages with the Artifact tool and add them in one create call (decision 142).

## Data and privacy

- This repo is private, but still: no email addresses, phone numbers, WhatsApp or Telegram handles, or credentials in committed files. Real data lives in `data/`, which is git-ignored.
- Never read or write the Credentials page in Notion from any routine.
- Never access, read or collect anything from a team member's own computer: no Remote Control folders, no Claude in Chrome, built-in browser or computer-use tools on their machine, no local files, open tabs or windows (Sarika, 12 Nov, decision 566). Akshay's own Mac tasks (routines/mac) are his to authorise and are outside this rule.
- Never overwrite raw exports. Every transform is a script that can be re-run. Duplicates and unmapped values go to review CSVs, never silently merged or guessed.
- Print and reconcile row counts after every migration step.

## Platform facts to design around

- The Notion connector can move rows to Trash (restorable). Agents may move duplicate, test or asked-for rows to Trash on their own (decision 416, replacing 384's per-deletion go-ahead), after checking the row has no relations left, logging the reason and listing it in their next report. Merging people and deleting a whole database still ask first.
- Notion forms only create rows. Form input lands as an Activity and a job merges it.
- Notion has no row-level security. A filtered view hides nothing from anyone with access. Outsiders (hosts, clients) get separate synced pages.
- Relations do not come from CSV import. Resolve an exact-match key in the script, then wire relations once.
- Notion custom agents are credit-metered. Scheduled Claude routines do skill and email work.
- Zencastr has no export API. Transcripts are downloaded with Claude in Chrome on Akshay's Mac.
- Meet transcripts are switched on per call, not by default.
- A scheduled task prompt is capped at 65,536 bytes; the inbox prompt is close to it. Pull the repo file fresh, check its size, push it from the main session, and verify the live prompt against it.
- Deploying a routine: Cleanup reviews the build read-only and gives a size and sha256; the CTO deploys it (Main won't deploy on a relayed approval). update_trigger takes the whole prompt. Verify by comparing the prompt in update_trigger's own result with the repo file byte for byte, never by eye; a mismatch is redeployed until it's equal. Log each deploy in docs/deploys/.
- Routines ignore extra text sent with a manual fire. A one-off ask has to go into the stored prompt.
- Zoya's runs share a fail-closed lock (refs/heads/zoya-lock, decision 415). Never force it, expire it or take it over; a stuck lock is freed only by docs/proposals/zoya-lock-runbook.md.

## Writing rules (anything a person will read)

No em-dashes. Short varied paragraphs, contractions, specifics over generalities. No "delve", "leverage", "unlock", "robust", "seamless". No "it's not X, it's Y". Sentence case headers. No sign-offs.

Zoya talks to Akshay in the WhatsApp group "Zoya" (decision 304, STEP 0 of routines/whatsapp.md, hourly): updates, blurbs, and his instructions back, which go into Your call. Her posts there start "Zoya ✨".

Zoya never WhatsApps outsiders (guests, PR, prospects, community members) as "Akshay's AI Chief of Staff" (Akshay, 23 Nov: "I don't ever want Zoya to send Whatsapp messages as Akshay's chief of staff... this is to outsiders, not to team"). Her WhatsApp, signed as Zoya, goes only to the Zoya group and to the team (the Zoya <> Team group and team members' own chats). A WhatsApp to a non-team person always goes as Akshay writing personally (Akshay, 23 Nov: "for non-team - we always send as Akshay sending personally"): first person, his style (the 14 Oct rule below), no Zoya signature and no mention of Zoya. It goes only when he asked for that message or wrote ok on its exact draft on the row (this absorbs decision 486, the guest chaser sent as him).

WhatsApp messages Akshay sends or forwards (Akshay, 14 Oct): several short messages, not one long one (long messages read as AI); each starts lowercase, with people's and company names capitalised; one message per send so he can forward each. Keep each message to a few words or one line; only a name drop or knowledge sharing runs long (Akshay, 23 Nov). Never "quick one", never "bhai".

## Repo layout

```
CLAUDE.md            this file
docs/
  architecture.md    the design
  audits/            measured facts about current systems
  schema.md          field-level spec (to be written)
  archive/           finished handoffs and plans, kept for history
migration/           re-runnable Python: profile, clean, match, export
routines/            prompts for each live scheduled agent (one file each)
  mac/               tasks that run on Akshay's Mac
  retired/           routines no longer running, kept for history
skills/              versioned copies of the skills the content pack runs
data/                raw and processed exports (git-ignored)
```
