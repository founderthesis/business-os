# Transcripts stuck in Akshay's Sent mail: proposal (CTO, 22 Oct 15:45)

Nothing here is built. It waits for Akshay's yes, relayed by the CTO.

## What's stuck

Zoya's 15:39 run left 8 rows at "attach the transcript from Akshay's Sent thank-you": Amit Das, Amit Patni, Ankit Mehra, Anmol Madan, Ashish Goel, Prashant Sachan (B2S), Raunak Bhinge and Vicky Dodani. The .txt files are on those thank-you mails. Zoya reads the mail but can't move the file into Notion: she'd have to retype tens of KB into a tool call.

The duplicate "ask Ranjita" rows: there were 5, not 8 (Amit Das, Ankit Mehra, Anmol Madan, Ashish Goel, Raunak Bhinge). All 5 are closed as of 22 Oct, Task state Done, each pointing at its 21 Oct row. Ranjita said on 21 Oct they aren't needed. The calendar's STEP 4 transcript step made them: it skips a recording only when a row already has Source ID "transcript:cal:<event id>", and the 21 Oct rows carry "mcpemails:" ids.

## What I checked (read only, 22 Oct)

- MCP Emails `email_read` action `attachment` on Raunak Bhinge's 9 Oct thank-you returned the full file. The result was too large to show, so the session saved it to disk. Decoded there, it's 79,914 bytes, the attachment's stated size (sha256 f7b837210f04646c).
- Notion `create-file-upload` returns an upload URL that takes one multipart POST of up to 20 MiB, so Bash can upload the file straight from disk. `create-attachment` with inline content would mean retyping the text: not used.

So the bytes never have to pass through the model.

## Options

1. **Builder pass from Main (recommended).** One script, one run, for the 8 rows. For each: find the Sent thank-you, fetch the attachment (MCP Emails), decode it from the saved result, check the size against the mail's stated size, sha256 it, create a file upload, POST it with curl, set the Episode's Transcript file, write "## Transcript" (file, bytes, sha256, source) at the top of the Episode body, and close the row. Then the decision 374 test on the Founder Thesis rows still at Booked. About 8 Notion writes per row; I'd list every planned write first and run them in one pass. No mail is sent. Cost: one session, roughly an hour.
2. **Mac task.** The existing "transcripts backlog on the Mac" row (mac-transcripts-v2) does this from Akshay's Mac. It needs Akshay to start it, and it already waits on him. Not recommended: it puts work on him.
3. **Drive copy.** Copy each .txt into the "Zencastr Transcripts" Drive folder, then let Zoya's step c take it from there. It only moves the problem: Zoya would still have to get bytes from Drive into Notion.

## Routine fixes (with the next batch, after option 1)

- **Calendar STEP 4 dedupe:** skip a recording when any open Kind Task "Transcript:" row exists for the same Engagement (For engagement) and date, whatever its Source ID.
- **Zoya INTERNAL TASKS c(1)-(2):** the same deterministic path. Fetch the attachment, decode the saved result in Bash, check bytes against the stated size, then create-file-upload and curl. Never inline content. If the result isn't saved to disk (a small file shown inline), she uses create-attachment, which takes up to 200 KB, as now.
- Open question for Cleanup: the routine sessions need network access to Notion's upload host for the curl POST. I haven't tested that from a routine.
