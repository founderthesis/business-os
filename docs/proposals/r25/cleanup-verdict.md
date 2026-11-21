# Cleanup verdict: r25 item 1 (WhatsApp as Akshay, decisions 535 and 537, PaaS approve-each) accepted at 169abf1; the 7-day per-person limit is still to come

Cleanup session, 10 Nov 2026, about 20:40 JST. Read-only. The one-set-per-person-per-7-days delta isn't pushed yet; I'll review it as a delta, and the deploy table below is final except for the WhatsApp line.

## Builds (each twice, byte-identical, equal to the commit; no new em dash; all under the caps)

| # | Routine | Base | Bytes / sha256 |
|---|---|---|---|
| 1 | Section 6 paste (r25/section6-535.md, replaces the WHATSAPP CHASE block and adds WHATSAPP INVITE) + Inbox actions | r24 845d0a41 | 48,332 / b9101c39987ca605 |
| 2 | WhatsApp (**changes with the 7-day delta**) | r24 bec8c1e1 | 35,841 / 6cfe881a09d57625 |
| 3a | zoya-slow-pin, moved to f6793c223a268f3d013c8bf93157b3955163adbd | | SLOW file 94,554 / 76080f19ee5675fd (94,550 characters) |
| 3b | Zoya SLOW task | r24 595f107f | 15,949 / b13ee043dfc8ce2f |

Unchanged: Zoya hourly 62,978 / 459d1dd1, calendar, capture, sweep, host boards, dossiers.

The SLOW task fetches f6793c2, expects sha prefix 76080f19ee5675fd and 94,550 characters, all matching the file.

Note: inbox actions isn't unchanged as the CTO's message says. 9a052ef changed its section 6 pointer (r24 845d0a41 to 48,332 / b9101c39), so it deploys with the paste.

## The CTO's checks

**(a) Nothing goes without a tick except the two standing templates, and only with the authorised writer's marker: holds, with S1.**
- STEP 0w sends only a draft with "Send WhatsApp" ticked, or one whose first line is "[standing: community-invite]" or "[standing: release-day]" and whose check holds:
  - community-invite: a Claude note line keeping Akshay's "invite <name>", a recording on the row, and FT Community at To invite or Invited, never Added;
  - release-day: the line "release-day WhatsApp drafted (Episode copywriter chat)", the Episode Published or with Actual release set, and its Short link in the draft.
- "Only those two are standing: nothing on a PaaS row goes without his tick." The SLOW file writes PaaS drafts "for his tick, never with a '[standing: ...]' line".
- A failed check or an unknown template sends nothing and goes to Akshay as one segment.
- **S1:** the community-invite check says only "a Claude note line keeping Akshay's 'invite <name>'". Pin it to the exact lines the two writers produce: 0a e0's "Akshay's call: 'invite <name>' (WhatsApp); standing invite drafted" and section 6's "Akshay's call: 'invite <name>'; standing invite drafted". As written, any note line that quotes an "invite" (an old call, a mail summary) could satisfy it.

**(b) Reply check across ad@, Zoya's inbox and the WhatsApp chat: holds, with S2.**
- NO REPLY reads ad@ and Zoya's inbox by every address on the person's People row, and their WhatsApp chat since our last message. A reply means untick and "Akshay: <name> replied, draft held".
- **S2:** it checks only the recipient. A reply from their PR or EA on the guest's row (by mail, which capture logs as an Email in Activity) doesn't hold a chaser to the guest. Add: "or any Email in Activity on the row from their side since the draft was written".

**(c) Number from People Phone only, with a country code: holds.** No FT Community, chat-search, thread, signature, form or memory number. With none, or no + or 00: untick and "no WhatsApp number". 519's lookup is gone (decision 535), so the CTO's enrichment should land before deploy, as the hand-off says.

**(d) Cap, quiet hours, 7 days:**
- 20 sets a day: holds, counted from "Akshay to" Activities with Source ID wa-send: or wa-chase:, by JST day, one person's set once.
- Quiet hours: hold (00:30 to 07:30 JST), and release-day only after 10:00 IST. One news post per member a quarter.
- **The 7-day per-person limit: not built** (the hand-off's open item 2). The coming delta.

**(e) Log before send, no double send on retry: holds.**
- The key is "wa-send:<row>:<first 12 hex of the draft's sha256, in python>". The Activity "Zoya sending ..." is logged before any send.
- On retry, a "Zoya sending" key means each message is looked up in the chat, and one found is never re-sent. Each message also carries its own idempotency key ("...-<n>").
- A failed send clears the key and unticks.
- The draft and tick are cleared only after the sends.

**(f) Sizes: hold.** WhatsApp is 35,841, SLOW task 15,949 and actions 48,332, all under 65,536. The hourly is unchanged at 62,978.

Also checked:
- 3n (Saturday news) writes drafts on the guest's Founder Thesis Engagement, which is what 0w reads, for his tick only.
- 3n is in the status-in-code step list (0, 0d, 0w, 1, 2, 2b, 3, 3n, 3d, 4).
- The 486/522 chaser goes through 0w, and the context line sits in the page body, never the column.
- One message per line settles my r24 " || " note.

## Should-fix (not blocking)

- **S1:** pin the community-invite check to the exact note lines above.
- **S2:** count a reply from the row's other people (Via or Stakeholders, by Email in Activity since the draft).
- **S3. The tick approves "the text at that moment", but nothing records it.** A team edit after Akshay ticks would go out as edited. The hand-off accepts team-level trust, and I agree for now. If it matters later, 0w can compare the draft's sha with the version at the tick, through Notion version history.
- **S4. Transition:** chasers mid-flow under the live 522 flow ("approved text" line plus "Zoya: send the approved WhatsApp to <name>") won't be sent by the new 0w, which reads only the column and the tick. Before deploy, query for that segment and move each one's approved text into "WhatsApp draft" with the box ticked, or put it back to Akshay.
