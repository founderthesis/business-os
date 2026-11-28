"""Decisions 400, 403 and 406 (CTO, 23 Oct 18:30 JST): Zoya creates invites for times agreed in writing, adds the
guest side's people to a booked call, and checks Akshay's calendar before any time goes out. Found on Adrian
(Steakhouse, un#): she confirmed 29 Oct 22:00 JST, back to back with Hitarth's recording, then routed the invite to
Akshay because the hard rule still said agents never create events with guests. The key is "zoya-key:", not
"bos-key:", so the calendar run never treats her invite as one of its own blocks; it still adds prep and cooling-off
around it as for any recording. Zoya on d-sel23's output (64,959 / 6cd33a24fa8ab061).
To fit, twelve provenance notes shrink to their citation (no rule text changes).
Usage: python3 d-invites.py <d-sel23 out dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
ZOYA = "trig_01UPT8LDrBDL5JQqW91Awgbo"
BASE = (64959, "6cd33a24fa8ab061")
INVITES = ("INVITES (decisions 400, 403, 406; detail on Rules for Zoya and Calendar rules). Before any call or recording "
           "time goes to their side, read Akshay's calendar: the slot and the 30 minutes before it (a recording, also the "
           "30 after) must be free, prep, cooling-off and Out of office entries included. A clash: send nothing to them; "
           "Akshay's list, \"Akshay: <guest>'s <D Mon HH:MM JST> clashes with <event>\". Clear and agreed in writing "
           "(outside quiet hours unless Akshay named it): confirm on the thread and in the same run create the invite "
           "(organiser ad@thepodium.in, Meet or studio link, everyone on their side from the thread, JST and IST, "
           "\"zoya-key:<row id>:<type>:<date>\" in the description; one with that key exists: create none), set Next date, "
           "Call type and Call link, log \"Zoya created: invite\". Missing addresses or time zone: ask once on the thread. "
           "Their side asks to add someone to a booked call: add them as attendees, People and Stakeholders, confirm in "
           "one line; never move the time or remove anyone.\n")
EDITS = [
 ("Once Sri picks, confirm it on the thread (C8) and put \"Akshay: send the un# recording invite for <guest> on "
  "<slot>\" on his list (agents never create events with guests).",
  "Once Sri picks, confirm it on the thread (C8) and create the invite (INVITES)."),
 ("- Never edit, cancel or create a calendar event with guests on it (a call their side cancelled in writing is the "
  "calendar run's, decision 398).",
  "- Never move, cancel or edit a calendar event with guests on it beyond INVITES' adds (a call their side cancelled "
  "in writing is the calendar run's, decision 398)."),
 ("STEP 2. FOLLOW-UPS DUE\n", INVITES + "STEP 2. FOLLOW-UPS DUE\n"),
]
TRIMS = [  # provenance narratives shortened to their citation; no rule text changes
 ("(CTO, 22 Oct: Bhoomika at Vicara got the same precall chase twice on 21 Oct, 16:43 and 16:46, for two guests on two rows)", "(CTO, 22 Oct)"),
 ("(CTO, 22 Oct: Byufuel's and Escobar Bandra's decision mails sat queued while runs went Partial on LT chase rows)", "(CTO, 22 Oct)"),
 ("(Codex, 23 Oct: a run said nothing was due with 29 rows past their Next date Waiting on Guest or PR)", "(Codex, 23 Oct)"),
 ("(decision 325, Akshay, 18 Oct: \"My queue is a decision inbox, not a notification inbox\")", "(decision 325)"),
 ("(CTO, 21 Oct, the HealthQuad close note held by the limit)", "(CTO, 21 Oct)"),
 ("(CTO, 22 Oct: three threads went to Akshay alone first)", "(CTO, 22 Oct)"),
 ("(decision 382, Akshay, 21 Oct: Sri's windows are short)", "(decision 382)"),
 ("(decision 323, Akshay, 18 Oct: \"humans miss follow ups\")", "(decision 323)"),
 ("(decision 307, Akshay, 17 Oct: \"switch on for un#\")", "(decision 307)"),
 ("(Codex, 22 Oct: four sends were logged twice, once per mailbox)", "(Codex, 22 Oct)"),
 ("(Akshay, 16 Oct: inter-team communication goes on WhatsApp)", "(Akshay, 16 Oct)"),
 ("(Akshay, 16 Oct: Zoya handles sponsored on her own)", "(Akshay, 16 Oct)"),
]
s = open(os.path.join(src, f"{ZOYA}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == BASE, (len(s.encode()), sha(s.encode()))
dashes = s.count("—")
for a, b in EDITS + TRIMS:
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, b)
b = s.encode()
assert len(b) <= 65536 - 200 and s.count("\u2014") == dashes, len(b)
print(ZOYA, len(b), sha(b))
open(os.path.join(out, f"{ZOYA}.txt"), "wb").write(b)
