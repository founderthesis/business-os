# Capture r7c: for the CTO to relay to Cleanup and deploy (2 Nov)

**Ready.** The offline replay (`replay7.json`, sections r7, r7b and r7c) passes every case the CTO listed except case 8 (Zoya on Bcc), which is partial on Zoya's side. Nothing was deployed by this session.

| File | Bytes / sha256 | Base |
|---|---|---|
| capture.txt | 39,481 / 4c22ac5037dc8874 | live r6c, 38,121 / d0f0e9bb |
| actions-v2.txt | 39,553 / c80b1cee0fdecbee | live actions, 39,354 / 19701651 |

Both were built twice, byte-identical, with `patch.py`.

**At deploy:**
- **Go-live day.** Rebuild with the go-live day (JST) as the 4th argument if it isn't 2026-11-03: `python3 patch.py ../cleanup/r6/capture.txt ../actions-v2.txt <out> <YYYY-MM-DD>`. Ad@-only mail received before that day is first checked against the msgid: rows older runs made. A wrong date means duplicates for mail r6c had already logged.
- **Deploy both prompts together.** Capture's new adid: rows are worked only by the new actions.
- **Sweep and Zoya are unchanged.** Sweep 4b dedupes its own forwards by Message-ID. Zoya looks up only msgid: keys, and capture never keys mail she's on as adid:.

**What r7 does:** `README.md` has the tables.
- **Ad@-only mail:** keyed `adid:<UID>`, with no raw fetch. That's most mail.
- **Mail sent from ad@:** raw at once, keyed `msgid:`. Zoya doesn't log our side's mail.
- **Mail Zoya is on:**
  - her row is found by MSGID FIND (Date and People candidates, confirmed by an All Mail HEADER search that must return this UID) and stamped;
  - with no row from her, the mail waits up to 2 hours without counting toward the cap;
  - after 2 hours, raw.
- **Actions** takes `adid:` rows. Their THREAD adds a forward search by subject.
- **UIDVALIDITY isn't exposed by MCP Emails,** so the record says so.

**Zoya-side, not built (Zoya stays untouched; decide whether to fix there):**
- **D6:** mail where Zoya is Bcc'd or on a team alias becomes an adid: row and then a second msgid: row from Zoya. Fix in Zoya: before creating a row, HEADER-search ad@ by the Message-ID and look up adid:<that UID>.
- **D12:** a send Zoya logs without a msgid: key gets logged again by capture after 2 hours. Fix in Zoya: log every send with its msgid: key.

**Nits left:**
- **N1:** an old msgid: row with no People can't be found, so it could become a duplicate.
- **N2:** HEADER searches run one per candidate.
- **N6:** "a team member in From" includes their own addresses, which is harmless.
- **The cutoff assert** checks the date's shape only.
