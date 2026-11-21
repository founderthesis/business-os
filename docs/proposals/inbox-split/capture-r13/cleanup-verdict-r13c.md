# Cleanup verdict: capture r13c (a48fd56, with r13b 2934584), 4 Nov ~15:55 JST

**Accepted. No blocker.** Deploy `capture-r13/capture.txt`, **48,319 / 40e787a224d73a24**. It replaces the r13 I accepted, 7482f2f1.

## Rebuild

`capture-r13/patch.py` on the live r12e (9caf2cdb), twice, is byte-identical, with no em-dashes. The diff on r12e holds only these four edits:
- 457, from r13;
- 463.7, a new guest on an existing thread;
- the 0L cursor;
- the bare loop-in.

## The selection fix (CTO item B), with before and after counts

- **Before:** the live SQL matched 11 rows, and LIMIT 10 returned 10, all already carrying a "link:" line. So there were 0 actionable rows, and the same 10 were re-read each run.
- **After:** with the cursor, the same SQL returns 0 rows on today's data. New unlinked mail is reached next.
- **The mechanism:**
  - The query orders by createdTime, then url, and starts after "0L after: <createdTime> <url>".
  - The cursor advances only past rows that all carry "link:".
  - An unsettled row holds it, and at its third try it becomes "link: ... stuck".
  - That's sound: every row is either linked or settled stuck, so nothing is skipped and nothing is re-read without end.
- **Edge (low):** a row created before the cursor that later loses its link (none today) would never be reached again. LINK sunsets on 5 Nov anyway.

## The other edits

- **The bare loop-in** matches Zoya r18's wording.
- **463.7:** a mail naming a new guest on an old thread gets the new guest's own Engagement on that show, found or created by the pitch bullet's rules. The old row gets only a Claude note line. That's consistent with decision 424: it creates nothing for a booker or a merely mentioned name, because the mail has to be a pitch of that person.

Nothing deployed by Cleanup.
