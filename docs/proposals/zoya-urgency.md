# Proposal v2.2: urgency-led follow-up for Zoya

Status: draft for Codex review, 22 Oct 2026. Extends the FAST/SLOW split (docs/proposals/zoya-split.md, v2.1, approved for trial; decision 394). It goes live with the split, after the dry runs, Cleanup's review and Akshay's yes. Nothing here touches the live Zoya prompt, which is about 1,000 bytes from the 65,536-byte cap.

## Why

Akshay, 22 Oct: "Zoya's response needs to be according to the urgency of the situation. When it is a situation which needs to be closed today, she should continue to follow up and close it same day, even during the silent period." He also expects an inline instruction in a mail ("@zoya pls share the invite also") to be acted on.

Today's behaviour, measured on 21 and 22 Oct:

1. **Every job waits for the same hourly run and the same cadence.** A call tomorrow and a 30-day chase get the same treatment. Quiet hours (00:30 to 07:30 JST) stop both alike.
2. **An "@Zoya" line inside Akshay's mail isn't a command.** The inbox logs the mail as an Activity. Zoya acts only on Your call, WhatsApp group instructions and queued Next action steps. On 22 Oct, "@Zoya will send the invite" (pi-labs precall, for the next morning) had no path to an invite. Decision 400 now lets Zoya create invites, but nothing makes it happen the same day.

## What

### 1. Urgency on every action

The split already keys every action as `<engagement id>:<type>:<origin>:<raised ISO>`. v2.2 adds one field, `urgency`, set when the action is raised and recomputed each run from facts, never from tone.

| Urgency | When | Examples |
| --- | --- | --- |
| **today** | The action blocks something within 36 hours of now, or Akshay addressed Zoya directly | Invite or link for a call tomorrow; same-day reschedule; a guest waiting on the recording link; any "@Zoya" instruction from Akshay; a confirmation the other side asked for, for a call within 36 hours |
| **soon** | A reply is owed, or Akshay decided | Unanswered substantive ask (v2.1's reply-owed rule); Akshay's decision mail |
| **paced** | Everything else | Follow-up chains, nurture, long-term chases |

The facts used are the next call on the Engagement (Next date, the calendar), dates named in the thread, and the author of the instruction. If the date or time zone is ambiguous, the action stays **today** and Zoya's first step is the clarifying question.

### 2. How each level runs

| | today | soon | paced |
| --- | --- | --- | --- |
| Picked up by | FAST, first in order | FAST | SLOW |
| First action | Next FAST run (within an hour) | Within one working day | Cadences schedule |
| Chase | Every 2 to 3 hours on the same thread, at most 3 a day | As now | Cadences |
| Quiet hours | Recipient's waking hours apply (07:00 to 22:00 in their time zone), not Akshay's | Akshay's | Akshay's |
| Escalation | One post in Akshay's Zoya WhatsApp group if open 3 hours before the deadline, or at 22:00 recipient time | Daily sweep | Daily sweep |

**Akshay is never woken.** He stays in Cc on mail (decision 229), but mail is silent. The WhatsApp escalation for a today action between 00:30 and 07:30 JST is held until 07:30 JST, unless the deadline falls before 09:00 JST.

### 3. Overnight FAST runs

FAST today runs 07:30 to 23:30 JST. v2.2 adds runs at 01:30, 03:30 and 05:30 JST (hourly, if Codex judges the gap too long). Each run first selects today actions only. If there are none, it ends straight away and writes a one-line run record. The prompt's first step is the selector, so an empty run costs a few tool calls.

### 4. Akshay's "@Zoya" lines are instructions

- **Where:** any mail from ad@thepodium.in with "@Zoya" (or an address line to zoya@myunnati.com) on a thread Zoya can see, plus the WhatsApp "Zoya" group (already the route under decision 304).
- **What:** the sentence addressed to Zoya becomes an action of type `instruction`, origin `msg-<Message-ID>`, urgency today. The inbox raises it when it logs the mail, and FAST also scans for it, so a missed inbox run doesn't lose it.
- **How it's done:** FAST maps it to a known capability, such as send the invite (decision 400), share the invite with named people, send the link, chase, or forward the transcript. It acts, then confirms on the thread in one line, e.g. "invite sent for Fri 23 Oct, 8:30 am IST".
- **Anything else:** if it doesn't map to a capability, or would need something Akshay hasn't approved (a price, a new link, a deletion), it goes to Akshay's queue as "Zoya: couldn't do '<instruction>': <reason>" and his WhatsApp group the same hour. It's never ignored.
- **Loop-ins:** "adding @Zoya to coordinate" is a loop-in, not an instruction (existing rule). It hands her the thread at its normal urgency.

### 5. Safety

- **Same guardrails:** every today send uses v2.1's idempotency key, thread check and matched completion. Urgency changes timing, never the content rules: Rules for Zoya, decisions 392, 395 and 399, the send cap, and one mail per person per run.
- **Chase cap:** the cap of 3 a day for today stops a chase loop. After the third chase, the action escalates and stops mailing.
- **Overnight runs:** they never send paced or soon work, even if the selector errs. The send step re-checks urgency.
- **Mislabelling:** a wrongly raised today label costs at most 3 extra mails to one thread in a day, with Akshay in Cc. The trial measures how often that happens.

## Trial measures (added to v2.1's table)

| Measure | Target |
| --- | --- |
| Today actions closed the same day (recipient's calendar day) | 95% or more |
| Akshay's "@Zoya" instructions done or escalated | within 2 hours, 100% |
| Today labels later judged wrong (manual sample of 20) | 10% or fewer |
| Overnight runs that found nothing, average cost | logged; drop to every 3 hours if cost exceeds 10% of FAST |
| Mails to a recipient outside 07:00 to 22:00 in their time zone | 0 |

## How

1. Codex reviews this doc against v2.1.
2. Main adds the urgency field, the today selector, the instruction parser and the overnight cron to the FAST and SLOW builds. Nothing goes into the live Zoya prompt.
3. Cleanup's replays, in addition to v2.1's:
   - the pi-labs thread of 22 Oct becomes a today invite, closed before 22:00 IST;
   - "@zoya pls share the invite also" adds named people to an existing invite and confirms on the thread;
   - an overnight run with no today work exits in under 5 tool calls;
   - a today action with an unclear time zone asks once and doesn't send an invite;
   - a third unanswered chase escalates and stops.
4. Akshay's yes, then go live with the split and add these measures to the trial.

## Decisions needed

- **Akshay:** overnight runs every 2 hours, or hourly?
- **Codex:** the 36-hour window for today; whether the recipient-hours rule is safe for guests whose time zone isn't known (default: IST); whether FAST should also run every 30 minutes in the daytime for today work.
