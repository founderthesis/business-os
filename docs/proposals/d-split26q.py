"""Round 4b findings (both runs; I1 and I4 pass, I3 fails, nothing resent), after d-split26p. Usage: python3
docs/proposals/d-split26q.py (repo root), then routines/zoya/build.py.
1/ I3: a send that answered its thread and crashed before logging was never seen again (STEP 1 takes only unanswered threads).
   Each run now reads its Sent for the last 24 hours and puts any message no Activity holds through the recovery check.
2/ I3: a run's own crashed record stayed Started for good (each run reads only the other kind's record). A run now closes its
   own kind's earlier record the same way when it is 60 minutes old or more.
3/ I4: the content test ("does what the action asks") could be read before the candidate count, find no match and resend.
   Candidates are counted first; content only excludes a mail that plainly does something else. The check runs before any
   hold rule.
4/ I1: a follow-up counted mail to that person on any thread, so a PR handling two guests made a false hold. Candidates are on
   the action's thread (a first mail with no thread: any thread).
5/ I4: one hold per candidate set, shared by the actions it holds, and a held action is skipped while that ask is open, so
   Akshay gets one ask, not two near-identical ones, and later runs don't re-add it.
6/ Both runs: "Action key only after a send receipt" against "a send found by the thread check gets its Action key too"."""
def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:60], s.count(a))
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8").write(s)
P = "routines/zoya/parts/"
old = open(P + "actions.txt", encoding="utf-8").read()
i = old.index("- Before sending:"); j = old.index("One message can complete several actions", i)
edit(P + "actions.txt", [
 (old[i:j],
  "- Before sending (before any hold rule): look for the action key on an Activity (property \"Action key\"), then list the "
  "candidates: messages from us in your Sent to that recipient on the action's thread (a first mail with no thread: any thread) "
  "since the action was raised, whose Message-ID no Activity holds (two Sent copies with one Message-ID are one), less any that "
  "plainly does something else (a holding reply, a loop-in, another row's ask). The Message-ID on the action's Activity, or one "
  "candidate: that is the match: send nothing, log the Activity if it is missing, complete the action. None: it is due. Two or "
  "more: HOLD, never send: Akshay in Waiting on and one segment per candidate set, shared by the actions it holds, \"Akshay: "
  "can't tell which mail completed <actions, short>: <each candidate's Message-ID and send time>. Write which in Your call\", "
  "Claude note \"YYYY-MM-DD: held for review (<keys>)\", named in the report; a held action is skipped while that segment is "
  "open. Each run also reads its Sent for the last 24 hours: a message from us no Activity holds goes through this check for "
  "its thread's row (the inbound it answers is logged too); nothing it completes: log it on that row and report it. "),
 ("Write \"Action key\" on the Activity only after a send receipt;",
  "Write \"Action key\" on the Activity only after a send receipt or a match above;"),
])
edit(P + "lease.txt", [(
 "and it holds nothing;",
 "and it holds nothing; close your own kind's earlier record the same way;")])
print("d-split26q applied")
