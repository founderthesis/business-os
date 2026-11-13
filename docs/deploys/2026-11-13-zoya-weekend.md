# 2026-11-13: Zoya weekend chat and day-chat cadence (decisions 580, 581)

Akshay, 13 Nov ~22:00 JST: keep the day chat over the weekend at 4 wakes a day; on weekdays one chat through the day at lower frequency (no mid-day rotation, "too much risk of breakage"); tell every PR team the tentative release week, replying on the post-recording mail, starting tomorrow for the whole inventory.

## Changes
- Seed routines/zoya-day.md updated (406b1bc): cadence, prompts read only via `git show 83e8fb0:docs/proposals/zoya-day/prompts/<file>` (r28 not deployed), SLOW pin 63d63ec, the 13 Nov overrides (decisions 569 to 577), the release-week rule (580), the amended stall rule.
- 13 Nov wake trig_01Y5WiS4oABkfHmcLDJpJ93a: cron `CRON_TZ=Asia/Tokyo 38 21-23 13 11 *`, so the 13 Nov chat stops after 23:38 and never fires again.
- Weekend chat "Zoya weekend, 14-15 Nov", Opus, session_019pwcUzREZR1vU2pKehScLi. At creation (22:09 JST) every business connector failed to connect (platform outage), so it was NOT marked ready and its wake trigger was not created yet.
- Monitor: trig_01VX6YtwUQ1jBMx23kMjnxM4 now `CRON_TZ=Asia/Tokyo 55 * * * 1-5`; new trig_012eTmTgQcdecGs94PYjPuje `CRON_TZ=Asia/Tokyo 55 8,12,16,20 * * 0,6`, both into the monitor chat session_019pwcV3kwZU8vnV3UmQq6wR.

## Planned
- Weekend wake (once the chat is ready): `CRON_TZ=Asia/Tokyo 38 8,12,16,20 14,15 11 *`, prompt "Wake: run what is due now per routines/zoya-day.md". First wake runs the release-week backfill (decision 580).
- Weekdays (decision 581): one chat per day, wakes `38 7-23/2` JST (9 a day), no mid-day rotation. The Sunday 20:45 CTO round creates Monday's chat; each weekday 20:45 round creates the next day's.

## Rollback
As in docs/deploys/2026-11-13-zoya-day.md: disable the wake and monitor triggers, archive the chat and wait until terminal, check zoya-lock is free, re-enable the seven paused routines.

## Seed prompt for a weekend chat (create_session: title "Zoya weekend, 14-15 Nov", model claude-opus-5-5, this repo and branch, tag zoya-day)

You are Zoya's weekend chat for Sat 14 and Sun 15 Nov 2026. Read CLAUDE.md, then routines/zoya-day.md (commit 406b1bc or later): it is your seed (cadence, the 83e8fb0 prompt pin via git show, SLOW pinned to 63d63ec, the 13 Nov overrides, the amended stall rule, the wake record). You wake at 08:38, 12:38, 16:38 and 20:38 JST; Zoya SLOW and the daily sweep are weekdays only. One-off job for your first wake (decision 580): after the due prompts, for every Founder Thesis Episode (FT and FT Tier 3 Spotlight only, never un#, Built to Share or Human by Design; decision 582) with Planned release set and Status not Published, Archived or Not releasing, reply on that guest's post-recording thread from Zoya's inbox with the "Release date (post-recording)" wording, word for word, To their side as that thread had them, Cc Akshay; the week from Planned release, paragraph 2 dropped within 2 weeks of release. Skip the 7 told on 13 Nov (Zeta/Aafia, Veritas/Niraj, Ideosphere/Gautam, Kaizzen/Raghu, JRB/Anmol, PRtainment/Srinivas, Value360/Amit) and any thread where our side already wrote last about the release; no thread means a report line only; stay under the cap; an Activity per send; list sent, skipped and no-thread in the wake record. Now: run nothing and send nothing; check git show 83e8fb0 for all 7 prompt files and make one cheap read each on Notion, MCP Emails, Google Calendar and Blueticks, then send_message the CTO session (session_015wSc87F8WCdJKB91Tm34tJ) "ready <session id>" with one line per check.
