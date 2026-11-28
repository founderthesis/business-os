#!/usr/bin/env python3
"""RECIPIENTS (decisions 229, 586, 592, 643, 646, 647) as code, for replay tests.

The prompts carry the rule in words (edits.py RECIPIENTS); this module encodes the
same rule so fixtures can be checked offline. Addresses here are placeholders.
Run: python3 recipients.py   (runs the fixtures; exit 1 on a failure)
"""

ZOYA = "zoya@example.test"
AD = "ad@example.test"


def required(kind, latest=None, people=None, show="FT", revenue=False,
             guest_facing_contact=None, new_mail_to=None):
    """Return (to, cc) as lower-case sets.

    kind: "reply" (thread with outsiders), "new" (no thread), "team" (team-only).
    latest: {"from": [...], "to": [...], "cc": [...]} of the thread's latest message.
    people: address -> {"team": bool, "bounced": bool, "dead": bool, "akshay_alt": bool,
                        "name": str, "role": str, "move": bool}
    """
    people = {k.lower(): v for k, v in (people or {}).items()}
    p = lambda a: people.get(a.lower(), {})

    def removed(a):
        a, r = a.lower(), p(a)
        return (a == ZOYA or r.get("bounced") or r.get("dead") or r.get("akshay_alt")
                or r.get("name") == "Mamatha")

    if kind == "team":
        addrs = set(a.lower() for a in (new_mail_to or []))
        assert all(p(a).get("team") for a in addrs), "team-only mail to a non-team address"
        addrs = {a for a in addrs if a != AD and not removed(a)}
        return addrs, set()

    if kind == "reply":
        start = [a.lower() for k in ("from", "to", "cc") for a in latest.get(k, [])]
    else:
        start = [a.lower() for a in (new_mail_to or [])]
    keep = [a for a in dict.fromkeys(start) if not removed(a)]

    adds = [AD]
    names = {"Chaandini": show in ("B2S", "HBD"), "Divir": show == "Pathfinders",
             "Ankita": show == "Pathfinders", "Jaya": revenue, "Sarika": revenue}
    for addr, r in people.items():
        if names.get(r.get("name")):
            adds.append(addr)
    if guest_facing_contact:
        adds.append(guest_facing_contact.lower())
    allr = list(dict.fromkeys(keep + [a.lower() for a in adds]))

    to = {a for a in allr if p(a).get("move")}
    if not to:  # fall back: their side who wrote last
        to = {a for a in (latest or {}).get("from", []) if a.lower() in allr and a.lower() != AD}
    to = {a.lower() for a in to if a.lower() != AD and not p(a).get("team")}
    cc = set(allr) - to
    return to, cc


def check(draft_to, draft_cc, to, cc):
    got = {a.lower() for a in draft_to} | {a.lower() for a in draft_cc}
    want = to | cc
    assert draft_to, "To is empty"
    assert AD not in {a.lower() for a in draft_to}, "ad@ in To"
    return got == want, sorted(want - got), sorted(got - want)


FIXTURES = []


def fixture(fn):
    FIXTURES.append(fn)
    return fn


@fixture
def f06_sri_stays_on_un():
    people = {"sri@x": {"name": "Sri"}, "guest@y": {"move": True}}
    latest = {"from": ["guest@y"], "to": [ZOYA], "cc": ["sri@x"]}
    to, cc = required("reply", latest, people, show="un#")
    assert to == {"guest@y"} and cc == {"sri@x", AD}, (to, cc)


@fixture
def f07_team_only_no_akshay():
    people = {"sarika@team": {"team": True, "name": "Sarika"}}
    to, cc = required("team", people=people, new_mail_to=["sarika@team"])
    assert to == {"sarika@team"} and cc == set(), (to, cc)


@fixture
def f08_bounced_and_dead_dropped():
    people = {"b@y": {"bounced": True}, "ravi@team": {"dead": True},
              "pr@z": {"move": True}, "mam@team": {"name": "Mamatha", "team": True}}
    latest = {"from": ["pr@z"], "to": [ZOYA, "b@y"], "cc": ["ravi@team", AD, "mam@team"]}
    to, cc = required("reply", latest, people)
    assert to == {"pr@z"} and cc == {AD}, (to, cc)


@fixture
def f08b_draft_missing_host_fails_check():
    people = {"satish@h": {"name": "Satish"}, "g@y": {"move": True},
              "ch@team": {"name": "Chaandini", "team": True}}
    latest = {"from": ["g@y"], "to": [ZOYA], "cc": ["satish@h"]}
    to, cc = required("reply", latest, people, show="B2S")
    ok, missing, extra = check(["g@y"], [AD, "ch@team"], to, cc)
    assert not ok and missing == ["satish@h"], (ok, missing, extra)


@fixture
def f08c_revenue_adds_jaya_sarika():
    people = {"j@team": {"name": "Jaya", "team": True}, "s@team": {"name": "Sarika", "team": True},
              "g@y": {"move": True}}
    latest = {"from": ["g@y"], "to": [ZOYA], "cc": []}
    to, cc = required("reply", latest, people, revenue=True)
    assert to == {"g@y"} and cc == {AD, "j@team", "s@team"}, (to, cc)


if __name__ == "__main__":
    import sys
    bad = 0
    for f in FIXTURES:
        try:
            f()
            print("pass", f.__name__)
        except AssertionError as e:
            bad += 1
            print("FAIL", f.__name__, e)
    sys.exit(1 if bad else 0)
