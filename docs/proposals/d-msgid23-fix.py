"""Dry run on d-msgid23 (24 Oct, 234 ad@ mails, 22 to 23 Oct JST): Pranav's mail matched, but the lookup missed 29
logged mails, so it fails Cleanup's zero-new-rows gate. Older Activities key one mail under several spellings: a bare
Gmail id (no "gmail:"), a bare Message-ID (no "msgid:"), and "mcpemails:<the Message-ID's part before @>" (checked:
mcpemails:288d6eed-... is Message-ID <288d6eed-...@mcpemails.com>, Gmail 1a16166b07e83d02); one older row has
"mcpemails:<full Message-ID in brackets>". Fix: look up every spelling, matching on the part before @ so all forms of
one Message-ID hit. New rows still use "msgid:". Inbox on d-msgid23's output (61,442 / f362e24b8767cd72).
Usage: python3 d-msgid23-fix.py <d-msgid23 out dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
INBOX = "trig_0189eZvAD8x4357cfevgZ3No"
BASE = (61442, "f362e24b8767cd72")
OLD = ("Before creating a mail Activity, look up that key and the provider ids you hold for the message (Gmail id, MCP "
       "Emails id): any hit means it is logged, so add only a missing link. ")
NEW = ("Before creating a mail Activity, look up that key and the provider ids you hold for the message (Gmail id, MCP "
       "Emails id) in every spelling older rows use: Source ID equal to the Gmail id with or without \"gmail:\", or "
       "containing the Message-ID's part before @ (it covers \"msgid:\", a bare Message-ID and \"mcpemails:<that "
       "part>\"); any hit means it is logged, so add only a missing link. ")
OLD2 = '(SQL, "Source ID" IN (...), 50 at a time; '
NEW2 = '(SQL, "Source ID" IN (...) for the ids and OR "Source ID" LIKE \'%<part before @>%\' for each Message-ID, 50 at a time; '
s = open(os.path.join(src, f"{INBOX}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == BASE, (len(s.encode()), sha(s.encode()))
assert s.count(OLD) == 1, s.count(OLD)
s = s.replace(OLD, NEW)
assert s.count(OLD2) == 1, s.count(OLD2)
s = s.replace(OLD2, NEW2)
b = s.encode()
assert len(b) <= 65536 - 200, len(b)
open(os.path.join(out, f"{INBOX}.txt"), "wb").write(b)
print(INBOX, len(b), sha(b))
