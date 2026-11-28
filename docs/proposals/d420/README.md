# Decision 420: ad@thepodium.in through MCP Emails; agents send only the loop-in

Decision 420 (Akshay, 28 Oct; CLAUDE.md "Sending mail"):
- **Reading:** every routine reads ad@thepodium.in through MCP Emails (inbox cd37e47e-89d8-4259-b907-9a243baf7048, IMAP), never the Gmail connector.
- **Sending:** the only mail agents send from ad@ is the "adding @Zoya" loop-in, also through MCP Emails.
- **Everything else** from ad@ is Akshay's own. Zoya sends what she can from her inbox; the rest goes on his list.
- **Drafts** for Akshay stay allowed.

**Order:** the inbox first, as its own deploy (it's down), then the rest as one batch.

## Coverage: every Gmail read and every ad@ send, by routine

Found by grepping each live prompt on 28 Oct: the calendar, sweep, WhatsApp, evals and dossiers prompts, Zoya's FAST prompt (zoya-one) and the pinned SLOW file.

| Routine | Gmail reads now | Mail from ad@ now | Change under 420 | Build |
|---|---|---|---|---|
| **Inbox** | STEP 1 search plus `get_thread` on every thread, RAW reads, CONTEXT CHECK and Stakeholders chain reads, forwards | STEP 6 loop-in (Gmail); 6a "Thanks for sharing, SG" to Saurabh; 6a/6b vendor one-liner with podm.in/pitch-to-us; STEP 5 `delete_draft`; STEP 7 `unlabel_thread` | Every read through MCP Emails, with a MAILBOX map for each Gmail tool and a THREAD recipe. The loop-in is the only send. Saurabh gets nothing. A vendor gets the loop-in, and Zoya asks for the form. Draft delete and RSVP archive go through MCP Emails. Plus a run record with a "read to" anchor, so a run reads only new mail. | `inbox.py`, ready, in test |
| **Zoya, FAST** (zoya-one) | TOOLS: Gmail `get_thread` on ad@; `rfc822msgid` search; STEP 1 loop-in threads read with Gmail | OUTSIDE MAIL: the terse follow-up from ad@ with Zoya added, and the "adding @Zoya" loop-in, both through Gmail | Reads through MCP Emails. From ad@, only the loop-in, through MCP Emails. The terse follow-up stops: Zoya sends the mail from her own inbox once the thread reaches her, and the loop-in is how it reaches her. A thread with no current contact goes on Akshay's list, as now. The Gmail-reply quote clause goes. | batch: VARIANT entries in build_one.py |
| **Zoya, SLOW** (pinned file) | the same TOOLS and MESSAGE IDENTITY lines | the same OUTSIDE MAIL rule | The same change. The SLOW file changes, so its **pin moves**: a new commit and a new `zoya-slow-pin` ref, which the CTO creates, and a new hash in zoya-one's pointer. | batch |
| **Calendar** | Searches for an attendee's address and name, stakeholders from the scheduling thread, `in:sent` checks for thank-yous, reads of booking threads | none. Its sends are Zoya's, from her inbox. | Reads through MCP Emails. Thank-you drafts: MCP Emails `draft` create on the ad@ inbox, not Gmail `create_draft`. They land in Akshay's Drafts the same way. | batch |
| **Daily sweep** | STEPS 2, 3, 3a, 4: row-by-row Gmail reads (up to 60 rows a run); 3b; 6c billing search | **6c: Gmail forward of billing documents to Jaya from ad@** | Reads through MCP Emails. 3d pre-release drafts: MCP Emails `draft`. **6c is a send from ad@ that isn't a loop-in.** Under 420 it stops unless Akshay exempts it (see below). | batch |
| **WhatsApp** | 0d: team questions may read ad@ threads with Gmail (read only) | none from ad@ | 0d reads through MCP Emails only. | batch (rides on B2 or live) |
| **Evals** (not in the CTO's list) | STEP 2a: pitch thread by `get_thread` on Source ID `gmail:<thread id>`; Gemini notes mails | none | Reads through MCP Emails. A `gmail:<thread id>` key has no MCP Emails equivalent, so the thread is found by the guest's or PR's address and subject on the ad@ inbox. | batch |
| **Dossiers** (not in the CTO's list) | STEP 2a: pitch thread in Gmail | none | Reads through MCP Emails, as for evals. | batch |
| Host boards, FT Community directory | none | none | none | none |

## Does anything still need the Gmail connector?

**Not after the batch.** Every read moves to MCP Emails, and the drafts move to MCP Emails `draft` on the ad@ inbox. An IMAP draft shows in Akshay's Gmail Drafts, and he sends it by hand as now.
- Until the batch deploys, the calendar, sweep, evals and dossiers still call Gmail, so they keep the connector. Each Gmail call they make risks the same quota.
- After the batch, the CTO can detach the Gmail connector from every routine.
- **One open point:** whether an MCP Emails draft keeps the html body as Gmail shows it. To be checked once, on a test draft to the team.

## For Akshay (via the CTO)

1. **Billing forwards to Jaya (sweep 6c, decision 176)** are automated sends from ad@ to a team member. Decision 420 allows only the loop-in. Options:
   - (a) Exempt them as internal forwards, through MCP Emails `forward` on the ad@ inbox.
   - (b) A Gmail filter in Akshay's account that auto-forwards invoices to Jaya, with no agent involved.
   - (c) Stop them.

   Until he picks, the batch build stops them and puts a weekly "Akshay: billing docs to forward to Jaya: <list>" line on his list.
2. **CLAUDE.md** still says "Drafts stay Gmail create_draft" in places through the routine pages (Calendar rules). Under 420, drafts go through MCP Emails. The CTO is updating Rules for Zoya and Calendar rules.

## Status

**Inbox: round 6 (auditor CX-20261028-mailbox-outage), 64,968 B / be47f9a467b0bc43, 368 B under the build limit.**
- Cursor: T comes only from the inbox's own run record ("read to"), never another routine's Activity. Messages collapse only by RFC Message-ID.
- A message that fails to log goes on the record's "pending" line, is retried every run, and holds "read to" back until it logs or is noise. Never dropped.
- Replay replayCX.json (offline): P1 a failed log survives 3 runs, P2 a newer Zoya Activity doesn't move the cursor, P3 first run, P4 Message-ID dedupe. All pass.
- Its three findings are fixed in this build: the pending line is carried from the same record T comes from (a run that died after "Started" can't drop it); a message pending over 24 hours shows as "pending since <time>" in the report, so the morning check sees it; the window filter uses received time, the same basis as "read to".
- Ready for Cleanup.

Round 5 (decision 421 loop-in rule) was 64,755 B / 5eb83eabfc5bf31d.
- Built twice, byte-identical. 581 B under the build limit, so the next inbox change needs a cut.
- Rounds 1 and 2 of replay are in replay1A/1B and replay2.
- Since round 3, the inbox searches `[Gmail]/All Mail`. folder_list on ad@ shows IMAP has no "archive" folder; All Mail holds inbox, sent and archived mail once each.
- Accepted gaps: sibling replies in a chain can be missed; `original` has no size guard; there's still no Drive connector for Gemini notes.

**Batch: round 3.** Builds, twice byte-identical:
- Calendar: 56,348 / b6d381c24680e75a
- Sweep: 35,047 / 06c4120b2cd48ef1 (decision 423: 6c forwards billing docs to Jaya through MCP Emails `forward` on the ad@ inbox, with dedupe by Message-ID plus a Sent Mail check before every forward; the weekly list fallback is gone. Decision 422: STEP 3r never revives un# sponsored)
- WhatsApp: 27,015 / 0a20919c1584acad (on B2 as amended 28 Oct, 28,344 / 5cac9f1325c2f2ba: 29,352 / 9eef0b863062cab2)
- Evals: 15,734 / 97ec4f6541710b3f
- Dossiers: 6,479 / 807a125e5518853f
- Zoya SLOW file: 63,617 / fae90990931445db at commit f70901f6f07d4a6610fda60132b4cdbb5ac43979. Adds the quote fix, the handover Cc rewording, and measured time (slow-partial-1638): start and end come from Bash date -u, and SLOW stops only at 40 measured minutes (then Partial), never for size or context. Replay: replayTIME.json, all pass.
  - the offer is the first mail linking unhashed.co/sponsored;
  - at most 2 follow-ups, counting chases by anyone, but not loop-ins or answers;
  - the row closes Unresponsive when the step after follow-up 2 falls due;
  - no nurture, revival or last check;
  - disinterest gets one short thank-you, logged as a sponsored close, never the FT close note;
  - either end closes only the sponsored pursuit: a booking on the same row keeps its Status and can still go to nurture.
  Replays: replay422.json (round 1) and replay422b.json (round 2: 11 of 12 pass; round 3 fixes the same-row booking case and the 6c retry risk).
- zoya-one candidate: 42,109 B / 23551dc5bb4a0d12, pinned to f70901f (built twice, identical; carries decision 424's new-thread rule)

At deploy the CTO moves `refs/heads/zoya-slow-pin` to that commit.

Replays: batch-replay1 and batch-replay2. Round 2 confirmed the Zoya loop-in fix. Round 3 fixes its smaller findings:
- The idempotency key goes only on the call that sends.
- A leftover loop-in draft is cleaned up.
- ad@ is never in To or Cc on a loop-in.
- The calendar's stakeholder rows are keyed msgid:.
- Sweep 6c skips Akshay's own sent mail.
- The stale cap clause is gone.
- Drafts log their latest draft_id.

**For the CTO and Akshay:**
1. **Calendar writes:** writes with notificationLevel ALL make Google mail notices from ad@'s calendar. These are the inbox's 6e cancel, calendar moves, Zoya's invites and WhatsApp 0d bookings. Does 420 allow them?
2. **Sweep 6c:** settled by decision 423 (option a): forwards stay, through MCP Emails.
3. **Skills:** ft-guest-eval and ft-host-dossier still say "Gmail". The prompts override that, but the skills should be updated.
4. **Rules for Zoya:** the page needs the 420 loop-in wording (the CTO).
5. **Predating 420:** the FT thank-you is "a reply" in the calendar prompt but "a standalone new mail" in SLOW.

**Superseded:** the gmail-hotfix build.
