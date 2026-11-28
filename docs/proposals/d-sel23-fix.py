"""Cleanup on d-sel23.py (08b6c10): accepted; one trim for headroom. Usage: python3 d-sel23-fix.py <d-sel23 out dir> <out dir>
d-sel23.py on live Zoya 64,340 / 6a82808cd870fbae gives 64,959 / 6cd33a24fa8ab061, 377 B under the 65,336 ceiling. The
paragraph's incident note repeats what the commit and d-sel23.md already record; cut to the source and date. The rule is
unchanged. The same cut goes into routines/zoya/parts/followups.txt."""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
ZOYA = "trig_01UPT8LDrBDL5JQqW91Awgbo"
A = ("SELECT BY STATUS AND DATE (Codex, 23 Oct: a run said nothing was due with 29 rows past their Next date Waiting on "
     "Guest or PR). ")
B = "SELECT BY STATUS AND DATE (Codex, 23 Oct). "
if __name__ == "__main__":
    s = open(os.path.join(src, f"{ZOYA}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == (64959, "6cd33a24fa8ab061")
    assert s.count(A) == 1
    s = s.replace(A, B)
    b = s.encode()
    open(os.path.join(out, f"{ZOYA}.txt"), "wb").write(b)
    print(ZOYA, len(b), sha(b), "under the 65,336 ceiling by", 65336 - len(b))
