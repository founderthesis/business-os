"""Codex finding 2, CTO 23 Oct: Zoya's 22 Oct acknowledgement to Pranav (ITUS) has two Activities,
40119a301a7f813484e9f6d68bfa6788 ("msgid:d3229f3c-...@mcpemails.com", logged by Zoya at send) and
40119a301a7f812caafed69e76703f23 ("gmail:1a163a17a75785e4", made by the inbox at 13:06 UTC from the ad@ Cc copy).
Trace: the Gmail connector returns no headers in its default, PLAIN_TEXT, MINIMAL or METADATA_ONLY reads; only
messageFormat RAW carries Message-ID. Read RAW, the header is "<d3229f3c-8d04-4f34-b13f-ec7a76dc2ad5@mcpemails.com>",
and an exact SQL lookup of "msgid:d3229f3c-8d04-4f34-b13f-ec7a76dc2ad5@mcpemails.com" finds Zoya's Activity (checked
23 Oct). So MESSAGE IDENTITY's fallback ("the provider's own id only when the header can't be read") fired on every
Gmail read, and a provider id can never match an Activity the other mailbox keyed by msgid. Fix: read RAW for the
header, and when it still can't be read, match Zoya's own sends by row, day and recipient before creating anything.
Inbox on the live prompt (60,868 / f9ddfac269b790e4). Usage: python3 d-msgid23.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
INBOX = "trig_0189eZvAD8x4357cfevgZ3No"
BASE = (60868, "f9ddfac269b790e4")
OLD = "(the provider's own id only when the header can't be read). "
NEW = ("(the provider's own id only when the header can't be read). In Gmail only messageFormat RAW carries the header "
       "(Codex, 23 Oct: Zoya's acknowledgement to Pranav got a second Activity keyed \"gmail:\" because the other reads "
       "have no headers): for each new message under 200 KB (sizeEstimate), get it as RAW, decode it in Bash and keep "
       "only its Message-ID line. When the header still can't be read, before creating an Activity keyed by a provider "
       "id: a mail From Zoya's address is logged by Zoya, so look for a \"Zoya sent:\" Activity on the same Engagement "
       "captured that day (JST) to the same recipient; a hit is that mail, create nothing. ")
s = open(os.path.join(src, f"{INBOX}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == BASE, (len(s.encode()), sha(s.encode()))
dashes = s.count("—")
assert s.count(OLD) == 1, s.count(OLD)
s = s.replace(OLD, NEW)
b = s.encode()
assert len(b) <= 65536 - 200 and s.count("—") == dashes, len(b)
open(os.path.join(out, f"{INBOX}.txt"), "wb").write(b)
print(INBOX, len(b), sha(b))
