"""Cleanup's fixes to the release cut d-split26k (ab182a4). Usage: python3 docs/proposals/d-split26k-fix.py (repo root), then routines/zoya/build.py.
d-split26k gives FAST 35,141 / 6b3bc064ebbe1c60, SLOW 62,217 / 1a833d7a8062f1b6.
1/ Edit 26 pointed SENDING's crash-window check ("check your Sent and the thread first") at ACTIONS' Before sending, which reads
   only the thread. A fresh mail (a first step, a decision mail) has no thread, so only Sent finds it. ACTIONS now reads Sent too.
2/ Edits 76 and 80 dropped "Next date today or earlier" from routine 1's and routine 7's own selector lines. Read alone, each
   picks rows not yet due. Restored."""
def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:60], s.count(a))
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8").write(s)
edit("routines/zoya/parts/actions.txt", [("then read the thread for a message from us after the action was raised",
                                          "then read your Sent and the thread for a message from us after the action was raised")])
edit("routines/zoya/parts/followups.txt", [
 ("rows at Status Sponsored offered, whatever Next action says", "rows at Status Sponsored offered whose Next date is today or earlier, whatever Next action says"),
 ("- 7 Long-term chase: Status LT chase, nurture rows included", "- 7 Long-term chase: Status LT chase, Next date today or earlier, nurture rows included"),
])
print("d-split26k fixes applied")
