"""Decision 379 (Akshay, 21 Oct, via the CTO): 1/ the inbox records a no to paying on any row whose thread carries our
sponsored offer, whatever its Status (Rahul Agarwal @ HealthQuad sat at Precall requested); 2/ the close note is Zoya's,
in her voice, from the wording page; 3/ a no from a PR or agency person marks the row so nurture and the decision 355
revival never pick it. Inbox, Zoya and sweep. Zoya and sweep apply on the live prompt or on the decision 377 build
(anchors don't overlap). Usage: python3 d379.py <base dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
INBOX, ZOYA, SWEEP = "trig_0189eZvAD8x4357cfevgZ3No", "trig_01UPT8LDrBDL5JQqW91Awgbo", "trig_01MdfUFg2qrebDWgiHwncgnd"
BASES = {INBOX: [(57267, "f48898f4ac396bf0")],
         ZOYA: [(52034, "d74d56bb06f20147"), (54989, "0a3ed4eb90f7b158")],
         SWEEP: [(30059, "60aa8ecdbe064c78"), (31253, "572dc9d9bd880de5")]}
MARK = "No revival: PR declined"
EDITS = {
 INBOX: [
  ("or offers an intro call in place of sponsoring, on a row at Sponsored offered (or Tier Sponsored). Record it first:",
   "or offers an intro call in place of sponsoring, on any row whose thread carries our sponsored offer, whatever its Status (decision 379: Precall requested, Booking or Decision pending too). Record it first:"),
  ("Next date untouched. Then the close note, once, is Zoya's:",
   "Next date untouched. If the no came from a PR or agency person (the sender or Via is not at the company's own domain and not its employee), add a dated line \"" + MARK + " (decision 379, <D Mon>)\" to the row's \"## Standing\" section: nurture and the quarterly revival never pick that row again. Then the close note, once, is Zoya's, in her voice from the wording page (decision 379):"),
  ("an inbound sponsored-no Activity of any age whose row is still Sponsored offered goes through this again",
   "an inbound sponsored-no Activity of any age whose row is still open (any Status but They declined, We declined or Parked) goes through this again"),
 ],
 ZOYA: [
  ("A decline gets Akshay's close note from ad@thepodium.in, once:",
   "A decline gets the sponsored close note from the wording page, from your inbox in your voice and signed as you (decision 379), once:"),
  ("Never a row we or Akshay declined or parked, a no-contact or held row,",
   "Never a row we or Akshay declined or parked, a row whose \"## Standing\" says \"" + MARK + "\" (decision 379), a no-contact or held row,"),
  ("never a plain \"not interested\" or anyone who asked us to stop. Start dates",
   "never a plain \"not interested\", anyone who asked us to stop, or a row marked \"" + MARK + "\" (the no came through a PR or agency; decision 379). Start dates"),
 ],
 SWEEP: [
  ("if it now has a decline, a no-contact request, a hold on this show, or Akshay",
   "if it now has a decline, a \"" + MARK + "\" line (decision 379), a no-contact request, a hold on this show, or Akshay"),
 ],
}
for tid, edits in EDITS.items():
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    base = (len(s.encode()), sha(s.encode()))
    assert base in BASES[tid], (tid, base)
    dashes = s.count("—")
    for a, b in edits:
        assert s.count(a) == 1, (tid, a[:60], s.count(a))
        s = s.replace(a, b)
    b = s.encode()
    assert len(b) <= 65536 - 200 and s.count("—") == dashes, (tid, len(b))
    open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
    print(tid, "on", base, "->", len(b), sha(b))
