"""Decision 398 (Akshay, 22 Oct: "purely admin work... I should not need to waste time on it"): when the guest, their PR or
EA says in writing they can't make a booked call, the calendar run deletes that invite (attendees notified) and its own prep
and cooling-off entries, Zoya chases a fresh slot, and nothing goes on Akshay's list. Overrides the ask-first rule on
editing guest events for this one case (CLAUDE.md, Calendar rules section 1, Rules for Zoya). A no-show stays Akshay's
(decision 234). The inbox's own cancel of decision 165 is unchanged; when it got there first, the calendar run only clears
the entries.
Calendar on the live prompt (d-codex22-fix as deployed 22 Oct); Zoya on top of d-dbl22 (deploy the two together).
Usage: python3 d398.py <live dir> <d-dbl22 out dir> <out dir>"""
import sys, os, hashlib
live, dbl, out = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
ZOYA, CAL = "trig_01UPT8LDrBDL5JQqW91Awgbo", "trig_01Voiz5YsK2SnVf2STF8PoSH"
SRC = {ZOYA: (dbl, 63645, "1569e456e69e6c4f"), CAL: (live, 55992, "fba6e2cd186d0903")}
WRITTEN = ("- CANCELLED IN WRITING (decision 398, Akshay, 22 Oct: \"purely admin work\"). The guest, their PR or EA says in "
           "writing (a mail on the row's threads in ad@thepodium.in or Zoya's inbox, or the note on their declined invite) "
           "that they can't make a booked future precall or recording. Delete that one event yourself: delete_event on "
           "ad@thepodium.in, notificationLevel ALL, only the event for that guest on the date they name (the guest's name in "
           "the title or an attendee from the thread, organiser ad@thepodium.in). If two events could match, or the words are "
           "unclear, delete nothing: Claude note line and a report line. Then delete its own prep and cooling-off entries "
           "(the bos-key entries for that event). Already gone (the inbox cancelled it, decision 165): delete only the "
           "entries. Log an Activity \"Zoya cancelled: <D Mon> <precall|recording> for <guest> at <who>'s request\", linked to "
           "the row. On the row: clear Call type; a recording at Booked goes back to Booking; take any Akshay ask about this "
           "cancellation out of Next action (and Akshay out of Waiting on if nothing else of his is left). Nothing goes on "
           "his list. The next bullet then hands Zoya the fresh slot. A no-show is not this: it stays Akshay's (decision "
           "234).\n")
EDITS = {
 CAL: [
  ("and deleting a duplicate booking the booker asked us to cancel, in STEP 1b rule 1 (decision 322).",
   "deleting a duplicate booking the booker asked us to cancel, in STEP 1b rule 1 (decision 322); and deleting a booked "
   "call its guest side cancelled in writing, with its own prep and cooling-off entries (CANCELLED IN WRITING, decision "
   "398)."),
  ("whose call is gone (cancelled, or no invite carries its call) is never deleted.",
   "whose call is gone (cancelled, or no invite carries its call) is never deleted, except under CANCELLED IN WRITING."),
  ("- An event cancelled: clear Call type, leave Next date.", WRITTEN + "- An event cancelled: clear Call type, leave Next date."),
  ("(never edit or delete an invite with guests on it).",
   "(never edit or delete an invite with guests on it, unless the decline's note or the thread says in writing they can't "
   "make it: CANCELLED IN WRITING)."),
 ],
 ZOYA: [
  ("if it is still on the calendar, say you'll sort it and put \"Akshay: cancel the <date> invite for <guest>\" on his list.",
   "if it is still on the calendar, reply that it's cancelled and ask for a fresh slot: the calendar run deletes the invite "
   "(decision 398), and nothing goes on Akshay's list."),
  ("- Never edit, cancel or create a calendar event with guests on it.",
   "- Never edit, cancel or create a calendar event with guests on it (a call their side cancelled in writing is the "
   "calendar run's, decision 398)."),
 ],
}
for tid, edits in EDITS.items():
    d, n, h = SRC[tid]
    s = open(os.path.join(d, f"{tid}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == (n, h), (tid, len(s.encode()), sha(s.encode()))
    dashes = s.count("—")
    for a, b in edits:
        assert s.count(a) == 1, (tid, a[:60], s.count(a))
        s = s.replace(a, b)
    b = s.encode()
    assert len(b) <= 65536 - 200 and s.count("—") == dashes, (tid, len(b))
    open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
    print(tid, len(b), sha(b))
