# Replay 1: FAST twice on the same data (split26c), 26 Oct 12:16 JST

Two read-only FAST runs, started in the same minute on build split26c (FAST 34,091 / c1b292450f738a01). Nothing was sent or written.

| | Run 1 | Run 2 |
| --- | --- | --- |
| Sends | 2: Amanda (Gather AI), "form received" mail; Prity (MaxVolt), 👍 | 2 in window: Amanda 👍, Prity 👍; plus 4 more 👍 on threads older than 72 h it advised against |
| Keys written | 149 | 154 |
| Release-date replies | keyed reply with real Message-IDs | keyed reply with "Message-ID not resolved" |
| Snooze segments | typed team | typed team |
| Steps with no number | Chase step + 1 | "?" (29 keys) |
| Ankush pi-labs step | decision | team |
| Raised times | JST offset | mixed UTC and IST offsets |
| Run record | due 7, sent 2, blocked 4 | due 12, sent 6, blocked 5 |

Byufuel and Escobar Bandra are in neither send list. Both runs read them correctly: Byufuel had nothing owed, and Escobar was declined with its close note sent.

**Verdict: FAIL.** The keys and send lists differ. Old-format keying can't be made stable from wording:
- step numbers are missing
- the nurture n is unknown
- snoozes fit no type
- some origins need Message-ID lookups
- some Zoya steps sit inside another owner's segment

Writing about 150 keys in one run also breaks decision 91.

Fix direction (next delta):
- Key the old-format steps once, as a migration before launch: one script and one reviewed file, written in a single pass, so FAST never infers a key from wording.
- Snoozes keep their own form (d394-keys.py).
- 👍 replies only on updates under 48 h old, normalised to JST.
- Message-ID lookups by Gmail rfc822msgid.

Both runs found every Zoya send filed twice in her Sent folder, with one Message-ID per pair. That points to a second filed copy, not a double delivery: the ad@ copy of the Gather AI thread shows one mail. It still needs a rule that two Sent copies are one send.
