#!/usr/bin/env python3
"""Offline fixtures for decision 637 date ownership (fix 1, 23 Nov).

Two parts, both must pass:
1. A row model of the five SLOW outcomes as the built prompt and Rules for Zoya:
   follow-ups now state them. Each keeps the person's Next date intact and writes
   Zoya date (or, for a cap, nothing).
2. Text checks on the built prompts (and, when given, the staged page text): no
   Zoya-step write of Next date is left, and each outcome's Zoya date wording is there.

Usage: python3 fixtures_637.py [<dir with the staged follow-ups.md>]
"""
import datetime as dt, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
D = dt.date


def outcome(row, kind, today, nxt=None, interval=None, first_ok=None):
    """Apply one SLOW outcome to a row dict, per SLOW work AFTER SEND and follow-ups 5a."""
    r = dict(row)
    if kind == "ordinary":      # step n sent: Zoya date = next step's due date
        r["chase_step"] += 1
        r["zoya_date"] = nxt
    elif kind == "nurture":     # nurture n sent: Zoya date = send date + interval for n
        r["chase_step"] = 0
        r["zoya_date"] = today + dt.timedelta(days=interval)
    elif kind == "deferral":    # a hold: segment date and Zoya date to the first allowed day
        r["zoya_date"] = first_ok
    elif kind == "failed":      # a failed send: only Zoya date moves
        r["zoya_date"] = nxt
    elif kind == "cap":         # a cap moves nothing
        pass
    return r


def model():
    today = D(2026, 11, 23)
    base = {"next_date": D(2026, 11, 27), "zoya_date": today, "chase_step": 2}  # 27 Nov: Akshay's precall
    cases = [
        ("ordinary send", outcome(base, "ordinary", today, nxt=D(2026, 12, 3)), D(2026, 12, 3)),
        ("nurture send", outcome(base, "nurture", today, interval=60), today + dt.timedelta(days=60)),
        ("deferral", outcome(base, "deferral", today, first_ok=D(2026, 11, 30)), D(2026, 11, 30)),
        ("failed send", outcome(base, "failed", today, nxt=D(2026, 11, 24)), D(2026, 11, 24)),
        ("cap", outcome(base, "cap", today), today),
    ]
    bad = 0
    for name, r, want_zoya in cases:
        ok = r["next_date"] == base["next_date"] and r["zoya_date"] == want_zoya
        bad += not ok
        print(f"{'ok ' if ok else 'BAD'} {name}: Next date {r['next_date']} (kept), Zoya date {r['zoya_date']}")
    return bad


FORBIDDEN_SLOW = [
    "Next date = the earliest of the next step's due date",
    "Next date = this send's date plus the NURTURE interval",
    "and Next date; a failed send moves only Next date",
    "moves its segment's date and Next date",
    "moves Next date 7 days on",
    "Chase step 0, Next date 30 days after",
    "Every hold writes Next date",
    "Sponsored offered whose Next date is today",
    "LT chase with Next date today or earlier",
    "stays due (Next date unchanged)",
    "set Next date 2 working days on",
]
REQUIRED_SLOW = [
    "Zoya date = the earliest of the next step's due date",            # ordinary
    "Zoya date = this send's date plus the NURTURE interval",          # nurture
    "moves its segment's date and Zoya date to the first day it may go",  # deferral
    "a failed send moves only Zoya date",                               # failed send
    "a cap moves nothing",                                              # cap
    "none of these ever moves Next date",
]
FORBIDDEN_PAGE = ["Next date = the next contact", "governs instead", "changes only Next date",
                  "Next date the next step's date", "Next date the send date", "moves only Next date",
                  "recheck Next date", "set Next date 3 months"]


def text_checks(page_dir):
    bad = 0
    slow = open(os.path.join(HERE, "prompts", "zoya-slow-work.txt"), encoding="utf-8").read()
    fast = open(os.path.join(HERE, "prompts", "zoya-fast.txt"), encoding="utf-8").read()
    for s in FORBIDDEN_SLOW:
        if s in slow:
            print("BAD SLOW still has:", s); bad += 1
    for s in REQUIRED_SLOW:
        if s not in slow:
            print("BAD SLOW lacks:", s); bad += 1
    if "selects by Status and Next date" in fast + slow:
        print("BAD keying text still selects by Next date"); bad += 1
    if page_dir:
        page = open(os.path.join(page_dir, "follow-ups.md"), encoding="utf-8").read()
        for s in FORBIDDEN_PAGE:
            if s in page:
                print("BAD page still has:", s); bad += 1
        if "Zoya date = the next contact" not in page:
            print("BAD page lacks the Zoya date row shape"); bad += 1
    print("text checks:", "clean" if not bad else f"{bad} failures")
    return bad


if __name__ == "__main__":
    n = model() + text_checks(sys.argv[1] if len(sys.argv) > 1 else None)
    sys.exit(1 if n else 0)
