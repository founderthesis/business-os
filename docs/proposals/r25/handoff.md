# r25 item 1: WhatsApp automation (decisions 535 and 537)

Main, 10 Nov. CTO ask of 17:55 JST, built on the live r24 prompts (deploy 311e607). Spec 41419a301a7f8130a4ebeabffd289e35, including "Your comments, applied"; templates 41419a301a7f81ea8e73e0deb08052aa. Both decisions are in force in the ledger. Nothing is deployed, the pin ref isn't moved, and nothing was written to Notion.

## Change, 10 Nov (Akshay: "don't automate paas messages - propose the draft to me and I will finalise and check the box")

- **PaaS follow-ups 1 and 2 are approve-each, not standing.** SLOW writes the one-liner into "WhatsApp draft", never with a "[standing: ...]" line, plus "Akshay: tick Send WhatsApp: PaaS follow-up for <first name> (<D Mon>)" with Akshay in Waiting on. Nothing goes out on a PaaS row without his tick.
- **WhatsApp STEP 0w accepts only two standing templates:** community-invite and release-day. A "[standing: paas-...]" line would fail its check and go to Akshay.
- **Below:** wherever this hand-off says "paas-1 or paas-2" is standing, read it as approve-each.

## Change, 10 Nov 20:45 JST: Cleanup's S1 and S2 (verdict 96bdfb8, accepted at 169abf1)

- **The 7-day per-person limit** is already in STEP 0w 3/ (since 4f55763). It's unchanged.
- **S1:** the community-invite check now accepts only the two exact note lines its writers produce, naming this person:
  - "Akshay's call: 'invite <name>' (WhatsApp); standing invite drafted", from STEP 0a e0;
  - "Akshay's call: 'invite <name>'; standing invite drafted", from section 6.

  Any other note quoting "invite" doesn't count.
- **S2:** NO REPLY also holds a draft when any Email in Activity from their side (Guest, Via or a Stakeholder) is on the row, dated after the draft was written. That covers a PR or EA replying by mail for the guest. It applies at a scheduled re-check too.
- S3 is unchanged. S4 (moving the open 522-era "Zoya: send the approved WhatsApp" rows) is the CTO's, before deploy.
- **WhatsApp is now 37,759 / 25ca6f44b5cbe1ea.** Nothing else changed.

## Change, 10 Nov: decision 538 (a pitch's Show comes from its subject, not the inbox it reached)

The case was Sung Hong at Patlytics: AI patent software, pitched only to the un# inbox, filed on un# and eval'd Decline for not being crypto. The CTO has moved that row to FT by hand.

- **Inbox capture STEP 3** (live r24 f64eb54e, now 50,724 / 73a73754): the Show line gets the CTO's sentence as written:
  > "The address it came to alone never decides: a pitch to a client-show inbox (un#, Built to Share, Human by Design) with no link to that show's subject (un#: crypto and web3; Built to Share: teams, leadership, ownership; Human by Design: AI and human outcomes) is Founder Thesis (decision 538)."

  The repo copy routines/inbox.md gets the same sentence.
- **Zoya hourly STEP 1** (parts/mail.txt): where she creates a row "as inbox capture STEP 3 creates it", it now reads "(a pitch: Show by subject, not inbox alone, decision 538; ...)".
  - Four cuts pay for it: "(Cleanup C1)", "(L1, Cleanup)" becomes "(L1)", "GUESTS AND THE FORM (6 Nov)" loses its date, and one parenthesis is shortened.
  - The hourly is 62,998 bytes, under 63,000.
  - Those cuts also reach the SLOW file and the SLOW task, so the pin moves to **a4a553f**. SLOW has no rule change.

## Change, 10 Nov: send at the time Akshay names (Akshay: "I will put the send day/time in my call. don't schedule.")

**WhatsApp STEP 0w TIMING.** A ticked draft goes at the day and time Akshay names. It reads that from the row's Your call, or from the Claude note line inbox actions keeps of his call: "Akshay's call: '...' (WhatsApp send time)". The time is IST unless he names a zone.
- **No time named:** it goes this run, as before.
- **A time already past:** it goes now.
- **Agents never pick a time:** no window and no default delay.

**A time still ahead:**
1. All of 3/'s checks run now: no reply, the number, and the cap and 7-day rule counted on the day he named. His time stands even inside quiet hours, because it's his choice.
2. It logs "Zoya scheduled: WhatsApp to <name> for <D Mon HH:MM IST>" under the send key, which also stops a second queueing.
3. It queues each message with Blueticks scheduled send, 20 seconds apart in order.
4. It records the time and the Blueticks ids in a Claude note line, unticks the box and keeps the draft.

**Each later run:**
- **Before the time:** it re-runs the no-reply check. A reply cancels the queued messages and puts "Akshay: <name> replied, scheduled WhatsApp cancelled" on his list.
- **After the time:** it reads the Blueticks status. If all were sent it logs and clears as before; if any failed it reports a failure.

**Section 6** (r25/section6-535.md, the WHATSAPP CHASE 5/ step) tells inbox actions to keep a send time from Your call as that Claude note line, so the WhatsApp routine can find it after Your call is cleared.

The duplicate-reply fix and the 7-day-per-person limit are kept. **WhatsApp is now 37,467 bytes.**

## URGENT, 10 Nov 20:30 JST: one inbound got two replies (TYC, Abhinav; 17:44 and 19:44 JST)

**Cause.**
- The 19:39 run raised the reply action again with its own time in the key ("...:reply:msg-...:2026-11-10T19:44:00+09:00").
- The Sent check looks for our mail "since the action was raised", so it looked only after 19:44 and missed the 17:44 reply.
- The run also says it skipped the Sent check.

**Fix, in the hourly, the SLOW file and episodes:**
- **(a) A reply's key carries no time:** "<engagement page id>:reply:msg-<the inbound's Message-ID>[-n]", or "uid-<inbox>-<UID>" when there's no Message-ID. One reply per inbound, ever. Its raised time is the inbound's own Date. The short form is "Zoya [reply msg-<id>-n]".
- **(b) The Sent check runs in a Bash python step, never by eye, never skipped, early exit or not:**
  - The step is given the thread and Sent as read: each message's From, Date and Message-ID, in a quoted heredoc.
  - It finds an Activity holding any key that starts "<row>:reply:msg-<id>", with or without a time, so older timestamped keys still match.
  - It then lists our messages to that recipient on the thread since the inbound's Date: yours, or ad@'s other than a loop-in.
  - A match means "completed match"; nothing is sent.
- **SLOW's OUTCOME CHECK** accepts the timeless reply key form.
- **Paying for it:** I cut dates and item numbers from cited rules in the hourly ("(decision 438; Akshay, 5 Nov, item 15)" becomes "(decision 438)" and so on), the duplicated decision 490 example list, two incident notes and one example. Every rule and decision number stays. **The hourly is 62,991 bytes, under 63,000.**
- **The pin moves to 205a2e6.** The SLOW file also carries the WhatsApp change below.

**Deploying the hourly alone:** the hourly can go ahead of the rest of r25. It doesn't depend on the WhatsApp build. If it goes first, SLOW should follow soon on pin a4a553f, because SLOW shares the Sent check and the key form. Until then, the live SLOW still keys with a time, but the new hourly's lookup matches either form.

## Change, 10 Nov (CTO's answers)

- **One WhatsApp set per person per 7 days** (spec section 4) is now in STEP 0w 3/. It counts only sets this routine sent from Akshay's number (Activities "Akshay to <name> on WhatsApp", keys wa-send: or wa-chase:); his own typed replies never count. A draft that would break it waits untouched until the day it may go. Group news posts are exempt; they keep their one-per-member-a-quarter rule.
- **SLOW is unblocked:** billing was fixed, and SLOW ran on r24 at 14:56 JST. So the PaaS drafts will be written once this deploys.
- **Release day:** the CTO gives the Episode copywriter chat the marker line at deploy.

## What's in it

**1. WhatsApp routine: one SEND step (STEP 0w, rewritten).** It sends from Akshay's number only:
- (a) a draft whose "Send WhatsApp" box is ticked; the tick approves exactly the text in "WhatsApp draft" at that moment;
- (b) a draft whose first line is "[standing: <template>]" and whose check holds:
  - **community-invite:** Akshay's "invite <name>" kept in a Claude note line, a recording on the row, and FT Community at To invite or Invited;
  - **release-day:** a Claude note line "release-day WhatsApp drafted (Episode copywriter chat)", the Episode Published or with Actual release set, and the draft holds the Episode's Short link;
  - **paas-1 or paas-2:** Show PaaS and Zoya SLOW's note line "PaaS WhatsApp <n> <key>".

  If a check fails, nothing is sent and "Akshay: tick Send WhatsApp: ... check failed" goes on his list.

What the step does with each draft:
- **Message split:** one message per non-empty line. A block between "[one message]" and "[/one message]" goes as one message (the invite's member list). The "[standing ...]" and "[to ...]" lines are never sent.
- **Recipient:** the Guest, or the person a "[to: <full name>]" line names.
- **Group news post:** "[to: group The Founder Thesis Community, tag <name>]" posts to that group and tags the member with mentions. At most one per member a quarter.
- **Before every send:**
  - quiet hours 00:30 to 07:30 JST, and release day only after 10:00 IST;
  - **20 sets a day**, one person's set counting once;
  - **no reply** from that person since our last message, in ad@, Zoya's inbox and their WhatsApp chat. A reply means untick and "Akshay: <name> replied, draft held";
  - **the number from People Phone only**, with a country code. Decision 535 replaces 519's FT Community and saved-contact lookup.
- **Log and clear:** it logs the Activity first ("Zoya sending ..." becomes "Akshay to <name> on WhatsApp: ..."), with key "wa-send:<row>:<draft sha 12>" and a per-message idempotency key, then clears the draft, the box and the tick segment.
- **486/522 chaser:** it now goes through this same step. There's no second sender.

**2. Draft writers, inside existing steps.**
- **Invite:**
  - **From WhatsApp:** "invite <name>" to Zoya is handled by STEP 0a e0, which now also writes the standing invite draft, for recorded guests only, from the template plus the invite kit's member list.
  - **From Your call:** "invite <name>" is handled by section 6's new WHATSAPP INVITE block, which the CTO pastes.
- **PaaS follow-ups:** done in the SLOW file (my call), replacing PAAS REMINDERS.
  - Follow-up 1 at 7 quiet days after our last message, follow-up 2 at 14 days after follow-up 1, each after a mail and WhatsApp reply check.
  - Each is written as a "[standing: paas-<n>]" draft.
  - No usable number: the reminder goes on Akshay's list as before. After follow-up 2 plus 14 quiet days: "Akshay: keep open or park?". Never a third.
  - Nurture stays monthly on his list.
  - Why SLOW: PAAS REMINDERS already lives there, so this cuts before it adds, and it already has the anchor logic and Blueticks.
- **Approve-each chaser (section 6, rewritten):** the draft goes in the column, with "Akshay: tick Send WhatsApp: chaser to <first name> (<D Mon>)" in Next action and Akshay in Waiting on, so it lands in his regular queue. Reading the chat first, mirroring his style and the "context:" line (now in the page body, never the column) are kept from 522. Each line is one message, so " || " is gone, which also settles Cleanup's r24 item 9 note.
- **News scan, STEP 3n (new):** the first WhatsApp run on a Saturday.
  - Checks up to 25 Added members a run for news in the last 7 days.
  - A verified hit, on a member with no post in 90 days, becomes a fresh post draft on their FT row, tagging them, with the link, for his tick.
  - Drafts only.

**3. Number enrichment: dropped from this build (CTO, 10 Nov).** The CTO is running it from the CTO session, since Akshay asked for it now. The read-only script Main wrote (`migration/wa_numbers.py`) is removed here so there's one source. It's in commit 9a052ef if it's useful.

## Builds

Each was built twice, byte-identical. The Zoya builds were also rebuilt from a fresh worktree at f70901f with r25/zoya/build_one.patch. No new em dash.

| Routine | Base (live) | Build | Bytes / sha256 |
|---|---|---|---|
| WhatsApp | r24 bec8c1e1 | r25/whatsapp.txt | 37,759 / 25ca6f44b5cbe1ea |
| Inbox actions | r24 845d0a41 | r25/actions.txt | 48,332 / b9101c39987ca605 |
| Zoya SLOW task | r24 595f107f | r25/zoya/zoya-slow.txt (pin a4a553f) | 15,687 / 179e14a574d076a6 |
| Zoya SLOW file | 1556243 (b6d1c52b) | routines/zoya/release/zoya-slow-work.txt at **a4a553f** | 94,725 / e9ac59f86b4bbabf |
| Zoya hourly | r24 459d1dd1 | r25/zoya/zoya-one.txt | 62,998 / ba816e8b94d604c9 |
| Inbox capture | r24 f64eb54e | r25/capture.txt | 50,724 / 73a73754fad00eec |
| Zoya episodes (not live) | r24 1d238933 | r25/zoya/zoya-episodes.txt | 50,091 / 97dd915197ddfad9 |

Unchanged: calendar, capture, sweep, host boards and dossiers.

**How to build:**
- Non-Zoya: `python3 docs/proposals/r25/patch.py <wa|act> docs/proposals/r24/<whatsapp|actions>.txt <out>`.
- Zoya: apply r25/zoya/build_one.patch at f70901f, then run `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin a4a553f37e1adb6f40030b08848a56850c097af8`.

**The section 6 paste:** r25/section6-535.md replaces the WHATSAPP CHASE block (the 522 text) and adds WHATSAPP INVITE. Paste it with inbox actions.

**Deploy order:**
1. Section 6 paste plus inbox actions.
2. WhatsApp.
3. Zoya pin a4a553f, then the SLOW task. The hourly is unchanged.

## For the CTO: unclear or needing a call

1. **PaaS timing replaces decision 496's reminders.** The old reminders were day 4 and 10 (New or Contacted) and day 3 and 10 (after a proposal). Under 535 and 537 they become the WhatsApp follow-ups at 7 and 14 quiet days, and the mail-only reminder stays only where there's no number. Confirm that's the intent.
2. **One WhatsApp per person per 7 days:** confirmed by the CTO and built (see the change above).
3. **The release-day writer is the Episode copywriter chat,** whose instructions aren't in this repo. For STEP 0w to accept a release-day draft, that chat has to write the draft starting "[standing: release-day]", with the Episode's Short link and Ranjita's post link, plus the Claude note line "YYYY-MM-DD: release-day WhatsApp drafted (Episode copywriter chat)" on the guest's row. Without the line, the draft goes to Akshay for a tick. The template's "PR in a separate message only if they handled the booking" isn't automated; it's a ticked draft.
4. **Numbers:** dropping 519's lookup means more "no WhatsApp number" asks until the CTO's enrichment writes land. Best if they land before this deploys.
5. **SLOW is unblocked** (billing fixed; it ran on r24 at 14:56 JST, 10 Nov).
6. **Standing lines rest on note markers.** A standing draft is trusted because of its "[standing: ...]" line plus the matching Claude note line that only the authorised writer adds. Anyone on the team with Notion edit access could still forge one; I judged that acceptable inside the team.
