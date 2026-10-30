"""Cleanup on d-dbl22.py (7af96d8): accepted with three lines. Usage: python3 d-dbl22-fix.py <d-dbl22 out dir> <out dir>
d-dbl22.py on live Zoya 62,409 / 6d26eaafecc9c94e gives 63,645 / 1569e456e69e6c4f.
Main's two questions: grouping by To only is right (merging mails with different To would mail one guest's PR about
another's thread); replies stay on their own threads, yes. Three gaps:
1/ The combined mail goes on one guest's thread with that row's Cc, so guest A's company comms would read guest B's ask.
   Its Cc is the team copies only.
2/ A person who gets a reply this run could still get a separate chase in the same run. They get one mail per run: the
   reply, and their chases wait for the next run.
3/ The team-wrote-last draft: a retry reuses that row's unsent draft after checking Sent, never a second draft.
The same three lines go into routines/zoya/parts/onemail.txt and sending.txt for the split."""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
ZOYA = "trig_01UPT8LDrBDL5JQqW91Awgbo"
EDITS = [
 ("on the thread of the most urgent row (the order in ONE PERSON, ONE ASK), naming each guest.",
  "on the thread of the most urgent row (the order in ONE PERSON, ONE ASK), naming each guest. Its Cc is the team copies "
  "SENDING requires and no one else: no other row's guest-side people, so one guest's company never reads another guest's ask."),
 ("A reply to a message the person sent stays on that message's own thread.",
  "A reply to a message the person sent stays on that message's own thread, and it is their one mail this run: their due "
  "chases wait for the next run (Claude note \"held: one mail per person per run\")."),
 ("read the draft back, then send it (CTO, 22 Oct:",
  "read the draft back, then send it; a retry checks Sent first and reuses that row's unsent draft, never a second draft (CTO, 22 Oct:"),
]
def apply(s):
    for a, b in EDITS:
        assert s.count(a) == 1, a[:60]
        s = s.replace(a, b)
    return s
if __name__ == "__main__":
    s = open(os.path.join(src, f"{ZOYA}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == (63645, "1569e456e69e6c4f")
    s = apply(s)
    b = s.encode()
    assert len(b) <= 65536 - 200
    open(os.path.join(out, f"{ZOYA}.txt"), "wb").write(b)
    print(ZOYA, len(b), sha(b))
