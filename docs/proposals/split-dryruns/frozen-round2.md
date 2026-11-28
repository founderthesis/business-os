# Frozen replays, round 2 (split26i, pinned inputs)

Two independent offline runs, A and B. Each used the same snapshot (sha256 3537b3e5c7ca55de) and the same migration file (d837edb33231084f). Both took their scenario scope and inbound Message-IDs from scenarios.json (495a699ead3a5229). Prompts: FAST 0895fe8d05fdd737, SLOW f4b432c126696eb3.

| Replay | Keys | Outcomes | Next date | Waiting on | Next action | Mails | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C contact holds | A listed fewer | same | same | same | Ronit differs | same | PASS, PASS |
| G same minute | same | same | same | same | same | same | FAIL, FAIL |
| H overlap | same | same | same | same | same | same | PASS, PASS |
| D caps | B also listed next-step keys | same | 4 rows: 2 Nov vs 3 Nov | same | same dates as Next date | same | PASS, PASS |
| E several asks | same | same | same | same | wording only | Cc wording only | PASS, PASS |

**Findings fixed in d-split26j:**
- **G: lease deadlock.** Both runs wrote Started at 10:08, so each held the lease against the other. FAST gave up after 10 minutes and the reply went 40 minutes late. Fix: the earlier start holds the lease, and FAST holds it when both start in the same minute.
- **C: Ronit's old waiting segment.** One run kept "Waiting on Payal: reply to the commercials" next to SLOW's new keyed step 2; the other replaced it. Fix: SLOW's self-keyed segment replaces the row's waiting segment for the same ask.

**D: the test's fault.** The scenario gave no offer date, so step 2's due date was ambiguous (offer + 14 vs step 1 + 7). Round 3 pins it.

**A and B both listed:**
- Akshat's 29 Oct and 2 Nov segments, each acted on its own date.
- Each run took only its own parts under the lease.
