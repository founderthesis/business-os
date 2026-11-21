# Cleanup re-verify: r22 at d93eeae (decisions 496, 497), and the paas-move plan 721dc6f2

Cleanup session, 6 Nov 2026, about 21:00 JST. Read-only. Nothing deployed.

## Builds: all reproduced twice, byte-identical, each equal to the commit

| Routine | Build | Bytes / sha256 | Since 4d7fb84 |
|---|---|---|---|
| Calendar sync | r22/calendar.txt | 62,470 / fb003b475adbd402 | 497 |
| Daily sweep | r22/sweep.txt | 46,451 / ba5cedefb895dd32 | unchanged |
| Inbox capture | r22/capture.txt | 49,350 / bf80bfe26d78c331 | unchanged |
| Inbox actions | r22/actions.txt | 47,673 / 7597b95f766b12b9 | 496 (2b) |
| WhatsApp | r22/whatsapp.txt | 30,220 / aa845019f55fcaa5 | unchanged |
| Zoya hourly | r22/zoya/zoya-one.txt | 62,955 / f366f769a799e92d | 496, 497 |
| Zoya SLOW task | r22/zoya/zoya-slow.txt (pin 8ffa546) | 15,813 / 8d44d20383c7725c | pin and hash |
| Zoya SLOW file | zoya-slow-work.txt at 8ffa546 | 91,041 / c3ef581ab3972bad (91,037 characters) | 496, 497 |
| Zoya episodes (not live) | r22/zoya/zoya-episodes.txt | 50,171 / aaf08db2321ca288 | |

No em dash was added; the sweep's one is in the live base.

## What changed, reviewed: accepted

- **496, Zoya:** no PaaS mail from any inbox. The as-Akshay ladder and gate are gone, and so is the ad@ line in the HARD rule, so decision 420 stands as it was.
  - The hourly puts each inbound on Akshay's list once per Message-ID, with no holding reply.
  - SLOW PAAS REMINDERS work from metadata only. Each writes one segment, "Akshay: follow up <first name> (...)", and never a second while one is open.
  - Each reminder has its key on a Claude note line, a "blocked ... ; Akshay" outcome line with note: and chk:, and stays outside the caps.
  - The old "migration segment is no hold" sentence is gone.
- **496, inbox actions 2b:** any mail of Akshay's to that person on that thread takes the reminder out, and the next one counts from his mail.
- **497, calendar 3b and Zoya:**
  - Human by Design's day-before note goes from Zoya, like the other shows. The Akshay draft path and its "signed Akshay" line are removed, and Chaandini is in the house copies on Human by Design.
  - {call link} is fscd.ai/studio, it's recognised as a recording link, and Zoya allows it only for recording mails and the recording invite.
  - It's on CLAUDE.md's list (fef9d85).

## Still not in: my two r22 conditions

Both files are byte-identical to the builds the conditions were written on, so the same replacements and hashes still hold.

- **C1, WhatsApp 0w:** "an Indian 10-digit number with 91 in front" is still there. Deploy **30,378 / f93f47f9f674dbe7** (the replacement in cleanup-verdict.md), not aa845019.
- **C2, sweep 3a4 b:** the relink still doesn't keep other links. Deploy **46,569 / 513e1a2acb1a6c9b**, not ba5cedef.

## Deploy hashes (r22, with C1 and C2)

- calendar fb003b47
- capture bf80bfe2
- actions 7597b95f, with section 6
- WhatsApp f93f47f9
- Zoya pin 8ffa546, then hourly f366f769 and SLOW task 8d44d203
- sweep 513e1a2a last

Read each back byte for byte.

## paas-move (plan 721dc6f2): still not ready to run

- **C1, the guard: not met.** Five routines still have no PaaS guard line: **calendar, sweep, inbox actions, inbox capture, WhatsApp**. Only Zoya (hourly and SLOW) has one. Actions mentions PaaS only in the 2b reminder clear and its decision 156 Deals note, and WhatsApp only in its People tag list.

  The move can't run until each of the five carries both lines and is live:
  - "Engagements on Show PaaS are production-service rows: no guest step, eval, chase, status change or flag by guest rules; mail on them is logged and anything it asks goes to Akshay's list."
  - "A Deal whose Next action starts 'Moved to Engagements' is retired: never flag, update or link to it; use its Engagement."

  Adding them to this round's builds before deploy is the quickest path.
- **C2, the relink: not met.** Nothing in plan.json, the README or the script changed. The write step still says only "add the Engagement to each listed Activity", and verify still checks only that the new id is present. Before the write:
  - say: read each Activity's Engagement relation, write back old plus new, read back;
  - snapshot those relations first, and have verify assert every old link is still there.
- **C3, the segment: mostly met.**
  - **What's right:** the "Zoya waits for the templates" segment is gone. Each row starts with the Deal's own Next action and Waiting on, Mamatha is dropped, and an open row with neither gets "Akshay: next step for <company>?".
  - **What's left, should-fix:**
    - 15 of the 33 carried steps have no owner at the front, such as "Chase after their episode goes live" or "Pitch PaaS to Sameet Gupte ...". With Akshay in Waiting on they show on his list as loose notes. The sweep's 3a owner rewrite covers only Founder Thesis rows, so nothing fixes them later.
    - 7 run past about 120 characters, up to 471 on Field Assist (B12).
    - Two are stale sweep flags from 26 Oct ("New, untouched 14+ days ... | was: ...").
    - One Parked row keeps Akshay in Waiting on ("sent via mail, set up recording").

    The fix belongs in the script:
    - put the Waiting on owner in front ("Akshay: ...", "Waiting on <name>: ...");
    - cut each step to about 120 characters (the whole text is already in the Claude note and page body);
    - drop "untouched 14+ days" flags in favour of the "was:" step;
    - leave Waiting on empty on Parked and Unresponsive rows.
