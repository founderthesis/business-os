# r23: capture Message-IDs and the Zoya lock release retry

Main, 7 Nov. These are the CTO's two Codex audit items from 18:40 JST. r23 is built on the r22 builds and deploys **after** tonight's r22 window. Nothing here touches r22. Nothing is deployed, no ref is moved, and nothing was written to Notion.

## 1. Capture: the Message-ID from RAW, in code

**What went wrong.** The 7 Nov 07:02 run pended 109791 (Jaya's October invoice), 109797 and 109801 because no Message-ID came out.
- When `email_read original` came back inline, the old path asked the model to copy the first 4,000 characters of base64 into a heredoc and grep the decoded output.
- That's a hand copy, so it can go wrong, and an attachment-heavy message can need more than 3 chunks.

**Fix (MAILBOX, RAWID).** One Bash python step, written out in full in the prompt, takes the `message_id` exactly as it was passed. It reads the saved result file, or with none, this run's own transcript (the newest `~/.claude/projects/*/*.jsonl`, where an inline tool result is already written by the next call; I checked that here). It then:
- finds the result whose `message_id` matches;
- decodes all of the base64;
- checks it against the result's `sha256`;
- parses the headers with Python's email parser and prints the Message-ID, or "NONE <why>".

If it prints NONE, the run fetches the original once more and runs RAWID again. Still NONE: the message is pended.

The HEADER Message-ID check that the id returns this same message stays as it is. "RAW by HEAD" now reads "RAW by RAWID" in all three places.

**Tested here, read-only** on message 108971 from this session:
- inline, read from the transcript: id found;
- the raw saved result: id found;
- the result wrapped as `[{"type":"text",...}]`: id found;
- base64 tampered with: "NONE sha256 mismatch";
- an id that isn't in the transcript: "NONE no result".

The script pulled out of the built prompt is byte-identical to the one tested.

**Pending across cursor moves.**
- The retry at the start no longer just checks whether a pending message got logged. A pending `mcp:` or `adid:` message is now worked again this run, before new mail and inside the cap: read by its id, RAWID, then STEPS 2 to 7.
- The pending line is built by a Bash python step from the previous line, this run's ledger and the messages at or before "read to". Every message the run left unlogged goes on it, whatever the reason: RAWID NONE, the attachment cap, a quota, rate-limit or 5xx error, any other error. A message leaves the line only when it's logged or noise.
- Messages held back by the 50 KB attachment cap now wait on the pending line. Before, they weren't pending, so the cursor could pass them.

## 2. Zoya lock: a release retry that re-reads first

The 6 Nov SLOW release was rejected five times and needed a manual release. RELEASE now says what to do on a non-zero exit or a rejected push:
1. Re-read the lock: `git fetch origin refs/heads/zoya-lock`, then `L=$(git rev-parse FETCH_HEAD)`.
2. L is $R: the release went.
3. L is $H, so the run still holds the lock: push the same $R with the same `--force-with-lease` again, then re-read again. At most 3 pushes in all, each only after a re-read shows $H, and never a new commit-tree.
4. L is anything else, or the fetch fails: touch nothing.
5. Still not released: one line "lock release rejected (<each push's output>)" on the run record, and the CTO frees it with the runbook.

Nothing expires, takes over or forces the lock. The edit applies in the three lock variants (hourly, SLOW task, episodes) and not in the SLOW file, so **the pin stays 8faf930**.

## Builds

Each built twice, byte-identical. The Zoya builds were also rebuilt from a fresh worktree at f70901f with build_one.patch applied. No new em dash.

| Routine | Base | Build | Bytes / sha256 |
|---|---|---|---|
| Inbox capture | r22/capture.txt (a4ac5ae2) | r23/capture.txt | 51,028 / c31d12952ed94852 |
| Zoya hourly | r22 (f366f769) | r23/zoya/zoya-one.txt | 63,387 / 8b0165ba0ae2d839 |
| Zoya SLOW task | r22 (d2253a19) | r23/zoya/zoya-slow.txt (pin 8faf930) | 16,245 / 988433fa745a6f33 |
| Zoya SLOW file | unchanged | routines/zoya/release/zoya-slow-work.txt at 8faf930 | 91,394 / d8ffcafefbb11e7c |
| Zoya episodes (not live) | r22 (aaf08db2) | r23/zoya/zoya-episodes.txt | 50,603 / cd422006fa8b9501 |

**How to build:**
- Capture: `python3 docs/proposals/r23/patch.py cap docs/proposals/r22/capture.txt <out>`.
- Zoya: apply `r23/zoya/build_one.patch` at f70901f. It holds r21_edits.py, r22_edits.py and the new r23_edits.py. Then run `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 8faf93058516e43a35cd534c4a4d8cb8f61b6177`.

**The hourly is 63,387 bytes, about 1,950 under the cap.** The next Zoya round has to cut before it adds.

## For Cleanup

- RAWID depends on the transcript path existing in the routine's container, as it does in this one. If it doesn't, the step prints "NONE no result" and the message pends, so it fails closed and never guesses an id.
- No replay was run on r23.

Deploy after r22 is verified: capture, then the Zoya hourly and SLOW task (the pin is unchanged).
