# r26: decision 555 (their newest thread wins)

Main, 11 Nov. CTO ask, built on the r25 Zoya builds (pin 12de32e). The early-exit and lock fixes (early-exits-and-lock.md) wait on the CTO's yes and will join this round. Nothing is deployed, the pin ref isn't moved, and nothing was written to Notion.

## Decision 555

**Zoya THREADING** (hourly, SLOW file, episodes): "Every mail that continues a conversation is a draft action reply on the original thread's latest message in your inbox" now goes on:

> (their side wrote on a newer chain: that one, decision 555; Cc who still matters from the old one, nothing more there; note "thread moved to <subject> on <D Mon>", which later mails, chases and Sent checks use)

The old rule stays where only our side has threads: it switches only when their side wrote on the newer chain, and "never a fresh mail to continue a thread" is unchanged. The SLOW file and episodes take the same THREADING part, so follow-ups and chases follow the note line too.

**Inbox capture and actions: no change.**
- Capture's only send is the loop-in from ad@, which already replies on the inbound message itself, so it's their newest chain by definition. Its repeat-pitch rule already sends the loop-in on the new thread.
- Actions never sends; it queues Zoya's steps, and she picks the thread.

Adding the rule to either would be a second copy of it (decision 357).

**Paid for** by description and citation trims, no rule:
- the follow-ups page's summary in the rules list goes;
- "(decision 415: one Zoya run at a time, fail-closed)" becomes "(decision 415)";
- "decision 490, amending 448" becomes "decision 490";
- "decision 453, item 10" becomes "decision 453";
- two example lists in the hourly are shortened (the Your call step types, and the held/blocked definitions in the record's first line).

## Decision 557 (a precall call with no Tier: the template follows the eval)

The case: Vishal Nigam @ WTF. The eval said Decline (sponsored route), and Akshay's call was just "invite to precall". STEP 6c a0's "pre-call -> Tier 1" sent him the Tier 1 mail.

- **Inbox actions STEP 6c a0,** the clause replaced in place, no new paragraph: "pre-call -> by Eval verdict, decision 557: Book immediately or Strong consider Tier 1, Pre-call needed or Evaluate after call Tier 1.5, anything else or no eval Tier 2". It sits under "No Tier:", so a Tier named on the row or in Your call still wins. "Sponsored track", the other verdict in Engagements, falls to Tier 2. The repo copy routines/inbox.md matches.
- **Zoya has no copy.** STEP 0e sends the template that inbox actions filled into "## Decision mail", so the fix reaches her mail through actions.
- **Replay:** r26/replay_557.py reads the clause from the built prompt and checks 8 cases. Decline plus "invite to precall" picks Tier 2; so do Sponsored track and no eval. The other four verdicts map as decided, and a named Tier 1 on a Decline row stays Tier 1. All pass.
- **Build:** `python3 docs/proposals/r26/patch.py act docs/proposals/r25/actions.txt <out>`, on r25's actions (d0a8c26a). Built twice, byte-identical, no new em dash. **Actions is 48,515 / 2b894385566ff415.**

## WhatsApp STEP 0w (three early exits, nothing sent since r25)

See whatsapp-early-exit.md. In short:
- a GATE: the status script decides, and an early Failed sends the run back;
- 0w takes at most 5 drafts a run;
- HIS OWN MESSAGE holds a draft once Akshay has messaged the person since it was written;
- GREETING holds a draft that greets someone other than its recipient.

**WhatsApp is 39,817 / c0ac14891bb14218,** on r25's ddb69276.

## Decision 558 (room asks to Mamatha: the hourly alone, by WhatsApp)

Sparsh Gupta's 12 Nov recording had no Zencastr room. The row's "ask Mamatha" segment was never sent: SLOW left it to the hourly, and the hourly only put "no recording room" on Akshay's list within 24 hours.

- **Hourly STEP 0r, ROOM ASK** (replaces the 24-hour sentence):
  - Each run, every Founder Thesis Booked recording with no room link anywhere (her mails and WhatsApp chat, the invite, Call link) and no "room asked" note goes into one WhatsApp to Mamatha, soonest first. It's sent by Blueticks to her one-to-one chat and opens "Zoya ✨" (decision 226).
  - Each row gets the note "room asked <event id> <date>", and "Zoya: room from Mamatha for <guest> (asked <D Mon>)" replaces any ask-Mamatha segment.
  - No link 24 hours later: one reminder. Within 48 hours of the recording and still none: Akshay's list, once.
  - Her chat is read each run from the oldest open ask, and a link there is handled as one in her mail: written to the invite and the row's Call link (and Recording link) in the same run. Both Zencastr forms already count (decision 553).
- **Hourly HARD and TOOLS:** "No WhatsApp in FAST work" now allows ROOM ASK to Mamatha, and TOOLS loads Blueticks ("+bluetick"). The hourly trigger already has the bluetick connector (checked with get_trigger), so no connector change is needed.
- **SLOW file:** the room ask joins the list SLOW never selects or sends ("the prep note, recording link, room ask to Mamatha (decision 558) and day-before note are the hourly task's"). That's the whole of SLOW's part: it had no room step of its own, only the habit of leaving the segment open.
- **Item 5 (the CTO round flags any recording within 72 hours with no link)** is in the CTO round's prompt, which is the CTO's to edit, not a Main build.
- **Paid for by cut before add (decision 357):** the hourly's VOICE paragraph repeated Rules for Zoya line for line. That covers tone, opening, fragments, numbered points, one ask, emoji, the never-corporate list, banned words, Plain English and the 40% rule. RULES LOAD loads that page in full every run and blocks every send if it's short. VOICE is now a pointer that keeps the sign-off, no em dashes, never describing herself and the 40% limit, saving 738 bytes. **Cleanup should check this cut specifically.**
- **Replay:** r26/replay_558.py checks the built hourly and SLOW file, 5 cases, all pass:
  - booked, no room, 6 days out: the ask is sent that run;
  - room already on the invite: nothing;
  - asked 25 hours ago: one reminder;
  - 40 hours out, already reminded: Akshay's list once;
  - SLOW sees "Zoya: ask Mamatha for the Zencastr link": SLOW does nothing.
- **The hourly is now 62,856** (144 bytes spare). The SLOW file changes, so the pin moves to **63d63ec**.

## Builds

Built twice, byte-identical, and rebuilt from a fresh worktree at f70901f with r26/zoya/build_one.patch. The r25 patch still reproduces the r25 builds. No new em dash.

| Routine | Base | Build | Bytes / sha256 |
|---|---|---|---|
| Zoya hourly | r25 821895c1 | r26/zoya/zoya-one.txt | 62,856 / d46c0e7de9649c49 |
| Zoya SLOW file | r25 12de32e (7e72f8dd) | routines/zoya/release/zoya-slow-work.txt at **63d63ec** | 94,833 / 78332307d8ba3cfd |
| Zoya SLOW task | r25 825a3716 | r26/zoya/zoya-slow.txt (pin 63d63ec) | 15,646 / 4da2f1466a600967 |
| WhatsApp | r25 ddb69276 | r26/whatsapp.txt | 39,817 / c0ac14891bb14218 |
| Inbox actions | r25 d0a8c26a | r26/actions.txt | 48,515 / 2b894385566ff415 |
| Zoya episodes (not live) | r25 f03f9677 | r26/zoya/zoya-episodes.txt | 50,146 / b796ea43640400c3 |

**How to build:** apply r26/zoya/build_one.patch at f70901f, then run `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 63d63ec2ef9211dbc6a6b77b388aa57f96201d1f`.

**Deploy:** after r25. WhatsApp and inbox actions, then pin 63d63ec with the SLOW task and the hourly.

The hourly has 10 bytes left under 63,000. The early-exit gate (about 230 bytes) will need its own cuts.
