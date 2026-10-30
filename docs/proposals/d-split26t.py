"""Round 5 findings on the lock path (both runs PASS 10 of 10 on c1669fd). Usage: python3 docs/proposals/d-split26t.py (repo
root, after d-split26s), then routines/zoya/build_one.py.
1/ "THE RULES ARE IN NOTION. Every run, before anything else, read" contradicted LOCK's "before ANY other read". LOCK comes first.
2/ A skipped run's record: RUN RECORD creates it as Started, LOCK step 3 writes it as Skipped. Now one write, created as Skipped.
3/ The 24-hour Sent scan would miss a crashed send once the lock had been held for more than a day (runbook delay). It now
   reaches back to the start of the last run that didn't end Completed, if that is earlier.
(build_one.py now fills @@VERSION@@ as build.py does: "zoya-one <first 12 of the sha256 with the stamp written back>".)"""
def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:60], s.count(a))
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8").write(s)
P = "routines/zoya/parts/"
edit(P + "rules-common.txt", [("THE RULES ARE IN NOTION. Every run, before anything else, read:",
                               "THE RULES ARE IN NOTION. Every run, right after LOCK and before anything else, read:")])
edit(P + "lock.txt", [("3. M not starting \"free:\": the lock is held. Write only the run record, Summary",
                       "3. M not starting \"free:\": the lock is held. Write only the run record, created once (never Started first) with Summary")])
edit(P + "actions.txt", [("Each run also checks its Sent for the last 24 hours:",
                          "Each run also checks its Sent for the last 24 hours, or back to the start of the latest run whose record isn't Completed if that is earlier:")])
print("d-split26t applied")
