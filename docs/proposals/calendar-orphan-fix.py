"""Calendar: orphan prep entries are never deleted; a blocked action never ends the run (CTO, 20 Oct, run cse_011mP2zw7ZY1xJQEKqKaL7iW).
Usage: python3 calendar-orphan-fix.py <base prompt> <out prompt>"""
import sys, hashlib
src, dst = sys.argv[1], sys.argv[2]
s = open(src).read()
R = [
 # hard rules: who may be deleted, plus the two new rules
 ("and deleting a duplicate booking the booker asked us to cancel, in STEP 1b rule 1 (decision 322).",
  "and deleting a duplicate booking the booker asked us to cancel, in STEP 1b rule 1 (decision 322).\n"
  "- ORPHAN ENTRIES: a prep, cooling-off or Podcast prep entry whose call is gone (cancelled, or no invite carries its call) is never deleted. Start passed: leave it. Future, created by ad@thepodium.in and no attendees: update_event, Summary \"Cancelled: <old summary>\", notificationLevel NONE, nothing else changed. Anything else, or if that is blocked: report \"orphan prep entry: <summary> <D Mon>\".\n"
  "- A BLOCKED OR REFUSED TOOL CALL NEVER ENDS THE RUN: skip that one item, finish every other step (the audit marker included: a blocked item is handled once it is in the report) and report it in one line. No push notification for a blocked item; push only if the whole run fails."),
 ("or sits on a call that is gone. Rename it to \"Prep: <guest> @ <company> (...)\" with \"Booked by: <name>\" in the description, or delete it. Never touch the invite.",
  "Rename it to \"Prep: <guest> @ <company> (...)\" with \"Booked by: <name>\" in the description. On a call that is gone: ORPHAN ENTRIES. Never touch the invite."),
 ("The call was cancelled: delete it.", "The call was cancelled: ORPHAN ENTRIES."),
 ("move it when the recording moves, delete it when the recording is cancelled.",
  "move it when the recording moves; a cancelled recording: ORPHAN ENTRIES."),
 ("Move it when the recording moves, delete it when the recording is cancelled, and update",
  "Move it when the recording moves (a cancelled recording: ORPHAN ENTRIES), and update"),
 ("prep entries created, moved, deleted;", "prep entries created, moved, marked cancelled; blocked actions;"),
]
for o, n in R:
    assert s.count(o) == 1, o[:60]
    s = s.replace(o, n)
assert "—" not in s
open(dst, "w").write(s)
print(len(s.encode()), hashlib.sha256(s.encode()).hexdigest()[:16])
