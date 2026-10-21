"""Decision 374 (post-recording v2), parts 2 and 3, composed on Cut 1 + decision 373 (cut-1-build.py, then cut-1-d373.py).
Part 2: inbox and Zoya STEP 1 capture every outside address on a matched thread into People and Stakeholders; every
guest-facing composer takes its Cc as the union of Stakeholders, Via and every outside address on the threads and invites.
Part 3 (cloud side): on Founder Thesis the calendar creates the Episode "Awaiting transcript" when a recording ends, drops the
Drive audio check and no longer sets Recorded or drafts the thank-you; the Mac transcripts task (routines/mac/transcripts.md,
fed74f0) does both from the transcript. Client shows are unchanged. The thank-you wording is not touched.
Usage: python3 post-recording-v2-build.py <dir with cut-1-d373 outputs trig_<id>.txt> <out dir>"""
import hashlib, os, sys

def sha(s): return hashlib.sha256(s.encode()).hexdigest()[:16]

INBOX, ZOYA, CAL = "trig_0189eZvAD8x4357cfevgZ3No", "trig_01UPT8LDrBDL5JQqW91Awgbo", "trig_01Voiz5YsK2SnVf2STF8PoSH"
BASES = {INBOX: (56942, "afc7176f665f1fe7"), ZOYA: (49590, "3b7fe7ed689c06ae"), CAL: (52992, "d036faaf20ef74cb")}

ROLE = "not the team's (People tagged Team, ad@thepodium.in, zoya@myunnati.com) and not a role or no-reply inbox (info@, hello@, contact@, press@, team@, noreply and the like)"
CAPTURE = ("is found in People (Email, Other emails) or created (Name from the display name, else the address; Email; Organisation from the domain; "
           "Source Agent; Source ID \"gmail:<thread id>\"; Captured today) and linked: the guest's own address on the Guest row, anyone else in "
           "Stakeholders unless already Via; never remove a link.")

def whole_line(s, prefix):
    lines = [l for l in s.split("\n") if l.startswith(prefix)]
    assert len(lines) == 1, (prefix, len(lines))
    return lines[0]

def edits_for(tid, s):
    if tid == INBOX:
        return [(
            "Find the Engagement where the person is the Guest, a Stakeholder or Via, on the right Show. Then update it only where the mail is clear:\n",
            "Find the Engagement where the person is the Guest, a Stakeholder or Via, on the right Show. Then update it only where the mail is clear:\n"
            "THREAD PEOPLE (decision 374): on every thread matched to an Engagement, each address in From, To or Cc that is " + ROLE + " " + CAPTURE +
            " Claude note line \"YYYY-MM-DD: added <name> (<company>) from mail\" per new link; never write an address into a Summary, Next action or note.\n")]
    if tid == ZOYA:
        return [
            ("People, Engagement, Last activity on the row.",
             "People, Engagement, Last activity on the row. Then the thread's people (decision 374): each address in From, To or Cc that is " + ROLE + " " + CAPTURE),
            ("never ask PR to pass something on when a company-side address exists. ",
             "never ask PR to pass something on when a company-side address exists. Cc on guest-facing mail, release mails included (decision 374): "
             "the union of Stakeholders, Via and every outside address on the Engagement's threads and invites, minus the To, anyone who asked to be "
             "dropped and anyone tagged Email bounced; an address not yet in People is added first (as in STEP 1a). "),
        ]
    # calendar
    att = whole_line(s, "Attendee capture (decision 373")
    intro = whole_line(s, "For each Engagement with Call type Recording whose recording event ended between 30 days ago and now")
    a = whole_line(s, "a. Did it happen? Founder Thesis: look in the Drive")
    ty = whole_line(s, "   Until Zencastr transcripts reach Drive on their own")
    return [
        (att + "\n", att + "\nGUEST-FACING CC (decision 374): every guest-facing mail or draft you write (day-before note, reschedule, client thank-you) "
         "has Cc = the union of Stakeholders, Via and every outside address on the Engagement's mail threads and invites, minus the To, anyone who asked "
         "to be dropped, anyone tagged Email bounced, team members who have left and Saurabh Garg; plus the house copies. An address not yet in People "
         "is added first, as in Attendee capture.\n"),
        ("Cc the main PR contact (Via), every other Stakeholder on the Engagement and the house copies, never Saurabh Garg and never a team member who has left.",
         "Cc per GUEST-FACING CC."),
        ("Cc: the guest's PR, comms or EA from the threads (the PR paragraph greets the main one), Zoya, and the house copies.",
         "Cc: per GUEST-FACING CC (the PR paragraph greets the main one), Zoya included."),
        (intro, "For each Engagement with Call type Recording whose recording event ended between 30 days ago and now, was not cancelled, and whose "
         "Status is Booked. Skip if Claude note already has a line \"recorded <that date> (\" (a confirmed recording)."),
        (a, "a. Did it happen? Founder Thesis: the transcript decides (decision 374). Once the event has ended and nothing on the thread or "
         "calendar says it was cancelled or moved, do a2 at once (the Episode, Status \"Awaiting transcript\") and add the Claude note line "
         "\"YYYY-MM-DD: <D Mon> recording ended, Episode awaiting transcript\" once. Set nothing else: Status, Call type, Waiting on and Next action "
         "stay. The Mac transcripts task reads the transcript, sets Recorded, drafts the thank-you, and asks Akshay itself when Zencastr has no "
         "recording. You ask only when it can't: 24 hours after the slot, if the Claude note says \"not counted as recorded\" for that date, or 48 "
         "hours after it the Episode is still \"Awaiting transcript\" and Next action has no ask about this recording, add Akshay to Waiting on and "
         "put \"Akshay: <guest>'s <D Mon> recording: cancelled or no-show?\" first in Next action, once (decision 236); never chase the guest. "
         "Other shows (un#, Built to Share, Human by Design record on Riverside; there is no Drive check): once the event ended 2 or more hours ago "
         "and nothing on the thread or calendar says it was cancelled or moved, set Status Recorded, clear Call type, Claude note line \"YYYY-MM-DD: "
         "recorded <date> (calendar, client show)\", then a2 and STEP 4d. If the thread says it didn't happen, leave Status alone and write a Claude "
         "note line \"YYYY-MM-DD: <D Mon> recording: thread says it didn't happen\" instead (decision 321, not on his list)."),
        ("Create: title \"<Guest full name> @ <Company> - <Show>\"", "Create: title \"<Guest full name> @ <Company> - <Show>\""),
        (", Status Recorded, Recording date = the recording's date,",
         ", Status \"Awaiting transcript\" on Founder Thesis, else Recorded, Recording date = the recording's date,"),
        ("at Status Recorded (set by STEP 4 or by Akshay)", "at Status Recorded (set by the Mac transcripts task or by Akshay)"),
        (ty, "   The Mac transcripts task drafts the thank-you, transcript attached, once the transcript confirms the recording (decision 374). Never draft one here."),
        ("2. Community. If the guest's FT Community row is Added, nothing.",
         "2. Community. First make sure the guest has an FT Community row (decision 359): by Person, else exact name plus company; none: create it "
         "(Name, Company, Person, Source FT guest, Membership To invite, Captured today); one row per person, never a second, and never touch Blurb "
         "link. If it is Added, nothing."),
    ]

src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
for tid, (n, h) in BASES.items():
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s)) == (n, h), (tid, len(s.encode()), sha(s))
    for a, b in edits_for(tid, s):
        if a == b: continue
        assert s.count(a) == 1, (tid, a[:80], s.count(a))
        s = s.replace(a, b)
    assert len(s.encode()) <= 65536 - 200 and "—" not in s, tid
    assert "Zencastr audio in Drive" not in s or tid != CAL, "calendar still checks Drive audio"
    open(os.path.join(out, f"{tid}.txt"), "w", encoding="utf-8").write(s)
    print(tid, n, "->", len(s.encode()), sha(s), f"({len(s.encode()) - n:+d})")
