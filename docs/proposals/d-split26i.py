"""Frozen replay H and D (26 Oct): two runs on the same snapshot differed only on whether a write that leaves Next
action alone (an owner-mail page-body line) recomputes Next date. One rule: a write that changes Next action sets Next
date to the earliest open segment date; any other write leaves Next date as it is. Usage: python3 d-split26i.py"""
import os
p = "routines/zoya/parts/actions.txt"
a = 'Next date is the earliest open segment date ("original due <YYYY-MM-DD>" counts; a snoozed or held-for-snooze one never does).'
b = ('A write that changes Next action sets Next date to the earliest open segment date ("original due <YYYY-MM-DD>" counts; a '
     'snoozed or held-for-snooze one never does); any other write leaves Next date as it is.')
s = open(p, encoding="utf-8").read()
assert s.count(a) == 1
open(p, "w", encoding="utf-8").write(s.replace(a, b))
print("edited actions.txt")
