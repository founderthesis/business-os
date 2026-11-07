"""Inbox: cap the read, never refuse it (CTO, 30 Oct 08:20 JST). The 08:03 run called a 12-hour backlog (about 40 messages)
"larger than one run can capture" and logged 0, so read to never moved. Input: the live inbox, 65,336 / 403f49ac840dc31b
(the inbox-writes hotfix). Usage: python3 patch.py <live.txt> <out.txt>."""
import hashlib, os, sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:16] == "403f49ac840dc31b"
dashes = s.count(chr(0x2014))

def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)

# The cap. "read to" (RUN RECORD) already means the newest received time up to which every message was logged or skipped
# as noise, so messages not reached simply sit after it; "pending" stays for messages that failed.
rep("Keep only messages received at or after T, one copy per RFC Message-ID",
    "Keep only messages received at or after T and work them oldest received first, at most 15 not yet logged a run (then Partial); the rest wait "
    "for the next run (not pending). A backlog never means working none. One copy per RFC Message-ID")

# Room: explanations only, no rule changes.
rep(" (a run whose read never finished has none, so its span is read again)", "")
rep(" (Zoya logs ad@ mail too)", "")
rep(" (a date matches from midnight UTC)", "")
rep("nothing (an unclear create response: query that Source ID, reuse the row if found, else create it once; never a second).",
    "nothing (unclear create: query that Source ID first; never a second row).")

out = s.encode()
assert s.count(chr(0x2014)) == dashes and len(out) <= 65536 - 200, len(out)
open(dst, "wb").write(out)
print(os.path.basename(dst), len(out), hashlib.sha256(out).hexdigest()[:16], "headroom", 65536 - 200 - len(out))
