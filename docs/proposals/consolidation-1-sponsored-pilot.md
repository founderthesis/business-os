# Consolidation 1: sponsored obligations as Task rows, canonical send identity

Status: proposal, 20 Oct 2026. Nothing here is built or deployed. It starts after AR-20261020-1 rev 2 is deployed and observed. It is not part of that package.

The architecture audit is the prompt for this. Its claims are being checked against source evidence separately, and this proposal relies only on what is verified.

## Problem, in one line

One Engagement row carries several independently dated obligations in one Next action string and one Next date. So a follow-up deferral can move a recording date, an eval rewrite can drop another ask, and two writers can race on one field.

## Pilot scope

- **Sponsored only**, on Founder Thesis and un#:
  - Engagements at Status Sponsored offered;
  - Engagements at Booking or later with Payment set and not Settled.
- **First wave:** at most 10 Engagements, chosen to cover the hard cases:
  - one with a booked recording and an open payment step;
  - one with an eval re-run due;
  - one with a PR shared with another row;
  - one snoozed ask;
  - one recent send.
- **Expansion:** precall and booking chases only after the pilot passes its three proofs on real runs.

## Model (existing schema, no new fields)

Each independently dated obligation becomes one Engagements row with Kind Task:

| Field | Value |
|---|---|
| Name | "<obligation>: <guest> @ <company>", e.g. "Sponsored chase: Teja Gudena @ Netradyne" |
| Kind | Task |
| For engagement | the guest's Engagement |
| Show | same as the Engagement |
| Waiting on | the obligation's owner only |
| Next action | the step, e.g. "Zoya: sponsored step 2 (soft bump)" |
| Next date | this obligation's own date |
| Chase step | this obligation's step |
| Task state | Handed over / Doing / Awaiting someone else / On hold / Done |
| Source ID | "obl:<type>:<engagement page id>", one open row per type per Engagement |
| Claude note | holds and sends for this obligation only |
| Page body | the obligation's planned mail, e.g. "## Next sponsored mail", moved from the Engagement |

**Pilot types:**
- sponsored chase;
- sponsored yes next steps (billing details, precall);
- payment reminder 1 and 2;
- Jaya confirmation.

The Engagement keeps the guest-level facts:
- Status;
- Tier, Payment and Amount;
- eval fields and the eval body section;
- the booked call in Next date, Call type and Call link (calendar-owned);
- Scheduling;
- a decision ask for Akshay, if any.

**No schema addition is needed.** Name prefix plus Source ID prefix give a filterable type. A "Obligation type" select would make views cleaner. It earns its place only if the pilot views prove hard to read, and it would be proposed separately.

## Write ownership (pilot rows)

| Field or row | Only writer | Others |
|---|---|---|
| Task row (sponsored chase, payment) | Zoya | Sweep may flag in Claude note; inbox may add an inbound Activity link |
| Engagement Status | Inbox (from mail) and Zoya (after her own send's outcome) | none |
| Engagement Next date, Call type, Call link | Calendar (booked calls) | Zoya never writes them for pilot rows |
| Eval verdict, Eval link, Eval date, "## Eval" body | Evals | Never touches Task rows or Next action |
| Your call | Akshay; inbox clears it | |
| Activities (sends) | The sender | Others only append a provider mapping to the canonical record |

## The three proofs (acceptance, on real runs)

1. **A follow-up deferral can't change a recording date.**
   - Setup: a pilot Engagement with a booked recording (Next date = recording, Call type Recording) and a payment Task row held by the 7-day rule.
   - Check: snapshot the Engagement's Next date, Call type and Call link before and after two Zoya runs. They are byte-identical, and only the Task row's Next date and Claude note changed.
2. **An eval can't erase another obligation.**
   - Setup: tick Rerun eval on a pilot Engagement with an open sponsored chase Task.
   - Check: after the evals run, the Task row (Next action, Next date, body, Task state) is unchanged and still linked, and the Engagement's non-eval fields are unchanged.
3. **A retry can't duplicate a send.**
   - Replay: Zoya sends, then the Activity write fails, as in AR-20261019-1's AFTER SEND case.
   - Check: the next run finds the message in Sent by its canonical identity (below), writes exactly one Activity, sends nothing, and advances the Task row once.

**Migration preserves every open obligation.**
- Before writing anything, export each pilot Engagement's Next action segments, Next date, Waiting on and body sections.
- After migration, every segment is either still on the Engagement (guest-level) or on exactly one open Task row, with its own date and owner.
- The script prints before/after counts per Engagement. A mismatch stops the migration for that row.
- Rollback is the export: Task rows are closed with Task state Done ("rolled back"), never deleted.

## Canonical send identity

- **Canonical key:** the delivered message's RFC 5322 Message-ID header.
  - Activities.Source ID = "rfc:<Message-ID>".
  - The page body carries "provider: gmail <id> | mcpemails <inbox uid>; idempotency: <key>".
  - Still to verify before build: that both connectors return the header (Gmail get_message, MCP Emails email_read). Where one doesn't, the provider id stays the key, and the first reader that sees the header upgrades the record in place.
- **One record per message.** Zoya's mail Cc's Akshay, so the same message shows up in ad@thepodium.in too. The inbox doesn't skip Zoya mail wholesale, which would lose evidence when Zoya's own log failed. Instead:
  - It looks up the Message-ID.
  - Found: it appends its provider id to that record.
  - Missing: it creates the canonical record itself, marked "logged by inbox (sender's log missing)".
- **Counting.** Sends are counted from Kind Email out records deduplicated by Message-ID: the daily cap, the 7-day rule and the run report. Never from Summary wording ("Zoya sent ..."). Loop-ins and incidental Cc are excluded by classification (decision 346), not by summary text.
- **Before any send or retry:** look up the idempotency key and the thread's Sent copy, as today, then the Message-ID once known. A found send is reconciled, never resent.
- **Legacy records** keyed by a provider id are upgraded in place when first touched, never duplicated.

## Safety rules carried over (from the 20 Oct direction)

- An empty Next date never authorises contact. A Task row needs an owner, a step and a date to be due.
- A decline closes only its evidenced scope. A declined sponsored chase doesn't close a payment, production or other-show obligation.
- No explicit decline is revived, no guest authority broadened and no commercial term changed by this migration.
- A missing run report means unconfirmed, not failed.

## Out of scope here (separate proposal)

The following is consolidation 2, written separately. It must preserve today's approved senders, approvals and handoffs exactly:
- inbox capture-only (the inbox records and routes, the owner routines act);
- one authority per rule (one Controls page per rule set, prompts point to it).

## Order

1. AR-20261020-1 rev 2: cleanup accepts, Main deploys, the observation checks confirm.
2. Verify the Message-ID availability on both connectors (read-only).
3. Pilot build (Zoya routine 1 and STEP 1b selectors read Task rows for pilot Engagements only; evals and calendar get the ownership lines), cleanup review, migration of up to 10 Engagements with the before/after check.
4. Observe the three proofs on real runs, then propose precall/booking.
