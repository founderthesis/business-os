"""Cleanup on d398.py (67e235b): accepted with two lines. Usage: python3 d398-fix.py <d398 out dir> <out dir>
d398.py gives calendar 57,489 / c80b63e6bcf2e6ee and Zoya 64,133 / b961623ed7462720 (on d-dbl22-fix).
1/ The "Zoya cancelled" Activity had no key, so a retried run logs it twice; it now carries Source ID "cancel:<event id>",
   looked up first, and an event already handled is skipped.
2/ Zoya replies in the run before the calendar's (:30 vs :35), and the calendar may decline to delete (two matches, unclear
   words, or an invite someone else organised). Zoya's reply says she is taking it off the calendar, not that it is gone.
Noted, no change: an invite organised by the guest side is never ours to delete; it stays for them to cancel."""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
ZOYA, CAL = "trig_01UPT8LDrBDL5JQqW91Awgbo", "trig_01Voiz5YsK2SnVf2STF8PoSH"
BASE = {CAL: (57489, "c80b63e6bcf2e6ee"), ZOYA: (64133, "b961623ed7462720")}
EDITS = {
 CAL: [("Log an Activity \"Zoya cancelled: <D Mon> <precall|recording> for <guest> at <who>'s request\", linked to the row.",
        "Log an Activity \"Zoya cancelled: <D Mon> <precall|recording> for <guest> at <who>'s request\", Source ID "
        "\"cancel:<event id>\", linked to the row; look that key up first and skip an event already handled.")],
 ZOYA: [("reply that it's cancelled and ask for a fresh slot:", "reply that you're taking it off the calendar and ask for a fresh slot:")],
}
for tid, edits in EDITS.items():
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == BASE[tid], tid
    dashes = s.count("—")
    for a, b in edits:
        assert s.count(a) == 1, (tid, a[:60])
        s = s.replace(a, b)
    b = s.encode()
    assert len(b) <= 65536 - 200 and s.count("—") == dashes, tid
    open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
    print(tid, len(b), sha(b))
