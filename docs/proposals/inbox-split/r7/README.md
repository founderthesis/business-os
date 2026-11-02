# Capture r7: key ad@-only mail by UID (Akshay, 2 Nov ~08:50 JST, option (a) of `../msgid-structural/proposal.md`)

**Bases:**
- live capture r6c: `../cleanup/r6/capture.txt`, 38,121 / d0f0e9bb;
- live actions: `../actions-v2.txt`, 39,354 / 19701651.

**Build:** `patch.py`, every edit asserted once, built twice, byte-identical.

| File | Bytes / sha256 |
|---|---|
| `capture.txt` | 38,891 / 5be8fda7548c7b95 |
| `actions-v2.txt` | 39,455 / f984dbefc2fcc607 |

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
