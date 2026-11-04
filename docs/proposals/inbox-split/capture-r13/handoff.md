# Capture r13b (4 Nov)

| File | Bytes / sha256 |
|---|---|
| `capture.txt` (r13c) | 48,319 / 40e787a224d73a24 |
| r13b (replaced) | 47,384 / 4029933c61f5a975 |
| r13 (replaced) | 46,842 / 7482f2f1132bd2e6 |
| Base: live r12e (`../capture-r12/capture.txt`) | 46,565 / 9caf2cdb |

**Build:** `python3 patch.py ../capture-r12/capture.txt <out>`. It asserts the base 9caf2cdb, and each edit exactly once. Patched twice, byte-identical, no em dashes.

1. **Decision 457 (KEY):** a pitch from outside the team with ad@ on To or Cc is never left for Zoya. Capture logs it in the same run: MSGID FIND, then REF, then RAW by HEAD.
2. **Decision 463.7 (STEP 3):** a mail that names a new guest on an existing thread belongs to that guest, whatever the old row's Status: open, Parked or closed. That covers Thinking Balloon on the Parked CloudThat thread.
   - Capture finds the guest's own Engagement on that show, or creates one as the pitch bullet says, and links the mail there.
   - The old row gets only a Claude note line, never a Status or Next action change.

3. **r13c, the STEP 0L cursor (CTO item B, 4 Nov 15:05).** Rows that were already classified kept filling 0L's LIMIT 10, so the rows behind them were never reached.
   - **The fix:** the SQL now takes only rows after a cursor. "0L after: <createdTime> <url>" sits on the capture record, and the query orders by createdTime, then url.
   - **How the cursor moves:** after each batch, the run writes the last row such that it and every row before it now has a "link:" line.
   - **An unsettled row:** it holds the cursor, gets "0L try <n> <run id>", and at the third try "link: <run id> stuck <why>".
   - **The first cursor:** it starts at the last classified row, measured today.
   - **Measured read-only, 4 Nov ~15:30 JST:**
     - **Before:** the live SQL matched 11 rows, and LIMIT 10 returned 10. All 10 already carried a "link:" line: 8 "no fit" (Zencastr support, a job applicant, Substack), and 2 "recovered" by the CTO's hand batch with no fit line. So the run had 0 actionable rows and kept re-reading the same 10.
     - **After:** the same SQL with the cursor returns 0 rows. Nothing is left to link today, and new unlinked mail is the next thing it reaches.
4. **r13c, a bare loop-in (Cleanup 718ada8 point 5).** Capture's "Optionally the ask in a few words" becomes "Nothing else (CTO, 4 Nov, clarifying decision 421): no chase, offer, sponsored ask or reminder of ours and no restated ask; Zoya chases from her own inbox." That's the same as Zoya r18.

Patched twice, byte-identical, no em dashes.

**Status:** built, not replayed. Ready for Cleanup. The CTO deploys.
