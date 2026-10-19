"""AR-20261019-6: hourly response loop and Salesblink retirement, prompt edits.

Bases are the installed prompts read back 19 Oct 2026 (12:12 to 12:16 UTC).
Usage: python3 ar20261019-6-build.py <dir with trig_<id>.txt bases> <out dir>
"""
import hashlib, os, sys

def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()[:16]

HOURLY = ("HOURLY (AR-20261019-6): you run every hour. Each run takes what is new or unfinished; "
          "work already done and recorded is not redone, so the look-back windows are only the catch-up "
          "after a missed run. More runs never mean more mails: follow-ups keep their due dates, and every "
          "once-a-day or one-time step keeps its own check.")

EDITS = {
    # Inbox, 64,848 B, cap 65,536
    "trig_0189eZvAD8x4357cfevgZ3No": ("07fbac63b5ca3509", [
        ("and Chaandini keeps cold outreach (Salesblink) until their side replies",
         "and Chaandini keeps cold outreach until their side replies"),
        ("You capture; apart from the replies in STEPS 6 to 6e, RSVP archiving (STEP 7) and merging guest forms (STEP 7b) you never act.",
         "You capture; apart from the replies in STEPS 6 to 6e, RSVP archiving (STEP 7) and merging guest forms (STEP 7b) you never act. HOURLY (AR-20261019-6): each run takes only new or unfinished work; the look-back windows are catch-up after a missed run, and more runs never mean more mails."),
    ]),
    # Zoya
    "trig_01UPT8LDrBDL5JQqW91Awgbo": ("7f71e2302f155d6f", [
        ("No human is watching this run: never stop to ask a question.",
         "No human is watching this run: never stop to ask a question. " + HOURLY),
        ("Cold outreach stays Chaandini's (Salesblink sequences, C1 and C2)",
         "Cold outreach stays Chaandini's (C1 and C2; Salesblink is retired, AR-20261019-6)"),
        ("an active Salesblink sequence to them (Waiting on Chaandini or a Salesblink Activity in 14 days; recheck on its next step or end);",
         "a Salesblink mail to them recorded on any of their rows in the last 14 days (Salesblink was retired on 19 Oct 2026, so this ends by 2 Nov 2026; Waiting on Chaandini alone is never a hold);"),
        ("At most 10 nurture and revival mails a run,",
         "At most 10 nurture and revival mails a day (JST),"),
        ("At most 10 moves a run;",
         "At most 10 moves a day (JST);"),
    ]),
    # Calendar sync
    "trig_01Voiz5YsK2SnVf2STF8PoSH": ("3d9f8bd7bd5bcef9", [
        ("No human is watching this run: never stop to ask a question.",
         "No human is watching this run: never stop to ask a question. " + HOURLY),
        ("and Chaandini keeps cold outreach (Salesblink) until their side replies",
         "and Chaandini keeps cold outreach until their side replies"),
        ("Check the next 30 days.",
         "Run this audit in the first run at or after 08:00, 16:00 and 22:00 JST, as before; skip it in the other hourly runs. Check the next 30 days."),
    ]),
    # Daily sweep (stays daily)
    "trig_01MdfUFg2qrebDWgiHwncgnd": ("f0bf956ef3253898", [
        ("and Chaandini keeps cold outreach (Salesblink) until their side replies",
         "and Chaandini keeps cold outreach until their side replies"),
    ]),
    # WhatsApp (already hourly): the inbox is now hourly too
    "trig_01MnmJYorWrd61K7b5BCqXr1": ("d4c9986b750e9cbd", [
        ("The inbox routine acts on Your call at its next run (00:00, 08:00, 16:00, 21:00 JST).",
         "The inbox routine acts on Your call at its next run (hourly, a few minutes past each hour)."),
        ("If it is still in Your call one hour after the inbox run that should have taken it (00:00, 08:00, 16:00, 21:00 JST), post",
         "If it is still in Your call two hours after it went in, post"),
    ]),
}

src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
for tid, (base_sha, reps) in EDITS.items():
    s = open(os.path.join(src, tid + ".txt")).read()
    assert sha(s) == base_sha, (tid, sha(s))
    before = len(s.encode())
    for a, b in reps:
        assert s.count(a) == 1, (tid, a[:60])
        s = s.replace(a, b)
    open(os.path.join(out, tid + ".txt"), "w").write(s)
    print(tid, before, "->", len(s.encode()), sha(s))
