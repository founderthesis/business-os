"""Round 5b findings (both runs PASS G, I3, SKIP on b75732e). Usage: python3 docs/proposals/d-split26u.py (repo root, after
d-split26t), then routines/zoya/build_one.py.
1/ Both runs: "back to the start of the latest run whose record isn't Completed" lands on the latest Skipped record (or the run's
   own Started one), never the crashed run that held the lock. After an outage over 24 hours the scan missed the crashed send. It
   now reaches back to the earliest run that took the lock since the last Completed one; Skipped records don't count.
2/ Run A: a skipped run must write its record but "no other read" forbade fetching the Activities schema; and a failed write had
   no rule. It may fetch the Activities data source for that write only; a failed write is retried once, then it stops anyway.
(The runbook now also closes the crashed run's Started record as Failed.)"""
def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:60], s.count(a))
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8").write(s)
P = "routines/zoya/parts/"
edit(P + "actions.txt", [(
 "or back to the start of the latest run whose record isn't Completed if that is earlier:",
 "or, if earlier, back to the start of the earliest run that took the lock since the last Completed one (Skipped records don't count):")])
edit(P + "lock.txt", [(
 "and stop: no other read, send or write.",
 "and stop: no other read, send or write (only the Activities data source may be fetched for that write; it fails twice: stop anyway).")])
print("d-split26u applied")
