# Zoya split: build for Cleanup (decision 394)

Built 22 Oct on the live prompts after the Codex batch went live (Zoya 62,409 / 6d26eaafecc9c94e). Spec: `zoya-split.md` v2.1. Nothing here is deployed. Deploy only on Akshay's yes in Main's chat, after Cleanup's checks pass.

## What's built

| Output | Bytes | sha256 (first 16) | How |
| --- | --- | --- | --- |
| zoya-fast | 30,689 | ebd8c8dac2ccce0d | `python3 routines/zoya/build.py <out>` |
| zoya-slow | 58,007 | 6c118861da53c4d4 | same |
| inbox + ACTION KEYS | 62,516 | 4ea87b9dfe33dad6 | `python3 docs/proposals/d394-keys.py <live dir> <out>` |
| calendar + ACTION KEYS | 57,246 | 74b272ae87917e5e | same |
| sweep + ACTION KEYS | 33,732 | 21abf475a49da21e | same |

- 37 part files in `routines/zoya/parts`. Every rule lives in one file. FAST and SLOW manifests and the per-prompt rewrites (VARIANT) are in `build.py`.
- Coverage: `build.py <out> <live Zoya prompt>` lists 13 live lines neither prompt carries word for word. All 13 are intended split edits: the intro, YOUR QUEUE, RUN ORDER (now FAST ORDER and SLOW ORDER), the report, the Action key edits to INTERNAL TASKS, SENDING, STEP 0e, STEP 1 a/b/e and AFTER SEND, the run-record name, and the hard WhatsApp line.
- WhatsApp routine: unchanged. Its only Zoya step is the snooze segment, which keeps its own form (spec).

## FAST size: about 30 KB for the trial (CTO, 22 Oct)

The CTO accepted about 30 KB for the trial: keep the rules for threads Zoya isn't on yet, and don't move rules to run-time page reads. The actual byte counts go in the trial log (above, and on the developer page at deploy). Trim after week 1 if FAST runs over time.

## Added on the CTO's notes of 22 Oct

- Version on the run record: each prompt's RUN RECORD writes its deployment reference as "zoya-fast a6d4dd148d42" or "zoya-slow 92cdf09faef9", the first 12 hex of the sha256 of the prompt with the stamp written as @@VERSION@@. build.py stamps it, so the trial measures can tie each run to a version. Only Zoya writes run records; the inbox, calendar, sweep and WhatsApp routines have none.
- Reply recipients: SENDING now says MCP Emails' reply goes to the thread's last sender, so when the last message is ours, Zoya creates a draft reply, sets To and Cc, reads it back, and sends that draft (from the 12:38 run).
- Rules for Zoya page: "works for us." becomes "that time is fine for us." (decision 392). This is a page edit, applied in the deploy window below.

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
5. On Rules for Zoya, section 1, Zoya's tone: replace "works for us." with "that time is fine for us.".
6. Read each back, sync `routines/`, update the developer page and Change log, and record FAST and SLOW bytes and version stamps in the trial log.
