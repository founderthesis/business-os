# Zoya split: Cleanup's review (decision 394)

Reviewed 22 Oct on `zoya-split-build.md` at a8dd253, with d-dbl22 and Cleanup's d-dbl22-fix carried in.

## Verdict

The text passes the four checks. It is **not accepted for deploy** until Main posts the replay outputs below: the gate is behaviour on live data, not wording.

Build after Cleanup's edits (parts `actions.txt`, `reconcile.txt`, `onemail.txt`, `sending.txt`, d398 in `mail.txt` and `hard.txt`, d399 in `decision.txt` and `hard.txt`):

| Output | Bytes | sha256 (first 16) |
| --- | --- | --- |
| zoya-fast | 36,211 | f4a541d352980139 |
| zoya-slow | 63,099 | 33ecf7c33c68d0ce |

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


## Keying migration, third build (7faa9b4)

Accepted for the write, with one rekey. Cleanup reproduced Main's file byte for byte (sha256 d837edb33231084f): 155 segments and 144 keys, no duplicates, 38 REVIEW flags and 19 notes. The only @ strings are Message-IDs, and there are no phone numbers.

The two owner-field corrections are in:
- `waiting_on_remove` takes Zoya off Ankush's row, the only one where the migration drops her last segment.
- `waiting_on_add` adds Zoya on 12 rows: the five rule 7 rows, plus Mithun Pangal, Priya Kumar, Rick Yvanovich, Dinesh Yadav, Akshit Bansal, Matthew (Magic Bus) and Vivek Iyer. Gulab Patil is no longer in scope, because his live row has no Zoya segment.

The seven drift rows, checked one by one:
- **Nikita Kumawat** and **Kumar Abhishek**: nurture n=1 on the segment's own date or on Next date. Correct.
- **Ryan Louvar**: a team data fix, dated from the Claude note. Correct.
- **Robert Mitchnick**: precall step 1 on 27 Oct by rulings 1 and 7. Correct.
- **Vivek Iyer**: Zoya's step is split out of Deepayan's segment and keyed sponsored step 2 on 2 Nov. Correct.
- **Matthew (Magic Bus)**: form chaser 1 is keyed for 29 Oct, but the row also carries Akshay's re-record question. STEP 2's skip ("Akshay holds a decision on this pursuit") stops the send until he answers. Correct, as long as that segment stays on the row.
- **Prashant Sachan: rekeyed by Cleanup.** The rules took the routine from Status Recorded, which is routine 5, the guest form. Key seq-5-1 would send guest form chaser 1 to Vineeta, but the ask is a photo and transcript feedback. Rule 9's fallback is routine 4, misc chase, so the key is now seq-4-1. Built to Share has no misc-chase wording yet (flagged 26 Oct), so SLOW blocks and reports it instead of sending the wrong mail.

Result: `keys-migration.csv` sha256 **d9366a4ef6593b5e**, identical on two builds, 155 segments and 144 unique keys.

The write still needs, at deploy and on Akshay's yes:
- The live re-read drift guard right before the write. Any row that changed since this build is rebuilt by the rules, or left out and listed, never written from the file.
- One writer.
- Counts before and after reconciled against the file.
- A read-back of every keyed segment and both owner fields.

Checks:
- Less text and fewer writers: the migration is one write by one writer, after which FAST and SLOW key by field.
- Selection by prefix or wording: the keys exist so nothing is selected by wording again. The build reads wording once, by fixed rules.
- Retry double-send: the migration sends nothing. Keys make a retry a no-op.
- Bytes and hashes: above.

## Cadence correction, and d-split26i (2ffa41c)

**Cleanup's error.** The approved SLOW cadence is `CRON_TZ=Asia/Tokyo 50 10,16 * * 1-5` (d-split26; CTO 26 Oct 17:15 JST). Cleanup's c66415e proposed `8 8-22/2`, which would mean eight launches a day, a cadence change nobody approved. It is withdrawn. That proposal had carried into 26h's SLOW intro and deploy step 4, and the 1ff6953 wording was written for it. At :50 that wording fails twice:
- "No new row after :30 past the hour you started" stops a 10:50 run before its first row.
- The 45-minute stale limit lets FAST at 11:38 treat a live 10:50 SLOW (48 minutes old) as crashed, and write alongside it.

`docs/proposals/d-split26h-fix2.py` corrects them:
- SLOW starts no new row 40 minutes after its start (11:30, 17:30).
- The lease's stale limit is 60 minutes.
- SLOW's intro reads "10:50 and 16:50 JST, weekdays".
- Deploy step 4 names `50 10,16`, with the lease as the overlap protection.

The timeline at :50:
- FAST 10:38 takes no new row after 11:03.
- SLOW 10:50 finds FAST's record Started and waits (up to 25 minutes, so until 11:15 at most). It writes once FAST closes, and starts no row after 11:30.
- FAST 11:38 finds SLOW's record either closed or Started under 60 minutes old, and waits up to 10 minutes.
- A crashed SLOW costs one FAST run (11:38 waits to 11:48, 58 minutes); 12:38 goes ahead.

The CTO's gate test, "FAST from 10:38 still running at 10:50", is Main's concurrency case. It must show SLOW reading only until FAST's record closes.

**d-split26i: accepted.** A write that changes Next action recomputes Next date, and any other write leaves it as it is. That settles the H/D difference in frozen round 1 (Akshat's owner-mail line). Holds and deferrals move the segment's "on <D Mon>", so they change Next action and stay consistent. One overlap is left: STEP 2 says "a failed send moves only Next date", without changing Next action. It's harmless on either reading, because the retry falls to SLOW's next run either way. No change made.

**Frozen round 1:** not a pass yet. C and H match on decision fields. G, D and E differ because the hypothetical inbounds had no fixed Message-IDs and run2 widened the scope. Main's round 2 fixes both in `scenarios.json`. Cleanup reviews round 2.

**Provider duplicate-send test: PASS.** Two identical self-addressed `email_compose` calls with one idempotency_key gave one send and one delivery; the second call returned `idempotent_replay`. The two Sent copies share one Message-ID, which is the known double filing. A retry that rewords the body isn't deduped by the provider, only by the thread check, so the kill/recovery case has to show that path.

**Result:** FAST 36,241 / 241555eabebac81c, SLOW 65,299 / e347c5cb20b7b720, each identical on two builds. **SLOW is 37 B under the ceiling.** The CTO's new gate item, actual token, cache and cost figures or "unknown" on each run record, adds text to RUN RECORD in both prompts. SLOW must lose about 200 B before that goes in.

Checks:
- Less text and fewer writers: the fix is a net 2 B on SLOW, and no writer is added.
- Selection by prefix or wording: none added.
- Retry double-send: the provider is proven for identical retries, and the reworded case rests on the thread check (the kill test).
- Bytes and hashes: above.

## Release cut d-split26k and d-split26j (ab182a4)

**Verdict: the cut passes with three fixes. The release build is not accepted until decision 412 is in it.**

Cleanup reproduced Main's build: FAST 35,141 / 6b3bc064ebbe1c60, SLOW 62,217 / 1a833d7a8062f1b6, identical on two runs. Cleanup's 8896129 cadence, stop and lease fixes are in.

### The 106 edits, line by line

I read every old and new string from `d-split26k.py`.
- About 60 edits drop dated attributions, AR ids, revision tags and decision numbers. None of them carries a rule.
- The pointers were checked against the text they point to:
  - Edit 9's "Outbound rows as on un#": the UN# bullet "Outbound un# rows at New or Contacted wait on no one" is there.
  - Edit 13: the intro keeps "Replies owed, Akshay's decision mails and holding replies are your FAST run's".
  - Edits 31 and 55: the same bullet still says it.
  - Edit 33: "in the window Cadences gives" stays.
  - Edit 65: un# links "only" stay in SCOPE.
  - Edit 71: the UN# first bullet keeps "pitch sheet and templates".
  - Edit 29: "Find the chat by their People Phone" stays.
  - Edit 64: WRITE PATH gives Next date and keeps other segments.

Main's least-sure edits:
- **2, 5, 12, 23, 54, 64, 66: fine.** 23 merges the two THREADING statements and keeps every step: the draft, the read-back of To, Cc and thread, the explicit To and Cc, outsiders in To with Akshay in Cc where the team wrote last, the Sent-first retry, and never a "Re:" subject.
- **26: fixed.** SENDING's crash-window check said "check your Sent and the thread first". The pointer went to ACTIONS' Before sending, which read only the thread. A fresh mail (a first step, a decision mail) has no thread, so only Sent finds it. That's the delivered-but-not-logged case in the CTO's gate item 3. ACTIONS now reads "your Sent and the thread".
- **76 and 80: fixed.** These edits dropped "Next date today or earlier" from routine 1's and routine 7's own selector lines. Read alone, either line picks rows that aren't due yet. Both restored.

Script: `docs/proposals/d-split26k-fix.py` (+78 B on SLOW, +14 on FAST).

### d-split26j

- **Lease tie-break: sound.** The earlier start holds the lease; in the same minute, FAST does. A start is recorded to the minute, so a same-second start resolves to FAST.
- **SLOW self-key replacing the waiting segment: sound, within a limit.** It replaces only the guest or PR side's "Waiting on <their side>: ..." segment for the same ask, never Akshay's or a team member's.
- **Usage receipts: fine.** Each run records its token, cache and cost figures, or "unknown" when it can't see them, never an estimate.

### Coverage of approved rules (CTO 19:30)

Main hasn't posted a coverage table, so Cleanup checked 411 to 413 against the build and Rules for Zoya, which both prompts read first every run:
- **411 (recording status settled internally; Akshay's actions go in his Notion queue):** carried by Rules for Zoya. Nothing in the build contradicts it. Transcript failures and recording questions already go on Akshay's list.
- **413 (themes from our side):** carried by Rules for Zoya. Nothing contradicts it.
- **412 (the thank-you draft goes without the transcript, as a standalone mail To the guests, Cc the PR and other stakeholders): FAILS.** SLOW's INTERNAL TASKS c(4) does three things against it:
  - it attaches the transcript to the thank-you draft;
  - it creates the FT thank-you draft only once a transcript has arrived;
  - it addresses that draft To the guest and the main PR.

  The prompt names no precedence between Rules for Zoya and its own text, so c(4) wins in practice. The decision lists "calendar and Zoya prompts with Main", so the fix spans the calendar's STEP 4c too, and it is Main's.

### Result

FAST 35,155 / ec1df0e316436ac9, SLOW 62,295 / e469a14d2cb7669d, each identical on two builds. SLOW is 3,241 B under the cap. Not frozen yet: the 412 change will move both hashes, and the frozen round, crash and lock tests must name the final ones.

Checks:
- Less text and fewer writers: 3,299 B less on SLOW, with no new writer.
- Selection by prefix or wording: none added. Edit 76 restores a date filter on a Status-based selector.
- Retry double-send: edit 26 would have weakened the Sent check, and the fix restores it.
- Bytes and hashes: above.

## Frozen build d-split26l (8e64140) and crash A (5d9c51d)

**Verdict: accepted with one fix, which moves the Zoya hashes. Inbox, calendar and sweep are accepted as frozen.**

### Reproduced

- Zoya: FAST 36,257 / 96c11beae7ec325b, SLOW 63,145 / a5b4ef40cfd85bb1, identical on two builds. Cleanup's d33ef96 restorations are in (ACTIONS reads "your Sent and the thread"; the routine 1 and routine 7 date filters).
- Inbox, calendar and sweep, rebuilt from the live prompts (inbox and calendar read by get_trigger today at 61,957 / aed0215a8bdf6a26 and 54,901 / 543c3499473860ac; sweep 33,824 / 7af60faaa021fa64) through `d394-keys.py` and `d-411-412-cal-sweep.py`:
  - inbox 63,536 / 2eade949aa242970;
  - calendar 56,272 / d9d1f508b9c797fd;
  - sweep 35,319 / 9db06d64df11ff7d.

  All three match Main's frozen hashes.

### Decisions 411 to 413, against Rules for Zoya (read today)

- **412: in.**
  - SLOW c(4) never attaches or waits for a transcript.
  - The FT thank-you is a standalone new mail ("Next Steps | ..."), To the guests, Cc the PR, every other stakeholder and the house copies.
  - Akshay gets "(draft ready)".
  - Calendar STEP 4c and 4d match.
- **411: in.** NOTION DATA's RECORDING STATUS, calendar STEP 4 a and sweep STEP 3a all settle it from our side, put the question in Akshay's Notion queue once, and never ask the guest or PR, or on WhatsApp. RECONCILE's stuck alert in the group "Zoya" is a status alert, not an ask, so it stays.
- **413: in.** Mail b takes themes from our side.
- **The Your call answer** (yes sets Recorded, no becomes the cancelled-or-no-show ask) is in notion-edits-26oct.md item 1, for the CTO to apply. Until that edit is live, the inbox reads "yes" as approving a proposal, so it is part of the deploy.

### Fixed: Mamatha and the recipient read-back

Rules for Zoya, section 2 Copies (the master): "Mamatha is never in Cc, and nothing waits on her, on any show (decisions 260, 352)". Its 413 entry is themes only. The build had:
- changed "never Mamatha" to "never add Mamatha (keep her only where she is on the latest inbound)";
- added a read-back requiring To and Cc to hold "everyone on the latest inbound", cited as decision 413.

The read-back would put Mamatha back on any thread she was on, and Sri back in Cc on un# ("Sri is never in Cc on routine mail"). The Krsnaa 17:40 mail was right to drop Mamatha. Main's open question is already answered by Rules for Zoya: never.

`docs/proposals/d-split26l-fix.py`:
- restores "never Mamatha";
- keeps the read-back but excludes "Mamatha and, on un#, Sri";
- drops the "decision 413" citation.

The read-back still catches Sreepriya's four dropped recipients.

Result: FAST 36,211 / f4a541d352980139, SLOW 63,099 / 33ecf7c33c68d0ce, identical on two builds, 2,437 B under the cap. Only SENDING changed, so frozen round 3 must run on these hashes. Crash A's trace reads ACTIONS and MESSAGE IDENTITY, which are unchanged, so it stands.

### Crash A recovery: PASS as a trace

The 19:20 self-addressed mail is in Zoya's Sent as two copies with one Message-ID, plus one INBOX delivery. Activities hold no row for it. The frozen ACTIONS ("read your Sent and the thread") and MESSAGE IDENTITY find it, so recovery plans one Activity and no send. This was Main's hand trace of what the prompt reads, not a prompt run. The Activity write is with the CTO (notion-edits item 2).

### Crash B plan: one weakness

The test puts the action key in the body as "bos-key", and recovery finds it by that marker. Real mails carry no such marker. Outside the provider window, recovery has to match by content: "a message from us after the action was raised that does what the action asks". Crash B should be judged on whether recovery finds the mail without the marker, or at least on both. Otherwise it proves less than gate item 3 asks.

Checks:
- Less text and fewer writers: the fix is -46 B, and no writer is added.
- Selection by prefix or wording: none.
- Retry double-send: crash A plans one Activity and no send; crash B is pending.
- Bytes and hashes: above.

