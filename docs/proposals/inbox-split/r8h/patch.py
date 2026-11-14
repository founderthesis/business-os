"""Capture r8h on r8g (CTO, 2 Nov 14:15 JST). The 14:02 run put Engagement ids on "stamped:"; it must be the Activity's own id.
Usage: python3 patch.py <r8g capture> <out>."""
import hashlib, sys
s = open(sys.argv[1], encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:8] == "309d96d9"
a = "linked to an Engagement or Deal: add its id to your record's \"stamped:\" line (actions repairs it);"
assert s.count(a) == 1
s = s.replace(a, "linked to an Engagement or Deal: add this Activity's own page id (never the Engagement's) to your record's \"stamped:\" line (actions repairs it);")
b = s.encode(); assert len(b) <= 65536
open(sys.argv[2], "wb").write(b); print(len(b), hashlib.sha256(b).hexdigest()[:16])
