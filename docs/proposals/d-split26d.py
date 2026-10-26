"""Split fixes from the scenario replays and replay 1 (Cleanup 559f1ab; split-dryruns/*.md). Edits routines/zoya/parts.
1/ Keying: SLOW keys the follow-ups it selects by Status and Next date itself (no wording needed); every other old-format
   segment is keyed once by a migration before launch, so no run infers keys from wording (replay 1 fail, decision 91).
2/ Concurrency: re-read after each row write and restore this action's own segment or owner once (FAST :30, SLOW even :00).
3/ Next date is the earliest open segment date in both runs; the legacy "original due <YYYY-MM-DD>" counts.
4/ Caps: one definition, never a hold; leftovers go first next run, oldest due first. RECONCILE exempts caps and hosts.
5/ Holds: a hold with no first day rechecks in 7 days, keeps an owner, never re-asks Akshay; PR limit per guest thread.
6/ Inbound completion; two reply actions from one inbound take -1, -2. Retries: the recovered send writes its Action key,
   the draft send carries the key, two Sent copies are one send. The decision 404 emoji only on updates under 48 hours.
7/ SLOW's own reply-shaped mails (payments, billing ask, vendor Your call) are team actions, keyed by SLOW.
Usage: python3 d-split26d.py (repo root)"""
import os
D = "routines/zoya/parts"
E = [
 ("actions.txt",
  "FAST keys every old-format step on the rows it reads, of any type, writing the type into the key; SLOW acts only on keyed "
  "segments, so one run decides each step's type and two runs never key one step two ways. SLOW's steps wait at most one FAST run.",
  "A follow-up STEP 2 selects by Status and Next date needs no wording: SLOW keys it itself as "
  "\"<row>:followup:seq-<routine number>-<step number>:<due date>T00:00:00+09:00\". Every other old-format segment is keyed "
  "once, before launch, by the keying migration; one still unkeyed is FAST's to key from its wording. Snooze segments "
  "(\"Zoya: back to Akshay on\") keep their form."),
 ("actions.txt",
  "followup (routines 1 to 6 and 8), nurture (routine 7, nurture, revival) and team (Jaya, Sarika, Ranjita, internal asks) are SLOW's.",
  "followup (routines 1 to 6 and 8), nurture (routine 7, nurture, revival) and team (Jaya, Sarika, Ranjita, internal asks, "
  "payments, billing asks, vendor Your call steps) are SLOW's."),
 ("actions.txt",
  "a FAST reply action, once per thread per 7 days.",
  "a FAST reply action, only on an update under 48 hours old, once per thread per 7 days (a payment notice is SLOW's). An "
  "inbound that answers our open asks completes each, each completion line naming its Activity; two reply actions raised by "
  "one inbound key as msg-<id>-1, msg-<id>-2."),
 ("actions.txt",
  "Send with the action key as email_compose idempotency_key (its SHA-256 hex if longer than 200 characters).",
  "Send with the action key as idempotency_key on email_compose or the draft send (its SHA-256 hex if longer than 200 "
  "characters). Two Sent copies with one Message-ID are one send; a send found by the thread check gets its Action key too."),
 ("actions.txt",
  "every other segment, owner and line stays as you found it, whoever wrote it.",
  "every other segment, owner and line stays as you found it, whoever wrote it. Then re-read: this action's segment or owner "
  "missing, rewrite it once and report it. Next date is the earliest open segment date (\"original due <YYYY-MM-DD>\" counts)."),
 ("slow-order.txt",
  "Within each, the least recently attempted first, then the oldest due. One you don't reach stays due exactly as it is (Next "
  "date unchanged: a processing cap is not a hold) with a Claude note line \"last attempted <YYYY-MM-DD HH:MM> JST\" (replacing "
  "the row's earlier one).",
  "Within each, the oldest due first. A cap is never a hold: one you don't reach stays due exactly as it is (Next date "
  "unchanged) and goes first next run."),
 ("fast-order.txt",
  "within a type, the least recently attempted first, then the oldest raised. Work them until none is left or the per-run cap "
  "on Cadences is reached. One you don't reach stays due as it is, with a Claude note line \"last attempted <YYYY-MM-DD HH:MM> "
  "JST\" (replacing the row's earlier one; a processing cap is not a hold).",
  "within a type, the oldest raised first. Work them until none is left or the per-run cap on Cadences is reached. A cap is "
  "never a hold: one you don't reach stays due as it is and goes first next run."),
 ("reconcile.txt",
  "Respect quiet hours, explicit holds and decisions pending with Akshay or Jaya (they are not misses).",
  "Quiet hours, explicit holds, a cap, and decisions or picks pending with Akshay, Jaya or a host (Sri, Satish, Arjun) are not misses."),
 ("followups.txt",
  "(the 7-day rule, ONE PERSON, ONE ASK, quiet hours, the weekday rule, the cap, a Salesblink or cold-outreach hold) moves Next "
  "date to the first day it may go",
  "(the 7-day rule, ONE PERSON, ONE ASK, quiet hours, the weekday rule, a Salesblink or cold-outreach hold; never the cap) moves "
  "its segment's date and Next date to the first day it may go"),
 ("followups.txt",
  "(a hold with no first day: a cold-outreach hold takes Zoya off Waiting on and leaves Next date to the row's owner; an Akshay "
  "hold with no date puts the row on Waiting on Akshay and rechecks in 7 days)",
  "(a hold with no first day, cold outreach or an Akshay hold with no date, rechecks in 7 days and keeps an owner: Chaandini for "
  "cold outreach, never empty; never a new ask to Akshay, decision 381)"),
 ("followups.txt",
  "a cap, deferral or failed send moves only Next date",
  "a deferral or failed send moves only Next date (a cap moves nothing)"),
 ("followups.txt",
  "a run that sends nothing (cap, deferral, failure) leaves them and changes only Next date, with a reason.",
  "a run that sends nothing (deferral, failure) leaves them and changes only Next date, with a reason; a cap changes nothing."),
 ("report-slow.txt", 'actions left with "last attempted"', "actions left for the next run (a cap)"),
 ("followups.txt",
  "Hold this mail only for: a substantive mail to them (LIMITS, decision 346) from any row in the last 7 days",
  "Hold this mail only for: a substantive mail to them (LIMITS, decision 346; a PR person per guest thread) from any row in the last 7 days"),
]
for f, a, b in E:
    p = os.path.join(D, f)
    s = open(p, encoding="utf-8").read()
    assert s.count(a) == 1, (f, a[:50], s.count(a))
    open(p, "w", encoding="utf-8").write(s.replace(a, b))
print("edited", len(E))
