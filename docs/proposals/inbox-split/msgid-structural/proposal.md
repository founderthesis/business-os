# Message-IDs in capture: a structural fix (CTO, 2 Nov 02:57 JST; for Akshay in the morning)

**The problem.** Capture keys every mail by its RFC Message-ID. MCP Emails only gives that from `original`, which returns the whole message inline as base64. The 02:34 run logged 1 message, and r5 runs did 2 to 8. About 95 messages are waiting, back to 31 Oct.

## What MCP Emails can and can't do (measured 2 Nov, read-only, ad@ inbox)

| Call | What it returns | Size measured |
|---|---|---|
| `search` (structured or raw IMAP `query`) | UID (`[Gmail]/All Mail:<n>`), from, to, subject, Date (the header's, to the second), preview, thread_id. No Message-ID | about 600 characters a message |
| `read`, `body_max_chars` 0 | the same headers plus cc, `in_reply_to` and `references`. No Message-ID of its own | 563 characters |
| `read_batch` | the same as `read`, up to 50 messages a call, bodies 2,000 characters by default | about 1,000 characters a message |
| `original` | the whole .eml as inline base64. Message-ID sits after the Received, ARC and DKIM headers, about 5 KB in | a 9,517-byte message (no attachment) came back as 12,692 base64 characters. Mail with HTML or an attachment is many times that |
| `search`, `query` `HEADER Message-ID "<id>"` | exactly the one message with that Message-ID (the IMAP SEARCH HEADER works; tested, 1 hit) | about 700 characters, 1 call |
| `search`, `query` `X-GM-RAW "rfc822msgid:..."` | nothing: the connector is IMAP (`search_syntax: imap`), so Gmail's own search isn't available | n/a |

Other findings:
- **No header-only fetch.** `read` with `body_max_chars` 0 doesn't carry Message-ID, and no `email_read` action or parameter returns raw headers.
- **One key reaches both mailboxes.** ad@ and zoya@ are both on this MCP Emails key, so either routine can search the other inbox.

**What this means.** No call goes from a message to its Message-ID except `original`. The reverse works cheaply: from a Message-ID to the message, with one HEADER search. So the fix has to avoid needing the Message-ID for most mail, and get it from the other side when dedupe needs it.

## Options weighed

**(a) Key ad@-only mail by its MCP Emails id. Recommended, with one addition.**
- **Ad@-only mail (Zoya not on From, To or Cc):** key it `adid:<UID>`, for example `adid:108971`. No other routine logs it, so there's nothing to dedupe against. The key comes from the search result with no extra call.
- **Mail Zoya is on:** capture doesn't create the row. Zoya's own routine logs it from her inbox, where she already gets its Message-ID: her rule is "log it if Akshay isn't on To or Cc, or if no Activity has its msgid:". Capture then finds her row and stamps it, as STEP 1's exception already does.
- **Finding Zoya's row:** query the "msgid:" rows logged since the message's date with Kind Email in or out and People overlapping its addresses. Confirm each candidate with one HEADER search in ad@ (`HEADER Message-ID "<that row's id>"`), which must return this same UID.
- **The addition:** a Zoya-on message with no row from her after 2 hours goes to `original` as today. That's the only raw fetch left.
- **Changes needed:**
  - capture: MAILBOX, STEP 1 and STEP 2's key rule, and the SELF-CHECK prefix;
  - actions: STEP 1's query takes `adid:` as well as `msgid:`;
  - nothing in Zoya.
- **The catch:** an IMAP UID is stable unless Gmail resets the folder's UIDVALIDITY, which is rare. If that happens, the old `adid:` rows still hold their thread, date and Link, and no row is lost; the risk is a new duplicate if a message is read again. The run record should note the UIDVALIDITY at each run when it can.

**(b) Get the Message-ID from In-Reply-To or References, and by HEADER search on subject and date.**
- **Partial.** A reply's `in_reply_to` names its parent's Message-ID, not its own. So it only helps when the parent is the message we need, which is the last message of a thread only.
- **No search by subject and date can produce the Message-ID.** It can only confirm a guess, and there's nothing to guess from.
- **Use:** it's useful as the confirm step in (a), not as the source of keys.

**(c) A cheap header call in MCP Emails.**
- None exists today: every `email_read` action and parameter was checked.
- Asking MCP Emails to add `message_id_header` to `read` and `search` would fix this at the root.
- That's an outside request for Akshay, and isn't needed for (a).

**(d) A content hash key in both routines (not now).**
- **The idea:** both routines key every mail by sha256 of from, the Date header to the second, and subject, all of which `read` gives in both mailboxes. That would remove raw from Zoya too.
- **Why not now:** it changes Zoya's prompt and every dedupe rule, and it splits on any mail two senders send in the same second with the same subject. Worth it only if (a) still leaves Zoya slow.

## Cost per message, ad@ capture

| Path | Tool calls | Characters into context |
|---|---|---|
| **Today**, every message | 1 read, 1 `original`, 1 to 3 Bash decodes, about 3 to 5 calls | 13,000 for the smallest mail; 50,000 to 200,000+ with HTML or attachments, and the inline result can be too big to decode (the 02:34 stop) |
| **(a)**, ad@-only (most mail) | a share of 1 `read_batch` (20 a call) and of one Notion key lookup, about 0.1 calls | about 1,000 to 2,000 |
| **(a)**, Zoya on it and her row exists | the above plus 1 Notion candidate query and 1 HEADER confirm a candidate, about 2 calls | about 3,000 |
| **(a)**, Zoya on it, no row after 2 hours (rare) | as today | as today |

These are character counts measured from the tool results above. Tokens weren't measured; base64 is the costliest part of today's path.

**Throughput.** Capture would be bounded by Notion writes and the 18-minute window, not by mail reads. A cap of 25 a run should hold. The backlog of 95 would clear in about 4 runs, the Zoya-on part as her rows are found.

## Before building (asks)

1. **Akshay's yes on the key change.** New ad@-only rows are keyed `adid:<UID>`, not `msgid:`. The provenance stays the same: source system, original id and capture date. The `adid:` key is a second spelling for the dedupe lookups.
2. **One read-only check in Notion:** that Zoya's routine logs ad@ mail she's only Cc'd on, with a msgid: key. Round 4's R1b already assumed this, and (a) depends on it. I can check it read-only in this session if asked.
3. **Then one build:** capture r7 and the one-line actions change, replayed and handed off as before.
