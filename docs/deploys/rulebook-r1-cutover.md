# Rulebook r1 cutover, 22 Nov 2026

Run by Main on the CTO's "go cutover" (20:52 JST) and "start now" (20:53 JST, window widened to 20:53 to 23:30 JST). Runbook: docs/proposals/rulebook-r1/cutover.md.

## 0. Preconditions (11:52 to 11:53 UTC)

- Window: started before 12:30 UTC on the CTO's written "start now" (Sunday's day-chat trigger disabled, Monday's first wake 07:38 JST).
- No day chat working: Sunday's and Monday's day chats idle; last zoya-oneshot (capture 20:40 JST) completed.
- zoya-lock: free (released 2026-11-19T23:49:33Z). Not touched.
- Branch up to date at 48d0565; build.py --check: no drift.
- Live files unchanged since 5d1e917.

## (d) ids.json

data/rulebook-r1/ids.json written from the live routines/zoya-day.md; git-ignored (check-ignore confirmed). Not committed.

## (a) Repo

- Release stamp: d2c73732a0b5a131bf78e0eea685ff416c4b4614. Work-file sha256 at 48d0565 matched manifest.json; build.py --release passed; no "{SLOW_WORK" left in zoya-slow.txt.
- Live files: bc6f10356c6cf6dab9e94a762332a52a49342e1a, pushed (ls-remote read back). zoya-day.md carries RELEASE d2c7373; daily-sweep.md moved to routines/retired/; skills/notion-business-os removed; docs/proposals/zoya-day/prompts kept as the rollback source.
- Checks: no "Overrides on top of", no group ids in zoya-day.md, all 8 prompts at R hash to manifest.json.
- Stored prompts sent to the CTO for (c): host-boards 8585 bytes 8ace96f5...ae16; editing-checks 9067 bytes 216d73ac...9afd; cto-round 7101 bytes 366fbeae...49b0. The CTO deploys them.

## (b) Notion

1. Four history pages moved under CTO Audit; the fresh Rules for Zoya fetch lists none of them.
2. 18 pages fetched fresh and saved by script to data/rulebook-r1/notion-cutover/ (the rollback copies).
3. apply_notion.py: all 18 clean (140 ops).
4. Writes, one page at a time: rules-for-zoya, cadences, follow-ups, wording, routines, client-show-mails, fu-1-sponsored (replace), fu-6-release (replace, child page kept), fu-2-precall, fu-3-recording, fu-8-revival, calendar-rules, inbox-your-call, rules-inbox (replace), links-limits (replace), rules-notion-list, data-rules, blurb-sources. No op matched nothing; the only warnings were three markdown parser notes on Rules for Zoya (<room>, <name>, <step> kept as text).
5. Read-back: all 18 pages MATCH the expected text after normalising Notion's own rendering (autolinks, escaped characters, <br />), and their last 200 characters agree.
6. Decisions ledger: rollback copy of 24 rows in data/rulebook-r1/decisions-before.json. 20 "Rewrite whole" rows written and read back, all equal to decisions-edits.md: 235, 329, 352, 366, 390, 420, 423, 427, 488, 514, 573, 575, 585, 618, 625, 637, 646, 647, 656, 657. Decision 367 has no row in the ledger, so nothing was written for it.
   - Trash, first pass held: the pre-check grep was not clean. routines/mac/transcripts.md cited 456, and the unscheduled routines/zoya.md and routines/calendar.md cited the four rows.
   - CTO's call (12:06 UTC): fix the callers, then Trash. routines/mac/transcripts.md source 5 now reads Ranjita's mail per decision 646 and clears her Engagement segment (repo copy only: Akshay's Mac copy is unverified until he re-runs it). routines/zoya.md and routines/calendar.md moved to routines/retired/ (not scheduled since 568). The grep then showed only the staged scripts' old-text anchors, the CLAUDE.md diff's old side and the unread old build in routines/zoya/release/. Rows 439, 456, 489 and 546 moved to Trash; a query by No. returns none of them (restorable from Trash).
7. Zoya routine page (3fb19a301a7f81b686adcbafec82287f): the stale body was replaced with a short current pointer (what runs now, where her rules live, the Routines inventory); the Change log is kept, with the cutover line added. Read back.

## (c) Stored prompts (CTO)

| Scheduled task | Trigger | Bytes | sha256 (first 16) | Result |
|---|---|---|---|---|
| Host boards | trig_01K8bueCr2xsPkbgQzjeRKsz | 8,585 | 8ace96f5e9031c1a | EQUAL (CTO, 11:55 UTC) |
| CTO coordination round | trig_019sfzEHt9djonNhbxcATgYA | 7,101 | 366fbeaee7d17fb3 | EQUAL (CTO, 11:56 UTC) |
| Sarika's editing asks | trig_01AU4fQevmq39TDZX6LvC4cq, trig_01SXrnWJb2iz5Q3zts34VZu4, trig_0177CBiFc4zP8SGCaVip97Gc | 9,067 | 216d73acc272c4f1 | EQUAL (deployed from their own session, session_019pwcV3jbCtwb56pcVB3o6J, 11:58 UTC; previous prompt 8,925 bytes, b8aef3c84386c0d4, kept there as rollback) |

Installed claude.ai cloud skills: unverified.

## Rollback

(b) and (a) together, before Monday 07:38 JST: replace_content each page from data/rulebook-r1/notion-cutover/, move the four history pages back under Rules for Zoya, restore the 20 rows from decisions-before.json, then git revert bc6f103 and push.

## Fix 1, 23 Nov: decision 637 date ownership (Auditor CX-20261123T0800 finding 2)

- Staged in b80a887 (prompts, fix637.py, fixtures_637.py); Cleanup's diff check said ship after one fix (the SLOW sponsored selector read Next date), applied in 09d6e71.
- Release candidate 3abad5205e92730289fdf46b014ce3973b19e42b: SLOW stamped to 09d6e71, work-file sha256 starting ce206094606d1366; all 8 prompts at R match manifest.json. The CTO sets the RELEASE line.
- Notion (08:51 JST): follow-ups 10 replaces, 7. Long-term chase 1, Rules for Zoya 2 (the "All 8 routines are live" line and the one-time un# loop-in removed). No op matched nothing. Read back: all three MATCH the staged text, last 200 characters equal. Before copies in data/rulebook-r1/fix637-before/ (rollback).
- fixtures_637.py passes: ordinary send, nurture, deferral, failed send and cap keep the person's Next date and write Zoya date (a cap writes nothing); no Zoya-step Next date write left in SLOW or on the page.
- Next fix (Cleanup findings 2 and 3, not blocking because SLOW's fallback picks a row with no Zoya date once): inbox-actions form chasers and LT-chase revisit, upkeep 7b form chaser, upkeep step 4 overdue flags, and the calendar transcript Task row still use Next date for Zoya's own steps.
