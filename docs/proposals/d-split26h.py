"""Overlap lease for the split's real schedule (CTO, 26 Oct 16:20 JST): FAST fires at :38 hourly (the Zoya trigger's
"30 7-23" is anchored by the server to its creation minute, observed 12:38 and 13:38 on 26 Oct) and SLOW at :08 on even hours,
weekdays (Cleanup c66415e: 8 8-22/2; FAST runs :38 to :03, SLOW :08 to :30). A run can last past 12 minutes, so the old different-minutes reasoning proves nothing. The run record
is the lease: neither run writes a row while the other's record is still Started (less than 45 minutes old, so a crashed
run never blocks for long). The lease covers a run that overruns its guard: SLOW starts no new row after :30 past any hour, and FAST none after 25
minutes. New part lease.txt in both
manifests; intros name the real times; PR COORDINATION trimmed (same rules) to fit SLOW.
Usage: python3 d-split26h.py (repo root)"""
import os
D = "routines/zoya/parts"
LEASE = ("LEASE (FAST and SLOW never write rows at once). Your run record is your lease. Before your first row write, read "
         "the latest \"Run zoya OTHER\" record: one still at Started, begun under 45 minutes ago, holds the lease. While it "
         "does, only read; re-check every 2 minutes (Bash sleep 120; if sleep is refused, re-check between read steps) for up "
         "to WAIT minutes, then if it is still held end Partial, \"lease held by OTHER <run id>\", having written no row.STOP")
open(os.path.join(D, "lease.txt"), "w", encoding="utf-8").write(LEASE + "\n")
p = "routines/zoya/build.py"
s = open(p, encoding="utf-8").read()
for a, b in [
 ('"identity", "runrecord", "fast-order"', '"identity", "runrecord", "lease", "fast-order"'),
 ('"identity", "runrecord",\n        "reconcile"', '"identity", "runrecord", "lease",\n        "reconcile"'),
 ('  ("runrecord", "Run zoya <", "Run zoya FAST <"),',
  '  ("runrecord", "Run zoya <", "Run zoya FAST <"),\n  ("lease", "OTHER", "SLOW"),\n  ("lease", "WAIT", "10"),\n  ("lease", "STOP", ""),'),
 ('  ("runrecord", "Run zoya <", "Run zoya SLOW <"),',
  '  ("runrecord", "Run zoya <", "Run zoya SLOW <"),\n  ("lease", "OTHER", "FAST"),\n  ("lease", "WAIT", "25"),\n'
  '  ("lease", "STOP", " Start no new row after :30 past any hour, so FAST\'s :38 run finds you done; the next run carries on."),'),
]:
    assert s.count(a) == 1, a
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)
E = [
 ("intro-fast.txt", "You run at :30 every hour, 07:30 to 23:30 JST;", "You run at :38 every hour, 07:38 to 23:38 JST;"),
 ("intro-slow.txt", "You run at :00 every 2 hours, 08:00 to 22:00 JST, weekdays;", "You run at :08 every 2 hours, 08:08 to 22:08 JST, weekdays;"),
 ("slow-order.txt", " Start no new row after 25 minutes, so you never overlap FAST's next run; the next run carries on.", ""),
 ("followups.txt",
  "while a PR or agency person on Via is coordinating a precall or recording that isn't booked yet and their side wrote in the "
  "last 30 days, the next mail goes 5 working days after the last substantive ask or exchange (a loop-in, a thanks or an "
  "out-of-office doesn't count; weekdays only, never Diwali week), unless they asked for a hold (their date wins).",
  "a PR or agency person on Via coordinating an unbooked precall or recording, their side having written in the last 30 days: "
  "the next mail goes 5 working days after the last substantive ask or exchange (not a loop-in, thanks or out-of-office; "
  "weekdays, never Diwali week), unless they asked for a hold (their date wins)."),
 ("followups.txt",
  "2 working days after our last ask until a recording is on the calendar, these rows only; this beats the 5-working-day gap, "
  "the 30 quiet days, the 7-day limit in LIMITS, the STALENESS GATE's span and the 3 unanswered chases;",
  "2 working days after our last ask until a recording is on the calendar, these rows only, beating all of the above, the "
  "STALENESS GATE's span and the 3 unanswered chases;"),
]
for f, a, b in E:
    q = os.path.join(D, f)
    t = open(q, encoding="utf-8").read()
    assert t.count(a) == 1, (f, a[:50], t.count(a))
    open(q, "w", encoding="utf-8").write(t.replace(a, b))
print("lease part written; build.py and", len(E), "parts edited")
