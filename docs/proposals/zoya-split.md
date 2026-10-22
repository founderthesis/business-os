# Proposal v2: a reduced FAST/SLOW trial for Zoya

Status: v2, 22 Oct 2026, revised after the Codex CTO's review of v1. Needs Akshay's yes before anything is built. Builds only after d390 (deploying now) and Codex's three audit fixes are live.

## Why

Zoya missed four approved mails in two days. On 21 Oct the 16:38, 17:38 and 21:38 JST runs ended Partial. The 21:38 run spent about 32 minutes on 5 overdue long-term chases and logged "other due follow-ups not worked (time and context limits)". Byufuel and Escobar Bandra had Akshay's "offer sponsored" queued, and both went out only when the CTO sent them by hand on 22 Oct.

Two causes:

1. **Cheap urgent work and expensive chases share one run.** Every run first loads the 59 KB prompt plus Rules for Zoya, the wording page and Cadences. That's more than 150 KB before any work. A long-term chase then reads whole threads and checks contact limits, at 10 to 20 tool calls a row. Urgent replies wait behind that work.
2. **Nothing reconciles what was due against what was sent.** Akshay found the misses himself.

d390 fixes the order: replies and queued decisions run first, and long-term chases are capped at 10 a run. v2 builds on that rather than replacing it.

## What changed from v1 (Codex's points)

| v1 | v2 | Why |
| --- | --- | --- |
| A whole Engagement belongs to FAST or SLOW, set by a Priority formula | Each pending **action** has a stable key and a type, and the action type decides the run. No Priority field | One row can hold a reply owed, a booking chase and a community-add ask. A formula can't see mailbox state |
| Dedupe on Activity Source IDs | The same **action key** in both runs, plus a fresh Sent and thread check right before sending. Runs staggered | Provider message IDs exist only after a send, so two runs could both pass the Activity check |
| Watchdog inside FAST, sends what it finds | **Reconcile only**, from SLOW and the daily sweep: check Sent and the thread first, then hand the action to the normal send path | A crash can leave a sent mail with no Activity, and FAST can't detect itself not running |
| Capped rows held a working day | Capped actions **stay overdue**; the next run takes the least recently attempted first | A processing cap is not a business hold |
| One prompt with a MODE line | **Two generated prompts** from shared rule files | A MODE line doesn't shrink what each run reads |
| "Always finishes", "roughly flat cost" | **Hypotheses** with numbers to measure in the trial | Not shown yet |

## What

### 1. Actions, keyed

An action is one obligation on an Engagement. It's either a segment of Next action, or a reply owed on a thread linked to the row. Each has a key:

`<engagement id>:<type>:<raised date YYYY-MM-DD>[:<thread id>]`

The types and which run owns each:

| Type | Example | Run |
| --- | --- | --- |
| reply | someone outside the team wrote on a thread linked to the row and is owed an answer | FAST |
| decision | a step from Akshay's call or Your call ("Zoya: send Akshay's decision mail") | FAST |
| hold | holding reply (decision 390) | FAST |
| followup | routines 1 to 5 chain steps | SLOW |
| nurture | nurture, revival, long-term chase | SLOW |
| team | WhatsApp to Jaya, Sarika or Ranjita, internal asks | SLOW |

Next action segments start with their owner today ("Zoya: ..."). v2 adds the type and the raised date in a fixed short form, for example "Zoya [decision 2026-10-21]: send Akshay's decision mail". Every routine that writes a Zoya step writes this form, so the step can be selected without reading prose. Completing an action removes only its own segment and leaves the others.

Reply-owed actions are found from the mailboxes: the latest message on a linked thread is from outside the team and has no later message from us. That check runs in FAST against both inboxes, reusing the inbox routine's thread matching.

### 2. Sending safely

- FAST runs at :30 every hour, 07:30 to 23:30 JST. SLOW runs at :00 every 2 hours, 08:00 to 22:00 JST, weekdays.
- Before every send, both runs look for the action key on an Activity, then check Zoya's Sent folder and the thread for a message to that recipient after the action's raised date. Any match means don't send: log the Activity if it's missing, complete the action and move on.
- The Activity is written only after a send receipt, with Source ID "action:<key>". An uncertain result leaves the action pending, and it's retried once after the Sent check. This is the same pattern as Codex's Sarika fix.

### 3. Reconcile, don't resend

- **SLOW, every run:** checks FAST's last run record. If FAST hasn't run in 90 minutes, or any decision or reply action is older than 2 hours, it reconciles: Sent and the thread first; if a mail was sent, it logs and completes the action; if not, it hands the action to FAST by keeping it due and leaves a note on the row. It doesn't send itself.
- **Daily sweep:** the same check across all actions, plus inbound mail unanswered for more than one working day.
- **WhatsApp alert** to Akshay's Zoya group only when an action is still unresolved after one reconcile pass.

### 4. Fair ordering

Within each run, actions are ordered by type, then by the date of the last attempt (oldest first), then by raised date. When a run hits its cap, unfinished actions stay due and carry a "last attempted <time>" note, so the next run starts with others. Nothing is postponed by a fixed delay.

### 5. Smaller prompts

The rules split into shared files: voice and links, sending and quiet hours, logging, contact limits, and the action format. Two deployed prompts are built from them: zoya-fast (replies, decisions, holds) and zoya-slow (routines 1 to 8, nurture, team, owner mail, scorecard). The target is FAST at 25 KB or less. Each prompt lists the Notion pages and sections it reads. FAST doesn't load the follow-up chains or the nurture rules.

## Trial: one week, then keep or drop

Accept the split only if, over 7 days:

| Measure | Target | Source |
| --- | --- | --- |
| Akshay decision queued until sent | 95% within 2 hours, none over 24 | action key times vs Activity times |
| Reply owed until reply or holding reply | none over 1 working day | daily sweep reconcile |
| Long-term and nurture actions progressing | no action unattempted more than 3 days past due | last-attempted notes |
| Duplicate sends | 0, including on retries | Sent folder vs Activities |
| Duplicate Activities | 0 on a full mailbox reread | Codex's acceptance test |
| Cost per day | within 20% of the week before the trial | run usage |

FAST "always finishes" and "flat cost" are hypotheses the trial tests.

## How

1. d390 goes live (in progress). Next batch: Codex's three fixes, plus the d390 cap rule changed from "held a working day" to "stays overdue, least recently attempted first".
2. Main builds the action format into every routine that writes Zoya steps (inbox, calendar, WhatsApp, sweep, Zoya), and the two prompts from shared files. Cleanup reviews it.
3. Replay 21 Oct and a crash test before go-live:
   - Byufuel and Escobar clear in FAST's first run.
   - A send killed after delivery and before logging is found by the Sent check and logged once.
   - FAST and SLOW started at the same minute on one row send nothing twice.
4. Akshay's yes in Main's chat, then go live, with the CTO reading the trial measures daily and reporting a verdict on day 7.

## Not in v2

No Priority field, no new database, no separate watchdog sender. One extra trigger (SLOW) and shared rule files in the repo.

## Decisions needed

- **Akshay:** yes or no to the trial, built after the fixes above.
- **Codex:** comments, especially on the action format in Next action, the reply-owed detection, and whether SLOW's reconcile check gives enough coverage between sweeps.
