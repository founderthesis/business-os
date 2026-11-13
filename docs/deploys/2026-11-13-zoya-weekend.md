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
