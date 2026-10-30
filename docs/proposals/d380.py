"""Decision 380 (Akshay, 21 Oct, via the CTO): on a thread Zoya is not on where we wrote last, she sends a fresh mail to
the current contact instead of putting it on Akshay's list. Zoya only, on the live composite (55,192 / ef291b33bb692d3b).
Usage: python3 d380.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
ZOYA = "trig_01UPT8LDrBDL5JQqW91Awgbo"
s = open(os.path.join(src, f"{ZOYA}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == (55192, "ef291b33bb692d3b")
a = "If we wrote last, send nothing and put \"Akshay: Zoya isn't on <guest>'s thread, <mail> waiting\" on his list."
b = ("If we wrote last (decision 380): send a fresh mail from your inbox to the current contact (read the thread and any later "
     "mail from that agency for a handover; a PR who left is replaced by whoever took over), Cc the rest of their side and Akshay, "
     "one opening line picking up the earlier conversation, then the approved wording; never on a closed or declined row. "
     "No current contact can be found (no one took over): send nothing and put it on Akshay's list as before.")
assert s.count(a) == 1
s = s.replace(a, b)
# Cleanup: the ad@ fallback said "reply-all", missed by the Cut 1 reply_all fix; recipients are set explicitly (OUTSIDE MAIL).
a = "send its mail from ad@thepodium.in instead, reply-all on its latest message,"
assert s.count(a) == 1
s = s.replace(a, "send its mail from ad@thepodium.in instead, a reply on its latest message with To and Cc set explicitly (OUTSIDE MAIL),")
b = s.encode()
assert len(b) <= 65536 - 200 and "—" not in s
open(os.path.join(out, f"{ZOYA}.txt"), "wb").write(b)
print(ZOYA, len(b), sha(b))
