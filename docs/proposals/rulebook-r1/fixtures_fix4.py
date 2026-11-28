#!/usr/bin/env python3
"""Offline fixtures for fix 4 (decisions 660, 661, 662), as amended by fix 5 (wording approved).

1. Sponsored model: what Zoya does next on a Founder Thesis or un# sponsored row.
2. Enrichment model: the daily Reach budget and who is picked.
3. Text checks on the built prompts and, when given, the staged page text.

Usage: python3 fixtures_fix4.py [<dir with the staged fix 4 pages>]
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def sponsored_next(show, days_since_offer, interest, followups_sent, replied_after_last,
                   free_offered=False, wording_approved=True, pending=None, days_since_their_mail=0):
    """Next step on a sponsored row, per Rules for Zoya: follow-ups 5c (fix 4)."""
    if pending == "free feature":           # they said they'd get back on the free feature
        return "check-in" if days_since_their_mail >= 7 else "wait"
    if pending == "money":                  # decision 625 pause
        return "check-in" if days_since_their_mail >= 30 else "wait"
    limit = 5 if show == "FT" else 2
    if not interest:
        if days_since_offer < 7:
            return "wait"
        if show == "un#":
            return "Unresponsive"
        return "nothing" if free_offered else ("free feature offer" if wording_approved else "hold: wording awaiting Akshay")
    if followups_sent < limit:
        return f"follow-up {followups_sent + 1}"
    if replied_after_last:
        return "answer"
    if show == "un#":
        return "Unresponsive"
    return "nothing" if free_offered else ("free feature offer" if wording_approved else "hold: wording awaiting Akshay")


def sponsored_cases():
    cases = [
        (("FT", 3, False, 0, False), "wait"),
        (("FT", 7, False, 0, False), "free feature offer"),                 # was: Park proposals
        (("FT", 7, False, 0, False, False, False), "hold: wording awaiting Akshay"),
        (("FT", 9, False, 0, False, True), "nothing"),                      # offered once, no chase
        (("FT", 20, True, 2, False), "follow-up 3"),                        # was: stop after 2
        (("FT", 50, True, 4, False), "follow-up 5"),
        (("FT", 60, True, 5, False), "free feature offer"),                 # after the fifth
        (("un#", 30, True, 2, False), "Unresponsive"),                      # un# keeps 422's 2
        (("un#", 7, False, 0, False), "Unresponsive"),
    ]
    bad = 0
    for args, want in cases:
        got = sponsored_next(*args)
        ok = got == want
        bad += not ok
        print(f"{'ok ' if ok else 'BAD'} sponsored {args[:4]}: {got}")
    for pending, days, want in [("free feature", 6, "wait"), ("free feature", 7, "check-in"),
                                ("money", 7, "wait"), ("money", 30, "check-in")]:
        got = sponsored_next("FT", 40, True, 1, False, pending=pending, days_since_their_mail=days)
        ok = got == want
        bad += not ok
        print(f"{'ok ' if ok else 'BAD'} pause {pending} day {days}: {got}")
    return bad


def enrichment_budget(used_today, account_remaining):
    return max(0, min(35 - used_today, account_remaining))


def enrich_pick(person):
    if "Team" in person.get("tags", []) or "No enrichment" in person.get("tags", []):
        return False
    if all(person.get(f) for f in ("LinkedIn", "Role", "What they do")):
        return False
    return bool(person.get("ft_guest") or person.get("whatsapp_group") or person.get("community")
                or person.get("replied") or person.get("call"))


def enrichment_cases():
    bad = 0
    for used, rem, want in [(0, 30, 30), (0, 40, 35), (20, 30, 15), (35, 30, 0), (10, 0, 0)]:
        got = enrichment_budget(used, rem)
        ok = got == want
        bad += not ok
        print(f"{'ok ' if ok else 'BAD'} budget used {used}, account left {rem}: {got}")
    people = [
        ({"ft_guest": True, "LinkedIn": None}, True),
        ({"replied": True, "Role": None, "LinkedIn": "x"}, True),
        ({"LinkedIn": None}, False),                                   # cold outreach only, no reply
        ({"tags": ["Team"], "ft_guest": True}, False),
        ({"ft_guest": True, "LinkedIn": "x", "Role": "x", "What they do": "x"}, False),  # nothing blank
    ]
    for p, want in people:
        got = enrich_pick(p)
        ok = got == want
        bad += not ok
        print(f"{'ok ' if ok else 'BAD'} pick {p}: {got}")
    return bad


def text_checks(page_dir):
    bad = 0
    P = os.path.join(HERE, "prompts")
    slow = open(os.path.join(P, "zoya-slow-work.txt"), encoding="utf-8").read()
    up = open(os.path.join(P, "upkeep.txt"), encoding="utf-8").read()
    must = [
        (slow, "a Founder Thesis row gets FREE FEATURE and a un# row Status Unresponsive"),
        (slow, "FREE FEATURE (decisions 660, 661; FT only)"),
        (up, "no \"free feature offered\" Claude note line"),
        (slow, "A pending free feature (not money): one check-in 7 days after that mail instead"),
        (slow, "only FREE FEATURE's revival text"),
        (up, "STEP 7c. PEOPLE LINKEDIN ENRICHMENT (decisions 659, 662)"),
        (up, "get_account_quotas"),
        (up, "35 reads a day across every agent"),
        (up, "STOP AT ONCE on any LinkedIn verification"),
        (up, "WRITE only blank fields, never overwrite"),
        (up, "5, 6c, 7b, 7c, then STEP 7."),
    ]
    for t, s in must:
        if s not in t:
            print("BAD prompt lacks:", s); bad += 1
    if "a Founder Thesis row goes on the Park proposals" in slow:
        print("BAD SLOW still parks a silent FT sponsored row"); bad += 1
    if page_dir:
        f = lambda n: open(os.path.join(page_dir, n + ".md"), encoding="utf-8").read()
        fu, w, fu1, fu8, cad = f("follow-ups"), f("wording"), f("fu-1-sponsored"), f("fu-8-revival"), f("cadences")
        for t, s in [(fu, "up to 5 follow-ups, 7 days apart"), (fu, "| The free feature offer |"),
                     (fu1, "### Mail 5: who's been on"), (fu8, "Free feature offer: sponsored revival (FT)"),
                     (cad, "Up to 5 follow-ups, 7 days apart"),
                     (w, "Free feature offer: silent sponsored lead (FT)"),
                     (w, "Free feature offer: sponsored revival (FT)"),
                     (w, "Free feature check-in (7 days)")]:
            if s not in t:
                print("BAD page lacks:", s); bad += 1
        for t, s in [(fu, "weekly Park proposals for Akshay (decisions 618, 656)"), (fu, "at most 2 follow-ups, no nurture"),
                     (cad, "After the second with no reply: Park proposals for you"), (fu8, "podm.in/sponsored")]:
            if s in t:
                print("BAD page still has:", s); bad += 1
    print("text checks:", "clean" if not bad else f"{bad} failures")
    return bad


if __name__ == "__main__":
    n = sponsored_cases() + enrichment_cases() + text_checks(sys.argv[1] if len(sys.argv) > 1 else None)
    sys.exit(1 if n else 0)
