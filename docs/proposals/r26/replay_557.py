"""Replay for decision 557: reads the clause from the built inbox actions prompt and checks the template each case picks.
Usage: python3 replay_557.py docs/proposals/r26/actions.txt"""
import re, sys
s = open(sys.argv[1], encoding="utf-8").read()
m = re.search(r"pre-call -> by Eval verdict, decision 557: (.*?); alignment", s)
assert m, "clause not found"
rule = {}
default = None
for part in m.group(1).split(", "):
    names, tier = part.rsplit(" Tier ", 1)
    if names == "anything else or no eval":
        default = "Tier " + tier
    else:
        for n in names.split(" or "):
            rule[n] = "Tier " + tier
def pick(verdict, row_tier=None):
    # "No Tier:" applies only when no Tier is named on the row or in Your call
    return row_tier or rule.get(verdict, default)
cases = [
    ("Decline", None, "Tier 2"),            # Vishal Nigam @ WTF: Decline + "invite to precall"
    ("Sponsored track", None, "Tier 2"),
    (None, None, "Tier 2"),                 # no eval
    ("Book immediately", None, "Tier 1"),
    ("Strong consider", None, "Tier 1"),
    ("Pre-call needed", None, "Tier 1.5"),
    ("Evaluate after call", None, "Tier 1.5"),
    ("Decline", "Tier 1", "Tier 1"),        # a named Tier wins
]
for v, t, want in cases:
    got = pick(v, t)
    print("%-20s named=%-7s -> %-8s %s" % (v, t, got, "ok" if got == want else "FAIL want " + want))
    assert got == want
print("replay 557: all", len(cases), "cases pass")
