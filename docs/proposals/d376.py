"""Decision 376 (Akshay, 21 Oct, via the CTO): Zencastr no longer gives standalone transcripts, so Zoya asks Ranjita for
each Founder Thesis recording's transcript and follows up internal Task rows. Calendar gets STEP 4f (one Task row per
recording); Zoya gets INTERNAL TASKS. Master wording: Rules for Zoya, "Internal ad-hoc tasks" and "Transcript requests".
Built on the live prompts (routines/*.md at 7eec76c). Usage: python3 d376.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
CAL, ZOYA = "trig_01Voiz5YsK2SnVf2STF8PoSH", "trig_01UPT8LDrBDL5JQqW91Awgbo"
BASE = {CAL: (52992, "d036faaf20ef74cb"), ZOYA: (50247, "2e05abc111942c9e")}
EDITS = {
 CAL: [
  ("\nSTEP 4e. EPISODE RECOVERY",
   "\nSTEP 4f. TRANSCRIPT REQUESTS (decision 376, Akshay, 21 Oct: Zencastr no longer gives a standalone transcript; runs on its own, outside STEP 4's filter). For every Founder Thesis recording event on ad@thepodium.in that ended between 30 days ago and now and was not cancelled (the recording events STEP 4e reads), find its Engagement as STEP 4e does. Skip it if its Episode already has a Transcript file, or if an Engagement with Kind Task, Show Internal and For engagement = that guest row already has a Name starting \"Transcript: \" for that recording date. Else create once a Task row: Name \"Transcript: <guest> @ <company> (FT, <D Mon> recording)\", Kind Task, Show Internal (40019a301a7f81d1a33fd4fba7cd920c), For engagement = the guest row, Task state Handed over, Waiting on Zoya, Next action \"Zoya: ask Ranjita for the transcript (decision 376)\", Next date today, Source Agent, Source ID \"transcript:cal:<event id>\", Captured today. Report the rows created.\n\nSTEP 4e. EPISODE RECOVERY"),
 ],
 ZOYA: [
  ("Anything else, or an Engagement with no Show: do nothing.",
   "Engagements with Kind Task and Show Internal (INTERNAL TASKS). Anything else, or an Engagement with no Show: do nothing."),
  ("\nSNOOZED ASKS (decision 302",
   "\nINTERNAL TASKS (decision 376, Akshay, 21 Oct; Rules for Zoya, \"Internal ad-hoc tasks\" and \"Transcript requests\", has the wording). Kind Task rows with Show Internal are team work, never guest mail. a. A row Waiting on Zoya with Next action \"Zoya: ask Ranjita for the transcript (decision 376)\": send the transcript request from your inbox in that wording, To Ranjita, Cc Akshay (addresses from their People rows, tagged Team), naming the guest, company and recording date; then Waiting on Ranjita, Next action \"Ranjita: transcript for <guest>'s <D Mon> recording\", Next date 2 working days after the send, Activity \"Zoya sent: transcript request for <guest>\" (Kind Email out, Source ID the sent message id). b. Any Kind Task row with Show Internal Waiting on a team member whose Next date is today or earlier: follow up on the same thread, To that person, Cc Akshay, and set Next date 2 working days on, until the row is Done or On hold; a date they give wins; a reply saying it can't be done goes to Akshay's list (\"Akshay: <who> can't <what>\"), with Akshay in Waiting on. c. When Ranjita's reply carries a .txt, .docx or .pdf transcript, leave the mail in your inbox and set Next action \"Mac: attach transcript from Zoya's thread\"; the row closes (Task state Done) when its Episode has a Transcript file. These are internal: quiet hours, the 7-day limit and ONE PERSON, ONE ASK don't apply to them; LEAK CHECK and SHOW CHECK don't either. Log each send as in AFTER SEND; they count toward the daily cap.\nSNOOZED ASKS (decision 302"),
 ],
}
for tid, edits in EDITS.items():
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    n, h = BASE[tid]
    assert (len(s.encode()), sha(s.encode())) == (n, h), (tid, len(s.encode()), sha(s.encode()))
    for a, b in edits:
        assert s.count(a) == 1, (tid, a[:60], s.count(a))
        s = s.replace(a, b)
    b = s.encode()
    assert len(b) <= 65536 - 200 and "—" not in s, tid
    open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
    print(tid, len(b), sha(b))
