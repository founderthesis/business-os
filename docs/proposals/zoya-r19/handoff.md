# Zoya r19: Claude note data loss on the 17:08 SLOW run (CTO, 4 Nov 17:40)

r19 is built on r18. **Command:** `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 95c4e79667baeb2d276211dcef0241cc3b15c971`, with `build_one.patch` at f70901f. Built twice, byte-identical, no em dashes.

| File | Bytes / sha256 |
|---|---|
| `zoya-slow-work.txt` (pinned SLOW file) | 82,109 / c4fd78d6828640fb (82,105 characters), at 95c4e79 |
| `zoya-slow.txt` (Zoya SLOW task) | 13,451 / 8c8765db87178fa5 |
| `zoya-one.txt` (hourly) | 55,192 / ee8f196655999a7a |
| `zoya-episodes.txt` (not live) | 45,698 / 3fa79d6fd1f8f0e2 |

## Changes (only these)

1. **CLAUDE NOTE WRITES:** a new shared HARD rule, so the hourly, SLOW and episodes prompts all carry it.
   - Read the row's **whole** Claude note first: a page fetch or rows mode, never an SQL value, a preview or any slice.
   - Put one dated line at the top and keep every older line.
   - Check in a Bash python step that the new length is at least the old length plus the new line's.
   - A failed check writes nothing, and the item is unfinished ("note check failed").
   - Never rewrite or shorten a Claude note.
2. **Outcome evidence on every outcome, not just completed:** held, blocked and overtaken lines also carry `note:<row id> <date>` from a read-back, and the python checks it. A miss makes the item unfinished. That's the S21 to S28 gap.
3. **Order:**
   - **SLOW FILE:** it's fetched only after the run record's Started write is confirmed.
   - **Chunks:** worked in S-number order, never one out of order (S15 ran after S16 and S17).

## The one-time reconcile of S21 to S28

The 8 rows need one dated note line each. **Not done by this session:**
- It's a Notion write, and this session makes none without Akshay's go-ahead given here.
- The outcomes live in the run record, which the CTO has.

**The CTO, as the one Notion writer:** after 17:45 JST, do a full read, prepend one line each, and repeat no action.

**Status:** built, not replayed. For Cleanup. Nothing is deployed, and the pin ref hasn't moved.
