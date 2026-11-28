"""Codex finding 1, CTO 23 Oct (missed follow-ups): Zoya's 12:38 run reported nothing due while 29 rows dated today or
earlier sat Waiting on Guest or PR (17 sponsored, 12 precall, e.g. Pragati and Pavan Kumar, some on old "step R" plans).
STEP 2 never said how to pick candidates, so runs picked them by Waiting on. This adds the selection: pursuit Status plus
Next date, whoever the row waits on, then the existing skips and holds. Zoya on the live prompt (64,340 / 6a82808cd870fbae).
The same text goes into routines/zoya/parts/followups.txt for the split. Usage: python3 d-sel23.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
ZOYA = "trig_01UPT8LDrBDL5JQqW91Awgbo"
BASE = (64340, "6a82808cd870fbae")
OLD = "STEP 2. FOLLOW-UPS DUE\nIn-scope Engagements only. "
NEW = ("STEP 2. FOLLOW-UPS DUE\nSELECT BY STATUS AND DATE (Codex, 23 Oct: a run said nothing was due with 29 rows past their "
       "Next date Waiting on Guest or PR). Candidates are in-scope rows at Sponsored offered, Precall requested, Booking, "
       "Recorded or LT chase with Next date today or earlier, plus routine 4, 6 and 8 rows, whoever Waiting on names (Guest, "
       "PR, Zoya, Chaandini or no one): waiting on their side is why a follow-up is due, never a reason to skip. Then apply "
       "the skips and holds below. A plan naming a step its routine page no longer has (an old step R) is worked from Chase "
       "step and the thread. The report's due count is this selection.\nIn-scope Engagements only. ")
s = open(os.path.join(src, f"{ZOYA}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == BASE, (len(s.encode()), sha(s.encode()))
dashes = s.count("—")
assert s.count(OLD) == 1, s.count(OLD)
s = s.replace(OLD, NEW)
b = s.encode()
assert len(b) <= 65536 - 200 and s.count("—") == dashes, len(b)
open(os.path.join(out, f"{ZOYA}.txt"), "wb").write(b)
print(ZOYA, len(b), sha(b))
