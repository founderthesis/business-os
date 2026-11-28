# Decision 486: WhatsApp chasers as Akshay, each one approved (hand-off)

Main, 6 Nov. Decision 486 is in force in the Notion ledger (Akshay, 6 Nov: "I want Zoya to send follow up chasers on whatsapp as me", "go, I will review each draft"). Nothing is deployed and nothing was written to Notion.

## Builds

Each was built twice, byte-identical, with no em dash added.

| Routine | Live base (6 Nov B-round deploy) | Build | Bytes / sha256 |
|---|---|---|---|
| Inbox actions (trig_012HbtmVKHUDeFZnFyooSgL3) | 459e4041 (b-round-5nov/actions.txt) | actions.txt | 46,693 / 6a97144aaa5bbe2a |
| WhatsApp to Business OS (trig_01MnmJYorWrd61K7b5BCqXr1) | 174d9317 (b-round-5nov/whatsapp.txt) | whatsapp.txt | 30,065 / 9ef1372585ad0c96 |

Command: `python3 patch.py <act|wa> <live prompt> <out>`. It asserts the live hash and each edit exactly once.

Plus `section6.md`: the WHATSAPP CHASE paragraph, added at the end of section 6 on the Controls page "Inbox and Your call rules". The inbox actions prompt already defers to that page, so the rule lives there and the prompt only points to it. The page change is a Notion write for the CTO. **Deploy it before or with the actions build.** Without it, inbox actions has the pointer but not the steps.

## How it flows

1. **Akshay asks.** He writes "whatsapp chase: <intent>" or "whatsapp chase: \"<his text>\"" in Your call.
2. **Inbox actions drafts.** The next run (section 6):
   - finds the recipient's People Phone. If there's none, the row gets the step "Akshay: no WhatsApp number for <name>".
   - writes the draft at the top of the page body in his voice: lowercase, 1 to 3 lines, one ask, no sign-off, never Zoya's name.
   - puts "Akshay: ok the WhatsApp to <first name>? (draft on the row, <D Mon>)" on his list.
3. **Akshay approves.** His "ok" copies the draft as it stands into an "approved text" line and hands the row to Zoya as "Zoya: send the approved WhatsApp to <first name> (<date>)". A change redrafts and asks again. "no" drops it.
4. **The WhatsApp routine sends.** STEP 0w, the fourth exception to READ-ONLY:
   - It sends only the approved text, exactly as written, as one message.
   - The chat id comes from that person's People Phone and nowhere else.
   - It holds off in quiet hours (00:30 to 07:30 JST) and once 10 have gone that day.
   - The Activity "Zoya sending: ..." is logged under the key "wa-chase:<row id>:<draft date>" before the send and renamed "Akshay to <name> on WhatsApp: ..." after it.
   - A failure goes back on Akshay's list.
   - A key already on a sent row is never sent again, and a crash mid-send is checked against the chat before any resend.
   - Replies arrive through STEP 2 as usual.

## What it replaces

Only for guest chasers, it replaces Akshay's 15 Oct "never pose as Akshay" rule. Team messages and every other WhatsApp send keep Zoya's signature. CLAUDE.md's Writing rules still state the 15 Oct rule without the exception; that line needs the 486 carve-out (a CTO edit).

## For Cleanup

Points to check:
- **The number source.** People Phone only, and an Indian 10-digit number gets 91 in front.
- **The approval binding.** Only the "approved text" line is sent, never the draft above it.
- **Ordering and counting.** The log comes before the send, and the cap counts "Akshay to" rows by JST day.
- **Fit with existing rules.** STEP 0w must sit cleanly with PRIVACY ("decide whether a chat is work") and with the READ-ONLY list.

One gap I noticed but haven't fixed: section 6's own text still says "Proposals you write in Next action end with 'Write ok, not ok or a change in Your call.'", which B12 retired everywhere else. Removing that sentence is a one-line page edit for the CTO, alongside this one.
