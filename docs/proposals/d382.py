"""Decision 382 (Akshay, 21 Oct, via the CTO ~22:00 JST; Rules for Zoya already carries it). 1/ un# rows at Status Booking
are chased every 2 working days until a recording is on the calendar (Sri's windows are short); their own date wins; this
beats the 5-working-day PR gap and the 7-day person limit for these rows only. 2/ A founder who wrote to us directly and went
quiet: a sponsored row goes to nurture as now; a non-sponsored row goes on Akshay's list as one ask, nothing sent first.
Zoya, sweep and inbox: every branch that moves a row to nurture, chase run-outs included. Decision 383 (CTO, same delta):
inbox, calendar and Zoya match People before creating one (LinkedIn slug, Email, Other emails, then normalised name plus
company); a name-only match links the existing row and flags it Possible duplicate. Built on the live prompts (Zoya 380,
sweep, inbox and calendar as deployed 21 Oct). HealthQuad fixes (CTO, ~22:45 JST, a live miss): a no to paying on any row
where we offered sponsored gets the close note, never an acknowledgement; a direct reply to their latest message is not a
chase, so neither the 7-day limit nor the hand-written pause holds it (quiet hours and caps still do). The calendar's FT
thank-you draft uses the wording page's approved text as it stands, with no local copy.
Decision 385 (Akshay via the CTO): a step about a person or company with an Engagement goes on that Engagement as a Next
action segment, not on a new Task row; all five routines that create Task rows (WhatsApp from its booking build too).
Decisions 386 and 387 (Akshay via the CTO): routine 5 ends with one ask on Akshay's list after the page's last chaser
(five), never closing on silence; the inbox's draft-and-edit comparison (STEP 2b a and b) is retired, keeping only the
Send draft status move and 2b c.
Usage: python3 d382.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
INBOX, ZOYA, SWEEP = "trig_0189eZvAD8x4357cfevgZ3No", "trig_01UPT8LDrBDL5JQqW91Awgbo", "trig_01MdfUFg2qrebDWgiHwncgnd"
CAL, WA = "trig_01Voiz5YsK2SnVf2STF8PoSH", "trig_01MnmJYorWrd61K7b5BCqXr1"
BASE = {INBOX: (57898, "a0fd61ea7a394a08"), ZOYA: (55592, "98c508cf990d341d"), SWEEP: (31157, "64d6170090757a62"),
        CAL: (54137, "f32d15fb85d8da18"), WA: (25202, "269a436c477194c2")}
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
CLOSE_OLD = "\"Zoya: send Akshay's sponsored close note to <name>\""
CLOSE_NEW = "\"Zoya: send the sponsored close note to <name>\""
EDITS[INBOX] += [
 ("on any row whose thread carries our sponsored offer, whatever its Status short of Booked",
  "on any row where we offered the sponsored route (on this thread, on any other thread with their side in ad@thepodium.in or "
  "Zoya's inbox, or Tier Sponsored), whatever its Status short of Booked"),
 ("put " + CLOSE_OLD + " first in Next action.", "put " + CLOSE_NEW + " first in Next action."),
 ("or a cc where a team member is the addressee.",
  "or a cc where a team member is the addressee. Never for a no to paying: that is STEP 3's sponsored no and gets "
  + CLOSE_NEW + " (decision 379)."),
]
EDITS[ZOYA] += [
 ("(the inbox hands these to you as " + CLOSE_OLD + ").",
  "(the inbox hands these to you as " + CLOSE_NEW + ", older rows " + CLOSE_OLD + ")."),
 ("any routine step don't count as hand-written.",
  "any routine step don't count as hand-written.\n- A reply to their latest message (a close note, an acknowledgement, an "
  "answer to what they asked) is not a chase: the 7-day limit, ONE PERSON, ONE ASK and the hand-written pause don't hold it; "
  "quiet hours and the caps still do (CTO, 21 Oct, the HealthQuad close note held by the limit)."),
]
EDITS[CAL] = [
 ("Wording: Rules for Zoya, Mail and WhatsApp wording, \"FT thank-you after recording\" (or \"FT thank-you, PR block variant\" "
  "when a PR is on the thread), in Akshay's voice: \"Akshay loved the conversation!\" becomes \"I loved the conversation!\", "
  "signed \"Regards,\" then \"Akshay\", patron paragraphs dropped for a Sponsored guest, FORM LINK for the form, and the line "
  "\"The transcript of the episode is attached for your reference.\" kept so he attaches it.",
  "Wording: Rules for Zoya, Mail and WhatsApp wording, \"FT thank-you after recording\" (Akshay's approved version, 21 Oct), "
  "read fresh each run and used exactly as the page has it: fill only its placeholders and follow its bracketed notes (patron "
  "paragraphs out for a Sponsored guest, the PR block only when a PR is on the To line, the transcript line only while "
  "transcripts are being attached, the form link as a real link); never a retired variant."),
]
EDITS[ZOYA].append((
 "- 5 Guest form: Status Recorded, no guest form, counting from the thank-you mail. Akshay in Cc.",
 "- 5 Guest form: Status Recorded, no guest form, counting from the thank-you mail. Akshay in Cc. The chaser count and days "
 "come from the routine 5 page (decision 386: five). After the last, no form and no reply for 7 days: not nurture; Waiting on "
 "Akshay, Next action \"Ask Akshay: no form from <guest> after <n> chasers. Chase another way, nurture, or close?\". The row "
 "never closes on silence."))
EDITS[INBOX] += [
 ("STEP 2b. LEARN FROM SENT MAIL (decision 102)",
  "STEP 2b. AKSHAY'S SENT MAIL (decision 387 retired the draft-and-edit comparison of decision 102)"),
 ("a. Sent from a draft: if an Activity with Kind Draft and Edit size empty exists on the same thread (Link) or on the same "
  "Engagement with the same subject, this mail is that draft going out. Compare the sent body with the drafted text in that "
  "Draft Activity's page body and set, on the Draft Activity: Edit size (None: only names, dates or greetings differ; Minor: "
  "small wording changes, up to one sentence; Major: a paragraph added, removed or rewritten; Rewritten: mostly new text), and "
  "Edit note (one line on what changed, for example \"dropped the patron paragraphs, added the PR's name\"). If the Engagement",
  "a. Sent from a draft: a Draft Activity on the same thread (Link) or on the same Engagement with the same subject means this "
  "mail is that draft going out (nothing is compared or scored). If the Engagement"),
 ("\nb. A Draft Activity older than 14 days that was never sent: Edit note \"not sent\", Edit size empty.\nc. His mail answers",
  "\nb. His mail answers"),
 ("(a Draft Activity on the row with Edit size empty)", "(a Draft Activity on the row whose draft is still in Gmail)"),
 ("and set that Draft Activity's Edit note \"not sent: <name> sent it by hand <date>, draft deleted\"",
  "and add the Claude note line \"YYYY-MM-DD: agent draft deleted, <name> sent it by hand\""),
 ("Sent drafts matched (edit size).", "Send draft rows moved on."),
]
# 386: the inbox's 3-chases branch never closes a Recorded row waiting on its form
EDITS[INBOX] = [(a, b.replace("or a un# row at Booking (decision 382: chased until a recording is on the calendar)",
  "or a un# row at Booking (decision 382: chased until a recording is on the calendar), or a Recorded row waiting on its "
  "guest form (decision 386: Zoya's routine 5 ends it)")) for a, b in EDITS[INBOX]]
for tid, line in PEOPLE.items():
    EDITS[tid].insert(0, (line, line + MATCH))
KIND = "closing it never touches the row in its For engagement or any other ask."
ONROW = (KIND + " PERSON STEPS GO ON THEIR ROW (decision 385, Akshay, 21 Oct): before you create a Kind Task row, look for an "
         "Engagement for the person or company it names (as Guest, Via, Stakeholder or Organisation; any Status, parked or closed "
         "included). One fits: write the step there as a Next action segment \"<owner>: <step>\" after \" | \" (other segments "
         "kept), add the owner to Waiting on, and create no Task row; several people, each one's own row. Create a Task row only "
         "when no Engagement fits. This covers guest-facing steps only: internal team requests (Show Internal, decision 376: "
         "transcripts to Ranjita, anything to Jaya or Sarika) and rows a step below keys by its own Source ID (transcript:, "
         "precall:) stay Kind Task rows.")
EDITS[WA] = []
for tid in (INBOX, ZOYA, SWEEP, CAL, WA):
    EDITS[tid].append((KIND, ONROW))
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
