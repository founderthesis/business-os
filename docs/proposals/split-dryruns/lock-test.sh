#!/usr/bin/env bash
# Zoya lock tests: the exact acquire and release commands in routines/zoya/parts/lock.txt, run as concurrent invocations.
# Usage: lock-test.sh <origin> <ref>   e.g. lock-test.sh /tmp/x/lock.git refs/heads/zoya-lock-test
#   A local bare repo exercises git's own atomic ref update, the same compare-and-swap GitHub enforces server-side
#   (lock-feasibility.md). Against GitHub, run it from a routine with the repo attached, on a test ref, never zoya-lock.
# Each "run" is one invocation of acquire; a winner later releases, unless the test kills it first.
set -u
ORIGIN=$1; REF=$2
G="git -c user.name=zoya -c user.email=zoya-lock@localhost"
W=$(mktemp -d); cd "$W" && git init -q && git remote add origin "$ORIGIN"

acquire() {  # $1 run id; prints "HELD <sha>" or "SKIP <reason>"
  local id=$1 F M H out
  git fetch -q origin "$REF" 2>/dev/null || { echo "SKIP fetch-failed"; return; }
  F=$(git rev-parse FETCH_HEAD); M=$(git log -1 --format=%s FETCH_HEAD)
  case "$M" in free:*) ;; *) echo "SKIP lock-held-by:${M#held: }"; return;; esac
  H=$($G commit-tree "$F^{tree}" -p "$F" -m "held: $id $(date -u +%FT%TZ)")
  out=$(git push --porcelain origin "$H:$REF" --force-with-lease="$REF:$F" 2>&1); rc=$?
  [ "${FAKE_FAIL:-}" = 1 ] && rc=1   # T9: the push landed but the client saw an error
  if [ $rc -ne 0 ] || echo "$out" | grep -q rejected; then
    git fetch -q origin "$REF" 2>/dev/null && [ "$(git rev-parse FETCH_HEAD)" = "$H" ] && { echo "HELD $H"; return; }
    echo "SKIP lost-race"
  else echo "HELD $H"; fi
}
release() {  # $1 run id, $2 held sha; prints "RELEASED" or "REJECTED"
  local R out
  R=$($G commit-tree "$2^{tree}" -p "$2" -m "free: released by $1 $(date -u +%FT%TZ)")
  out=$(git push --porcelain origin "$R:$REF" --force-with-lease="$REF:$2" 2>&1); rc=$?
  if [ $rc -ne 0 ] || echo "$out" | grep -q rejected; then
    git fetch -q origin "$REF" 2>/dev/null && [ "$(git rev-parse FETCH_HEAD)" = "$R" ] && { echo "RELEASED"; return; }
    echo "REJECTED"
  else echo "RELEASED"; fi
}
state() { git fetch -q origin "$REF"; git log -1 --format=%s FETCH_HEAD; }
race() {  # $1 label, $2 n concurrent invocations; prints winners count
  local i; rm -f "$W"/r.*
  for i in $(seq 1 "$2"); do ( acquire "$1-$i" > "$W/r.$i" ) & done; wait
  cat "$W"/r.* | sort | uniq -c | sed "s/^/  $1: /"
  grep -l '^HELD' "$W"/r.* | wc -l
}
pass=0; fail=0; check() { if [ "$1" = "$2" ]; then echo "PASS $3"; pass=$((pass+1)); else echo "FAIL $3 (got $1, want $2)"; fail=$((fail+1)); fi; }

echo "start: $(state)"
# T1 (L1, I2b): concurrent invocations on a free lock, 10 rounds of 5: exactly one holds each round.
for r in $(seq 1 10); do
  n=$(race "T1r$r" 5 | tail -1); check "$n" 1 "T1 round $r: one winner of 5 concurrent acquires"
  h=$(grep -h '^HELD' "$W"/r.* | awk '{print $2}'); check "$(release "T1r$r" "$h")" RELEASED "T1 round $r: winner releases"
done
# T2 (H, L3, L4): while held, every later invocation skips, including a manual start and a retry.
a=$(acquire T2-holder); h=${a#HELD }
check "$(acquire T2-manual | cut -d: -f1)" "SKIP lock-held-by" "T2: a manual start skips while held"
check "$(acquire T2-retry | cut -d: -f1)" "SKIP lock-held-by" "T2: a retry skips while held"
check "$(release T2-holder "$h")" RELEASED "T2: holder releases"
# T3 (L2, I1, I3): a holder crashes (never releases): every later run skips, with no expiry, until the runbook's guarded release.
a=$(acquire T3-crashed); h=${a#HELD }
sleep 2
for k in 1 2 3; do check "$(acquire T3-later-$k | cut -d: -f1)" "SKIP lock-held-by" "T3: run $k after the crash skips (no expiry, no takeover)"; done
check "$(state | cut -c1-5)" "held:" "T3: the lock still shows held by the crashed run"
# T4: a release with the wrong sha (not the holder) is rejected and changes nothing.
check "$(release T4-impostor "$(git rev-parse FETCH_HEAD~1)")" REJECTED "T4: release by a non-holder is rejected"
check "$(state | cut -c1-5)" "held:" "T4: the lock is still held after the rejected release"
# T5: the runbook's guarded release (CTO, after evidence) frees it; then the next run acquires.
check "$(release CTO "$h")" RELEASED "T5: guarded release by the CTO with the held sha"
a=$(acquire T5-next); check "${a%% *}" HELD "T5: the next run acquires after recovery"
h2=${a#HELD }
# T6: a stale holder that resumes after recovery can't release the new holder's lock.
check "$(release T3-crashed "$h")" REJECTED "T6: the resumed old holder's release is rejected"
check "$(release T5-next "$h2")" RELEASED "T6: the current holder releases normally"
# T7 (G, L1 at release time): a release racing a new acquire: at most one holds afterwards, never two.
a=$(acquire T7-a); h=${a#HELD }
( release T7-a "$h" > "$W/rel" ) & ( acquire T7-b > "$W/acq" ) & wait
s=$(state); case "$s" in free:*|"held: T7-b"*) check ok ok "T7: release racing acquire leaves the lock free or held by one run ($s)";; *) check "$s" "free or T7-b" "T7";; esac
case "$s" in held:*) release T7-b "$(awk '{print $2}' "$W/acq")" >/dev/null;; esac
# T8 (the "+" finding): a run reads "free", another run acquires, then the first pushes on its stale read: must be rejected.
git fetch -q origin "$REF"; F0=$(git rev-parse FETCH_HEAD)
case "$(git log -1 --format=%s FETCH_HEAD)" in free:*) ;; *) echo "T8 setup: lock not free";; esac
a=$(acquire T8-winner); h=${a#HELD }
Hs=$($G commit-tree "$F0^{tree}" -p "$F0" -m "held: T8-stale $(date -u +%FT%TZ)")
out=$(git push --porcelain origin "$Hs:$REF" --force-with-lease="$REF:$F0" 2>&1); rc=$?
if [ $rc -ne 0 ] || echo "$out" | grep -q rejected; then r=REJECTED; else r=ACCEPTED; fi
check "$r" REJECTED "T8: a push on a stale free read is rejected after another run acquired"
check "$(state)" "$(git log -1 --format=%s "$h")" "T8: the winner still holds"
check "$(release T8-winner "$h")" RELEASED "T8: winner releases"
# T9 (Cleanup): a push that lands but reports failure. The run re-reads the ref, finds its own commit and holds; it then releases.
a=$(FAKE_FAIL=1 acquire T9-ambiguous); check "${a%% *}" HELD "T9: an ambiguous push that landed is read back as held"
check "$(release T9-ambiguous "${a#HELD }")" RELEASED "T9: that holder releases"
b=$(acquire T9-next); check "${b%% *}" HELD "T9: the next run acquires"; release T9-next "${b#HELD }" >/dev/null
echo "end: $(state)"
echo "passed $pass, failed $fail"
