"""Cleanup's fix for round 4's R1 finding "house copies undefined" (3dfa2e4), on d-split26q-fix. Usage: python3
docs/proposals/d-split26q-fix2.py (repo root), then routines/zoya/build.py.
Neither Zoya prompt defines "house copies" (the sweep and calendar do: Zoya in Cc on every ad@ mail or draft, plus Chaandini on
Built to Share and Human by Design, never Mamatha; decisions 180, 305, 352). INTERNAL TASKS c(4) drafts only the Founder Thesis
thank-you in ad@, so its house copy is Zoya: it now says "you". Saves 13 B."""
p = "routines/zoya/parts/internal.txt"
s = open(p, encoding="utf-8").read()
a = "Cc the PR, every other Stakeholder and the house copies, no attachment"
b = "Cc the PR, every other Stakeholder and you, no attachment"
assert s.count(a) == 1
open(p, "w", encoding="utf-8").write(s.replace(a, b))
print("d-split26q fix 2 applied")
