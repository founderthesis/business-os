"""Inbox capture r13 (decision 457, Akshay, 3 Nov, Tab 13 item 16): a pitch with Akshay on To or Cc is capture's to log at
once. Zoya hands those to the inbox and never logs them, so the 2-hour wait for her left Eshna Malhotra's two un# pitches
unlogged. One edit on the live capture r12e (46,565 / 9caf2cdb). Usage: python3 patch.py <capture r12e.txt> <out.txt>."""
import sys, hashlib
src, out = sys.argv[1], sys.argv[2]
b = open(src, "rb").read()
assert hashlib.sha256(b).hexdigest().startswith("9caf2cdb"), "not capture r12e (46,565 / 9caf2cdb)"
s = b.decode("utf-8")
EDITS = [
 ('Mail Zoya is on: her routine logs it first; MSGID FIND. Found: logged (STEP 1\'s exception stamps it). None, under 2 hours old: leave it for the next run',
  'Mail Zoya is on: her routine logs it first; MSGID FIND. Found: logged (STEP 1\'s exception stamps it). A pitch from outside the team (a guest, sponsored, PR or vendor pitch) with ad@thepodium.in on To or Cc is never left for her (decision 457: her STEP 1 d hands it to the inbox and logs nothing): MSGID FIND first, then REF, then RAW by HEAD, this run, no wait. Any other, none found, under 2 hours old: leave it for the next run'),
]
for a, c in EDITS:
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, c)
assert "—" not in s
ob = s.encode("utf-8")
assert len(ob) <= 65536 - 200
open(out, "wb").write(ob)
print(len(ob), hashlib.sha256(ob).hexdigest()[:16])
