"""Decision 382 (Akshay, 21 Oct, via the CTO ~22:00 JST; Rules for Zoya already carries it). 1/ un# rows at Status Booking
are chased every 2 working days until a recording is on the calendar (Sri's windows are short); their own date wins; this
beats the 5-working-day PR gap and the 7-day person limit for these rows only. 2/ A founder who wrote to us directly and went
quiet: a sponsored row goes to nurture as now; a non-sponsored row goes on Akshay's list as one ask, nothing sent first.
Zoya, sweep and inbox: every branch that moves a row to nurture, chase run-outs included. Decision 383 (CTO, same delta):
inbox, calendar and Zoya match People before creating one (LinkedIn slug, Email, Other emails, then normalised name plus
company); a name-only match links the existing row and flags it Possible duplicate. Built on the live prompts (Zoya 380,
sweep, inbox and calendar as deployed 21 Oct). Usage: python3 d382.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
INBOX, ZOYA, SWEEP = "trig_0189eZvAD8x4357cfevgZ3No", "trig_01UPT8LDrBDL5JQqW91Awgbo", "trig_01MdfUFg2qrebDWgiHwncgnd"
CAL = "trig_01Voiz5YsK2SnVf2STF8PoSH"
BASE = {INBOX: (57898, "a0fd61ea7a394a08"), ZOYA: (55592, "98c508cf990d341d"), SWEEP: (31157, "64d6170090757a62"),
        CAL: (54137, "f32d15fb85d8da18")}
# decision 383: one rule under the People line, for every create in the prompt
MATCH = ("\n  PEOPLE MATCH (decision 383), before you create any People row anywhere below: 1/ look for the person by LinkedIn "
         "(the slug after /in/, case and a trailing slash ignored), Email and Other emails; 2/ then by Name with spaces, dots, "
         "hyphens and initials ignored, plus the same Organisation or email domain. Found: use that row (a new address goes in "
         "Other emails). 3/ The same name alone (company different or unknown): don't create; use that row, set Match status "
         "Possible duplicate and add a dated line to Duplicate check \"YYYY-MM-DD <routine>: name-only match for <the address or "
         "company seen>\" (once per address), and list it in the report. Create only when none of these finds a row. Never "
         "merge or delete People rows.")
PEOPLE = {INBOX: "- People: collection://e6c44319-7f81-4da6-8b80-8441a4875d7a  (Email, Other emails, Organisation, LinkedIn, Tags; team members are tagged Team, e.g. Sarika, Jaya)",
          CAL: "- People: collection://e6c44319-7f81-4da6-8b80-8441a4875d7a  (Email, Other emails, LinkedIn, Blurb, Tags; team tagged Team)",
          ZOYA: "- People: collection://e6c44319-7f81-4da6-8b80-8441a4875d7a (Email, Other emails, Phone, Tags; team members are tagged Team)"}
# the one branch every nurture move checks first
DIRECT = ("a founder who wrote to us directly (no PR or agency on the thread) on a row with no sponsored offer on its thread "
          "and Tier not Sponsored, and not at Status Booking (decision 382: a recording-slot chase that runs out always goes to "
          "nurture, whoever pitched it): don't move it and send nothing; put it on Akshay's list once, Akshay added to "
          "Waiting on, the chase segment of Next action \"Akshay: <guest> went quiet after <the open ask> (since <D Mon YYYY>): "
          "nurture, park or decline?\", Claude note \"YYYY-MM-DD: went quiet, on Akshay's list (decision 382)\". A sponsored row "
          "goes to nurture as below.")
UN = " un# rows at Status Booking (decision 382, Akshay, 21 Oct: Sri's windows are short)"
EDITS = {
 ZOYA: [
  ("their own date wins (decision 375).",
   "their own date wins (decision 375)." + UN + ": 2 working days after our last ask until a recording is on the calendar, "
   "these rows only; this beats the 5-working-day gap, the 30 quiet days, the 7-day limit in LIMITS, the STALENESS GATE's span "
   "and the 3 unanswered chases; a decline, a stop or a hold still ends it, and their own date wins."),
  ("- 3 Recording slot: Status Booking, no recording on the calendar.",
   "- 3 Recording slot: Status Booking, no recording on the calendar. On un#, every 2 working days (PR COORDINATION, decision 382)."),
  ("3 working days for Tier 1 inbound in its first month)",
   "3 working days for Tier 1 inbound in its first month, 2 for un# Booking rows)"),
  ("When a routine runs out (last step,",
   "Before any move to nurture, " + DIRECT + " When a routine runs out (last step,"),
 ],
 SWEEP: [
  ("(c) An approved pursuit (AR-20261019-1:",
   "(b2) " + DIRECT[0].upper() + DIRECT[1:] + " (c) An approved pursuit (AR-20261019-1:"),
 ],
 INBOX: [
  ("an Akshay or Jaya decision or hold on this pursuit: change nothing. (b) In nurture: Chase step 0 only. (c) An approved pursuit:",
   "an Akshay or Jaya decision or hold on this pursuit, or a un# row at Booking (decision 382: chased until a recording is on "
   "the calendar): change nothing. (b) In nurture: Chase step 0 only. (b2) " + DIRECT[0].upper() + DIRECT[1:] +
   " (c) An approved pursuit:"),
 ],
}
EDITS[CAL] = []
for tid, line in PEOPLE.items():
    EDITS[tid].insert(0, (line, line + MATCH))
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
