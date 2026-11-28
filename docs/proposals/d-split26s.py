"""Round 4 R1 and R2, held back for bytes; the one-writer build (build_one.py) has room. Usage: python3
docs/proposals/d-split26s.py (repo root, after d-split26r), then routines/zoya/build_one.py.
1/ R1 (run B): with no Episode yet, c(2) said "retry next run" and (5) closes the row, so a run could read the thank-you as
   waiting on the Episode, against decision 412. (3) and (4) now run at once; only the attach waits; (5) closes the row only
   after (2) is done.
2/ R2 (both runs): a PR's release-date question about a recording whose status is open went to Akshay through 1c as a second
   ask, beside the 411 question. It now waits on his answer with a holding reply.
3/ R2 (both runs): Next date was read from the recording date in the 411 question's text ("did the 23 Oct recording"). Only a
   due date counts as a segment's date."""
def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:60], s.count(a))
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8").write(s)
P = "routines/zoya/parts/"
edit(P + "internal.txt", [
 ("(once), and retry next run; the calendar's STEP 4e creates it.",
  "(once), and retry the attach next run (the calendar's STEP 4e creates it); (3) and (4) still run now."),
 ("(5) Close the row:", "(5) Once (2) is done, close the row:"),
])
edit(P + "notion-data.txt", [(
 "A question from their side about it while that is open adds no second Akshay ask: it waits on his answer.",
 "While that is open, a question from their side about that recording or its episode (how it went, when it's out) adds no "
 "second Akshay ask: a holding reply, and it waits on his answer.")])
edit(P + "actions.txt", [(
 "(a segment's date: the date its text gives, else its key's;",
 "(a segment's date: the due date its text gives (\"on\", \"by\" or \"original due\", never a date the ask is about), else its key's;")])
print("d-split26s applied")
