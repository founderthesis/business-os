# Retries (replay 4, controlled failure), 26 Oct

Read-only replay on build split26c (FAST 34,091 / c1b292450f738a01, SLOW 63,710 / b34422106ee6f517), 26 Oct 12:20 JST. Nothing sent or written.

Row: Subodh Bhardwaj @ Navaratna Concepts (3fa19a301a7f8118a06aea18fea5d7f9). The send is real: sponsored step 1 went at 08:44 JST, Message-ID eb338e74... The run dying before the Activity is written is hypothetical.

Key: `3fa19a301a7f8118a06aea18fea5d7f9:followup:seq-1-1:2026-10-25T00:00:00+09:00`

What the next SLOW run does:
1. AFTER SEND's reconcile finds the mail in Sent: two copies, one Message-ID.
2. It logs one Activity (Source ID msgid:eb338e74...).
3. Chase step 1, segment "step 2 on 2 Nov", Next date 2 Nov.
4. No re-send, and the key is unchanged.

Timeout case: the action stays pending and is retried with the same key after the thread check.

**Verdict: PASS on logic. Blocked until the "Action key" property exists on Activities** (added at deploy).

Gaps:
1. A send recovered by the thread check has no receipt, so the rule doesn't say whether its Activity gets the Action key.
2. Threading sends through draft send, but the idempotency key is only named for email_compose.
3. Nothing says that two Sent copies with one Message-ID are one send.
