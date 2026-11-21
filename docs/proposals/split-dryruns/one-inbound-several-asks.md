# One inbound answering several asks (replay 5), 26 Oct

Read-only replay on build split26c (FAST 34,091 / c1b292450f738a01, SLOW 63,710 / b34422106ee6f517), 26 Oct 12:20 JST. Nothing sent or written.

Row: Akshat (hypothetical mail). Jheel answers both the price and the production-cost ask in one message.

**Outbound side: PASS.** "One message can complete several actions: one Activity, each action's completion line naming it."

**Inbound side: FAIL.**
- No sentence completes our open asks from an inbound or names the inbound Activity in completion lines.
- STEP 1e's "move each row on" contradicts WRITE PATH.
- Two reply actions raised by one inbound get the same key (`<row>:reply:msg-<id>:<ts>`). They collide if handled separately.
