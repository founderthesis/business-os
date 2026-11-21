# Cleanup re-check: Zoya r15c and capture r12e (b732cb3, bc50317), 3 Nov ~22:45 JST

**Accepted. No blocker.** This is the last gate, and it's clear. Deploy:

| Build | File | Bytes / sha256 |
|---|---|---|
| Actions r11b | (unchanged, accepted in `cleanup-verdict.md`) | 46,112 / 07832eb6 |
| Zoya A (FAST) | `zoya-r15/zoya-one.txt` | 53,152 / e2a016c50140abc4 |
| Zoya B (SLOW task) | `zoya-r15/zoya-slow.txt` | 12,515 / ce54c367b7c72390 |
| SLOW file | at b732cb3c663681cb80736d696de2201bf8ce5e38 | 77,925 / d2955ae3ba0e2e0d |
| Capture r12e | `inbox-split/capture-r12/capture.txt` | 46,565 / 9caf2cdba8a63698 |

## Rebuild

- **Zoya:** a worktree at f70901f with `zoya-r15/build_one.patch`, then `build_one.py <dir> refs/heads/zoya-slow-pin b732cb3c663681cb80736d696de2201bf8ce5e38`, twice. All three files are byte-identical to the repo, and the SLOW file equals `git show b732cb3:...`.
- **Capture:** `capture-r12/patch.py` on the live base, `inbox-split/r11/capture.txt` (043dbe3a), twice. Byte-identical.
- There are no em-dashes.
- **The pin** is at 63fcf669. b732cb3 descends from 251388d, which descends from 63fcf669.

## The diff against r15b and r12d holds only these changes

**Z1: closed.** LEAK CHECK now runs "on the text you write, and on the gmail_quote and MCP's plain-text quote with every nested part, unless every recipient outside the team was on the quoted message's own From, To or Cc (decision 452); a quote that fails goes, with the mail, to Akshay's list unsent".
- zoya-one.txt line 105;
- zoya-slow-work.txt line 151;
- the zoya-slow.txt copy.

**Z2: closed.** Both rules now carry "(the gmail_quote and MCP's plain-text quote aside)":
- "Never a link ...": zoya-one.txt 104, zoya-slow-work.txt 150;
- SHOW CHECK: zoya-one.txt 106, zoya-slow-work.txt 152.

**C1: closed.** "only the innermost message from outside the team, with every forward layer and every note by Akshay, Saurabh or anyone tagged Team removed; unsure: no quote", in capture-r12 line 5.

**(b): closed.** zoya-slow-work.txt 66 says "Only in a team hour as Cadences gives it (none there: never before 09:00 or after 20:00 IST, so the 08:08 JST run, 04:38 IST, sends none)". Line 72 says "team WhatsApp waits for a team hour".

## Akshay's four points

1. **PREFLIGHT** (zoya-slow.txt line 1): it exits before any business read or send. When the message is exactly "PREFLIGHT", it:
   - takes the lock and loads the tools;
   - makes one read-only call per connector that reads no business row (folder_list, the Activities data source fetch, list_calendars, a Blueticks chats call that sends nothing);
   - checks the repo origin and the SLOW file's fetch and sha256 ("no load past the hash"), and the model;
   - writes one "Preflight" record, then RELEASE and stop: "no RULES LOAD, no selection, no business read, nothing sent".
2. **Metadata-first selection** (zoya-slow-work.txt line 82): the list is "found from metadata only: SQL on Engagements ... and Activities ..., never a thread or page read to build the list; full context ... is read only for the selected items, one at a time, with each outcome saved in its chunk".
3. **Crash recovery** (zoya-slow-work.txt line 83): "before redoing a carried key, check it as ACTIONS' Sent check does (your Sent and ad@'s Sent since the earlier run's start, and an Activity holding that Action key): a match is 'completed match <Message-ID>' ..., logged 'recovered: S<nn> <key>', and is never sent again".
4. **Lock behaviour.**
   - zoya-slow.txt line 1: "A held lock means an immediate Skipped record and stop: no wait, no retry, no takeover".
   - Line 8: "Write only the run record ... Skipped: lock held by ... and stop".
   - Lines 9 and 10: `--force-with-lease` against the sha that was read.
   - Line 11: "never a "+" refspec or --force". The only other "+" is in the ToolSearch names (line 3).

## Gates and order (as the CTO set them)

- **D2:** settled read-only (Drafts:322 became 323 through draft update and kept its HTML; sent as Sent Mail:849).
- **Cadences:** read back the Diwali line and the FAST reserve before enabling B. The pause starts Fri 6 Nov.
- **Order, all in one window:**
  1. actions r11b;
  2. FAST A;
  3. move the pin to b732cb3 and read back d2955ae3;
  4. fire B with "PREFLIGHT" by hand and check its Preflight record;
  5. enable B;
  6. capture r12e (independent).
  - Read each prompt back byte for byte.

**The should-fix items in `cleanup-verdict.md` remain follow-ups.** The two that matter most:
- a run whose outcome check printed nothing must be Failed;
- check the time before each item, not only each chunk.

Nothing deployed by Cleanup.
