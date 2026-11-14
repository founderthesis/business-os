# Tidy Next action (Akshay, 1 Nov, via the CTO)

**The problem.** Next action carries Zoya's action keys ("[reply msg-<Message-ID> <ISO>]"), multi-sentence history and finished steps, so Akshay can't read it. Adrian's un# row is the example.

**The change.**
1. **Keys move out.** A new Engagements text field, "Action keys", holds Zoya's keys, one per line as "<short name> = <key>". Next action never holds one. Zoya's KEYS rule (actions.txt) also rewrites every "Zoya [<key>]: <step>" template in her prompts as "Zoya: <step>" plus that line, and moves old bracketed keys out on her next write to a row.
2. **One line per step.** Next action is one line per open step, "<owner>: <what>", about 80 characters, joined by " | ". History, past message dates and reasons go in the Claude note.
3. **Done steps leave.** Completing or superseding a step removes it, and its key, in the same write. A write that moves Status forward, or passes the call date, drops the earlier stage's steps.
4. **Sweep trim step.** Sweep Part A gets STEP 3t. It trims finished or past-stage steps, segments over 120 characters and bracketed keys, at most 30 rows a run, each with a Claude note line. It never drops a step whose key is still open or that waits on a decision.

**Deploy order.** Create the "Action keys" field first (text, on Engagements; approved, created at deploy). Then deploy the prompts. Then the backfill.

## Files (round 2; each built twice, byte-identical)

| Routine | File | Bytes / sha256 | Built on |
|---|---|---|---|
| Zoya FAST | `zoya-one.txt` | 43,565 / e04512accf236171 | pinned to SLOW at 39a5cce; includes the CTO's 13:55 decision-action fix |
| Zoya SLOW | `routines/zoya/release/zoya-slow-work.txt` at 39a5cce90dfd468ecd3bdfe413e5ef9981b4313d | 64,714 / 9403ac13d1527139 | f70901f |
| Inbox | `inbox.txt` | 65,306 / dcd1c44215676619 | the msgid patch rev 2, 65,233 / debcde463cd9cd0f |
| Calendar | `calendar.txt` | 58,379 / 60535446d9b0d650 | B1, 57,968 / f6d140196f3b75b4 |
| Daily sweep | `sweep.txt` | 36,093 / 642eb4bd576c1d93 | accepted d420, 35,047 / 06c4120b2cd48ef1 |
| Host boards | `hostboards.txt` | 8,885 / 8a3fd4b5a3bb6b77 | live, 8,474 / 5819ccf7528ca16f |

**The inbox needed a trim.** It's now 39 bytes under the build limit. The room came from:
- three sentences that repeat earlier rules ("zero rows", "Kind follows the From header", HOURLY's look-back explanation);
- the repeat-pitch template's history ("Earlier: <date> to <name>, <subject>, <what we said>"), which now goes in the Claude note, as the new rule says.

**Pin.** At deploy, Zoya's pin moves to 39a5cce. Cleanup accepted the d420 Zoya build at f70901f, and this build sits on top of it.

## Replay (`replayNA.json`) and round 2

Every round 1 diff held only the intended edits, and Z1, I1, H1 and the sizes passed.

| Case | Round 1 finding | Round 2 fix |
|---|---|---|
| Z2 | A step with a bracketed key counted as old-format, so its key was rebuilt | Old-format means "no Action keys line and no "[...]"; a "[...]" is its key" |
| Z3 | The key-writing phrases weren't covered, and nurture never moved its key line on | KEYS covers "writes a key onto a segment"; a send that moves a step on replaces its line with the next key. WRITE PATH now lists the Action keys line and allows the bracket move and NEXT ACTION's drops |
| Z4 | Short names could prefix each other | No short name is the start of another on the row; a segment's key is the line whose name its step starts with |
| S1 | Sweep 3t didn't define the short name, and shortening could break the match | Defined, and kept when shortening |
| Others | Removing a done step left its key behind; long templates conflicted with the rule | The other routines' rule says the step leaves with its key; templates follow the rule, with history in the Claude note |

Round 2 hasn't been re-replayed.

## One-off backfill plan (read-only first)

**1. Inventory (read only).**
- Query open Engagements. For each, count:
  - bracketed keys in Next action ("[" followed by reply, decision, hold, followup, nurture or team);
  - segments (split on " | ");
  - segments over 120 characters;
  - segments tied to a past stage: an "Ask Akshay to approve" ask on a row past Decision pending, or a precall step on a row past Precall done.
- Write a review CSV to `data/` with each row's id, the current Next action, the proposed Next action, the proposed Action keys, and the proposed Claude note line.
- Report the counts.

**2. Review.** Rows whose proposed text drops a step that isn't plainly done go to the report, not the write.

**3. Write (one Notion writer).**
- Run while no Zoya run holds the lock: between :46 and :37, so never :38 to :45. Zoya also re-keys rows in her own runs.
- For each row: set Action keys, set the new Next action, and add a Claude note line "YYYY-MM-DD: Next action tidied (backfill): keys moved, <what removed>".
- Batch the writes.
- Do a drift check before each write: if the row changed since the inventory, skip it and list it.

**4. Reconcile.**
- Re-query. There should be zero bracketed keys left in Next action and no segment over 120 characters, except the listed rows.
- Every key in the inventory should be on its row's Action keys.
- Report counts before and after.
