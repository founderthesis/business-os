# AR-20261019-5: episode asset filing (Main 2)

Branch claude/ar-20261019-5-episode-assets, cut from main 6352db2. It is separate from the AR-20261019-3 Episode-recovery proposal (e250cd0), which neither depends on nor touches. This is for cleanup review; Main 1 integrates and deploys. Nothing here is live. No mail was sent, nothing was uploaded, and no Notion record was changed.

## 1. Source versions and changed paths

- routines/inbox.md at main 6352db2, blob f42afe42a6ee (the version the task names). Prompt block 64,848 bytes before, **64,934 after (+86, 602 under the 65,536 cap)**. Main 1 re-checks the size against whatever AR-9 and the WhatsApp work add.
- docs/proposals/ar20261019-5-inbox.patch changes two paragraphs:
  - **STEP 6d "Assets for an episode"**: filing runs first, on every asset message and open pending line, whoever replied. The details move to the rule page. The reply text, its gate ("no reply from our side since") and its log are unchanged, except that the Claude note no longer claims "added to the Episode".
  - **STEP 3 "Edit notes"**: the original attachment is filed too; extracted text never replaces it.
- docs/proposals/ar20261019-5-episode-asset-filing.md: the text of a new Controls rule page, "Episode asset filing". Main 1 creates it and replaces PAGEID_PLACEHOLDER_32CHARS_XXXXXX (same length as a page id, so the size check holds).
- No schema change, no new database, routine, watcher, sender or Mac dependency. Pending work uses an "## Assets to file" section on the existing Engagement page.

## 2. What the cloud can do today (probed read-only, 19 Oct 06:50 UTC)

| Step | Tool | Result |
|---|---|---|
| Find attachments, stable id | Gmail get_message | filename, mime type, attachment id; Gmail message id. No size, no bytes. |
| Size and bytes | MCP Emails email_read (ad@thepodium.in) | read gives filename, mime type and size_bytes (114,483 and 823,589, both matching Codex's records). Action attachment returns base64, **and the session saves the original file to disk**: 823,589 bytes, JPEG, sha256 854e942b470053f3. |
| Upload to Notion | notion-create-file-upload + POST | **Blocked here**: api.notion.com returns 403 at the proxy. This is the existing pending item "Network access: add api.notion.com under Allowed domains". |
| Text files | notion-create-attachment with content | Works with no network change, for UTF-8 text of 200 KB or less. |

So binary filing becomes fully automatic once api.notion.com is allowed in the environment the inbox runs in (assumed to be the same one; the rule page detects a 403 and parks the file with reason "upload blocked"). Until then, every asset is still recorded as pending with its key and reason, never as filed. Each attachment download also puts its base64 into the run's context (about 25k tokens, truncated), so the rule caps uploads at 3 a run.

## 3. Dry run: the Prashant Sachan thread (Built to Share)

Read window on 19 Oct: Vineeta's two messages on thread 1a13c903aeaaed42, plus earlier ones.

| Message | File | Key | Step 4 result | Action |
|---|---|---|---|---|
| 1a152bc45497118d, 11:26 IST | Prashant Sachan Photo.png, 114,483 B | gmail:1a152bc45497118d#0 | B2S Episode has a file block with this name, a mail link ending /1a152bc45497118d and "114,483 bytes" | already filed, no upload, no line |
| 1a152dda3e18bb7c, 12:03 IST | Copy of 13.jpg, 823,589 B | gmail:1a152dda3e18bb7c#0 | same, /1a152dda3e18bb7c, "823,589 bytes" | already filed, no upload, no line |
| 1a149f36e53a11c9 (Akshay, 17 Oct) | prashant-satish-akshay.txt | n/a | sent by our side | skipped (rule 1) |

Result: 0 uploads, 0 pending lines, 0 duplicates. Episode match: the Engagement is the Built to Share row, its Episode relation holds only the B2S Episode, and Prashant's Founder Thesis Episode is on another show, so it is never a candidate.

Unchanged and outside this patch: the acknowledgement gate. Akshay replied at 11:50 IST before the 12:03 message, so under today's gate that second message still counts as having no reply from our side since. Whether an acknowledgement is sent stays with the existing sender rules (Main 1).

## 4. Replay tests (traced against the patch and the rule page)

| # | Case | Expected |
|---|---|---|
| 1 | The two filed Prashant photos | Step 4 finds both: zero uploads. |
| 2 | Akshay or anyone on our side already replied | Filing runs anyway; only the reply is gated. |
| 3 | Two files with the same filename and different bytes (or different messages) | Different keys and sizes, so both are filed as separate lines and blocks. Neither is treated as a newer version. |
| 4 | The same message arrives twice, or a run retries | Same key, step 4 finds the filed file: nothing new. |
| 5 | Upload succeeds, then the page write fails | No block on the Episode; the pending line stays "to upload". The next run uploads again; the orphan upload expires in 1 hour. |
| 6 | Page write succeeds, then the run stops before marking pending | Next run: step 4 finds block and key, marks the line filed, no upload. |
| 7 | Asset arrives before the Episode exists (booked, not recorded) | Pending line "no Episode yet" on the Engagement. Once the calendar run creates the Episode, the next inbox run files it. No speculative Episode. |
| 8 | Same guest on two shows (Prashant FT and B2S) | Only Episodes on the Engagement's own Show and in its relation are candidates. A name match never counts. |
| 9 | Edit notes as an attachment | Original filed with purpose "edit notes"; the STEP 3 extracted list stays as it is. |
| 10 | Signature logo, tracking pixel, .ics | Skipped by rule 1, not reported as pending. |
| 11 | Upload fails (403, size mismatch, over 20 MB) | Pending line with that reason; nothing marked filed; no other line touched. |
| 12 | Drive or WeTransfer folder link | Stored as a link line; pending stays open "link only" until a person adds the files. |
| 13 | Two Episodes match | "unclear episode", nothing filed. |
| 14 | Pending older than the read window | Open lines are taken first, with no age limit. |

## 5. Limits stated plainly

- Binary upload needs api.notion.com allowed in the routine environment. Text files of 200 KB or less don't.
- Files only in Zoya's inbox (not copied to ad@) are out of scope here; the inbox reads ad@.
- Over 20 MB (single-part upload limit): pending, filed by hand.
- Links: stored, not downloaded.
- No real test mail and no draft-attachment probe were used. Calling automatic ingestion reliable needs the next real incoming file, after deploy and the network change.
