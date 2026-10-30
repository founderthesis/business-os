"""Cleanup's fix to d-split26q (659c330). Usage: python3 docs/proposals/d-split26q-fix.py (repo root), then routines/zoya/build.py.
d-split26q gives FAST 38,233 / 3da29ae693347239, SLOW 65,297 / 0464082b0360545a.
Recovery's candidate list drops "any that plainly does something else (a holding reply, a loop-in, another row's ask)". For a
hold action the holding reply is the very mail that completes it: a FAST that crashed after sending one would find no candidate,
call the action due and send the holding reply again. Only a holding reply for another action is excluded now."""
p = "routines/zoya/parts/actions.txt"
s = open(p, encoding="utf-8").read()
a = "(a holding reply, a loop-in, another row's ask)"
b = "(another action's holding reply, a loop-in, another row's ask)"
assert s.count(a) == 1
open(p, "w", encoding="utf-8").write(s.replace(a, b))
print("d-split26q fix applied")
