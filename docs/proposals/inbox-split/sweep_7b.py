"""Daily sweep takes the inbox's STEP 7b (guest form submissions), verbatim, in Part B (inbox split, 1 Nov).
Input: the accepted d420 sweep, 35,047 / 06c4120b2cd48ef1. Usage: python3 sweep_7b.py <sweep.txt> <step7b.txt> <out.txt>"""
import hashlib, sys
src, step7b, dst = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:16] == "06c4120b2cd48ef1"
b = open(step7b, encoding="utf-8").read().rstrip("\n")
assert b.startswith("STEP 7b. GUEST FORM SUBMISSIONS")
dashes = s.count(chr(0x2014))

def rep(a, x):
    global s
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, x)

rep("STEP 4b, 3i, 3h, 3g, 3b, 3d, 4, 5, 6c.", "STEP 4b, 3i, 3h, 3g, 3b, 3d, 4, 5, 6c, 7b.")
rep("\nSTEP 7. REPORT\n", "\n" + b + "\n(7b moved from the inbox, 1 Nov: once a day here.)\n\nSTEP 7. REPORT\n")
out = s.encode()
assert s.count(chr(0x2014)) == dashes and len(out) <= 65536 - 200
open(dst, "wb").write(out)
print("sweep", len(out), hashlib.sha256(out).hexdigest()[:16])
