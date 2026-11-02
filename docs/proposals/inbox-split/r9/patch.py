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
  "Next date = that date, replacing any chase date.\n"
  "Never move, clear or overwrite any other Next date")
R("Next date only in the three cases above.", "Next date only in the four cases above.")
R("This never changes Next date.", "This never changes Next date, except decision 443's request below.")
# 443 and 444 in STEP 3.
R("- \"Add to outbound\" (the PR agency drops out):",
  "- A scheduling request (decision 443): the guest or their team asks for a call on a date or window: at once, whatever "
  "the chase step or Next date said, Zoya added to Waiting on, first in Next action \"Zoya: reply to <who>: slots for "
  "<date>\" (other segments kept), Next date = that date. A recording on a host show stays the host's pick (above).\n"
  "- New inbound on a closed row (decision 444): a fresh pitch or ask from their side on a row at They declined, We "
  "declined, Parked or Unresponsive (Kind blank is a guest row) is never left: read the earlier history, keep Status, "
  "add Akshay to Waiting on and put first in Next action \"Akshay: <who> wrote again about <what>; earlier <how it "
  "closed>. Re-open, or have Zoya reply?\", once per inbound. A sponsored no or a plain thanks is not a fresh ask.\n"
  "- \"Add to outbound\" (the PR agency drops out):")

out = s.encode()
assert s.count(chr(0x2014)) == dashes and len(out) <= 65336
open(dst, "wb").write(out)
print("actions r9", len(out), hashlib.sha256(out).hexdigest()[:16])
