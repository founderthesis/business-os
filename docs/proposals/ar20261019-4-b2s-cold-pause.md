# AR-20261019-4: narrow the Built to Share hold to cold outreach (19 Oct)

Akshay, 19 Oct: "keep only the cold-outreach pause". Decision 337 (Chaandini's blanket hold) stopped replies, booked calls and delivery as well as cold mail. Decision 338 narrows it. Active replies, requested later contact, confirmed calls and recorded-episode delivery carry on. Decision 328's rescinded approvals and every explicit restriction stay.

## State

| Control | Prepared | Reviewed | Deployed | Observed |
|---|---|---|---|---|
| Rules for Zoya top paragraph | yes | owner's exact text, so no review step | applied 19 Oct 15:41 JST, before Zoya's 16:30 run | no |
| Decision 338 in docs/decisions.md | yes, this commit | n/a | n/a | n/a |
| Salesblink sync prompt | yes, this commit | **not yet: needs cleanup before the 18:40 JST run** | no | no |
| 122-row relabel (Notion AI file) | yes, this commit | not yet | no | no |

Codex already restored Karri Saarinen (Next date 8 Dec 2026, Waiting on Chaandini). This package doesn't touch that row.

## 1. Rules for Zoya (3f719a301a7f81a09de3ee3ad6ad98a3), top paragraph

**Before:**
> **Built to Share outreach is on hold (Chaandini, 19 Oct: "we pause outreach for everyone - do not mention any followup date - every thing is on hold").** No follow-up, nurture, revival or Salesblink step to any Built to Share guest, and no follow-up date on any Built to Share row, until Chaandini lifts it. A mail in from a Built to Share guest goes on the row as Waiting on Chaandini; nothing is sent back. Not affected: Guy Tytunovich's booked recording, and Akshay's own relationships (decision 327). Human by Design carries on as normal.

**After (the task's exact text):**
> **Built to Share cold outreach is paused (Akshay clarification, 19 Oct).** No new cold invitations, Salesblink steps or cold re-engagement until that pause is lifted. Active/replied conversations, requested later contact, confirmed-call coordination, recorded-episode delivery and independent internal obligations continue under the current sender, owner, cadence and approval rules. Keep their owners and dated next steps. Inbound replies follow normal triage; the cold pause never suppresses a reply or erases unrelated work. Decision 328's rescinded approvals and explicit row/person/show restrictions remain in force.

## 2. Salesblink sync (trig_01KpyDSfNqRKAGEABwyMBREA)

Live base, read back 19 Oct: **8,948 B / 0be727d48ce3c933**, byte-equal to repo `routines/salesblink-sync.md`. After: **9,276 B / 6b94365084520118**. Only the "BUILT TO SHARE ON HOLD" paragraph changes. Patch: `ar20261019-4-salesblink-sync.patch`. Build: `ar20261019-4-build.py` (asserts the old paragraph once).

| | Old (337) | New (338) |
|---|---|---|
| a), d) Status and Chase step from Salesblink | not run on B2S | run; no Next date, no Waiting on |
| b) bounces | not run | run as written |
| c) replies | dateless note, Waiting on Chaandini, "outreach on hold" | in full: Status, owner and dated next step; the reply step replaces the "On hold" note (old note kept in Claude note) |
| e) new rows | blocked | created, state as a) |
| f) Unresponsive move, Re-engage date | blocked | **still blocked** (the cold step) |
| g), h) connect safety | h) blocked | run as written |
| Decision 328 | not mentioned | pre-18 Oct approvals count for nothing; a reply asks Satish afresh; Claude note and "## Standing" restrictions stand |
| HBD | as written | as written |

The cold-campaign protection stays: the sync never sends, and Salesblink stays paused. No setting in this prompt starts or restarts a campaign.

**Flag, not changed:** step c) still names Chaandini as the reply owner on both shows. That predates decision 323 (Zoya runs B2S and HBD follow-ups). Changing it would touch HBD, which is out of scope here. It's a separate item.

## 3. The 122 rows

Engagements whose Next action starts with the 337 prefix: 122, all Outbound (120 Contacted, plus Decision pending and New ones). Old steps behind "| was:": 64 Salesblink B2S counters, about 19 queued in Salesblink, about 13 Outliers needing Satish's yes, about 5 Chaandini cold adds, 5 bounced, 2 "Follow-up 1".

- **Cold:** all 122. None is a reply, a booked call, a recording or a requested later contact.
- **Ambiguous:** 2, Alexi Robichaux (BetterUp) and Craig Walker (Dialpad). ad@thepodium.in has no reply from either; their outreach went from Chaandini's mailbox, which agents can't read. Treated as cold; next check, Chaandini confirms.
- **Dates restored:** 0. No row has a source-supported date. No bulk restore.
- **Not in the set:** Karri (restored), Guy/CHEQ (Booked), AppsForBharat (Recorded), and the decision-328 held rows (they carry a different note).

Over 10 rows, so it goes to Notion AI: `ar20261019-4-relabel.md`. Prefix becomes "On hold: cold outreach paused (Akshay, 19 Oct, AR-20261019-4). No cold mail, Salesblink step or re-engagement until it lifts; a reply follows normal triage". The "| was:" part stays and the before-state goes into the Claude note. Without the relabel, the new sync still works on these rows: a reply replaces any "On hold" note.

## 4. Acceptance replays (new sync text, by hand)

| Case | Result |
|---|---|
| Cold prospect, Salesblink shows step 2 of 6 sent | Status and Chase step recorded, no Next date, no Waiting on, "On hold" note stays in front. No f). Paused. |
| New positive reply from a B2S prospect | c) in full: Replied, owner and dated next step; the "On hold" note moves to Claude note. Routed. |
| Karri Saarinen, later-contact plan | Not in the 122. a) and d) set no date on B2S, and f) doesn't run, so 8 Dec 2026 / Chaandini survives. |
| Guy / CHEQ, Booked | Not a Salesblink cold row; nothing here clears Status or Next date. Stays actionable. |
| AppsForBharat, Recorded | Same. |
| Decision-328 name replies | c) runs, approval treated as void, Satish asked afresh; Claude note restriction stands. Held. |
| HBD row | a) to h) as written, unchanged. |
| Independent FT ask | Not a B2S Salesblink row; unaffected. |

## 5. Rollback

Re-push the live base (8,948 B / 0be727d48ce3c933, equal to repo `routines/salesblink-sync.md` before this change). Rules for Zoya: put back the Before paragraph above. The relabel can be reversed from each row's Claude note line. No schema, database, scheduler or Salesblink change.

## 6. Timing (JST, 19 Oct)

- 15:41: Rules for Zoya applied.
- Now: package posted for cleanup.
- Sync deploy: as soon as cleanup accepts, before the **18:40** run if possible. Precondition: live equals 0be727d48ce3c933; readback must equal 6b94365084520118.
- If review isn't done by 18:40: the old rule runs once more. It parks any B2S reply dateless with Chaandini and sends nothing. The next run is 12:40 on 20 Oct, and any reply parked in between gets re-routed then.
- Relabel: Akshay uploads the Notion AI file whenever he's next in Notion; nothing depends on its timing.
