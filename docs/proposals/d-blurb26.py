"""CTOA-20261025-03 phase 1 (Build board card 40519a301a7f81c3b43ddda14107cd6d; Akshay, 25 Oct: Claude stops blurbs, the
Codex chat writes them; Claude keeps the records and the To invite queue). Removes every Claude blurb write: calendar
STEP 4b and 4b2 (replaced by a records-only STEP 4b), the blurb in the precall WhatsApp-invite check, STEP 4c's call into
4b; the WhatsApp routine's "blurb follows from the calendar run" promise; the inbox's pointer to the calendar's blurb.
Kept: identity and source capture, Episodes and transcripts, membership reconciliation, LinkedIn, To invite / Invited,
Akshay's community asks (their text unchanged, so the WhatsApp routine still clears them), his blurb notes in the
"Blurb, <date>" section (WhatsApp 0e). Same build: the calendar's HOURLY line becomes its six-run schedule (CTO, 26 Oct,
cron 35 7,10,13,16,19,22 JST); the audit windows 08-16, 16-22 and 22-08 still each get two runs, so the skip rule holds.
Usage: python3 d-blurb26.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
CAL, WA, INBOX = "trig_01Voiz5YsK2SnVf2STF8PoSH", "trig_01MnmJYorWrd61K7b5BCqXr1", "trig_0189eZvAD8x4357cfevgZ3No"
BASE = {CAL: (57578, "6ee76a95f744d5b9"), WA: (26005, "02c3c04c2e28591d"), INBOX: (61792, "e0bd396e5fa81afc")}
NO_BLURB = ("Akshay, 25 Oct: Claude writes no blurbs; the Codex blurb chat writes them")
EDITS = {
 CAL: [
  ("HOURLY (AR-20261019-6): you run every hour. Each run takes",
   "SIX RUNS A DAY (CTO, 26 Oct): 07:35, 10:35, 13:35, 16:35, 19:35 and 22:35 JST. Each run takes"),
  ("so the next hourly run does the audit again.", "so the next run does the audit again."),
  ("); if the page body has no \"Blurb, \" line yet, write the blurb as in STEP 4b from the precall and research (Blurb "
   "on the row, Membership stays Invited; Blurb link holds only the guest's editing chat, decision 359: never write it); "
   "the add itself", "); never write its Blurb or Blurb link (" + NO_BLURB + "); the add itself"),
  ("If the page body has no \"Blurb, <date>\" section dated on or after the recording (Akshay set Recorded himself), do "
   "STEP 4b first; STEP 4e", "Do STEP 4b's record check first; STEP 4e"),
 ],
 WA: [
  ("STEP 3d completes LinkedIn in this same run (do that row first); the calendar run writes the blurb from the full "
   "sources (decision 331).", "STEP 3d completes LinkedIn in this same run (do that row first); no routine writes the "
   "blurb (" + NO_BLURB + ")."),
  ("Reply \"Zoya ✨ noted: <name> is on your invite list, blurb follows from the calendar run\" (decision 310).",
   "Reply \"Zoya ✨ noted: <name> is on your invite list\" (decision 310)."),
  ("- Blurb and Blurb link are not yours: the calendar run writes the Blurb (decision 331) and Blurb link holds only the "
   "guest's editing chat (decision 359).",
   "- Blurb and Blurb link are not yours: the Codex blurb chat writes the Blurb (Akshay, 25 Oct) and Blurb link holds "
   "only the guest's editing chat (decision 359)."),
 ],
 INBOX: [
  ("leave Blurb link as it is (only the guest's editing chat goes there, decision 359), and leave Blurb to the calendar "
   "run, which writes it from the precall, recording and research (decision 331, page \"Blurb sources\");",
   "leave Blurb and Blurb link as they are (" + NO_BLURB + "; Blurb link holds only the guest's editing chat, decision "
   "359);"),
 ],
}
# Calendar STEP 4b and 4b2 are replaced whole: find them by their headings.
def replace_4b(s):
    a = s.index("STEP 4b. WHATSAPP BLURB")
    b = s.index("STEP 4f. TRANSCRIPT REQUESTS")
    new = ("STEP 4b. FT COMMUNITY RECORD (" + NO_BLURB + "; decisions 309, 359). For every Founder Thesis Engagement at "
           "Recorded or Form filled whose recording was in the last 14 days: make sure the guest has one FT Community row "
           "(by Person, else exact name plus company; none: create it with Name, Company, Person, Source FT guest, Type "
           "Founder or Investor, Membership To invite, Captured today) and that its LinkedIn is set (the People row's "
           "LinkedIn, else web search on name plus company with the headline confirmed, never a guess; write it to People "
           "too). Set Membership To invite only if it is empty; never change another Membership. Never write Blurb, Blurb "
           "link or a \"Blurb, <date>\" section, and never run the founder-thesis-blurb skill.\n\n")
    return s[:a] + new + s[b:]
for tid, edits in EDITS.items():
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == BASE[tid], (tid, len(s.encode()), sha(s.encode()))
    dashes = s.count("—")
    for a, b in edits:
        assert s.count(a) == 1, (tid, a[:60], s.count(a))
        s = s.replace(a, b)
    if tid == CAL:
        s = replace_4b(s)
        assert "STEP 4b2" not in s and "founder-thesis-blurb skill (no Slack" not in s
    b = s.encode()
    assert len(b) <= 65536 - 200 and s.count("—") == dashes, (tid, len(b))
    open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
    print(tid, len(b), sha(b))
