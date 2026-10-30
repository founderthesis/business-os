"""Cleanup's fixes to decision 377 (d377.py at 66eaadb), applied to its output. Usage: python3 d377-fix.py <d377 out dir> <out dir>
d377.py gives calendar 54,224 / 2156c1eefc5edbcb, sweep 31,253 / 572dc9d9bd880de5, Zoya 54,989 / 0a3ed4eb90f7b158.
1/ Transcript rows are found by Source ID, never by a Name starting "Transcript: " or by Next action wording. PREREQUISITE for
   the deploy: give each hand-made 21 Oct "Transcript: " row a Source ID ("transcript:cal:<event id>" when the recording has a
   calendar event, else "transcript:episode:<Episode page id>"), read back, before these prompts go live.
2/ The calendar also skips a recording whose Episode already has a "transcript:episode:" row, so calendar and sweep never make two.
3/ Edit notes to Sarika: keyed by Source ID "editnotes:<Activity id>" and logged before the send, so a retry never sends twice."""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
CAL, ZOYA, SWEEP = "trig_01Voiz5YsK2SnVf2STF8PoSH", "trig_01UPT8LDrBDL5JQqW91Awgbo", "trig_01MdfUFg2qrebDWgiHwncgnd"
BASE = {CAL: (54224, "2156c1eefc5edbcb"), ZOYA: (54989, "0a3ed4eb90f7b158"), SWEEP: (31253, "572dc9d9bd880de5")}
EDITS = {
 CAL: [
  (", or if a Kind Task row with For engagement = that guest row and a Name starting \"Transcript: \" already names that recording's date (rows made by hand on 21 Oct have no Source ID).",
   ", or if any Engagement has Source ID \"transcript:episode:<that recording's Episode page id>\"."),
 ],
 SWEEP: [
  (", or if a Kind Task row with For engagement = the Episode's Engagement and a Name starting \"Transcript: \" names its Recording date.", "."),
 ],
 ZOYA: [
  ("a row with Task state Handed over, Waiting on Zoya and a Name starting \"Transcript: \".",
   "a row with Task state Handed over, Waiting on Zoya and Source ID starting \"transcript:\"."),
  ("; rows whose Next action already says the request went need none)", ")"),
  ("unless an Activity \"Zoya sent: WhatsApp to Sarika: edit notes for <guest>\" is dated after it. Send it this run per TEAM WHATSAPP",
   "unless an Activity with Source ID \"editnotes:<that Activity's id>\" exists. First log \"Zoya sent: WhatsApp to Sarika: edit notes for <guest>\" with Source ID \"editnotes:<that Activity's id>\" (a retry never sends twice), then send it this run per TEAM WHATSAPP"),
  (", log \"Zoya sent: WhatsApp to Sarika: edit notes for <guest>\", and take the step out.", ", and take the step out."),
 ],
}
for tid, edits in EDITS.items():
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == BASE[tid], tid
    dashes = s.count("\u2014")
    for a, b in edits:
        assert s.count(a) == 1, (tid, a[:60], s.count(a))
        s = s.replace(a, b)
    b = s.encode()
    assert len(b) <= 65536 - 200 and s.count("—") == dashes, tid
    open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
    print(tid, len(b), sha(b))
