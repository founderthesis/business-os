# Episode asset filing (proposed Notion rule page, Controls)

Proposed text for a new rule page under Business OS developer > Rules, marked **Controls**. Main 1 creates the page, puts its id into the inbox passage (PAGEID_PLACEHOLDER_32CHARS_XXXXXX in the patch), and records it on the developer page. Until then nothing below is live. AR-20261019-5, Main 2, 19 Oct 2026.

The page text starts below the line.

---

**Episode asset filing.** The inbox reads this page every run (STEP 3 edit notes, STEP 6d assets). It stores the original files that guests, PRs and companies send for an episode on that episode's Notion page, so the production and marketing team can open them without Gmail. Filing is separate from replying: it never sends a mail, never waits on one, and never changes Status, Waiting on or Next action. Storing a file approves nothing, publishes nothing and changes no terms.

**1. What gets filed.** Files sent for a specific recorded or booked episode: guest photos, logos, videos, b-roll, audio, production briefs, edit notes, marketing and release documents. Folder or file links (Drive, Dropbox, WeTransfer) are filed as links, see 6. Never filed:
- signature images and tracking pixels (inline images under 20 KB, image001.png-style names, logos inside a signature);
- calendar invites (.ics);
- any file our side sent, including our own transcript coming back quoted on a reply;
- anything not about an episode. A product or sales document goes on its own Task row or Deal, not an Episode.

**2. Which Episode.** Start from the thread's Engagement (Kind not Task). Use only Episodes in that Engagement's Episode relation on the Engagement's own Show. Never match by guest name alone: a returning guest has a separate Episode per show and per recording. If there is more than one, take the one whose Recording date is the latest on or before the message date. If there is still more than one, or none, don't guess: the file stays pending (step 5) with reason "unclear episode" or "no Episode yet". Booked but not yet recorded is "no Episode yet". The calendar run creates the Episode, and a later run files the file.

**3. Identity of a file.** Each file has one key: "gmail:<Gmail message id>#<attachment position>", plus its filename and byte size.
- Take the Gmail message id from the Gmail connector, which is what Activities already use.
- To fetch the bytes, find the same message in MCP Emails (ad@thepodium.in): same sender, same date to the second, same subject.
- Check that the attachment's filename and size_bytes match before using it.
A reused filename is not the same file. Same name with different bytes, or a different message, is a different file, and both are kept.

**4. Already filed?** A file is already filed when the Episode page body, under "## Guest assets", holds a file block with that filename, and a line naming the same Gmail message id (as "gmail:<id>" or a mail link ending in /<id>) and the same byte count. Then do nothing more for it: no upload, no new line. This covers files filed by hand, such as the two Prashant Sachan photos of 19 Oct.

**5. Pending first, then upload.**
a. Before any upload, make sure the Engagement page body has a section "## Assets to file" with one line for the file: "<key> | <filename> | <bytes> bytes | <reason> | since <YYYY-MM-DD>". The reason is "to upload" for now. Write it once; on later runs only update its reason.
b. Download the bytes: MCP Emails email_read, action attachment, on that message and position. The run saves the original file on disk and prints its path. Check that the file's byte count equals size_bytes, and compute sha256 (shasum -a 256 or sha256sum). A mismatch: reason "download mismatch", stop for this file.
c. Upload:
- A text file of 200 KB or less (.txt, .csv, .md, .srt) may go through notion-create-attachment with its content.
- Anything else: notion-create-file-upload with the original filename, then one multipart POST of the file to the upload_url it returns, with every returned header (curl -sS -X POST "<upload_url>" -H ... -F "file=@<path>").
- Over 20 MB: reason "too large for single upload", stop.
- If the POST fails (for example 403 because the upload host is not allowed on this network): reason "upload blocked: <status>", stop. Nothing is filed.
d. Place it on the Episode page body under "## Guest assets" (create the heading if missing, newest first). Write one line, then the file block:
"<YYYY-MM-DD> | <who> (<company>) | <purpose, a few words, in their words> | <filename> | <type> | <bytes> bytes | sha256 <first 16> | gmail:<message id>#<position>"
e. Read back: re-fetch the Episode. The file is filed only if the file block with that filename and the line with that key are both there. Then mark the pending line "filed <YYYY-MM-DD>". If either is missing, the reason becomes "page write not confirmed" and the next run retries from 4.
f. Never write download or upload URLs into any line, note, report or Activity. Never share, publish or move a file.

**6. Links.** A folder or file link is stored as given under "## Guest assets", in a line of the same shape with "link" in place of the type and bytes. A link is not a stored file, so the pending line stays open with reason "link only: someone opens it and adds the files". It is shown in the report until a person adds the files and marks the line done.

**7. Retries.** Every run takes open "## Assets to file" lines first, oldest first, then new mail. Open lines have no age limit, so work outside the read window is still done. At most 3 uploads a run (each download is heavy). If a run stops after an upload but before the page write, the upload simply expires and the next run uploads again. If it stops after the page write but before marking the pending line, the next run finds the file in step 4 and only marks the line. A failed file never marks anything filed and never closes another file's line.

**8. Edit notes.** File the original attachment exactly as above, with purpose "edit notes". The extracted list of changes stays where STEP 3 writes it: extraction never replaces the file.

**9. Pointer.** The first time a file is filed for an Engagement, add one line to its page body under "## Guest assets": "Files for this guest are on the Episode: <Episode mention>". Add it once; never copy the files onto the Engagement.

**10. Report and notes.** One report line per file: filed, already filed, pending (with reason), or skipped (with reason). Add a Claude note line on the Engagement only when something was filed: "<YYYY-MM-DD>: filed <n> asset(s) on the <D Mon> Episode".
