# r28: completion that counts the work (Codex CX-20261113T0800 items 2 and 3)

Main, 13 Nov, for the CTO's 08:55 ask. Built on r27 (accepted at 193549d, pin 582ad08, not yet deployed) and the live sweep (r24, 2203cc3f, also the day chat's copy). Not deployed, the pin ref isn't moved, nothing written to Notion.

## Item 2: SLOW can't say Completed with required work left

The 00:11 run said Completed with the feedback and bounce categories unfinished and Sent reconciliation skipped. Its python counted selected keys only.

- **Category lines count the work** (SLOW BATCH 3/): "category <name>: selected <n>, done <n>, remaining <n> (<why any remain>) | not due". This replaces "checked <n> | ... | unfinished <why>", for the same list of categories.
- **SENT RECONCILIATION is now a named category,** since Codex's term had no step behind it. Every Message-ID in Zoya's Sent and ad@'s Sent since the run's start is matched to a completed line and its Activity, and each completed line's Message-ID must be found there. A miss is reported, never fixed by a resend.
- **The status** (4/): Completed now also needs the required categories (STEP 0b feedback, STEP 0c bounces, SENT RECONCILIATION) each to have a line with remaining 0 or not due. One missing or short makes it at best Partial, named with its counts. Failed for an unexplained unfinished key is unchanged.

The SLOW file grows by 419 bytes. The SLOW task changes only by its pin. The hourly and episodes are unchanged.

**What it can't prove:** the note checks still rest on what the run reports. r27 already makes a SQL read fail its chk: line, and the python can only check what's in the record. Codex's "preserved notes agree" is something the audit corroborates, not this build.

## Item 3: sweep Part B

The 12 Nov run said "Failed: early exit: 3i, 3p, 3h, 3g, 3k, 3b, 3d, 4, 7b" after about 2 minutes. 3h had been skipped for the third time, and billing only searched "invoice".

- **Per-phase counts:** each step line in STEP 7 is "step <name>: selected <n>, done <n>, remaining <n> | unfinished (...)". STATUS IN CODE gives Completed only when each step is done and its remaining is 0. Anything else stays Partial (a measured minute 40, a cap or a tool error) or Failed, as before.
- **Saved skipped phases first:** every step the previous run of the same part left unfinished, without a line, or with remaining above 0 runs first, in the part's order, but STEP 3h before the rest. Before, it said only "a step it skipped runs first".
- **Billing search:** one search per term in subject or body (invoice, bill, payment, receipt, GST, remittance), merged by Message-ID, then judged by the existing forward and never-forward rules. Transaction alerts stay excluded by those rules, so the wider search doesn't widen what's forwarded.
- **3h's source:**
  - It read the OS Audit page (3fc19a301a7f8171b1e2ef19ded7c239), its "Independent review, latest checkpoint" section. That's the historical trail now.
  - It now reads the CTO Audit page's "Latest checkpoint" (40419a301a7f81c48c29d894e433750d, decision 516).
  - Each item's id is "<checkpoint id> item <n>" (CX-<date>T<time>, else its old AR- id).
  - **No duplicates:** an item is skipped when a CTOA card on the Build board already carries that checkpoint id in its body (the CTO answers Codex there), or an Engagement has the id in its Name or Source ID. In practice 3h will create a Task row only for something the CTO hasn't taken onto a card.

**The sweep is 51,107 / e9f29ebc3144640b** (live 50,569 / 2203cc3f). Its one em dash went with the old section name.

## Builds

Each was built twice, byte-identical. The Zoya builds were rebuilt from a fresh worktree at f70901f with r28/zoya/build_one.patch, and the SLOW file matches the pin commit. No em dash.

| Routine | Base | Build | Bytes / sha256 |
|---|---|---|---|
| Zoya SLOW file | r27 582ad08 (ce4d0b3f) | routines/zoya/release/zoya-slow-work.txt at **6b306d4** | 95,464 / a9c6ca42092bff97 |
| Zoya SLOW task | r27 856318d3 | r28/zoya/zoya-slow.txt (pin 6b306d4) | 15,652 / 274f3f2c8bf4b795 |
| Zoya hourly | r27 | unchanged | 62,992 / 839117217edc49ed |
| Zoya episodes (not live) | r27 | unchanged | 50,152 / 2a0c1bffce85c8c9 |
| Daily sweep | live r24 2203cc3f | r28/sweep.txt | 51,107 / e9f29ebc3144640b |

**How to build:**
- Zoya: apply r28/zoya/build_one.patch at f70901f, then run `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 6b306d43c18f1265449a30e2c9bca4077fa84f5d`.
- Sweep: `python3 docs/proposals/r28/patch.py sweep docs/proposals/r24/sweep.txt <out>`.

**Deploy (CTO, after r27 and the day-chat verdict):** pin 6b306d4 with the SLOW task (the hourly as r27), and the sweep. The day chat's copies are docs/proposals/zoya-day/prompts/zoya-slow.txt and daily-sweep.txt.
