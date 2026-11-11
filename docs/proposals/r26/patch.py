"""r26 non-Zoya edits, built on the r25 builds (not yet live at writing; r25 is deployed first).
Usage: python3 patch.py act docs/proposals/r25/actions.txt <out>
- act: decision 557 (Akshay, 11 Nov): with no Tier named, a precall call picks its template from Eval verdict.
Each edit is asserted once; no new em dash; size cap."""
import sys, hashlib
which, src, out = sys.argv[1], sys.argv[2], sys.argv[3]
b = open(src, "rb").read()
BASE = {"act": "d0a8c26a"}
assert hashlib.sha256(b).hexdigest().startswith(BASE[which]), "not the r25 %s" % which
s = b.decode("utf-8")
EDITS = {
"act": [
 ("No Tier: pick the template from the instruction (pre-call -> Tier 1; alignment",
  "No Tier: pick the template from the instruction (pre-call -> by Eval verdict, decision 557: Book immediately or Strong consider Tier 1, Pre-call needed or Evaluate after call Tier 1.5, anything else or no eval Tier 2; alignment"),
],
}
for a, c in EDITS[which]:
    assert s.count(a) == 1, (which, a[:70], s.count(a))
    s = s.replace(a, c)
assert s.count(chr(0x2014)) == b.decode("utf-8").count(chr(0x2014)), "new em dash"
ob = s.encode("utf-8"); assert len(ob) <= 65536 - 200, (which, len(ob))
open(out, "wb").write(ob); print(which, len(ob), hashlib.sha256(ob).hexdigest()[:16])
