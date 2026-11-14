# Frozen replays, round 1 (split26h, snapshot 26 Oct 16:23 JST)

Two independent offline runs, run1 and run2, used the same snapshot, the same migration file (sha256 d837edb33231084f) and the same prompts (FAST e8e94fc6c3afb3ff, SLOW 3a7dd1590f30770f). Both gave PASS on C, G, H, D and E.

Comparison on decision fields only. Free text, rule quotes and field labels are left out.

| Replay | Keys | Row outcomes | Next dates | Mails (key, to, cc, thread) |
| --- | --- | --- | --- | --- |
| C contact holds | same | same | same | same (Ronit step 1, reply on our 18 Oct mail, To Payal, Cc Akshay) |
| H overlap | same | same | differ on Akshat | same |
| G same minute | differ | differ | differ | Jheel next-steps mail: same to and cc |
| D caps | differ (placeholder ids) | same pattern: 39 sent, 6 left | differ on Akshat | same pattern |
| E several asks | differ | differ | same where both acted | Jheel reply -1: same to and cc |

The differences have two causes:
1. **The inputs weren't fully frozen.** The hypothetical inbound mails had no fixed Message-ID, so each run invented one. Run2 also ran G and E on every snapshot row, not just Akshat's. This was the test's fault, not the prompt's. Round 2 fixes the ids and scope in `scenarios.json`.
2. **One real ambiguity (H and D).** Run1 recomputed Akshat's Next date on a write that left Next action alone (the owner-mail line); run2 didn't. Fixed by d-split26i: a write that changes Next action sets Next date to the earliest open segment date, and any other write leaves Next date as it is.
