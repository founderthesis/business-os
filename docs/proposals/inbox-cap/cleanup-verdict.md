# Cleanup: inbox per-run cap (f6b1f19, on the branch at 8625b3d)

**Verdict: ACCEPTED. Inbox 65,325 B, sha256 e6cf4db2bc37918b.**

## Reproduced

`patch.py` on the live inbox gives 65,325 / e6cf4db2bc37918b. Built twice, byte-identical to `docs/proposals/inbox-cap/inbox.txt`, with 11 B under the build limit.

The live inbox was read from trig_0189eZvAD8x4357cfevgZ3No just now: 65,336 / 403f49ac840dc31b, enabled, updated 29 Oct 22:55Z, last fired 23:02Z.

## The four checks

1. **Oldest first, up to the cap: yes.** The new rule is "work them oldest received first, at most 15 not yet logged a run (then Partial); the rest wait for the next run (not pending)".
2. **read to only past messages logged or skipped as noise: yes, unchanged.** "the newest received time up to which every message was logged or skipped as noise, never past a pending one". Messages the cap doesn't reach sit after read to, and the next run's T (read to minus 30 minutes) covers them.
3. **Never 0 logged when real messages exist: yes.** "A backlog never means working none." No refusal wording ("too large", "one run can") exists in the base or the build.
4. **WRITES and IDENTITY unchanged from 403f49ac: yes.**
   - The WRITES line, the IDENTITY `original` gate, the pending retry and the "read to" definition are byte-for-byte as in 403f49ac.
   - The other edits only trim explanations: three parentheticals, and the shorter unclear-create wording, which keeps "query that Source ID first; never a second row".

## Replay on the real window, read-only

The cursor is at 12:00Z, so T = 11:30Z. Run as an MCP Emails search on ad@, metadata only, with no flags touched. It returned 148 messages since 29 Oct: 100 on page 1, and page 2 is all before T. **57 arrived at or after T.**

Three runs in sequence were simulated under the build's rules. Noise means calendar replies, SaaS notices and newsletters, and Zoya's own mail counts as already logged by her. That classification is a heuristic, so the counts are approximate.

| Run | T | Window | Logged | First to last | read to after |
|---|---|---|---|---|---|
| 1 | 11:30Z | 57 | 15 | 11:44 to 13:06 | 13:06 |
| 2 | 12:36Z | 50 | 15 | 13:07 to 22:40 (the overlap re-read is skipped as logged) | 22:42 |
| 3 | 22:12Z | 18 | 4 | 22:47 to 23:24 | 23:47 |

The backlog clears in 3 runs. No run logs 0, nothing is skipped, and nothing is logged twice: the 30-minute overlap is covered by the msgid dedupe. Same-minute messages at a cap boundary (12:52, 23:47) fall inside the next run's overlap.

## Follow-ups (not blocking)

- Whether pending retries count toward the 15 isn't stated. Either way works.
- At 11 B of headroom, the next inbox change has to cut text first.

Checks:
- Less text and fewer writers: -11 B, no new writer.
- Selection by prefix or wording: none.
- Retry double-write: unchanged.
- Bytes and hashes: above.
