"""Inbox: Message-ID before any Activity, full steps for every capped message, no backlog approvals (CTO, 1 Nov 12:35 JST).
The 12:12 run logged 15 Activities under allmail: keys "to save load", skipped STEPS 3 to 6e, and duplicated at least 4
msgid: rows; earlier runs asked for "Akshay's backfill approval". Input: the live inbox, 65,325 / e6cf4db2bc37918b (the cap
build). Usage: python3 patch.py <live.txt> <out.txt>."""
import hashlib, os, sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:16] == "e6cf4db2bc37918b"
dashes = s.count(chr(0x2014))

def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)

# 1/ No Message-ID, no Activity. The allmail: fallback goes; rows it already made are found and re-keyed.
rep("(the provider's own id only when the header can't be read)", "(no Message-ID, no Activity)")
rep("email_read read has no Message-ID: get it from email_read original (decode in Bash, keep that line), one call at a time, "
    "only when read lists attachments under 50 KB in all; a larger one's header counts as unreadable. Header unreadable: key "
    "\"allmail:<MCP Emails id>\"; a mail From Zoya is Zoya's: for each \"Zoya sent:\" Activity on its Engagement that day (JST), "
    "search text = its Message-ID; one returning this mail is it, create nothing.",
    "email_read read has no Message-ID: get it from email_read original (decode in Bash, keep that line), one call at a time, "
    "never skipped to save load. None after one retry, error or not: create nothing; pend it as \"mcp:<its id>\", not Failed.")
rep("Source ID containing the Gmail id (", "Source ID \"allmail:<its MCP Emails id>\", containing the Gmail id (")
rep("An id that comes back already has its Activity:",
    "A lone allmail: row: set its Source ID to the msgid: key and work it as new. Any other id that comes back already has its Activity:")

rep("any hit means it is logged, so add only a missing link", "any hit but a lone allmail: row means it is logged; add only a missing link")
rep("line (search text = it)", "line (search text = it; mcp: ones by id)")
# M1: batching across messages broke "before the next".
rep("Batch the creates (up to 50 pages per call).", "Batch one message's creates.")
# 2/ and 3/ The cap limits messages, never steps, and is the approval.
rep("A backlog never means working none.",
    "Each gets STEPS 2 to 6e before the next; the cap is the approval: a backlog never means working none, "
    "skipping a step or asking Akshay.")

out = s.encode()
assert s.count(chr(0x2014)) == dashes and len(out) <= 65536 - 200, len(out)
open(dst, "wb").write(out)
print(os.path.basename(dst), len(out), hashlib.sha256(out).hexdigest()[:16], "headroom", 65536 - 200 - len(out))
