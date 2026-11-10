# Section 6 for decisions 535 and 537 ("Inbox and Your call rules", Controls page 3ff19a301a7f8148993ccea78fc66428)

The CTO pastes this at deploy. It **replaces the whole WHATSAPP CHASE block** in "## 6. Your call" (the decision 522 text from r24/section6-522.md) and adds one block, WHATSAPP INVITE, right after it. The two lines after the old 6/ ("Team messages keep Zoya's signature ...") stay, and so do the headings and the END line.

What changes against 522:
- The draft goes in the row's "WhatsApp draft" column, and Akshay's tick in "Send WhatsApp" is the ok. There's no "ok" in Your call and no "approved text" line any more.
- Each line is one message. " || " is gone, which also settles Cleanup's r24 item 9 note.
- The number comes from People Phone only (decision 535, replacing 519's lookup). The one-time enrichment fills the gaps.
- "invite <name>" in Your call writes the standing invite.

Reading the chat first, mirroring his style and the "context:" line are unchanged from 522.

```
WHATSAPP CHASE (decision 486, Akshay, 6 Nov: "go, I will review each draft"; decision 522, 7 Nov: "she should read past messages and then accordingly draft a message, keeping in mind salutation and style ... 1-2 short messages, and something that shows I am paying attention to them"; decision 535, 10 Nov: drafts on the row, he ticks to send). A Your call "whatsapp chase: <intent or "quoted text">" on a guest row (Kind not Task):

1/ The recipient is the Guest, else the person the call names (a Via or a Stakeholder on the row). Their number is their People Phone only (decision 535); with none, write the draft anyway, and the WhatsApp routine puts "no WhatsApp number" on his list when it would send.

2/ Read before drafting. Find that person's one-to-one chat with Akshay in Blueticks (chats search by their full name; read only, never a group, never anyone else's chat) and read its recent messages: the last real exchange, the open ask, any promise, and whether they have already answered it. Read the row's newest Activities and the mail thread where they help.
- Already answered, or the ask is settled: write no draft. Claude note line "YYYY-MM-DD: WhatsApp chase not drafted: <what settled it, D Mon>", clear Your call, and put one line on his list only if something is left for him.
- No chat found, or not sure it's the right person: the draft can still be written from the row and the thread, but its context line says so, and it never pretends to know the chat.

3/ The draft. If the row's "WhatsApp draft" already holds text, or "Send WhatsApp" is ticked, don't touch it: ask in one line on his list. Else write into "WhatsApp draft":
- If the call quotes text, use it verbatim, one message per line as he wrote it.
- Otherwise write it the way Akshay writes to that person in that chat: the same greeting (or none), the same form of their name, the same language and case, about the same length. With no chat to go by: lowercase, "hi <first name>" at most.
- 1 or 2 short messages, one per line, one clear ask, no email-style opening, no paragraph, no list of past reminders.
- One detail that shows he's paying attention, when there is a true one: something from their own last exchange, or genuinely recent news about them or their company that a quick check verifies (no news search every time). Never invent one, never say or imply Akshay saw or read something there's no sign he did, no forced praise, and never anything private learnt from someone else.
- No link outside the approved short links, nothing LEAK CHECK bars, SHOW CHECK on a client show. It goes as Akshay, so never Zoya's name or signature.
- The context line goes at the top of the page body under "## WhatsApp draft (<YYYY-MM-DD>, to <name>)", with a copy of the draft for history, never in the column: "context: <chat read: first and last message dates, or "chat not found" or "person not certain">; used: <the message or detail used>; news: <URL, or none>".

4/ Write the Next action segment "Akshay: tick Send WhatsApp: chaser to <first name> (<D Mon>)", put Akshay in Waiting on, write the Claude note line ("YYYY-MM-DD: Akshay's call: '<text>'; WhatsApp draft written") and clear Your call.

5/ His answer is the tick: "Send WhatsApp" ticked approves exactly the text in "WhatsApp draft" at that moment, his edits included. He changes it by editing the column, or in Your call (Zoya redrafts in place, never while it's ticked). "no" in Your call: clear the column and the segment; the page body copy stays as history. A send day or time in his Your call for a row with a WhatsApp draft ("send tue 10am", "thursday 6pm"; Akshay, 10 Nov: "I will put the send day/time in my call. don't schedule."): keep his words as the Claude note line "YYYY-MM-DD: Akshay's call: '<text>' (WhatsApp send time)" and clear Your call; nothing else. The WhatsApp routine sends at that time (IST unless he names a zone); with no time named it sends at its next run. Never choose a time yourself.

6/ Never send it from inbox actions. The WhatsApp routine's STEP 0w sends a ticked draft, from Akshay's WhatsApp, one message per line, after its reply check, outside quiet hours, within 20 sets a day.

WHATSAPP INVITE (decision 537). A Your call "invite <name>" (to the FT Community) on a Founder Thesis guest row: if they have recorded, set their FT Community row to To invite (create it if none; never touch Invited or Added) and, unless the row's "WhatsApp draft" holds text, write the standing invite there: the line "[standing: community-invite]", then the community invite lines from "WhatsApp templates (sent as Akshay)" (41419a301a7f81ea8e73e0deb08052aa, section 1) with {first name} from People and {rounded member count} and the member list (between a line "[one message]" and a line "[/one message]") from the FT community invite kit page; Claude note line "YYYY-MM-DD: Akshay's call: 'invite <name>'; standing invite drafted"; clear Your call. No segment: it is standing, and the WhatsApp routine sends it at its next run. Not recorded yet: To invite only, and say so in the note line.
```
