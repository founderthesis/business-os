# Cleanup: inbox and WhatsApp write hotfix (44d144a)

**Verdict: both ACCEPTED.**
- Inbox: 65,336 B, sha256 403f49ac840dc31b.
- WhatsApp: 26,336 B, sha256 ca8009c24aaeda15.

## Reproduced

- **Inbox:** `patch.py` on the live inbox gives 65,336 / 403f49ac840dc31b, twice, byte-identical to `docs/proposals/inbox-writes/inbox.txt`. The live inbox was read from trig_0189eZvAD8x4357cfevgZ3No just now: 65,333 / d1bba5802ca8872d, disabled, connectors Notion, Calendar, Blueticks and MCP Emails (Gmail detached).
  - **Size:** exactly at the 65,336 build limit, which is 200 B under the 65,536 cap. The next inbox change must cut before it adds.
- **WhatsApp:** `patch_wa.py` on 26,007 / 9e8b9f4891e9c03d gives 26,336 / ca8009c24aaeda15, twice, byte-identical to `docs/proposals/inbox-writes/whatsapp.txt`.

## The fix

**Every create names its parent:**

    WRITES: every create names parent {"type": "data_source_id", "data_source_id": "<its collection id>"}, allow_async false, the title set. Then fetch the page it returns: no parent data source: a failed write, never logged; retry once, else report it, end Partial.

This matches the Notion create-pages schema exactly. The schema says "If omitted, pages are private at the workspace level", which is how the 23:19 run's 18 loose pages were made.

- `allow_async false` keeps the synchronous result, so the page id is there to fetch.
- The WhatsApp prompt gets the same rule, adding "never a create with no parent".

**Checks:**
- **R2: passes.** The STEP 1 read line is now "(action read; original only per IDENTITY)". It is no longer unconditional.
- **R7: passes.** The read-back fetches the page the create returned, so it works for rows with no Source ID (People, brand Engagements, FT Network, WhatsApp digests). A retry is decided by the fetched parent, not by a Source ID lookup, so it can't duplicate.
- **IDENTITY:** `original` runs one call at a time, and only when read lists attachments under 50 KB in all. Otherwise the header counts as unreadable and the key is "allmail:<MCP Emails id>". A mail From Zoya is matched against her "Zoya sent:" Activities by Message-ID search. The Gmail rfc822msgid path is gone.
- **Duplicates (CX-20261029-03):** "report both, never retire one". The fold is removed, which also clears the fold gaps from Cleanup's d420 inbox verdict.
- **Unverified: does `email_read read` list attachment sizes?** It's documented, not observed. The MCP Emails tool description says attachment metadata "(filename, mime_type, size_bytes, attachment_index) always comes back". Cleanup's only live read so far was of a message with no attachments ("attachments": []). The first live run's report should show a size-gated `original` decision on a mail with an attachment.

## Follow-ups (none blocks re-enabling)

1. **The failed attempt's loose page stays behind.** A create that lands with no parent is retried, but the orphan from the first attempt isn't removed. Add "trash the loose page (decision 416) and list it", or at least list its page id in the report. The 18 pages from 23:19 need the same clean-up, once each is confirmed to have no relations.
2. **"allmail:<MCP Emails id>" keys** depend on the IMAP UID in All Mail staying stable. A later run that can read the header would key the same mail by msgid, so a large mail could be logged twice under two keys. It's rare; the duplicate report would show it.
3. **B2 and the d420 batch** rebase on the new WhatsApp output, together with Cleanup's three B2 privacy fixes (759daf4).

Checks:
- Less text and fewer writers: +3 B on the inbox, with the fold removed; no new writer.
- Selection by prefix or wording: none added.
- Retry double-write: closed by the fetched parent, apart from the orphan in follow-up 1.
- Bytes and hashes: above.
