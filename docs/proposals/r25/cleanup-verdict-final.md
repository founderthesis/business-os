# r25 final: Cleanup verdict on the delta from 169abf1 (head 66e6839)

Cleanup, 10 Nov. Read-only. I built every file twice and got byte-identical results both times. The Zoya builds came from a fresh worktree at f70901f with r25/zoya/build_one.patch, pinned at a4a553f37e1adb6f40030b08848a56850c097af8.

**Verdict: accepted. Deploy it.** None of the notes below blocks the deploy. T1 is a one-line fix and is worth adding before deploy if Main can do it in minutes.

## What's in the delta

| Commit | What |
|---|---|
| 96560c5 + 205a2e6 | URGENT: a reply key carries no time, and the Sent check runs as a Bash python step |
| f5ce685 | WhatsApp TIMING: send at the time Akshay names; section 6 keeps his time as a note line |
| a4a553f + 57bfbad | Decision 538 in capture STEP 3 and the hourly's row create, paid for by citation cuts |
| 66e6839 | S1 and S2 |

Inbox actions is byte-identical to 169abf1 (b9101c39). Only section6-535.md changed on that side.

## Checks

### (a) to (f) from 96bdfb8

These still hold. No new em dash in any build. Every size is under its cap; the hourly is 62,998 bytes, under 63,000.

### 7-day limit

It's in STEP 0w 3/. It counts sets with "Akshay to <name> on WhatsApp" and key wa-send: or wa-chase:. Akshay's own typed replies don't count. A held draft waits untouched. Group news posts are exempt.

### S1

The community-invite check accepts only the two exact note lines, each naming the person:
- "Akshay's call: 'invite <name>' (WhatsApp); standing invite drafted"
- "Akshay's call: 'invite <name>'; standing invite drafted"

Any other note quoting "invite" is refused.

### S2

NO REPLY now also holds a draft when the row has any Email in Activity from their side (Guest, Via or a Stakeholder) dated after the draft. It applies at the scheduled re-check too, through "NO REPLY again".

### Decision 538 against the Notion row

Row 538 is "In force", with Routines Inbox and Zoya. The ledger lists the subjects as:
- un#: crypto and web3
- Built to Share: teams, leadership and ownership
- Human by Design: AI and human outcomes

Capture STEP 3 states the same three subjects, and an off-topic pitch to a client-show inbox goes to Founder Thesis. routines/inbox.md carries the same sentence. The hourly's row create cites it as "(a pitch: Show by subject, not inbox alone, decision 538)", and that create points to capture STEP 3.

It matches. One wording note is under N4.

### Send time is Akshay's alone

STEP 0w TIMING takes the time only from two places:
- the row's Your call;
- the Claude note line "Akshay's call: '...' (WhatsApp send time)", written since the draft. Section 6 writes that line from his own words, verbatim, then clears Your call.

The rule reads "You never choose a time: no window, no default delay." With no time named, the draft goes this run, as before. I grepped for send_at and scheduled_messages_write: it appears only in WhatsApp STEP 0w, never in the SLOW file, the hourly or actions. No agent picks a time anywhere.

Holds, with T1 below.

### URGENT reply-key fix

These match in the hourly and the SLOW file:
- the timeless key "<row>:reply:msg-<id>[-n]";
- the lookup "any key starting <row>:reply:msg-<id>, with or without a time", so older keys still match;
- "since the inbound's Date";
- "never by eye and never skipped, early exit or not".

### Citation cuts

I diffed word by word, sentence by sentence, against r24 for the hourly and against f6793c2 for the SLOW file. Only dates, item numbers, "(Cleanup C1)", "(6 Nov, the Dinesh case)", "(CTO, 4 Nov: no correcting after the fact)" and one example list were removed. No rule and no decision number was lost. The hourly's deployment reference moved to e3401ba5b374.

### SLOW task

It names the same pin and file as the build:
- `git show a4a553f…:routines/zoya/release/zoya-slow-work.txt`
- `must start e9ac59f86b4bbabf`
- `total = 94,721 characters`

## Notes (none blocks)

### T1: resolve a named day forward, from the day he wrote it (should-fix, one line)

"A named time already past at the run: it goes now." Suppose Akshay writes "tue 10am" on Wednesday. If the run reads that as the Tuesday just gone, the message goes at once, a week early. Section 6 already dates its note line, so the fix is easy.

Proposed wording: "A day name or time without a date is the next such moment after the date his call was written (the note line's date, or today for Your call), never an earlier one."

### T2: how later runs find a queued row (clarity)

After queueing, the box is unticked and the draft is kept. The (a)/(b) loop no longer picks the row up. "Each later run" should say where to look: "rows with an Activity whose Summary starts 'Zoya scheduled:' and no sent or cancelled outcome".

Also, Akshay's "tick Send WhatsApp" segment stays in his queue while the send is queued. Swapping it for a note "WhatsApp queued for <time>" would read better.

### T3: cap and 7-day counts for a named future day ignore other queued sets

On the named day, those counts read only "Akshay to" Activities. Two queued sets for the same day or person aren't counted against each other. This is rare, and the fix is to count "Zoya scheduled" Activities for that day too.

### T4: a second set while one is queued

The draft stays in the column, unticked, while its set is queued. If someone redrafts it, or Akshay re-ticks an edited text, the new text gets a new sha and a new key. That would queue or send a second set alongside the first.

Suggested fix: while a row has an open "Zoya scheduled" Activity, no new send or queue goes out for that row. A changed draft cancels the queued ids first.

### N1: the SLOW file lost its only copy of decision 490's examples

The removed examples were: thanks, an acknowledgement, "will revert", agreement. The rule itself ("needs nothing of him … decision 490") stays, and the hourly still has the examples. This is fine, but SLOW now applies 490 from the rule alone.

### N2: handoff.md's Builds section is stale

It says "Unchanged: … capture …" and "The hourly is unchanged". Both changed in this round. The table below is the one to use.

### N3: Akshay's "I will put the send day/time in my call. don't schedule." has no Decisions row

The newest row is 538. It amends 535 and 537, so per CLAUDE.md it should be logged. That's the CTO's job.

### N4: wording order in capture STEP 3

The line starts "Show = the one of ours the mail names … anything else is Founder Thesis", and the 538 sentence comes after it. Row 538's operative rule is the inbox address, so both versions file the Patlytics case correctly. A pitch that names un# but has nothing to do with crypto is a judgement call under either wording. No change needed unless the CTO wants the 538 sentence to override naming.

### Still open from earlier rounds

- S3: the tick isn't snapshotted. Accepted as team trust.
- S4: move the 522-era "Zoya: send the approved WhatsApp" rows. That's the CTO's job, before deploy.
- Zoya episodes is not live and still not fully reviewed.

## Final deploy table, in deploy order

| # | What | Bytes | sha256 |
|---|---|---|---|
| 1 | Section 6 paste: r25/section6-535.md (replaces WHATSAPP CHASE, adds WHATSAPP INVITE) | 6,083 | 2624ed44147f3781bd89b237556dd50cf3ce6f4c125cb8634cb95a534f7d2593 |
| 1 | Inbox actions: r25/actions.txt (same as 169abf1) | 48,332 | b9101c39987ca6051c3f93f63e55568213ed87723239c14e201e5449e27dcdaa |
| 2 | Inbox capture: r25/capture.txt | 50,724 | 73a73754fad00eec54bf584b295e16a030047e344dde672a8a932d1691149f25 |
| 3 | WhatsApp: r25/whatsapp.txt | 37,759 | 25ca6f44b5cbe1ea5295d100beacd500398395aef46cd5c2f378e1f0cbdff53f |
| 4 | Move refs/heads/zoya-slow-pin from 1556243 to a4a553f37e1adb6f40030b08848a56850c097af8. That is the SLOW file routines/zoya/release/zoya-slow-work.txt (94,721 characters) | 94,725 | e9ac59f86b4bbabfe3833c6a8a703540cc410b799c099a9dec95637bbdd7e2dc |
| 4 | Zoya SLOW task: r25/zoya/zoya-slow.txt | 15,687 | 179e14a574d076a695edb60002ffaab8eef895194f2bd81846fa6871e9595a7c |
| 5 | Zoya hourly: r25/zoya/zoya-one.txt | 62,998 | ba816e8b94d604c9860cea20e7027ed6a0c361bc870177bd70f9435a5a755966 |

Steps 4 and 5 should go out together, or close together. Both carry the timeless reply key and the Sent check. The new lookup matches either key form, so the order between them is safe. Not deployed in this round: calendar, sweep, host boards, dossiers and Zoya episodes.

If T1 or T4 goes in, only WhatsApp (and section 6 for T1) changes. I'll review that delta alone.
