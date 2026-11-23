#!/usr/bin/env python3
"""Offline fixtures for fix 5 (23 Nov): free feature wording approved, 30-day park.

Usage: python3 fixtures_fix5.py [<dir with the staged fix 5 pages>]
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def after_free_offer(days_since_offer, replied_since, show="FT", revival=False):
    """What Zoya does on an FT sponsored row after the free feature offer went."""
    if show != "FT":
        return "not used"
    if replied_since:
        return "handle their reply"
    if revival:
        return "nothing"              # revival rows are closed already; never parked
    return "Park proposals" if days_since_offer >= 30 else "wait (Zoya date = offer + 30)"


def cases():
    bad = 0
    for args, want in [((0, False), "wait (Zoya date = offer + 30)"),
                       ((29, False), "wait (Zoya date = offer + 30)"),
                       ((30, False), "Park proposals"),
                       ((45, True), "handle their reply"),
                       ((40, False, "FT", True), "nothing"),
                       ((40, False, "un#"), "not used")]:
        got = after_free_offer(*args)
        ok = got == want
        bad += not ok
        print(f"{'ok ' if ok else 'BAD'} after offer {args}: {got}")
    return bad


def text_checks(page_dir):
    bad = 0
    slow = open(os.path.join(HERE, "prompts", "zoya-slow-work.txt"), encoding="utf-8").read()
    for s in ["Zoya date the send date + 30 days", "reason \"free feature, no reply in 30 days\"",
              "the wording page's toggle word for word"]:
        if s not in slow:
            print("BAD SLOW lacks:", s); bad += 1
    for s in ["PROPOSED", "wording awaiting Akshay", "never a chase end under PARKED", "never the Park proposals"]:
        if s in slow:
            print("BAD SLOW still has:", s); bad += 1
    if page_dir:
        f = lambda n: open(os.path.join(page_dir, n + ".md"), encoding="utf-8").read()
        fu, w, fu8, cad = f("follow-ups"), f("wording"), f("fu-8-revival"), f("cadences")
        for t, s in [(w, "Free feature offer: silent sponsored lead (FT)"), (w, "Free feature check-in (7 days)"),
                     (w, "Akshay. interested?"), (w, "<b>Status:</b> approved (decision 661, Akshay, 23 Nov)."),
                     (fu, "the Saturday Park proposals and Akshay decides"), (cad, "no reply 30 days after it: Park proposals for you")]:
            if s not in t:
                print("BAD page lacks:", s); bad += 1
        if w.count("approved (decision 661, Akshay, 23 Nov).") != 3:
            print("BAD wording: want 3 approved toggles"); bad += 1
        if w.count("free, built from a 30-minute call with Akshay. ok to go ahead?") != 1:
            print("BAD wording: only the repeat-guest toggle (decision 642) keeps \"ok to go ahead?\""); bad += 1
        for t, s in [(w, "PROPOSED: Free feature"), (fu8, "PROPOSED"), (fu, "wording awaiting Akshay")]:
            if s in t:
                print("BAD page still has:", s); bad += 1
    print("text checks:", "clean" if not bad else f"{bad} failures")
    return bad


if __name__ == "__main__":
    sys.exit(1 if cases() + text_checks(sys.argv[1] if len(sys.argv) > 1 else None) else 0)
