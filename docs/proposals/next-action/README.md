# Tidy Next action (Akshay, 1 Nov, via the CTO)

**The problem.** Next action carries Zoya's action keys ("[reply msg-<Message-ID> <ISO>]"), multi-sentence history and finished steps, so Akshay can't read it. Adrian's un# row is the example.

**The change.**
1. **Keys move out.** A new Engagements text field, "Action keys", holds Zoya's keys, one per line as "<short name> = <key>". Next action never holds one. Zoya's KEYS rule (actions.txt) also rewrites every "Zoya [<key>]: <step>" template in her prompts as "Zoya: <step>" plus that line, and moves old bracketed keys out on her next write to a row.
2. **One line per step.** Next action is one line per open step, "<owner>: <what>", about 80 characters, joined by " | ". History, past message dates and reasons go in the Claude note.
3. **Done steps leave.** Completing or superseding a step removes it, and its key, in the same write. A write that moves Status forward, or passes the call date, drops the earlier stage's steps.
4. **Sweep trim step.** Sweep Part A gets STEP 3t. It trims finished or past-stage steps, segments over 120 characters and bracketed keys, at most 30 rows a run, each with a Claude note line. It never drops a step whose key is still open or that waits on a decision.

**Deploy order.** Create the "Action keys" field first (text, on Engagements; approved, created at deploy). Then deploy the prompts. Then the backfill.

## Files (each built twice, byte-identical)

| Routine | File | Bytes / sha256 | Built on |
|---|---|---|---|
| Zoya FAST | `zoya-one.txt` | 42,879 / 05927d11c1225f47 | parts at 6948d57, pinned to SLOW at 6948d57 |
| Zoya SLOW | `routines/zoya/release/zoya-slow-work.txt` at 6948d572794c9cf38a7f0ee3bbe4544376837108 | 64,387 / 20bc0a0389291942 | f70901f |
| Inbox | `inbox.txt` | 65,336 / f960013dfd8bc96e | the msgid patch, 65,334 / 2f3250ed1d45e7db |
| Calendar | `calendar.txt` | 58,332 / 616420ef070ba51f | B1, 57,968 / f6d140196f3b75b4 |
| Daily sweep | `sweep.txt` | 35,983 / 5370749162eb70d6 | accepted d420, 35,047 / 06c4120b2cd48ef1 |
| Host boards | `hostboards.txt` | 8,838 / a7d31a70b3b491d2 | live, 8,474 / 5819ccf7528ca16f |

**The inbox needed a trim.** It's now exactly at the build limit, 200 bytes under the real cap. The room came from three sentences that repeat earlier rules:
- "The same mail read again ... makes zero rows" repeats "one Activity per message, ever".
- "Kind follows the From header" repeats the Kind line below it.
- The HOURLY paragraph's explanation of the look-back windows.

Its NEXT ACTION rule is the short form. The next inbox change needs a real cut. Candidates: the MAILBOX paragraph once every routine is on MCP Emails, and the release-date aside, which decision 427 may have overtaken.

**Pin.** Zoya's pin moves from f70901f (or wherever it is at deploy) to 6948d57. Cleanup accepted the d420 Zoya build at f70901f, and this build sits on top of it.

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
