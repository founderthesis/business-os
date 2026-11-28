# Capture r11: REF path before RAW (CTO, 3 Nov ~13:15 JST)

## Why
The 12:02 capture run worked 0 of 10 old allmail rows. Its record said each needed a RAW fetch, whose base64 (about 14 KB) came back inline and had to be copied through Bash by hand, so it stopped. The 11:03 run worked 3 of 10 for the same reason. Running more often wouldn't fix this.

## What changes (three edits to r10 capture.txt, nothing else)
1. **STEP 0A path 4 becomes REF.** For mail sent from ad@, or with Zoya on it, and no MSGID FIND match:
   - read the thread's later messages with read_batch, body_max_chars 0;
   - collect the ids in their In-Reply-To and References that no Activity holds;
   - HEADER-confirm each until one returns this UID. No RAW is needed.
   RAW becomes path 5, by HEAD.
2. **MAILBOX RAW recipe (HEAD).** The run copies only the first 4,000 base64 characters; base64 decodes in 4-character groups, so the headers come out on their own. It adds the next 4,000 only if no id appears, up to 3 chunks, then pends the row. It never copies the whole message.
3. **STEP 2.** For a msgid: key: REF first, then RAW by HEAD.

## Evidence (CTO, by hand, 3 Nov)
- Row 108690 (Akshay to Robert Ford, 29 Oct).
- 108692's In-Reply-To was CAPzDPD8rme5...@mail.gmail.com.
- query HEADER Message-ID "<that id>" returned [Gmail]/All Mail:108690, total 1.
- That took 3 MCP Emails calls and no RAW.

## Size
43,905 bytes (r10: 43,475).
