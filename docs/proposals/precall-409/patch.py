"""Decision 409 (24 Oct): precall promises go on the guest's own Engagement as Next action segments, never
Kind Task rows; the "precall:" exemption in 385 is removed. Cleanup proposal, 5 Nov.
Usage: python3 patch.py <cal|sweep|wa> <live prompt> <out>. Asserts the live hash and each edit exactly once."""
import sys, hashlib
which, src, out = sys.argv[1], sys.argv[2], sys.argv[3]
b = open(src, "rb").read()
LIVE = {"cal": "e4b39d67", "sweep": "76b49956", "wa": "8628f42a"}
assert hashlib.sha256(b).hexdigest().startswith(LIVE[which]), "not the live %s prompt" % which
s = b.decode("utf-8")
EXEMPT = ("rows a step below keys by its own Source ID (transcript:, precall:) stay Kind Task rows.",
          "rows a step below keys by its own Source ID (transcript:) stay Kind Task rows; precall promises go on the guest's own row (decision 409).")
EDITS = {
 "sweep": [EXEMPT],
 "cal": [EXEMPT,
  ("the add itself is its own Task row (New actions, below; decision 360).",
   "the add itself is a promise segment on this row (New actions, below; decision 409)."),
  ("Each one is its own Task row in Engagements, never a segment of this row's Next action: Name \"Task: <the promise> (<guest>, <D Mon> precall)\", Kind Task, For engagement = this row, Show = this row's Show, Waiting on its owner (Akshay for what he said he would do, Guest or PR for what their side owes), Task state Handed over (Awaiting someone else for their side), Next action \"<owner>: <the promise>\", Next date the date named, else 7 days after the precall, Source Agent, Source ID \"precall:<event id>:<n>\" (reuse a row that has that key; never a second), Captured today.",
   "Each one is a segment of this row's Next action, never a Task row (decision 409, Akshay, 24 Oct: \"They should be clubbed\"): \"<owner>: <the promise> (precall <D Mon>, by <the date named, else 7 days after the precall>)\" after \" | \" (other segments kept), its owner added to Waiting on (Akshay for what he said he would do, Guest or PR for what their side owes, Zoya for a routine mail); a community add is the one \"Akshay: invite <first name> to the FT Community\" segment, added once. Never change Next date. A segment already on the row with the same owner and promise is not added twice."),
  ("Claude note line \"YYYY-MM-DD: precall <date> actions checked, <n> Task rows\".",
   "Claude note line \"YYYY-MM-DD: precall <date> actions checked (<event id>), <n> promises: <owner>: <promise>; ...\"."),
 ],
 "wa": [EXEMPT,
  ("for each precall whose Task rows (Source ID \"precall:<event id>:<n>\") are new since your last post,",
   "for each Engagement whose Claude note gained a line \"precall <date> actions checked (<event id>), <n> promises: ...\" with n of 1 or more since your last post (decision 409: the promises are segments on the guest's row, not Task rows),"),
 ],
}
for a, c in EDITS[which]:
    assert s.count(a) == 1, (which, a[:70], s.count(a))
    s = s.replace(a, c)
assert s.count(chr(0x2014)) == b.decode("utf-8").count(chr(0x2014)), "new em dash"
assert "precall:<event id>" not in s, "precall Task key left"
ob = s.encode("utf-8"); assert len(ob) <= 65536 - 200
open(out, "wb").write(ob); print(which, len(ob), hashlib.sha256(ob).hexdigest()[:16])
