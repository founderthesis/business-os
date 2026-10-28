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

**Inbox: round 3, 64,773 B / b3fd1a1ab8fb9f80.** Built twice, byte-identical. 563 B under the build limit, so the next inbox change needs a cut.

Results so far:
- **Round 1** (replay1A/1B): 12 defects, all fixed.
- **Round 2** (replay2): all 12 scenarios pass, with zero Gmail calls and no ad@ mail other than the loop-in.

Round 3 fixes:
- The repeat-pitch wording: STEP 3 sends that loop-in, and STEP 6 skips it.
- The vendor loop-in catch-up.
- A "loop-in skipped: <why>" marker, so deliberate skips aren't re-read.
- One read per message across folders.
- "read to" no longer pinned by a message that fails twice.
- One mapping for rfc822msgid.
- "unlinked" defined.

Known and accepted:
- References aren't stored, so sibling replies in a chain can be missed.
- `original` has no size guard.
- There's no Drive connector to open Gemini notes (as before).

For Akshay: STEP 6e's invite cancel (decision 398) makes Google mail cancellation notices from ad@'s calendar. Does decision 420 allow that?

**Batch: round 2.**

Builds (twice, byte-identical):
- Calendar: 56,220 / 61cd1bb523e77225
- Sweep: 34,289 / 1289ac6ee35c716b
- WhatsApp: 26,977 / 0e08ab80d46e6cb8 (on B2: 28,939 / 0289a64b1f92e8f4)
- Evals: 15,696 / 96ed4f172486c865
- Dossiers: 6,441 / 43d8eae28c50f4f5
- Zoya SLOW file: 61,353 / 0516b0cf911067ff at commit 2ee52c4
- zoya-one candidate: 40,809 / eb083c28637ec9a0, pinned to 2ee52c4 (this folder)

At deploy the CTO moves `refs/heads/zoya-slow-pin` to 2ee52c4.

Round 1's batch replay is in batch-replay1.json. Fixed since:
- **Zoya's loop-in:** where we wrote last it would have gone to Akshay. It now replies on the addressed person's own message, or uses a reply draft whose To is set by update.
- **MAILBOX** now holds inside skills, reads archive and looks up Message-IDs.
- **Sweep 6c:** the forward wording is gone, and there are no cross-week duplicates.
- **Reply drafts:** their To is set by update.

Two things for the CTO:
- **Skills to update:** ft-guest-eval step 5 and ft-host-dossier Stage 0 still say "Gmail". MAILBOX tells the routines a skill's "Gmail" means MCP Emails, but the skills themselves should be updated (account skills, not in this repo's control).
- **Rules for Zoya:** the page still describes the old terse follow-up from ad@ and needs the 420 wording. The CTO is updating it.

**Superseded:** the gmail-hotfix build.
