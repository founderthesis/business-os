"""Cleanup on d382.py rev 5 (5e991ec). Main folded in Cleanup's part-3 fix (Booking rows skip the direct-founder branch).
One fix left, for WhatsApp only: the booking build went live as 25,202 / 269a436c477194c2 without d378-fix.py's line, so the
slot is still not re-read before the write and has no default length. This adds it on d382.py's WhatsApp output.
d382.py rev 6 (da1612c) on the live bases gives: Zoya 58,469 / ffc1a8f4b82d6c24, sweep 32,478 / 6acd0d5b1ce40f20, inbox
60,255 / 14fbb21f1a0993b8, calendar 55,582 / 4f28ce91cd6dbc3f (all accepted as they are), WhatsApp 25,922 / 6f2dc3c0001c6fdd
(run this on it).
Usage: python3 d382-fix.py <d382 out dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
WA = "trig_01MnmJYorWrd61K7b5BCqXr1"
s = open(os.path.join(src, f"{WA}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == (25922, "6f2dc3c0001c6fdd"), "run on d382.py's WhatsApp output"
a, b = "and create_event there:", "re-read that slot just before you write, and create_event there for the length they ask (else 30 minutes):"
assert s.count(a) == 1
s = s.replace(a, b)
b = s.encode()
open(os.path.join(out, f"{WA}.txt"), "wb").write(b)
print(WA, len(b), sha(b))
