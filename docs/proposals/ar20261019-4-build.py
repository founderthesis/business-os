"""AR-20261019-4: narrow the Built to Share block in the Salesblink sync to the cold-outreach pause (Akshay, 19 Oct:
"keep only the cold-outreach pause"; narrows decision 337, keeps decision 328). Run: python3 -I psb.py <root>"""
import sys, os, re
ROOT = sys.argv[1]
OLD = 'BUILT TO SHARE ON HOLD (Chaandini, 19 Oct: "we pause outreach for everyone - do not mention any followup date - every thing is on hold"). On Built to Share rows (any B2S sequence) apply none of a), b), d), e), f) or h): never set a Next date, never set Waiting on, never move Status, never create rows. Leave Next action alone when it starts "On hold". The only B2S write: a new reply from a lead. Append one Claude note line with what they said, put "Replied <date>: <one-line gist>. Chaandini to decide (outreach on hold)" in front of the Next action (keep the rest after " | "), Waiting on Chaandini, no Next date; a clear no is still They declined. Human by Design is not on hold: a) to h) apply to HBD as written. This lasts until Chaandini lifts the hold.'
NEW = ('BUILT TO SHARE COLD OUTREACH PAUSED (Akshay, 19 Oct, AR-20261019-4: "keep only the cold-outreach pause"; narrows decision 337). Until the pause is lifted, on Built to Share rows only the cold steps change: '
 'a) and d) still record Status and Chase step from Salesblink but set no Next date and no Waiting on; f) does not run (no Unresponsive move, no Re-engage date); and a Next action that starts "On hold" keeps that text in front, anything new after " | ". '
 'Everything else applies as written: b) bounces, e) new rows (state as a) above), g), h) connect safety, and c) every reply in full. A reply is never cold: its Status, owner and dated next step follow c), its step replaces an "On hold" cold note on that row (the old note goes into the Claude note), and nothing here ever leaves a reply without an owner. '
 'Decision 328 still holds: a Built to Share approval given before 18 Oct counts for nothing, so a reply on such a row follows c) and asks Satish afresh, and a row, person or show restriction in its Claude note or "## Standing" still stands. Human by Design: a) to h) as written.')
p = os.path.join(ROOT, 'routines', 'salesblink-sync.md')
s = open(p, encoding='utf-8').read()
assert s.count(OLD) == 1, s.count(OLD)
s = s.replace(OLD, NEW)
open(p, 'w', encoding='utf-8', newline='').write(s)
t = re.search(r'```text\n(.*?)\n```', s, re.S).group(1)
import hashlib; print('salesblink-sync', len(t.encode()), hashlib.sha256(t.encode()).hexdigest()[:16])
