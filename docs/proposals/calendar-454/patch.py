"""Calendar sync 454 (Akshay, 3 Nov, Tab 13 items 5 and 8), on the live calendar prompt (57,968 / f6d14019, read back
4 Nov ~01:30 JST from trig_01Voiz5YsK2SnVf2STF8PoSH). Usage: python3 patch.py <live calendar.txt> <out.txt>.
1/ decision 454: a prep event's description is compared line by line with the row's links, and the Dossier and Prep note
   lines go at the top; 2/ decision 453: the day-before note never waits on the recording link;
3/ decision 445 (r12b D8): zencastr.app.link counts as a Zencastr link everywhere (STEP 1 classification and Call link, audit rule 4, STEP 4e), and rule 4 leaves the no-link ask to Zoya."""
import sys, hashlib
src, out = sys.argv[1], sys.argv[2]
b = open(src, "rb").read()
assert hashlib.sha256(b).hexdigest().startswith("f6d14019"), "not the live calendar prompt (57,968 / f6d14019)"
s = b.decode("utf-8")
EDITS = [
 ("- One exists but the Engagement's Eval, Dossier, Prep note or LinkedIn link is new or has changed since (the dossiers routine rebuilds dossiers, decision 127): update the description only.",
  "- One exists but its description lacks a line for an Eval, Dossier, Prep note or LinkedIn link the Engagement now has, or shows a different one (compare the lines with the row every run, never a memory of an earlier run; the dossiers routine rebuilds dossiers, decision 127): update the description only, with the \"Dossier:\" and \"Prep note:\" lines first, at the top (decision 454, Akshay, 3 Nov: the prep event carries the dossier), notificationLevel none; it is private with no guests, so this is an add, never a move."),
 ("Fill {guest first name}, {show name}, {call link} (the recording link),",
  "Fill {guest first name}, {show name}, {call link} (the recording link; none on the row or the invite yet: drop the sentence that carries it and send or draft the note anyway, never hold it for the link: decision 453, the link goes in Zoya's recording-link mail, decision 445),"),
 ("4. Studio link: a recording 14 days or less away whose invite has no zencastr.com, riverside.fm or studio link.",
  "4. Studio link: a recording 14 days or less away whose invite has no zencastr.com, zencastr.app.link, riverside.fm or studio link."),
 ("If there is no link anywhere: \"Akshay: no Zencastr link yet for <guest>, recording <D Mon>\".",
  "If there is no link anywhere: a Claude note line only, \"no recording link yet (Zoya's STEP 0r asks Mamatha, and Akshay within 24 hours, decision 445)\", once; never an Akshay ask from here."),
  ("or the description or location holds a zencastr.com or riverside.fm link.",
  "or the description or location holds a zencastr.com, zencastr.app.link or riverside.fm link."),
 ("Call link: the zencastr.com or riverside.fm URL from the description or location for a recording,",
  "Call link: the zencastr.com, zencastr.app.link or riverside.fm URL from the description or location for a recording,"),
 ("or the event holds a zencastr.com, riverside.fm, built2share.in/studio or unhashed.co/studio link;",
  "or the event holds a zencastr.com, zencastr.app.link, riverside.fm, built2share.in/studio or unhashed.co/studio link;"),
]
for a, c in EDITS:
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, c)
assert "—" not in s
ob = s.encode("utf-8")
assert len(ob) <= 65536 - 200
open(out, "wb").write(ob)
print(len(ob), hashlib.sha256(ob).hexdigest()[:16])
