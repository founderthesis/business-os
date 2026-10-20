"""Due versus done (roadmap item 1, 20 Oct 2026): one daily check folded into the daily sweep. Counts only.

Base: the daily sweep as installed 20 Oct 2026 11:46 UTC (35,943 B / b0888b6624e6848f).
Usage: python3 due-vs-done-build.py <base prompt file> <out file>
"""
import hashlib, sys

def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()[:16]

STEP = ('STEP 4b. DUE VERSUS DONE (roadmap item 1). Counts only: change no row, send nothing. The window is since the previous '
        'sweep run (Friday\'s on a Monday), JST. (a) Zoya\'s run records: Activities whose Source ID starts "run:zoya:" in the '
        'window; sum the first-line counts due, sent, held, blocked; count the hours in the window with no record (Zoya runs at :30 each '
        'hour) and the records not Completed or No-op. (b) Overdue now: open Engagements of any Kind with Zoya in Waiting on and Next date before today, '
        'with no linked "Zoya sent" Activity dated on or after that Next date and no Claude note "held:" line from the window; a '
        'weekend or Diwali Next date counts from the next allowed weekday. (c) "Zoya sent" Email out Activities in the window with '
        'Source ID empty. (d) Possible duplicates: one Source ID on two Activities, or two "Zoya sent" mails to the same recipient '
        'on the same Engagement and day. Report one line "Due vs done <D Mon>: due <n>, sent <n>, held <n>, blocked <n>; hours '
        'without a record <n>; overdue now <n>; sent without id <n>; possible duplicates <n>", then up to 10 overdue rows '
        '"<Name>: <its Zoya segment> (due <D Mon>)".\n\n')

EDITS = [
    ("STEP 5. COUNT\n", STEP + "STEP 5. COUNT\n"),
    ("Plain and short, no em dashes, with a count for every step (0 is a valid count, but say why): ",
     "Plain and short, no em dashes, with a count for every step (0 is a valid count, but say why): the due vs done line and its overdue rows (STEP 4b); "),
]

src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert sha(s) == "b0888b6624e6848f", sha(s)
for a, b in EDITS:
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, b)
open(out, "w", encoding="utf-8").write(s)
print(out, len(s.encode()), sha(s))
