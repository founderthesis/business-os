"""Fixes from frozen round 3 (split-dryruns/frozen-round3.md) on the frozen build 8e64140 (FAST 96c11beae7ec325b,
SLOW a5b4ef40cfd85bb1). Usage: after Cleanup's d-split26l-fix.py (1303cea), python3 docs/proposals/d-split26m.py (repo root), then routines/zoya/build.py.
1/ E (both runs FAIL) and R2: one inbound, several asks, one of them for Akshay. The answer mail to the routine ask now carries
   the holding line for the other ("one receipt at most" meant no second mail, not no acknowledgement), and the Akshay ask keeps
   its own reply segment beside his "Ask Akshay" segment.
2/ G (run A finding): "a row that waits on Akshay" read literally sent a sponsored yes to Akshay because he had an unrelated
   travel step on the row. Now it is the ask that waits on him, not the row.
3/ R3 (both): the 413 read-back named only the inbound's To and Cc, which leaves out its sender and includes our own address.
4/ L1 (both): residual same-minute race. A run that read before the other's Started record existed would proceed, and so would
   the other by the tie-break. A second read 1 minute later, before the first row write, closes it.
5/ R1 (both): c(2) had no branch for a recording with no Episode yet, and c(4) said "the row" where it means the guest row.
6/ R2 (both): a PR question about a recording whose status is open added a second Akshay ask for the same fact."""
def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:60], s.count(a))
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8").write(s)
P = "routines/zoya/parts/"
edit(P + "actions.txt", [(
 "write each open reply action as its own segment \"Zoya [reply msg-<id>-n <ts>]: <ask>\".",
 "write each open reply action as its own segment \"Zoya [reply msg-<id>-n <ts>]: <ask>\"; an ask that goes to Akshay keeps "
 "that segment beside his \"Ask Akshay\" one, neither replacing the other.")])
edit(P + "mail.txt", [
 ("c. Not routine, or a message on a row that waits on Akshay's decision or wording",
  "c. Not routine, or an ask that waits on Akshay's decision or wording (an unrelated step of his on the row doesn't count)"),
 ("unless one went on it in the last 7 days or the real answer goes on it this run (one receipt at most):",
  "unless one went on it in the last 7 days (one receipt at most); when your answer to another ask goes on that thread this run, "
  "the holding line goes inside that mail instead of a second one:"),
])
edit(P + "sending.txt", [(
 "that To and Cc together hold everyone on the latest inbound, To and Cc, less bounced addresses,",
 "that To and Cc together hold everyone on the latest inbound, its From, To and Cc, less your own address, bounced addresses,")])
edit(P + "lease.txt", [(
 "if both are Started, the earlier start holds it, and in the same minute FAST does.",
 "if both are Started, the earlier start holds it, and in the same minute FAST does. Read again 1 minute after your first read "
 "(Bash sleep 60), still before any row write: a record the other run wrote meanwhile counts the same way.")])
edit(P + "internal.txt", [
 ("(2) Attach the .txt to the Episode's Transcript file",
  "(2) No Episode for that recording yet: leave the row at Doing, Claude note \"YYYY-MM-DD: transcript held: no Episode yet\" "
  "(once), and retry next run; the calendar's STEP 4e creates it. Else attach the .txt to the Episode's Transcript file"),
 ("Then make sure Waiting on has Akshay and Next action has",
  "Then make sure the guest row's Waiting on has Akshay and its Next action has"),
])
edit(P + "notion-data.txt", [(
 "Still unclear: once, Akshay in Waiting on and the segment \"Akshay: did the <D Mon> recording with <guest> happen? Write yes or "
 "no in Your call\".",
 "Still unclear: once, Akshay in Waiting on and the segment \"Akshay: did the <D Mon> recording with <guest> happen? Write yes or "
 "no in Your call\". A question from their side about it while that is open adds no second Akshay ask: it waits on his answer.")])
print("d-split26m applied")
# 7/ R1, R2, E (both runs): Next date was undefined when no open segment names a date, and runs split on whether a key's
#    raised time counts. A segment's date is now: the date its text gives, else its key's, else the day it was written.
# 8/ D (both runs): after a late step 1, AFTER SEND dated step 2 in the past (offer + 14 = today), so the next run re-selected
#    all 40 rows only to hold them under the 7-day limit. The next step's date now starts no earlier than LIMITS allows.
edit(P + "actions.txt", [(
 "A write that changes Next action sets Next date to the earliest open segment date (",
 "A write that changes Next action sets Next date to the earliest open segment date (a segment's date: the date its text "
 "gives, else its key's, else the day it was written; ")])
edit(P + "followups.txt", [(
 "Next date = the earliest of the next step's due date and any other open segment's date (weekdays only; PR COORDINATION's gap where it applies)",
 "Next date = the earliest of the next step's due date and any other open segment's date (weekdays only; PR COORDINATION's gap "
 "where it applies; the next step never before the first day LIMITS' 7-day rule allows)")])
print("d-split26m 7/ 8/ applied")
