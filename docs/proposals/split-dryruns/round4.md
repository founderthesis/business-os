# Round 4 (27 Oct): every scenario plus the interactions

Two independent offline runs, A and B. Nothing was sent or written.

**Inputs:**
- Prompts: FAST 8164ff3dde5b2218 and SLOW 01495aef6aad16c0 (72aa104: d-split26o on Cleanup's d6a1209).
- Snapshot: 3537b3e5c7ca55de.
- Scenarios: round4/scenarios.json (73067b4c6217c776).

Outputs are in round4/. "Canon" is a fixed comparison block both runs filled in the same shape.

| Scenario | A | B | Canon fields that differ |
|---|---|---|---|
| C contact holds | PASS | PASS | none |
| D cap | PASS | PASS | mails, rows (A used a placeholder recipient; same 40 sent, 5 left, Partial) |
| G same minute, sponsored yes | PASS | PASS | none |
| H overlap | PASS | PASS | rows, run records (whether a run with nothing due waits on the lease) |
| E several asks | PASS | PASS | none |
| L1 same-second tie | PASS | PASS | none |
| L2 crashed holder | PASS | PASS | none |
| L3 wait/skip leaves work due | **FAIL** | **FAIL** | none: both find FAST can close a still-live SLOW as stale |
| L4 FAST still running at 10:50 | PASS | PASS | none |
| R1 thank-you (412) | PASS | **FAIL** | mails (B: does c(2)'s Episode retry hold the thank-you? "house copies" undefined) |
| R2 recording unclear (411) | **FAIL** | **FAIL** | rows: a release-date question still adds a second Akshay ask; Next date read from the recording date |
| R3 recipients | PASS | PASS | rows (no Status on booking) |
| I1 lock + crash recovery | PASS | PASS | lease holder wording |
| I2a lock + duplicate, FAST vs SLOW | PASS | PASS | none |
| I2b two FAST runs | **FAIL** | **FAIL** | none: the lease doesn't cover same-kind runs |
| I3 recovery + duplicate | **FAIL** | **FAIL** | rows, run records: the answered send is never logged; FAST's own crashed record stays Started |

## Status per defect

| Defect | Status |
|---|---|
| E: several asks in one inbound | **Fixed and tested** (PASS on both runs) |
| Read-back: sender in, our address out, Mamatha never | **Fixed and tested** (R3 PASS on both) |
| Same-second tie, crashed-holder expiry, waiting run leaves work due | **Fixed and tested** (L1, L2 and L4 PASS on both). This shows the rules are followed. It doesn't make them a lock |
| Cap ends Partial; windows from lease acquisition | **Fixed and tested** (D and L4) |
| L3: a live run can be closed as stale | **Blocked, architectural.** No prompt rule can make a run close on time; the CTO and Akshay are settling how Zoya's writes are serialised |
| I2b: two same-kind runs | **Blocked, architectural** (same) |
| I3: an answered send never logged; own crashed record left Started | **Fixed** in d-split26q (659c330). Test pending: round 4c is running |
| R1: Episode retry and the thank-you; "house copies" undefined | **Still failing** on run B. The fix is one line, but SLOW has 39 B of headroom (Cleanup's size gate wants 3,000), so it waits for the size work |
| R2: second Akshay ask from a release-date question; Next date from the recording date | **Still failing.** The fix waits for the size work, as above |
| No Status after a mailed sponsored yes | **Blocked**: a rule change for the CTO and Akshay |
| Payal's duplicate People rows | **Blocked**: a data merge needing Akshay's go-ahead |
