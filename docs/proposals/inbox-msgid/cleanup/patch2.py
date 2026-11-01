"""Cleanup rev of the inbox Message-ID patch (1 Nov). Input: Main's build, 65,334 / 2f3250ed1d45e7db.
1/ a pending mcp: id (retried by id) never holds "read to", so one unreadable mail can't freeze the cursor;
2/ the 50 KB guard comes back as a bound, not a skip: at most 2 heavy originals a run, the rest wait;
3/ a lone allmail: row is worked on that row, never a second Activity.
Room: a redundant parenthesis and the RAW alias (defined in the Gmail tool map). Usage: python3 patch2.py <in> <out>."""
import hashlib, os, sys
s = open(sys.argv[1], encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:16] == "2f3250ed1d45e7db"
dashes = s.count(chr(0x2014))
def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)
rep("never past a pending one;", "never past a pending one but an mcp: one;")
rep("get it from email_read original (decode in Bash, keep that line), one call at a time, never skipped to save load.",
    "get it from RAW, one call at a time, never skipped to save load; at most 2 with attachments over 50 KB a run, the rest wait.")
rep("set its Source ID to the msgid: key and work it as new.", "set its Source ID to the msgid: key and work it as new on that row.")
rep(" (never collapsed by sender, subject or time)", "")
out = s.encode()
assert s.count(chr(0x2014)) == dashes and len(out) <= 65536 - 200, len(out)
open(sys.argv[2], "wb").write(out)
print(os.path.basename(sys.argv[2]), len(out), hashlib.sha256(out).hexdigest()[:16], "headroom", 65536 - 200 - len(out))
