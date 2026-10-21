"""Cleanup on d382.py rev 5 (5e991ec). Main folded in Cleanup's part-3 fix (Booking rows skip the direct-founder branch).
One fix left, for WhatsApp only: the booking build went live as 25,202 / 269a436c477194c2 without d378-fix.py's line, so the
slot is still not re-read before the write and has no default length. This adds it on d382.py's WhatsApp output.
d382.py on the live bases gives: Zoya 58,324 / 3dacc1864b8a1de0, sweep 32,333 / 2a3fbdb8fbc35ccb, inbox 60,110 / 053ae63d99a0191d,
calendar 55,437 / a92b0f73e7bba1db (all accepted as they are), WhatsApp 25,777 / 07af8cf65e033c0e (run this on it).
Usage: python3 d382-fix.py <d382 out dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
WA = "trig_01MnmJYorWrd61K7b5BCqXr1"
s = open(os.path.join(src, f"{WA}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == (25777, "07af8cf65e033c0e"), "run on d382.py's WhatsApp output"
a, b = "and create_event there:", "re-read that slot just before you write, and create_event there for the length they ask (else 30 minutes):"
assert s.count(a) == 1
s = s.replace(a, b)
b = s.encode()
open(os.path.join(out, f"{WA}.txt"), "wb").write(b)
print(WA, len(b), sha(b))
