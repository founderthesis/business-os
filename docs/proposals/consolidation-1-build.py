#!/usr/bin/env python3
"""Consolidation 1 pilot: Zoya prompt edits (sponsored obligations as Kind Task rows).
Usage: python3 c1-build.py <routines/zoya.md at the deployed base> <out.md>
Checks the base by sha256 of the prompt block, applies each edit exactly once, prints sizes."""
import sys, re, hashlib
BASE_SHA16 = "487ebbf6feef8db7"   # Zoya prompt block as deployed 20 Oct (9ae734d)
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
def block(t):
    m = re.search(r"```text\n(.*?)\n```", t, re.S); return m.group(1)
b = block(s).encode()
assert hashlib.sha256(b).hexdigest()[:16] == BASE_SHA16, "base mismatch: " + hashlib.sha256(b).hexdigest()[:16]

OBL = ('OBLIGATIONS (Consolidation 1). A sponsored obligation can have its own row: Engagements Kind Task with Obligation set '
 '(Sponsored chase, Sponsored next steps, Payment reminder, Payment confirmation), For engagement the guest\'s Engagement, '
 'Source ID "obl:<obligation>:<engagement page id>" (one open row per obligation and Engagement). That row is the only record of '
 'its obligation: its Next date, Chase step, Waiting on, Next action, Task state and Claude note belong to it alone, and its page '
 'body holds its planned mail ("## Next sponsored mail"). Select these rows by Kind Task, Obligation, Task state not Done or On hold '
 'and Next date today or earlier, never by Next action text. While a guest Engagement has an open row for an obligation, that '
 'obligation is worked only through the row: routine 1 and STEP 1b skip the Engagement for it, and you never write the '
 'Engagement\'s Next date, Chase step or Next action for it (the Engagement\'s Next date is its booked call only). Status and '
 'Payment stay on the Engagement and you still set them from what happened. Before acting, read the Engagement (Status, Payment, '
 'Your call, Standing, holds) and the thread exactly as for a guest row; every STEP 2 rule (GUARD, NURTURE, ONE PERSON, ONE ASK, '
 'STALENESS GATE, LIMITS, quiet hours, holds) applies to the row as if it were the Engagement, and a hold moves only the row\'s '
 'Next date. AFTER SEND writes go to the row (Chase step, Next date, Next action, Claude note, Waiting on); the Activity links the '
 'Engagement and names the row in its body. A reply from their side sets the row to Task state Awaiting someone else, Waiting on '
 'Guest or PR, Next date the next step\'s due date. A decline, a no-contact request, or Akshay\'s decline or park closes every open '
 'obligation row of that Engagement in the same run (Task state Done, Claude note "YYYY-MM-DD: closed: <why>"); a declined '
 'sponsored chase never closes a payment row unless the decline covers it. A payment row ends Done when Payment reaches Settled. '
 'Never create, reopen or delete these rows except as this paragraph says.\n')

edits = [
 # 1. queue exclusion
 ('Rows whose Next action starts "Agent: sponsored step" or "Zoya: <routine> step" are follow-ups, not queue steps',
  'A Kind Task row with Obligation set is a follow-up (OBLIGATIONS), never a queue step. Rows whose Next action starts "Agent: sponsored step" or "Zoya: <routine> step" are follow-ups, not queue steps'),
 # 2. STEP 1b uses obligation rows
 ('STEP 1b. PAYMENTS (sponsored, Akshay, 16 Oct)\n',
  'STEP 1b. PAYMENTS (sponsored, Akshay, 16 Oct). For an Engagement with an open Payment reminder, Payment confirmation or Sponsored next steps row, do these steps on that row (OBLIGATIONS).\n'),
 # 3. OBLIGATIONS paragraph before STEP 2
 ('STEP 2. FOLLOW-UPS DUE\n', OBL + '\nSTEP 2. FOLLOW-UPS DUE\n'),
 # 4. routine 1 selector
 ('- 1 Sponsored offers: rows at Status Sponsored offered whose Next date is today or earlier, whatever Next action says',
  '- 1 Sponsored offers: open Sponsored chase rows due today or earlier (OBLIGATIONS), and rows at Status Sponsored offered with no open Sponsored chase row whose Next date is today or earlier, whatever Next action says'),
]
for a, bb in edits:
    assert s.count(a) == 1, "anchor not unique: " + a[:60]
    s = s.replace(a, bb)
open(out, "w", encoding="utf-8").write(s)
nb = block(s).encode()
print("prompt", len(b), "->", len(nb), "bytes; sha256", hashlib.sha256(nb).hexdigest()[:16], "; spare", 65536 - len(nb))

# ---- sweep: an Engagement whose obligations live on Task rows is not "quiet" for an empty Next date
if len(sys.argv) > 4:
    ssrc, sout = sys.argv[3], sys.argv[4]
    t = open(ssrc, encoding="utf-8").read()
    tb = block(t).encode()
    assert hashlib.sha256(tb).hexdigest()[:16] == "b0888b6624e6848f", "sweep base mismatch"
    a = "Sponsored offered, Booking, LT chase) with Next date empty and no Activity in 14 days."
    bb = "Sponsored offered, Booking, LT chase) with Next date empty, no open obligation row (Kind Task, For engagement this row, Task state not Done or On hold) and no Activity in 14 days."
    assert t.count(a) == 1
    t = t.replace(a, bb)
    open(sout, "w", encoding="utf-8").write(t)
    ntb = block(t).encode()
    print("sweep", len(tb), "->", len(ntb), "bytes; sha256", hashlib.sha256(ntb).hexdigest()[:16])
