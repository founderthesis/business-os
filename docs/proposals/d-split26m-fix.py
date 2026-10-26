"""Cleanup's fix to d-split26m (edc49c1), finding 7. Usage: python3 docs/proposals/d-split26m-fix.py (repo root), then routines/zoya/build.py.
d-split26m gives FAST 36,811 / 1b4cca2a0d0b284e, SLOW 63,845 / 94943a20df0745dd.
"a segment's date: the date its text gives, else its key's, else the day it was written" gives every undated segment of another
owner (an old "Waiting on Payal: reply to the commercials", an Akshay ask) the day it was written. A row whose Zoya step is dated
2 Nov but which also carries a 14 Oct waiting segment gets Next date 14 Oct for good: SLOW's SELECT re-picks it every run with
nothing due (no write, so the date never moves), and the sweep's STEP 4b counts it as unexplained overdue every day.
Now an undated segment doesn't count; only a row with no dated segment at all takes the day of the write, which still settles
R1, R2 and E (their new segments are undated)."""
p = "routines/zoya/parts/actions.txt"
s = open(p, encoding="utf-8").read()
a = "(a segment's date: the date its text gives, else its key's, else the day it was written; "
b = "(a segment's date: the date its text gives, else its key's; undated segments don't count, and with none dated it is the day of the write; "
assert s.count(a) == 1
open(p, "w", encoding="utf-8").write(s.replace(a, b))
print("d-split26m fix applied")
