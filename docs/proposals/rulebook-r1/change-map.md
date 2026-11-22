# Rulebook r1: change map

Batch 1 covers the nine examples on the audit page (42019a301a7f81eb82d0cc814724b24e) plus the conflicts found on the way. Nothing here is live. The CTO cuts over; Cleanup reviews.

How the staged rulebook is built:
- Prompts: `build.py` takes the pinned bytes (`git show 83e8fb0:` for the six routine prompts, `63d63ec:` for the SLOW work file), applies `edits.py`, and writes `prompts/` and `manifest.json` (sizes, sha256, source hashes). Every edit must match exactly once or the build fails. `build.py --check` reports drift.
- Notion: `notion_edits.py` holds the edits as address-free anchors; `apply_notion.py <fresh fetch dir> <out dir>` applies them to a fresh fetch at cutover and fails on any miss. Output stays out of git (the pages carry mailto links).
- `routines/zoya-day.md` is a rewrite, not a patch. `claude-md/CLAUDE.md` and its `.diff`, `seeds/composer-seed.md`, `decisions-edits.md` are the other staged files.

## Before and after (bytes, or characters for Notion)

| Source | Before | After | Note |
|---|---|---|---|
| routines/zoya-day.md | 49,523 | 26,035 | No override section; duties only the day chat runs |
| CLAUDE.md | 27,140 | 18,280 | Zoya section points to the rule pages |
| zoya-fast.txt | 62,996 | 65,443 | Recipients, team roles and parking written in once; Mamatha and Sri clauses replaced |
| zoya-slow.txt | 15,646 | 15,243 | Schedule, work-file pin stamped at release |
| zoya-slow-work.txt | 94,833 | 96,443 | Sponsored, pauses, recording chase, transcripts, owner mail removed |
| calendar.txt | 62,916 | 63,120 | Ranjita, no Builder, no delete_event on guest events |
| inbox-capture.txt | 50,812 | 50,913 | Team roles, recipients |
| inbox-actions.txt | 48,515 | 48,576 | Team roles |
| whatsapp.txt | 39,817 | 39,820 | Mamatha |
| host-boards.md / editing-checks.txt / cowork-evals.md | 9,357 / 8,925 / 15,198 | 9,209 / 9,067 / 15,121 | Mamatha, dated branches, B2S/HBD hand-offs to Zoya |
| daily-sweep.txt | 50,569 | retired | Its live steps: upkeep.txt, 35,929 (S17) |
| Rules for Zoya (Notion) | 66,758 | 62,420 | Release table, sender table, full links list, standing checks; hold, 25 Oct corrections, Mamatha section, transcript-by-mail, Gmail-connector line removed |
| Cadences | 9,540 | 5,847 | Old timetables removed; sponsored rows rewritten |
| Rules for Zoya: follow-ups | 17,074 | 18,949 | Sponsored and pause table added; nurture branch for sponsored removed |
| Mail and WhatsApp wording | 91,251 | 76,917 | Retired toggles, the Retired section, the sweep's Mamatha list and the un# pre-release ask removed; Release v3 marked live on un# |
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
| S12 | Inbox capture now runs in a composer that sends nothing (653), but its ad@ loop-in step for fresh pitches has no other sender | Capture leaves a Row change "loop-in due"; the day chat sends it in inbox actions. Needs CTO confirmation of what happened to loop-ins since 22 Nov |
| S13 (done) | "Book immediately: ask for recording slots" against 654 | Already fixed in routines/cowork-evals.md at db38ce7; the sweep's copy is retired; no skill routes to a slot ask |
| S14 | PRE-SEND CHECKS "every team address never in To" against team-only mail | Covered by RECIPIENTS 3/ (staged) |
| S15 (staged) | Rules for Zoya "System-audit corrections, 25 Oct" and "More rules (decisions 373 to 382)" restate and supersede older text | Staged: the two still-valid checks (reach claims, verified completion) kept as "Standing checks"; the rest already lives in its topic section or is obsolete (Zencastr Mac task, eval migration, Codex blurbs, which 652 replaced). The appendix is renamed and its 376 transcript-by-mail paragraph replaced by Ranjita's flow |
| S16 (staged) | Stored prompts: Sarika's editing asks (Mamatha transcripts, 456; Mamatha in the share list) and Host boards (Waiting on Mamatha or Chaandini; "until 19 Oct" branches) | Staged routines/editing-checks.txt and routines/host-boards.md; B2S and HBD host yes/no now hand the step to Zoya (decision 323) |
| S17 (staged) | The sweep's live steps had no owner after 657 | prompts/upkeep.txt, cut by line number from the sweep's own text plus 12 edits; the day chat runs it once a weekday |
| S18 | The CTO reminder for Monday's seed says "SLOW and the sweep back on" | Reported to the CTO, 22 Nov 20:00 JST |
| S19 | skills/notion-business-os: not installed, not referenced, carries Mamatha examples and the retired Deals board | Delete at cutover |

## Uninspected or unverified

- Cloud skills installed on claude.ai: unreadable from here. Their repo sources are listed in inventory.md; every installed copy is unverified.
- Stored scheduled-task prompts: read in batch 2 with list_triggers (read only).
- The live day chat's context: edits don't reach a running conversation; the cutover needs the daily rollover.
