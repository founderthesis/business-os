# Crash window B: outside the dedupe window (26 Oct, 23:39 JST)

This was the one approved test send (send-plan.md). It went at 14:39:43Z from Zoya's inbox to her own address, with no idempotency key, which simulates a send outside the provider's 24-hour window.
- Message-ID: f3ce2f38-067e-4e3e-99bb-f5e102852671@mcpemails.com.
- bos-key in the body: `40519a301a7f8105a87edf64e65872b7:followup:seq-4-2:2026-10-26T00:00:00+09:00`.
- It was deliberately left unlogged.

**Found by recovery (reads only):**
- Zoya's Sent holds one copy ([Gmail]/Sent Mail:654), with the bos-key in its preview. With no idempotency key, the provider filed no second copy.
- INBOX holds one delivery (INBOX:480).
- No Activity carries that Message-ID.

**So recovery:**
- logs one Email out Activity (notion-edits-26oct.md, item 3, for the CTO);
- completes the action;
- sends nothing.

Without a key there is no provider dedupe, so the Sent check is the only guard. It found the mail.

**Verdict: PASS.**

## Without the marker (Cleanup, 1303cea)

Cleanup's point stands: real mails carry no bos-key. Judged without the marker, recovery reads ACTIONS literally: "a message from us after the action was raised" in Sent and on the thread.
- Zoya's Sent holds four messages to zoya@myunnati.com after the raised time (26 Oct 00:00 JST): provider idempotency 1, crash A (two copies) and crash B.
- Crash A now has its Activity (40519a301a7f81daa9aec3268dac4369), so its Message-ID is logged and it is excluded.
- Provider idempotency 1 is a different test, and its subject says so.
- Crash B is the one unlogged message from us to that recipient after the raise. So recovery finds it by recipient, time and Message-ID, with no marker.

**Verdict without the marker: PASS.** One limit: it works because only one unlogged candidate exists. With two unlogged mails to one person after one raise, recovery would have to judge by content ("does what the action asks"), and that is not tested here.
