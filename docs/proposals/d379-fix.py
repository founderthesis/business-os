"""Cleanup's fixes to decision 379 (d379.py at 78be855), applied to its output. Usage: python3 d379-fix.py <d379 out dir> <out dir>
Composed order: live, d377.py, d377-fix.py, d379.py (with d377-fix's bases), this. Inputs: inbox 57,732 / 686597781be65989,
Zoya 55,230 / fae1815edcc77d27, sweep 31,172 / cd6a824726bccb32.
1/ The no-revival mark is a Tag, "No revival", that nurture, revival and the sweep read; the "## Standing" line stays for people.
   PREREQUISITE: add the option "No revival" to Engagements Tags and set it on the HealthQuad row, read back, before deploy.
2/ A sponsored no never re-closes a row that went ahead: the trigger and the repair skip Booked, Recorded and Form filled rows,
   and the repair runs only when nothing on the thread came after that no (a guest who declined paid but booked organically
   stays booked)."""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
INBOX, ZOYA, SWEEP = "trig_0189eZvAD8x4357cfevgZ3No", "trig_01UPT8LDrBDL5JQqW91Awgbo", "trig_01MdfUFg2qrebDWgiHwncgnd"
BASE = {INBOX: (57732, "686597781be65989"), ZOYA: (55230, "fae1815edcc77d27"), SWEEP: (31172, "cd6a824726bccb32")}
M = "\"No revival: PR declined\""
EDITS = {
 INBOX: [
  ("on any row whose thread carries our sponsored offer, whatever its Status (decision 379: Precall requested, Booking or Decision pending too).",
   "on any row whose thread carries our sponsored offer, whatever its Status short of Booked (decision 379: Precall requested, Booking or Decision pending too; never a Booked, Recorded or Form filled row)."),
  ("add a dated line " + M[:-1] + " (decision 379, <D Mon>)\" to the row's \"## Standing\" section:",
   "add Tags \"No revival\" and a dated line " + M[:-1] + " (decision 379, <D Mon>)\" to the row's \"## Standing\" section:"),
  ("whose row is still open (any Status but They declined, We declined or Parked) goes through this again",
   "whose row is still open and short of Booked (not They declined, We declined, Parked, Booked, Recorded or Form filled), with nothing on the thread after that no, goes through this again"),
 ],
 ZOYA: [
  ("a row whose \"## Standing\" says " + M + " (decision 379),", "a row with Tags \"No revival\" (decision 379),"),
  ("or a row marked " + M + " (the no came", "or a row with Tags \"No revival\" (the no came"),
 ],
 SWEEP: [("a " + M + " line (decision 379)", "Tags \"No revival\" (decision 379)")],
}
for tid, edits in EDITS.items():
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == BASE[tid], tid
    dashes = s.count("—")
    for a, b in edits:
        assert s.count(a) == 1, (tid, a[:70], s.count(a))
        s = s.replace(a, b)
    b = s.encode()
    assert len(b) <= 65536 - 200 and s.count("—") == dashes, tid
    open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
    print(tid, len(b), sha(b))
