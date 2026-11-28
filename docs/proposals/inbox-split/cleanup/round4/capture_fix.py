"""Cleanup's fix for round 4's four blockers (V1 to V4), applied to Main's capture.txt (35,848 / 0c7cb3d1a16d13bd).
Main can fold these into split.py; actions-v2, yourcall and sweep are unchanged. Usage: python3 capture_fix.py <in> <out>."""
import hashlib, sys
s = open(sys.argv[1], encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:16] == "0c7cb3d1a16d13bd"
dashes = s.count(chr(0x2014))
def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, b)
# V1: the record's last write keeps the "stamped:" line.
rep('page body = a line "pending: <Message-ID>, ..."',
    'page body = the "stamped:" line as built (first line, kept), then a line "pending: <Message-ID>, ..."')
# V2: list the id before stamping, so a crash can't lose the row.
rep('gets that line and any missing link, once, and you add its id to your record\'s body line "stamped: <ids>" as you stamp it',
    'first has its id written to your record\'s body line "stamped: <ids>", then gets that line and any missing link, once')
rep('There: add the "capture:" line and, if unlinked',
    'There: in one write add the "capture:" line and Captured today and, if unlinked')
# V3: a text search never finds a Message-ID in ad@ (tested live); the raw HEADER query does.
rep('rfc822msgid: email_read search with text = the Message-ID',
    'rfc822msgid: email_read search with query HEADER Message-ID "<id>" (text search never finds it)')
rep('(search text = it; mcp: ones by id)', '(query HEADER Message-ID "<it>"; mcp: ones by id)')
# V3 + V4: STEP 0's lookup, and its "add nothing" rows leave the queue.
rep('Else look for its message in ad@ (search text = the Message-ID). Not there: it is Zoya\'s, add nothing.',
    'Else look for its message in ad@ (query HEADER Message-ID "<id>"). Not there: it is Zoya\'s; only set Captured today.')
rep('an Email out whose Summary starts "Zoya" is hers: add nothing.',
    'an Email out whose Summary starts "Zoya" is hers; only set Captured today.')
out = s.encode()
assert s.count(chr(0x2014)) == dashes and len(out) <= 65536 - 200
open(sys.argv[2], "wb").write(out)
print(len(out), hashlib.sha256(out).hexdigest()[:16])
