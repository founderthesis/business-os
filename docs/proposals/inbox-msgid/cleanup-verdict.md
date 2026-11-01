# Cleanup verdict: inbox Message-ID patch (1 Nov)

**Accepted as Cleanup's rev: `cleanup/inbox.txt`, 65,328 / 32697b029b1fde5f.** Main's build, 65,334 / 2f3250ed1d45e7db, isn't accepted as it stands. The rev is Main's build plus four small edits (`cleanup/patch2.py`). Built twice, byte-identical, 8 bytes under the build limit, em-dash count unchanged.

## What I checked

- **Live base.** I read the live inbox trigger back at 1 Nov 04:50Z: 65,325 / e6cf4db2bc37918b, enabled, cron `2 7-23` JST. That's the cap build.
- **Main's build.** `patch.py` on the cap build reproduces 65,334 / 2f3250ed1d45e7db byte for byte. The diff holds only the intended edits, in STEP 1, IDENTITY and STEP 2's batching.
- **What's right in it.**
  - "no Message-ID, no Activity" and "never skipped to save load" close the 12:12 and 13:02 path.
  - The `allmail:` fallback is gone, and the lookup now finds `allmail:` rows.
  - "Each gets STEPS 2 to 6e before the next" plus "Batch one message's creates" force full steps per message.
  - "the cap is the approval ... or asking Akshay" ends the backlog-approval asks.
  - The round-1 fixes for M1 to M5 read correctly.

## Why it needed a rev

**1. One unreadable mail would freeze the inbox cursor for good (blocking).**
- The run record's "read to" is "never past a pending one", and the pending line is "carried ... never dropped".
- An `mcp:` entry stays pending until its Message-ID can be read. If it never can (the message was deleted, its UID is gone, or the tool errors on it every time), "read to" never moves again.
- After that, every run starts from the same T and re-reads a window that keeps growing.
- An `mcp:` entry is retried by id, not by the window, so it doesn't need to hold the cursor.
- **Fix:** "never past a pending one but an mcp: one". It stays on the pending line and in the over-24h report.

**2. Taking out the 50 KB guard brings back the heavy reads (blocking).**
- The guard went in on 29 Oct (558e6c0) for exactly this. `original` returns the whole stored message as base64 .eml, so a mail with a pitch deck attached puts megabytes into the run's context. There is no headers-only source for the Message-ID: a `body_max_chars 0` read doesn't carry it, I checked this on 29 Oct, and ad@ is generic IMAP.
- Restoring the guard as a skip would break the CTO's rule, because large pitches would never get an Activity.
- **Fix: a bound, not a skip.** "at most 2 with attachments over 50 KB a run, the rest wait". "Wait" has the same meaning as the cap's: not logged, not pending, and "read to" stops before it. A run of decks clears at 2 an hour. Nothing is ever skipped.

**3. "Work it as new" could make a second Activity (should fix).**
- STEP 2 continues "Otherwise create one Activity:", so a model can re-key the `allmail:` row and then create a fresh one.
- **Fix:** "work it as new on that row".

**Room for the fixes.**
- I cut "(never collapsed by sender, subject or time)". The next sentence already says "Date and recipient alone never match".
- IDENTITY now says "get it from RAW". The Gmail tool map at the top already defines RAW as `email_read original` (decode it in Bash, keep only the Message-ID line).
- None of these strings are ones the Next action patch replaces.

## Next action inbox rebases cleanly

- `docs/proposals/next-action/patch.py inbox` on 2f3250ed reproduces 65,297 / 932472e0a326181e.
- With only its INPUT hash changed to 32697b029b1fde5f, it applies to this rev and gives **65,291 / 2352e359308b3306**, with 45 bytes of headroom.
- Main should rebuild Next action's inbox on this rev, not on 2f3250ed.

## Reconciliation plan (`reconcile-allmail.md`)

**Accepted, with four changes:**
1. **Timing.** Run it only after this rev is live. Until then every hourly run can add `allmail:` rows. Also use the Next action backfill's window, **:46 to :37, never :38 to :45**. ":10 to :55" overlaps Zoya's :38 run, and she writes Activities too (one Notion writer).
2. **Scope.** Don't stop at 15. Inventory every `allmail:` row: the 13:02 run and any later one added more.
3. **Class A linking.** Link to existing People, Engagement and Deal rows only. Create nothing, and follow decision 424: a booker is never the guest, and a match on organisation or domain alone links nothing and goes to the list.
4. **Loop-ins.** STEP 6's catch-up looks back only 72 hours. List every re-keyed pitch older than that which never got a loop-in, so it's caught in the report rather than missed.

Class B (fold into the `msgid:` row, check no relations are left, then Trash under decision 416) and class C (leave and list) are right as written.
