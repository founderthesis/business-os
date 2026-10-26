# Round 4c: crash recovery after d-split26q (27 Oct, about 01:00 JST)

Two independent offline runs, A and B. Nothing was sent or written.

**Inputs:**
- Prompts: FAST 3da29ae693347239 and SLOW 0464082b0360545a (659c330).
- Snapshot: 3537b3e5c7ca55de.
- Scenarios: round4b/scenarios.json (a5435613e4be70aa).

Outputs are in round4c/.

| Scenario | A | B | Outcome both runs gave |
|---|---|---|---|
| I1 lock + crash recovery | PASS | PASS | One Activity for the unlogged send. No resend. Chase step 1, Next date 3 Nov |
| I3 recovery + duplicate prevention | PASS | PASS | FAST closes its own crashed 10:38 record as Failed. The Sent scan finds the answered reply, logs it and the inbound once, and completes the action. No resend |
| I4 two candidates, window expired | PASS | PASS | Both actions are held under one Akshay segment naming both candidates. Nothing logged or resent; not re-added on later runs |

I3 failed on both runs in round 4b. It passes on both here.

## Found by both runs, fixed in d-split26r

1. **A held candidate could be logged and lose its hold.** The Sent scan's catch-all ("nothing it completes: log it on that row") could log a mail named in an open "can't tell which mail" segment. It would then stop being a candidate, the held follow-up would read as due, and step 1 could go twice. Run A passed I4 only by letting the specific rule win, and run B named it the real risk. Now a mail named in an open "can't tell" segment is left alone.
2. **A send logged without its action key became invisible.** The candidate rule counted only mails "no Activity holds". So a send the scan logged without an Action key no longer showed up, and the step's own check read "none: it is due". Only AFTER SEND stopped a resend. Now an Activity holding a candidate's Message-ID with no Action key still counts as that candidate.

**Bytes:** two wording-only cuts in the same paragraph. The "two Sent copies are one" clause repeated MESSAGE IDENTITY and ACTIONS' own line, and the property name "Action key" was given twice.

**Build:**
- FAST 38,248 / a277f0f9fc4b73e0.
- SLOW 65,312 / 5175f781a9887ad5. That is 24 B under the cap less 200.

Built twice and identical; reproduces from 3dfa2e4 in a clean worktree. Not a release candidate: the CTO will name the architecture, then one final build is made and every affected test re-run on it.

## Noted, not fixed (not on the crash path, or not in scope)

- **A crash recovery doesn't add missing Cc's.** The recovered revenue mail in I3 lacked Jaya and Sarika, and recovery can't fix a sent mail. Report-only would be new scope.
- **One crash costs SLOW its whole slot** (I3): it waits 25 minutes and ends Partial. This belongs to the architecture question.
- **The edit rule can fight a shared hold.** WRITE PATH's "only this action's own segment" against SLOW joining FAST's hold segment: both runs joined it anyway.
- **The hold asks Akshay to settle a data question.** That is accepted by decision 414, which overrides decision 90 for this case.
