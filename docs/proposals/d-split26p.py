"""Akshay's decision, CTO 00:05 JST 27 Oct: crash recovery never guesses. Usage: python3 docs/proposals/d-split26p.py (repo
root, after d-split26o), then routines/zoya/build.py.
The original send is identified only by the Message-ID on its Activity, or by exactly one unlogged message from us to that
recipient on that thread since the action was raised. Anything else (two or more unlogged candidates, or one that can't be tied
to the action) is HELD for review: Akshay in Waiting on, a Next action naming the candidates, never a resend.
Limitation, stated in split-blocker.md: guaranteed duplicate prevention holds only inside the provider's 24-hour idempotency
window, unless a unique Sent match exists."""
P = "routines/zoya/parts/actions.txt"
s = open(P, encoding="utf-8").read()
a = ("A later acknowledgement, holding reply, loop-in or unrelated mail is not a match. A match: send nothing, log the Activity "
     "if it is missing, complete the action.")
b = ("A later acknowledgement, holding reply, loop-in or unrelated mail is not a match. A match must be unique: the Message-ID on "
     "the action's Activity, or exactly one message from us to that recipient (on that thread for a reply) since the action was "
     "raised whose Message-ID no Activity holds (two Sent copies with one Message-ID are one). A unique match: send nothing, log "
     "the Activity if it is missing, complete the action. Two or more such candidates, or one you can't tie to the action: HOLD "
     "it, never send: add Akshay to Waiting on and the segment \"Akshay: can't tell which mail completed <action, short>: "
     "<each candidate's Message-ID and send time>. Write which in Your call\", Claude note line \"YYYY-MM-DD: held for review "
     "(<key>)\", and name it in the report.")
assert s.count(a) == 1
open(P, "w", encoding="utf-8").write(s.replace(a, b))
print("d-split26p applied")
