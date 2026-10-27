# Pending on Akshay

When Akshay asks what's pending on him, read this list, check each item is still open, and give him the open ones. Remove an item once it's done. The 21 Oct list before pruning is in docs/archive/akshay-pending-2026-10-21.md.

## Moved to Notion (27 Oct)
Akshay's open items now live in Engagements as Kind Task rows, Waiting on Akshay (his queue view). Akshay, 27 Oct: "Add all pending tasks for me to my engagements view". 11 rows were created 27 Oct (Source ID akshay-pending.md or CTOA-01 item 10). Add new items there, not here. Dropped as done or overtaken:
- Host board sync agent: created.
- Yuti: a sponsored offer went out 22 Oct.
- Sanjiv Bajaj: Zoya runs the sponsored chase.

## Notion tool permissions (27 Oct, after Akshay's fix)
- The policy push at 00:39Z on 27 Oct shows notion-create-pages on always_ask, and notion-delete-pages and notion-delete-databases on always_allow. That is the reverse of what's wanted. Akshay to flip those three. CTO still asks before any deletion (decision 384).

## Before the next paid API run
- Standing rule for the rerun script added to .claude/settings.json by the CTO (22 Oct, f869f55). New sessions read it at start. If the auto-mode check still blocks paid runs, approve in the worker's chat or switch its mode from Auto to Accept edits for the run.

## Open questions on pages
- Calendar rules: what Out of office means for you, and hours never to book.
- Rules for Zoya: keep the day-before release WhatsApp? Should the agent write the 3 post options from the transcript?
- Inbox items from 13 Oct: FieldAssist contract revision; Sanjiv Bajaj call follow-up. Still open?

## Go-aheads (23 Oct)
- Done 23 Oct: the follow-up fix (d-sel23) is live, and the duplicate Pranav Activity is in Trash.
- Still to come: your yes on the message identity fix (d-msgid23), then on the invite rules (d-invites, decisions 400, 403, 406), each after Cleanup accepts it.
