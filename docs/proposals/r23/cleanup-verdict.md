# Cleanup verdict: r23 at 3647e23 (capture RAWID and pending, Zoya lock release retry)

Cleanup session, 7 Nov 2026, about 19:40 JST. Read-only. Per the CTO, no Notion write while the PaaS move writer is live, so this verdict lives only in this file.

## Verdict: accepted. Deploy after r22 is verified.

### Changed live prompts (each built twice, byte-identical, equal to the commit; no em dash)

| Routine | Base | Build | Bytes / sha256 |
|---|---|---|---|
| Inbox capture | r22 a4ac5ae2 | r23/capture.txt | 51,028 / c31d12952ed94852 |
| Zoya hourly | r22 f366f769 | r23/zoya/zoya-one.txt | 63,387 / 8b0165ba0ae2d839 |
| Zoya SLOW task | r22 d2253a19 | r23/zoya/zoya-slow.txt | 16,245 / 988433fa745a6f33 |

**Unchanged:** the SLOW file at pin 8faf930 (91,394 / d8ffcafe), so the pin doesn't move. Episodes (not live) is 50,603 / cd422006.

The Zoya diff against r22 is only the RELEASE paragraph and the deployment reference line. The capture diff is only patch.py's seven asserted edits, and no "by HEAD" is left.

### 1. Capture RAWID: sound

- **No hand copy.** One Bash python step takes the message_id and reads the saved file, or with none, the run's newest transcript. It decodes the whole base64, checks its sha256 and parses the headers with email.parser. A NONE result triggers one re-fetch, then the message pends.
- **It fails closed.** No result, a sha256 mismatch or no header gives NONE, so the message pends and an id is never guessed. The HEADER Message-ID check that the id returns the same message still follows.
- **Built and tested here.** I pulled the script out of the built prompt; it compiles. On a synthetic transcript it returns the right id.
- **The crafted-mail path is closed in practice.** I tested a mail whose body is a JSON object naming the same message_id with spoofed "data" and no sha256. It isn't picked up. In a transcript the body sits one JSON level deeper, so its `"data"` key is escaped and fails the script's `'"data"' in o` test, and the walk never parses it.

### 2. Pending across cursor moves: sound

- A pending mcp: or adid: message is worked again first, inside the cap: read by its id, RAWID, then STEPS 2 to 7.
- The pending line is built in python from the previous line, the ledger and every message at or before "read to". Every unlogged message stays on it, whatever the reason, including the 50 KB attachment cap, until it's logged or noise.
- This closes the gap where the cursor could pass a message held back by the attachment cap.

### 3. Zoya lock release retry: safe

- On a non-zero exit or a rejection, the run re-reads the lock first.
  - L is $R: it went.
  - L is $H: re-push the same $R with the same `--force-with-lease`, at most 3 pushes, each only after a re-read shows $H. Never a new commit-tree.
  - Anything else, or the fetch fails: touch nothing.
  - Still held: one "lock release rejected" line, then the runbook.
- No "+", no --force, and never a release of a lock the run doesn't hold.
- It's in the hourly, the SLOW task and episodes, and not the SLOW file, which is why the pin stays.

## Should-fix (not blocking)

- **S1. Require the sha256 in RAWID.** `if o.get("sha256") and ...` skips the check when a matched object has no sha256 field. Real `original` results always carry one, so make its absence a NONE. It's one token: `if not o.get("sha256") or hashlib.sha256(b).hexdigest()!=o["sha256"]`.
- **S2. Wait before each re-push.** The three pushes run back to back. The 6 Nov rejections were transient, so a short `sleep 5` before each re-push makes success more likely. The routine's Bash allows it, unlike this session's.
- **S3. RAWID needs the transcript path** (`~/.claude/projects/*/*.jsonl`) to exist in the routine container. If it doesn't, the message pends ("NONE no result"), which is safe but silent. After deploy, check the first capture run's ledger for RAWID ids versus NONE.
- **S4. The hourly is 63,387 bytes, about 1,950 under the cap.** The next Zoya round has to cut before it adds.

## Deploy order

After r22 is verified live:
1. capture c31d1295
2. Zoya hourly 8b0165ba
3. Zoya SLOW task 988433fa (pin unchanged)

Read each back byte for byte.
