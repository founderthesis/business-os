# Section 6 edit for decision 519 ("Inbox and Your call rules", Controls page 3ff19a301a7f8148993ccea78fc66428)

The CTO pastes this at deploy. Only step 1/ of WHATSAPP CHASE changes. Nothing else on the page moves.

Replace this paragraph:

```
1/ The recipient is the Guest, else the person the call names (a Via or a Stakeholder on the row). Their number is that person's People Phone only, never one from a thread, a signature, a form or memory. If there's none, write the segment "Akshay: no WhatsApp number for <name> (<D Mon>)", put Akshay in Waiting on, write the Claude note line, clear Your call and stop.
```

with this one:

```
1/ The recipient is the Guest, else the person the call names (a Via or a Stakeholder on the row). Draft for them whether or not their People Phone is filled. The WhatsApp routine finds the number when it sends (STEP 0w, decision 519): People Phone, else their FT Community row's WhatsApp ID, else the one saved WhatsApp contact matching their full name (with their company where it's saved). It writes that number to People Phone before it sends. When all three come up empty, it puts "Akshay: no WhatsApp number for <name>" on the row. Never a number from a thread, a signature, a form or memory.
```

## Why the lookup sits only in STEP 0w

- **One place:** the lookup needs Blueticks chats search, and the WhatsApp routine is the one that sends. Section 6 used to stop at "no People Phone" before Akshay even saw a draft. That's exactly what happened with Yash Varyani and Abhijith H K: their numbers were in FT Community or saved contacts.
- **No inbox actions change:** the prompt only points to section 6. It never says "People Phone only", so it doesn't need an edit.
- **The no-number ask moves:** it now reaches Akshay from STEP 0w, at the first send attempt after his ok. It used to arrive before he saw the draft.
