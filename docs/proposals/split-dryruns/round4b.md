# Round 4b: crash recovery under the hold rule (27 Oct, about 00:30 JST)

Two independent offline runs, A and B. Nothing was sent or written.

**Inputs:**
- Prompts: FAST d710353e5afc67fc and SLOW c3d1616659c8a686 (d-split26p, c78d8b9).
- Snapshot: 3537b3e5c7ca55de.
- Scenarios: round4b/scenarios.json (a5435613e4be70aa).

Outputs are in round4b/.

| Scenario | A | B | Outcome both runs gave |
|---|---|---|---|
| I1 lock + crash recovery | PASS | PASS | FAST at 11:38 waits until SLOW's crashed record turns 60, closes it as Failed, and has nothing of its own on the row. SLOW at 16:50 finds the one unlogged send, logs it once and sends nothing. One Activity; Chase step 1; Next date 3 Nov |
| I3 recovery + duplicate prevention | **FAIL** | **FAIL** | Nothing is resent. But the unlogged reply is never logged: FAST's STEP 1 takes only unanswered threads, and this one was answered. FAST's own crashed record also stays Started for good, because each run reads only the other kind's record |
| I4 two candidates, window expired | PASS | PASS | Both actions are held for Akshay, naming both candidates. Nothing is logged or resent |

**Findings, fixed in d-split26q:**
1. **I3:** each run now reads its Sent for the last 24 hours. Any message from us that no Activity holds goes through the recovery check, and the inbound it answers is logged too.
2. **I3:** a run now closes its own kind's earlier record as Failed when it is 60 minutes old or more.
3. **I4 (both runs):** the content test could be read before the candidate count, find no match and resend. Candidates are now counted first. Content only excludes a mail that plainly does something else. The check runs before any hold rule.
4. **I1 (A):** a follow-up counted mail to that person on any thread, so a PR handling two guests made a false hold. Candidates now come only from the action's thread.
5. **I4 (both):** there is now one hold per candidate set, shared by the actions it holds, and a held action is skipped while that ask is open. Akshay gets one ask, and later runs don't re-add it.
6. **Both:** "Action key only after a send receipt" conflicted with recovery's match. It now reads "after a send receipt or a match above".

**Not fixed (noted):**
- The seq key's due date is ambiguous once holds have moved Next date (B). The match came out the same either way.
- WRITE PATH can take an old date from a legacy segment's text (B).
- Both are existing behaviour outside the crash path.

**Re-freeze:** FAST 38,233 / 3da29ae693347239, SLOW 65,297 / 0464082b0360545a. Each was built twice and is identical. SLOW has 39 B of headroom: the next change needs cuts, or rules moved to a Controls page (phase 8).

Round 4c re-runs I1, I3 and I4 twice on this build.
