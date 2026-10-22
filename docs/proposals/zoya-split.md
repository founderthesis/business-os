# Proposal: split Zoya's run so urgent mail always goes

Status: proposed by the CTO session, 22 Oct 2026. Needs Akshay's yes. For review by the Codex CTO.

## Why

Zoya missed four approved mails in two days. Byufuel and Escobar Bandra got Akshay's "offer sponsored" call on 21 Oct, and both mails sat queued until the CTO sent them by hand on 22 Oct. Every miss has the same cause: one hourly run does all of Zoya's work and stops before it finishes.

What the run records show (Activities "Run zoya ...", 21 Oct):

- The 16:38, 17:38 and 21:38 JST runs ended Partial. The 21:38 record says "other due follow-ups not worked (time and context limits)". It spent about 32 minutes on 5 overdue long-term chase rows.
- Before any work, each run reads its prompt (about 59 KB) and the Notion pages it controls by: Rules for Zoya (about 59 KB), the wording page (about 57 KB), Cadences, and the routine pages. That's more than 150 KB of rules per run.
- A long-term chase is the most expensive row. Zoya reads the whole thread (some have 50+ mails), checks the person's other rows for the 7-day limit, runs the staleness gate, then writes, logs and updates. That's 10 to 20 tool calls per row.
- The rules say replies and Akshay's decisions come first, but the run worked due rows oldest first. The queue cleanup (decision 381) and nurture had just made dozens of old rows due, so they filled the run.
- Nothing checks that what was due was sent. Akshay found the misses himself.

The d390 batch (Cleanup accepted, e6605af) fixes the order and caps long-term chases at 10 a run. That stops today's failure. Two things stay true after it: replies and decisions still share a run with expensive chases, and a run that dies halfway goes unnoticed.

## What

Same routine, same rules, same inbox. Two schedules and one check.

1. **Zoya, fast run (hourly, 07:30 to 23:30 JST).** Only:
   - replies to anyone outside the team who wrote to us;
   - queue steps from Akshay's decisions (Waiting on Zoya where the step comes from his call or Your call);
   - holding replies (decision 390);
   - the watchdog (point 3).

   It reads only the rule sections these need. When nothing is due, it ends in under a minute.
2. **Zoya, slow run (every 2 hours, 08:30 to 22:30 JST, weekdays).** Follow-ups by routine, nurture, revivals, long-term chases, the owner mail and the Monday scorecard. It keeps the d390 cap of 10 long-term rows a run, and any row it doesn't reach is held a working day with the reason written. It never touches a row the fast run owns.
3. **Watchdog, inside the fast run (no new routine).** Each run checks two things:
   - an Akshay decision queued for Zoya more than 2 hours ago, with no sent Activity;
   - a message to Zoya's or Akshay's inbox from outside the team, older than one working day, with no reply and no hold rule that explains it (a pending Akshay decision gets a holding reply under decision 390).

   It sends what's due with the approved wording and posts one line in the Zoya WhatsApp group: "Zoya ✨ caught 2: <names>, sent now". The Monday scorecard adds one number, inbound mail unanswered over 24 hours. The target is zero.
4. **A computed priority field on Engagements.** A formula, set by no one: 1 = Akshay's decision or a reply owed, 2 = active follow-up, 3 = nurture or long-term chase. Each run selects its rows by Priority, Waiting on and Next date, never by reading Next action text.

## How

1. **Prompt.** One prompt file, routines/zoya.md, with a MODE line at the top that each trigger sets (FAST or SLOW). Shared rules stay in one place. Each mode lists the Notion sections it reads, so the fast run doesn't load the follow-up chains or the nurture rules.
2. **Triggers.** The existing Zoya trigger becomes FAST, and one new trigger runs SLOW. Both use the same connectors (MCP Emails, Notion, Gmail read, Calendar read, Blueticks).
3. **Notion.** Add the Priority formula to Engagements, plus one view, "Zoya due", sorted by Priority then Next date. No new database.
4. **Ownership.** Rows at Priority 1 belong to FAST and the rest to SLOW. If a row changes priority mid-run, the next run of the right mode picks it up. Dedupe stays on Activity Source IDs, so a mail is never sent twice.
5. **Build order.**
   1. Deploy d390 (accepted).
   2. Deploy Codex's three audit fixes: owner mail selects guest decisions, one message identity per send, Sarika edit notes logged only after a send receipt. These make "one ask, one verified send, one Activity, one next step" true, and the watchdog depends on that.
   3. Build this split. Cleanup reviews it, then it goes live on Akshay's yes in Main's chat.
6. **Test before go-live.** Replay 21 Oct against the new prompts. FAST must send Byufuel and Escobar within its first run. SLOW must work the long-term rows within its cap. The watchdog must flag nothing that was sent and catch a queued decision we hold back on purpose.

## Cost

- **FAST:** 17 runs a day. Most find nothing and end quickly, so the extra cost is small. The current hourly run already pays the full rule-reading cost every time.
- **SLOW:** 8 runs a weekday. It does the heavy work the single run does today, spread over fewer runs, so it costs about the same or less.
- **Net:** roughly flat on tokens, in exchange for a guaranteed path for urgent mail.

## Risks and how they're handled

- **Two runs write the same row.** Ownership is by Priority; dedupe uses Source IDs, and the 7-day limit reads Activities, so a mail from either run counts once.
- **Rules drift between modes.** One file and one set of Notion pages; modes only choose what to load.
- **The watchdog duplicates a send.** It sends only when no Activity exists for that step, and it uses the same Source ID the run would have used.
- **More moving parts.** One more trigger and one formula. No new database, page or decision process.

## Decision needed

Akshay: yes or no on the split (points 1 to 4), built after d390 and Codex's three fixes are live.

Codex: comments welcome, especially on the Priority formula, the ownership rule, and whether the watchdog belongs in the fast run or the daily sweep.
