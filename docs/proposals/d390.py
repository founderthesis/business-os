"""Fix batch of 22 Oct (CTO, from misses Akshay flagged after the d382 deploy), plus decision 390.
1/ Run order (Byufuel, Escobar Bandra): Zoya's Partial runs spent their time on overdue LT chase rows and never sent
   Akshay's queued decision mail. Every run now does replies and queue steps before any follow-up, and caps LT chase and
   nurture mails per run so they can't starve the rest.
2/ The inbox logged Akshay's "adding @Zoya" loop-ins as "Zoya sent: holding reply"; they are logged as loop-ins now.
3/ The inbox loop-in went to a closed thread (Mirabilis, Parked); closed rows and threads we closed get no loop-in, and
   neither does Zoya's ad@ fallback.
4/ Decision 390 (Akshay, 22 Oct: "Yes"): someone outside the team writing on a row that waits on Akshay gets a one-line
   holding reply from Zoya the same run, at most once per thread per 7 days; Akshay's item stays.
Zoya and inbox, on the live prompts (d382 rev 7 as deployed 22 Oct). Usage: python3 d390.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
INBOX, ZOYA = "trig_0189eZvAD8x4357cfevgZ3No", "trig_01UPT8LDrBDL5JQqW91Awgbo"
BASE = {INBOX: (59880, "e43762c3e3f36909"), ZOYA: (58765, "3bf4743448026ac2")}
CLOSED = "Parked, We declined, They declined or Unresponsive"
HOLD = ("\"hi <first name>, checking with akshay, will come back by <weekday, 3 working days out>.\"")
EDITS = {
 ZOYA: [
  ("STEP 2. FOLLOW-UPS DUE\nIn-scope Engagements only.",
   "RUN ORDER (CTO, 22 Oct: Byufuel's and Escobar Bandra's decision mails sat queued while runs went Partial on LT chase "
   "rows). Every run works STEP 0 to STEP 1b in full before STEP 2: Akshay's feedback, his decision mails (STEP 0e), "
   "every other queue step Waiting on Zoya, replies to people who wrote to us and payments, oldest first, whatever their "
   "Next date. Only then STEP 2: routines 1 to 6 and 8, oldest due first, then routine 7 and nurture rows, at most 10 of "
   "those a run; the rest move Next date to the next working day with \"held: LT chase cap\" in the Claude note. A run short "
   "of time stops inside STEP 2, never before the queue is done, and a Partial report names every queue step left.\n\n"
   "STEP 2. FOLLOW-UPS DUE\nIn-scope Engagements only."),
  ("c. Not routine (Rules for Zoya sections 4 and 7:",
   "c. Not routine, or a message on a row that waits on Akshay's decision or wording (Rules for Zoya sections 4 and 7:"),
  ("Set Waiting on Akshay, Next action \"Ask Akshay: <who> asks <what>, in one line\".\nA pitch answered",
   "Set Waiting on Akshay, Next action \"Ask Akshay: <who> asks <what>, in one line\". Then the holding reply (decision 390, "
   "Akshay, 22 Oct), this run, from your inbox on that thread, unless one went on it in the last 7 days: one line, " + HOLD +
   " It is a reply, not a chase: the 7-day limit and ONE PERSON, ONE ASK don't hold it; quiet hours do. Log \"Zoya sent: "
   "holding reply to <name>\"; Akshay's item stays.\nA pitch answered"),
  ("if their side wrote last, send from there only \"thanks <first name>, adding @Zoya to coordinate\" (Cc you;",
   "if their side wrote last, send from there only \"thanks <first name>, adding @Zoya to coordinate\" (never on a row at "
   + CLOSED + ", or after our decline or close-out on the thread; Cc you;"),
 ],
 INBOX: [
  ("Skip repeat pitches (STEP 3) and vendor pitches (STEP 6b). Log \"Zoya sent: holding reply to <name>\";",
   "Skip repeat pitches (STEP 3), vendor pitches (STEP 6b), and any thread whose row is " + CLOSED + " or whose last mail "
   "from our side was a decline or a close-out: capture it only (CTO, 22 Oct: a loop-in reopened a Parked thread). Log "
   "\"Akshay to <name>: Zoya loop-in\" (Kind Email out, Source ID the sent message id; a loop-in, never logged as a reply);"),
  ("set Waiting on Akshay with Next action \"Ask Akshay: <who> asks <what>, in one line\". These are the only mails",
   "set Waiting on Akshay with Next action \"Ask Akshay: <who> asks <what>, in one line\". On an Engagement, also add Zoya to "
   "Waiting on with the queue step \"Zoya: holding reply to <who> (decision 390)\", unless a holding reply went on that "
   "thread in the last 7 days; Akshay's item stays. These are the only mails"),
 ],
}
for tid, edits in EDITS.items():
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == BASE[tid], (tid, len(s.encode()), sha(s.encode()))
    dashes = s.count("—")
    for a, b in edits:
        assert s.count(a) == 1, (tid, a[:60], s.count(a))
        s = s.replace(a, b)
    b = s.encode()
    assert len(b) <= 65536 - 200 and s.count("—") == dashes, (tid, len(b))
    open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
    print(tid, len(b), sha(b))
