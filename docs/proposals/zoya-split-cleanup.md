# Zoya split: Cleanup's review (decision 394)

Reviewed 22 Oct on `zoya-split-build.md` at a8dd253, with d-dbl22 and Cleanup's d-dbl22-fix carried in.

## Verdict

The text passes the four checks. It is **not accepted for deploy** until Main posts the replay outputs below: the gate is behaviour on live data, not wording.

Build after Cleanup's edits (parts `actions.txt`, `reconcile.txt`, `onemail.txt`, `sending.txt`, d398 in `mail.txt` and `hard.txt`, d399 in `decision.txt` and `hard.txt`):

| Output | Bytes | sha256 (first 16) |
| --- | --- | --- |
| zoya-fast | 34,837 | 67fb06d626d03c71 |
| zoya-slow | 64,676 | 567af96c27c1db2e |

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
| SLOW once (slow.md) | Informative, not a replay pass: no follow-up sends planned, 82 unkeyed steps left alone (the deadlock, fixed), 11 problems found and fixed in d-split26c (accepted in text). |
| Replays 4 to 8 | Not run. |
| Failure, concurrency and provider idempotency tests | Not run. |

Cleanup's change to d-split26b: the deadlock was real (SLOW could never act on an old-format step), but letting each run key "its own types" by wording brings back the two-readings risk. Now FAST keys every old-format step it reads, any type, and writes the type into the key; SLOW acts only on keyed segments. SLOW's old steps wait at most one FAST run.

For the CTO, from fast-b.md: two Rules-page texts disagree with live rules (Client show mails sign-off "Stay awesome" vs decision 345; quiet hours 23:00 to 10:00 vs Cadences 00:30 to 07:30), and 10 rows wait on Mamatha with no Zoya step.

d-split26c (b7924b1) accepted in text: seq keys take the step's due date at 00:00 JST; a release date counts as confirmed only when Akshay wrote it or the episode link exists; feedback is Akshay's message about Zoya's mail, not his guest-facing replies; dateless holds get a rule; the Mamatha swap covers only Zoya's steps; bounces and edit notes look back 7 days, deduped by their existing Activity or marker. SLOW is now 63,710, 1,626 B under the ceiling: the same pressure as the single prompt is coming back on SLOW.

## Scenario replays on split26c (ea4c8c5), 26 Oct 12:20 JST

Main's seven read-only replays, as reported in `split-dryruns/`:

| Replay | Main's verdict | Cleanup |
| --- | --- | --- |
| Retries (crash after send) | Pass on logic | Agree. Close its three gaps in text: a send recovered by the thread check writes the Action key; draft-then-send carries the idempotency key too; two Sent copies with one Message-ID are one send (say it in ACTIONS). |
| Same minute | Pass by rule | Agree, with one condition: route SLOW's unkeyed reply-shaped sends (vendor Your call, "they've paid" thank-you, GST ask) through FAST or key them in SLOW. |
| Concurrent asks (Akshat) | Fail | Agree. See below. |
| Contact holds | Dated pass; cold and dateless fail | Agree. |
| Capped leftovers | Fail | Agree. |
| One inbound, several asks | Outbound pass, inbound fail | Agree. |
| Holding reply | Pass | Agree; add hosts (Sri, Satish, Arjun) to RECONCILE's exemptions. |

Not accepted. What would make the failures pass, in the fewest words:

1. **Keying.** Cleanup's "SLOW acts only on keyed segments" deadlocks every follow-up on a row waiting on PR, because d-sel23 selects follow-ups by Status and Next date, and those rows have no Zoya segment. A follow-up key needs no wording: `<row>:followup:seq-<routine>-<step>:<due date>`. So SLOW keys the follow-ups it selects that way itself, and FAST keys every other old-format segment (the wording-typed ones). One run decides each key, and the deadlock goes.
2. **Concurrency.** Notion has no compare-and-set, so the re-read before a write narrows the race but can't close it. Two cheap guards: run FAST and SLOW in different minutes with a hard runtime limit, so they never overlap (FAST at :30, SLOW at :00 on even hours, each told to stop new work after 25 minutes); and after every row write, re-read the row, and if this action's own segment or owner is missing, rewrite it once and report it.
3. **Next date.** FAST needs the same rule as SLOW: Next date is the earliest open segment date. DATED SEGMENTS must also read the legacy forms ("original due <YYYY-MM-DD>"), or Main rewrites those rows once at deploy.
4. **Caps.** One definition everywhere: a cap is not a hold; the row stays due; leftovers go first next run (oldest due first, not "least recently attempted"). STEP 2's hold list, AFTER SEND and NURTURE must say the same. RECONCILE exempts rows a cap held.
5. **Holds.** A cold-outreach or dateless hold sets a recheck date (7 days) as the row's Next date, keeps an owner (Chaandini for cold outreach, never empty), and never re-asks Akshay (decision 381). ONE PERSON, ONE ASK follows Cadences' per-guest-thread PR limit.
6. **Inbound completing asks.** One sentence: an inbound message that answers our open asks completes each of them, each completion line naming the inbound Activity. Two reply actions raised by one inbound take a suffix in the key (`msg-<id>-1`, `-2`).

When these are in text, Main re-runs the seven replays, plus FAST twice on the same data (replay 1). Cleanup accepts on those outputs. The provider idempotency test and a real kill test still come before go-live.

## Replay 1, FAST twice (e922498)

Fail, and Cleanup agrees: two runs on the same data wrote 149 and 154 keys, typed one step two ways and sent different lists. Keys inferred from wording can't be stable. This supersedes fix 1 above.

Main's direction is accepted, with four conditions:
1. **Keys are migrated once, before launch.** One script builds every old-format step's key from Notion data and writes a review file: row, segment, type, origin, raised time and key, one line each. Cleanup reviews the file before anything is written, then the keys are written in one pass, with counts reconciled before and after.
2. **After the migration, no run infers a key.** FAST and SLOW act only on keyed segments. An unkeyed Zoya segment is an error: it is reported and left alone, never guessed. The inbox, calendar and sweep write the keyed form from launch, via the ACTION KEYS delta, so new unkeyed segments shouldn't appear. Snoozes keep their own form.
3. **Follow-ups chosen by Status and date** (rows waiting on PR with no Zoya segment) take the deterministic key `<row>:followup:seq-<routine>-<step>:<due date>`, built from fields, not wording.
4. **One send, two Sent copies.** Say it in ACTIONS: two Sent copies with one Message-ID are one send. The 👍 reply goes only on updates under 48 hours old.

Live check, done by Cleanup: Zoya is 65,210 / 90b11cd34a3bdca1, updated 12:28 JST. That matches d-thread26 with Cleanup's fix.

## d-split26d and the migration spec (dab24c8)

Accepted in text, with three changes in the parts:
1. **No free reading after the migration.** ACTIONS still let FAST key a later unkeyed segment "from its wording", which is how replay 1 failed. The ACTION KEYS delta covers only the inbox, calendar and sweep, so evals, host boards and WhatsApp will still write old-form Zoya steps. FAST now keys those by the migration's fixed rules only, and reports and leaves alone any it can't type. The routines can't read the repo, so Main publishes the rules from d394-migrate.md on the developer page under Rules, as a Controls page named "Zoya action keys", before launch.
2. **Overlap.** SLOW starts no new row after 25 minutes, so it never runs into FAST's :30 run.
3. Builds: FAST 34,837 / 67fb06d626d03c71, SLOW 64,676 / 567af96c27c1db2e. **SLOW is 660 B under the ceiling.** The split has refilled the larger prompt. The next SLOW addition needs an equal cut, or rules moved to Notion pages.

The migration gate stands as Main wrote it: two identical migration runs, then FAST twice with the file applied, giving identical keys and send lists. Cleanup also reviews `keys-migration.csv` before anything is written, the rule 7 splits in particular, since they edit text another owner wrote. Still before go-live: the provider idempotency test and a real kill test.
