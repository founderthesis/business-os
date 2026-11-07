"""r24 for inbox capture (CTO, 7 Nov 20:55 JST; Cleanup's r23 S1): RAWID treats a result with no sha256 as NONE, so
every id it prints comes from a checksum-verified message. Built on the live r23 capture (c31d1295).
Usage: python3 patch.py cap <r23/capture.txt> <out>. The edit is asserted once; no new em dash; size cap."""
import sys, hashlib
which, src, out = sys.argv[1], sys.argv[2], sys.argv[3]
assert which == "cap"
b = open(src, "rb").read()
assert hashlib.sha256(b).hexdigest().startswith("c31d1295"), "not the live r23 capture"
s = b.decode("utf-8")
EDITS = [
 ('if o.get("sha256") and hashlib.sha256(b).hexdigest()!=o["sha256"]:print("NONE sha256 mismatch");sys.exit()',
  'if not o.get("sha256") or hashlib.sha256(b).hexdigest()!=o["sha256"]:print("NONE sha256 missing or mismatch");sys.exit()'),
]
for a, c in EDITS:
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, c)
assert s.count(chr(0x2014)) == b.decode("utf-8").count(chr(0x2014)), "new em dash"
ob = s.encode("utf-8"); assert len(ob) <= 65536 - 200, len(ob)
open(out, "wb").write(ob); print(which, len(ob), hashlib.sha256(ob).hexdigest()[:16])
