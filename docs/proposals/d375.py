"""Decision 375 (Akshay, 21 Oct, via the CTO): a hand-written mail pauses a thread's sequence for 4 working days, not 14, and
with no reply by then its ask is chased like any other; Tier 1 inbound PR coordination cadence. Zoya only, composed on the live Cut 1 Zoya
(activity-identity.py output). Usage: python3 d375.py <final dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
tid = "trig_01UPT8LDrBDL5JQqW91Awgbo"
s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
R = [
 ("- A hand-written mail from Akshay or the team on a thread pauses its sequence for 14 days.",
  "- A hand-written mail from Akshay or the team on a thread pauses its sequence for 4 working days (decision 375); with no reply by then, its ask is chased like any other."),
 ("After 30 quiet days the page's schedule takes over.",
  "After 30 quiet days the page's schedule takes over. Tier 1 inbound (pitched to us), until a call or recording is on the calendar: 3 working days after our last ask for the first month, then weekly to the end of month 3, then the routine's Tier 1 schedule; it beats the 5-working-day PR coordination gap, and their own date wins (decision 375)."),
]
for o, n in R:
    assert s.count(o) == 1, o[:50]
    s = s.replace(o, n)
b = s.encode()
open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
print(tid, len(b), hashlib.sha256(b).hexdigest()[:16])
