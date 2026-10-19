"""AR-20261020-1 rev 2: Akshay's 20 Oct feedback batch (items 1 to 6), decisions 346 and 347, prompt edits.

rev 2 (Codex 20 Oct 08:03 review): snoozes matched anywhere in Next action with their own dates; repeat wording only for
a completed appearance on the same show; the run report is the accepted AR-20261018-8 RUN RECORD (Source empty, run:zoya:<run id>);
loop-ins and incidental Cc never start the 7-day clock (decision 346); WhatsApp blurb posts and rewrites retired (decision 347).

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

RUN_RECORD = ('RUN RECORD (AR-20261018-8). Before your first Notion write, fix this run\'s id once: Bash printenv CLAUDE_CODE_REMOTE_SESSION_ID; if empty, once echo "syn-$(date -u +%Y%m%dT%H%M%SZ)-$(od -An -N4 -tx1 /dev/urandom | tr -d \' \\n\')" (synthetic); if neither works, write no record and report "run record skipped: no id". Never derive it again. Then one Activity: Kind Note, Source empty, Summary "Run zoya <YYYY-MM-DD HH:MM> JST: Started", Source ID "run:zoya:<run id>", Date the start, Captured today, linked to nothing. Unclear create response: query that Source ID first and reuse its row; never a second. Last write: the same row, Summary "Run zoya <start> JST: <Completed|No-op|Partial|Failed>" (No-op: nothing to act on; Partial: a step failed or was skipped; Failed: stopped early), body = the report plus end time, deployment reference (Unknown unless known), counts, errors, blocked items with next owner and links to this run\'s Activities. Invent nothing. The run id never replaces a send\'s idempotency key or any dedupe. The record never sets Last activity, Waiting on or a contact date and never counts toward the cap. A failed write: retry once, then report it; never repeat a business action.')

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
        # item 5: snoozes matched anywhere in Next action, each on its own date (rev 2)
        ('A row Waiting on Zoya whose Next action starts "Zoya: back to Akshay on <D Mon>: <ask>" is an ask of Akshay\'s he has put off. Before that date do nothing with it.',
         'Any segment of Next action, wherever it sits, reading "Zoya: back to Akshay on <D Mon>: <ask>" is an ask of Akshay\'s he has put off (AR-20261020-1). Find these by the segment, not by Next date or position; each returns on its own <D Mon>, whatever Next date or another segment says. Before its date leave that segment alone; the row\'s other segments are worked as usual.'),
        ('Then Waiting on Akshay, Next action "Akshay: <ask>" (updated by what you read), Claude note line "YYYY-MM-DD: snooze over, back to Akshay".',
         'Then rewrite only that segment as "Akshay: <ask>" (updated by what you read), add Akshay to Waiting on, drop "(held for Akshay\'s snooze)" from the steps that waited on it, keep every other segment and owner, set Next date to the earliest date still open on the row, Claude note line "YYYY-MM-DD: snooze over, back to Akshay (<ask, short>)". A segment already rewritten is done: a retry changes nothing.'),
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
         'STEP 0e. AKSHAY\'S DECISION MAIL (decisions 235, 313, P2r; Founder Thesis, and un# from 19 Oct 2026 08:00 JST). A Sponsored decision on a row whose "## Prior appearance" section names a completed recording on this row\'s own Show uses only "Sponsored for a repeat guest" from the wording page, naming that show and month exactly as the section has them: no price, ends "lmk if interested" (AR-20261020-1). An appearance on another show only is context, never repeat wording.'),
        # item 6: the accepted AR-20261018-8 run record (rev 2), with this batch's counts
        ("\n\nSTEP 0. GO-LIVE AND AKSHAY'S FEEDBACK\n",
         "\n\n" + RUN_RECORD + "\n\nSTEP 0. GO-LIVE AND AKSHAY'S FEEDBACK\n"),
        ("STEP 3. REPORT\nPlain and short, no em dashes:",
         "STEP 3. REPORT\nAlso the run record's page body (RUN RECORD), opening with one line: due <n>, sent <n>, held <n> (by rule), blocked <n>, remaining <n>. Plain and short, no em dashes:"),
        # decision 346: loop-ins and incidental Cc never start the 7-day clock
        ("- At most one mail from our side to a person per 7 days, whoever sent it.",
         "- At most one mail from our side to a person per 7 days, whoever sent it. Only a substantive mail to them counts (decision 346, Akshay, 20 Oct): an ask, offer, follow-up or answer addressed to them. An administrative loop-in (\"adding @Zoya to coordinate\", an acknowledgement) and an incidental Cc (they are only copied on a mail whose ask is to someone else) never start or reset the clock; a mail with a real ask counts even if it also loops someone in."),
        ("Hold this mail only for: a mail to them from any row in the last 7 days (14 for nurture or revival);",
         "Hold this mail only for: a substantive mail to them (LIMITS, decision 346) from any row in the last 7 days (14 for nurture or revival);"),
        # item 4
        ("HARD RULES (always hold, whatever a page says)\n",
         "HARD RULES (always hold, whatever a page says)\n- " + OWNERS + "\n"),
    ]),
    # WhatsApp: blurb posts and rewrites in the Zoya group retired (decision 347); everything else unchanged
    "trig_01MnmJYorWrd61K7b5BCqXr1": ("d4c9986b750e9cbd", [
        (" and the Skill tool (skill founder-thesis-blurb, for blurb rewrites). If either is missing,",
         ". If either is missing,"),
        (" A blurb goes as its own message so he can forward it untouched.",
         " You never post a blurb here (decision 347)."),
        (' Posted blurbs: Summary "Zoya posted: blurb for <guest>", Source ID "blurb:<engagement page id>:<blurb date>".',
         ''),
        ("e. A change to a blurb: a message that quotes a blurb post, or starts \"blurb\" and names the guest, or says what to change about the last blurb posted: see 0b, b.",
         "e. A message about a blurb (it quotes one, starts \"blurb\", or asks to change one): never rewrite or post it here (decision 347). Add his words at the top of the guest's newest \"Blurb, <date>\" section on their Founder Thesis Engagement as \"Akshay, <YYYY-MM-DD> (WhatsApp): <his words>\", then reply once \"Zoya ✨ noted for <guest>'s blurb. Edit it in its chat: <link>\" with the \"Editing chat:\" link under that section, or \"Zoya ✨ noted for <guest>'s blurb; its editing chat isn't set up yet\" if there is none."),
        ('0b. BLURBS\na. New blurbs: FT Community rows with Blurb not empty and Membership To invite or Invited, whose Blurb link\'s page body has a "Blurb, <date>" section from the last 14 days with no "Zoya posted: blurb for" Activity for that page and date. Post two messages: first "Zoya ✨ blurb: <guest> @ <company> (<recorded or precall> <D Mon>)" plus the line "page: <Engagement URL>" and "reply with changes and I\'ll rewrite it"; then the blurb text alone, exactly as on the page. Log it.\nb. Edits: read the Notion page "Blurb sources" (3fc19a301a7f81eb9bcfc36f3a1cd6a9), then rerun the founder-thesis-blurb skill (no Slack, never ask a question) with the current blurb, its Source line, the Episode\'s Transcript file (read it through Notion: fetch with file URLs, then download; if it can\'t be read, change only the wording he asked for and add no new facts) and Akshay\'s message as the brief: keep what he didn\'t object to, change what he asked, and take any new fact only from those sources. Write the new blurb at the top of the Engagement\'s page body under "Blurb, <YYYY-MM-DD> (edited: <his ask, short>)", keep the old one below, and update the FT Community row\'s Blurb (never People). Post it the same two-message way, header "Zoya ✨ blurb, edited: <guest>". Log it.\n',
         '0b. BLURBS: retired (decision 347, Akshay, 20 Oct: "kill this process"). Never post a blurb to this group and never rerun the blurb skill from here. Blurbs are drafted by the calendar routine and edited in each recording\'s own editing chat, linked under its "Blurb, <date>" section. Old blurb posts and their Activities stay as they are.\n'),
        ('Zoya group (messages handled and what each became, blurbs posted or edited, digest',
         'Zoya group (messages handled and what each became, digest'),
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
