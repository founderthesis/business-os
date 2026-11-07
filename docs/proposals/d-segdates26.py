"""Dated segments (Codex CX-20261026-01; Akshat dry run 26 Oct: FAIL). Akshat's row holds two asks: the guest chase due
2 Nov and Akshay's travel ask due 29 Oct. Selection is by the row's one Next date (2 Nov), so the 29 Oct ask only
reaches Akshay by the owner mail's age rule, not by its date. Fix, in the split parts (the single Zoya prompt has 117 B
left): a segment may carry its own date "on <D Mon>"; Next date is the earliest open segment date; a run works only the
segments due, so selecting the row for one date never sends another's step early; finishing one never moves another's
date; a dated Akshay segment counts as due on its date for OWNER MAIL. Row repair for Akshat goes with the deploy:
segment B written "Akshay: <ask> on 29 Oct", Next date 29 Oct, segment A "Zoya: sponsored step 1 on 2 Nov".
Usage: python3 d-segdates26.py (repo root)"""
import os
D = "routines/zoya/parts"
EDITS = [
 ("followups.txt", "The report's due count is this selection.",
  "The report's due count is this selection. DATED SEGMENTS (Codex, 26 Oct): a Next action segment may carry its own "
  "date, \"<owner>: <step> on <D Mon>\". Next date is always the earliest date still open on the row. A run works only "
  "the segments due today or earlier: a row picked for one segment's date leaves later-dated segments alone, and "
  "finishing one never moves another's date or text."),
 ("followups.txt", "Next date = the next step's due date",
  "Next date = the earliest of the next step's due date and any other open segment's date"),
 ("ownermail.txt", "An item due within 2 days goes at once in its own mail.",
  "An item due within 2 days (a dated \"Akshay: ... on <D Mon>\" segment counts by its date) goes at once in its own "
  "mail."),
]
for f, a, b in EDITS:
    p = os.path.join(D, f)
    s = open(p, encoding="utf-8").read()
    assert s.count(a) == 1, (f, a[:40], s.count(a))
    open(p, "w", encoding="utf-8").write(s.replace(a, b))
    print("edited", f)
