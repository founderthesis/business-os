"""WhatsApp to Business OS, decision 465.2 (Akshay, 4 Nov: "add to whatsapp list once added"), on the live prompt
(26,336 / ca8009c2, read back 4 Nov ~15:30 JST from trig_01MnmJYorWrd61K7b5BCqXr1). A third Added signal: Akshay's own word,
in an Engagement's Your call (or the Claude note line that keeps it once Your call is cleared) or his message to Zoya in the
Zoya group. Usage: python3 patch.py <live whatsapp.txt> <out.txt>. Each edit is asserted exactly once."""
import sys, hashlib
src, out = sys.argv[1], sys.argv[2]
b = open(src, "rb").read()
assert hashlib.sha256(b).hexdigest().startswith("ca8009c2"), "not the live WhatsApp prompt (26,336 / ca8009c2)"
s = b.decode("utf-8")
EDITS = [
 ("e. A message about a blurb (it quotes one,",
  "e1. A community add done (\"added sankalp to the FT group\", \"added to whatsapp group\"; decision 465): find the person as in e0; set their FT Community row Membership Added and Added on = the message date (create the row as e0 does if none, Membership Added), whatever it held before (To invite, Invited, Declined or Unresponsive; never a Left row: report it), then clear his asks as STEP 3 b2 does. Reply \"Zoya ✨ noted: <name> is in the FT Community\".\ne. A message about a blurb (it quotes one,"),
 ("(2) The person replying that they joined, or thanking him for adding them: set Membership Added and Added on today (create the row as above if none).",
  "(2) The person replying that they joined, or thanking him for adding them: set Membership Added and Added on today (create the row as above if none). (3) Akshay's own word (decision 465, Akshay, 4 Nov: \"add to whatsapp list once added\"): an Engagement whose Your call, or a Claude note line of the last 14 days that keeps one of his calls (\"Akshay's call: '...'\", \"Akshay on WhatsApp: '...'\"), says he added that person to the group (Sankalp Arora's \"added to whatsapp group, remove from my queue\"): set Membership Added and Added on = the date he wrote it (create the row as above if none), never on a Left row (report it). Every run, not only the first of the day."),
 ("b2. Clear Akshay's community asks: for every row set Added in a or b,",
  "b2. Clear Akshay's community asks: for every row set Added in a, b or 0a e1, and every row already Added that still has one,"),
]
for a, c in EDITS:
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, c)
assert s.count(chr(0x2014)) == b.decode("utf-8").count(chr(0x2014)), "new em dash"
ob = s.encode("utf-8")
assert len(ob) <= 65536 - 200
open(out, "wb").write(ob)
print(len(ob), hashlib.sha256(ob).hexdigest()[:16])
