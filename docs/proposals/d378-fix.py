"""Cleanup on decision 378 rev 2 as carried in d378.py at 78be855 (Main folded in Cleanup's earlier fixes).
Without booking: accepted as is, WhatsApp 24,701 / 2fea6fc12f7e2e24 on the live base 21,598 / 0b4dda9276486041. No fix needed.
With BOOKING 1 (only after Akshay's own ok): d378.py gives 25,202 / 269a436c477194c2; run this on it for the one fix below,
which gives 25,285 / 1c58ce0b16317ee2. Fix: the slot is re-read just before the write, and the length is what they ask, else 30 minutes.
Usage: python3 d378-fix.py <d378 BOOKING out dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
WA = "trig_01MnmJYorWrd61K7b5BCqXr1"
s = open(os.path.join(src, f"{WA}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == (25202, "269a436c477194c2"), "run on d378.py BOOKING 1 output"
a, b = "and create_event there:", "re-read that slot just before you write, and create_event there for the length they ask (else 30 minutes):"
assert s.count(a) == 1
s = s.replace(a, b)
b = s.encode()
open(os.path.join(out, f"{WA}.txt"), "wb").write(b)
print(WA, "BOOKING", len(b), sha(b))
