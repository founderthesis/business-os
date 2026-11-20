# Decisions audit, 21 Nov 2026

What was done the same night: 102 superseded or obsolete rows moved to Notion Trash (none cited by a live file), 373 to 380 copied into Notion, the repo archive removed, 646 and 647 filled in, the second set of 635 to 638 renumbered 648 to 651. Next free number: 652. Still open: the CONFLICT and UNSURE rows below, and retiring the stale routine files that cause most conflicts.

# Decisions ledger audit, 20 Nov 2026

Read-only audit of the Notion Decisions data source (collection://cfcc0ef3-3e83-4655-98ed-56ed950b02ec) against the live repo files. Full row list: audit.csv in this folder.

Rows audited: 591 (516 In force, 70 Superseded, 3 Open, 2 blank status).

Live files scanned (123): CLAUDE.md, routines/zoya-day.md, docs/proposals/zoya-day/prompts/*.txt, routines/*.md, routines/mac/*.md, skills/**, docs/engagement-chat-seed.md, docs/blurb-chat-seed.md, plus routines/zoya/parts/*.txt, routines/zoya/release/* (the SLOW work file and the parts deployed prompts are built from) and routines/editing-checks.txt.

## Counts per verdict

| Verdict | Rows |
|---|---|
| KEEP | 441 |
| SUPERSEDED | 77 |
| OBSOLETE | 24 |
| CONFLICT | 33 |
| UNSURE | 16 |

## Counts per Area

| Area | KEEP | SUPERSEDED | OBSOLETE | CONFLICT | UNSURE | Total |
|---|---|---|---|---|---|---|
| (no Area) | 9 | 1 | 0 | 0 | 0 | 10 |
| Calendar and recordings | 38 | 2 | 0 | 1 | 0 | 41 |
| Data model | 27 | 7 | 2 | 0 | 0 | 36 |
| Evals | 16 | 5 | 0 | 1 | 0 | 22 |
| Host shows (un# / B2S / HBD) | 36 | 7 | 4 | 1 | 1 | 49 |
| Inbox | 30 | 11 | 1 | 3 | 1 | 46 |
| Links | 7 | 1 | 0 | 2 | 0 | 10 |
| Mail wording and voice | 27 | 5 | 0 | 4 | 1 | 37 |
| People and dedupe | 13 | 1 | 2 | 1 | 0 | 17 |
| Platform and tooling | 25 | 3 | 4 | 7 | 1 | 40 |
| Release and episodes | 62 | 11 | 4 | 1 | 7 | 85 |
| Sponsored and revenue | 17 | 7 | 3 | 2 | 1 | 30 |
| Team and roles | 26 | 6 | 0 | 3 | 2 | 37 |
| WhatsApp and community | 26 | 2 | 0 | 1 | 1 | 30 |
| Zoya and follow-ups | 82 | 8 | 4 | 6 | 1 | 101 |

## CONFLICT rows (33)

A row the ledger treats as Superseded (or whose content a later decision replaced) that a live file still cites. Most are harmless history pointers ("was four times a day, decisions 202, 231"); the operative ones are 89, 102, 146, 155, 156, 351 and 386, where a live prompt still applies the replaced rule. Fix the file, then the row can be retired.

- **67 The Queue is Mamatha's worklist** (Superseded). Replaced by: 79. Cited: routines/calendar.md:12. Marked Superseded (by 79) but still cited in live files
- **68 Automations as four Claude routines** (Superseded). Replaced by: 83, 131, 146, 173. Cited: routines/calendar.md:12. Marked Superseded (by 83, 131, 146, 173) but still cited in live files
- **89 Deals: cold target list plus live pipeline** (In force). Replaced by: 518. Cited: routines/inbox.md:135. Deals target list; Deals retired by 518 but routines/inbox.md still applies it
- **98 Mail wording lives in the Templates database** (Superseded). Replaced by: 194, 207. Cited: docs/proposals/zoya-day/prompts/calendar.txt:17; docs/proposals/zoya-day/prompts/daily-sweep.txt:14; docs/proposals/zoya-day/prompts/inbox-actions.txt:19; routines/calendar.md:33; routines/daily-sweep.md:27; routines/inbox.md:34. Marked Superseded (by 194, 207) but still cited in live files
- **102 Email automation: draft, learn, then send** (In force). Replaced by: 387. Cited: docs/proposals/zoya-day/prompts/daily-sweep.txt:70; docs/proposals/zoya-day/prompts/inbox-actions.txt:54; routines/daily-sweep.md:77; routines/inbox.md:83. Draft-learn-send loop retired by 387, yet daily-sweep and inbox-actions prompts cite 102
- **107 Reply on Saurabh's forwarded pitches** (Superseded). Replaced by: 122, 131. Cited: docs/proposals/zoya-day/prompts/inbox-capture.txt:125; routines/inbox.md:143. Marked Superseded (by 122, 131) but still cited in live files
- **123 Short plain-text links in agent mail** (Superseded). Replaced by: 184. Cited: CLAUDE.md:65; docs/proposals/zoya-day/prompts/calendar.txt:17; routines/calendar.md:33; routines/daily-sweep.md:27; routines/inbox.md:34. Marked Superseded (by 184) but still cited in live files
- **128 Zencastr jobs as a Mac Cowork task** (In force). Replaced by: 439, 445. Cited: routines/mac/zencastr-mac.md:3. Mac Zencastr task vs Mamatha creating rooms (439, 445); routines/mac/zencastr-mac.md still cites it
- **131 No holding reply on inbound pitches** (Superseded). Replaced by: 195, 199. Cited: docs/proposals/zoya-day/prompts/inbox-capture.txt:110; docs/proposals/zoya-day/prompts/zoya-fast.txt:76; routines/inbox.md:91; routines/zoya.md:100; routines/zoya/parts/decision.txt:4; routines/zoya/release/zoya-one.txt:73. Marked Superseded (by 195, 199) but still cited in live files
- **135 Links as unlinked text** (Superseded). Replaced by: 184. Cited: docs/proposals/zoya-day/prompts/calendar.txt:17; docs/proposals/zoya-day/prompts/daily-sweep.txt:14; docs/proposals/zoya-day/prompts/inbox-actions.txt:103; routines/calendar.md:33; routines/daily-sweep.md:27; routines/inbox.md:34,164. Marked Superseded (by 184) but still cited in live files
- **138 Inbox runs three times a day** (Superseded). Replaced by: 174, 202, 231. Cited: routines/inbox.md:3. Marked Superseded (by 174, 202, 231) but still cited in live files
- **140 Outbound at New goes to Mamatha** (Superseded). Replaced by: 167, 211. Cited: docs/proposals/zoya-day/prompts/daily-sweep.txt:24; docs/proposals/zoya-day/prompts/inbox-actions.txt:95; routines/daily-sweep.md:37; routines/inbox.md:136. Marked Superseded (by 167, 211) but still cited in live files
- **146 Evals and dossiers move to Cowork tasks** (In force). Replaced by: 593. Cited: routines/cowork-evals.md:20. Evals and dossiers as Cowork tasks replaced by engagement chats (593); routines/cowork-evals.md still cites it
- **149 Repeat pitch gets a one-line reply** (Superseded). Replaced by: 303. Cited: docs/proposals/zoya-day/prompts/inbox-capture.txt:115; routines/inbox.md:97. Marked Superseded (by 303) but still cited in live files
- **154 Mamatha handles only FT cold outreach** (Superseded). Replaced by: 167, 211. Cited: docs/proposals/zoya-day/prompts/daily-sweep.txt:15; docs/proposals/zoya-day/prompts/inbox-actions.txt:20; docs/proposals/zoya-day/prompts/inbox-capture.txt:50; routines/cowork-evals.md:10,11; routines/daily-sweep.md:28; routines/inbox.md:37. Marked Superseded (by 167, 211) but still cited in live files
- **155 "When does it go live?" goes to Akshay** (In force). Replaced by: 427. Cited: docs/proposals/zoya-day/prompts/daily-sweep.txt:131; routines/inbox.md:180,201. Release-date asks to Akshay replaced by 427; inbox.md and daily-sweep still cite 155
- **156 Deals are only for PaaS** (In force). Replaced by: 518. Cited: routines/inbox.md:125. Deals only for PaaS; Deals retired by 518, routines/inbox.md still cites it
- **174 Inbox runs at 09:00, 16:00 and 22:00** (Superseded). Replaced by: 202, 231. Cited: routines/calendar.md:3. Marked Superseded (by 202, 231) but still cited in live files
- **180 Zoya's mail rules** (Superseded). Replaced by: 225, 229. Cited: CLAUDE.md:46; docs/proposals/zoya-day/prompts/calendar.txt:20; docs/proposals/zoya-day/prompts/daily-sweep.txt:17; docs/proposals/zoya-day/prompts/inbox-capture.txt:51; routines/calendar.md:36; routines/daily-sweep.md:30; routines/inbox.md:40. Marked Superseded (by 225, 229) but still cited in live files
- **186 Public FT Community directory, split record** (Superseded). Replaced by: 190. Cited: routines/community-directory.md:3. Marked Superseded (by 190) but still cited in live files
- **187 Host boards sync from the inbox routine** (Superseded). Replaced by: 261. Cited: routines/host-boards.md:3. Marked Superseded (by 261) but still cited in live files
- **201 Zoya's tone** (Superseded). Replaced by: 345. Cited: CLAUDE.md:50; routines/zoya.md:57. Marked Superseded (by 345) but still cited in live files
- **202 Inbox runs four times a day** (Superseded). Replaced by: 231. Cited: routines/inbox.md:3; routines/whatsapp.md:3. Marked Superseded (by 231) but still cited in live files
- **205 Zoya live for FT; Akshay in Cc 10 days** (Superseded). Replaced by: 225, 229. Cited: routines/zoya.md:5,36. Marked Superseded (by 225, 229) but still cited in live files
- **206 Zoya's sign-off** (Superseded). Replaced by: 345. Cited: CLAUDE.md:50; routines/zoya.md:57. Marked Superseded (by 345) but still cited in live files
- **213 Mail-safe "For mails" section on Engagements** (Superseded). Replaced by: 214. Cited: routines/cowork-evals.md:21. Marked Superseded (by 214) but still cited in live files
- **231 Morning runs move to 8am JST** (In force). Replaced by: 344, 581. Cited: routines/calendar.md:3; routines/inbox.md:3; routines/zoya.md:3. 8am morning runs replaced by hourly routines and the day chat; cited as history
- **233 Re-audit before the first 8am runs** (In force). Replaced by: n/a. Cited: routines/mac/transcripts.md:12. One-off re-audit; routines/mac/transcripts.md cites it only to say its mail is retired
- **334 Mac tasks handle Zencastr rooms and transcripts** (In force). Replaced by: 439, 456. Cited: routines/mac/README.md:16; routines/mac/transcripts.md:12. Mac tasks for rooms and transcripts vs Mamatha supplying both; routines/mac still cites it
- **351 Waiting on Akshay over 3 days goes in the owner mail; WhatsApp adds stay on him** (In force). Replaced by: 619. Cited: routines/zoya.md:105. Owner mail retired by 619; routines/zoya.md still cites 351
- **384 Deleting records needs Akshay's go-ahead per deletion** (Superseded). Replaced by: 416. Cited: CLAUDE.md:119. Marked Superseded (by 416) but still cited in live files
- **386 Guest form chasers: five, then one ask to Akshay** (In force). Replaced by: 523. Cited: routines/inbox.md:116; routines/zoya.md:140; routines/zoya/parts/followups.txt:14; routines/zoya/release/zoya-slow-work.txt:133. Five form chasers replaced by 523; routines/inbox.md and zoya.md still cite "five"
- **556 Zoya SLOW runs on Sonnet (replaces decision 450's Opus)** (In force). Replaced by: 559. Cited: CLAUDE.md:32. Zoya SLOW on Sonnet reverted by 559; CLAUDE.md cites it as history

## UNSURE rows (16)

- **15 Content pack: Claude automatic, others manual** (In force). Replaced by: n/a. Cited: none. Content pack with Gemini/ChatGPT manual; copy now runs through editing and copy docs (500, 506, 527)
- **17 Zencastr transcripts via Claude in Chrome** (In force). Replaced by: 439, 456. Cited: none. Transcripts now come from Mamatha (456), yet CLAUDE.md platform facts still say Claude in Chrome on the Mac
- **41 Tier decides workload** (In force). Replaced by: 527. Cited: none. Tier-based light pack contradicted by 527 (copy doc every tier); work order may still hold in routines/tasks.md
- **42 Reels to guest and company on release day** (In force). Replaced by: 601. Cited: none. Reels on release day not in Release v2 (601); unclear if still done
- **43 Science and PhD guests review a frame** (In force). Replaced by: 600. Cited: none. Guest frame review vs 600 (no preview unless the guest paid); one live file mentions Guest review
- **85 Transcripts attached from Akshay's Mac** (In force). Replaced by: 456, 644. Cited: none. Mac transcript task vs transcripts from Mamatha (456); routines/mac/transcripts.md still in the repo
- **109 One dashboard page per person** (In force). Replaced by: n/a. Cited: none. Per-person dashboard pages; Mamatha has since left most work (352), unclear what remains
- **203 First sponsored mail promises access** (In force). Replaced by: 573. Cited: none. "Promise access" framing may be replaced by 573's toned-down offer
- **311 Every Claude skill is copied into Notion** (In force). Replaced by: n/a. Cited: none. Skills copied into Notion; no live file mentions a Skills database
- **335 Persistent nurture replaces silence closures** (In force). Replaced by: 573, 605, 618, 625. Cited: none. Persistent nurture narrowed by later chase rules; Tier 1 part may stand
- **361 Host boards move to a Notion agent with two-way sync** (In force). Replaced by: n/a. Cited: none. Host boards to a Notion agent; routines/host-boards.md still describes a Claude routine
- **461 Episodes workflow: cap of 6, release dates, editor notes** (In force). Replaced by: 526. Cited: none. Work-started cap of 6 and one-time setup; unclear after the 24-step workflow
- **473 The FT Community ask lives only on the To invite list** (In force). Replaced by: 608. Cited: none. No community-invite segments vs 608 (invite asks in Akshay's queue)
- **475 Plain slot wording** (In force). Replaced by: 569. Cited: none. "Pick any slot" wording vs 569 (never "pick any slot" alone for /30min)
- **567 Allocation mails stay as they are** (In force). Replaced by: 592. Cited: none. Allocation mail unchanged, but 592 removes Akshay from Cc on team mails
- **(no No.) O3: Inbox backlog clean-up** (Open). Replaced by: n/a. Cited: none. Open inbox backlog clean-up; no evidence it was closed

## Metadata to fix

**Missing No. and Status** (body-only rows, created 20 and 21 Nov):
- 646. Ranjita covers Mamatha's tasks while Mamatha is on a long break (41e19a301a7f81cf936fe2841ced809d)
- 647. Reply-all keeps Sri and client-show hosts; Zoya checks the recipient list against the latest message before every send (41e19a301a7f811283b2cbbacde7c230)

**Open rows with no No.**: O1 Field-level spec, O2 Release cadence, O3 Inbox backlog clean-up.

**Duplicate numbers** (two different rows share one No.):
- 104: 104a: Holds get a date / Chaandini's views follow her shows
- 635: An open Akshay ask sets Next date, so it shows in his queue / Claude never touches Salesblink for the B2S outreach list
- 636: No organic slot: offer a free founderthesis.com feature or a sponsored video / Pre-IPO companies go on the B2S list only if they match the B2S theme and the founder is easy to get
- 637: One copywriter chat per B2S episode, spawned from Chaandini's assistant chat / Zoya gets her own date field; Next date is for people only
- 638: Episode row gets the doc and chat links as soon as they exist / Release v3 goes live for un#, starting with Adrian (Steakhouse)

**Missing Area**: 381, 498, 499, 569, 570, 571, 572, 573, 646., 647.

**Superseded with an empty Replaced by**: none. Row 87 has free text ("Override of 9 Oct") instead of a number.

**In force but with text in Replaced by** (amendment notes in the wrong field): 529 (Tracxn half replaced by 532), 537 (PaaS follow-ups amended 10 Nov).

**In force in Notion but replaced in substance** (status should become Superseded): 28 (by 533), 32 (by 500, 506, 527), 34 (by 499, 510, 526), 35 (by 514, 515), 39 (by 521), 40 (by 508, 526), 53 (by 416), 95 (by 615), 96 (by 477, 615), 110 (by 340), 132 (by 260, 352, 489), 159 (by 420, 572), 164 (by 420), 178 (by 307, 323), 228 (by 412, 563, 615), 260 (by 352, 489), 367 (by 573, 618), 370 (by 393, 547), 431 (by 514, 515), 455 (by 593), 467 (by 619), 471 (by 488), 474 (by 588), 477 (by 563, 615), 507 (by 565), 543 (by 613), 548 (by 620).

**Same rule recorded twice**:
- 470 and 583: no ad@ loop-in when Zoya is already on the mail
- 362, 370, 393 and 547: quiet hours, three generations; only 393 as amended by 547 stands
- 543 and 613: sharing Akshay's WhatsApp number (613 replaces 543)
- 548 and 620: search impressions line (620 replaces 548)
- 450, 556 and 559: Zoya SLOW model (Opus, then Sonnet, then Opus again)
- 177/194/207 and CLAUDE.md: who Zoya is and where her rules live
- 95, 96, 228, 412, 477, 563 and 615: five versions of the FT thank-you; only 563 and 615 stand
- 32, 500, 506, 527 and 564: where episode copy lives
- 35, 431, 514 and 515: who sets FT release dates
- 584 and 632: pitch-receipt wording and its exception

**Rows missing from Notion**: 373, 374, 375, 376, 377, 378, 379 and 380 are in docs/decisions.md but have no Notion row, so the archive's "every row 1 to 467 is also in Notion" is false. 373 to 379 are cited as operative rules by live prompts (calendar.txt, daily-sweep.txt, inbox-actions.txt, whatsapp.txt, routines/zoya.md, routines/mac/transcripts.md): attendee capture (373), post-recording v2 (374), follow-up speed (375), internal tasks and transcripts (376, 377), team @zoya questions on WhatsApp (378), sponsored no from a PR agency (379). 380 (Akshay's call on a thread Zoya isn't on) is not cited. Copy all eight into Notion; 374 and 376/377 are probably already partly replaced (615, 439, 456, 646) and should land as Superseded.

**Cited-but-spent**: some KEEP rows are one-off or retired items that a live file still names (for example 394, the "one-week trial" that became permanent, and 230, a routine audit record). Dropping those pointers from the files would let the rows go.


## docs/decisions.md against Notion

- Every number in docs/decisions.md (391 numbers, with 104 used twice) is in Notion except **373 to 380** (eight rows, above).
- Notion holds 20 numbers up to 467 that the archive never had: 341 to 343, 357 to 372 and 381. That is fine (the archive froze late), but the archive's header overstates its completeness.
- 240 to 259 and 264 to 299 exist in neither place and nothing cites them.

Files that refer to docs/decisions.md:
- Live: CLAUDE.md (lines 16, 101, 147), README.md (line 5, still tells readers to start with it), routines/inbox.md (line 13, "Decided: 61 ... 68 in docs/decisions.md"), skills/bts-guest-eval/SKILL.md (line 262), docs/tool-eval-seed.md.
- History: docs/archive/handoff.md, docs/archive/handoff-ft-email.md, docs/cleanup-2026-10.md, and 17 files under docs/proposals/ (ar20261019-4-b2s-cold-pause.md, ar20261019-6-inventory.md, blue-legacy/plan.md, d420/replay424.json, dossier-466/cleanup-verdict.md, inbox-split/r9/README.md, inbox-split/r9/replay9.json, inbox-split/r10/replay10.json, precall-409/cleanup-proposal.md, zoya-r12/replay.json, zoya-r12/replay-r12c.json, zoya-r13/replay.json, zoya-r15/cleanup/inbox.json, zoya-r15/handoff.md, zoya-r15/replay.json, zoya-r16/cleanup-verdict.md, zoya-split-cleanup.md).

## Other notes

- 635 ("Claude never touches Salesblink for the B2S outreach list", 20 Nov) implies Salesblink is still in use for B2S, while 344 retired Salesblink. Worth one line from Akshay on which is true.
- Several files the brief counts as live are themselves overtaken by later decisions: routines/cowork-evals.md and routines/cowork-dossiers.md (replaced by engagement chats, 593), routines/mac/zencastr-mac.md and routines/mac/transcripts.md (rooms and transcripts now from Mamatha or Ranjita, 439, 456, 646), and routines/zoya.md (the old single Zoya routine, now zoya-fast/zoya-slow). Most CONFLICT rows are cited only from these files. Retiring the files would clear about half the conflicts in one move.
- The citation scan is pattern based ("decision N", "decisions N, M", "N to M", "amends/replaces N", bare "(N)" on a line that mentions a decision). Dates like "20 Nov" are filtered out. Citations of a duplicated number (104, 635 to 638) cannot tell the two rows apart.
