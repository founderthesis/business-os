"""Replay for decision 558 against the built r26 prompts (no model run; the decision each prompt's text gives).
Usage: python3 replay_558.py <zoya-one.txt> <zoya-slow-work.txt>"""
import sys
one = open(sys.argv[1], encoding="utf-8").read()
slow = open(sys.argv[2], encoding="utf-8").read()
i = one.find("ROOM ASK (decision 558")
assert i >= 0, "hourly has no ROOM ASK"
ask = one[i:i + 1200]
# The hourly's ask: every FT Booked recording with no room link anywhere and no "room asked" note, with no time window.
assert "every Founder Thesis Booked recording with no room link anywhere" in ask
assert "within 24 hours with no room link" not in one, "old 24-hour-only rule still present"
assert "one WhatsApp to Mamatha" in ask and "soonest first" in ask
def hourly(booked, has_link, asked, hours_to_recording, hours_since_ask=None, reminded=False, listed=False):
    if not booked or has_link:
        return "nothing"
    if not asked:
        return "ask Mamatha (WhatsApp, listed soonest first)"
    out = []
    if hours_since_ask is not None and hours_since_ask >= 24 and not reminded:
        out.append("one reminder")
    if hours_to_recording <= 48 and not listed:
        out.append("Akshay's list once")
    return " + ".join(out) or "wait"
# SLOW: the room ask is the hourly's; never selected or sent there.
assert "room ask to Mamatha (decision 558)" in slow and "never select or send them here" in slow
def slow_run(segment_present):
    return "nothing (the hourly's; reported only)" if segment_present else "nothing"
cases = [
    ("booked, no room, 6 days out", hourly(True, False, False, 144), "ask Mamatha (WhatsApp, listed soonest first)"),
    ("booked, room in invite", hourly(True, True, False, 144), "nothing"),
    ("asked 25h ago, 5 days out", hourly(True, False, True, 120, 25), "one reminder"),
    ("asked, reminded, 40h out", hourly(True, False, True, 40, 50, True), "Akshay's list once"),
    ("SLOW sees 'Zoya: ask Mamatha for the Zencastr link'", slow_run(True), "nothing (the hourly's; reported only)"),
]
for name, got, want in cases:
    print("%-55s -> %-45s %s" % (name, got, "ok" if got == want else "FAIL want " + want))
    assert got == want
print("replay 558: all", len(cases), "cases pass")
