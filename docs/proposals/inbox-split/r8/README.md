# Capture r8 (CTO, 2 Nov 12:25 JST)

**Base:** the live r7, `../cleanup/r7/capture.txt`, 39,522 / 3f08b76e.
**Build:** `patch.py` makes eight edits, each asserted once. Built twice, byte-identical.

| File | Bytes / sha256 |
|---|---|
| `capture.txt` | 39,999 / 64da655e68a0371e |

| # | Change | Where |
|---|---|---|
| 1 | **LINK class in STEP 0:** mail rows (msgid: or adid:) with no People and no Engagement, created since 2026-11-01T03:00Z, Captured before today. Superseded by r8b and r8c below: LINK sits inside STEP 0's 15 and runs through 5 Nov | STEP 0 |
| 2 | **allmail: rows that are ad@-only** (and not sent from ad@) re-key to adid:<UID> with no RAW. MSGID FIND and STEP 2's lookup still run first. An id outside All Mail is found there by from, subject and date | STEP 0 |
| 3 | **RAW returned inline** is written to a file, the whole value in order, 8,000 characters per appended heredoc. The decode strips newlines, so the chunk boundaries don't matter, and runs after each chunk. It stops once a complete id shows. The existing rule that a failure pends as mcp: and never stops the run is unchanged | MAILBOX RAW |

**Why "Captured before today" and not "regardless of Captured":** Notion can't filter on body text, and STEP 0 marks a row as tried by setting its Captured. Without that cut, a row that can't be linked would come back every run and use cap slots for nothing.

## r8b (replay8.json)

| Defect | Fix |
|---|---|
| D1, high: one shared file `f` | Inline RAW goes to a new file per message: `cat > r<id>` for the first chunk, `>>` after. The decode reads `r<id>` |
| D2: the cap rules contradicted each other | LINK is a third STEP 0 class, inside STEP 0's 15. It never counts toward STEP 1's cap or BACKLOG, so new mail keeps its slots. This departs from the CTO's "BACKLOG cap" wording |
| D3: the pass never ended | LINK runs until 2026-11-06. Today's 14 rows link from 3 Nov: Captured can't mark them today, and Notion can't filter on body text |
| D4: Kind filter and Zoya's rows | msgid: or adid: mail only, and never an Email out whose Summary starts "Zoya" |
| D5: double pending | A STEP 0 row whose RAW fails gets the body line only, never an mcp: pending entry |
| D6: a loop-in from linking | LINK only links, with no loop-in |
| D7 | The 65,336 guard is the cap minus a 200-byte margin, on purpose. r8b is 39,999 B |
| D8: the shape of the data value | A real `original` result fetched on 1 Nov had standard base64 in one unbroken string, which the recipe fits |

## r8c (replay8.json, r8b section)

| Item | Fix |
|---|---|
| N1, medium: undefined file name | The file is `r<UID>`, with UID as KEY defines it, so the name has no slash or colon |
| N2: quota | STEP 0 takes up to 5 of each of its three classes, the others filling the rest |
| N3: LINK created nothing | LINK creates what STEPS 2 and 3 would (People, an Engagement for a pitch), never a loop-in |
| N4 | LINK runs "through 2026-11-05" |
| N5 | This README and patch.py's comments are updated |

**For the CTO:** LINK doesn't use the BACKLOG cap you named. It sits inside STEP 0's 15, so new mail keeps its 15 or 25 slots.
