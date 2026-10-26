"""Release-build behaviour fixes from frozen round 2 (split-dryruns/frozen-round2.md) and the CTO's 17:15 run receipts.
1/ Lease tie-break: two runs whose records are both Started each held the lease against the other (replay G). The earlier
   Started holds it; the same minute, FAST does.
2/ When SLOW self-keys a row with no Zoya segment, its keyed segment replaces the row's waiting segment for that same ask
   ("Waiting on <their side>: ..."), so one ask is one segment (replay C, Ronit: the two runs differed).
3/ Run receipts: provider usage (input, cache read, cache write, output tokens, cost) when the run can see it, else
   "unknown", never an estimate.
Usage: python3 d-split26j.py (repo root)"""
import os
D = "routines/zoya/parts"
E = [
 ("lease.txt", "holds the lease. While it does,",
  "holds the lease; if both are Started, the earlier start holds it, and in the same minute FAST does. While it does,"),
 ("actions.txt", "writes that key onto the row as its segment the first time it selects it (send, hold or block).",
  "writes that key onto the row as its segment the first time it selects it (send, hold or block), in place of the row's "
  "waiting segment for that ask (\"Waiting on <their side>: ...\")."),
 ("runrecord.txt", "counts, errors,",
  "counts, usage (input, cache read, cache write and output tokens and cost, as the run can see them, else \"unknown\"; "
  "never an estimate), errors,"),
]
for f, a, b in E:
    p = os.path.join(D, f)
    s = open(p, encoding="utf-8").read()
    assert s.count(a) == 1, (f, a[:50], s.count(a))
    open(p, "w", encoding="utf-8").write(s.replace(a, b))
print("edited", len(E))
