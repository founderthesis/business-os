# Self-addressed test sends, consolidated (CTO order 20:31 JST, step 3)

Build: FAST 96c11beae7ec325b, SLOW a5b4ef40cfd85bb1 (frozen, 8e64140).

**Exact count: 1 send, 1 approval prompt (MCP Emails email_compose).** It goes from Zoya's inbox to zoya@myunnati.com only.

| # | Test | Sends | Prompts | Why |
|---|---|---|---|---|
| 1 | Crash A recovery, re-run on the frozen build | 0 | 0 | The 19:20 mail exists. Recovery is reads plus one Activity write (crash-a-recovery.md, PASS; the write is with the CTO) |
| 2 | Crash B, outside the 24-hour dedupe window, simulated with dedupe disabled | 1 | 1 | email_compose with no idempotency_key. A distinct action key goes in the body as "bos-key". The send is left unlogged. Recovery must find it by Message-ID and bos-key in Sent and plan one Activity, never a resend |
| 3 | Anything else | 0 | 0 | Provider duplicate-send already passed (provider-idempotency.md). Lock tests and frozen round 3 are offline. Decision 412's thank-you is a draft, never sent |

Crash B's action key is `40519a301a7f8105a87edf64e65872b7:followup:seq-4-2:2026-10-26T00:00:00+09:00`, distinct from crash A's seq-4-1.

The subject is "[split launch test] crash window B".

The body says it is a self-addressed test, gives the bos-key line, and says recovery must log it and never resend it.
