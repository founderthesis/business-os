"""AR-20261019-4 part 2: Built to Share reply owner and protected-status reply paths.

Applies to the deployed Salesblink sync prompt (9,276 B, sha256 6b94365084520118).
Usage: python3 ar20261019-4-replies-build.py <base> <out>
"""
import hashlib, sys

base, out = sys.argv[1], sys.argv[2]
s = open(base).read()
assert hashlib.sha256(s.encode()).hexdigest()[:16] == "6b94365084520118", "base is not the deployed prompt"

R = [
    # R1: bounces on paused B2S rows record only; replies go to the new paragraph
    ('Everything else applies as written: b) bounces, e) new rows (state as a) above), g), h) connect safety, and c) every reply in full.',
     'b) records a bounce (Claude note, and "Bounced <date>: find a new email when outreach restarts" after the On hold note) with no Next date and no Waiting on. Everything else applies as written: e) new rows (state as a) above), g), h) connect safety, and every reply as BUILT TO SHARE REPLIES says.'),
    # R2: reply owner follows the new paragraph, not c)'s Chaandini
    ('A reply is never cold: its Status, owner and dated next step follow c), its step replaces',
     'A reply is never cold: its Status, owners and dated next step follow BUILT TO SHARE REPLIES, its step replaces'),
    # R3: decision 328 replies go to Akshay's curation, never straight to an invite
    ('so a reply on such a row follows c) and asks Satish afresh, and',
     'so a reply on such a row goes to Akshay as BUILT TO SHARE REPLIES says, never straight to an invite, and'),
    # R4: the new paragraph, before the never-backward rule
    ('Human by Design: a) to h) as written.\nNever move a row backward:',
     'Human by Design: a) to h) as written.\n'
     'BUILT TO SHARE REPLIES (decision 323: replies and follow-ups are Zoya\'s, and Chaandini keeps cold outreach until their side replies; AR-20261019-4). On Built to Share rows read each reply as c) says, but the owners and steps are these. The reply sits on Chaandini\'s Salesblink thread, which Zoya is not on, so the first step is Chaandini\'s: Next action "Chaandini: add @Zoya on <first name>\'s reply of <date> | Zoya: <step>", Waiting on Chaandini and Zoya. Leave out Chaandini\'s part (and Chaandini) when the row already has a "Zoya sent" Activity on that thread. A reply is new only if its date is not already in the row\'s Claude note; an old one changes nothing.\n'
     '   - yes, interested, asks for details or a call: Status Interested, Next date today, <step> "answer <first name>; eval, then Akshay decides on Satish\'s board (decision 326)".\n'
     '   - later, after a date, not now: Status LT chase, Next date the date they give, else 90 days from today, <step> "revisit <first name>: <what they said>".\n'
     '   - they name another person or address to write to: Status Contacted, Next date today, <step> "write to <who> as <first name> asked".\n'
     '   - a clear no: They declined, as c). Left the company with nobody named, an out-of-office or an auto-reply: still cold, so note it in Claude note, keep the On hold note, no Next date and no Waiting on.\n'
     '   - a row already at a status in the never-move-backward list below: Status, Call type and every existing owner, ask and date stay. Add Chaandini and Zoya to Waiting on (as above), put "Chaandini: add @Zoya on <first name>\'s reply of <date> | Zoya: answer it: <gist>" in front of the Next action, keep the rest after " | ", and set Next date to today unless it is already earlier. At They declined, We declined or Parked a reply reopens nothing: add Akshay to Waiting on, put "Akshay: <first name> wrote again on <date> after <status>: <gist>" in front, Next date today.\n'
     '   - a decision 328 row (Next action starts "On hold: Satish\'s approval rescinded", or its Claude note names decision 328): the hold stays in front and nobody invites or follows up. Add Akshay to Waiting on, put "Akshay: <first name> replied <date> (<gist>); approval rescinded 18 Oct: put on Satish\'s board?" after the hold note, Next date today. A clear no is still They declined.\n'
     'Never move a row backward:'),
    # R5: LT chase protected from a) and d) on B2S; B2S replies on protected rows get their step
    ('except to append a Claude note when a new reply arrives.\na) MAILED',
     'except to append a Claude note when a new reply arrives (on Built to Share the reply also gets its step, as BUILT TO SHARE REPLIES says). On Built to Share LT chase is protected too: a) and d) never touch it, and c) still moves it forward.\na) MAILED'),
]
for a, b in R:
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
open(out, "w").write(s)
b = s.encode()
print(len(b), hashlib.sha256(b).hexdigest()[:16])
