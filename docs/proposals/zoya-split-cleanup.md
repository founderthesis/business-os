# Zoya split: Cleanup's review (decision 394)

Reviewed 22 Oct on `zoya-split-build.md` at a8dd253, with d-dbl22 and Cleanup's d-dbl22-fix carried in.

## Verdict

The text passes the four checks. It is **not accepted for deploy** until Main posts the replay outputs below: the gate is behaviour on live data, not wording.

Build after Cleanup's edits (parts `actions.txt`, `reconcile.txt`, `onemail.txt`, `sending.txt`, d398 in `mail.txt` and `hard.txt`, d399 in `decision.txt` and `hard.txt`):

| Output | Bytes | sha256 (first 16) |
| --- | --- | --- |
| zoya-fast | 33,788 | 40d6fffbda4a31a2 |
| zoya-slow | 62,555 | 33e48c020b3a8657 |

The inbox, calendar and sweep ACTION KEYS deltas are unchanged from Main's table.

## Two fixes made in the parts

1. **Old-format steps could be keyed two ways.** FAST and SLOW each built a key "from the wording" at pickup. A step whose wording reads as either type could be claimed by both runs with different keys, so the idempotency key wouldn't stop a double send. Now only FAST keys old-format steps. SLOW acts only on keyed segments.
2. **Reconcile.** The stuck alert has pending and sent states (Codex, 23 Oct): a pending marker keyed `alert:<action key>` before the post, marked posted only on a message key, and a later run checks the group before any second post. Its "still due" note line now replaces the earlier one instead of stacking every SLOW run.

## Replays Main runs before deploy

Cleanup can't run a routine without its sends and writes, so Main runs each prompt as a one-off session. Each run starts with a dry-run preamble: no sends, no Notion or calendar writes. The run prints the send list (action key, To, Cc, row) and every row write it would make. Post the printed outputs on the branch.

| # | Replay | Pass when |
| --- | --- | --- |
| 1 | FAST on today's data, twice in a row | Byufuel and Escobar Bandra are in the first send list. Both runs print the same action keys, and old-format steps get the same key both times. |
| 2 | FAST and SLOW started in the same minute | No action key appears in both send lists. |
| 3 | One row with two actions (a reply and a follow-up) | Two different keys. Each run's planned write changes only its own segment and owner. |
| 4 | The 21 Oct crash case: a mail in Sent with no Activity | Thread check finds it. Planned: log once, send nothing. |
| 5 | One inbound mail answering two asks | One Activity planned, and both actions get a completion line naming it. |
| 6 | A holding reply on a row | The reply action stays open. |
| 7 | Full mailbox reread (inbox, dry run) | Zero new Activities planned. |
| 8 | SLOW reconcile with FAST's record over 90 minutes old | Stuck actions in quiet hours, holds or Akshay's pending decisions get no alert. Others get one alert each, keyed. |

## Launch gate added 23 Oct (Codex, via the CTO)

Printed dry runs alone don't pass. Main also posts:

1. **Controlled failure tests.** Kill a run after the send and before the log (mail and the stuck-alert post). The next run finds the message, logs it once and sends nothing.
2. **Concurrency tests.** FAST and SLOW write the same Engagement in overlapping runs. Both actions complete, and the row keeps both segments, both owners and both note lines.
3. **Provider idempotency.** Send the same test mail twice to a team address with the same idempotency_key, inside 24 hours. MCP Emails delivers one, and the response says so. Repeat after the window to show the thread check is what stops it then.

A replay or test that fails goes back to Main. A pass on all of them, plus Akshay's yes, clears the deploy.

## Status, 26 Oct (outputs in `split-dryruns/`)

| Gate | Result |
| --- | --- |
| Replay 1: FAST twice, same keys | **Fail.** Runs A and B on the same data differed: A held Todd McDonald and skipped Sukant; B completed Sukant and missed Todd. Neither wrote keys. Re-run twice after d-split26b and this fix; pass only on identical send lists, holds and keys. |
| Replay 2: FAST and SLOW same minute | Not run. |
| Replay 3: two actions on one row (Akshat) | **Fail**, fixed in d-segdates26 (dated segments). Re-run pending. |
| Replays 4 to 8 | Not run. |
| Failure, concurrency and provider idempotency tests | Not run. |

Cleanup's change to d-split26b: the deadlock was real (SLOW could never act on an old-format step), but letting each run key "its own types" by wording brings back the two-readings risk. Now FAST keys every old-format step it reads, any type, and writes the type into the key; SLOW acts only on keyed segments. SLOW's old steps wait at most one FAST run.

For the CTO, from fast-b.md: two Rules-page texts disagree with live rules (Client show mails sign-off "Stay awesome" vs decision 345; quiet hours 23:00 to 10:00 vs Cadences 00:30 to 07:30), and 10 rows wait on Mamatha with no Zoya step.
