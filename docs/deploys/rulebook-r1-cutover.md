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
   - Trash held: the pre-check grep did not come back clean. Live or semi-live files still cite the four rows: routines/mac/transcripts.md (456), routines/zoya.md and routines/calendar.md (old standalone prompts), routines/retired/daily-sweep.md, and the staged scripts' old-text anchors. Rows 439, 456, 489 and 546 stay in the ledger, In force, until the CTO decides.
7. Change log line added on the Zoya routine page (3fb19a301a7f81b686adcbafec82287f).

## Rollback

(b) and (a) together, before Monday 07:38 JST: replace_content each page from data/rulebook-r1/notion-cutover/, move the four history pages back under Rules for Zoya, restore the 20 rows from decisions-before.json, then git revert bc6f103 and push.
