# Cleanup verdict: r22 at b8f7187 (changes since 3b7a35c), and paas-move plan 5d5f02cd

Cleanup session, 7 Nov 2026, about 18:30 JST. Read-only. Nothing deployed.

## Verdict: accepted, and the PaaS move is unblocked once these builds are live

### Builds (each reproduced twice, byte-identical, equal to the commit)

| Routine | Bytes / sha256 |
|---|---|
| Calendar sync | 62,814 / 0e755649ab95d9ba |
| Inbox capture | 49,694 / a4ac5ae216da6103 |
| Inbox actions (with section 6) | 48,017 / c17734c21ca88163 |
| WhatsApp | 32,054 / eb41ecdd81c92edb |
| Zoya hourly (unchanged) | 62,955 / f366f769a799e92d |
| Zoya SLOW task (pin 8faf930) | 15,813 / d2253a1923da5de1 |
| Zoya SLOW file at 8faf930 | 91,394 / d8ffcafefbb11e7c (91,390 characters, which the task states) |
| Daily sweep (last) | 49,579 / 51412bd9ce7385df |
| Zoya episodes (not live) | 50,171 / aaf08db2321ca288 |

No em dash was added; the sweep's one is in the live base.

### 1958305: my C1 and C2 are in

Building with that commit's patch.py reproduces exactly WhatsApp 30,378 / f93f47f9 and sweep 46,569 / 513e1a2a, the hashes I accepted. Later commits build on top of them.

### f27ba62: PaaS guard, 514, 499, paas-move C2 and C3

- **The guard:** both lines, word for word as I proposed, in calendar, sweep, actions, capture and WhatsApp, on the shared exemption line. Zoya already had its own. Nothing else changed in calendar, actions or capture.
- **514 (Zoya SLOW):** Sarika or Akshay confirming a release date counts. A missing date becomes "Sarika: release date for <guest>'s release mail" with Sarika in Waiting on, never Akshay's list. Anything else missing still goes to him. The decision 427 hold is unchanged.
- **499 (Zoya SLOW INTERNAL TASKS):** post-production work lives in Team tasks and is never an Engagements Task row.

### b8f7187: sweep and WhatsApp stop skipping steps

**The two time limits fit their schedules:**
- **Sweep, 40 minutes:** it runs at 13:10 (Part A) and 15:10 (Part B) JST, so a part ends by 13:50 or 15:50 at the latest and never meets the other.
- **WhatsApp, 25 minutes:** it runs hourly at :45, so it ends by :10, well before the next run.

Both limits need a measured `date -u` stop line, which the status python checks against the start time. Steps left at the limit run first next time.

**Status in code (both):**
- One line per step, and python prints the status.
- Completed needs every step done. Partial is allowed only for the time limit, a cap the prompt sets, or a tool error with its text.
- Anything else, or a missing step line, is Failed "early exit: <step>".
- "Counting rows without handling them is not done." This closes the 6 Nov Sweep B pattern (STEP 4 skipped, 3g and 3k counted only) and the 7 Nov WhatsApp "ran out of effort".

**Sweep STEP 4:** the three Gmail checks read at most 40 rows a run: the carry-over first, then the oldest Last activity. The rest goes on a "step 4 carry-over:" line, and the step is Partial (cap). Field-only checks run on every row. A large backlog shows as Partial with a stated cap, which the morning check accepts as a reason.

**Smaller changes:**
- **3h b** reads the Live line from the page body, with no new field, and reports a row that has none.
- **3a2 Mamatha** moves rows, at most 30 a run: routine steps to Zoya, decisions to Akshay.
- **WhatsApp 3d and 4** run every run. STEP 3 stays due until a run reports "step 3: done". Its kit send is still guarded by "Member count at last send", so a repeat run doesn't resend.

### paas-move (plan 5d5f02cd0d57931a, placeholder Show id): C1 to C3 met

- **C1:** the guard is in all five non-Zoya builds above, plus Zoya. Live once this round is deployed.
- **C2:**
  - Each op carries "activities_relink": snapshot every listed Activity's Engagement relation to data/paas/activities-before.json, write back old plus new, read back.
  - verify takes the snapshot as its third argument and fails on "OLD LINK LOST" or "ACTIVITY NOT READ BACK".
- **C3:**
  - Every open row's step has its owner in front, and the longest is 118 characters.
  - The stale "untouched 14+ days" flags are dropped in favour of their "was:" step.
  - Parked and Unresponsive rows have Waiting on empty and a "Closed: ..." line. One Parked row has no Deal step at all and gets an empty Next action, which is fine for a closed row.
  - The full Deal text stays in the Claude note and page body.

**Run notes for the CTO** (not blocking):
1. Deploy this round first, and read back the five guard routines live. Then create the Show "PaaS".
2. Re-run `plan` with the real Show id **and today's date**. The committed plan says Captured 2026-11-06.
3. Take the snapshot before the first write.
4. Run `verify plan.json readback.json data/paas/activities-before.json`. verify only checks old links when given the snapshot, so pass the third argument.
5. Reconcile: 33 Engagements on Show PaaS, and 33 Deals whose Next action starts "Moved to Engagements".

## Deploy order

1. calendar 0e755649
2. capture a4ac5ae2
3. actions c17734c2, with section 6
4. WhatsApp eb41ecdd
5. Zoya: pin 8faf930, then hourly f366f769 and SLOW task d2253a19
6. sweep 51412bd9
7. the PaaS move

Read each prompt back byte for byte.
