"""Cleanup on d-sweep24.py (5dd1ed7): accepted with one line. Usage: python3 d-sweep24-fix.py <d-sweep24 out dir> <out dir>
d-sweep24.py on the live sweep 32,478 / 6acd0d5b1ce40f20 gives 33,768 / 6b22fa05d3da7d92.
Fix: a second run of the same part on the same day (a retry, or a manual fire) would log a second report Activity under
the same Source ID; it now updates the existing one, so each part has one report a day and the next run reads the latest."""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
SWEEP = "trig_01MdfUFg2qrebDWgiHwncgnd"
s = open(os.path.join(src, f"{SWEEP}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == (33768, "6b22fa05d3da7d92")
dashes = s.count("—")
a = "Source ID \"sweep:<A|B>:<today>\", the report in the page body.\n"
b = "Source ID \"sweep:<A|B>:<today>\", the report in the page body; one already there for today is updated, never a second.\n"
assert s.count(a) == 1
s = s.replace(a, b)
b = s.encode()
assert s.count("—") == dashes
open(os.path.join(out, f"{SWEEP}.txt"), "wb").write(b)
print(SWEEP, len(b), sha(b))
