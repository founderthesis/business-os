"""Codex CX-20261026-dedupe-fallback (26 Oct): live inbox STEP 2's fallback (header unreadable, e.g. over 200 KB) treats a
same-day "Zoya sent:" Activity on the same Engagement to the same recipient as this mail, so two different mails that
share those attributes would be merged and the second never logged. Fix: match only by identity. For each such Activity
whose Source ID holds a Message-ID, Gmail search rfc822msgid:<that Message-ID> (no RAW download, any size); a result with
this mail's Gmail id is the same mail. Date and recipient alone never match. Inbox on d-blurb26's output
(61,754 / 77d366ae3c8e8d28). Usage: python3 d-msgid23-fallback.py <d-blurb26 out dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
INBOX = "trig_0189eZvAD8x4357cfevgZ3No"
OLD = ("a mail From Zoya's address is logged by Zoya, so look for a \"Zoya sent:\" Activity on the same Engagement captured "
       "that day (JST) to the same recipient; a hit is that mail, create nothing.")
NEW = ("a mail From Zoya's address is logged by Zoya, so for each \"Zoya sent:\" Activity on the same Engagement captured "
       "that day (JST) whose Source ID holds a Message-ID, search Gmail rfc822msgid:<that Message-ID>; one that returns "
       "this mail's Gmail id is this mail, create nothing. Date and recipient alone never match: two mails are two rows.")
s = open(os.path.join(src, f"{INBOX}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == (61754, "77d366ae3c8e8d28"), (len(s.encode()), sha(s.encode()))
assert s.count(OLD) == 1
s = s.replace(OLD, NEW)
b = s.encode()
assert len(b) <= 65536 - 200
open(os.path.join(out, f"{INBOX}.txt"), "wb").write(b)
print(INBOX, len(b), sha(b))
