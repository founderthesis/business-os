# Rulebook r1: change map

Batch 1 covers the nine examples on the audit page (42019a301a7f81eb82d0cc814724b24e) plus the conflicts found on the way. Nothing here is live. The CTO cuts over; Cleanup reviews.

How the staged rulebook is built:
- Prompts: `build.py` takes the pinned bytes (`git show 83e8fb0:` for the six routine prompts, `63d63ec:` for the SLOW work file), applies `edits.py`, and writes `prompts/` and `manifest.json` (sizes, sha256, source hashes). Every edit must match exactly once or the build fails. `build.py --check` reports drift.
- Notion: `notion_edits.py` holds the edits as address-free anchors; `apply_notion.py <fresh fetch dir> <out dir>` applies them to a fresh fetch at cutover and fails on any miss. Output stays out of git (the pages carry mailto links).
- `routines/zoya-day.md` is a rewrite, not a patch. `claude-md/CLAUDE.md` and its `.diff`, `seeds/composer-seed.md`, `decisions-edits.md` are the other staged files.

## Before and after (bytes, or characters for Notion)

| Source | Before | After | Note |
|---|---|---|---|
| routines/zoya-day.md | 49,523 | 26,760 | No override section; duties only the day chat runs |
| CLAUDE.md | 27,140 | 18,280 | Zoya section points to the rule pages |
| zoya-fast.txt | 62,996 | 59,851 | Under the 60,000 target. Recipient rule moved to Rules for Zoya and checked in code; Mamatha and Sri clauses replaced; minute-25 logic, the links list and the duplicate-fold detail removed |
| zoya-slow.txt | 15,646 | 15,194 | Schedule, work-file pin stamped at release |
| zoya-slow-work.txt | 94,833 | 94,524 | Sponsored, pauses, recording chase, transcripts; owner mail and its keys removed |
| calendar.txt | 62,916 | 63,120 | Ranjita, no Builder, no delete_event on guest events |
| inbox-capture.txt | 50,812 | 50,913 | Team roles, recipients |
| inbox-actions.txt | 48,515 | 48,576 | Team roles |
| whatsapp.txt | 39,817 | 39,820 | Mamatha |
| host-boards.md / editing-checks.txt / cowork-evals.md | 9,357 / 8,925 / 15,198 | 9,209 / 9,067 / 15,121 | Mamatha, dated branches, B2S/HBD hand-offs to Zoya |
| daily-sweep.txt | 50,569 | retired | Its live steps: upkeep.txt, 35,929 (S17) |
| Rules for Zoya (Notion) | 66,758 | 62,886 | Release table, sender table, full links list, standing checks; hold, 25 Oct corrections, Mamatha section, transcript-by-mail, Gmail-connector line removed |
| Cadences | 9,540 | 5,847 | Old timetables removed; sponsored rows rewritten |
| Rules for Zoya: follow-ups | 17,074 | 18,949 | Sponsored and pause table added; nurture branch for sponsored removed |
| Mail and WhatsApp wording | 91,251 | 76,917 | Retired toggles, the Retired section, the sweep's Mamatha list and the un# pre-release ask removed; Release v3 marked live on un# |
| Routines | 4,001 | 3,004 | One runtime inventory replaces the historical overview |

FAST and SLOW work both shrink: the recipient rule lives once, on Rules for Zoya section 2 (read in full every run), and each prompt runs its check in code before every send.

## Subjects

### S1. Parking authority
- Authority: decision 656 (Akshay, 22 Nov: "don't park any engagement without my go ahead").
- Losing clauses: day file lines 45-48 and 98 (618's 7-day park), 104 (625's park after check-in); Cadences FT sponsored "then Parked"; Rules for Zoya "anyone else, Park with the reason" (366) and "We declined (33) and Parked (34)"; follow-ups 5a revival start by the sweep.
- Final wording: PARKED in edits.py (`STATUS_AUTHORITY`), written into FAST and SLOW work. Only Akshay parks; their side's no is They declined; a chase that ends goes on the weekly Park proposals; a blocked step keeps its date.
- Consumers: zoya-fast.txt, zoya-slow-work.txt, zoya-day.md (weekly Park proposals duty), Rules for Zoya, Cadences, decisions 366, 573, 618, 625, 656.
- Verify: fixtures F04, F05.

### S2. Sponsored eligibility, limits and stops
- Authority: 227, 237, 367, 422, 573, 618, 625, 656; Akshay 22 Oct on un# ("at max 2 follow ups and then kill it").
- Losing clauses: Cadences FT row ("then Parked" and "Silent for 60 days: moves to nurture" in one cell); follow-ups routine 1 ("Give us time doesn't [stop]", silent leads to nurture); 5a's "sponsored offer silent past the limit" branch; SLOW work STALENESS GATE "60 silent days on sponsored"; Rules for Zoya "Sponsored stops only on their no ... silence never stops it".
- Final wording: one table, follow-ups section 5c (`SPONSORED_TABLE`), plus the pause table. SLOW work's routine 1 and UN# SPONSORED point to it; sponsored rows never move to nurture.
- Consumers: Cadences, follow-ups, zoya-slow-work.txt, decisions 367, 573, 618, 625.
- Verify: F01, F02, F03. Open: questions 2, 4, 5.

### S3. Recipients for FAST, SLOW and OUTBOX
- Authority: 229, 586, 592, 643, 646, 647, 658 (one draft update to fix recipients).
- Losing clauses: FAST and SLOW work read-back list (Sri and hosts dropped unless they wrote; Mamatha kept if on the thread, 489); PRE-SEND CHECKS 2/; un# and B2S/HBD "never in Cc unless he wrote"; the separate Cc paragraph; day file 79 (586/647 override), 73 (643), 90 (592), OUTBOX 2a "never edit, delete" (against 658's one update); inbox-capture's loop-in Mamatha clause.
- Final wording: RECIPIENTS in edits.py, one definition with its Bash check, in FAST and SLOW work; every send path names it, OUTBOX included.
- Consumers: zoya-fast.txt, zoya-slow.txt, zoya-slow-work.txt, inbox-capture.txt, zoya-day.md OUTBOX, decision 647.
- Verify: F06, F07, F08.

### S4. Ranjita's roles
- Authority: 646 (Akshay, 21 Nov: "mamatha is on long break, Ranjita will replace her - direct all mamatha tasks to ranjita"), 558, 644.
- Losing clauses: day file line 70 ("wherever a prompt says Mamatha, read Ranjita"); FAST STEP 0r and ROOM ASK to Mamatha; SLOW work TRANSCRIPT ASKS by mail to Mamatha with follow-ups; calendar's transcript segments; "Nothing waits on Mamatha" in five prompts; Rules for Zoya "Zencastr link and transcript from Mamatha" (439) and its Cc line; Rules section 6's WhatsApp list without Ranjita.
- Final wording: TEAM ROLES in edits.py; Ranjita named directly in every step. Real past correspondence is untouched.
- Consumers: all six prompts, SLOW work, zoya-day.md, Rules for Zoya, decisions 352, 439, 456, 489, 646.
- Verify: F09, F10. Not yet done: six Mamatha mentions in wording toggles (batch 2).

### S5. ad@ send and read permissions, and allowed forwards
- Authority: 420, 423, 435, 574, CTO 20 Nov (MCP Emails draft on ad@ stops on a permission prompt), 658.
- Losing clauses: Rules for Zoya section 2 "Akshay's automated mail goes through the Gmail connector"; decision 235 text; FAST/SLOW loop-in "always the draft way" on ad@ and NO COMPOSE REPLY "from either inbox" (against the day file's email_compose reply); Rules section 1 naming only the billing forward.
- Final wording: one sender table on Rules for Zoya (mailbox, who, action, tool, approval); NO COMPOSE REPLY scoped to Zoya's inbox; the loop-in uses email_compose reply with To and Cc passed and checked.
- Consumers: Rules for Zoya, FAST, SLOW, SLOW work, CLAUDE.md, decisions 235, 420, 423.
- Verify: F11, F12.

### S6. Sweep retirement and the SLOW schedule
- Authority: 657 (sweep retired; SLOW 11:08 and 17:08 weekdays).
- Losing clauses: day file composer branch "Zoya SLOW or the daily sweep"; SLOW prompt's seven slots (546); follow-ups "10:38 and 16:38"; Cadences' historical timetable; Routines' historical overview; SLOW work REVIVAL "after the daily sweep moved it"; composer seed.
- Final wording: zoya-day.md table and SLOW composer bullet; Routines' runtime inventory.
- Obligations the sweep carried that need a current owner (for the CTO, not a policy question):
  | Sweep step | Proposed owner |
  |---|---|
  | 3r Tier 1 revival start | SLOW (staged) |
  | 3i Episodes without a transcript | Day chat (decision 644 duty, staged) |
  | 6c Billing and invoices forwarded to Jaya (an allowed ad@ forward) | upkeep.txt STEP 6c (staged) |
  | 7b Guest form submissions merge | upkeep.txt STEP 7b (staged) |
  | 3g Founder Thesis guests list (podm.in/guest-list) | upkeep.txt STEP 3g (staged) |
  | 3k FT Community rows for recorded guests (backstop) | upkeep.txt STEP 3k (staged) |
  | 3p BD prospect episodes to PaaS rows | upkeep.txt STEP 3p (staged) |
  | 3h Auditor handoffs to Task rows, fix checks | Auditor items go to the CTO and the Build board (655); fix checks: upkeep.txt STEP 3h (staged) |
  | 3, 3a, 3a2, 3a3, 3a4, 3b, 4, 4b, 5 (data upkeep, owners, flags, due vs done) | 4, 4b, 5: upkeep.txt (staged). 3, 3a, 3a2, 3a3, 3b: the day chat's row tidying (588) and inbox actions. 3a4 one-time moves: ended |
  | 2 Decisions sync | Retired: the ledger is Notion (350) |
  Also STEP 3d, client-show pre-release drafts for Built to Share and Human by Design: upkeep.txt (staged). upkeep.txt is cut by line number from the sweep's own text and run by the day chat once a weekday. No new schedule.
- Verify: F15.

### S7. Engineering work ownership
- Authority: 405, 655.
- Losing clauses: CLAUDE.md line 24 ("builder actions all live there"); calendar's Waiting on list with Builder and "Builder: delete the invite"; SLOW work's Mail issues "Waiting on Builder" row.
- Final wording: CLAUDE.md principle (Engagements, Team tasks, Build board); calendar and SLOW work send builder steps to the CTO session.
- Consumers: CLAUDE.md, calendar.txt, zoya-slow-work.txt, zoya-day.md, decision 329.
- Verify: F13.

### S8. One-off repairs and retired templates
- Saman Khan / Keshav Baljee reply (585): done, Activity "Zoya sent: reply to Saman (Consocia)" 13 Nov 23:54. Zoya date backfill (637): done, wake record 20 Nov 15:38 (122 Zoya dates set, 113 Next dates cleared). Both removed from recurring text.
- WisdomTree (Ryan Louvar, un#) hands-off: lifted by the CTO on 17 Nov and the recording happened on 18 Nov. Removed.
- Owner mail (619): SLOW work STEP 0f deleted. Other owner-mail references in SLOW work (batch keys, Mail issues "Needs Akshay not yet mailed"): batch 2.
- Wording page: 6 retired toggles, the "Retired: do not send" section, the sweep's "Mamatha's daily list" and the Templates database sentence removed. Old FT release toggles that Release v2 replaced: batch 2.
- Verify: F14.

### S9. Release-date authority
- Authority: 427, 514 (Sarika sets dates), 575 (hold lifted for the tentative week on FT post-recording chains), 582, 589, 601, 628, 630, 638 (Release v3 live on un# from 20 Nov).
- Losing clauses: Rules for Zoya's 30 Oct blanket hold callout; Rules section 1 "Release mail 1 ... Zoya (235)"; the live day file's "Release v3 is PROPOSED, not live", which contradicts 638 (the un# release has no executor in the live day file); the wording page's PROPOSED labels on v3; the un# pre-release ask toggle that v3 replaced; follow-ups' duplicate "Release week" paragraph; the sweep's STEP 3d covering un#.
- Final wording: the release-date table on Rules for Zoya (per show: before and after confirmation); zoya-day.md's release duty covering FT (v2) and un# (v3); upkeep STEP 3d for Built to Share and Human by Design until their v3 starts.
- Consumers: Rules for Zoya, wording, follow-ups, zoya-day.md, upkeep.txt, decisions 427, 514, 575.
- Verify: F16, F17, F20. No question left for Akshay.

## Other conflicts found (batch 2 unless noted)

| # | Conflict | Proposed resolution |
|---|---|---|
| S10 (staged) | Rules for Zoya's holding reply (390: "checking with akshay, will come back by <day>") against 571 ("hi <first name>, will get back to you on this", never "Akshay") and 418 (no deadlines) | 571's wording; rewrite 390's section |
| S11 | Rules for Zoya section 1 table: thank-you "Akshay by hand", Release mail 1 "Zoya (235)" against v2 | Release rows staged; thank-you row checked in batch 2 |
| S12 (staged) | Capture runs in a composer that sends nothing (653). The CTO checked: loop-ins still went (SK Minerals, Sujal/Novix and 12 more), sent by the day chat from the composer's report, by habit | Written down: the composer lists "loop-in due" lines; the day chat sends each right after the report with FAST's loop-in mechanics (zoya-day step 4, composer seed) |
| S13 (done) | "Book immediately: ask for recording slots" against 654 | Already fixed in routines/cowork-evals.md at db38ce7; the sweep's copy is retired; no skill routes to a slot ask |
| S14 | PRE-SEND CHECKS "every team address never in To" against team-only mail | Covered by RECIPIENTS 3/ (staged) |
| S15 (staged) | Rules for Zoya "System-audit corrections, 25 Oct" and "More rules (decisions 373 to 382)" restate and supersede older text | Staged: the two still-valid checks (reach claims, verified completion) kept as "Standing checks"; the rest already lives in its topic section or is obsolete (Zencastr Mac task, eval migration, Codex blurbs, which 652 replaced). The appendix is renamed and its 376 transcript-by-mail paragraph replaced by Ranjita's flow |
| S16 (staged) | Stored prompts: Sarika's editing asks (Mamatha transcripts, 456; Mamatha in the share list) and Host boards (Waiting on Mamatha or Chaandini; "until 19 Oct" branches) | Staged routines/editing-checks.txt and routines/host-boards.md; B2S and HBD host yes/no now hand the step to Zoya (decision 323) |
| S17 (staged) | The sweep's live steps had no owner after 657 | prompts/upkeep.txt, cut by line number from the sweep's own text plus 12 edits; the day chat runs it once a weekday |
| S18 | The CTO reminder for Monday's seed says "SLOW and the sweep back on" | Reported to the CTO, 22 Nov 20:00 JST |
| S20 (staged) | FAST WRITE PATH set Next date from Zoya's own segments, against 637; NEXT ACTION SIZE (438, 120 characters) against 588 (about 15 words); FAST's own holding line said "checking with akshay" (against 571); release-date and final-cut asks were routed to Akshay (against 427, 600) | WRITE PATH sets Zoya date for Zoya steps and Next date for people only; 588's rule; 571's line; 427 and 600 answered by Zoya |
| S21 | inbox-capture STEP 0 and 0A are one-off repairs ("every run until none is left", 1 and 2 Nov) still in the recurring prompt | CTO to check they find nothing, then batch 3 removes them |
| S19 | skills/notion-business-os: not installed, not referenced, carries Mamatha examples and the retired Deals board | Delete at cutover |

## Uninspected or unverified

- Cloud skills installed on claude.ai: unreadable from here. Their repo sources are listed in inventory.md; every installed copy is unverified.
- Stored scheduled-task prompts: read in batch 2 with list_triggers (read only).
- The live day chat's context: edits don't reach a running conversation; the cutover needs the daily rollover.

## Batch 3

| # | What | Staged |
|---|---|---|
| B3-1 | CTO coordination round stored prompt: quiet hours 00:30 (now 01:30, 547) in 2b; 2c's "v2 warm welcomes" toggle (Akshay, 22 Nov: the new blurb replaces the old in its section and the Blurb field; sources checked first; ft-community-blurb); 2d's standing Evals session (disabled; evals run in engagement chats, 593); "builders can't message you" (they can) | routines/cto-round.txt (full replacement) |
| B3-2 | Follow-up routine pages. Routine 1 (sponsored) was five stacked overrides ("since 19 Oct", "since 13 Nov ... overrides", "since 19 Nov ... overrides everything below") with mails 3 to 10 retired and a 7-day auto-park | Rewritten whole: 9,747 to 3,646 chars; points to the 5c table; only mails 1 and 2 |
| B3-3 | Routine 6 (release) still described the pre-v2 run (Mail 1 from Zoya, a 3-day task for Akshay, a +4-day nudge) | Rewritten whole as a pointer to the release table, the day duty and the v2/v3 toggles: 9,046 to 670 chars |
| B3-4 | Routine 3 (recording slot): override callout and "since" history; no precall-first rule (654) | Top rewritten with 594, 618, 654 |
| B3-5 | Routine 2: "anyone else is Parked (366)" twice; routine 8: PR-routed sponsored leads "then nurture while silent" | Park proposals; no nurture (5c) |
| B3-6 | Calendar rules: Zencastr links and transcripts from Mamatha (439); "the evals routine" re-runs the eval; the 15 Oct audit snapshot and the moved double-booking mail kept in the reading path | Ranjita (646); engagement chat (593); history sections removed (open questions kept) |
| B3-7 | Client show mails C15 to C17 still read as current for un# | Scoped to Built to Share and Human by Design until their Release v3; not un# (638) |
| B3-8 | inbox-capture STEP 0L ("through 2026-11-05"), 0A and 0 (one-offs, "every run until none is left"): checked 22 Nov, 0 allmail rows and 0 old unlinked rows | Removed with their run-record lines, order gate and windows; the REF lookup capture still needs is now written where it's used. inbox-capture.txt 50,812 to 42,288 bytes |
| B3-9 | Leftovers in prompts: Salesblink hold "ends 2 Nov" (SLOW work), "the evals routine" (calendar, actions), minute-25 machinery (WhatsApp, inside the day chat, 591), old deployment references (SLOW) | Removed or replaced |

Not inspected: Inbox and Your call rules beyond a keyword pass (nothing stale found), Rules index child pages "Rules for your inbox", "Rules for your Notion list", "Data rules", "Links and limits", "Blurb sources", "Episode asset filing", "Host board sync" (batch 4 if wanted).

## Cleanup review of 57aae30: fixes

| # | Finding | Fix |
|---|---|---|
| 1 | drop_section "Retired: do not send" ran to page end and deleted the live "Recording link" and "Release date (post-recording)" toggles | Only the heading and intro are removed; the 18 retired toggles go by marker. apply_notion.py asserts MUST_KEEP titles survive |
| 2 | Loop-in vs the recipient check (ad@ added in Cc to its own mail) | Rules for Zoya section 2 item 7: the loop-in rule (sender ad@, never in To or Cc, Zoya added). FAST and SLOW work pass idempotency_key "loopin:<Message-ID>" on email_compose and read ad@'s Sent copy after, asserting To, Cc and In-Reply-To |
| 3 | Day-chat sends could run before Rules for Zoya is loaded | zoya-day step 2 RULES GATE before any send (loop-ins, OUTBOX, Your call); OUTBOX cites section 2; capture points at section 2; section 2 item 8 removes people who handed over |
| 4 | FT sponsored silent with no interest never ended (CTO) | 5c row: 7 days after the offer with no interest, FT to Park proposals, un# Unresponsive (618 under 656); SLOW work routine 1 clause; decision 618 text |
| 5 | SLOW work still said 08:08; TEAM WHATSAPP lacked Ranjita and had the 456 clause and two openers | 11:08 and 17:08 (657); Ranjita added; 456 clause gone; opener "Zoya ✨" |
| 6 | Rules section 1 kept "Earlier rule, superseded: since decision 235 ..." | Rewritten to the current facts, ending "Signed \"Regards, Akshay\"" |
| 7 | Release v3 WhatsApps toggle marked approved | Dropped: client shows send no WhatsApps (638); FT uses v2 (601) |
| 8 | NURTURE still took Sponsored offered rows and routine 8's sponsored angle; no-contact meant Parked | Removed; a no-contact request is They declined plus the note (SLOW work and follow-ups 5a) |
| 9 | Day flow (CTO) | Your call runs before the capture composer starts; composer seed and capture STEP 8 report back by send_message to the day chat (id in the brief, else newest zoya-day session); capture's ZOYA LIVE now says it sends nothing |
| 10 | upkeep.txt dangling references and missing tools | OWNERS written in; "as STEP 3" replaced; window since the last "upkeep:" report; "(daily sweep)" and "Part B" gone; Gmail connector create_draft for 3d with decision 123 links; claude-code-remote loaded wherever send_message to the CTO is called (upkeep, calendar, SLOW work), fallback to Akshay's list; 657 cited |
| 11 | Runtime inventory incomplete | Host boards, Sarika's editing asks, FT Community sync, the monitor, the CTO round, Codex review, Monday scorecard and upkeep added; the "retired" line now names only what list_triggers shows not enabled |
| 12 | Dropped obligations | Restored in zoya-day.md: (a) engagement chats decide Status, Waiting on, Next action (593) and hand them over as Row changes (609); (b) release compression with "Akshay: send release Mail 1 ... today" first on his list and in the WhatsApp brief, same-day Mail 2 and WhatsApp 1 when release is tomorrow (628); (c) share rate in the Monday scorecard (589); (d) leads quiet over 60 days get an interest-only first mail (569); (e) a Zoya step and Zoya date for a missing transcript (644); (f) don't retry a blocked call in another chat (609) |
| 13 | 25 Oct checks cut | Kept as standing checks on Rules for Zoya: RFC threading and "record a blocker, never a replacement thread"; one company per conversation; keep ad@, drop the alias, never remove by name match; check before chasing the team, one 24-hour WhatsApp nudge |
| 14 | Host's No on B2S/HBD (CTO) | Rules section 7 line scoped: Parked is Akshay's only; We declined is Akshay's or a client-show host's no |
| 15 | Smalls | Room ask: reminder after 2 days, Akshay when under 48 hours (consistent in FAST, Rules, Calendar rules). Transcript chase: action key, Activity, 2 working days. Pathfinders its own release row (pre-launch, 626). un# "ask Sarika to confirm" and "Sri in Cc on Mail 1" kept: both are in Release v3's approved per-show table (638). The one recipient draft update cites the CTO, not 658 |
| Size | FAST must stay under 60,000 | build.py fails if FAST reaches 60,000, if SLOW, SLOW work or capture grows past its pin, or any stored prompt reaches 65,536. FAST 59,497, SLOW work 94,364. Leak and show checks in the prompts now point to Rules for Zoya section 2's lists |
| Privacy | WhatsApp group ids in zoya-day.md | Staged zoya-day.md names the groups and points to Rules for Zoya section 6 "Group chat ids"; apply_notion.py fills the ids from data/rulebook-r1/ids.json (git-ignored) and fails if any are missing. Other committed ids: routines/zoya-day.md (live, both groups) and docs/proposals/cut-1-whatsapp.py (the community group and one personal number, 91956...@c.us, twice each). No other @g.us/@c.us ids or phone numbers in tracked files |
