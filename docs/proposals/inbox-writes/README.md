# Inbox hotfix: parentless Notion writes and a lighter Message-ID read

Asked by the CTO (30 Oct, 00:05 JST). It has to be accepted before the 07:02 JST inbox run. Akshay pastes the inbox prompt himself.

## Files to deploy (after Cleanup accepts)

| Routine | File | Bytes / sha256 | Input (live) |
|---|---|---|---|
| Inbox | `inbox.txt` | 65,336 / 403f49ac840dc31b | 65,333 / d1bba5802ca8872d |
| WhatsApp (live prompt, not B2) | `whatsapp.txt` | 26,336 / ca8009c24aaeda15 | 26,007 / 9e8b9f4891e9c03d |

Each is built by `patch.py` / `patch_wa.py` from the live prompt, twice, byte-identical.
- The inbox file is exactly at the build limit, 200 bytes under the real cap. The next inbox change needs a cut first.
- B2 and the d420 WhatsApp batch rebase onto `whatsapp.txt` once it's accepted.

## (a) Why the creates had no parent

**What the evidence shows.** This session can't read run transcripts: it has no list_events tool, so the CTO can confirm against session_019pwcV3pSeQt6odgqQeT1A6. The orphan run record (40819a301a7f8154a91ef06f37ba9921) has:
- no ancestor at all;
- an empty title;
- only the body text.

**What that points to.** The Notion create-pages tool's own description says that if `parent` is omitted, pages are private at the workspace level. Outside a database it keeps only a title.
- So the run's creates went out with no usable parent, or with a malformed one: for example the `collection://...` URL put where the tool expects a bare id, which then fell back.
- The tool still returned page ids, so the run counted them as logged.
- The WhatsApp routine did the same twice at 13:01Z, and its later creates landed. So it's the call shape the model chose, not a fault on Notion's side. Neither prompt says how to name the parent.

**The fix (both prompts): a WRITES rule.**
- Every create names `parent {"type": "data_source_id", "data_source_id": "<the collection id above>"}`, with `allow_async false` and the title set.
- After a create, the run fetches the page it got back. If that page has no parent data source, the write failed and is never counted as logged. It's retried once, then reported, and the inbox run ends Partial.
- Checking the parent works for creates that carry no Source ID (People, brand Engagements, FT Network, WhatsApp digests), so the replay's R7 case is covered.
- In the inbox, the WRITES line sits right under the NOTION heading, so "its collection id below" covers every data source in the list.

## (b) A lighter Message-ID read

- A headers-only `email_read read` (`body_max_chars 0`) returns In-Reply-To and References but **not** the message's own Message-ID. I checked this read-only on one ad@ message. So `original` stays the only source for it.
- The new rule: `original` is called one at a time, and only when the read lists attachments under 50 KB in total. For anything larger the header counts as unreadable. The prompt's existing provider-id rule then applies: key `allmail:<MCP Emails id>`, looked up like a Message-ID before any create.
- The old Gmail-era fallback for mail from Zoya now uses an MCP Emails `search text = <Message-ID>` instead of `rfc822msgid`.
- The identity rules hold otherwise: one Activity per message, and date plus recipient never match.
- **Cost:** a large message from someone other than Zoya, which another routine logged under `msgid:`, can get a second Activity under `allmail:`. That's rare (large attachments) and visible in the sweep's duplicate count.

## Round 2 (replayIW.json)

The first replay failed two cases, now fixed:
- **R2:** STEP 1's read line still said "then original" without condition. It now reads "original only per IDENTITY".
- **R7 and W1:** the read-back by Source ID couldn't find rows created without one, so they'd have been retried into duplicates. The check is now the fetched page's parent.

Also restored: "that day (JST)" in the check for mail from Zoya.

## Room made

The live inbox carried decision 424's fold. Codex's CX-20261029-03 puts that on hold until the fold is rebuilt. The live inbox now says: "A duplicate row: report both, never retire one (CX-20261029-03); never merge People (decision 424)." This also frees the bytes the fix needs.

## Not done

- The 20 orphan pages are left as they are, for Akshay to confirm.
- Nothing is deployed from this session.
