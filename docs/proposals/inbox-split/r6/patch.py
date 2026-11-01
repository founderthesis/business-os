"""Capture r6 on the live r5 (CTO, 2 Nov 01:40 JST: split live). Usage: python3 patch.py <r5 capture.txt> <out>
Input: docs/proposals/inbox-split/cto-r5/capture.txt, 36,666 / 405a30d3 (live). Every edit is asserted once; all else byte-identical."""
import hashlib, sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:8] == "405a30d3"
dashes = s.count(chr(0x2014))

def R(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)

# 1. STEP 0 duplicate (108855, 108860): full STEP 2 lookup before any re-key; any hit folds.
R("allmail: read the message by that MCP Emails id and get its Message-ID (IDENTITY). A msgid: row for it exists: copy",
  "allmail: read the message by that MCP Emails id and get its Message-ID (IDENTITY), then run STEP 2's full lookup for it "
  "(the IN on its ids and the LIKE on the Message-ID's part before @, Zoya's rows included). Any hit other than this row: "
  "fold into that row, never re-key: copy")
R("None exists: set its Source ID to the msgid: key", "No hit: set its Source ID to the msgid: key")
# 2a. Work to the cap or STOP TIME.
R("STOP TIME: start no new message after :20 past the hour; the rest wait for the next run (not pending).",
  "STOP TIME: start no new message after :20 past the hour; the rest wait for the next run (not pending). Work until the "
  "cap or STOP TIME, whichever comes first: ending earlier while due messages remain is Partial, \"stopped early\", listed "
  "in the report as a defect.")
# 2b + 2e. Batched reads; backlog mode.
R("at most 15 not yet logged a run (then Partial)",
  "at most 15 not yet logged a run (BACKLOG: more than 15 due at the start: 25, and STEP 0's rows count toward it) "
  "(then Partial)")
R("read each once (action read; original only per IDENTITY)",
  "read bodies once, action read_batch, up to 20 ids a call, body_max_chars 2000 (action read only where a step needs "
  "the full body; original only per IDENTITY)")
R("STEP 0's rows don't count toward STEP 1's cap of 15.",
  "STEP 0's rows don't count toward STEP 1's cap of 15, except in BACKLOG.")
# 2d. Message-ID from a later message's References or In-Reply-To.
R("get it from RAW (the Bash recipe in MAILBOX), one call at a time, never skipped to save load;",
  "get it from RAW (the Bash recipe in MAILBOX), one call at a time, never skipped to save load, except: when a later "
  "message's References or In-Reply-To names a Message-ID, confirm it with query HEADER Message-ID \"<id>\" (the message "
  "it returns has that Message-ID) and skip that message's RAW;")
# 2c. Stakeholders: full get_thread sweep only when it can add someone.
R("on every thread you touch, read the whole chain with get_thread and collect every From, To and Cc address across all "
  "its messages.",
  "on a new pitch, a new thread, or a message with an address not yet in People, read the whole chain with get_thread and "
  "collect every From, To and Cc address across all its messages; otherwise only this message's From, To and Cc.")

out = s.encode()
assert s.count(chr(0x2014)) == dashes and len(out) <= 40000
open(dst, "wb").write(out)
print("capture r6", len(out), hashlib.sha256(out).hexdigest()[:16])
