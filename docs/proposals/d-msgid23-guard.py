"""Cleanup on d-msgid23-fix.py (bf83d15): accepted with one guard. Usage: python3 d-msgid23-guard.py <d-msgid23-fix out dir> <out dir>
The widened lookup matches any Source ID that contains a Message-ID's part before @. Our own ids are long UUIDs, but an
outside sender's Message-ID can have a short local part ("<1234@example.com>"), which would match unrelated rows and stop
a real mail being logged. Under 16 characters, the part is matched exactly ("msgid:<part>@...", or the bare Message-ID).
Order on the inbox: d-msgid23.py (61,442), d-msgid23-fix.py (61,723 / 97126cc3f3501dac), this, then d-slots407.py with
its base check moved to this output (the two anchors don't overlap)."""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
INBOX = "trig_0189eZvAD8x4357cfevgZ3No"
s = open(os.path.join(src, f"{INBOX}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == (61723, "97126cc3f3501dac")
a = "\"mcpemails:<that part>\"); any hit means it is logged,"
b = ("\"mcpemails:<that part>\"; a part under 16 characters is matched exactly, never as a substring); any hit means it is logged,")
assert s.count(a) == 1
s = s.replace(a, b)
b = s.encode()
open(os.path.join(out, f"{INBOX}.txt"), "wb").write(b)
print(INBOX, len(b), sha(b))
