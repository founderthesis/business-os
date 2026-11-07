# Zoya lock tests (27 Oct, about 00:35 JST)

Harness: lock-test.sh. It runs the exact acquire and release commands in routines/zoya/parts/lock.txt as concurrent invocations.

**Origin used: a local bare repository.** It exercises git's own atomic ref update, the same compare-and-swap GitHub applied in lock-feasibility.md. This session may push only to its own branch, so it pushed no lock or test ref to GitHub. The same script runs from a routine with the repo attached, on a test ref (never zoya-lock): `lock-test.sh https://github.com/founderthesis/business-os refs/heads/zoya-lock-test`, after the runbook's setup step has made that ref "free". That run is for the CTO.

## A finding first: "+" turns the lease off

The feasibility protocol pushed `"+<new>:<ref>" --force-with-lease=<ref>:<expected>`. With the "+" (a forced refspec), git does not apply the lease. A push whose expected sha was stale went through as a "forced update". Probed on git 2.43 against a local bare repo:
- stale expected sha, with "+": accepted, ref overwritten;
- the same push without "+": `[rejected] (stale info)`.

The feasibility rejections ("cannot lock ref ... is at X but expected Y") were the server refusing a ref that moved between the advert and the update, while two pushes raced in the same instant. They were not the lease. With "+", a run that read "free" and pushed a moment after another run had acquired would have overwritten the holder. That means two holders.

**Fix (in lock.txt and the runbook):** no "+" and no --force, ever. Each lock commit's parent is the sha the run read. So a plain push lands only as a fast-forward from exactly that sha, and the lease is checked as well. T8 below is that case. It fails under the old form and passes now.

## Results: two runs, both 37 of 37

| Test | What it shows | Maps to |
|---|---|---|
| T1, 10 rounds | 5 concurrent acquires on a free lock: exactly one holds, every round; the winner releases | L1, G, I2b (two invocations racing) |
| T2 | While held, a manual start and a retry both skip | H, L3, L4 |
| T3 | A holder crashes without releasing: three later runs skip, with no expiry and no takeover; the ref still shows the crashed holder | L2, I1, I3 (a run dies holding the lock) |
| T4 | A release by a non-holder (wrong sha) is rejected and changes nothing | |
| T5 | The runbook's guarded release frees it; the next run acquires | recovery |
| T6 | A crashed holder that resumes after recovery can't release the new holder's lock | the no-fencing case, fail-closed |
| T7 | A release racing a new acquire leaves the lock free or held by one run, never two | G |
| T8 | A push on a stale "free" read is rejected after another run acquired | the "+" finding |

Raw output: lock-test-run1.txt and lock-test-run2.txt. Every push printed git's harmless "push negotiation failed; proceeding anyway" warning, as in the feasibility run.

## What this demonstrates, and what it doesn't

**Demonstrated:**
- One run at a time starts business work. A run only proceeds after its own push lands as a fast-forward from the "free" commit it read.
- Every other invocation ends at the lock with no business reads or writes.
- A crashed holder stops everything until the guarded manual release.

**Not demonstrated:**
- Fencing of a paused holder: Notion and MCP Emails check no token, hence fail-closed.
- Protection for anything without the repo attached.
- The GitHub run of this exact script; the feasibility run covered GitHub's own CAS.
