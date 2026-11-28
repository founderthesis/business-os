"""CTO, 22:45 JST: the rest of frozen round 3 run A's findings, after d-split26m. Usage: python3 docs/proposals/d-split26n.py
(repo root, after d-split26l-fix.py and d-split26m.py), then routines/zoya/build.py.
Already in d-split26m: E (the holding line rides in the answer mail), the same-minute re-read, FAST's carve-out for an unrelated
Akshay step, Next date with no dated segment, the read-back taking the inbound's sender and leaving out our own address.
1/ Crashed records: a record still Started at 60 minutes or more is closed as Failed by the run that finds it.
2/ FAST's wait outlasts the stale limit: when the holder's record turns 60 minutes old within 20 minutes of the run's start, the run
   waits until then instead of giving up first (L2 case 1: a 48-minute-old crashed record made FAST give up at 58 minutes).
3/ SLOW's and FAST's no-new-row windows count from when the run holds the lease, not from its start (L4: a long FAST ate SLOW's
   window). This also replaces the "(11:30, 17:30)" parenthetical that read wrong for an off-schedule start.
4/ 1c against WRITE PATH: "Set Waiting on Akshay, Next action ..." read as replacing the row's other owners and segments.
5/ A cap ends the run Partial, stated (it was only implied by "a cap is never a hold").
6/ The holding reply's key form: type hold, the same origin as the ask it acknowledges, its own raised time."""
def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:60], s.count(a))
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8").write(s)
P = "routines/zoya/parts/"
edit(P + "lease.txt", [
 ("one still at Started, begun under 60 minutes ago, holds the lease;",
  "one still at Started, begun under 60 minutes ago, holds the lease; one Started 60 minutes ago or more is stale: set it "
  "Failed, \"stale: no end written (closed by <your run id>)\", and it holds nothing;"),
 ("for up to WAIT minutes; still held, end Partial",
  "for up to WAIT minutes, or until the holder's record turns 60 minutes old if that comes within 20 minutes of your start; "
  "still held, end Partial"),
])
edit(P + "fast-order.txt", [(
 "A cap is never a hold: one you don't reach stays due as it is and goes first next run. Start no new row after 25 minutes.",
 "A cap is never a hold: one you don't reach stays due as it is and goes first next run, and the run ends Partial. Start no "
 "new row 25 minutes after you hold the lease.")])
edit(P + "slow-order.txt", [(
 "A cap is never a hold: one you don't reach stays due as it is (Next date unchanged) and goes first next run, ahead of its group's order.",
 "A cap is never a hold: one you don't reach stays due as it is (Next date unchanged) and goes first next run, ahead of its "
 "group's order, and the run ends Partial.")])
edit(P + "mail.txt", [(
 "Set Waiting on Akshay, Next action \"Ask Akshay: <who> asks <what>, in one line\".",
 "Add Akshay to Waiting on and the segment \"Ask Akshay: <who> asks <what>, in one line\" (WRITE PATH: other owners and "
 "segments stay).")])
edit(P + "actions.txt", [(
 "A Zoya segment carries its key in short form:",
 "A holding reply's key: type hold, the origin of the ask it acknowledges, raised when you send it. A Zoya segment carries its "
 "key in short form:")])
B = "routines/zoya/build.py"
edit(B, [(
 "(\"lease\", \"STOP\", \" Start no new row 40 minutes after your start (11:30, 17:30); the next run carries on.\"),",
 "(\"lease\", \"STOP\", \" Start no new row 40 minutes after you hold the lease (on schedule, 11:30 or 17:30); the next run carries on.\"),")])
print("d-split26n applied")
