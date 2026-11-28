"""Inbox actions r9 on the live r8e: decisions 443 and 444 (Akshay, 2 Nov). Usage: python3 patch.py <r8e actions.txt> <out>
Input: docs/proposals/inbox-split/r8e/actions.txt, 39,935 / 1d483cbd (live). Each edit asserted once."""
import hashlib, sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:8] == "1d483cbd"
dashes = s.count(chr(0x2014))

def R(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)

# 443: a fourth Next date case.
R("You set it in exactly three cases and never otherwise:", "You set it in exactly four cases and never otherwise:")
R("Next date = the date they give, else 90 days from today.\nNever move, clear or overwrite any other Next date",
  "Next date = the date they give, else 90 days from today.\n"
  "- A scheduling request (decision 443): the guest or their team asks for a call on a date or window (STEP 3). "
  "Next date = that date (a window: its first day; a date already past: today, the step keeps the date they asked "
  "for), replacing any Next date but a calendar booking's.\n"
  "Never move, clear or overwrite any other Next date")
R("Next date only in the three cases above.", "Next date only in the four cases above.")
R("This never changes Next date.", "This never changes Next date, except decision 443's request below.")
# 443 and 444 in STEP 3.
R("- \"Add to outbound\" (the PR agency drops out):",
  "- A scheduling request (decision 443) on an open row: the guest or their team asks for a call on a date or window: "
  "at once, whatever the chase step or a chase Next date said, Zoya added to Waiting on, first in Next action \"Zoya: "
  "reply to <who>: slots for <date>\"; the row's chase or went-quiet segment for them leaves (they wrote), every other "
  "segment kept; Next date as NEXT DATE's fourth case. It is a reply owed now: its owner answers in the next run (Zoya "
  "with slots, or Akshay as below); the Next date marks the call window, never a reason to wait, and a recording "
  "reaches Booked only on their written confirmation of a time. A Tier 1 guest or a date today or tomorrow (decision 425): "
  "\"Akshay: <who> asks for a call on <date>: pick a slot\", Akshay in Waiting on instead of Zoya. On a revenue row "
  "(decision 151) this goes first and his other items stay. A recording on a host show stays the host's pick (above), "
  "Next date untouched.\n"
  "- New inbound on a closed row (decision 444): a substantive new pitch or ask from their side on a row at They "
  "declined, We declined, Parked or Unresponsive (Kind blank is a guest row) is never left: reconcile it with the thread "
  "and the row's earlier outcome, keep Status, add Akshay to Waiting on and put first in Next action one recommendation, "
  "never an open question: \"Akshay: <who> wrote again about <what>; earlier <how it closed>. Recommend: <re-open as "
  "<status> and have Zoya send <the reply> | have Zoya reply no>, because <one line>. Write ok, not ok or a change in Your call. (<D "
  "Mon>)\" (other segments kept); the commercial decision stays his; one such segment already open on the "
  "row: update its what, recommendation and date, never a second. A scheduling request there is this too, not 443. Until Akshay "
  "chooses, STEP 5 and 6e queue no Zoya reply on that thread but the holding reply (decision 390), and 6e bucket C "
  "adds no second Akshay ask there. Acknowledgements, thanks, auto-replies, a sponsored no and noise never trigger it.\n"
  "- \"Add to outbound\" (the PR agency drops out):")

# r9e: Akshay's ok on a 444 re-open may move Status back.
R("Never move Status backward, except to LT chase or a closed outcome.",
  "Never move Status backward, except to LT chase or a closed outcome, or on Akshay's ok to a decision 444 re-open.")
# N1: STEP 5's revenue rule keeps a 443 step first.
R("Then set Waiting on Akshay (keep others) and put first in Next action",
  "Then set Waiting on Akshay (keep others) and put first in Next action (after a decision 443 step queued this run)")
out = s.encode()
assert s.count(chr(0x2014)) == dashes and len(out) <= 65336
open(dst, "wb").write(out)
print("actions r9", len(out), hashlib.sha256(out).hexdigest()[:16])
