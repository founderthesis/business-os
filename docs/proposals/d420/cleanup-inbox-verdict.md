# Cleanup: quick acceptance of the decision 420 inbox (urgent, Gmail quota outage)

**Verdict: ACCEPTED for deploy. Inbox 65,333 B, sha256 d1bba5802ca8872d.**

Built from HEAD 5d5c709 by `docs/proposals/d420/inbox.py`, on the live inbox prompt. The base was re-read from trig_0189eZvAD8x4357cfevgZ3No today: 61,957 B / aed0215a8bdf6a26, updated 26 Oct 03:32Z. Two builds were byte-identical.

Neither README figure is the current build. 64,968 / be47f9a467b0bc43 is round 6, and replay424's 65,334 / 4d8a49fdf3ca91c7 is an earlier 424 round.

## The CTO's five checks

1. **Under 65,536: yes.** 65,333 B is 203 B under the cap and 3 B under the 65,336 build limit. The next inbox change has to cut text first.
2. **No Gmail connector call: yes, in the text.**
   - "read and written only through MCP Emails ... never the Gmail connector", and the TOOLS line loads only MCP Emails, Notion, Calendar and Blueticks.
   - Every Gmail tool a step still names maps to an MCP Emails call in one table: search, get_thread, raw, rfc822msgid, delete_draft and unlabel_thread.
   - Belt and braces: the Gmail connector is still attached to the trigger. Detach it at deploy so a Gmail call becomes impossible rather than just forbidden. Its quota is exhausted anyway.
3. **Only the loop-in is sent from ad@: yes.**
   - "The only mail you send from ad@thepodium.in is the loop-in", ZOYA LIVE, and HARD RULES' "no other sends, replies, forwards, drafts".
   - STEP 6c queues Akshay's decision mail for Zoya. The Saurabh step's replies are the loop-in. There are no billing forwards (the sweep's, decision 423).
   - The other mailbox actions are draft deletion and RSVP archiving, plus calendar cancellations in STEP 6e (a calendar action, existing behaviour).
4. **Replays: re-run independently on this exact build, offline, by two fresh reviewers with the cases restated and no earlier verdicts shown.**
   - **replayCX P1 to P4: all PASS.** A failed log is retried every run, never dropped, and holds "read to". A run that dies after Started still carries it. Another routine's Activity never moves the cursor. The first run uses 3 days. One Activity per RFC Message-ID, and never collapsed by sender, subject or time.
   - **replay424, inbox cases:** I1 (company employee, one open row) PASS; I2 (new agency, new guest) PASS; I4 (PR who is Via on two rows) PASS; F2 (organisation only, never folded) PASS.
     - **I3** (same domain, a different person named): the exception attaches the sender as a Stakeholder on company membership. That exception is in Akshay's amended decision 424 ("or the booker works at the guest's own company and that company has exactly one open row on that show"), so it is decision-conformant. Its edge, a mail naming a different person, goes to the next change.
     - **F1** (fold) passes with gaps, below.
5. **Unread flags preserved: yes, tested live.**
   - No mark-read or flag call exists: "Reading leaves mail unread", "never flag read or unread", "Never mark anything read in this mailbox" (decision 199).
   - MCP Emails `read` and `original` were run on two unread self-addressed test mails in Zoya's inbox (INBOX:237, INBOX:238). Both stayed unread.
   - ad@ uses the same connector and the same backend (provider imap, service gmail), so reads there leave mail unread too.

## For the next inbox change (none blocks this deploy)

1. **Repeat-pitch loop-in scope:** STEP 3 sends it, but the scope lines say "STEPS 6 to 6b". Either reading is harmless: a skipped loop-in, or a loop-in on a Built to Share or Human by Design repeat pitch.
2. **Two imperatives read as an ad@ send:** STEP 3's "reply that we'd like to keep <original guest>" and YOUR CALL's "decline politely". The three loop-in-only rules override them. Reword them as Zoya's steps.
3. **"Completed" is undefined.** Make it "Completed only when the pending line is empty and nothing failed".
4. **The cursor tracks logging only.** A logged message whose later steps never ran isn't revisited, except the loop-in's catch-up. This predates the change.
5. **"read to" when nothing qualifies:** carry the previous value.
6. **Decision 424 folds:**
   - the duplicate's Via and Guest go only to Stakeholders;
   - "Eval (the kept row's wins)" can drop a valid eval when the kept link is empty;
   - "clear the duplicate's relations" should be "check none remain", and the Episode and Deal links aren't in the move list;
   - which row is kept is unstated.
7. **I3's edge:** limit the company exception to mails that name no other person. **I4:** say what to do when the sender's own lookup returns two rows.
8. **Leftover "Gmail" wording** in steps that the table covers.

Checks:
- Less text and fewer writers: no new writer, and one connector removed from use.
- Selection by prefix or wording: none added.
- Retry double-send: the loop-in still has its existing dedupe.
- Bytes and hashes: above.
