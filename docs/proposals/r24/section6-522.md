# Section 6 WHATSAPP CHASE for decisions 519 and 522 ("Inbox and Your call rules", Controls page 3ff19a301a7f8148993ccea78fc66428)

The CTO pastes this at deploy. It **replaces the whole WHATSAPP CHASE block** in "## 6. Your call", from its first line ("WHATSAPP CHASE (decision 486, ...") through 5/. It also supersedes section6-519.md: step 1/ below already holds 519's change. The two lines after 5/ ("Team messages keep Zoya's signature ...") stay as they are, and so do the headings and the END line.

Decision 522 (Akshay, 7 Nov 23:34 JST) refines only the draft. Contact matching (519), cadence, holds, the exact-draft ok and the send-as-Akshay rule are unchanged.

```
WHATSAPP CHASE (decision 486, Akshay, 6 Nov: "go, I will review each draft"; decision 522, 7 Nov: "she should read past messages and then accordingly draft a message, keeping in mind salutation and style ... 1-2 short messages, and something that shows I am paying attention to them"). A Your call "whatsapp chase: <intent or "quoted text">" on a guest row (Kind not Task):

1/ The recipient is the Guest, else the person the call names (a Via or a Stakeholder on the row). Draft for them whether or not their People Phone is filled: the WhatsApp routine finds the number when it sends (STEP 0w, decision 519).

2/ Read before drafting. Find that person's one-to-one chat with Akshay in Blueticks (chats search by their full name, matched as STEP 0w matches it; read only, never a group, never anyone else's chat) and read its recent messages: the last real exchange, the open ask, any promise, and whether they have already answered it. Read the row's newest Activities and the mail thread where they help.
- Already answered, or the ask is settled: write no draft. Claude note line "YYYY-MM-DD: WhatsApp chase not drafted: <what settled it, D Mon>", clear Your call, and put one line on his list only if something is left for him.
- No chat found, or not sure it's the right person: the draft can still be written from the row and the thread, but its context line says so, and it never pretends to know the chat.

3/ Write the draft at the top of the page body under "## WhatsApp draft (<YYYY-MM-DD>, to <name>)":
- If the call quotes text, use it verbatim.
- Otherwise write it the way Akshay writes to that person in that chat: the same greeting (or none), the same form of their name, the same language and case, about the same length. With no chat to go by: lowercase, "hi <first name>" at most.
- 1 or 2 short messages, one clear ask, no email-style opening, no paragraph, no list of past reminders. Two messages go on one line, separated by " || ".
- One detail that shows he's paying attention, when there is a true one: something from their own last exchange, or genuinely recent news about them or their company that a quick check verifies (no news search every time). Never invent one, never say or imply Akshay saw or read something there's no sign he did, no forced praise, and never anything private learnt from someone else.
- No link outside the approved short links, nothing LEAK CHECK bars, SHOW CHECK on a client show. It goes as Akshay, so never Zoya's name or signature.
- Under the draft, on its own line: "context: <chat read: first and last message dates, or "chat not found" or "person not certain">; used: <the message or detail used>; news: <URL, or none>". The context line is never part of the text that gets sent.

4/ Write the Next action segment "Akshay: ok the WhatsApp to <first name>? (draft on the row, <D Mon>)", put Akshay in Waiting on, write the Claude note line ("YYYY-MM-DD: Akshay's call: '<text>'; WhatsApp draft written") and clear Your call.

5/ Act on his Your call on that ask:
- "ok", "yes" or "go": copy the draft text exactly as it stands on the row now (the message line, never the context line) into the same section, as the line "approved text (<YYYY-MM-DD HH:MM JST>): <text>". The ok approves that text and nothing typed later. The segment becomes "Zoya: send the approved WhatsApp to <first name> (<draft date>)", Waiting on Zoya. Akshay leaves Waiting on unless another segment of his stays.
- A change: redraft under a new dated heading (reading the chat again if it moved), retitle the old one "(superseded)", and ask again as in 4/.
- "no": drop the segment and retitle the section "(dropped)". The text stays as history.

6/ Never send it from inbox actions. The WhatsApp routine's STEP 0w sends only the approved text, from Akshay's WhatsApp, as one message, or two in order when it holds " || ". It sends outside quiet hours, at most 10 chasers a day, logged under the key "wa-chase:<row id>:<draft date>". A draft section without an approved text line is never sent.
```

## What changed against the live block

- **1/:** decision 519. It drafts whether or not People Phone is filled, and STEP 0w finds the number.
- **2/ is new:** read the person's chat first. If it's already answered, no draft.
- **3/:** mirror his style; 1 or 2 messages joined by " || "; one true detail; the context line, which is never sent.
- **5/:** the approved text copies the message line only.
- **6/:** two-part sends.
- **4/:** unchanged apart from its number, since the steps moved down by one.

## The prompt side (r24, this commit)

- **Inbox actions:** its pointer to section 6 now says to read that person's one-to-one chat with Akshay through Blueticks, read only, before drafting. Its connector list already has Blueticks, and its hard rule limits only WhatsApp sends.
- **WhatsApp STEP 0w:**
  - 4/ sends one message, or two in order when the approved text holds " || ", and never sends the context line.
  - 2/'s crash check looks for each part in the chat, so a part that already went is never sent twice.
