"""Capture r8f on r8e (CTO, 2 Nov 13:40 JST). The 13:19 run skipped STEP 0 as "too heavy" and never reached LINK.
Usage: python3 patch.py <r8e capture> <out>."""
import hashlib, sys
s = open(sys.argv[1], encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:8] == "c0abafcd"
d = s.count(chr(0x2014))
a = "within each, oldest Captured first, then oldest Date. Start no row more than 8 minutes after the run's start."
assert s.count(a) == 1
s = s.replace(a, a + " Work LINK rows first (no RAW). STEP 0 is never skipped or judged too heavy: a run that works none of it "
    "while rows are due is Partial, \"STEP 0 skipped\", a defect; a slow row only waits for the next run.")
b = s.encode(); assert s.count(chr(0x2014)) == d and len(b) <= 65536
open(sys.argv[2], "wb").write(b); print(len(b), hashlib.sha256(b).hexdigest()[:16])
