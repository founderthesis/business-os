# Crash window A: recovery on the frozen build (26 Oct, 21:40 JST)

Build: FAST 96c11beae7ec325b, SLOW a5b4ef40cfd85bb1 (8e64140). Reads only; nothing sent.

**Setup (19:20 JST).**
- One self-addressed mail went from Zoya's inbox with idempotency key `40519a301a7f8105a87edf64e65872b7:followup:seq-4-1:2026-10-26T00:00:00+09:00`.
- Its Message-ID is a21e2f20-99d5-4dce-a3ed-2d5a2c7c7ae4@mcpemails.com.
- It was deliberately left unlogged, which simulates a run that died after sending.

**What recovery reads, per the frozen build:**
- ACTIONS: "read your Sent and the thread for a message from us after the action was raised".
- MESSAGE IDENTITY: "Before creating a mail Activity, look up that key ... any hit means it is logged"; "Two Sent copies with one Message-ID are one send".

**Found:**
- Zoya's Sent holds two copies, [Gmail]/Sent Mail:644 and :645, at 10:20:25Z and 10:20:26Z. They are one send: the provider's copy plus Gmail's.
- Zoya's INBOX holds one delivery (INBOX:471).
- Activities have no row with that Message-ID or subject (SQL on Source ID and Summary).

**So recovery:**
- logs one Email out Activity, with Source ID msgid:<that id>, the action key and the sent body;
- completes the action;
- sends nothing.

The Activity write is a Notion write. It is in notion-edits-26oct.md, item 2, for the CTO to apply, because this session's Notion writes still prompt.

**Verdict: PASS.** Recovery found the mail by Sent and Message-ID, and the plan creates exactly one Activity. No resend is possible: the action is complete once the Activity exists, and inside the 24-hour window a resend with the same key would return idempotent_replay anyway (provider-idempotency.md).
