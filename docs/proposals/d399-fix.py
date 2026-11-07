"""Cleanup on d399.py (b60db17): accepted; one trim for headroom. Usage: python3 d399-fix.py <d399 out dir> <out dir>
d399.py gives inbox 60,868 / f9ddfac269b790e4 (accepted as is) and Zoya 64,404 / e3d24df7f8c76e80, which leaves Zoya 932 B
under the 65,336 build ceiling (1,132 under the 65,536 cap). The quoted example of Anuj Jain's company description adds
bytes and a guest's details to the prompt without changing the rule ("strip any description of the guest's company" is
enough with LEAK CHECK's ban), so it goes. The inbox needs nothing: its line is a straight replacement and shorter."""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
ZOYA = "trig_01UPT8LDrBDL5JQqW91Awgbo"
s = open(os.path.join(src, f"{ZOYA}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == (64404, "e3d24df7f8c76e80")
a = "first strip any description of the guest's company, such as \"(supply chain tech and RFID, 25+ years in the space)\": name the company and stop, decision 399),"
assert s.count(a) == 1
s = s.replace(a, "first strip any description of the guest's company: name the company and stop, decision 399),")
b = s.encode()
open(os.path.join(out, f"{ZOYA}.txt"), "wb").write(b)
print(ZOYA, len(b), sha(b), "under the 65,336 ceiling by", 65336 - len(b))
