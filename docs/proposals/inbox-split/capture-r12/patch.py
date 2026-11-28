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
  'page body = first the lines "0L: <n> due, <n> worked (<n> passed over)" and "0A: <n> due, <n> worked (meeting <n>, fold <n>, adid <n>, REF <n>, RAW <n>, pended <n>)" (due: the row count each SQL returned; worked: rows settled this run, by the path that settled them, a 0L row passed over for its "link:" line and a 0A row struck or pended with its record line included; a row left by a quota, rate-limit or 5xx error is not worked), then the "stamped:" line as built (kept), then a line "pending:'),
 # 2/ a stop for time is measured, and a skip of 0L or 0A is Failed.
 ('Work until the cap or STOP TIME, whichever comes first: ending earlier while due messages remain is Partial, "stopped early", listed in the report as a defect.',
  'Work until the cap or STOP TIME, whichever comes first: ending earlier while due messages remain is Partial, "stopped early", listed in the report as a defect. MEASURED STOP (CTO, 3 Nov): a stop for time, here or at STEP 0A\'s or STEP 0\'s window, is read from Bash date -u at that moment, never estimated, and the record says "stopped at minute <n> of <limit>" (minutes since the run\'s start; limit 18, or the window\'s own minute). Rows of this run\'s 0L or 0A batch left unworked while no measured limit has passed (STOP TIME, or 0A\'s window: 5 minutes after 0L ends or minute 10) make the run Failed, "0A skipped at minute <n>" (or "0L skipped at minute <n>"), never Partial; rows left only by a quota, rate-limit or 5xx error are Failed as RUN RECORD says, naming that error, never "skipped".'),
 # 1/ order gate: 0L's SQL and 0A's SQL are the first two Notion queries after the run record.
 ('STEP 0L. LINK FIRST (through 2026-11-05; CTOA-03): right after the run record, before anything else, run this SQL on Activities:',
  'ORDER GATE (CTO, 3 Nov): after the run record (and OVERLAP\'s check), your first two SQL queries (the data-source fetches and the run record\'s own checks aside) are STEP 0L\'s SQL and then STEP 0A\'s SQL, both run before STEP 1\'s search or any other MCP Emails call, each one\'s row count logged in the record as the "due" figure of its 0L or 0A line (RUN RECORD); then work 0L\'s rows, then 0A\'s. A run that searched mail first, or whose record lacks either line or gives a due figure no SQL returned (a line like "0L: not run" lacks it), is Failed, "order gate". OVERLAP\'s No-op record is exempt; with no record (RUN RECORD\'s no-id case), the two lines open the final report instead.\n\nSTEP 0L. LINK FIRST (through 2026-11-05; CTOA-03): right after the run record, before anything else, run this SQL on Activities:'),
 # r12c, decision 452: Gmail shows the HTML, so the loop-in's html_body carries the quoted chain.
 ('the loop-in (LOOP-IN) as body and html_body (<p>...</p>), no link,',
  'the loop-in (LOOP-IN) as body and html_body (<p>...</p>, then, decision 452, <div class="gmail_quote">On <date>, <name> &lt;<address>&gt; wrote:<br><blockquote style="margin:0 0 0 .8ex;border-left:1px solid #ccc;padding-left:1ex">[the pitch message, read with action read and include_html true, its full body; only the innermost message from outside the team, with every forward layer and every note by Akshay, Saurabh or anyone tagged Team removed; unsure: no quote; its HTML body\'s inner content (no <html>, <head>, <body>, <style> or <script>, no cid: images), else its text HTML-escaped with each line break as <br>]</blockquote></div>, its date, name and address from that message\'s own Date and From headers (that innermost message\'s own); the plain-text body keeps MCP Emails\' own quote; a draft or send whose html lacks the blockquote is fixed before it goes), no link,'),
 # r12d, replay D8: include_html is allowed for the loop-in quote.
 ('include_html only where a step needs HTML (Gemini notes)',
  "include_html only where a step needs HTML (Gemini notes, the loop-in's quote, decision 452)"),
]
for a, c in EDITS:
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, c)
assert "—" not in s
ob = s.encode("utf-8")
assert len(ob) <= 65536 - 200
open(out, "wb").write(ob)
print(len(ob), hashlib.sha256(ob).hexdigest()[:16])
