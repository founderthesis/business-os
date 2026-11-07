"""Inbox hotfix on the live d420 prompt (CTO, 30 Oct 00:05 JST): Notion writes that land nowhere, and a lighter Message-ID read.
Input: the live inbox, 65,333 / d1bba5802ca8872d (Akshay pasted it 29 Oct). Usage: python3 patch.py <live.txt> <out.txt>."""
import hashlib, os, sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:16] == "d1bba5802ca8872d"
dashes = s.count(chr(0x2014))

def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)

# 1. Writes. The 23:19 run's run record and 17 Activities were created with no parent: the Notion tool then makes a loose,
#    untitled workspace page and drops the properties, and the run still counted them as logged.
rep("NOTION\n- Activities: collection://290f715d-fd45-4203-ade6-3642c2326c6c",
    "NOTION\nWRITES: every create names parent {\"type\": \"data_source_id\", \"data_source_id\": \"<its collection id "
    "below>\"}, allow_async false, the title set. Then fetch the page it returns: no parent data source: a "
    "failed write, never logged; retry once, else report it, end Partial.\n- Activities: collection://290f715d-fd45-4203-ade6-3642c2326c6c")
rep("(action read, then original for its Message-ID)", "(action read; original only per IDENTITY)")

# 2. Message-ID. `original` returns the whole .eml as base64: 1 to 2 MB messages filled the run and hit the 2-download limit.
rep("email_read read has no headers: for each new message, read it with email_read original, decode it in Bash and keep only "
    "its Message-ID line.",
    "email_read read has no Message-ID: get it from email_read original (decode in Bash, keep that line), one call at a "
    "time, only when read lists attachments under 50 KB in all; a larger one's header counts as unreadable.")
rep("When the header still can't be read, before creating an Activity keyed by a provider id: a mail From Zoya's address is "
    "logged by Zoya, so for each \"Zoya sent:\" Activity on the same Engagement captured that day (JST) whose Source ID holds a "
    "Message-ID, search Gmail rfc822msgid:<that Message-ID>; one that returns this mail's Gmail id is this mail, create nothing.",
    "Header unreadable: key \"allmail:<MCP Emails id>\"; a mail From Zoya is Zoya's: for each \"Zoya sent:\" Activity on its "
    "Engagement that day (JST), search text = its Message-ID; one returning this mail is it, create nothing.")

# 3. Room: decision 424's fold is on hold until CX-20261029-03 is built (Codex, 29 Oct); until then duplicates are reported.
rep("Fold only a proven duplicate: its note lines, open asks, Activities, Call, Eval (the kept row's wins) and Dossier links, "
    "and its people as Stakeholders, move to the kept row; read it back, clear the duplicate's relations, Trash it (decision "
    "416), report it; never merge People (decision 424).",
    "A duplicate row: report both, never retire one (CX-20261029-03); never merge People (decision 424).")

out = s.encode()
assert s.count(chr(0x2014)) == dashes and len(out) <= 65536 - 200, len(out)
open(dst, "wb").write(out)
print(os.path.basename(dst), len(out), hashlib.sha256(out).hexdigest()[:16], "headroom", 65536 - 200 - len(out))
