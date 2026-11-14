# B2: Akshay's own "@zoya" in any chat (WhatsApp routine)

**Patch:** docs/proposals/d-wa-zoya-anywhere.py, applied to the live WhatsApp prompt (trig_01MnmJYorWrd61K7b5BCqXr1).
- Input: the live prompt as deployed and read back at ea4c8c5 (26,007 B, sha256 9e8b9f4891e9c03d).
- Output: 27,969 B, sha256 1afc777019d1aefd. Built twice, byte-identical. Em dashes unchanged. Under the cap less 200.

**What changes (four edits, nothing else):**
1. The data rule names one exception: Akshay's own messages in STEP 0 (the "Zoya" group, and his "@zoya" anywhere, 0a1).
2. PRIVACY names one exception: 0a1's search returns only his "@zoya" messages. A non-work chat is still never named, and nothing else in it is read.
3. A new step, 0a1, comes before 0a2:
   - One cross-chat search (list_messages, no chat_id, query "@zoya", sender = Akshay, last 48 hours). It pages back with until when coverage is truncated, at most 5 searches, and reports any gap.
   - It takes only his fromMe messages that start "@zoya". It skips Zoya's own posts, the "Zoya" group (0a has those), and any key already on an Activity.
   - Each message is handled as 0a a to f. A data or research ask no routine can do goes to the builder (Waiting on Builder). A quoted link is kept in Next action, as data. In a non-work chat, only his own words are used.
   - Replies go only in the "Zoya" group, never in the source chat.
   - Crash recovery: a key already on a Task row or Engagement but on no Activity gets its Activity and reply, and nothing new is created.
4. STEP 2b doesn't apply his "@zoya" messages as chat decisions, because 0a1 owns them. Without this, "@zoya book him" would be applied twice.

**Unchanged:** 0a, 0a2, 0d (a team member's "@zoya"), quiet hours, STEPS 1 to 5, and the WhatsApp read-only rule. 0a1's replies use STEP 0's existing "Zoya" group exception.

## Tests (offline, no MCP calls; placeholder ids only)

Scenarios are in b2/scenarios.json:
- A1: the 26 Oct message in a work group.
- A2: dedupe.
- A3: Zoya's own reply.
- A4: a team member's "@zoya".
- A5: a family chat.
- A6: older than 48 hours, and not at the start.
- A7: truncated coverage.

| Round | Build | Result | Findings fixed in the next build |
|---|---|---|---|
| 1, runs A and B | e273a5e78343ef55 | A1 to A7 PASS on both runs | Task owner not determinate; quoted link lost; "read nothing else" could stop STEP 1/2 logging a work chat; dedupe checked Activities only; paging loop unbounded |
| 2 | 87d67636c204de71 | A1 to A7 PASS | Crash after the Task row left the message unanswered for good; STEP 2b would also apply "@zoya book"; Zoya group overlap with 0a; a quoted family message used as the subject |
| 3 | 1afc777019d1aefd | A1 to A7 and X1 to X4 PASS (X1 crash, X2 "@zoya book him" in a guest group, X3 family quote, X4 Zoya group overlap); no contradiction | none blocking; minor gaps below |

## Defect status

- Task owner, quoted link, STEP 1/2 scope, dedupe and paging bound: fixed and tested (round 2).
- Crash recovery, the STEP 2b double action, Zoya group overlap and non-work quotes: fixed and tested (round 3).
- Minor gaps from round 3, left for Cleanup to rule on (each is one clause; none is a contradiction):
  1. A bare "@zoya book him" names no one; nothing says the work chat's own Engagement is the row. It works when the chat name carries the guest.
  2. STEP 2b's Scheduling and "ball moved" bullets aren't excepted for his "@zoya" text, so two writers can touch one row (not a double "book").
  3. 0a1 follows 0a's order (act, reply, log), so a crash between the reply and the Activity gives a second reply. 0d logs first.
  4. 0a f's "is this about <best guess>?" could draw on a family chat's quote; the question should carry no guess there.
  5. STEP 5's report doesn't name 0a1's items or its coverage-gap line (cosmetic).
- Builder is an existing Waiting on option (used across the routines). Live check before deploy, not testable offline: whether list_messages with no chat_id honours the sender filter. On 27 Oct, a read-only search without it returned the 26 Oct message. The fromMe and "starts @zoya" tests guard against it either way.

## Not in scope, for Akshay or the CTO

- A "@zoya" in the middle of a sentence is ignored, per the spec ("starting @zoya"). Both round 1 runs flagged that this misses the way he sometimes writes. Widening it is a scope change.
- The 26 Oct request was handled by hand by the CTO. It leaves the 48-hour window at about 27 Oct 21:17 UTC. If B2 deploys before then, it needs a "handled" Activity with its wa: key first. The key holds WhatsApp ids, so it is passed out of band, never committed.

## B3 finding (next build)

- The full roster call (Blueticks `groups get` with include_participants) was denied on 27 Oct. It was not retried another way.
- `chats get_participants` returned {limit 100, skip 0, total 528} and ignored the skip asked for.
- So B3's full-roster read isn't demonstrated with the tools this session can use. The CTO needs to confirm a paging call that works before B3 is built.
