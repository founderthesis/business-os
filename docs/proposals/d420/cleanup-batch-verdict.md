# Cleanup: d420 batch, calendar, sweep and WhatsApp

Built from HEAD (cc84214 and later) on the live prompts:
- calendar 55,082 / 8fb664a1c94776b5, read from its trigger today;
- sweep 33,824 / 7af60faaa021fa64;
- WhatsApp on B2 as amended, 28,344 / 5cac9f1325c2f2ba, rebuilt here from the live 26,007 / 9e8b9f4891e9c03d.

Two runs of `batch.py` were byte-identical. An independent offline replay was run on the exact builds, without the earlier verdicts.

## 1. Calendar: ACCEPTED as the B1 build, 57,968 B / f6d140196f3b75b4

- The batch output alone (56,348 / b6d381c24680e75a) does **not** carry decision 424. The replay failed it on K2 (an EA from the guest's company gets her own row) and K3 (a PR booking for one of two guests gets a row). Don't deploy it alone.
- `docs/proposals/b1/calendar_b1.py` on that output adds BOOKER and FOLD (424). Built twice, identical: 57,968 / f6d140196f3b75b4, 7,368 B of headroom.
- Traced on that text:
  - **K2 passes:** "the booker works at the guest's own company (not an agency) and that company has exactly one open row on that show ... add the person to that row's Stakeholders ... and create no row".
  - **K3 passes:** "A booker who acts for someone else ... without that evidence, or with two candidate rows: attach nothing, create nothing, one report line".
  - Only "someone booking for themselves with no match gets a new Engagement".
- **420, from the replay:**
  - no Gmail path (TOOLS has no Gmail, and MAILBOX says "never the Gmail connector");
  - no mail sent from ad@ ("ad@thepodium.in is otherwise only read (MAILBOX) and drafted in");
  - the thank-you is a draft in ad@, "never sent by you";
  - no mark-read.
- B1's bos-key removal isn't in this build. The event key is still `bos-key:`.
- Follow-ups:
  - **Zoya's replies:** say "a reply uses a message read from Zoya's inbox; if the thread isn't there, a new mail". A reply on an ad@ message id under Zoya's inbox_id would fail, not send from ad@, but the wording should close it.
  - HARD RULES says "Two exceptions" and then lists four.
  - The fold's Guest and Via go into Stakeholders (the same note as Zoya and the inbox).
- **For Akshay (it predates 420):** five calendar actions use notificationLevel ALL, so Google emails attendees from ad@'s calendar:
  - delete a duplicate booking;
  - add the studio link;
  - delete a call cancelled in writing;
  - create the host prep invite;
  - move the un# host prep invite.

  Decision 420 limits mail agents send. These are calendar notices, so whether they're allowed is his call, not Cleanup's.

## 2. Sweep: ACCEPTED, 35,047 B / 06c4120b2cd48ef1

- **S1 passes, the billing forward (423).** It goes through MCP Emails `forward` on the ad@ inbox, with idempotency_key "billing:<Message-ID>", and is skipped if an Activity or Sent already holds it.
- **S2 passes:** a transaction alert isn't forwarded.
- **S3 passes (422):** "never a un# sponsored pursuit" in 3r.
- **S4 passes:** "Never send mail other than STEP 6c"; the 3d drafts are "Never send it".
- No Gmail call path, and no mark-read.
- Follow-ups:
  1. **STEP 3 (b2) and (c), and STEP 4's "Promise lapsed" and "Quiet", lack 3r's un# exclusion.** They can move a un# sponsored row to LT chase or flag a chase. Zoya's own 422 rule stops any send, so the risk is row state, not mail.
  2. Line 20 still names `get_thread`. It should name MAILBOX's thread recipe.
  3. The 6c Sent check, "same subject, sender and date", doesn't fit a forward's own headers. The Activity and the key are the real guards.

## 3. WhatsApp with B2: NOT ACCEPTED, three privacy fixes (owner Main)

29,352 B / 9eef0b863062cab2 reproduces. W1 (work group), W2 (family chat, never named, nothing posted) and W3 (ad@ read through MCP Emails only) pass.

Three gaps in B2's 0a1 text touch Akshay's family chats. Cleanup missed the first one in its 28 Oct B2 acceptance:

1. **A phone number stored in Notion.** 0a1 logs Source ID "wa:<message key>", and a Task row uses the same. A WhatsApp message key carries the chat id, which in a one-to-one family chat is that person's phone number. PRIVACY bans chat ids only in titles, Next action, notes and reports, not in Source ID. Fix: for a chat that isn't work, use only the message-id part of the key (or its sha256) as the Source ID.
2. **The context read is unbounded.** "one list_messages with its chat_id and until = his message time" sets no limit, while the rule says 20. Fix: add "limit 20".
3. **A link from a non-work chat can reach Notion.** "a Task row keeps any link in the quoted message in its Next action" has no non-work exception, against "nothing of them is logged, quoted or named". Fix: "in a work chat only".

Further follow-ups:
- 0a and 0a1 reply before logging, so a crash can give a second reply. Log first, as 0d does.
- 0a a says both "most recently active if several" and "ask which one".
- 0d c books events with outside attendees under notificationLevel ALL, with no quiet-hours check. That's decision 378's standing approval, which predates 420.

All three replace the WhatsApp line in `batch.py`'s accepted-input set once B2 is rebuilt, so the batch output hash will change.

Checks:
- Less text and fewer writers: no new writer.
- Selection by prefix or wording: none added.
- Retry double-send: the sweep forward is deduped three ways. The WhatsApp reply-before-log is a follow-up.
- Bytes and hashes: above.
