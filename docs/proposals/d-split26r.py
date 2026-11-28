"""Round 4c run B findings on the hold rule (d-split26q), crash path only. Usage: python3 docs/proposals/d-split26r.py
(repo root), then routines/zoya/build.py.
1/ A later Sent scan could log a mail named in an open "can't tell which mail" segment as "nothing it completes"; it then stops
   being a candidate, the held step reads as due and could go twice. Such a mail is now left alone until Akshay answers.
2/ A send the Sent scan logged without an Action key became invisible to the candidate rule (only mails "no Activity holds"
   count), so the step's own check read "none: it is due" and only AFTER SEND stopped a resend. An Activity holding a
   candidate's Message-ID without a key now counts as that candidate.
Bytes: SLOW had 39 B of headroom; the scan sentence is reworded to fit."""
def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:60], s.count(a))
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8").write(s)
edit("routines/zoya/parts/actions.txt", [
 ("since the action was raised, whose Message-ID no Activity holds (two Sent copies with one Message-ID are one)",
  "since the action was raised, whose Message-ID no Activity holds or only one with no Action key (two Sent copies with one "
  "Message-ID are one)"),
 ("Each run also reads its Sent for the last 24 hours: a message from us no Activity holds goes through this check for "
  "its thread's row (the inbound it answers is logged too); nothing it completes: log it on that row and report it. ",
  "Each run also checks its Sent for the last 24 hours: a message from us no Activity holds goes through this check for its "
  "thread's row (log the inbound it answers too); none it completes: log it there and report it; one named in an open \"can't "
  "tell\" segment: leave it. "),
])
print("d-split26r applied")
# Bytes, wording only: the "two Sent copies are one" clause repeats MESSAGE IDENTITY and ACTIONS' own line, and the property
# name "Action key" is given where Activities are written.
edit("routines/zoya/parts/actions.txt", [
 (" or only one with no Action key (two Sent copies with one Message-ID are one)", " or only one with no Action key"),
 ("- Before sending (before any hold rule): look for the action key on an Activity (property \"Action key\"), then list",
  "- Before sending (before any hold rule): look for the action key on an Activity, then list"),
])
print("d-split26r cuts applied")
