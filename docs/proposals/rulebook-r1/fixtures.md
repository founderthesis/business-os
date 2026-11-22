# Rulebook r1: offline replay fixtures

Each case is a situation, the staged text that decides it, and the expected outcome. Checked by reading the staged files, with no live sends. "Pass" means the staged text leads to exactly one outcome and nothing in it points the other way. Batch 2 adds runnable checks for RECIPIENTS.

| ID | Situation | Deciding text | Expected | Batch 1 check |
|---|---|---|---|---|
| F01 | FT sponsored offer sent 9 days ago; their side silent | follow-ups 5c; SLOW work routine 1 | No mail. Any "Zoya: sponsored step" segment dropped, Waiting on Guest or PR. Status unchanged. | Pass |
| F02 | FT sponsored offer; their side asks "what are the fees?" on day 3; Zoya answers; one chase already went from ad@ before the interest rule | 5c rows "After interest" and "What counts" | Answer from the wording page; then at most 1 more follow-up (the ad@ chase counts toward 2) | Pass (timing: question 2) |
| F03 | un# offer; they write "we'll get back to you when ready" | pause table | Nothing for 30 days, one check-in, then nothing; row on Park proposals | Pass |
| F04 | Rule ends a FT sponsored chase after follow-up 2, no reply; Akshay has said nothing | PARKED; 5c "Stop: no reply" | Status unchanged, no send, row added to Saturday's Park proposals | Pass |
| F05 | Akshay writes "park" in Your call on that row | PARKED; zoya-day "Akshay's calls" | Status Parked, his segment cleared | Pass |
| F06 | un# reply; latest message From the guest, Cc Sri (Sri never wrote) | RECIPIENTS 1/ | Sri stays in Cc; Akshay added in Cc; Zoya not on it | Pass |
| F07 | Task allocation mail to Sarika only | RECIPIENTS 3/ | To Sarika; no Akshay; no Mamatha | Pass |
| F08 | Latest message has a bounced address and Ravi's dead mailbox | RECIPIENTS 1/ | Both removed; everyone else kept; check passes | Pass |
| F09 | FT row reaches Booking, no room link anywhere | FAST ROOM ASK | One WhatsApp to Ranjita listing it; "Ranjita: create <guest>'s Zencastr room..." with Ranjita in Waiting on; reminder after 2 days | Pass |
| F10 | FT recording happened yesterday, no Transcript file | SLOW work TRANSCRIPT ASKS; zoya-day 644 duty | "Ranjita: download ... attach it" segment plus one WhatsApp; chase once after 2 days; then Akshay's list | Pass |
| F11 | A billing invoice arrives in ad@ | Sender table | Forwarded to Jaya through MCP Emails | Fail: no current owner since the sweep retired (S6). Batch 2 |
| F12 | Thread not in Zoya's inbox; a follow-up is due | FAST SENDING loop-in; sender table | ad@ loop-in by email_compose reply, To and Cc passed and checked; never the draft tool on ad@ | Pass |
| F13 | Calendar run finds a guest-cancelled recording | calendar STEP (cancel) | No delete_event; "Akshay: delete ... (blocked: auto mode)" on the row; message to the CTO session | Pass |
| F14 | First wake after cutover | zoya-day.md | No Saman reply and no Zoya date backfill run (both one-offs gone) | Pass, pending S8 verification |
| F15 | Weekday 14:08 JST | zoya-day table; zoya-slow.txt | No SLOW composer (slots are 11:08 and 17:08) | Pass |
| F16 | FT guest asks for the release date; Planned release set, not confirmed | release-date table | "Next steps and release date", no date | Pass |
| F17 | Sarika confirms the FT date in Zoya <> Team | zoya-day release duty | Planned release set, group reply, release workflow starts from the step the date calls for | Pass |
| F18 | New FT recording, eval says Book immediately, no precall yet | zoya-day 654 duty; SLOW work routine 3 | Precall invite (podm.in/30min), never podm.in/book | Pass in staged files; Fail in cowork-evals.md and skills until batch 2 (S13) |
| F19 | Weekday wake: every authorised SLOW slot | zoya-day table | SLOW composer at 11:08 and 17:08 only | Pass |
