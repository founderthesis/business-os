# Zoya split: build for Cleanup (decision 394)

Built 22 Oct on the live prompts after the Codex batch went live (Zoya 62,409 / 6d26eaafecc9c94e), with d-dbl22, Cleanup's d-dbl22-fix and decision 398 (d398) carried in (Zoya with all three: 64,133 / b961623ed7462720), and Cleanup's edits to the parts (zoya-split-cleanup.md). Spec: `zoya-split.md` v2.1. Nothing here is deployed. Deploy only on Akshay's yes in Main's chat, after Cleanup's checks pass.

## What's built

| Output | Bytes | sha256 (first 16) | How |
| --- | --- | --- | --- |
| zoya-fast | 32,256 | 027280c16715df43 | `python3 routines/zoya/build.py <out>` |
| zoya-slow | 59,590 | 4ec8f42428b4c4cc | same |
| inbox + ACTION KEYS | 62,516 | 4ea87b9dfe33dad6 | `python3 docs/proposals/d394-keys.py <live dir> <out>` |
| calendar + ACTION KEYS | 57,246 | 74b272ae87917e5e | same |
| sweep + ACTION KEYS | 33,732 | 21abf475a49da21e | same |

- 37 part files in `routines/zoya/parts`. Every rule lives in one file. FAST and SLOW manifests and the per-prompt rewrites (VARIANT) are in `build.py`.
- Coverage: `build.py <out> <live Zoya prompt>` lists 14 lines of the patched prompt that neither split prompt carries word for word. All 14 are intended split edits: the ONE MAIL PER PERSON bullet (now its own part, onemail, in both prompts), the intro, YOUR QUEUE, RUN ORDER (now FAST ORDER and SLOW ORDER), the report, the Action key edits to INTERNAL TASKS, SENDING, STEP 0e, STEP 1 a/b/e and AFTER SEND, the run-record name, and the hard WhatsApp line.
- WhatsApp routine: unchanged. Its only Zoya step is the snooze segment, which keeps its own form (spec).

## FAST size: about 30 KB for the trial (CTO, 22 Oct)

The CTO accepted about 30 KB for the trial: keep the rules for threads Zoya isn't on yet, and don't move rules to run-time page reads. The actual byte counts go in the trial log (above, and on the developer page at deploy). Trim after week 1 if FAST runs over time.

## Added on the CTO's notes of 22 Oct

- Version on the run record: each prompt's RUN RECORD writes its deployment reference as "zoya-fast f6703180f687" or "zoya-slow dcf544029889", the first 12 hex of the sha256 of the prompt with the stamp written as @@VERSION@@. build.py stamps it, so the trial measures can tie each run to a version. Only Zoya writes run records; the inbox, calendar, sweep and WhatsApp routines have none.
- Double sends (d-dbl22, CTO 22 Oct): ONE MAIL PER PERSON PER RUN groups each run's sends by To address, in FAST and SLOW alike (action keys are per Engagement, so they don't catch it); SENDING builds a reply as a draft with To and Cc from the thread wherever the team wrote last, and never sends a mail whose only recipients are team.
- Rules for Zoya page: the CTO already removed "works for us." (22 Oct), so it is off the deploy list.
- Decision 398 (a call cancelled in writing is admin): Zoya's mail and hard-rule lines carried into the mail and hard parts. The ACTION KEYS delta's calendar base is today's live calendar; once d398 is live (calendar 57,489 / c80b63e6bcf2e6ee), rebase d394-keys.py on it before the split deploys.
- Decision 399 (never describe the guest's company): no part file asks for a business detail. The inbox's STEP 6c instruction goes in d399.py; once it is live, rebase d394-keys.py's inbox base on it too.
- Decision 395 (LinkedIn numbers are "us" and rounded, no breakdown): no part file carries audience numbers or show facts; mails take them from the sales page and Rules for Zoya, which already carry 395. Nothing to change in the build.

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
5. Read each back, sync `routines/`, update the developer page and Change log, and record FAST and SLOW bytes and version stamps in the trial log.
