"""Cleanup on d-thread26.py (ef5d367): accepted with two changes, net smaller. Usage: python3 d-thread26-fix.py <d-thread26 out dir> <out dir>
d-thread26.py on live Zoya 65,160 / bdc550a275e6957d gives 65,219 / fa1a541c2bb37f7c (117 B under the 65,336 ceiling).
1/ Read-back before every send (Codex CX-20261026-02): the delta read back only the team-wrote-last drafts; a plain
   email_compose reply went out unchecked. Every reply is now a draft reply, read back (To, Cc, thread), then sent.
2/ One company, two threads (MaxVolt's Vishal and Mukesh): "one shared thread" would defer the second guest a week when
   the company's two rows sit on two threads. Rows of one company may share one mail, on the more urgent row's thread;
   different companies (Findoc, Scalar Field) never do.
The same edits go into routines/zoya/parts (python3 d-thread26-fix.py --parts)."""
import sys, os, hashlib
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
ZOYA = "trig_01UPT8LDrBDL5JQqW91Awgbo"
EDITS = [
 ("is a reply (email_compose action reply, or draft action reply then send) on the original thread's latest message",
  "is a draft action reply, read back (To, Cc, thread) and then sent, on the original thread's latest message"),
 ("Rows on one shared thread (one company) may share one mail;", "Rows of one company may share one mail, on the more urgent row's thread;"),
 ("one mail covers both only if both are on one thread (one company);", "one mail covers both only if both are one company;"),
]
if sys.argv[1] == "--parts":
    d = "routines/zoya/parts"
    for a, b in EDITS:
        hits = [f for f in os.listdir(d) if a in open(os.path.join(d, f), encoding="utf-8").read()]
        print(a[:40], hits)
        for f in hits:
            p = os.path.join(d, f); s = open(p, encoding="utf-8").read(); open(p, "w", encoding="utf-8").write(s.replace(a, b))
else:
    src, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    s = open(os.path.join(src, f"{ZOYA}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == (65219, "fa1a541c2bb37f7c")
    for a, b in EDITS:
        assert s.count(a) == 1, a[:50]
        s = s.replace(a, b)
    b = s.encode()
    assert len(b) <= 65536 - 200
    open(os.path.join(out, f"{ZOYA}.txt"), "wb").write(b)
    print(ZOYA, len(b), sha(b), "headroom", 65336 - len(b))
