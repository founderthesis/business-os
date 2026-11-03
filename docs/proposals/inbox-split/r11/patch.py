"""Inbox actions r11b (decisions 446 and 448, Akshay, 3 Nov, Tab 13), on the live actions r10d-cleanup
(43,955 / 4ac5406d). Usage: python3 patch.py <live actions.txt> <out.txt>. Each edit is asserted exactly once."""
import sys, hashlib
src, out = sys.argv[1], sys.argv[2]
b = open(src, "rb").read()
assert hashlib.sha256(b).hexdigest().startswith("4ac5406d"), "not the live actions r10d-cleanup"
s = b.decode("utf-8")
EDITS = [
 # 446: client-show scheduling goes to Akshay first, not straight to the host.
 ('For un#, B2S and HBD the recording is with the host (Sri, Satish, Arjun), not Akshay: set Waiting on to the host and Next action "<host>: pick a slot for <guest> on your board (<the slots>)" when Host board is ticked on the row (the host boards routine copies them to the board), else "<host>: pick a slot for <guest> (<the slots>)". Never ask Akshay for a host show\'s recording slot (decision 114).',
  'For un#, B2S and HBD the recording is with the host (Sri, Satish, Arjun), but every scheduling turn goes to Akshay first (decision 446, Akshay, 3 Nov: "For client podcasts, best to ask me for next action first"; it replaces decision 114 here): their slots or windows, a "can\'t do", a reschedule, the host\'s pick. Add Akshay to Waiting on and put first in Next action one recommendation, "Akshay: <guest> (<show>) scheduling: <what came in>. Recommend: <one step: put the slots on <host>\'s board | confirm <slot> and create the invite | ask for new windows>, because <one line>. Write ok, not ok or a change in Your call. (<D Mon>)" (other segments kept; one already open on the row: update it, never a second). Until he answers, STEP 5 and 6e queue no Zoya reply on that thread but the holding reply (decision 390), and 6e bucket C adds no second Akshay ask. On his ok, the host step is "<host>: pick a slot for <guest> on your board (<the slots>)" when Host board is ticked on the row (the host boards routine copies them to the board), else "<host>: pick a slot for <guest> (<the slots>)"; any other step is Zoya\'s. A mail from Akshay on the thread with an instruction ("block the 17th as well") is his ok: Waiting on Zoya, "Zoya: <his step>".'),
 ('A recording on a host show stays the host\'s pick (above), Next date untouched.',
  'A recording on a host show goes to Akshay first (above, decision 446), Next date untouched.'),
 # 448: a reply on Akshay's own thread comes to him with one recommendation.
 ('- A guest, PR person or stakeholder wrote and the thread now waits on us:',
  '- A reply to a mail Akshay wrote himself (decision 448, Akshay, 3 Nov: "why did this not come into my queue?"): the message it answers (its In-Reply-To, else our side\'s last message on the thread) is from ad@thepodium.in and is his own, not a loop-in or a mail of his handing the thread to Zoya, the billing forward, an agent\'s send or a team member\'s mail; an auto-reply, out-of-office or bounce is no reply. Even a "will revert" or a mail with no ask: add Akshay to Waiting on and put first in Next action one recommendation, "Akshay: <who> replied on your <D Mon> mail: <what, a few words>. Recommend: <one step>, because <one line>. Write ok, not ok or a change in Your call. (<D Mon>)" (other segments kept; one already open for that thread: update it, never a second). A scheduling turn on a client show (STEP 3, decision 446) or new inbound on a closed row (decision 444) keeps that STEP 3 segment instead, never a second. This wins over the Zoya, acknowledgement and ball-in-their-court bullets below for that mail; Zoya gets only the holding reply (decision 390), and only when it asks something.\n- A guest, PR person or stakeholder wrote and the thread now waits on us:'),
 ('and that no earlier step already answered this run. Put each in exactly one bucket:',
  'and that no earlier step already answered this run. A reply to a mail Akshay wrote himself is in no bucket: it keeps STEP 5\'s decision 448 segment. Put each other one in exactly one bucket:'),
 # 448 beats 151's 'wins over every other bullet' on revenue rows (r11b, replay D4).
 ('This rule wins over every other bullet below.',
  'This rule wins over every other bullet below but decision 448\'s (a reply to his own mail still comes to him in that bullet\'s form).'),
]
for a, c in EDITS:
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, c)
assert "—" not in s
ob = s.encode("utf-8")
assert len(ob) <= 65536 - 200
open(out, "wb").write(ob)
print(len(ob), hashlib.sha256(ob).hexdigest()[:16])
