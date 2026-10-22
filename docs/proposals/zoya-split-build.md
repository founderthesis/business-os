# Zoya split: build for Cleanup (decision 394)

Built 22 Oct on the live prompts after the Codex batch went live (Zoya 62,409 / 6d26eaafecc9c94e). Spec: `zoya-split.md` v2.1. Nothing here is deployed. Deploy only on Akshay's yes in Main's chat, after Cleanup's checks pass.

## What's built

| Output | Bytes | sha256 (first 16) | How |
| --- | --- | --- | --- |
| zoya-fast | 30,363 | 06e02da3d8d8c6c9 | `python3 routines/zoya/build.py <out>` |
| zoya-slow | 57,681 | 37be2effa0bc451a | same |
| inbox + ACTION KEYS | 62,516 | 4ea87b9dfe33dad6 | `python3 docs/proposals/d394-keys.py <live dir> <out>` |
| calendar + ACTION KEYS | 57,246 | 74b272ae87917e5e | same |
| sweep + ACTION KEYS | 33,732 | 21abf475a49da21e | same |

- 37 part files in `routines/zoya/parts`. Every rule lives in one file. FAST and SLOW manifests and the per-prompt rewrites (VARIANT) are in `build.py`.
- Coverage: `build.py <out> <live Zoya prompt>` lists 13 live lines neither prompt carries word for word. All 13 are intended split edits: the intro, YOUR QUEUE, RUN ORDER (now FAST ORDER and SLOW ORDER), the report, the Action key edits to INTERNAL TASKS, SENDING, STEP 0e, STEP 1 a/b/e and AFTER SEND, the run-record name, and the hard WhatsApp line.
- WhatsApp routine: unchanged. Its only Zoya step is the snooze segment, which keeps its own form (spec).

## FAST is over the 25 KB target by 4,763 bytes

FAST already leaves out everything it doesn't use: WhatsApp, web search, vendor forms, internal tasks, Mail issues, peers, Task-row creation, un# routine timing, two-show follow-ups and the release-mail exception. What's left is the rules a reply or decision run needs (sending, mail, scope for the three client shows, decision mail, hard rules, actions). Getting to 25 KB means changing behavior, so it's the CTO's call. The options:

1. Accept about 30 KB as the trial size. It's still half the single prompt.
2. In FAST, drop SENDING's two paragraphs for a thread Zoya isn't on (about 1.9 KB). FAST would then loop in and send next run, the way decision mails already do. That's a slower path for short replies on threads she isn't on.
3. Point FAST at Rules for Zoya sections 2 and 4 for copies, voice and the leak, show and context checks (about 3 KB). The page is staler than the prompt (it still shows "works for us.", which decision 392 banned), so this needs a page refresh first.

## Cleanup's checks, and the text each relies on

| Check | Where in the build |
| --- | --- |
| 1. Stable identity | ACTIONS: key from the engagement, type, origin and raised time, never from our outgoing mail; old-format steps keyed at pickup and written back. SENDING: the action key as idempotency_key, SHA-256 over 200 characters. Past 24 hours: ACTIONS' thread match plus completion. |
| 2. Concurrent updates | ACTIONS, WRITE PATH: re-read the row, change only this action's segment, Waiting on entry and Claude note line. |
| 3. Useful alerts | RECONCILE: respects quiet hours, holds and pending decisions; one alert per action key, deduped by Source ID "alert:<action key>". |
| 4. One mail, several asks | ACTIONS: one Activity, each matched action completed with its own completion line. MESSAGE IDENTITY keeps it one Activity. |

The spec's go-live replays (21 Oct, crash test, same-minute FAST and SLOW, two actions on one row, a holding reply leaving the ask open, full reread, old-format steps) need dry runs against live data. They're Cleanup's.

## At deploy (Akshay's yes only)

1. Add a text property "Action key" to Activities.
2. Deploy the ACTION KEYS delta to the inbox, calendar and sweep in the same window as the split, never before: the live single Zoya prompt doesn't read the keyed form.
3. Point the Zoya trigger at zoya-fast (cron unchanged, CRON_TZ=Asia/Tokyo 30 7-23 * * *).
4. Create the SLOW trigger: CRON_TZ=Asia/Tokyo 0 8-22/2 * * 1-5, Zoya's connectors.
5. Read each back, sync `routines/`, and update the developer page and Change log.
