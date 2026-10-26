"""Cleanup's correction for SLOW's approved cadence, CRON_TZ=Asia/Tokyo 50 10,16 * * 1-5 (d-split26; CTO 26 Oct 17:15 JST).
Cleanup's c66415e and 1ff6953 assumed 8 8-22/2, which is not approved. At :50:
1/ SLOW's stop rule "after :30 past the hour you started" would stop a 10:50 run before its first row. It now names the times: 11:30 and 17:30.
2/ The lease's 45-minute stale limit would let FAST at 11:38 treat a live 10:50 SLOW (48 minutes old) as crashed. Now 60 minutes:
   a 10:50 SLOW waits for FAST at most to 11:15, starts no row after 11:30, so it's done well before 11:50. A crashed SLOW costs one FAST run (11:38 waits to 11:48, 58 minutes).
3/ SLOW's intro and deploy step 4 name the approved times.
Usage: python3 docs/proposals/d-split26h-fix2.py (repo root), then routines/zoya/build.py."""
def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:60], s.count(a))
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8").write(s)
edit("routines/zoya/build.py", [("Start no new row after :30 past the hour you started;", "Start no new row 40 minutes after your start (11:30, 17:30);")])
edit("routines/zoya/parts/lease.txt", [("begun under 45 minutes ago", "begun under 60 minutes ago")])
edit("routines/zoya/parts/intro-slow.txt", [("You run at :08 every 2 hours, 08:08 to 22:08 JST, weekdays;", "You run at 10:50 and 16:50 JST, weekdays;")])
edit("docs/proposals/zoya-split-build.md", [
 ("CRON_TZ=Asia/Tokyo 8 8-22/2 * * 1-5 (Cleanup c66415e)", "CRON_TZ=Asia/Tokyo 50 10,16 * * 1-5 (the approved cadence, d-split26)"),
 ("First, the minutes: FAST :38 to :03, SLOW :08 to :30. Second, the LEASE part (d-split26h): neither run writes a row while the other's run record is Started and under 45 minutes old.",
  "SLOW at :50 starts inside FAST's :38 run, so the LEASE part (d-split26h) is the protection: neither run writes a row while the other's run record is Started and under 60 minutes old. SLOW waits up to 25 minutes, FAST up to 10, and SLOW starts no row after 11:30 or 17:30."),
])
print("cadence correction applied")
