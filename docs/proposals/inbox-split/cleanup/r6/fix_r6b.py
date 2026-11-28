"""Cleanup on CTO r5 (2 Nov): the inline recipe decoded each 8000-character chunk alone, so a Message-ID header that
straddles a chunk boundary came out truncated (reproduced: "CAN8JMk1W=sG"), and a hand-copied character can corrupt it.
Append chunks to one file, accept only a complete id, and check every id against ad@ before using it.
Input: Main r6b capture.txt 37,954 / 9b55110e2cead4c2 (same replacement as cleanup/r5/fix2.py). Usage: python3 fix2.py <in> <out>."""
import hashlib, sys
s = open(sys.argv[1], encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:16] == "9b55110e2cead4c2"
def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, b)
rep("Returned inline: copy the data value's first 8000 characters into a file in Bash (a heredoc), then "
    "base64 -d <file> 2>/dev/null | grep -aim1 -A1 '^Message-ID:'; not there, the next 8000 (offsets multiples of 4). ",
    "Returned inline: copy the data value's first 8000 characters into a file in Bash (a heredoc), then "
    "base64 -d <file> 2>/dev/null | grep -aim1 -A1 '^Message-ID:'; no complete id (one ending \">\"), append the next 8000 "
    "to the same file and run it again. Either way, check the id: email_read search with query HEADER Message-ID \"<id>\" "
    "must return this message, else it is not its id. ")
out = s.encode()
assert len(out) <= 65536 - 200 and s.count(chr(0x2014)) == 0
open(sys.argv[2], "wb").write(out)
print(len(out), hashlib.sha256(out).hexdigest()[:16])
