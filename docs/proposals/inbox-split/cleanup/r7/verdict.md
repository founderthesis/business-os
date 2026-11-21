# Cleanup verdict: capture r7c and actions (ea48aed), 2 Nov ~11:30 JST

Blockers only.

**Accept with one blocker fixed.** Deploy together:
- capture: `cleanup/r7/capture.txt`, **39,522 / 3f08b76efda59776**, which is r7c plus one replacement (`cleanup/r7/fix_r7c.py`). Built twice, byte-identical, with no em-dashes. It's built for the 2026-11-03 cutoff; for another date, rebuild r7c with that date and apply the same one replacement.
- actions: `r7/actions-v2.txt`, **39,553 / c80b1cee0fdecbee**, unchanged.

## Rebuild

`r7/patch.py ../cleanup/r6/capture.txt ../actions-v2.txt <out> 2026-11-03`, run twice, reproduces both outputs byte for byte: capture 39,481 / 4c22ac5037dc8874 and actions 39,553 / c80b1cee0fdecbee. Neither has em-dashes, and the diffs hold only the r7 edits.

## Blocker

**B1. MSGID FIND misses most existing msgid: rows, so pre-cutoff ad@-only mail gets a duplicate adid: row.**
- MSGID FIND's candidates need "People overlapping its From, To and Cc".
- **Measured live (read-only):** of the 36 msgid: Email in/out rows dated since 31 Oct, **33 have no People**. That covers Zoya's sends and inbound like "Akshit Bansal (Statiq) to Akshay", "Team Nxt to ThePodium" and "Dhiraj Jain to Akshay".
- For ad@-only mail received before the cutoff, MSGID FIND is the only check. With no candidate, it keys `adid:<UID>`, and that makes a second row for mail r5/r6c already logged.
- **Fix:** Activity Date holds the message time to the minute (all 36 rows are datetimes). Candidates become "Date within 2 minutes of the message (People or not), or within a day with People overlapping its From, To and Cc", each still confirmed by the HEADER search returning this UID. That's a tight candidate set, and the confirm step is unchanged.
- The same fix stops Zoya-on mail waiting 2 hours and then fetching raw when her row has no People.

## Checked, not blocking

- **Duplicates with Zoya's rows:**
  - Mail sent from ad@ is fetched raw and keyed msgid:, so the full lookup finds Zoya's row or the earlier one.
  - Zoya-on mail is either matched to her row through MSGID FIND, or after 2 hours fetched raw and caught by the msgid lookup. No duplicate either way.
- **Actions picks up adid: rows:**
  - STEP 1's query takes "msgid: or adid:";
  - THREAD for an adid: row uses the subject search;
  - a gmail: thread key becomes the first message's key.
- **The 2-hour wait can't stall read-to for good:**
  - "never past ... a Zoya-on one left for her under 2 hours" holds the cursor for at most 2 hours;
  - after that the mail is fetched raw and either logged, or pended `mcp:`, which doesn't hold the cursor.
- **D6 (Zoya on Bcc or a team alias):** a possible duplicate, rare and visible. It's a follow-up on Zoya's side, as Main proposes.
- **D12 (Zoya logging a send without a msgid: key):** not blocking.
  - Every "Zoya sent:" row since 31 Oct has a msgid: key.
  - Only the two older invented keys (28 and 29 Oct) exist, and they still need re-keying.
- **Follow-up:** Akshay's own sends are still fetched raw, the heavy path. That's fine for now; watch throughput.

Nothing deployed by Cleanup.
