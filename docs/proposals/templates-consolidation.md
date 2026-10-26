# Templates consolidation: one source per outgoing message

Prepared by Main 2 for the CTO, 26 Oct 2026, at Akshay's request. Read-only: nothing was written to Notion, no prompt was changed, no mail was sent. The CTO decides.

**Akshay's preferred target.** Each outgoing message has one existing Templates database record. That record holds the wording and the sending controls: who sends, when, To and Cc, mode and approval. Rules for Zoya and the "Mail and WhatsApp wording" page link to the record instead of keeping their own copy.

**Evidence.** The full inventories are in `docs/proposals/templates-consolidation/`:
- `templates-vs-wording.md`: all 55 Templates rows against all 73 wording toggles.
- `rules-decisions.md`: Rules for Zoya, Client show mails, the other wording pages and both decision ledgers.
- `routines.md`: what every routine prompt reads and what it carries itself.

This file is the summary and the plan.

## 1. Where things stand

**Wording lives in five places today, and controls in seven.**

| Source | Holds | Read by a live routine? |
|---|---|---|
| Templates database (collection b2976a03, 55 rows) | Wording plus Mode, Approved, Sender, Owner routine, Trigger, Subject | **No.** Inbox, calendar and sweep each say "The Templates database is retired: never read it." |
| Mail and WhatsApp wording page (3fa19a30...81b6, 73 toggles) | Wording plus From, When and Status per toggle | Yes: inbox 6c, calendar 1b, 3b and 4c, Zoya (all one-off mails), Mac transcripts 7g |
| Client show mails (3fc19a30...8175, subpage of the wording page) | Three pitch sheets (B2S, un#, HBD), templates C1 to C19, show check | Yes: Zoya, calendar 4d, sweep 3d |
| Rules for Zoya and its subpages | Who sends what, Cc, voice and limits, plus wording of its own: routine pages 1 to 8 (follow-up chains), Mock follow-ups, transcript request, internal asks, nurture 5a | Yes: Zoya every run, inbox in parts |
| Routine prompts | About 25 literal messages, including loop-ins, holding reply, vendor redirect, Saurabh thanks, owner mail, scorecard, team WhatsApp, group posts and the un# price | They are the prompts |
| Controls-only pages | Cadences (caps, windows), Calendar rules, Inbox and Your call rules, Episode asset filing, Links and limits (stale), CLAUDE.md link list | Yes, several claim "this page wins" |
| Engagement page bodies | "## Decision mail" and "## Next sponsored mail" snapshots | Yes: Zoya sends from them |

**The Templates database has fallen behind.** Compared with the wording page:
- **Wording:**
  - 20 rows are identical.
  - 16 differ in small ways, mostly the sign-off: Mamatha or Akshay against "best, / Zoya ✨".
  - 19 differ in substance.
- **Live controls:**
  - 10 rows are on Mode Send and 5 on Draft.
  - 7 of the Send rows still name Akshay or Mamatha as sender where the page says Zoya. Four of those carry a link, which only Zoya may send.
  - Tier 1, 1.5 and 2 are still Draft rows, though the page retired them on 16 Oct (decision 235).
- **Stale content:**
  - "Sponsored commercials (FT)" still signs "Stay awesome ✨" (decision 206, replaced by 345).
  - "Show credentials" still names Ashneer Grover.
  - "Form received" says 8 to 10 weeks, where the page says 10 to 12.
  - "Reschedule from our side" still gives a reason (against decision 208).
- **Missing rows:** 17 approved messages exist only on the wording page. Among them are the holding reply, no-show note, price negotiation, sponsored yes, both payment mails, repeat-guest sponsored, double-booking check and the three team WhatsApps. C1 to C19, the routine-page chains and the prompt literals have no row either.

**These clashes are harmless today, and only because nothing reads the database.** Pointing a routine at the database before its content is fixed would send the wrong sender, wrong wording and links from Akshay's account.

## 2. Inventory, by group

The full per-message tables are in the evidence files. Here is the grouping the migration follows.

| Group | Messages | Wording lives now | Controls live now | Copies differ? |
|---|---|---|---|---|
| A. Templates row and wording toggle | 55 (of which 23 retired on the page) | Both; the page is the one routines read | Toggle From/When/Status; row Mode/Sender/Trigger (unread) | 35 of 55 differ (16 minor, 19 material) |
| B. Wording toggle only | 17 (section 0 lines, sponsored and payment, double booking, video ask, team WhatsApp) | Page | Page plus Rules for Zoya | n/a |
| C. Client show templates | C1 to C19, plus 3 pitch sheets (facts, not messages) | Client show mails | Page header, Rules for Zoya, decisions 305, 306, 313 and 323 | Uses "Stay awesome" (against 345); C13 attaches the transcript; HBD sheet says "outreach on" |
| D. Follow-up chains | Routines 1 to 8, nurture 5a, revival 8 | Routine pages under Rules for Zoya; Mock follow-ups claims to be "the approved source" | Routine pages, Cadences, Zoya prompt | Mock page and routine pages differ; both use idioms banned by decision 392 |
| E. Internal mails | Transcript request to Ranjita, internal team asks | Rules for Zoya trailing blocks (376, 377) | Same plus the Zoya prompt | n/a |
| F. Literals in prompts | Loop-in (3 variants, in inbox and Zoya), Saurabh thanks, vendor one-liner, holding reply, "looping in Akshay", release mail 2 opener, un# price, edit-notes phrase, Jaya forward (sweep), Mac subject and sign-off, team WhatsApp frame, contact card to Akshay | Prompt text | Prompt text | The vendor redirect differs between inbox 6b and the wording toggle |
| G. Reports to Akshay and the team | Owner mail, Monday scorecard, feedback replies, Zoya group posts, "@zoya" replies, invite set (WhatsApp 3c) | Prompt text, FT community invite kit | Prompt text | n/a |
| H. Snapshots on rows | "## Decision mail", "## Next sponsored mail" | Engagement page body (filled from A or D) | Zoya prompt | By design, per row |

## 3. Decisions that govern the source, and the conflicts

Two decisions are the ones that matter here:
- **Decision 194 (in force):** Rules for Zoya is the single source of truth, and its wording subpage replaces the Templates database (decision 98) "at go-live".
- **Rules for Zoya section 8:** the Templates database "is deleted at go-live".

Akshay's target reverses that direction, so it needs a new decision that supersedes 194 and section 8. Codex reached the same recommendation independently on 25 Oct (CTOA-20261025-03: Templates as the canonical record, the wording page as an index), marked "for owner decision".

These conflicts are flagged here, not resolved:

1. **98 vs 194 and 207: is Templates retired?**
   - 207, the go-live itself, says "Templates database stays for now".
   - No decision records the retirement.
   - Rules for Zoya section 10 says it's "Still open" (step 5 not done).
   - The roadmap says it was retired on 23 Oct.
   - The repo prompts say "retired: never read it".
   - CLAUDE.md says the inbox and calendar still read it.
2. **102 vs 238 and 313: where approval sits.**
   - Decision 102 (in force) puts send permission in the Templates Mode field ("only Akshay moves a row to Send").
   - Decision 238 puts approval on the wording page (the test mail, then "marked Approved"), which has no Mode field.
   - Decision 313 overrides Mode for client shows.
3. **194 vs Calendar rules and Inbox and Your call rules.** Each of those pages says it wins over its prompt, and each carries mail rules outside Rules for Zoya.
4. **235 vs 333 vs 379: who sends the close notes and acknowledgements.** Rules for Zoya section 1 disagrees with its own 379 block on the same page. Two Send rows in Templates still name Akshay.
5. **184 vs 235: which connector sends Akshay's mail.** 184 says MCP Emails; 235 says Gmail. calendar.md still says MCP Emails.
6. **305 vs 345: the sign-off.** Client show mails and one Templates row still use "Stay awesome ✨".
7. **300 vs 412: the transcript on the FT thank-you.** Four writers draft this mail with different controls (calendar 4c, Mac 7g, zoya.md INTERNAL c(4), the split's internal.txt). Only the split follows 412.
8. **159 vs 395: where figures come from.** 159 says the sales page is the source of truth for numbers; 395 says rounded figures from saved wording win.
9. **357 vs practice: which decision ledger is real.**
   - Notion's Decisions database stops at 381 on 21 Oct.
   - The repo's decisions.md runs to 414 and lacks 357 to 372.
   - Rules for Zoya cites numbers from both ranges.
   - So neither ledger alone governs, and the new decision has nowhere clean to be recorded.
10. **Mock follow-ups vs routine pages 1 to 3, and Cadences vs Links and limits.** Each claims to be the master copy, and they differ.

## 4. Consumers: who reads what, and what they would read after

| Routine (prompt size, headroom to 65,536) | Reads today | After the move |
|---|---|---|
| Inbox (61,957 B, 3,579) | Wording page: decision-mail toggles and Show credentials (6c). Inbox and Your call rules, Cadences, Client show mails. Own literals: loop-in, Saurabh, vendor, contact card. | Templates rows by name for the 6c fills and its own one-liners. Controls rows for loop-in and vendor. Cross-message rules stay on Cadences and Rules for Zoya. |
| Calendar (54,901 B, 10,635) | Wording page: day-before, double booking, FT thank-you (1b, 3b, 4c). Client show mails C12 and C13 (4d). Calendar rules. | Templates rows. C12 and C13 become rows. Calendar rules keep behaviour only. |
| Daily sweep (33,824 B, 31,712) | Client show mails pre-release (3d). Literal Jaya forward (6c). | Templates rows. |
| Zoya (65,210 B, 326) | Rules for Zoya, the wording page, Client show mails C1 to C19, routine pages 1 to 8, Cadences, sales page, page-body snapshots. About 15 literals. | Templates rows for every message, including chain steps. Rules for Zoya, routine pages and Cadences keep rules and timing only. Snapshots stay as fills. |
| WhatsApp (26,007 B, 39,529) | Literals for group posts and "@zoya" replies; the invite kit page | Group posts and invite-set rows if group G is in scope (see question 5). |
| Mac transcripts (20,669 B) | Wording page FT thank-you (7g), plus its own subject and sign-off literals | Templates row "FT thank-you after recording". |
| Zoya split, not accepted (FAST 38,248 B; SLOW 65,312 B) | Parts copy the same sources, plus decision 412's thank-you | Rebuilt on rows, if the split lands. |

Host boards, community directory, Zencastr links, tasks, feedback call and cowork evals send no messages and are not consumers.

**Prompt bytes.** Reading a row by name costs about what reading a toggle by name costs. The saving comes from moving literals and per-message control prose out of the prompts: roughly 3 KB on the inbox, 4 KB on the calendar and several KB on Zoya. Zoya has 326 B of headroom today, so she should move last, or ride the split if that lands.

## 5. Proposed target record

The record is one Templates row per message. Existing fields stay: Name, Purpose, Show, Mode, Approved, Sender, Subject, Trigger, Owner routine, Notes, Version, and the body as wording. Proposed additions, kept to the fields a routine actually needs to decide:

| Field | Type | Why |
|---|---|---|
| Status | Select: Live, Test sent, Retired | Replaces the toggle's Status line. A retired row stays as history (decision 384: no deletion without Akshay's yes). |
| From | Select: Zoya (MCP), Akshay (Gmail, link-free), Akshay (draft he sends), Chaandini, team WhatsApp | Encodes 235, 313 and 333 per message, instead of in prose |
| To / Cc | Text | "Whose move it is" rules and message-specific Cc. House copies stay a shared rule on Rules for Zoya. |
| Channel | Select: Mail, WhatsApp | Group D, E and team WhatsApp rows |
| Decisions | Text | The governing decision numbers, which the toggles carry today |
| Read by | Multi-select of routine and step | Shows every consumer, so nothing gets retired while still read |
| Chain / Step | Text and number | For follow-up chains (group D) |

Mode keeps decision 102's meaning (Off, Draft, Send; only Akshay sets Send). Approved records decision 238's test-mail approval. Cross-message controls stay where they are: caps, quiet hours, intervals and the link list on Cadences and Rules for Zoya; show facts on the pitch sheets (decision 306). The rows link to those pages.

Under this model:
- Rules for Zoya keeps rules, and its section 8 becomes a link to the database.
- The wording page becomes an index: a linked view of Templates grouped by stage.
- Client show mails keeps the three pitch sheets as fact pages, and its C1 to C19 move to rows.

## 6. Migration order

Nothing is retired until every consumer is moved and verified.

0. **Decide (CTO, then Akshay).**
   - Record the target as a decision that supersedes 194 and Rules for Zoya section 8.
   - Settle which ledger records it (conflict 9).
   - Answer the open questions in section 7.
1. **Schema.** Add the section 5 fields to Templates, and set every existing row to Status Retired or Live to match the wording page. No consumer changes.
2. **Content, one source at a time, page-wins.** Use the live wording, because that's what Akshay approved and what goes out today.
   - Rewrite the 35 rows that differ, and fix Sender, Mode and Trigger on the 15 active rows. The 7 Send rows with the wrong sender go to From Zoya or to Off.
   - Create rows for group B (17), group C (C1 to C19), group D (chain steps), group E, and the external literals in group F.
   - Akshay sees one list of the rows whose live wording changes. He doesn't approve each row: the wording itself is already approved.
   - Write as one .md upload for Notion AI, since this is well over 10 rows.
3. **Verify the content before any reader moves.** Script a comparison of every Live row body against its toggle or source text: it should show zero material differences. Fix the conflicts the CTO decides first (2 approval, 4 senders, 6 sign-off, 7 thank-you).
4. **Move consumers one at a time, lowest risk first.** Each move is a prompt change built on the live base, reviewed by Cleanup, read back after deploy, and checked with one "[Zoya test]" send or draft per changed message.
   1. Daily sweep.
   2. Mac transcripts.
   3. Calendar.
   4. Inbox.
   5. WhatsApp, if in scope.
   6. Zoya, last, or inside the split.
   During each step the old source stays in place and unchanged.
5. **Repoint the documents.**
   - Rules for Zoya section 8 and 10: link the database.
   - Wording page: becomes a linked view, with each toggle replaced by a link to its row.
   - Client show mails: keeps its sheets; C1 to C19 become links.
   - Mock follow-ups: retired.
   - CLAUDE.md "Zoya" and "Sending mail" lines updated.
   - Home page card for Templates and the developer page change log updated.
6. **Retire the duplicates.** Once every Read-by consumer is verified on rows for a full week, empty the old toggles and copies. Deletion of any page needs Akshay's yes per deletion (decision 384).

**Rollback at any step.** The previous prompt is restored, and the old source is still there.

## 7. Open questions for the CTO

1. **The new decision.** Does Akshay's target supersede 194 and Rules for Zoya section 8 outright? Where is it recorded, given the split ledgers (conflict 9)?
2. **Winner rule.** In step 2, does the live source win every material difference? Or should Akshay see the 19 material pairs first? Proposed: the live source wins, and Akshay gets one list of what changes.
3. **Follow-up chains (group D).** One row per mail in a chain? Proposed: yes, with Chain/Step fields. The routine pages then keep only who, when and stop rules.
4. **Pitch sheets.** Are they facts (they stay as pages under the show check) or messages? Proposed: facts, linked from each client-show row.
5. **Scope of "outgoing message".** Are internal reports to Akshay and the team in scope (group G: owner mail, scorecard, group posts, "@zoya" replies)? Proposed: external mail and WhatsApp in scope (groups A to F); group G stays in prompts for now.
6. **Approval model.** Keep both Mode (102, only Akshay sets Send) and Approved by test mail (238) on the row? Is decision 313's "draft he sends by hand whatever the Mode" encoded as From = "Akshay (draft he sends)"?
7. **Read mechanics.** Should routines query rows by name each run, or by Show and Purpose? Zoya may need about 30 rows a run. Is one query of Live rows, filtered by Read by, acceptable on time and connector limits?
8. **Prices in prompts.** Do these move to rows or to a single commercial page: un# USD 1,500 (Zoya), the paid-article rates (inbox STEP 4) and the INR 30,000 + GST floor (inbox, sweep, Zoya)?
9. **FT thank-you.** The four writers and the 300 vs 412 conflict need fixing whatever the source. Should that land before step 4 or ride it?
10. **Already-stale pages.** Links and limits, Rules for your inbox, the "Stay awesome" sign-off on Client show mails, and the HBD "outreach on" line: fix now as plain data fixes, or leave until step 5?

## 8. Noted while reading (not acted on)

- **Out-of-date files and pages:**
  - CLAUDE.md says the inbox and calendar read the Templates database. They don't.
  - routines/inbox.md and daily-sweep.md still cite decision 135 (links as unlinked text), which 184 replaced.
  - calendar.md says Akshay's mail goes through MCP Emails.
  - The sweep says "lines joined with <br>", against CLAUDE.md.
- **Inconsistent link lists:** four approved-link lists in the prompts differ. Some links on the pitch sheets (unhashed.co/studio and three YouTube handles) are not on the CLAUDE.md list.
- **Templates row edited today:** I edited "FT thank-you after recording" earlier today on Akshay's instruction. It now matches the wording page, but its Mode (Send) and Trigger (Drive audio) are stale. No routine reads the row.
- **Timing mismatches:** the calendar's header says hourly, but its prompt says six runs a day. The sweep's header says one run; its prompt has two parts.
