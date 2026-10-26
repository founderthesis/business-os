"""Cleanup's fixes to d-split26h (0cd9dfe). Usage: python3 docs/proposals/d-split26h-fix.py (repo root), then routines/zoya/build.py.
d-split26h gives FAST 36,165 / e8e94fc6c3afb3ff, SLOW 65,194 / 3a7dd1590f30770f.
1/ The PR COORDINATION trim said un# Booking rows go "beating all of the above". In SLOW, LIMITS sits above STEP 2, so that
   reads as beating the daily cap, the follow-up window, quiet hours and Diwali week. Restored the named list it beats.
2/ The lease and RECONCILE found the other run's record by Summary wording ("Run zoya FAST"). Run records now carry the run
   in their key, Source ID "run:zoya:fast:<run id>" or "run:zoya:slow:<run id>", and both read by that key. The sweep's
   STEP 4b still matches them ("run:zoya:" prefix).
3/ "No new row after :30 past any hour" lets a SLOW run still going at 09:05 start rows again. Now: past the hour it started."""
import os
D = "routines/zoya/parts"
def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:60], s.count(a))
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8").write(s)
edit(os.path.join(D, "followups.txt"), [
 ("these rows only, beating all of the above, the STALENESS GATE's span",
  "these rows only, beating the gaps and 30 quiet days above, the 7-day limit in LIMITS, the STALENESS GATE's span"),
])
edit(os.path.join(D, "lease.txt"), [
 ('read the latest "Run zoya OTHER" record:', 'read the latest run record with Source ID starting "run:zoya:KEY:":'),
])
edit(os.path.join(D, "reconcile.txt"), [
 ('read the latest "Run zoya FAST" record.', 'read FAST\'s latest run record (Source ID starts "run:zoya:fast:").'),
])
edit("routines/zoya/build.py", [
 ('  ("runrecord", "Run zoya <", "Run zoya FAST <"),\n',
  '  ("runrecord", "Run zoya <", "Run zoya FAST <"),\n  ("runrecord", "run:zoya:<run id>", "run:zoya:fast:<run id>"),\n  ("lease", "KEY", "slow"),\n'),
 ('  ("runrecord", "Run zoya <", "Run zoya SLOW <"),\n',
  '  ("runrecord", "Run zoya <", "Run zoya SLOW <"),\n  ("runrecord", "run:zoya:<run id>", "run:zoya:slow:<run id>"),\n  ("lease", "KEY", "fast"),\n'),
 ("Start no new row after :30 past any hour,", "Start no new row after :30 past the hour you started,"),
])
print("d-split26h fixes applied")
