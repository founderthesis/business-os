"""The recipient read-back against Rules for Zoya's new "Reply all" line (Akshay, 27 Oct, tab 11 item 13; CTO note with c6f3ae8).
Usage: python3 docs/proposals/d-split26v.py (repo root, after d-split26u and c6f3ae8's decision 418 line), then build_one.py.
"Reply all": nobody outside the team on the message answered is dropped, "and a person who has left ... moves to the new contact
only when the mail says so". The read-back required everyone on the latest inbound with no such exception, so it would have
flagged a correct handover reply. Now it allows exactly that one drop. "Quote what you answer" governs the body, not recipients;
the read-back doesn't touch it."""
P = "routines/zoya/parts/sending.txt"
s = open(P, encoding="utf-8").read()
a = "less your own address, bounced addresses, Akshay's other addresses, Mamatha and, on un#, Sri, plus Akshay)"
b = ("less your own address, bounced addresses, Akshay's other addresses, Mamatha, on un#, Sri, and anyone the mail itself says "
     "has handed over to a new contact (the new contact is on it), plus Akshay)")
assert s.count(a) == 1, s.count(a)
open(P, "w", encoding="utf-8").write(s.replace(a, b))
print("d-split26v applied")
