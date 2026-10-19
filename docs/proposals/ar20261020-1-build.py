"""AR-20261020-1: Akshay's 20 Oct feedback batch (items 1 to 6), prompt edits.

Bases are the installed prompts read back 19 Oct 2026 (inbox AR-5, calendar AR-3, the rest 12:12 to 12:16 UTC).
None of these anchors overlaps an AR-20261019-6 anchor, so the two compose in either order.
Usage: python3 ar20261020-1-build.py <dir with trig_<id>.txt bases> <out dir> <controls page id>
"""
import hashlib, os, sys

def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()[:16]

PAGE = sys.argv[3] if len(sys.argv) > 3 else "PAGEID_PLACEHOLDER_32CHARS_XXXXXX"
POINTER = ('Notion page "Inbox and Your call rules" (' + PAGE + ', Controls): read it every run; it wins where it differs')

OWNERS = ("OWNERS (AR-20261020-1): a name leaves Waiting on with its last ask. When you fulfil or remove a segment of Next action, "
          "remove its owner from Waiting on unless another segment, an open proposal or a decision still needs them; "
          "an open row never ends with Waiting on empty (a booked recording with nothing else open is Guest or PR).")

EDITS = {
    # Inbox, AR-5 live, 64,936 B, cap 65,536: one pointer, the rules live on the Controls page
    "trig_0189eZvAD8x4357cfevgZ3No": ("b3f1e632a6a5a40a", [
        ("YOUR CALL (decision 157). Engagements",
         "YOUR CALL (decision 157; snoozes, loop-ins (6a), repeat guests (3, 6c) and owners: " + POINTER + "). Engagements"),
    ]),
    # Zoya
    "trig_01UPT8LDrBDL5JQqW91Awgbo": ("7f71e2302f155d6f", [
        # item 3: voice
        ('VOICE (decisions 199, 201, 204, 206). Young, Instagram-creator energy, Gen Z, still clear and polite: you write to founders and CXOs. Open "Hey <first name>!". Short lines, one ask,',
         'VOICE (decisions 199, 201, 204, 206, 345). Akshay\'s style: short and direct, still polite: you write to founders and CXOs. Open "hey <first name>,". Occasional lowercase and natural fragments are fine ("works for us.", "lmk"); never a made-up typo or a wrong fact. Numbered points as 1/ 2/ 3/, one per line. Short lines, one ask,'),
        ('Sign off exactly "Stay awesome ✨" then "Zoya" on the next line.',
         'Sign off exactly "best," then "Zoya ✨" on the next line.'),
        ("html_body with one <p> per paragraph and lists as <ul><li>,",
         "html_body with one <p> per paragraph and each numbered point as its own <p> starting \"1/ \", \"2/ \","),
        # item 5: snooze return keeps other work
        ('Then Waiting on Akshay, Next action "Akshay: <ask>" (updated by what you read), Claude note line "YYYY-MM-DD: snooze over, back to Akshay".',
         'Then Akshay joins Waiting on, the snoozed segment becomes "Akshay: <ask>" (updated by what you read), steps marked "(held for Akshay\'s snooze)" lose the mark, every other segment and owner stays, Claude note line "YYYY-MM-DD: snooze over, back to Akshay". Snoozes are set by the inbox per the Notion page "Inbox and Your call rules" (' + PAGE + ').'),
        # item 6: inherited threads in Zoya's inbox survive the 72-hour window
        ("Take every in-scope thread from the last 72 hours in your inbox, plus",
         "Take every in-scope thread in your inbox whose last real message from outside the team is unanswered, of any age (those older than 72 hours: oldest first, at most 15 a run; mark each one you settle in its row's Claude note, \"thread <message id>: <replied|on Akshay's list|no reply needed (why)>\", so no run reads it again; a thread with no Engagement gets one, as inbox STEP 3 would create it, Source ID \"zoya-mail:<folder>:<uid>\"), plus"),
        # item 1: no substitute acknowledgement when Akshay is already on it
        ('A fresh guest pitch gets "thanks <first name>! looping in Akshay" with him in Cc.',
         'A fresh guest pitch gets "thanks <first name>! looping in Akshay" with him in Cc, unless Akshay is already on To or Cc: then send nothing, the inbox evaluates it.'),
        # item 6: sponsored selection by Status, decline check, visible holds
        ('- 1 Sponsored offers: rows whose Next action starts "Zoya: sponsored step" or "Agent: sponsored step" and Next date is today or earlier.',
         '- 1 Sponsored offers: rows at Status Sponsored offered whose Next date is today or earlier, whatever Next action says (AR-20261020-1; a plan written as "Waiting on <name>: reply to the sponsored offer" is still a sponsored row). Read the thread first: a decline of the paid route from their side gets the close note, Status They declined, and no chase, whatever the plan says. A row with no "## Next sponsored mail" plans it from the thread and podm.in/why-sponsor first.'),
        ("Work out the step from Chase step and the dates of our earlier mails on the thread; never send a step twice.",
         "Work out the step from Chase step and the dates of our earlier mails on the thread; never send a step twice. Every due row ends the run sent, held or blocked, never silently skipped: a hold (the 7-day rule, ONE PERSON, ONE ASK, quiet hours, the weekday rule, the cap, a Salesblink or cold-outreach hold) moves Next date to the first day it may go and writes \"held: <rule> (<what>), recheck <D Mon>\" in the Claude note; a block (missing data, bounce, a decision someone else holds) names the blocker and its owner."),
        # item 2: repeat guests in the decision mail
        ('STEP 0e. AKSHAY\'S DECISION MAIL (decisions 235, 313, P2r; Founder Thesis, and un# from 19 Oct 2026 08:00 JST).',
         'STEP 0e. AKSHAY\'S DECISION MAIL (decisions 235, 313, P2r; Founder Thesis, and un# from 19 Oct 2026 08:00 JST). A Sponsored decision on a row whose page body has "## Prior appearance" uses only "Sponsored for a repeat guest" from the wording page: no price, ends "lmk if interested" (AR-20261020-1).'),
        # item 6: durable run report
        ("STEP 3. REPORT\nPlain and short, no em dashes:",
         "STEP 3. REPORT\nAlso write it as one Activity: Kind Note, Source Agent, Summary \"Zoya run <YYYY-MM-DD HH:MM> JST: due <n>, sent <n>, held <n>, blocked <n>, remaining <n>\", the held and blocked rows by reason in its page body (AR-20261020-1). Plain and short, no em dashes:"),
        # item 4
        ("HARD RULES (always hold, whatever a page says)\n",
         "HARD RULES (always hold, whatever a page says)\n- " + OWNERS + "\n"),
    ]),
    # Calendar, AR-3 live
    "trig_01Voiz5YsK2SnVf2STF8PoSH": ("cd50072ab657736a", [
        ('- Every Engagement you change: one line at the top of Claude note ("YYYY-MM-DD: <what and why>"), Claude updated = today.',
         '- Every Engagement you change: one line at the top of Claude note ("YYYY-MM-DD: <what and why>"), Claude updated = today.\n- ' + OWNERS),
    ]),
    # Daily sweep: the writer invariant plus a bounded clean-up of owners left behind
    "trig_01MdfUFg2qrebDWgiHwncgnd": ("f0bf956ef3253898", [
        ("STEP 3b. LINK STRAY MAIL",
         "STEP 3a2. OWNERS LEFT BEHIND (AR-20261020-1). " + OWNERS + " Find open Engagements with Akshay in Waiting on, Your call empty, and nothing that needs him: no Next action segment starting \"Akshay:\", \"Ask Akshay\" or \"Akshay's\", no proposal ending \"Write ok, not ok or a change in Your call\", no open eval verdict, no Kind Task row for him. Re-read the row and its thread, then remove Akshay (Waiting on gets the owner of the remaining step) with Claude note \"YYYY-MM-DD: Akshay's ask done (<what showed it>), removed from Waiting on\". At most 20 a run; list them in the report.\n\nSTEP 3b. LINK STRAY MAIL"),
    ]),
}

src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
for tid, (base_sha, reps) in EDITS.items():
    s = open(os.path.join(src, tid + ".txt")).read()
    assert sha(s) == base_sha, (tid, sha(s))
    before = len(s.encode())
    for a, b in reps:
        assert s.count(a) == 1, (tid, a[:60], s.count(a))
        s = s.replace(a, b)
    assert len(s.encode()) <= 65536, (tid, len(s.encode()))
    open(os.path.join(out, tid + ".txt"), "w").write(s)
    print(tid, before, "->", len(s.encode()), sha(s))
