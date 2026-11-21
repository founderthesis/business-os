"""Decision 407 (Akshay, 24 Oct: "when a guest proposes a slot, check it against my calendar and flag it asap before I
take it to host. Ideally send me an email from Zoya on the calendar conflict"). The inbox already writes every offered
slot to Scheduling and hands host-show slots to the host; this checks each slot first, with decision 406's margins.
A clash never reaches the host or the guest side: it leaves the slot out and queues a Zoya step to mail Akshay. Zoya
does that as an ordinary queue step (mail to the team is never held), so her prompt, at its ceiling, needs no change.
Inbox on d-msgid23's output (61,442 / f362e24b8767cd72). Usage: python3 d-slots407.py <d-msgid23 out dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
INBOX = "trig_0189eZvAD8x4357cfevgZ3No"
BASE = (61442, "f362e24b8767cd72")
OLD = "Never ask Akshay for a host show's recording slot (decision 114).\n"
NEW = ("Never ask Akshay for a host show's recording slot (decision 114). SLOT CHECK (decision 407, every show), before "
       "any slot step: check each offered slot on Akshay's calendar (ad@thepodium.in) with decision 406's margins: the slot "
       "and the 30 minutes before it, for a recording also the 30 after, free, prep, cooling-off and Out of office entries "
       "included. Clear slots go on as above. A clashing slot goes to no one: leave it out of the host or booking step (no "
       "clear slot left: no such step), Zoya added to Waiting on, and after \" | \" in Next action \"Zoya: mail Akshay "
       "calendar clash: <guest>, <slot JST> clashes with <event> (To Akshay only, subject Calendar clash: <guest> <D "
       "Mon>)\". End the Scheduling line with \"(checked: clear)\" or \"(checked: clash)\"; a checked line is never "
       "checked again.\n")
s = open(os.path.join(src, f"{INBOX}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == BASE, (len(s.encode()), sha(s.encode()))
dashes = s.count("—")
assert s.count(OLD) == 1, s.count(OLD)
s = s.replace(OLD, NEW)
b = s.encode()
assert len(b) <= 65536 - 200 and s.count("—") == dashes, len(b)
open(os.path.join(out, f"{INBOX}.txt"), "wb").write(b)
print(INBOX, len(b), sha(b))
