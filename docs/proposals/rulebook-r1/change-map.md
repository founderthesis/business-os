# Rulebook r1: change map

Batch 1 covers the nine examples on the audit page (42019a301a7f81eb82d0cc814724b24e) plus the conflicts found on the way. Nothing here is live. The CTO cuts over; Cleanup reviews.

How the staged rulebook is built:
- Prompts: `build.py` takes the pinned bytes (`git show 83e8fb0:` for the six routine prompts, `63d63ec:` for the SLOW work file), applies `edits.py`, and writes `prompts/` and `manifest.json` (sizes, sha256, source hashes). Every edit must match exactly once or the build fails. `build.py --check` reports drift.
- Notion: `notion_edits.py` holds the edits as address-free anchors; `apply_notion.py <fresh fetch dir> <out dir>` applies them to a fresh fetch at cutover and fails on any miss. Output stays out of git (the pages carry mailto links).
- `routines/zoya-day.md` is a rewrite, not a patch. `claude-md/CLAUDE.md` and its `.diff`, `seeds/composer-seed.md`, `decisions-edits.md` are the other staged files.

## Before and after (bytes, or characters for Notion)

| Source | Before | After (batch 1) | Note |
|---|---|---|---|
| routines/zoya-day.md | 49,523 | 25,520 | No override section; duties only the day chat runs |
| CLAUDE.md | 27,140 | 18,280 | Zoya section points to the rule pages |
| zoya-fast.txt | 62,996 | 65,443 | Recipients, team roles and parking written in once; Mamatha and Sri clauses replaced |
| zoya-slow.txt | 15,646 | 15,243 | Schedule, work-file pin stamped at release |
| zoya-slow-work.txt | 94,833 | 96,443 | Sponsored, pauses, recording chase, transcripts, owner mail removed |
| calendar.txt | 62,916 | 63,120 | Ranjita, no Builder, no delete_event on guest events |
| inbox-capture.txt | 50,812 | 50,913 | Team roles, recipients |
| inbox-actions.txt | 48,515 | 48,576 | Team roles |
| whatsapp.txt | 39,817 | 39,820 | Mamatha |
| daily-sweep.txt | 50,569 | retired | Obligations: S6 |
| Rules for Zoya (Notion) | 66,758 | 68,032 | Release table, sender table, full links list added; hold, Mamatha section, Gmail-connector line removed |
| Cadences | 9,540 | 5,847 | Old timetables removed; sponsored rows rewritten |
| Rules for Zoya: follow-ups | 17,074 | 18,949 | Sponsored and pause table added; nurture branch for sponsored removed |
| Mail and WhatsApp wording | 91,251 | 78,289 | 6 retired toggles, the Retired section and the sweep's Mamatha list removed |
| Routines | 4,001 | 3,004 | One runtime inventory replaces the historical overview |

The prompts grow slightly in batch 1 because three shared rules (RECIPIENTS, TEAM ROLES, PARKED) are written in whole; batch 2 removes the scattered clauses they replace.

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
  | 6c Billing and invoices forwarded to Jaya (an allowed ad@ forward) | Day chat, daily: **unowned since 657**; batch 2 stages it |
  | 7b Guest form submissions merge | Day chat, daily: **unowned**; batch 2 |
  | 3g Founder Thesis guests list (podm.in/guest-list) | Saturday chat: **unowned**; batch 2 |
  | 3k FT Community rows for recorded guests (backstop) | Saturday chat: **unowned**; batch 2 |
  | 3p BD prospect episodes to PaaS rows | Saturday chat: **unowned**; batch 2 |
  | 3h Auditor handoffs to Task rows, fix checks | Auditor items go to the Build board and the CTO (655); Mail issues fix checks to SLOW: batch 2 |
  | 3, 3a, 3a2, 3a3, 3a4, 3b, 4, 4b, 5 (data upkeep, owners, flags, due vs done) | Day chat wake record and row tidying (588); 3a4 one-time moves end |
  | 2 Decisions sync | Retired: the ledger is Notion (350) |
  Recommendation: batch 2 builds these steps into one `upkeep.txt` made mechanically from the sweep's own text, run by the day chat (daily and Saturday parts). No new schedule.
- Verify: F15.

### S7. Engineering work ownership
- Authority: 405, 655.
- Losing clauses: CLAUDE.md line 24 ("builder actions all live there"); calendar's Waiting on list with Builder and "Builder: delete the invite"; SLOW work's Mail issues "Waiting on Builder" row.
- Final wording: CLAUDE.md principle (Engagements, Team tasks, Build board); calendar and SLOW work send builder steps to the CTO session.
- Consumers: CLAUDE.md, calendar.txt, zoya-slow-work.txt, zoya-day.md, decision 329.
- Verify: F13.

### S8. One-off repairs and retired templates
- Saman Khan / Keshav Baljee reply (585, 13 Nov) and the Zoya date backfill (637, 20 Nov): removed from recurring text. **To verify before cutover**: that Zoya's reply to Saman went (Activity on Keshav Baljee's Engagement after 13 Nov) and that the backfill report reached the CTO session. If either is missing, it goes on its existing row with its original date.
- WisdomTree (Ryan Louvar, un#) hands-off: a row-specific hold, not policy. Moved out of the day file; **to verify** it is on that Engagement's Next action or Claude note before cutover.
- Owner mail (619): SLOW work STEP 0f deleted. Other owner-mail references in SLOW work (batch keys, Mail issues "Needs Akshay not yet mailed"): batch 2.
- Wording page: 6 retired toggles, the "Retired: do not send" section, the sweep's "Mamatha's daily list" and the Templates database sentence removed. Old FT release toggles that Release v2 replaced: batch 2.
- Verify: F14.

### S9. Release-date authority
- Authority: 427, 580, 582, 589, 601, 628, 630; the 30 Oct hold (Akshay, until he lifts it).
- Evidence: the hold was never lifted in writing on the page, but later Akshay decisions send dates for Founder Thesis once Sarika or he confirms. No decision lifts it for other shows.
- Final wording: the release-date table on Rules for Zoya; zoya-day.md's release duty; Rules section 1's release rows (Mail 1 is Akshay's, 2 to 6 Zoya's, replacing the 235 row).
- Open: question 1.
- Verify: F16, F17.

## Other conflicts found (batch 2 unless noted)

| # | Conflict | Proposed resolution |
|---|---|---|
| S10 | Rules for Zoya's holding reply (390: "checking with akshay, will come back by <day>") against 571 ("hi <first name>, will get back to you on this", never "Akshay") and 418 (no deadlines) | 571's wording; rewrite 390's section |
| S11 | Rules for Zoya section 1 table: thank-you "Akshay by hand", Release mail 1 "Zoya (235)" against v2 | Release rows staged; thank-you row checked in batch 2 |
| S12 | Inbox capture now runs in a composer that sends nothing (653), but its ad@ loop-in step for fresh pitches has no other sender | Capture leaves a Row change "loop-in due"; the day chat sends it in inbox actions. Needs CTO confirmation of what happened to loop-ins since 22 Nov |
| S13 | "Book immediately: ask for recording slots" in routines/cowork-evals.md and in inbox-actions and the sweep, against 654 | Rewrite cowork-evals.md TEAM ROLES and the skills' route text (ft-guest-eval) |
| S14 | PRE-SEND CHECKS "every team address never in To" against team-only mail | Covered by RECIPIENTS 3/ (staged) |
| S15 | Rules for Zoya "System-audit corrections, 25 Oct" and "More rules (decisions 373 to 382)" sections restate and supersede older text | Fold each into its topic section, remove the history |

## Uninspected or unverified

- Cloud skills installed on claude.ai: unreadable from here. Their repo sources are listed in inventory.md; every installed copy is unverified.
- Stored scheduled-task prompts: read in batch 2 with list_triggers (read only).
- The live day chat's context: edits don't reach a running conversation; the cutover needs the daily rollover.
