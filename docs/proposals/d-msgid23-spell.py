"""Cleanup's post-deploy check of d-msgid23 (26 Oct, 12:02 JST run), and one spelling the lookup still misses.
Usage: python3 d-msgid23-spell.py <d-msgid23-fallback out dir> <out dir>
Five 22 Oct Activities are keyed "msgid:gmail:<Gmail id>" (e.g. Shoaib, White Marque: "msgid:gmail:1a16301d826f4b7b"
next to its duplicate "gmail:1a16301d826f4b7b"). The live lookup matches a Source ID *equal to* the Gmail id with or
without "gmail:", so a re-read of such a mail logs it again. The lookup now matches any Source ID containing the Gmail id
(16 hex characters, unique in practice). Inbox on d-msgid23-fallback's output (61,903 / 43c8b79d735e5772)."""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
INBOX = "trig_0189eZvAD8x4357cfevgZ3No"
s = open(os.path.join(src, f"{INBOX}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == (61903, "43c8b79d735e5772")
a = "Source ID equal to the Gmail id with or without \"gmail:\","
assert s.count(a) == 1
s = s.replace(a, "Source ID containing the Gmail id (\"gmail:\", \"msgid:gmail:\" or bare),")
a = "OR \"Source ID\" LIKE '%<part before @>%' for each Message-ID,"
assert s.count(a) == 1
s = s.replace(a, "OR \"Source ID\" LIKE '%<part before @>%' for each Message-ID and LIKE '%<Gmail id>%' for each Gmail id,")
b = s.encode()
open(os.path.join(out, f"{INBOX}.txt"), "wb").write(b)
print(INBOX, len(b), sha(b))
