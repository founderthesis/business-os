"""Cleanup's fix to decision 382/383 (d382.py at 9dfd788), applied to its output. Usage: python3 d382-fix.py <d382 out dir> <out dir>
d382.py gives Zoya 57,293 / 59bb6008a32a21d8, sweep 31,650 / 554309495f5c594d, inbox 59,199 / c6d54995de67c48e and calendar
54,860 / 1a3e320af3b2cb9b (calendar unchanged by this fix).
Decision 382 part 3 was not built: a recording-slot chase that runs out goes to long-term check-ins whoever pitched, but the new
direct-founder branch caught it first and sent it to Akshay's list. The branch now lets those through to nurture."""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
BASE = {"trig_01UPT8LDrBDL5JQqW91Awgbo": (57293, "59bb6008a32a21d8"), "trig_01MdfUFg2qrebDWgiHwncgnd": (31650, "554309495f5c594d"),
        "trig_0189eZvAD8x4357cfevgZ3No": (59199, "c6d54995de67c48e"), "trig_01Voiz5YsK2SnVf2STF8PoSH": (54860, "1a3e320af3b2cb9b")}
A = "and Tier not Sponsored (decision 382): don't move it and send nothing;"
B = ("and Tier not Sponsored (decision 382), unless it is a recording-slot chase (Status Booking) that ran out, which goes to "
     "nurture whoever pitched (decision 382, part 3): don't move it and send nothing;")
for tid, base in BASE.items():
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == base, tid
    dashes = s.count("—")
    if tid != "trig_01Voiz5YsK2SnVf2STF8PoSH":
        assert s.count(A) == 1, tid
        s = s.replace(A, B)
    b = s.encode()
    assert len(b) <= 65536 - 200 and s.count("—") == dashes, tid
    open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
    print(tid, len(b), sha(b))
