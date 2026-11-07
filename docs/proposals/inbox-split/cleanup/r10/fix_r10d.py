"""Cleanup on actions r10d (2 Nov): three REPAIR guards. Input: r10/actions.txt 43,621 / 97190a21b962a5fc.
B1 Status, Tier, Your call and decisions are guarded too; B2 an unknown set time counts as newer; B3 REPAIR never cancels
an invite or deletes a draft. Usage: python3 fix_r10d.py <in> <out>."""
import hashlib, sys
s = open(sys.argv[1], encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:16] == "97190a21b962a5fc"
d = s.count(chr(0x2014))
a = "a 443 or 444 step replaces the chase segment for that person, and its Next date, as STEP 3 says."
assert s.count(a) == 1, s.count(a)
s = s.replace(a, a + " A value whose set date can't be shown older than this mail counts as newer. Never change Status, Tier "
    "or Your call, or undo a decision, set after this mail (a closed outcome on a row moved since goes to Akshay's list "
    "instead). Never cancel an invite or delete a draft from a recovered mail (a cancel still due goes to Akshay's list).")
b = s.encode(); assert s.count(chr(0x2014)) == d and len(b) <= 65536
open(sys.argv[2], "wb").write(b); print(len(b), hashlib.sha256(b).hexdigest()[:16])
