"""Decision 394 (FAST/SLOW trial; spec docs/proposals/zoya-split.md v2.1, section 1): every routine that writes a Zoya step
writes it in the keyed short form "Zoya [<type> <origin> <raised ISO>]: <step>", so FAST and SLOW select their own actions
without reading prose. One ACTION KEYS paragraph each for the inbox, calendar and sweep; the inbox also raises reply steps
only for a substantive ask (spec: reply-owed). The WhatsApp routine is unchanged: its only Zoya step is the snooze segment,
which keeps its own form. Deploy in the same window as the split prompts (routines/zoya/build.py), never before: the live
single Zoya prompt doesn't read the keyed form.
On the live prompts (d-codex22 + fix as deployed 22 Oct; sweep d382 rev 7). Usage: python3 d394-keys.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
INBOX, CAL, SWEEP = "trig_0189eZvAD8x4357cfevgZ3No", "trig_01Voiz5YsK2SnVf2STF8PoSH", "trig_01MdfUFg2qrebDWgiHwncgnd"
# Rebased 26 Oct on the live prompts as read back that day (the anchors are unchanged; 22 Oct bases were 60,937, 55,992, 32,478)
BASE = {INBOX: (61957, "aed0215a8bdf6a26"), CAL: (54901, "543c3499473860ac"), SWEEP: (33824, "7af60faaa021fa64")}
KEYS = ("ACTION KEYS (decision 394, the FAST/SLOW trial). Every Zoya step you write in Next action, wherever this prompt "
        "says \"Zoya: <step>\", goes in the keyed short form \"Zoya [<type> <origin> <raised>]: <step>\". Type, by what the "
        "step does: reply (an answer owed to someone who wrote: a reply, acknowledgement, admin confirmation, a rebook after "
        "their cancel), decision (a step from Akshay's decision, Your call or approval: his decision mail, a precall invite, "
        "a slot ask, a decline, the commercials, an approved draft), hold (a holding reply), followup (a chase or routine "
        "step), nurture (nurture or revival) or team (an ask of Jaya, Sarika or Ranjita). Origin: \"msg-<Message-ID header "
        "without angle brackets>\" of the inbound mail that raised it; else \"call-<id of the Activity that recorded it, else "
        "this row's page id>\"; \"seq-<routine>-<step n>\" for a followup or nurture step. Raised: when the step arose, ISO "
        "with offset (2026-10-22T13:07+09:00). Snooze segments (\"Zoya: back to Akshay on ...\") keep their own form. The key "
        "is the step's identity: a step already on the row, keyed or not, is the same step and is never written twice; "
        "matching or removing a step by its wording matches it with or without the key, and you never rewrite another "
        "step's key.")
REPLY = (" Raise a reply step only for a substantive ask (a question, request or proposal), never for an auto-reply, "
         "out-of-office, bounce, a mail that only thanks or acknowledges, a loop-in or an incidental Cc. A holding reply "
         "(hold) never closes the reply or decision step for the same ask: that stays until the mail that answers it.")
TEAM_END = ("\"Fix:\" flags are data problems for you (decision 90): fix them from the thread and People, else list them in "
            "the report.\n")
EDITS = {
 INBOX: [(TEAM_END, TEAM_END + KEYS + REPLY + "\n")],
 CAL: [("never put text in front of \"Zoya: ...\".\n", "never put text in front of \"Zoya: ...\".\n" + KEYS + "\n")],
 SWEEP: [("Next action \"Zoya: <step>\".\n", "Next action \"Zoya: <step>\".\n" + KEYS + "\n")],
}
for tid, edits in EDITS.items():
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == BASE[tid], (tid, len(s.encode()), sha(s.encode()))
    dashes = s.count("—")
    for a, b in edits:
        assert s.count(a) == 1, (tid, a[:60], s.count(a))
        s = s.replace(a, b)
    b = s.encode()
    assert len(b) <= 65536 - 200 and s.count("—") == dashes, (tid, len(b))
    open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
    print(tid, len(b), sha(b))
