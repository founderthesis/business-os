"""Due versus done (roadmap item 1, 20 Oct 2026): one daily check folded into the daily sweep. Counts only.

Failure it prevents: a follow-up that was due and never sent goes unnoticed (Mon 19 Oct: 22 rows due, nothing sent, found by hand).
Removes: STEP 6, Mamatha's daily list mail (decision 352: nothing waits on Mamatha), and its count in STEP 5.
Adds: STEP 4b, selected only by structured fields (Waiting on, Next date, Activity Kind, Date, Engagement, Source ID).
Net: the sweep ends smaller.
How we'll know: each weekday sweep report carries the due vs done line; overdue now should read 0 from Wed 21 to Tue 27.

Base: the daily sweep as installed 20 Oct 2026 11:46 UTC (35,943 B / b0888b6624e6848f).
Usage: python3 due-vs-done-build.py <base prompt file> <out file>
"""
import hashlib, re, sys

def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()[:16]

STEP = ('STEP 4b. DUE VERSUS DONE (roadmap item 1). Counts only: change no row, send nothing. Select by fields, never by '
        'summary or Next action wording. Window: since the previous sweep run (Friday\'s on a Monday), JST. (a) Zoya\'s run records '
        '(Activities whose Source ID starts "run:zoya:", Date in the window): sum their due, sent, held and blocked counts; count the '
        'hours with no record and the records not Completed or No-op. (b) Overdue now: open Engagements (any Kind) with Zoya in '
        'Waiting on and Next date before today, with no linked Activity of Kind Email out dated on or after that Next date. (c) Email '
        'out Activities in the window with Source ID empty. (d) Possible duplicates: one Source ID on two Activities, or two Email out '
        'Activities on one Engagement within 10 minutes. Report "Due vs done <D Mon>: due <n>, sent <n>, held <n>, blocked <n>; '
        'hours without a record <n>; overdue now <n>; no message id <n>; possible duplicates <n>", then up to 10 overdue rows '
        '"<Name> (due <D Mon>)".\n\n')

def cut_step6(s):
    i = s.index("STEP 6. MAIL MAMATHA\n")
    j = s.index("STEP 6b. TEMPLATE REVIEW MAIL")
    return s[:i] + s[j:]

EDITS = [
    ("STEP 5. COUNT\n", STEP + "STEP 5. COUNT\n"),
    ("Never send mail other than STEP 6, STEP 6b and STEP 6c (billing forwards to Jaya);",
     "Never send mail other than STEP 6b and STEP 6c (billing forwards to Jaya), within the daily cap of 150 sends across all routines (decision 317, JST);"),
    (", the rows on Mamatha's list (other shows only)", ""),
    ("Plain and short, no em dashes, with a count for every step (0 is a valid count, but say why): ",
     "Plain and short, no em dashes, with a count for every step (0 is a valid count, but say why): the due vs done line (STEP 4b); "),
]

src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
base = len(s.encode())
assert sha(s) == "b0888b6624e6848f", sha(s)
s = cut_step6(s)
for a, b in EDITS:
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, b)
assert "STEP 6." not in s.replace("STEP 6b", "").replace("STEP 6c", ""), "dangling STEP 6 reference"
assert len(s.encode()) < base, (len(s.encode()), base)
open(out, "w", encoding="utf-8").write(s)
print(out, base, "->", len(s.encode()), sha(s))
