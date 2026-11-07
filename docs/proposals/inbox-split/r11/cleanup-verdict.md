# Cleanup verdict: capture r11 (6d041a5), 3 Nov ~13:10 JST

**Accepted. No blocker.** Deploy `r11/capture.txt`, **43,905 / 45d23795c5385aa4**.

## Diff against r10 (82004b7ce0da42d7)

Exactly three edits, and nothing else moved:
1. MAILBOX's inline RAW recipe becomes HEAD.
2. STEP 0A's path 4 becomes REF, with RAW as path 5.
3. STEP 2's msgid: line reads "REF first ..., then RAW by HEAD".

There are no em-dashes.

## Can REF confirm the wrong message? No.

- A candidate counts only if `query HEADER Message-ID "<id>"` "returns this UID".
- The IMAP HEADER search is an exact match on the Message-ID header (tested 1 and 2 Nov, total 1). If it returns this row's own `[Gmail]/All Mail:<UID>`, that id is this message's Message-ID.
- Every other candidate fails the test and is skipped.
- Gmail keeps one All Mail copy per message, so a match can't land on a different copy.

**Fail-closed edge:** REF also reads Zoya's inbox, but its confirm search doesn't name a folder. A confirm run in Zoya's inbox returns her ids ("INBOX:<n>"), which never equal `[Gmail]/All Mail:<UID>`. So it fails safe, falling to RAW, and never confirms wrongly.
- **Should-fix:** say "in ad@, include_folders ["[Gmail]/All Mail"], returning [Gmail]/All Mail:<this UID>", as MSGID FIND does, so REF doesn't fall to RAW needlessly.

## HEAD (RAW): OK

- **It keeps my r5 safeguards:**
  - chunks are appended to one file (">>"), not decoded alone, so the header can't be cut at a boundary;
  - only a complete id ending ">" counts;
  - "Either way, check the id ... HEADER ... must return this message" still follows the recipe.
- **Reach:** 3 chunks of 4,000 base64 characters decode to about 9 KB of headers. In both real ad@ originals I measured (1 Nov), the Message-ID sat 6 to 7 KB in, so that's enough.
  - Heavier ARC or DKIM stacks pend, which is safe.
  - If too many rows pend that way, raise it to 4 chunks.

## Notes

- **REF takes only ids "that no Activity holds".** A row whose true id an Activity already holds won't confirm through REF. It then goes to RAW, and STEP 2's lookup folds it, so there's no duplicate, only cost. MSGID FIND normally catches that case first.

Nothing deployed by Cleanup.
