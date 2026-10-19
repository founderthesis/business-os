# AR-20261019-5: episode asset filing (Main 2), revision 4

Branch claude/ar-20261019-5-episode-assets. It is separate from the AR-20261019-3 Episode-recovery proposal (branch claude/ar-20261019-3-episode-recovery), which it neither depends on nor touches. Revision 2 answers Codex's review of dac2f94. For cleanup review; Main 1 integrates and deploys. Nothing here is live. No mail was sent, nothing was uploaded and no Notion record was changed. The two Prashant Sachan photos already filed were not touched.

## 1. Source versions and changed paths

- routines/inbox.md at 420ca4f (integration branch), blob f42afe42a6ee, unchanged since 6352db2. Prompt block 64,848 bytes before, **64,937 after (+89, 599 under the 65,536 cap)**; result blob 8b46769a8901. Main 1 re-checks the size against whatever else lands first.
- docs/proposals/ar20261019-5-inbox.patch changes two paragraphs:
  - **STEP 6d "Assets for an episode"**: anyone may send material, our team included, in ad@thepodium.in or Zoya's inbox. Filing runs first on every such message and every open pending line, whoever replied. The details live on the rule page. The reply keeps its gate and is sent only to a guest, PR or company.
  - **STEP 3 "Edit notes"**: the original attachment is filed too; extracted text never replaces it.
- docs/proposals/ar20261019-5-episode-asset-filing.md: the text of a new Controls rule page, "Episode asset filing". Main 1 creates it and replaces PAGEID_PLACEHOLDER_32CHARS_XXXXXX (same length as a page id, so the size check holds).
- No schema change, new database, routine, sender or Mac dependency. Pending work lives in an "## Assets to file" section on the Engagement page; links get one Kind Task row for Sarika.

## 2. Codex correction 1: the binary path in the actual runner

The inbox run (trig_0189eZvAD8x4357cfevgZ3No) executes in environment env_01Pb9xdJdFEZj6Xuxuq5Kxid: its last run, session 015MkYX3X9jTtqKkLtjCZbXg, shows that environment, Claude Code 2.1.303, and the Bash and Agent tools. This session runs in the same environment and version. Its connectors are Notion, Gmail, Google Calendar, Blueticks and MCP Emails; there is no Drive connector. All probes below ran read-only on 19 Oct.

| Step | Path | Result |
|---|---|---|
| Download, ad@ | Gmail get_message, RAW | **Works with zero inline bytes.** The session saves the result to a file and shows only its path (no preview): 174,837, 179,200 and 1,159,063-byte messages. Python decodes it (field raw, base64url) into the original parts, with the Message-ID and each part's Content-ID and X-Attachment-Id. |
| Download, either inbox | MCP Emails email_read, action original | **Works the same way.** Results of 239,236 and 1,545,721 characters were saved to file with no preview, and include a sha256 of the .eml that matched on decode. Message-ID and part bytes are identical to the Gmail RAW of the same message. |
| Download (old path) | MCP Emails action attachment | Rejected. The image block and its base64 come inline until truncated at 25,000 tokens. The file lands on disk, but the context cost is that of a whole file, which is what Codex flagged. |
| Native server-side upload | notion-create-attachment source_url | Not usable. It needs a public HTTPS URL, and neither mailbox connector exposes one: Gmail returns attachment ids only, MCP Emails returns bytes. |
| Native text upload | notion-create-attachment content | Works with no network change, for UTF-8 text of 200 KB or less. |
| Binary upload | notion-create-file-upload, then multipart POST to upload_url | **Blocked**: the CONNECT to api.notion.com is refused with 403 by this environment's network policy. Re-checked 19 Oct. |

**Evidence on a genuinely missing eligible file.** Rohit Manglik (Founder Thesis): headshot 16768.jpg, first sent 31 Aug (Gmail 1a056589dddf7302), quoted back inline on 19 Oct (Gmail 1a152a28fe0963b6, MCP Emails INBOX:48153). His Episode 3ed19a301a7f81c09fcbeb5d8be8e6a0 has no Guest assets section. Gmail RAW and MCP Emails original of both messages each gave 115,795 bytes, sha256 800a0253a8496d4b..., MIME part 2, inline with Content-ID. That equals MCP Emails size_bytes and the attachment-action download. The same check on Prashant's larger message (1,159,063 bytes) gave "Copy of 13.jpg" at 823,589 bytes, sha256 854e942b470053f3, from both sources. That is the photo already on his B2S Episode, which was read only, not uploaded again.

**What is missing, exactly.** The Notion connector has no server-side way to upload a binary file. Its file-upload tool hands back an upload_url on api.notion.com that the runner must POST to itself. **Minimum network requirement:** in the cloud environment the inbox run uses (env_01Pb9xdJdFEZj6Xuxuq5Kxid), add **api.notion.com** under Network access > Allowed domains, keeping "Allow package managers" ticked. Nothing else is needed: downloads already work through the connectors. Main 1 owns this step (section 8): it prepares the exact setting for Akshay and the upload and readback check, and the check doesn't have to wait for production deployment. Revision 3 drops this branch's pending-list edit: docs/akshay-pending.md is again identical to the integration branch at fa7062f, so the completed B2S relabel item from the older copy is not restored. Until then each binary file is recorded as pending, reason "upload blocked: 403", with its key, bytes and sha256, and never as filed. Uploading the original binary has not yet been proved end to end: the only missing step is the one POST.

**Context cost per file**, once the network allows it: one saved-to-file read, a decode script that prints one line, one upload tool call, one curl, one page update. The rule page runs the downloads in one subagent that returns only key, path, bytes and sha256. A message small enough to come back inline is small by definition. No credentials were read or used.

## 3. Codex correction 2: recording and file identity

- **Recording.** Rule page section 4: explicit evidence first (an Episode link or the recording date in the thread), then the Engagement's only recording, then the thread's own recording (the one booked, confirmed, moved or thanked on that thread). Otherwise pending, "unclear recording". The target is the Episode carrying that recording's cal: key (AR-20261019-3), in any status, Scheduled and booked included. "Latest Episode on or before the message date" is gone.
- **Message.** Keyed by the RFC Message-ID (sha256, first 16 hex). It is the same in Gmail and MCP Emails and survives moves. This replaces the sender, date and subject bridge. Each file is downloaded from the inbox where it was found, so no cross-provider lookup is needed. Messages in both inboxes collapse onto one key.
- **File.** Keyed by message key plus MIME part path, with sha256 of the decoded bytes on every line. Two same-name, same-size files in one message have different part paths and, when their bytes differ, different sha256.

## 4. Codex correction 3: coverage

- **Team-sent files are in.** Editor drafts, internal briefs and marketing deliverables are filed. Exclusions are by purpose and provenance: signature images, copies already filed (same sha256), templates sent to every guest, transcripts (Transcript file workflow), .ics, invoices and contracts, and anything not about one episode. An image the mail names is filed at any size.
- **Zoya-only mail.** The inbox run already holds the MCP Emails connector, so it reads Zoya's inbox (last 72 hours) into the same filing path. That keeps one writer for Guest assets; the Zoya routine is not changed. Today Zoya's inbox (live since 15 Oct, 260 messages) has no Zoya-only attachment. The photo sends to it so far (INBOX:248, INBOX:253) also went to ad@ and collapse onto the same Message-ID key.
- **Links.** The runner has no Drive, Dropbox or WeTransfer access, so a link is stored as given and that is never counted as storing the files. Sarika is the production default for episode files only; a link to a product or commercial document never reaches this path. See section 7 for how a link line closes.

## 5. Dry runs (read-only, 19 Oct)

| Case | Key and evidence | Result |
|---|---|---|
| Prashant Sachan Photo.png, B2S | Gmail 1a152bc45497118d, 114,483 B | 5b legacy match (file block, Gmail id, bytes): already filed. 0 downloads, 0 uploads. |
| Copy of 13.jpg, B2S | Gmail 1a152dda3e18bb7c, 823,589 B | Same: already filed, 0 uploads. |
| Rohit 16768.jpg, FT, quoted on 19 Oct | sha 800a0253a8496d4b; earliest carrier is the 31 Aug message | Section 2 copy rule: file the 31 Aug message's part 2. Recording: one Engagement, one Episode (recorded 20 Aug, unkeyed, Source ID "Blue ..." kept), so 4b and the single-Episode rule apply if the calendar shows one recording. Download proven above. Upload: "upload blocked: 403". One pending line on the Engagement, nothing marked filed. |
| Zoya-only attachment | none exists yet | Nothing to file; path tested on ad@ copies via MCP Emails original. |

## 6. Acceptance tests (traced against the rule page and the patch)

| # | Case | Expected |
|---|---|---|
| 1 | Prashant's two filed photos | 5b finds both: zero downloads and uploads. |
| 2 | Akshay or Zoya already acknowledged the mail | Filing runs anyway; only the reply is gated. |
| 3 | Editor draft or internal brief from our team | Filed (section 2); no reply sent (the reply is only for guests, PR or companies). |
| 4 | Zoya-only mail with an attachment | Read from Zoya's inbox, downloaded with MCP Emails original, filed by the same rules. |
| 5 | Same mail in both inboxes | Same Message-ID key: filed once. |
| 6 | Explicit small logo ("attaching our logo", 8 KB PNG) | Filed: the mail names it. A signature image001.png nobody mentions is not. |
| 7 | Returning guest: an upcoming recording booked, an earlier Episode on the same show | Thread about the new booking: pending "no Episode yet (cal:<new event>)", never the earlier Episode. A thread naming neither: "unclear recording". |
| 8 | Episode exists in Scheduled status for a booked recording | Filed on it if it carries that recording's key. |
| 9 | Two same-name, same-size files with different bytes in one message | Two part paths, two sha256: two keys, two lines, two blocks. |
| 10 | The same bytes arriving again (quoted reply, forward) | Same sha256 on the Episode: already filed, no upload. |
| 11 | Retry after the upload, before the page write | No block on the Episode; the line stays open and the next run uploads again (the orphan expires). |
| 12 | Uncertain page write (the update errors or times out) | Read-back: only a file block directly under the keyed line marks it filed; else "page write not confirmed". The next run starts at 5b, which handles each partial outcome (rows 19 to 21). |
| 13 | Upload blocked (403 today), size over 20 MB, decode mismatch | Pending with that reason; nothing marked filed; no other line touched. |
| 14 | Transcript attachment | Not filed here: the transcript workflow owns it. |
| 15 | Two Episodes could match | "unclear recording" with the dates; nothing filed. |
| 16 | Pending older than the read window | Open lines go first, with no age limit. |
| 17 | Drive or WeTransfer link | Link line stored, pending "link only: files not stored", one open Task for Sarika carrying the Engagement's Show (row 23). |
| 18 | Edit notes as an attachment | Original filed with purpose "edit notes"; the STEP 3 list stays. |
| 19 | Metadata only: the keyed line is on the Episode, no file block under it (rev 3) | Not filed. Reason "file block missing"; the file is downloaded and uploaded, and only the block is added under the existing line. Read-back then marks it filed. |
| 20 | Block only: a file block with this filename, no line (rev 3) | The block is downloaded and hashed first. Same sha256: the line is written above it, no upload. Different: treated as another file and filed on its own. Not downloadable: "block unverified", stop. |
| 21 | Both present after an uncertain write (rev 3) | "already filed": no download, no upload. |
| 22 | Link Task marked Done, nothing under the link line (rev 4) | Line stays open. First Done: the same Task (found by Source ID "assets-links:<Engagement id>") goes back to Handed over with "files aren't on the Episode yet" and a "reopened <date>" line. Second Done: left Done, no new Task, reported every run. A link line added after the reopen date reopens the same Task once more. |
| 23 | Link follow-up Task (rev 4) | Looked up by Source ID "assets-links:<Engagement id>" in any Task state, so a reopened Task with a rewritten Next action, or a Done one, is still found and never duplicated. Created only when that key is absent, with Show = the Engagement's Show checked equal to the Episode's (else "show mismatch", no Task). |
| 24 | Link closed properly (rev 4) | File blocks under the link line, each hashed and given its own line, or a terminal disposition with name and date ("not needed", "cancelled by <who>"): then the line closes. |
| 25 | "expired, asked again 20 Oct" written on a link line (rev 4) | Not terminal: the line stays open with that reason, and the Task stays with Sarika (reopened if it was Done). The replacement files close it when they land under the line. |
| 26 | Two runs in a row after a reopen (rev 4) | Run 1 reopens the Task and rewrites its Next action. Run 2 finds it by its Source ID, open, and reuses it: still one Task. |

## 7. Revision 3: completion evidence (Codex's 0f25c83 review)

- **Only a stored file closes a file.** 5b now needs a file block directly under the keyed line. A line alone is pending ("file block missing"). A block alone is checked by downloading it and comparing sha256 before a line is added, so nothing is uploaded twice and nothing is closed on text. 5f's read-back uses the same test. Prashant's two hand-filed photos stay closed by their legacy receipts.
- **Block check proven here, read-only.** Notion fetch with file URLs, then curl, then sha256 on the B2S Episode's "Copy of 13.jpg": HTTP 200, 823,589 bytes, sha256 854e942b470053f3, equal to the source. Notion's file host is reachable from this environment; only the upload host (api.notion.com) is blocked.
- **Links close on evidence.** File blocks under the link line, or a dated disposition a person wrote. A Task marked Done alone never closes a line.
- **Every follow-up Task carries its Show**, the Engagement's Show checked against the Episode's. There is one open Task per Engagement.

## 7b. Revision 4: link follow-ups (cleanup's 107613d verdict)

- **Only a terminal disposition closes a link line**: "not needed" or "cancelled by <who>", with name and date. "expired, asked again <date>" keeps the line open with its owner until the files land or someone cancels.
- **The follow-up Task has a stable key**, Source ID "assets-links:<Engagement page id>", looked up in any Task state. Open: reuse. Done once: reopen once (a "reopened <date>" line on its page body). Done again: report only, create nothing. A newer link line reopens the same Task. No path creates a second Task for the same Engagement.
- Sections 5 and 2 to 4 are unchanged, and so is the inbox patch (+89 bytes). Delta: docs/proposals/ar20261019-5-rev3-to-rev4.diff.

## 8. For Main 1: network setting and upload check (proposed, not done by Main 2)

1. Akshay, in the environment the inbox run uses (env_01Pb9xdJdFEZj6Xuxuq5Kxid; cloud environment menu, Edit, Network access): add api.notion.com under Allowed domains, "Allow package managers" left ticked. Nothing broader; no credentials.
2. Confirm from a session in that environment: a CONNECT to api.notion.com no longer returns 403.
3. Upload check on a genuinely missing file, Rohit Manglik's headshot (no test mail, no Prashant re-upload):
   - Download Gmail 1a056589dddf7302 RAW and decode part 2: 16768.jpg, 115,795 bytes, sha256 800a0253a8496d4b.
   - notion-create-file-upload, then one multipart POST.
   - Place the line and file block under "## Guest assets" on Episode 3ed19a301a7f81c09fcbeb5d8be8e6a0.
4. Readback: re-fetch the Episode with file URLs, download the block, and confirm 115,795 bytes and the same sha256. Only then is binary filing proven end to end.
5. Until steps 1 to 4 pass, every binary file stays "upload blocked", and nobody claims automatic filing works.

## 9. Limits stated plainly

- Binary upload needs api.notion.com allowed in env_01Pb9xdJdFEZj6Xuxuq5Kxid. Text files of 200 KB or less don't.
- Downloads were proven up to a 1.16 MB message. Messages near 25 MB have not been tried; a failure there becomes "download failed" and stays pending.
- Over 20 MB per file (single-part upload limit): pending, filed by hand.
- Links: stored, not downloaded.
- No real test mail and no draft-attachment probe were used. Calling capture reliable needs one real incoming file after deploy and the network change.
