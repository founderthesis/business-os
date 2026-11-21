# Lock harness on GitHub, routine-side (27 Oct 2026)

Akshay, 27 Oct: "run the lock harness test now". This is the acceptance condition from decision 415: the routine-side harness, including T8, the stale-reader case. It replaces the superseded feasibility result at 3d16a28.

## Setup

- **Routine:** trig_0198DiGddneFcwahiUgg8QXx, "TEST lock harness on GitHub (delete after)", fired manually.
  - Run: session_01VP63PNEdmgJt1jENsuefNA (cse_01VP63PNEdmgJt1jENsuefNA), 2026-10-27 00:28:36Z.
  - The routine was disabled again right after it fired.
- **Harness:** docs/proposals/split-dryruns/lock-test.sh, pinned by blob b814cbb6, sha256 9ed2e179...4c32. The routine checked this hash before running. The script is the version from e63106e, which uses the same acquire and release commands as routines/zoya/parts/lock.txt.
- **Target:** refs/heads/zoya-lock-test on github.com/founderthesis/business-os. refs/heads/zoya-lock was not touched; it doesn't exist yet.
- **Setting the ref free:** a guarded fast-forward from 30068e1 ("routine A3") to 8a9c376 ("free: harness setup by CTO test routine"). It used no "+" and no --force, and the expected commit was the parent. The push exited 0: `30068e1..8a9c376`.

## Result

| Run | Start | End | Result |
|---|---|---|---|
| 1 | free: harness setup | free: released by T9-next 00:30:20Z | passed 40, failed 0 |
| 2 | free: released by T9-next 00:30:20Z | free: released by T9-next 00:31:48Z | passed 40, failed 0 |

There were no 403, auth or network errors. The final ref is bf57f85, "free: released by T9-next 2026-10-27T00:31:48Z".

What the tests covered:
- **T1:** one winner from 5 concurrent acquires, in each of 10 rounds.
- **T2 and T3:** while the lock is held, every later run skips, including a manual start, a retry and runs after a crash. Nothing expires and nothing takes over.
- **T4 and T6:** a release by a non-holder, or by a stale holder, is rejected.
- **T5:** the CTO's guarded release works.
- **T7:** a release racing an acquire leaves one holder or none.
- **T8:** a push based on a stale "free" read is rejected after another run has acquired.
- **T9:** a push that landed but reported failure is read back as held.

All of these held against GitHub's own ref update, from the routine's own tools. Each run's full verbatim PASS lines are in the run's transcript (tool results 00:30:22Z and 00:31:51Z).

## Scope

This proves the git operation is exclusive on GitHub. It does not stop a paused holder from writing to Notion or mail. That limit is why the design fails closed and recovery goes through the runbook (decision 415).
