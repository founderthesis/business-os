"""Inbox capture r12 (CTO, 3 Nov ~14:30 JST): the 14:02 run wrote "STEP 0L, 0A, STEP 0: not worked this run, stop time"
at minute 2.5 and never ran 0L's or 0A's SQL. Three edits on the live capture r11 (43,989 / 043dbe3a), nothing else:
1/ order gate, 2/ measured stop, 3/ 0L and 0A count lines first in the record's body.
Usage: python3 patch.py <capture r11.txt> <out.txt>. Each edit is asserted exactly once."""
import sys, hashlib
src, out = sys.argv[1], sys.argv[2]
b = open(src, "rb").read()
assert hashlib.sha256(b).hexdigest().startswith("043dbe3a"), "not capture r11 (43,989 / 043dbe3a)"
s = b.decode("utf-8")
EDITS = [
 # 3/ the record's first body lines are the 0L and 0A counts.
 ('page body = the "stamped:" line as built (first line, kept), then a line "pending:',
  'page body = first the lines "0L: <n> due, <n> worked" and "0A: <n> due, <n> worked (REF <n>, RAW <n>, adid <n>, fold <n>)" (due: the row count each SQL returned; worked: rows finished this run, by the path that settled them), then the "stamped:" line as built (kept), then a line "pending:'),
 # 2/ a stop for time is measured, and a skip of 0L or 0A is Failed.
 ('Work until the cap or STOP TIME, whichever comes first: ending earlier while due messages remain is Partial, "stopped early", listed in the report as a defect.',
  'Work until the cap or STOP TIME, whichever comes first: ending earlier while due messages remain is Partial, "stopped early", listed in the report as a defect. MEASURED STOP (CTO, 3 Nov): a stop for time, here or at STEP 0A\'s or STEP 0\'s window, is read from Bash date -u at that moment, never estimated, and the record says "stopped at minute <n> of <limit>" (minutes since the run\'s start; limit 18, or the window\'s own minute). Rows of this run\'s 0L or 0A batch left unworked while no measured limit has passed (STOP TIME, or 0A\'s window: 5 minutes after 0L ends or minute 10) make the run Failed, "0A skipped at minute <n>" (or "0L skipped at minute <n>"), never Partial.'),
 # 1/ order gate: 0L's SQL and 0A's SQL are the first two Notion queries after the run record.
 ('STEP 0L. LINK FIRST (through 2026-11-05; CTOA-03): right after the run record, before anything else, run this SQL on Activities:',
  'ORDER GATE (CTO, 3 Nov): after the run record (and OVERLAP\'s check), your first two Notion queries are STEP 0L\'s SQL and then STEP 0A\'s SQL, both run before STEP 1\'s search or any other MCP Emails call, each one\'s row count logged in the record as the "due" figure of its 0L or 0A line (RUN RECORD); then work 0L\'s rows, then 0A\'s. A run that searched mail first, or whose record lacks either line, is Failed, "order gate".\n\nSTEP 0L. LINK FIRST (through 2026-11-05; CTOA-03): right after the run record, before anything else, run this SQL on Activities:'),
]
for a, c in EDITS:
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, c)
assert "—" not in s
ob = s.encode("utf-8")
assert len(ob) <= 65536 - 200
open(out, "wb").write(ob)
print(len(ob), hashlib.sha256(ob).hexdigest()[:16])
