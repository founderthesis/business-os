# Rulebook r1: Monday 23 Nov checks

The CTO runs these against Monday's natural runs. Never fire, resend or redo anything to prove a check. A failed check is a finding for the CTO round; the rollback is in docs/deploys/rulebook-r1-cutover.md.

Day chat: session_019pwcV3YCMEek9acNBYwJAU (tag zoya-day). Weekday wakes at 07:38, 09:38, 11:38, 13:38 and so on, every 2 hours to 23:38 JST. A prompt runs at the first wake at or after its slot.

Release values to check against:
- RELEASE: d2c73732a0b5a131bf78e0eea685ff416c4b4614
- SLOW work file: 48d056527f0bddb06059b8720ec404a5b3d187fd:docs/proposals/rulebook-r1/prompts/zoya-slow-work.txt, sha256 starting 594fbbddeda9044b

## 1. First wake, 07:38 JST

1. In the day chat's transcript (list_events, kinds ["assistant","user"]), it reads the routine prompts with `git show d2c7373...:docs/proposals/rulebook-r1/prompts/<file>`. It never reads them from the working tree, and never from 83e8fb0 or docs/proposals/zoya-day/prompts.
2. RULES GATE: Rules for Zoya, Mail and WhatsApp wording, Cadences and Client show mails are each read in full (each read equals its total) before any send. Pass: no send or draft tool call (MCP Emails email_compose, draft, Gmail create_draft or reply, Blueticks send, calendar create_event) appears before the fourth full read.
3. Run record "Run zoya-day 2026-11-23 07:38 JST: <Completed|Partial|Failed>" in Activities. A Partial or Failed status must give a reason.
4. The day chat starts the capture composer (title "Capture 2026-11-23 07:38 JST", tags ["zoya-oneshot"], model claude-sonnet-5-5). Its report reaches the day chat by send_message. The run record "Run inbox capture 2026-11-23 07:38 JST: <status>, read to <ISO>" exists, and the capture composer made no send or draft call.

## 2. Capture loop-ins

For each "loop-in due: <row>, <name>, <Message-ID>" line in the capture report:
1. The day chat sends it after the capture report and before inbox actions, from ad@thepodium.in (inbox cd37e47e) with MCP Emails email_compose action reply, idempotency_key "loopin:<Message-ID>". It never uses the MCP Emails draft tool on ad@.
2. The Bash RECIPIENTS check ran on the To and Cc before the call.
3. Sent read-back: an email_read of ad@'s Sent copy, with a Bash assert on its To and Cc and that In-Reply-To equals the Message-ID.
4. In ad@ Sent: exactly one loop-in on that thread. To is the person whose move it is, Zoya is in Cc, ad@ is not in To or Cc, there is no link, and the mail threads under the original.
5. Activity "Zoya sent: Zoya loop-in to <name>" on the row. None goes on a Parked, We declined, They declined or Unresponsive row, or where Zoya was already on the latest message.
6. No loop-in due: record that, and that nothing went from ad@ apart from the allowed forwards.

## 3. SLOW, 11:08 slot (runs at the 11:38 wake)

1. The SLOW composer starts with title "Zoya SLOW 2026-11-23 11:38 JST" (the wake time), tags ["zoya-oneshot"], model claude-opus-5-5.
2. Its transcript shows `git show 48d0565...:docs/proposals/rulebook-r1/prompts/zoya-slow-work.txt`, with a sha256 starting 594fbbddeda9044b. A mismatch must mean "do no SLOW", with that said in the record.
3. Run record "Run zoya-slow 2026-11-23 ... JST: <status>". Its body carries the work-file hash, and STEP 0g's six MONDAY NUMBERS lines: follow-ups due and sent, sponsored moved and won, tier 1 booked, stuck, next, share rate.
4. No scorecard or numbers mail to Akshay anywhere (Zoya's Sent, ad@ Sent).
5. The composer drafts only. Every send comes from the day chat's OUTBOX, after the RULES GATE, with RECIPIENTS checked.
6. The 17:08 slot runs at the 17:38 wake. It must not write MONDAY NUMBERS a second time.

## 4. Upkeep, first weekday wake at or after 13:00 (the 13:38 wake)

1. Its transcript shows `git show d2c7373...:docs/proposals/rulebook-r1/prompts/upkeep.txt`.
2. Record "Upkeep 23 Nov: <Completed|Partial|Failed>", with its report covering:
   - client pre-release drafts (Gmail drafts in ad@ only, never sent);
   - the guests list;
   - the FT Community backstop;
   - BD prospect episodes;
   - quiet-row flags;
   - billing forwards to Jaya (MCP Emails forward, the only send);
   - guest form merges;
   - Mail issues fix checks.
3. No daily-sweep run or record anywhere (decision 657).

## 5. Scheduled tasks

1. Host boards (trig_01K8bueCr2xsPkbgQzjeRKsz), 08:15 JST:
   - last_run fired;
   - its report gives per-board counts (created, updated, Not now, host calls pulled, availability copied) with no error;
   - no mail or message sent.
2. Sarika's editing asks, 11:17 IST (trig_01AU4fQevmq39TDZX6LvC4cq; 13:15 is trig_01SXrnWJb2iz5Q3zts34VZu4):
   - the run ends at once with no message, or does parts A, B and C;
   - allocation mails go to team members only, never Akshay in To or Cc;
   - calendar blocks go on Zoya's calendar only.
3. CTO round, 08:45 JST (trig_019sfzEHt9djonNhbxcATgYA): it runs on the new prompt (7,101 bytes, 366fbeaee7d17fb3).

## 6. Whole day

1. No mail, Cc or WhatsApp to Mamatha (Zoya's Sent, ad@ Sent, Blueticks), and no row newly Waiting on Mamatha.
2. No new Status Parked written by an agent (decision 656).
3. No sponsored follow-up to a row with no interest shown (5c).
4. Every Ranjita ask is a "Ranjita: ..." segment, with at most one WhatsApp to her per batch.
5. Each Sent mail has one Activity, and each send-path Activity has a Sent mail: compare Zoya's Sent and ad@ Sent against the day's "Zoya sent:" Activities.
6. Fixtures: compare docs/proposals/rulebook-r1/fixtures.md with what happened, as far as the day's mail allows.
7. After a good Monday: delete docs/proposals/zoya-day/prompts/ in a later commit (the rollback source).
