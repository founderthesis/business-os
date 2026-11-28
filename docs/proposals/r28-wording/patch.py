"""r28 wording (Main 2, 13 Nov): decisions 571 and 569, Akshay 13 Nov.
- 571: the holding line becomes "will get back to you on this" (was "checking with akshay, will come back to you").
- 569: the BOOKING LINKS example names podm.in/30min as a 30-minute planning call with Akshay; never "pick any slot available on this link".
Usage: python3 docs/proposals/r28-wording/patch.py  (edits the files in place; each edit asserted, no new em dash, size cap)."""
import hashlib
A_OLD = '"hi <first name>, checking with akshay, will come back to you."'
A_NEW = '"hi <first name>, will get back to you on this." (decision 571)'
B_OLD = '"you can pick any slot available on this link: podm.in/30min"; never a paragraph or line break of its own.'
B_NEW = ('"you can book a 30-minute planning call with Akshay here: podm.in/30min" (decision 569: podm.in/30min is always named as a 30-minute planning call with Akshay, '
         'never "pick any slot available on this link"); never a paragraph or line break of its own.')
FILES = {
 "routines/zoya.md": [A_OLD],
 "routines/zoya/parts/mail.txt": [A_OLD],
 "routines/zoya/release/zoya-one.txt": [A_OLD],
 "routines/zoya/release/zoya-slow-work.txt": [B_OLD],
 "docs/proposals/zoya-day/prompts/zoya-fast.txt": [A_OLD, B_OLD],
 "docs/proposals/zoya-day/prompts/zoya-slow.txt": [B_OLD],
}
NEW = {A_OLD: A_NEW, B_OLD: B_NEW}
for path, olds in FILES.items():
    b = open(path, "rb").read(); s = b.decode("utf-8"); d = s.count("—")
    before = (len(b), hashlib.sha256(b).hexdigest()[:16])
    for old in olds:
        assert s.count(old) == 1, (path, old[:40])
        s = s.replace(old, NEW[old])
    assert "checking with akshay, will come back" not in s and "pick any slot available on this link:" not in s, path
    assert s.count("—") == d, path
    o = s.encode("utf-8")
    if path not in ("routines/zoya.md", "routines/zoya/release/zoya-slow-work.txt"):  # the SLOW work file is read from the pin, not a trigger prompt
        assert len(o) < 65536, (path, len(o))
    open(path, "wb").write(o)
    print(path, before, "->", len(o), hashlib.sha256(o).hexdigest()[:16])
