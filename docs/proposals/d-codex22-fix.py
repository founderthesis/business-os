"""Cleanup on d-codex22.py (e62fa1c): accepted with two fixes. Usage: python3 d-codex22-fix.py <d-codex22 out dir> <calendar live dir> <out dir>
d-codex22.py on the live bases (d390 rev 3 + fix) gives Zoya 62,375 / 68825661fda2be52, inbox 60,937 / 40b7edec9145134e.
1/ The calendar sends from Zoya's inbox too (day-before note, double-booking check) and logs those Activities with no message
   key, so the inbox's msgid: lookup can't see them and logs the ad@ copy again (Michelle's day-before note, 21 Oct). The
   calendar gets the same MESSAGE IDENTITY rule and puts the msgid: key on every mail it sends. Live calendar 55,616 /
   48c2e04fc2ac846c.
2/ The LT cap's "last attempted" line replaces the row's earlier one, so hourly runs don't stack a line per run on every
   unreached row."""
import sys, os, hashlib
src, cal_src, out = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
INBOX, ZOYA, CAL = "trig_0189eZvAD8x4357cfevgZ3No", "trig_01UPT8LDrBDL5JQqW91Awgbo", "trig_01Voiz5YsK2SnVf2STF8PoSH"
BASE = {INBOX: (60937, "40b7edec9145134e"), ZOYA: (62375, "68825661fda2be52"), CAL: (55616, "48c2e04fc2ac846c")}
KEY = ("MESSAGE IDENTITY (Codex, 22 Oct: four sends were logged twice, once per mailbox). A mail's identity is its RFC "
       "Message-ID header, the same in both mailboxes. Every Activity for a mail you send carries Source ID \"msgid:<Message-ID "
       "without angle brackets>\" (the provider's own id only when the header can't be read), so the inbox finds it when the "
       "ad@thepodium.in copy arrives.\n")
EDITS = {
 ZOYA: [("with a Claude note line \"last attempted <YYYY-MM-DD HH:MM> JST\",",
         "with a Claude note line \"last attempted <YYYY-MM-DD HH:MM> JST\" (replacing the row's earlier one),")],
 INBOX: [],
 CAL: [("DAILY CAP: the number on the Notion page", KEY + "DAILY CAP: the number on the Notion page")],
}
for tid, edits in EDITS.items():
    s = open(os.path.join(cal_src if tid == CAL else src, f"{tid}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == BASE[tid], (tid, len(s.encode()), sha(s.encode()))
    dashes = s.count("—")
    for a, b in edits:
        assert s.count(a) == 1, (tid, a[:60], s.count(a))
        s = s.replace(a, b)
    b = s.encode()
    assert len(b) <= 65536 - 200 and s.count("—") == dashes, tid
    open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
    print(tid, len(b), sha(b))
