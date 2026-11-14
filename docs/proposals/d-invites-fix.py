"""Cleanup on d-invites.py (bf5fbea): accepted with two lines, paid for with two trims. Usage:
python3 d-invites-fix.py <d-invites out dir> <out dir>   (Zoya)
python3 d-invites-fix.py --parts                          (the same edits in routines/zoya/parts)
d-invites.py runs on d-sel23.py's output (64,959) and already carries d-sel23-fix's trim, so skip d-sel23-fix.py: the
order is d-sel23.py, d-invites.py, this. d-invites.py gives 65,201 / fd175c0e40522fdf, 135 B under the 65,336 ceiling.
1/ Invite before confirmation: the delta confirmed on the thread and then created the invite, so a failed create left
   their side holding a confirmed time with no invite and nothing on the calendar to block it. The invite comes first.
2/ Same-run clash: two rows confirmed in one run could take the same free slot, since each read the calendar before the
   other's invite existed. The check counts invites created earlier in the run.
Trims (citations only, rules unchanged): decision 392's note, and the Tanuj Shori / Mukund Jha example."""
import sys, os, hashlib
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
ZOYA = "trig_01UPT8LDrBDL5JQqW91Awgbo"
EDITS = [
 ("confirm on the thread and in the same run create the invite (", "create the invite, then confirm it on the thread in the same run ("),
 ("prep, cooling-off and Out of office entries included.", "prep, cooling-off and Out of office entries included, and invites you created earlier this run."),
 ("(decision 392, Akshay, 22 Oct: many readers use English as a second language)", "(decision 392)"),
 ("(Codex, 22 Oct: Tanuj Shori, Mukund Jha)", "(Codex, 22 Oct)"),
]
if sys.argv[1] == "--parts":
    d = "routines/zoya/parts"
    for a, b in EDITS:
        hits = [f for f in os.listdir(d) if a in open(os.path.join(d, f), encoding="utf-8").read()]
        assert len(hits) == 1, (a[:50], hits)
        p = os.path.join(d, hits[0]); s = open(p, encoding="utf-8").read()
        assert s.count(a) == 1
        open(p, "w", encoding="utf-8").write(s.replace(a, b)); print("part", hits[0])
else:
    src, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    s = open(os.path.join(src, f"{ZOYA}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == (65201, "fd175c0e40522fdf")
    for a, b in EDITS:
        assert s.count(a) == 1, a[:50]
        s = s.replace(a, b)
    b = s.encode()
    assert len(b) <= 65536 - 200
    open(os.path.join(out, f"{ZOYA}.txt"), "wb").write(b)
    print(ZOYA, len(b), sha(b), "under the 65,336 ceiling by", 65336 - len(b))
