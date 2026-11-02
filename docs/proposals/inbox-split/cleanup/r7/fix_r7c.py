"""Cleanup on capture r7c (2 Nov): MSGID FIND required People overlap, but 33 of the 36 msgid: Email rows dated since 31 Oct
have no People (measured read-only), so pre-cutoff ad@-only mail would get a duplicate adid: row. Activity Date carries the
message time to the minute, so a Date match within 2 minutes is a tight candidate set; HEADER confirms each as before.
Input: Main r7c capture.txt 39,481 / 4c22ac5037dc8874. Usage: python3 fix_r7c.py <in> <out>."""
import hashlib, sys
s = open(sys.argv[1], encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:16] == "4c22ac5037dc8874"
def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, b)
rep("Date within a day of the message, People overlapping its From, To and Cc, each confirmed",
    "Date within 2 minutes of the message (People or not), or within a day with People overlapping its From, To and Cc, each confirmed")
out = s.encode()
assert len(out) <= 65536 - 200 and s.count(chr(0x2014)) == 0
open(sys.argv[2], "wb").write(out)
print(len(out), hashlib.sha256(out).hexdigest()[:16])
