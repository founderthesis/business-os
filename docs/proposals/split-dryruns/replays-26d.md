# Scenario replays on split26d, 26 Oct (read-only)

This run used build split26d (FAST 34,671 / 673d026804db698d, SLOW 64,413 / 90a893c929f453d4). It assumed the keying migration had run and that the Activities database has an "Action key" property. Real rows were used where possible.

| Scenario | Verdict | Note |
| --- | --- | --- |
| A retries (Subodh) | PASS | One Activity, key unchanged. MCP Emails accepts idempotency_key on both email_compose and the draft send. |
| B concurrent asks (Akshat) | PASS | SLOW keys the follow-up without a Zoya segment. The two runs produce different keys. Both runs set Next date to the earliest open segment, legacy date forms included. |
| C contact holds | PARTIAL FAIL | Amit and Ronit pass. Vijay is classed as a skip, a hold and a block by three different sentences, and the owner named (Chaandini) is wrong for Founder Thesis. |
| D capped leftovers | PASS | A cap is never a hold, and every part of the prompt now says so. "At most 10" was ambiguous. |
| E one inbound, several asks | PASS | The order of the -1/-2 suffixes was undefined. STEP 1e still read as a whole-row rewrite. |
| F holding reply (Mekin) | PASS | FAST had no rule for a reply waiting on a host's pick. |
| G same minute | FAIL | The billing ask could be sent twice, once by each run. Vendor Your call steps were typed as decision by FAST but team by SLOW. |

Other findings:
- Intro run times were flagged as wrong; checked against zoya-split-build.md, they are right.
- AFTER SEND wrote the next step without its key.
- WRITE PATH ignored the snooze exception for Next date.

d-split26e fixes every finding in the prompt text. Rule 5 of the migration spec now sends vendor Your call steps to team.

Not fixable in the prompt text alone:
- Notion has no conditional write, so the re-read-and-restore rule narrows the race between the two runs but can't close it.
- Live rows to fix at launch:
  - Vijay: Waiting on is empty.
  - Mekin: no Next date.
  - Akshat: Next date 2 Nov, but his earliest open date is 29 Oct.
