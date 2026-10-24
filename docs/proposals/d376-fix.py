"""Cleanup's fixes to decision 376 (d376.py at e33b94f), applied to its output. Usage: python3 d376-fix.py <d376 out dir> <out dir>
Live bases: calendar 52,992 / d036faaf20ef74cb, Zoya 50,247 / 2e05abc111942c9e. d376.py gives calendar 53,955 / 268477a7d70f0fb4
and Zoya 51,816 / 6fa587ed0c28903f; this gives calendar 53,973 / c84e76c9db708291 and Zoya 52,034 / d74d56bb06f20147.
1/ Rows are found by Source ID and Task state, never by Name or Next action wording. 2/ A retry never creates a second row or
resends (Source ID lookup; no send while an Email out Activity is linked). 3/ The calendar backfill takes at most 5 rows a run.
4/ Follow-ups never go to Akshay (decision 325) and say which thread. 5/ Only quiet hours and the 7-day limit are lifted for
internal mail; LEAK CHECK and SHOW CHECK still apply. 6/ Zoya closes the row once the Episode has its Transcript file."""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
CAL, ZOYA = "trig_01Voiz5YsK2SnVf2STF8PoSH", "trig_01UPT8LDrBDL5JQqW91Awgbo"
BASE = {CAL: (53955, "268477a7d70f0fb4"), ZOYA: (51816, "6fa587ed0c28903f")}
EDITS = {
 CAL: [
  ("Skip it if its Episode already has a Transcript file, or if an Engagement with Kind Task, Show Internal and For engagement = that guest row already has a Name starting \"Transcript: \" for that recording date. Else create once a Task row:",
   "Skip it if its Episode already has a Transcript file, or if any Engagement already has Source ID \"transcript:cal:<event id>\" (look it up first; a retry never creates a second row). Else create a Task row:"),
  ("Captured today. Report the rows created.", "Captured today. At most 5 new rows a run, oldest recording first. Report the rows created."),
 ],
 ZOYA: [
  ("a. A row Waiting on Zoya with Next action \"Zoya: ask Ranjita for the transcript (decision 376)\": send",
   "a. A row with Task state Handed over, Waiting on Zoya and Source ID starting \"transcript:cal:\", and no Email out Activity linked to it yet (a retry never resends): send"),
  ("Activity \"Zoya sent: transcript request for <guest>\" (Kind Email out, Source ID the sent message id).",
   "Activity \"Zoya sent: transcript request for <guest>\" (Kind Email out, Source ID the sent message id, linked to the row)."),
  ("b. Any Kind Task row with Show Internal Waiting on a team member whose Next date is today or earlier: follow up on the same thread,",
   "b. Any Kind Task row with Show Internal Waiting on a team member other than Akshay whose Next date is today or earlier, and no Email out Activity linked to it today: follow up on the thread of its last Email out Activity (none: a new mail),"),
  ("the row closes (Task state Done) when its Episode has a Transcript file.",
   "on the first run after its Episode has a Transcript file, set Task state Done and clear Waiting on."),
  ("These are internal: quiet hours, the 7-day limit and ONE PERSON, ONE ASK don't apply to them; LEAK CHECK and SHOW CHECK don't either.",
   "These are internal: quiet hours and the 7-day limit (LIMITS and ONE PERSON, ONE ASK) don't apply to them; every other check does."),
 ],
}
for tid, edits in EDITS.items():
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == BASE[tid], tid
    for a, b in edits:
        assert s.count(a) == 1, (tid, a[:60])
        s = s.replace(a, b)
    b = s.encode()
    assert len(b) <= 65536 - 200 and "—" not in s, tid
    open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
    print(tid, len(b), sha(b))
