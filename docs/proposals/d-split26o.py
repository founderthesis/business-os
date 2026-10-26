"""CTO, 22:55 JST (Akshay's new rules): the lock tie and crashed-lock choice, after d-split26n. Usage: python3
docs/proposals/d-split26o.py (repo root, after d-split26l-fix, d-split26m and d-split26n), then routines/zoya/build.py.
1/ Tie: "in the same minute FAST does" becomes "the later writer backs off": the earlier record by created time, to the second,
   holds the lease; only an exact same-second tie goes to FAST. The re-read is now explicitly after acquiring.
2/ Crashed lock, the choice: keep the 60-minute stale limit, let the wait outlast it and close a stale record as Failed
   (d-split26n). Why not shorten the limit: a live run's record must never look stale, and a shorter limit would need a shorter
   window than SLOW's approved 40 minutes. The gap this exposed (a SLOW that waited 25 minutes could start rows past 60) is
   closed by Cleanup's 45-minute cap from SLOW's start (d-split26m-fix 2/, d6a1209); this script no longer adds its own cap.
Order: d-split26l, d-split26l-fix, d-split26m, d-split26m-fix, d-split26n, Cleanup's build.py STOP change, d-split26o."""
def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:60], s.count(a))
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8").write(s)
P = "routines/zoya/parts/"
edit(P + "lease.txt", [
 ("if both are Started, the earlier start holds it, and in the same minute FAST does. Read again 1 minute after your first read "
  "(Bash sleep 60), still before any row write: a record the other run wrote meanwhile counts the same way.",
  "if both are Started, the earlier record holds it (its created time, to the second): the later writer backs off; only an exact "
  "same-second tie goes to FAST. Once you hold it, read again 1 minute later (Bash sleep 60), still before any row write: a record "
  "the other run wrote meanwhile counts the same way, and if it now holds, you back off."),
])
print("d-split26o applied")
