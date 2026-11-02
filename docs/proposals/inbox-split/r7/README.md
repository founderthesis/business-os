# Capture r7: key ad@-only mail by UID (Akshay, 2 Nov ~08:50 JST, option (a) of `../msgid-structural/proposal.md`)

**Bases:**
- live capture r6c: `../cleanup/r6/capture.txt`, 38,121 / d0f0e9bb;
- live actions: `../actions-v2.txt`, 39,354 / 19701651.

**Build:** `patch.py`, every edit asserted once, built twice, byte-identical.

| File | Bytes / sha256 |
|---|---|
| `capture.txt` | 39,435 / 66bad277d94155c4 |
| `actions-v2.txt` | 39,593 / f5f31ac135bda7e6 |

## Capture

- **KEY** (new, in STEP 2 IDENTITY). The key a mail gets depends on whether Zoya is on it:
  - **Ad@-only mail** (Zoya not on From, To or Cc) is keyed `adid:<UID>`, the number in its All Mail search id. No RAW.
  - **Mail Zoya is on** is hers to log first. Capture finds her `msgid:` row: candidates by Date within a day plus People overlap, each confirmed by `query HEADER Message-ID` returning this same UID. Then STEP 1's exception stamps it.
  - **No row from Zoya and the mail is under 2 hours old:** it's left for the next run, not pending.
  - **No row from Zoya and the mail is older:** RAW, keyed `msgid:` as before.
- **Other places that change:**
  - **The dedupe lookup** covers `adid:` as well as the old spellings.
  - **STEP 1's skip and STEP 0's re-key and fold** use "its key".
  - **The Source ID bullet** says the same, and `adid:` rows have no Link.
  - **The loop-in's idempotency key** is the pitch's key, and STEP 6's catch-up re-reads a pitch by its key.
- **Unchanged:** capture's own loop-ins keep their `msgid:` key, from RAW of the sent mail.
- **SELF-CHECK** accepts `msgid:` or `adid:`. The ledger line is "<key>: Activity <id>".
- **read to** never passes a Zoya-on mail left for her under 2 hours.
- **The record** says "UIDVALIDITY: not exposed". The tool shows none: `folder_list`, `inbox_list`, `search` and `read` were all checked on 2 Nov.

## Actions

- **STEP 1** and the intro take Source ID `msgid:` or `adid:`.
- **THREAD for an `adid:` row:** read `[Gmail]/All Mail:<UID>`, then the messages its References name.

## Checked and left as they are

- **Sweep 4b** (billing forward to Jaya) keys its own forwards by the original's Message-ID and dedupes on them. It doesn't read capture's keys.
- **Zoya** looks up only `msgid:` keys for mail in her inbox. Capture never makes an `adid:` row for mail she's on, so nothing collides.
- **Zoya BCC'd:** capture can't see a BCC, so a mail where Zoya is BCC'd looks ad@-only and gets `adid:`. Zoya's routine would then log it again as `msgid:`. This is rare: our side puts Zoya in Cc, not BCC.

## r7b (replay7.json)

| Defect | Fix |
|---|---|
| D1 duplicates at cutover | MSGID FIND (msgid: candidates by Date and People, confirmed by an All Mail HEADER search returning this UID) runs first for ad@-only mail received before 2026-11-03 and for every STEP 0 allmail: row. If r7 goes live after 2 Nov, move that date to the go-live day |
| D2 new rows needed a Message-ID | A new row's "gmail:<thread id>" is the first message's key, in both prompts |
| D3 Zoya doesn't log our side's mail | Mail sent from ad@ (Akshay or a team member in From) is fetched raw at once and keyed msgid:, like capture's own loop-ins |
| D4 adid: threads saw no later replies | THREAD for adid: adds an All Mail search by subject since its date, kept where the People overlap (both prompts) |
| D5 pending line | Holds a Message-ID, an adid: key or an mcp: id; adid: entries are retried by id |
| D7 HEADER confirm folder | All Mail, and it must return [Gmail]/All Mail:<this UID> |
| D8 STEP 0 "No Message-ID" | Only for Zoya-on rows whose RAW gives none |
| D9 Gemini rows | KEY covers Email in and Email out only |
| D10 loop-in key | "loopin:<Message-ID>", or "loopin:adid:<UID>" for an adid: pitch |
| D11 waiting mail | Doesn't count toward the cap; ledger line "<UID>: waiting (Zoya)" |

**Zoya-side, not built (Zoya stays untouched):**
- **D6:** mail where Zoya is Bcc'd or on a team alias gets an adid: row from capture, and Zoya then logs it again as msgid:. Fix in Zoya: before creating a row, HEADER-search ad@ for the Message-ID and check adid:<that UID>.
- **D12:** a Zoya send she logs without a msgid: key gets logged again by capture after 2 hours. Fix in Zoya: log every send with its msgid: key.
