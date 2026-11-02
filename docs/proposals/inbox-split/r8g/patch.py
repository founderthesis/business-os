"""Capture r8g on r8f (CTO, 2 Nov 13:55 JST). Two runs (13:19, 13:37) ignored LINK inside STEP 0; give it its own step with the query.
Usage: python3 patch.py <r8f capture> <out>."""
import hashlib, sys
s = open(sys.argv[1], encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:8] == "b034a489"
d = s.count(chr(0x2014))
a = "STEP 0. OLD ROWS (one-off,"
assert s.count(a) == 1
s = s.replace(a, "STEP 0L. LINK FIRST (through 2026-11-05; CTOA-03): right after the run record, before anything else, run this SQL on Activities: "
    "SELECT url, \"Summary\" FROM <Activities> WHERE (\"Source ID\" LIKE 'msgid:%' OR \"Source ID\" LIKE 'adid:%') AND (\"People\" IS NULL OR \"People\" IN ('','[]')) "
    "AND (\"Engagement\" IS NULL OR \"Engagement\" IN ('','[]')) AND datetime(createdTime) >= datetime('2026-11-01T03:00:00Z') AND \"Summary\" NOT LIKE 'Zoya%' ORDER BY createdTime LIMIT 10. "
    "Fetch each; one whose body has a \"link:\" line is passed over; work every other one as STEP 0's LINK says (these are STEP 0's LINK rows, never deferred). "
    "Report line \"link: <n> linked, <n> internal, <n> no fit, <n> passed over\"; a report without it is Partial.\n\n" + a, 1)
b = s.encode(); assert s.count(chr(0x2014)) == d and len(b) <= 65536
open(sys.argv[2], "wb").write(b); print(len(b), hashlib.sha256(b).hexdigest()[:16])
