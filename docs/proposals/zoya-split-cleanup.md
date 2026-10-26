# Zoya split: Cleanup's review (decision 394)

Reviewed 22 Oct on `zoya-split-build.md` at a8dd253, with d-dbl22 and Cleanup's d-dbl22-fix carried in.

## Verdict

The text passes the four checks. It is **not accepted for deploy** until Main posts the replay outputs below: the gate is behaviour on live data, not wording.

Build after Cleanup's edits (parts `actions.txt`, `reconcile.txt`, `onemail.txt`, `sending.txt`, d398 in `mail.txt` and `hard.txt`, d399 in `decision.txt` and `hard.txt`):

| Output | Bytes | sha256 (first 16) |
| --- | --- | --- |
| zoya-fast | 36,160 | cf2c34ef3465d775 |
| zoya-slow | 65,229 | f43cf8b2c00d16e9 |

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

## Re-run on split26d and d-split26e (f77f04e)

Main's re-run: A, B, D, E and F pass; C (Vijay) is a partial fail and G (same minute: billing ask, vendor Your call) fails. d-split26e fixes both in text. Accepted in text; Cleanup reproduced the builds: FAST 35,144 / 36ffead8fae85afa, SLOW 64,996 / 7730656105c89751.

Before the gate closes:
1. Re-run C and G on split26e. Pass = Vijay is one hold with an owner and a recheck date; the billing ask and the vendor Your call appear in only one run's send list.
2. Fix the three live rows at launch, as Main listed (Vijay's empty Waiting on, Mekin's missing Next date, Akshat's Next date to 29 Oct). That's 3 rows, a direct write.
3. **SLOW is 340 B under the ceiling.** No further SLOW text goes in without a cut. Suggested cut, before launch: NURTURE and ONE PERSON, ONE ASK already have their master copy on Rules for Zoya section 5a, which SLOW reads every run. Point to it instead of carrying the full text. That saves about 3 KB with no rule change, but Cleanup reviews it as its own delta.
4. Unchanged: two identical migration runs, Cleanup's review of keys-migration.csv, FAST twice identical with the keys applied, the provider idempotency test, and a real kill test. The overlap guard (no new row after 25 minutes) and the Controls page "Zoya action keys" stay required.

## Keying migration file (d992814) and replay 1 with keys applied (889fd47)

**Replay 1: pass.** FAST twice with the keys applied: same single send under the same key, the same two completions by match, no new keys. The only difference was a label (held vs blocked on release-date replies). The run-twice gate passes once the label clause is in.

**keys-migration.csv, Cleanup's checks:** 155 lines, one per row; 144 keys, all unique; every key well-formed (`<row>:<type>:<origin>:<ISO +09:00>`); generated twice, byte-identical. The only `@` strings are Message-IDs, no addresses. The two 2027 dates (Nikita Kumawat, Mohit Bedi) are real revisit dates.

**Rulings on the judgement calls:** 1, 2, 3, 5, 6, 9, 10, 11, 12, 13 and 14 are accepted as Main made them. For 4 and 8, see below.

**Before the write, change the file and regenerate it (twice, identical):**
1. Fold in replay 1b's findings:
   - Sukant: the reply is complete by Akshay's 25 Oct mail; add a SLOW follow-up dated 30 Oct.
   - Ankush: drop the segment, already completed by match.
   - Release-date steps (Vineet, Anmol, Srinivas and Mandar's release part): SLOW follow-ups rechecked weekly, not FAST replies.
   - Remove the two AD Personal Task rows.
   - Ankit Utreja: write the reply-wait segment with a date and set Next date.
2. The rule 7 rows whose Waiting on lacks Zoya (Mandar, Manan Thakkar, Anirudh Damani and the rest the notes flag): add Zoya to Waiting on in the same write, as OWNERS requires.
3. Mandar's WhatsApp-raised reply: key it `reply:call-<WhatsApp Activity id>:<its date>`, so it isn't left unkeyed.
4. Mohit Bedi (judgement 4): keep n=1 from Activities, as rule 3 says; the unlogged 16 Oct check-in isn't evidence.
5. **Write the extensions into the rules.** "sponsored chase", "sponsored follow-up", "precall chase", "chases" and bare "follow-up" (by Status) count as rule 2. LT chase revisit wording counts as rule 3. Rule 3 takes its date from rule 2's chain. These go into d394-migrate.md and the "Zoya action keys" Controls page, so FAST keys later segments exactly as the migration did.

**The write:** one pass of 155 rows, direct (decision 341). Each row is read back. Counts are checked before and after: 144 keyed, 9 snoozes unchanged, the rest listed. Rule 7 rows edit another owner's text only by moving the Zoya clause out; the read-back confirms that owner's words are unchanged.

d-split26f (e976831) accepted: held is a timing rule or a host's pick, blocked is a missing fact or someone else's decision. That closes replay 1b's only difference, so replay 1 passes. FAST 35,262 / 4d493ffe6f7f888d (reproduced), SLOW unchanged.

## Keying migration, second build (083167c)

Cleanup's five changes are in, and the build checks out. 153 rows, 142 keys, all unique and well-formed, byte-identical on repeat. Replay 1b's findings are folded in:
- Sukant becomes a misc follow-up on 30 Oct.
- Ankush is dropped (done by match).
- The release-date steps (Vineet, Anmol, Srinivas, Mandar) are routine 6 step 0, rechecked weekly.
- The AD Personal rows are gone.
- Ankit Utreja gets Next date 27 Oct.
- Rule 7 rows get `waiting_on_add` Zoya.
- Mandar's step is a release-date follow-up, which is right since that is what it is.
- Mohit Bedi stays at n=1.

The rulings are written into d394-migrate.md, which Main publishes as the "Zoya action keys" Controls page.

The drift guard is accepted, and it is the right answer to rows changing between build and write. Rows whose live text no longer matches `old_segment` are rebuilt by the same rules and come to Cleanup before they're written.

The file is accepted for the write once Main's two open items are in it:
1. Ankush: Zoya comes off Waiting on, since the migration removes her last step.
2. Mithun Pangal, Priya Kumar, Gulab Patil, Rick Yvanovich and Dinesh Yadav: Zoya goes into Waiting on.

Then rebuild once more, two identical builds, and post the drift list at the write. One process point: the write is a data change of 153 rows. It happens at the deploy, on Akshay's yes in Main's chat, with the counts reconciled after.

## d-split26g (7f42237)

Accepted in text. Cleanup reproduced FAST 35,717 / c5c2c64c0ab380ae and SLOW 64,831 / bd6d25a767199f83. The NURTURE shortening bought back 165 B on SLOW, which now sits 505 B under the ceiling. Both of Cleanup's earlier guards are still in: the "Zoya action keys" rules page, and the 25-minute stop, which now covers FAST too.

Main's 26f replays (C, G, H, D, E) failed, and each failure has a matching fix in 26g:
- holds move the segment's own date
- undated holds become holds with a recheck segment
- one PR same-day rule
- the per-run cap counts this run's sends, not the day's
- leftovers go first
- restore covers note lines
- one inbound completes every ask it answers, and the -n reply keys are stored as segments
- a mailed sponsored yes is FAST's

Re-run C, G, H, D and E on 26g before the gate closes.

Accepted as residual risk, with no text fix possible: Notion has no conditional write. A third party's segment lost in a two-way race can't be restored, and row-level fields (Status, Chase step, Last activity) are last-writer-wins. The different minutes, the 25-minute stops and the re-read after each write keep the window small. The trial measures should count restore events, so the race shows up if it bites.

Data at launch, as Main listed: Vijay, Akshat and Mekin. Payal Dash's two People rows are flagged only; merging is Akshay's call, under decision 384.

Not yet on the branch: the migration write route. Cleanup reviews it when it lands.

## Overlap at the real fire times (CTO, 26 Oct 16:20 JST)

The server anchors an every-hour or every-N-hours cron to the minute it was created, so the live Zoya trigger fires at about :38, not :30, and the SLOW trigger would fire at about :50. With FAST at :38 and SLOW at :50, the two runs overlap on every even hour. A FAST run started at 10:38 may take new rows until 11:03, and SLOW starts at 10:50. **The 25-minute guards don't prevent that.**

What passes: SLOW starts at about :08 past even hours. Then FAST runs :38 to :03 and SLOW :08 to :33, each with a 25-minute guard and five minutes clear either side. Set it with a non-zero minute so the server stores it verbatim: `CRON_TZ=Asia/Tokyo 8 8-22/2 * * 1-5`. Check `next_run_at` on both triggers after the deploy. The proof Cleanup accepts is two triggers' `next_run_at` plus one weekday of run records whose start and end times never overlap.

Cleanup removed the stale ":30" from SLOW ORDER ("so you never overlap FAST's next run"): SLOW 64,832 / 763ca3d646aefde5, FAST unchanged.

The retired single Zoya trigger: the deploy repoints it to FAST and doesn't create a second hourly Zoya, so nothing retires. If Main instead creates a new FAST trigger, the old one is disabled in the same deploy, and Cleanup checks `list_triggers` shows exactly one hourly Zoya.

## d-split26h, the overlap lease (0cd9dfe)

Accepted with three fixes, applied by `docs/proposals/d-split26h-fix.py` plus three byte trims. Cleanup reproduced Main's build first: FAST 36,165 / e8e94fc6c3afb3ff, SLOW 65,194 / 3a7dd1590f30770f, identical on two runs.

What holds:
- The run record is written before the first Notion write, and the lease is checked after it. If FAST and SLOW start together, each sees the other's Started record. FAST gives up after 10 minutes and ends Partial, which closes its record. SLOW then sees no live FAST record and goes ahead. That's no deadlock, and neither run writes rows while the other does.
- A crashed run leaves a Started record that blocks the other run for at most 45 minutes. That costs at most one FAST run (the :38 after a crashed :08 SLOW). The lease waits show up in the run records.
- A run that ends on a held lease has written no row. Every send is logged before it goes, so it has sent nothing either. A retry can't send twice.
- Deploy steps 3 and 4 now repoint the existing Zoya trigger to FAST, keep exactly one hourly Zoya, and set SLOW to `8 8-22/2 * * 1-5`.

Fixed:
1. **The PR COORDINATION trim widened a rule.** "beating all of the above" sits below LIMITS in SLOW. It reads as exempting un# Booking rows from the daily cap, the follow-up window, quiet hours and Diwali week, and Diwali week is 8 Nov. Restored the named list: "beating the gaps and 30 quiet days above, the 7-day limit in LIMITS, the STALENESS GATE's span and the 3 unanswered chases".
2. **The lease and RECONCILE found the other run by Summary wording** ("Run zoya FAST"). Run records now carry the run in their key: Source ID "run:zoya:fast:<run id>" or "run:zoya:slow:<run id>". The lease and RECONCILE read by that prefix. The sweep's STEP 4b still matches on "run:zoya:". The Started state still sits in the record's Summary, as AR-8 defines it. That is the record's own state, not work selection.
3. **"No new row after :30 past any hour"** would let a SLOW run still going at 09:05 start rows again. Now it reads "past the hour you started".

The trims needed to stay under the ceiling are the lease's wait clause, SLOW's stop sentence and one phrase in SLOW ORDER. They change no meaning.

Result: FAST 36,160 / cf2c34ef3465d775, SLOW 65,229 / f43cf8b2c00d16e9. Both rebuilt twice and came out identical. Neither has an em dash or a leftover placeholder. SLOW is 107 B under the ceiling, so the next SLOW change has to cut before it adds.

Checks:
- Less text and fewer writers: the lease adds about 400 B to each prompt and no new writer. The lease is how FAST and SLOW stop being two writers at once.
- Selection by prefix or wording: the lease now selects by key, not Summary.
- Retry double-send: no.
- Bytes and hashes: above.

The split is still not accepted for deploy. Still needed: replays C, G, H, D and E on this build against frozen inputs; the concurrency, retry, hold, cap, multi-ask, kill/recovery and provider duplicate-send outputs (the concurrency run should now show a lease wait); and the migration write route. The overlap proof stays next_run_at on both triggers plus one weekday of run records.

