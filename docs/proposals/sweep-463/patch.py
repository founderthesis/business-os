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
  "- One row per person interviewed, never one per episode (decision 232): for every Founder Thesis Engagement at Recorded or Form filled, and every Founder Thesis Episode whose Recording date is on or after 2026-09-01 and today or earlier (its Engagements and Guests; whatever the Engagement's Status: a row still at Booked after its recording counts; decisions 463, 465: on the list in the week of the recording), except an unusable recording (an Episode at Not releasing, at Hold, or a corrupted one: Magic Bus stays out), the Guest and every co-guest"),
 ("Flag (skip if Next action already says the same thing):\n",
  "Flag (skip if Next action already says the same thing):\n- No owner (decision 463, Akshay, 4 Nov): an open guest Engagement (Kind empty; Status not They declined, We declined, Parked, Unresponsive or Published) whose Waiting on is empty, except an Outbound row at New (decision 167) and a Cold outreach Deal: fix it from the row and its thread when the owner is plain (OWNERS: a booked recording with nothing else open is Guest or PR; an unanswered mail from their side is Zoya's), with a Claude note line \"YYYY-MM-DD: Waiting on was empty, set <who> (daily sweep)\"; not plain: a report line \"no owner: <name> (<Status>)\" under For Akshay, nothing changed. Count both in the report.\n"),
 ("Founder Thesis guests list rows added and links filled;",
  "Founder Thesis guests list rows added and links filled (and recorded FT guests still missing, by name); open Guest rows with no owner (fixed, flagged);"),
 # 463 as corrected (CTO, 4 Nov 15:14): recorded FT guests get an FT Community row; blurbs flagged, never written.
 ('At most 10 a run, oldest Recording date first. Report the rows created.\n\n',
  'At most 10 a run, oldest Recording date first. Report the rows created.\n\nSTEP 3k. FT COMMUNITY FOR RECORDED GUESTS (decision 463, Akshay, 4 Nov, Tab 15 item 1: the FT Community list, view "WhatsApp: to add"; calendar STEP 4b covers the last 14 days, this is the backstop). FT Community: collection://aefa65ce-8b38-40cb-8ef2-19d167adeea0. For every Founder Thesis Episode whose Recording date is on or after 2026-09-01 and today or earlier, except an unusable recording (Not releasing, Hold, or corrupted: Magic Bus stays out), each of its guests (Episode Guests, a People row) has one FT Community row, matched by its Person relation to that People row only (decision 465: never by name; a name-only hit with Person empty or another Person is a different row, listed in the report, never linked by you). None: create it with Name, Company, Person, Source FT guest, Type Founder or Investor, Membership To invite, Captured today. Found: set Membership To invite only if it is empty, never another change. While its Membership is To invite or Invited, the guest\'s Founder Thesis Engagement carries one "Akshay: invite <first name> to the FT Community" segment with Akshay in Waiting on (add it once if neither it nor "Akshay: WhatsApp addition pending" is there; other segments kept); Added: none (the WhatsApp routine\'s b2 clears it). Blurb empty and Membership To invite, Invited or Added (never Declined, Unresponsive or Left): the Episode has a transcript (Transcript file or Transcript link): a report line under For the blurb chat, "<name>: blurb due, transcript in (<Episode>)"; no transcript yet: a report line "<name>: blurb waits for the transcript". Never write Blurb, Blurb link or a "Blurb, <date>" section, and never run the founder-thesis-blurb skill (Akshay, 25 Oct: the Codex blurb chat writes blurbs). At most 15 creates a run, oldest recording first; one you can\'t settle goes in the report.\n\n'),
 ('A run at or after 14:00 JST is PART B, in this order: STEP 4b, 3i, 3h, 3g, 3b, 3d, 4, 5, 6c, 7b.',
  'A run at or after 14:00 JST is PART B, in this order: STEP 4b, 3i, 3h, 3g, 3k, 3b, 3d, 4, 5, 6c, 7b.'),
 ('open Guest rows with no owner (fixed, flagged);',
  'open Guest rows with no owner (fixed, flagged); FT Community rows created for recorded guests, and blurbs due or waiting (STEP 3k);'),
 # decision 456 (Cleanup should-fix 5): transcript requests name Mamatha.
 ('decision 376: transcripts to Ranjita,',
  'decision 376: transcripts to Mamatha (decision 456),'),
 ('Next action "Zoya: ask Ranjita for the transcript (decision 376)"',
  'Next action "Zoya: ask Mamatha for the transcript (decision 456)"'),
 # decision 465: the guests list matches by Person (LinkedIn), never by name prefix.
 ('Each such person with no row (match by name, then surname plus company):',
  'Each such person with no row (decision 465: match the guest list by the People row\'s LinkedIn, else exact full name plus company; never a name prefix or surname alone, and "Saket Saurabh @ Nexla" is not "Saket Saurav @ Refit Global"; case and spacing ignored, so "SREEPRIYA N S" is "Sreepriya NS"):'),
]
for a, c in EDITS:
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, c)
assert s.count(chr(0x2014)) == b.decode("utf-8").count(chr(0x2014)), "new em dash"
ob = s.encode("utf-8")
assert len(ob) <= 65536 - 200
open(out, "wb").write(ob)
print(len(ob), hashlib.sha256(ob).hexdigest()[:16])
