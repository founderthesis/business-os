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

## Builds

Built twice, byte-identical, and rebuilt from a fresh worktree at f70901f with r26/zoya/build_one.patch. The r25 patch still reproduces the r25 builds. No new em dash.

| Routine | Base | Build | Bytes / sha256 |
|---|---|---|---|
| Zoya hourly | r25 821895c1 | r26/zoya/zoya-one.txt | 62,990 / 5631d1497077a7a5 |
| Zoya SLOW file | r25 12de32e (7e72f8dd) | routines/zoya/release/zoya-slow-work.txt at **63a4908** | 94,797 / df8adb0224c6a0e5 |
| Zoya SLOW task | r25 825a3716 | r26/zoya/zoya-slow.txt (pin 63a4908) | 15,646 / d25036d209ea2bb8 |
| Zoya episodes (not live) | r25 f03f9677 | r26/zoya/zoya-episodes.txt | 50,146 / b796ea43640400c3 |

**How to build:** apply r26/zoya/build_one.patch at f70901f, then run `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 63a49087f53f6b5589ef0cbdb09ee79aeff0e281`.

**Deploy:** after r25. Pin 63a4908, then the SLOW task and the hourly.

The hourly has 10 bytes left under 63,000. The early-exit gate (about 230 bytes) will need its own cuts.
