# 2026-11-15: Monday weekday Zoya chat (decision 581)

Created by the Sun 15 Nov 20:45 JST CTO round, per decision 581 (one chat per weekday, wakes every 2 hours, no mid-day rotation).

## Changes
- New chat "Zoya day, Mon 16 Nov", Opus, session_019pwcV3UgWtZi7iTapXeEMj, this repo and branch, tag zoya-day. Seed below; routines/zoya-day.md at HEAD (overrides 569 to 587), prompts via `git show 83e8fb0:docs/proposals/zoya-day/prompts/<file>`, SLOW pinned to 63d63ec (r27 and r28 not deployed).
- Wake trigger "Zoya day wake (Mon 16 Nov)": `CRON_TZ=Asia/Tokyo 38 7-23/2 16 11 *` (9 wakes, 07:38 to 23:38 JST), prompt "Wake: run what is due now per routines/zoya-day.md". Created only after the chat reported ready.
- Monitor (session_019pwcV3kwZU8vnV3UmQq6wR) told to watch the new chat from 07:38 Mon, window 2h30m on weekdays.
- Weekend wake trig_017N56wuJbUnFDLq31sYWfjV unchanged: its cron is limited to 14 and 15 Nov, so it never fires again.

## Carry-overs in the seed
Mandar Dandekar's release mail once Sarika confirms the date; Ryan Louvar (WisdomTree) hands-off until Akshay writes in Your call; 13 Nov ad@-only release threads all done except Mandar; Vivek Sinha published 13 Nov.

## Next
Each weekday 20:45 CTO round creates the next day's chat and its one-day wake trigger the same way.

## Rollback
As in docs/deploys/2026-11-13-zoya-day.md: disable the wake trigger, archive the chat and wait until terminal, check zoya-lock is free, re-enable the seven paused routines.
