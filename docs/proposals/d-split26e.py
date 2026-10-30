"""Split fixes from the scenario re-run on split26d (split-dryruns/replays-26d.md). Edits routines/zoya/parts.
1/ Contact holds: a hold is never a skip; a block moves Next date 7 days on; the kept owner is the outreach owner.
2/ Caps: "at most 10" binds routine 7 and nurture only.
3/ One inbound: -1, -2 in the order the asks appear; STEP 1e follows WRITE PATH; a reply waiting on a host's pick waits.
4/ Same minute: vendor Your call, billing and payment steps are SLOW's in FAST's queue too; SLOW's billing ask only when
   no "Sponsored yes: next steps" is on the thread.
5/ AFTER SEND writes the next step keyed; a hold changes only "on <D Mon>". Snoozes never set Next date.
6/ Run times: the intros already match zoya-split-build.md (FAST :30 hourly, SLOW 0 8-22/2 weekdays); no change.
Usage: python3 d-split26e.py (repo root)"""
import os
D = "routines/zoya/parts"
E = [
 ("followups.txt", "(a verdict, an offer, a negotiation, a price, a no-show or a hold)",
  "(a verdict, an offer, a negotiation, a price, a no-show; a hold goes by the hold rule below, never a skip)"),
 ("followups.txt", "a block (missing data, bounce, a decision someone else holds) names the blocker and its owner",
  "a block (missing data, bounce, a decision someone else holds) names the blocker and its owner and moves Next date 7 days on"),
 ("followups.txt", "keeps an owner: Chaandini for cold outreach, never empty;",
  "keeps an owner, never empty (the outreach owner: Chaandini on Built to Share and Human by Design, else Zoya);"),
 ("followups.txt", 'segment "Zoya: <routine> step <n+1> on <D Mon>"',
  'segment "Zoya [followup seq-<routine>-<n+1> <its due date>]: <routine> step <n+1> on <D Mon>" (a hold changes only "on <D Mon>", never the key)'),
 ("slow-order.txt", "routine 7 and nurture, at most 10 of those a run", "routine 7 and nurture (at most 10 of these a run)"),
 ("actions.txt", "two reply actions raised by one inbound key as msg-<id>-1, msg-<id>-2.",
  "two reply actions raised by one inbound key as msg-<id>-1, msg-<id>-2, in the order the asks appear."),
 ("actions.txt", "Next date is the earliest open segment date (\"original due <YYYY-MM-DD>\" counts).",
  "Next date is the earliest open segment date (\"original due <YYYY-MM-DD>\" counts; a snoozed or held-for-snooze one never does)."),
 ("mail.txt", "Move each row on: Status, Waiting on (usually Guest or PR), Next action,",
  "Move each row on (WRITE PATH: only this action's own segment): Status, Waiting on (usually Guest or PR), Next action,"),
 ("mail.txt", "c. Not routine, or a message",
  "A reply whose answer waits on a host's pick (a step on the row says so) waits with it: mark the thread \"waiting on <host>\".\nc. Not routine, or a message"),
 ("queue-fast.txt", "a step from his Your call or mail (a slot ask, a precall invite, a decline, next steps after a sponsored yes, a price negotiation reply), a holding reply.",
  "a step from his Your call or mail (a slot ask, a precall invite, a decline, next steps after a sponsored yes, a price negotiation reply), a holding reply. Vendor Your call, billing and payment steps are SLOW's (team)."),
 ("payments.txt", "A yes where billing details are still pending (Status Booking or Sponsored offered with Payment empty or Not started):",
  "A yes where billing details are still pending (Status Booking or Sponsored offered with Payment empty or Not started) and no \"Sponsored yes: next steps\" from us on the thread:"),
 ("followups.txt", "(Salesblink was retired on 19 Oct 2026, so this ends by 2 Nov 2026; Waiting on Chaandini alone is never a hold)",
  "(retired 19 Oct, so this ends 2 Nov; Waiting on Chaandini alone is never a hold)"),
]
for f, a, b in E:
    p = os.path.join(D, f)
    s = open(p, encoding="utf-8").read()
    assert s.count(a) == 1, (f, a[:50], s.count(a))
    open(p, "w", encoding="utf-8").write(s.replace(a, b))
print("edited", len(E))
