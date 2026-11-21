"""r23 for inbox capture (CTO, 7 Nov 18:40 JST, Codex audit item 1). Built on r22/capture.txt (a4ac5ae2), so it
deploys after r22. Usage: python3 patch.py cap <r22/capture.txt> <out>
RAWID: the Message-ID comes from one Bash step that reads the email_read original result itself (the saved file, or
this run's own transcript when the result came back inline), decodes the whole base64, checks its sha256 and parses
the headers. Nothing is copied by hand. Pending messages (RAWID NONE, the attachment cap, quota or errors) stay on the
pending line across cursor moves and are worked again first. Each edit is asserted; no new em dash; size cap."""
import sys, hashlib
which, src, out = sys.argv[1], sys.argv[2], sys.argv[3]
assert which == "cap"
b = open(src, "rb").read()
assert hashlib.sha256(b).hexdigest().startswith("a4ac5ae2"), "not r22 capture"
s = b.decode("utf-8")
SCRIPT = 'import sys,json,glob,os,base64,hashlib,email.parser\nmid=sys.argv[1];fs=sys.argv[2:] or sorted(glob.glob(os.path.expanduser("~/.claude/projects/*/*.jsonl")),key=os.path.getmtime)[-1:]\nd=[]\ndef w(o):\n if isinstance(o,dict):\n  if o.get("message_id")==mid and o.get("data"):d.append(o)\n  for v in o.values():w(v)\n elif isinstance(o,list):\n  for v in o:w(v)\n elif isinstance(o,str) and mid in o and \'"data"\' in o:\n  try:w(json.loads(o))\n  except Exception:pass\nfor f in fs:\n t=open(f,errors="replace").read()\n try:w(json.loads(t))\n except Exception:\n  for l in t.splitlines():\n   if mid in l:\n    try:w(json.loads(l))\n    except Exception:pass\nif not d:print("NONE no result");sys.exit()\no=d[-1];b=base64.b64decode(o["data"])\nif o.get("sha256") and hashlib.sha256(b).hexdigest()!=o["sha256"]:print("NONE sha256 mismatch");sys.exit()\nm=email.parser.BytesHeaderParser().parsebytes(b).get("Message-ID")\nm="".join(str(m or "").split()).strip("<>")\nprint(m if m and "@" in m else "NONE no header")'
EDITS = [
 (("The result saved to a file: python3 -c", "still none: pend it."),
  "RAWID (CTO, 7 Nov: the 07:02 run pended three messages, Jaya's October invoice among them, for want of an id; never copy any of the data by hand): saved to a file or returned inline, run this Bash step with the message_id exactly as you passed it, plus the saved file's path if the result was saved (with none it reads this run's own transcript, where an inline result already is): python3 - \"<message_id>\" [<file>] <<'X'\n" + SCRIPT + "\nX\nIt decodes the whole message, checks its sha256, parses the headers and prints the Message-ID, or \"NONE <why>\". NONE: email_read original once more, then RAWID again; still NONE: pend it."),
 ("then RAW by HEAD (the Bash recipe in MAILBOX)", "then RAW by RAWID (MAILBOX)"),
 ("5/ only then RAW, by HEAD.", "5/ only then RAW, by RAWID."),
 ("then RAW by HEAD, this run, no wait.", "then RAW by RAWID, this run, no wait."),
 ("at most 2 with attachments over 50 KB a run, the rest wait.", "at most 2 with attachments over 50 KB a run, the rest wait on the pending line."),
 ("logged now, or noise, leaves it; else it stays pending.",
  "logged now, or noise, leaves it; else an mcp: or adid: one is worked again this run, before new mail and inside the cap (read by its id, RAWID, then STEPS 2 to 7), and it stays pending until it is logged or noise."),
 ("carried from the record T comes from, never dropped;",
  "carried from the record T comes from, never dropped; built by a Bash python step from that line, this run's ledger and the messages at or before \"read to\": every message this run left unlogged for any reason (RAWID NONE, the attachment cap, a quota, rate-limit or 5xx error, any other error) is on it, and one leaves it only when logged or noise;"),
]
for a, c in EDITS:
    if isinstance(a, tuple):
        st, en = a
        assert s.count(st) == 1 and s.count(en) == 1, (st[:40], en[:40])
        i, j = s.index(st), s.index(en); assert j > i
        s = s[:i] + c + s[j + len(en):]
    else:
        assert s.count(a) == 1, (a[:60], s.count(a))
        s = s.replace(a, c)
assert "by HEAD" not in s and "(HEAD)" not in s
assert s.count(chr(0x2014)) == b.decode("utf-8").count(chr(0x2014)), "new em dash"
ob = s.encode("utf-8"); assert len(ob) <= 65536 - 200, len(ob)
open(out, "wb").write(ob); print(which, len(ob), hashlib.sha256(ob).hexdigest()[:16])
