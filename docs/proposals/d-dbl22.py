"""Double sends of 21 and 22 Oct (CTO checked Akshay's inbox from 20 Oct; bug fixes under existing decisions, no new process).
1/ One PR, two guests: Bhoomika (Vicara) handles two guests on two rows and two threads, and the 16:38 run of 21 Oct sent her
   the same precall chase at 16:43 and 16:46. Before the first send, the run groups its send list by To address: one mail
   per person per run, carrying every guest's ask; the other rows are covered by that Message-ID.
2/ A reply where the team wrote last: MCP Emails' reply puts the last sender in To, so three "adding @Zoya" threads went
   to Akshay alone first and were resent (Chris George and Palak 11:16, Pallavi 10:37, 22 Oct). Such a reply is built as a
   draft with To and Cc set from the thread, then sent; never a reply whose only recipients are team.
Not a bug: Zoya's Sent shows each mail twice (MCP's filed copy and the SMTP copy, one Message-ID); never suppress a send
for it. Zoya only, on the live prompt (d-codex22 + fix as deployed 22 Oct). Usage: python3 d-dbl22.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
ZOYA = "trig_01UPT8LDrBDL5JQqW91Awgbo"
BASE = {ZOYA: (62409, "6d26eaafecc9c94e")}
ONE = ("- ONE MAIL PER PERSON PER RUN (CTO, 22 Oct: Bhoomika at Vicara got the same precall chase twice on 21 Oct, 16:43 and "
       "16:46, for two guests on two rows). Before the first send in a run, build the run's full send list and group it by "
       "To address. Where several rows would mail the same person, send one mail carrying every guest's ask, on the thread of "
       "the most urgent row (the order in ONE PERSON, ONE ASK), naming each guest. Its one Activity links every row it covers "
       "(MESSAGE IDENTITY), and each covered row moves on as if sent, with the Claude note line \"YYYY-MM-DD: covered by "
       "msgid:<Message-ID>\". A reply to a message the person sent stays on that message's own thread. Zoya's Sent folder "
       "shows each mail twice (MCP's filed copy and the SMTP copy, one Message-ID): that is one mail, never a reason to hold a "
       "send.\n")
REPLY = ("Reply on the existing thread (action reply, reply_all false, To and Cc set explicitly, on its latest message in your "
         "inbox).")
TEAMLAST = (" MCP Emails' reply puts the thread's last sender in To, so on any thread where the team wrote last (Akshay, you "
            "or anyone tagged Team), build the reply as a draft, set To and Cc from the thread (the people outside the team in "
            "To, Akshay in Cc), read the draft back, then send it (CTO, 22 Oct: three threads went to Akshay alone first). Never "
            "send a mail whose only recipients are team, unless it is meant for the team.")
EDITS = {
 ZOYA: [
  ("one mail covers both.\n", "one mail covers both.\n" + ONE),
  (REPLY, REPLY + TEAMLAST),
 ],
}
for tid, edits in EDITS.items():
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == BASE[tid], (tid, len(s.encode()), sha(s.encode()))
    dashes = s.count("—")
    for a, b in edits:
        assert s.count(a) == 1, (tid, a[:60], s.count(a))
        s = s.replace(a, b)
    b = s.encode()
    assert len(b) <= 65536 - 200 and s.count("—") == dashes, (tid, len(b))
    open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
    print(tid, len(b), sha(b))
