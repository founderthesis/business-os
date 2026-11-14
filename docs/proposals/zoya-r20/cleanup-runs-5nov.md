# Cleanup: 5 Nov run-record review (CTO asks 1 to 5), fixes for r20

Cleanup session, 5 Nov 2026, about 13:20 JST. Read-only: run records, page version history, Zoya's and ad@'s Sent and All Mail (headers only), the zoya-lock log. Nothing written outside the repo.

## 1. SLOW 11:08: Claude notes written from an SQL read

No note was shortened. I compared each row's Claude note before and after the run (page version history, 02:08 to 02:33Z) for all 16 rows the run wrote, S02 to S17. In 15 the new note is the old note exactly, with one dated 5 Nov line on top. S07 (Pritika Singh) lost two stray backslashes from an old `\\\|` escape, which became `\|`. The words, dates and links are unchanged, and no line was dropped. Each row got one note write and no repeats. The Charge Zone row (3f019a301a7f81c8a99ac2a9a29a4a2b) wasn't touched.

So the rule was broken, but no data was lost. S04 to S17 were read by SQL, and "by construction" stood in for the python step, both against r19's CLAUDE NOTE WRITES. It held this time because SQL returned these notes whole. SQL drops mentions and link destinations, so the next row with a mention or a link would lose it. S07 also shows that a write can change escapes, which a length check can't tell apart from loss.

r20 fix (wording plus a code check, so it doesn't rely on the model reading the rule):
- (a) In CLAUDE NOTE WRITES, after "never an SQL value": "SQL results, including a full column, are never a read of the note: the old note given to python is the text of a notion-fetch of that row, pasted verbatim into a quoted heredoc".
- (b) The python asserts new == line + "<br />" + old (N1). After the write it re-fetches and asserts that the stored note, with backslash escapes normalised, ends with the old note normalised the same way (N2). A miss: write nothing more, the item is unfinished ("note check failed").
- (c) Every outcome line that carries note: also carries "chk:<old length>+<line length>=<new length> fetch". 4/'s python treats a note: with no chk: as a miss, so "by construction" can't pass the outcome check.

## 2. Amit Goel decision mail, 25 Oct: sent once

Zoya's Sent holds two copies, [Gmail]/Sent Mail:550 (11:39:52Z) and :551 (11:39:39Z). A `query HEADER Message-ID "a89a9f5c-...@mcpemails.com"` (the msgid on its "Zoya sent" Activity) returns both, so they are one message. Akshay was in Cc, and ad@'s All Mail has exactly one copy (All Mail:107969). Gmail keeps two different Message-IDs as two messages, so one delivery went out.

The same thing shows on Amit Chand's 25 Oct mail: Sent :574 and :575, 7 seconds apart, one Message-ID (2439a841-...), one copy in ad@. The extra Sent copy looks like the provider saving the SMTP copy while the client also files one. No guard missed anything.

r20 fix: wherever a rule counts or compares sent mail (the Sent check, CRASH RECOVERY, the sweep's "possible duplicates" in 4b), make the unit the Message-ID and never the Sent item. Two Sent items with one Message-ID count as one send. Only two Message-IDs to the same recipient for the same action are a double send.

## 3. Hourly 12:39 Partial: not a time problem

The lock log shows the run held zoya-lock from 03:38:47Z to 03:42:35Z, under 4 minutes. The hourly has a measured 25-minute limit ("FAST work starts no new row 25 minutes after the run's start"). So "most of the run went on rules loading" isn't what stopped it.

It's a pattern. Yesterday's hourly Partials gave reasons the prompt says never count:
- 19:38: a thumbs-up left due "because quoting the 22k-character thread was costly".
- 22:38: the over-72-hour sweep "was not done this run (time)".
- 12:39: that sweep and STEP 0r skipped for "rules loading".
None cited a measured minute.

The two required pages (Rules for Zoya, 64,167 characters, and the wording page, 62,131) cost about 30,000 tokens, which is small for the context. The cause is that FAST's status isn't checked in code. "Partial: a step failed or was skipped" lets a run skip a step for any reason and still look legitimate. SLOW fixed the same thing with 4/ OUTCOME CHECK IN CODE.

r20 fix (hourly):
- (a) One line per FAST step in the record ("step <name>: done <n> | not due | unfinished (minute 25 | cap | tool error: <tool> <error>)").
- (b) The end time and elapsed from `date -u`.
- (c) A python step before the last write that parses those lines and sets the status. A step that is unfinished for any other reason, or has no line, makes the run Failed "early exit at minute <n>", never Partial.
- (d) Add "rules loading, thread length or cost is never a reason to leave a step" next to TIME.
The 12:39 record's "end see below" with no end time also fails (b).

## 4. "FAST reserve missing on Cadences": add the line to Cadences

The behaviour is right. SLOW stops 30 short of the daily cap when Cadences gives no reserve, so 120 of 150. Only the warning repeats. Add the line "FAST reserve: 30 mails a day" on Cadences. It states what already happens, so nothing changes and the warning stops. Keep the prompt's fallback and its report line, so a later edit that drops the line shows up. If Akshay wants a different reserve, that's his call, as a decision-459 row.

## 5. L1 and L2, still open

The records for 4 to 5 Nov are complete except 18:38 JST on 4 Nov (09:38Z): no record and no lock entry, as found yesterday.

Correction to my own check: run records are all there. createdTime is stored as "YYYY-MM-DD HH:MM:SSZ", so a 'T' bound in SQL drops a whole day. Any routine that filters Activities by createdTime the same way will miss rows. The prompts filter on Date and Source ID, so I know of none.

The Started-only record is the 4 Nov 10:40 JST run (40e19a301a7f8148ae70fb9604849cfc), before the r18 deploy. L1 (write a Failed record on the no-repo path) and L2 (before RELEASE, re-read the record and assert its Summary carries the status) stand as written in docs/proposals/zoya-r19/cleanup-verdict.md. Both fit in r20.
