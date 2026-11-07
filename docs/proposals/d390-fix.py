"""Cleanup on d390.py rev 3 (3b2bc4f): accepted with one line in Zoya. Usage: python3 d390-fix.py <d390 out dir> <out dir>
d390.py on the live bases gives Zoya 60,398 / 2b0c6d0bd8908ace, inbox 60,397 / e5a2339a8fdbd848, calendar 55,616 /
48c2e04fc2ac846c (inbox and calendar accepted as they are).
Fix: a holding reply can start two ways in one run (the inbox queues "Zoya: holding reply to <who>" for a mail to ad@ that
also reached Zoya, and her own STEP 1 c answers the same message). The queued step now checks the thread first, so the
person never gets two."""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
ZOYA = "trig_01UPT8LDrBDL5JQqW91Awgbo"
s = open(os.path.join(src, f"{ZOYA}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == (60398, "2b0c6d0bd8908ace")
dashes = s.count("—")
a = "Log \"Zoya sent: holding reply to <name>\"; Akshay's item stays."
b = ("Log \"Zoya sent: holding reply to <name>\"; Akshay's item stays. A queued \"Zoya: holding reply to <who>\" step (the inbox "
     "sets it) follows the same check: if the thread already has a holding reply from the last 7 days, take the step out and "
     "send nothing.")
assert s.count(a) == 1
s = s.replace(a, b)
b = s.encode()
assert len(b) <= 65536 - 200 and s.count("—") == dashes
open(os.path.join(out, f"{ZOYA}.txt"), "wb").write(b)
print(ZOYA, len(b), sha(b))
