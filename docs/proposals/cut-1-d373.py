"""Decision 373 (CTO, 59a9f5b), composed on Cut 1: the calendar's attendee capture paragraph after the STEP 1 match,
and Zoya's guest-facing To rule in SENDING. Text is taken verbatim from routines/*.md at 59a9f5b.
Usage: python3 cut-1-d373.py <cut-1 out dir> <out dir>"""
import sys, os, hashlib, subprocess
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
def at(path):
    return subprocess.run(["git", "show", f"59a9f5b:{path}"], capture_output=True, text=True, check=True).stdout
cal = [l for l in at("routines/calendar.md").splitlines() if l.startswith("Attendee capture (decision 373")]
zl = at("routines/zoya.md")
i = zl.index("Guest-facing mail (day-before note"); j = zl.index("company-side address exists. ", i) + len("company-side address exists. ")
EDITS = {
 "trig_01Voiz5YsK2SnVf2STF8PoSH": ("If nothing matches, STEP 1a.\n", "If nothing matches, STEP 1a.\n\n" + cal[0] + "\n"),
 "trig_01UPT8LDrBDL5JQqW91Awgbo": ("move everyone else to Cc, Akshay included. ", "move everyone else to Cc, Akshay included. " + zl[i:j]),
}
assert len(cal) == 1
for tid in ["trig_0189eZvAD8x4357cfevgZ3No", "trig_01UPT8LDrBDL5JQqW91Awgbo", "trig_01Voiz5YsK2SnVf2STF8PoSH", "trig_01MdfUFg2qrebDWgiHwncgnd", "trig_01MnmJYorWrd61K7b5BCqXr1"]:
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    if tid in EDITS:
        o, n = EDITS[tid]; assert s.count(o) == 1, tid; s = s.replace(o, n)
    b = s.encode(); assert len(b) <= 65536 - 200
    open(os.path.join(out, f"{tid}.txt"), "w", encoding="utf-8").write(s)
    print(tid, len(b), hashlib.sha256(b).hexdigest()[:16])
