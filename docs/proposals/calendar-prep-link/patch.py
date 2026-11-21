"""Calendar prep-link build (Main 2, 11 Nov; Build card 40219a301a7f812a8d35eedc5cf0e4b6; Cleanup verdict
docs/proposals/r25/cleanup-verdict-9b38353.md, section 2). Built on the live r24 prompt (deploy 311e607).
Usage: python3 patch.py docs/proposals/r24/calendar.txt <out>
- (a) The prep entry's Engagement line is https://app.notion.com/p/<id> (the /p/ form; without it the link doesn't open).
- (b) The "One exists" check also compares the Engagement line, so entries with the old form heal on the next run.
- (c) STEP 4 transcript asks also skip when a pre-493 open "Transcript:" Task row already points at this guest row.
Each edit is asserted once; no new em dash; size cap."""
import sys, hashlib
src, out = sys.argv[1], sys.argv[2]
b = open(src, "rb").read()
assert hashlib.sha256(b).hexdigest().startswith("c613af00"), "not the live calendar (r24)"
s = b.decode("utf-8")
dashes = s.count("—")
EDITS = [
 ('"Engagement: <Notion URL>"',
  '"Engagement: https://app.notion.com/p/<engagement page id, 32 hex, no dashes>" (always with /p/: without it the link does not open)'),
 ("build the Eval, Dossier, Prep note and LinkedIn lines it should carry",
  "build the Engagement, Eval, Dossier, Prep note and LinkedIn lines it should carry"),
 ('or if any Engagement has Source ID "transcript:episode:<that recording\'s Episode page id>". Else (decision 493',
  'or if any Engagement has Source ID "transcript:episode:<that recording\'s Episode page id>", or if an open Kind Task row (Task state not Done) whose Name starts "Transcript:" has For engagement = this guest row (a leftover from before decision 493). Else (decision 493'),
]
for old, new in EDITS:
    assert s.count(old) == 1, old[:60]
    s = s.replace(old, new)
assert s.count("—") == dashes, "new em dash"
o = s.encode("utf-8")
assert len(o) < 65536, len(o)
open(out, "wb").write(o)
print(len(o), hashlib.sha256(o).hexdigest())
