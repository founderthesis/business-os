"""Cleanup's fix to the one-writer LOCK (2636857). Usage: python3 docs/proposals/d-split26s-fix.py (repo root), then
routines/zoya/build_one.py <out> claude/business-os-structure-k3sqo5 <full sha of the commit carrying the SLOW work file>.
The SLOW work file doesn't change (LOCK is only in the one prompt), so its pin and hash stay valid.
1/ Ambiguous acquire: a push can land on GitHub while the client sees an error. LOCK read that as "another run won" and stopped,
   leaving the lock held by a run that ended: Zoya paused until the runbook. Now a failed push is checked by fetching again: the
   ref is your commit, you hold it; else another run won.
2/ A failed fetch read as "held by <blank>". It now ends Skipped "lock unreadable".
3/ A rejected release is checked the same way: the ref already reads your free commit, it went.
lock-test.sh mirrors the same commands (T9 added: a push that lands but reports failure)."""
def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:60], s.count(a))
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8").write(s)
edit("routines/zoya/parts/lock.txt", [
 ("2. git fetch origin refs/heads/zoya-lock; F=$(git rev-parse FETCH_HEAD); M=$(git log -1 --format=%s FETCH_HEAD).",
  "2. git fetch origin refs/heads/zoya-lock; F=$(git rev-parse FETCH_HEAD); M=$(git log -1 --format=%s FETCH_HEAD). The fetch fails: stop as in 3, \"lock unreadable\"."),
 ("Exit code not 0, or the output says rejected: another run won; stop as in 3 (\"lock taken by another run\"). Else you hold the lock; keep $H.",
  "Exit code not 0, or the output says rejected: fetch it again; it is now $H: you hold it; else another run won; stop as in 3 (\"lock taken by another run\"). Else you hold the lock; keep $H."),
 ("Rejected: add one line \"lock release rejected (<output>)\" to the run record and touch nothing else.",
  "Rejected: fetch it again; it is $R: it went; else add one line \"lock release rejected (<output>)\" to the run record and touch nothing else."),
])
print("d-split26s fix applied to lock.txt")
