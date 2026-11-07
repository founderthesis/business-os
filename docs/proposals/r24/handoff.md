# r24: Zoya's new rows go to evals, Cleanup's r23 should-fixes, the PaaS batch name

Main, 7 Nov. This is the CTO's 20:55 JST list. It's built on the live r23 builds (deploy log docs/deploys/2026-11-07-r23.md). Nothing is deployed, no ref is moved, and nothing was written to Notion. The "caught via Saurabh" WhatsApp line isn't in r24; it waits on Akshay's yes.

## 1. Zoya hourly STEP 1: a row she creates from a pitch goes to evals, not Akshay's list

The Sung Hong un# row put "Akshay: evaluate and decide" on his list. STEP 1 said only "as inbox STEP 3 would create it", which left the owner to the model. It now reads:

> a thread with no Engagement gets one as inbox capture STEP 3 creates it (a pitch: Status New, Waiting on empty, nothing on Akshay's list; the evals routine takes it)

That matches capture's own create rule. Founder Thesis and un# rows get their owner from the evals routine.

**For Cleanup:** capture's rule says the Built to Share and Human by Design owner comes from "STEP 5", but capture has no STEP 5 (its steps go 3, 6, 6a, 6b, 7, 7c, 8). That pointer is already dangling in the live capture prompt, and r24 doesn't change it. Worth a look: say whether the evals routine also covers those two shows, or where that step went.

## 2. Cleanup's r23 should-fixes

- **S1 (capture RAWID):** a result with no sha256 now counts as NONE ("NONE sha256 missing or mismatch"), so every id printed comes from a checksum-checked message. The script pulled out of the build was tested on message 108971:
  - the saved result gave the id;
  - a tampered result gave NONE;
  - the same result with its sha256 removed gave NONE.
- **S2 (lock release):** "sleep 5" comes before each re-push. The rest of the retry is as live: re-read first, the same $R and the same `--force-with-lease`, at most 3 pushes, each only after a re-read shows $H, never a new commit-tree. It's in the hourly, the SLOW task and episodes.
- **S4 (size):** I cut before adding, and the hourly is **62,886 bytes**, under 63,000. Nothing cut is a rule:

| Cut | Where |
|---|---|
| The superseded PaaS citation (the 6 Nov "send follow up as Akshay" quote and the follow-up rules page id; decision 496 replaced both). It now reads "PAAS (decision 496)." | hourly |
| The Samiksha incident story behind "(Akshay, 5 Nov, item 2)" | hourly, SLOW task, episodes |
| The rationale in brackets after "never a + refspec or --force" (the ban stays) | hourly, SLOW task, episodes |
| "(Akshay, 27 Oct: ...)" becomes "(decision 415: one Zoya run at a time, fail-closed)" | hourly, SLOW task, episodes |
| The quotes in the decision 446 and 445 headings (the decision, Akshay and date stay) | hourly (446 also in episodes) |
| Shorter wording in the RELEASE retry | hourly, SLOW task, episodes |

The SLOW file isn't touched, so **the pin stays 8faf930** (91,394 / d8ffcafe). It still carries the old PaaS citation; that can go the next time the pin moves.

## 3. migration/paas_move.py: the batch comes from the date argument

`BATCH` is now "paas-move-%s", filled with the plan's date. The 6 Nov inputs still give plan 5d5f02cd0d57931a, byte-identical to the committed plan.json, so the written move is unaffected. With 2026-11-09, all 33 ops carry "paas-move-2026-11-09".

## Builds

Each was built twice, byte-identical. The Zoya builds were also rebuilt from a fresh worktree at f70901f with build_one.patch applied. No new em dash.

| Routine | Base (live) | Build | Bytes / sha256 |
|---|---|---|---|
| Inbox capture | r23 c31d1295 | r24/capture.txt | 51,042 / 179034c51a3b3b2b |
| Zoya hourly | r23 8b0165ba | r24/zoya/zoya-one.txt | 62,886 / 6a8ae791bd519928 |
| Zoya SLOW task | r23 988433fa | r24/zoya/zoya-slow.txt (pin 8faf930) | 15,949 / 93b32d6877620ef4 |
| Zoya SLOW file | unchanged | routines/zoya/release/zoya-slow-work.txt at 8faf930 | 91,394 / d8ffcafefbb11e7c |
| Zoya episodes (not live) | r23 cd422006 | r24/zoya/zoya-episodes.txt | 50,246 / 8c1fbcb603d61eb3 |

**How to build:**
- Capture: run `python3 docs/proposals/r24/patch.py cap docs/proposals/r23/capture.txt <out>`.
- Zoya: apply `r24/zoya/build_one.patch` at f70901f. It holds r21 to r24 edits. Then run `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 8faf93058516e43a35cd534c4a4d8cb8f61b6177`.

No replay was run on r24.

Deploy order: capture, then the Zoya hourly and SLOW task (the pin is unchanged). Read each back byte for byte.
