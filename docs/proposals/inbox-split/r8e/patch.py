"""Capture r8e on Main's r8d, and actions r8e on live r7 (CTO, 2 Nov 13:20 JST, CTOA-03 expedite CX-20261102T1307).
Usage: python3 patch.py <r8d capture> <r7 actions> <out dir>. Each edit asserted once."""
import hashlib, sys
cap_src, act_src, out = sys.argv[1], sys.argv[2], sys.argv[3]

def load(p, h):
    s = open(p, encoding="utf-8").read()
    assert hashlib.sha256(s.encode()).hexdigest()[:8] == h, p
    return s

def R(s, a, b):
    assert s.count(a) == 1, (a[:70], s.count(a))
    return s.replace(a, b)

c = load(cap_src, "5ef8b937"); cd = c.count(chr(0x2014))
# 1. Today's known batch: LINK also takes rows created 2 Nov before 03:00Z (the 10:03 run's), passed over once tried.
c = R(c, "created since 2026-11-01T03:00Z, Captured before today, not an Email out",
      "created since 2026-11-01T03:00Z, Captured before today or created before 2026-11-02T03:00Z (body without a \"link:\" line), not an Email out")
# 2-3. LINK outcome line, repair hand-off to actions, internal mail, repeat pitch.
c = R(c, "found rows keep Status, Waiting on, Next action; unsure: say so.",
      "found rows keep Status, Waiting on, Next action and later decisions, except STEP 3's repeat-pitch bullet, applied in full; "
      "new People or Engagements only on verified identity. Then body line \"link: <run id> <linked to | internal | no fit>\": "
      "linked to an Engagement or Deal: add its id to your record's \"stamped:\" line (actions repairs it); only our team on it: "
      "People = those team members, \"internal\"; else \"no fit\", in the report. Unsure: say so.")
c = c.encode(); assert c.decode().count(chr(0x2014)) == cd and len(c) <= 65536

a = load(act_src, "c80b1cee"); ad = a.count(chr(0x2014))
# 4. Actions takes a LINK-repaired row again, for unperformed effects only.
a = R(a, "Skip, without a ledger line, any other and any whose body has \"actions: done\" or \"actions: stuck\".",
      "Skip, without a ledger line, any other and any whose body has \"actions: done\" or \"actions: stuck\", except a stamped row "
      "with a \"link:\" line after its last \"actions: done\" (REPAIR: capture linked it late): work it again for effects not yet "
      "performed only. First read its thread in ad@ and Zoya's inbox, its Engagement's newest Activities, Sent and Action keys; "
      "never resend what went, never undo a newer Your call, Status or decision; ledger \"<id>: repair: <steps> | nothing left\".")
a = a.encode(); assert a.decode().count(chr(0x2014)) == ad and len(a) <= 65536

for name, b in (("capture.txt", c), ("actions.txt", a)):
    open(f"{out}/{name}", "wb").write(b)
    print(name, len(b), hashlib.sha256(b).hexdigest()[:16])
