# Episode asset filing (proposed Notion rule page, Controls)

Proposed text for a new rule page under Business OS developer > Rules, marked **Controls**. Main 1 creates the page, puts its id into the inbox passage (PAGEID_PLACEHOLDER_32CHARS_XXXXXX in the patch), and records it on the developer page. Until then nothing below is live. AR-20261019-5, Main 2, 19 Oct 2026. Revision 2 answers Codex's review of dac2f94: download path, recording and file identity, team and Zoya-only coverage.

The page text starts below the line.

---

**Episode asset filing.** The inbox run reads this page every run (STEP 3 edit notes, STEP 6d assets). It is the only writer of "## Guest assets" and "## Assets to file". It stores the original files sent for an episode on that episode's Notion page, so the production and marketing team can open them without a mailbox. Filing is separate from replying: it never sends a mail, never waits on one, and never changes Status, Waiting on or Next action. Storing a file approves nothing, publishes nothing and changes no terms.

**1. Where files come from.** Two inboxes, one filing path:
- ad@thepodium.in: the messages this run reads (Gmail).
- Zoya's inbox (MCP Emails, inbox_id c786413a-f604-4661-9312-e7226917028a): every message of the last 72 hours. List it page by page (has_attachment is ignored there, and list rows can show no attachment when there is one), then read_batch with body_max_chars 0 to see each message's attachments.
A mail that reached both inboxes is one message (same Message-ID, see 3) and is filed once.

**2. What gets filed: decided by purpose and provenance, never by sender or size alone.** File every file sent for a specific episode, by anyone, our team included: guest photos and logos, videos, b-roll, audio, editor drafts and cuts, edit notes, production and internal briefs, research for the episode, thumbnails, clips, release and marketing copy. A file the mail names or asks us to use ("attaching our logo") is filed at any size. Not filed, each with its reason in the report:
- a signature image: an inline image placed in the sender's signature (after the sign-off, often named image001.png) that nothing in the mail points to;
- a copy: the same bytes already filed on that Episode (any message, any inbox), such as a photo quoted back on a later reply. If those bytes are not filed yet, file the earliest message that carries them;
- a template we send to every guest: the same bytes on threads of other Engagements;
- transcripts: they belong to the transcript workflow (the Episode's Transcript file), never here;
- calendar invites (.ics), invoices, contracts and billing (they go to the Deal), and anything not about one episode (a product or sales deck goes on its own Task row or Deal).
If you can't tell whether a file is for an episode, it stays pending (5a) with reason "purpose unclear: <what it looks like>", never silently skipped.

**3. Identity of a message and of a file.**
- Message key: "mid:<first 16 hex of sha256 of the Message-ID header, trimmed>". It is the same in both inboxes and doesn't change when mail moves. A message without a Message-ID stays pending, reason "no Message-ID".
- File key: "<message key>#<MIME part path>", the path being the 1-based part positions from the top of the message, joined with dots (the same path every parse of those bytes gives). Two files with the same name and size in one message are two keys; their sha256 also differs when their bytes differ.
- Every line also carries the file's sha256 (first 16 hex), filename and bytes. A reused filename is never the same file: same key or same sha256 is.

**4. Which recording, which Episode.** Start from the thread's Engagement (Kind not Task) and its Show. A file is for one recording of that Engagement, each recording being one calendar event, keyed "cal:<event id>" (the key the calendar run writes on the Episode's Source ID or as a "Recording key:" line in its page body, AR-20261019-3). Never match by guest name alone: a returning guest has a separate Episode per show and per recording.
a. Explicit: the mail or its thread links an Episode page, or names the recording's date. That recording, if it belongs to this Engagement and Show.
b. Only one: the Engagement has exactly one recording, past or upcoming. That one.
c. Several: the thread's own recording: the only one whose slot was booked, confirmed, moved or thanked on this thread. A thread that spans two recordings, or names none, is not evidence.
d. Otherwise pending, reason "unclear recording: <the dates>". Never the latest earlier Episode by default: an upcoming recording's material is not an earlier Episode's.
The Episode is the one carrying that recording's key, in any status (Scheduled or booked included). An Episode of this Engagement and Show with no recording key counts only when the Engagement has a single recording and a single Episode. No Episode yet for the recording: pending, reason "no Episode yet (cal:<event id>)"; the calendar run creates it and a later run files the file.

**5. Pending first, then download, upload and read back.**
a. Before any download, make sure the Engagement page body has a section "## Assets to file" with one line for the file: "<file key> | <filename> | <bytes or ?> bytes | <reason> | since <YYYY-MM-DD>". The reason is "to file" for now. Write it once; later runs only update its reason. One line per file key, never two.
b. Already filed? The Episode's "## Guest assets" holds a line with this file key, or with this sha256, or (files filed before this page, such as the two Prashant Sachan photos of 19 Oct) a file block with this filename next to a line naming the same Gmail message id and the same byte count. Then mark the pending line "already filed" and stop: no download, no upload, no new line.
c. Download: keep the bytes out of the conversation. ad@thepodium.in: Gmail get_message, messageFormat RAW. Zoya's inbox: MCP Emails email_read, action original. The session saves a large result to a file and shows only its path. Decode that file with a short Python script (Gmail: field raw, base64url; MCP Emails: field data, base64, and check its sha256 field). Parse the message, take the part at the key's path, and write the decoded file under the session's scratch folder with its original filename. Check that the part's filename and type match what the mailbox lists, and compute its sha256. Never print base64 or file contents. A result shown inline (a small message) is fine; a parse failure, a missing part or a mismatch gives reason "download failed: <what>", and you stop for this file. Do the downloads for a run in one subagent that returns only key, path, bytes and sha256, so the main run sees a few lines per file.
d. Upload:
- A UTF-8 text file of 200 KB or less (.txt, .md, .csv, .srt, .vtt that is not a transcript) goes through notion-create-attachment with its content.
- Anything else: notion-create-file-upload with the original filename, then one multipart POST of the file to the upload_url it returns, with every returned header (curl -sS -X POST "<upload_url>" -H ... -F "file=@<path>").
- Over 20 MB: reason "too large for single upload", stop.
- POST refused (for example 403 because api.notion.com is not allowed on this network): reason "upload blocked: <status>", stop. Nothing is filed.
e. Place it on the Episode page body under "## Guest assets" (create the heading if missing, newest first). One line, then the file block:
"<YYYY-MM-DD> | <who> (<company or team>) | <purpose, a few words> | <filename> | <type> | <bytes> bytes | sha256 <first 16> | <file key> | <cal:event id>"
f. Read back: re-fetch the Episode. The file is filed only if the file block with that filename and the line with that key are both there. Then mark the pending line "filed <YYYY-MM-DD>". Either missing: reason "page write not confirmed", and the next run starts again at b, which finds a write that did land.
g. Never write download or upload URLs into any line, note, report or Activity. Never share, publish or move a file.

**6. Links.** A folder or file link (Drive, Dropbox, WeTransfer, Frame.io) is stored as given under "## Guest assets", in a line of the same shape with "link" in place of the type, bytes and sha256, keyed "<message key>#link<n>". This run has no authorised way to download from those services, so the pending line stays open with reason "link only: Sarika saves the files". Once per Engagement, while such a line is open and no open Task row for it exists, create one Engagement row Kind Task, For engagement this Engagement, Waiting on Sarika, Task state Handed over, Next action "Sarika: save <guest>'s linked files to the <D Mon> Episode (links under Guest assets)". When she marks it Done, the next run closes the link lines.

**7. Retries and limits.** Every run takes open "## Assets to file" lines first, oldest first, then new mail. Open lines have no age limit, so work outside the read window is still done. At most 5 uploads a run. If a run stops after an upload but before the page write, the upload expires and the next run uploads again. If it stops after the page write but before marking the pending line, 5b finds the file and only marks the line. A failed file never marks anything filed and never closes another file's line.

**8. Edit notes.** File the original attachment exactly as above, with purpose "edit notes". The extracted list of changes stays where STEP 3 writes it: extraction never replaces the file.

**9. Pointer.** The first time a file is filed for an Engagement, add one line to its page body under "## Guest assets": "Files for this guest are on the Episode: <Episode mention>". Add it once; never copy the files onto the Engagement.

**10. Report and notes.** One report line per file: filed, already filed, pending (with reason) or not filed (with reason from 2). Add a Claude note line on the Engagement only when something was filed: "<YYYY-MM-DD>: filed <n> asset(s) on the <D Mon> Episode".
