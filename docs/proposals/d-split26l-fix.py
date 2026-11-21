"""Cleanup's fix to d-split26l (8e64140). Usage: python3 docs/proposals/d-split26l-fix.py (repo root), then routines/zoya/build.py.
d-split26l gives FAST 36,257 / 96c11beae7ec325b, SLOW 63,145 / a5b4ef40cfd85bb1.
Rules for Zoya (the master, section 2 Copies): "Mamatha is never in Cc, and nothing waits on her, on any show (decisions 260, 352)".
Its decision 413 entry is themes only; the recipient read-back has no decision behind "413".
1/ SENDING: "never add Mamatha (keep her only where she is on the latest inbound)" goes back to "never Mamatha". The Krsnaa 17:40
   mail was right to drop her.
2/ THREADING read-back: "everyone on the latest inbound" now excludes the people a rule keeps off: Mamatha, and Sri on un# (UN#: "Sri
   is never in Cc on routine mail"). The "decision 413" citation is dropped. The check itself stays: it catches Sreepriya's four
   dropped recipients."""
def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:60], s.count(a))
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8").write(s)
edit("routines/zoya/parts/sending.txt", [
 ("never add Mamatha (keep her only where she is on the latest inbound);", "never Mamatha;"),
 ("less bounced addresses and Akshay's other addresses, plus Akshay: decision 413)",
  "less bounced addresses, Akshay's other addresses, Mamatha and, on un#, Sri, plus Akshay)"),
])
print("d-split26l fix applied")
