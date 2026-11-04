"""Daily sweep, decisions 463.1 and 463.6 (Akshay, 4 Nov, Tab 15), on the live sweep (39,131 / 6783dd01, read back
4 Nov from trig_01MdfUFg2qrebDWgiHwncgnd; it equals docs/proposals/inbox-split/sweep.txt).
1/ 463.1: STEP 3g takes recorded guests from Episodes' Recording date too, not only Engagements at Recorded or Form
   filled, so a guest goes on the list in the week of the recording (15 were missing on 4 Nov).
2/ 463.6: STEP 4 flags any open Guest row with an empty Waiting on.
Usage: python3 patch.py <live sweep.txt> <out.txt>. Each edit is asserted exactly once."""
import sys, hashlib
src, out = sys.argv[1], sys.argv[2]
b = open(src, "rb").read()
assert hashlib.sha256(b).hexdigest().startswith("6783dd01"), "not the live sweep (39,131 / 6783dd01)"
s = b.decode("utf-8")
EDITS = [
 ("- One row per person interviewed, never one per episode (decision 232): for every Founder Thesis Engagement at Recorded or Form filled, the Guest and every co-guest",
  "- One row per person interviewed, never one per episode (decision 232): for every Founder Thesis Engagement at Recorded or Form filled, and every Founder Thesis Episode whose Recording date is today or earlier (its Engagements and Guests; whatever the Engagement's Status: a row still at Booked after its recording counts; decision 463, Akshay, 4 Nov: on the list in the week of the recording), except an Episode at Not releasing or Hold (a Hold guest is added once the Episode leaves Hold; Magic Bus stays out, a corrupted recording), the Guest and every co-guest"),
 ("Flag (skip if Next action already says the same thing):\n",
  "Flag (skip if Next action already says the same thing):\n- No owner (decision 463, Akshay, 4 Nov): an open guest Engagement (Kind empty; Status not They declined, We declined, Parked, Unresponsive or Published) whose Waiting on is empty, except an Outbound row at New (decision 167) and a Cold outreach Deal: fix it from the row and its thread when the owner is plain (OWNERS: a booked recording with nothing else open is Guest or PR; an unanswered mail from their side is Zoya's), with a Claude note line \"YYYY-MM-DD: Waiting on was empty, set <who> (daily sweep)\"; not plain: a report line \"no owner: <name> (<Status>)\" under For Akshay, nothing changed. Count both in the report.\n"),
 ("Founder Thesis guests list rows added and links filled;",
  "Founder Thesis guests list rows added and links filled (and recorded FT guests still missing, by name); open Guest rows with no owner (fixed, flagged);"),
]
for a, c in EDITS:
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, c)
assert s.count(chr(0x2014)) == b.decode("utf-8").count(chr(0x2014)), "new em dash"
ob = s.encode("utf-8")
assert len(ob) <= 65536 - 200
open(out, "wb").write(ob)
print(len(ob), hashlib.sha256(ob).hexdigest()[:16])
