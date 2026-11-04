"""Calendar sync 454b (454, then 462) (Akshay, 3 Nov, Tab 13 items 5 and 8), on the live calendar prompt (57,968 / f6d14019, read back
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
 # 454b, decision 462 (Akshay, 4 Nov): Zoya sends the day-before mail on FT, un# and Built to Share, on the guest thread, with the recording link.
 ('Otherwise use the toggle "Recording tomorrow: looking forward, prep note". On un#, Built to Share and Human by Design it is always a draft (decision 313). Founder Thesis (P2r, decision 235): send it from Zoya\'s inbox, Akshay in Cc, only if all hold:',
  'Otherwise use the toggle "Recording tomorrow: looking forward, prep note". Zoya sends it (decision 462, Akshay, 4 Nov, replacing decision 313\'s draft) on Founder Thesis, un# and Built to Share: from Zoya\'s inbox, on the guest\'s own thread (a reply on its latest message that someone outside the team sent or received, the way Zoya\'s THREADING says; no thread: a new mail), To the guest, Cc Via, every other Stakeholder and the house copies (Akshay; Chaandini on Built to Share), never the host unless they wrote on the thread, never Saurabh Garg or a team member who has left. Human by Design stays a draft in Akshay\'s account (decision 313) until Akshay names its recording link. Before any send: SHOW CHECK on a client show, and a LEAK CHECK (no eval, verdict, score, fit, tier, route or sponsored-only words, no revenue or funding figure their side hasn\'t made public, no description of their company; a note that fails goes to Akshay\'s list unsent). Send only if all hold:'),
 ('On FT the note is in Zoya\'s voice, the wording page\'s "Recording tomorrow: looking forward, prep note": filled as below (the prep note pasted the same way), {conversation} = "your conversation with Akshay", Akshay in the third person throughout, her sign-off;',
  'The note is in Zoya\'s voice, the wording page\'s "Recording tomorrow: looking forward, prep note" (on un# and Built to Share its "Recording tomorrow (client show)" toggle when there is one): filled as below (the prep note pasted the same way), {conversation} = "your conversation with Akshay" on Founder Thesis, else "your conversation with <host first name>", the host and Akshay in the third person throughout, her sign-off;'),
 ("Client shows: a draft in Akshay's account, new mail, To the guest,",
  "Human by Design: a draft in Akshay's account, new mail, To the guest,"),
 ('{call link} (the recording link; none on the row or the invite yet:',
  "{call link} (the recording link: Founder Thesis, the guest's Zencastr room, zencastr.app.link, from the row's Call link or the invite; un#, unhashed.co/studio; Built to Share, built2share.in/studio; Human by Design, the row's Call link; none yet:"),
 ('The client-show draft is signed Akshay (Akshay, 12 Oct),',
  'The Human by Design draft is signed Akshay (Akshay, 12 Oct),'),
]
for a, c in EDITS:
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, c)
assert "—" not in s
ob = s.encode("utf-8")
assert len(ob) <= 65536 - 200
open(out, "wb").write(ob)
print(len(ob), hashlib.sha256(ob).hexdigest()[:16])
