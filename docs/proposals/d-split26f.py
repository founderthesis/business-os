"""Replay 1b's one label difference: two FAST runs counted the release-date replies as held in one and blocked in the
other. A step waiting on a missing fact is blocked (STEP 2's "missing data"); held means a timing rule. FAST only.
Usage: python3 d-split26f.py (repo root)"""
import os
p = "routines/zoya/parts/report-fast.txt"
a = "held <n>, blocked <n>, remaining <n>, by type."
b = ("held <n>, blocked <n>, remaining <n>, by type (held: a timing rule or a host's pick; blocked: a missing fact, date, "
     "link or name, or a decision someone else holds).")
s = open(p, encoding="utf-8").read()
assert s.count(a) == 1
open(p, "w", encoding="utf-8").write(s.replace(a, b))
print("edited report-fast.txt")
