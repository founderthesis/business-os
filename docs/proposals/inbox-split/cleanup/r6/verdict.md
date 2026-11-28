# Cleanup verdict: capture r6b (2811c39), 2 Nov ~02:10 JST

Blockers only, as the CTO asked.

**Accept with one blocker fixed.** Deploy `cleanup/r6/capture.txt`, **38,121 / d0f0e9bb407b7f5a**, not 9b55110e. It's r6b plus the same one replacement as `cleanup/r5/fix2.py` (`cleanup/r6/fix_r6b.py`). Built twice, byte-identical, with no em-dashes.

## Rebuild

- `r6/patch.py` on the live r5 (`cto-r5/capture.txt`, 405a30d3) reproduces **37,954 / 9b55110e2cead4c2**. Built twice, byte-identical, and the same as the repo file.
- The diff holds only the listed edits:
  - OVERLAP;
  - STOP TIME relative to the run's start;
  - working to the cap;
  - STEP 0's 8-minute stop and its full lookup before any fold or re-key;
  - BACKLOG 25;
  - read_batch;
  - Message-IDs taken from References and confirmed by HEADER;
  - the narrower Stakeholders sweep.

## Blocker

**B1. The live r5 recipe can store a truncated Message-ID, and r6b keeps it.** This is the defect in `cleanup/r5/verdict.md`, reproduced there.
- r5 went live as 405a30d3 before that review landed. r6b is built on it, so it still says "not there, the next 8000 (offsets multiples of 4)". Each chunk is decoded on its own.
- A Message-ID header across the 8,000-character boundary decodes as a cut-off id (`CAN8JMk1W=sG`). The run would store that as the `msgid:` key, which makes a wrong key and a duplicate row, and later lookups miss it.
- It's likely to hit: in both real ad@ originals I read, the header sits past base64 offset 8,000.
- **Live check (read-only):** no `msgid:` row created since 28 Oct lacks a full "@domain", so it hasn't hit yet.
- r6b's References path already checks with HEADER. The RAW path doesn't.
- **Fix (one replacement):**
  - With no complete id (one ending ">"), append the next 8000 to the same file and run it again.
  - On either path, check the id with query HEADER Message-ID "<id>": it must return this message, otherwise the message pends.

## Not blocking (follow-ups)

- **Two old Zoya rows have invented keys:** "msgid:INBOX564-ragini-2026-10-29T04:32:59Z" (29 Oct) and "msgid:mcpemail-INBOX544-anuradha-20261028" (28 Oct). They aren't real Message-IDs, so STEP 2's lookup will never match them. Look at Zoya's logging and re-key these two.
- **Hand runs:** the overlap guard doesn't cover Zoya's :38 run. The hand-off already says never to run between :35 and :50.

Nothing deployed by Cleanup.
