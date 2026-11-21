# Cleanup verdict: Tidy Next action round 2 (decision 438), 1 Nov

**Not accepted yet.** Round 3 needs two blocking fixes and three small ones. The builds are sound, and Z2 and the identity cases pass. The replay is in `replayNA2.json`.

## Builds (all rebuilt, byte-identical)

| File | Bytes / sha256 |
|---|---|
| zoya-one (FAST, pin arg `refs/heads/zoya-slow-pin`) | 43,565 / e04512accf236171 |
| SLOW at 39a5cce | 64,714 / 9403ac13d1527139 |
| inbox on msgid rev 2 | 65,306 / dcd1c44215676619 |
| inbox on Cleanup's msgid rev (the one to deploy) | 65,300 / 430ceefdda112a3f |
| calendar | 58,379 / 60535446d9b0d650 |
| sweep | 36,093 / 642eb4bd576c1d93 |
| host boards | 8,885 / 8a3fd4b5a3bb6b77 |

- Every diff holds only the intended edits.
- Em-dash counts are unchanged, and every file is under 65,336.
- Host boards' live input isn't in the repo. Taking out the rule line gives exactly 5819ccf7528ca16f.

## Replay

| Case | Result |
|---|---|
| Z2 | PASS: "a "[...]" is its key", and it moves to Action keys on the next write |
| Z3 | PASS with gaps. "Write it back onto that segment" and five "Zoya [..]" templates are covered only by the KEYS override. Nurture's next key is never spelled out. Templates still carry "(since <D Mon YYYY>)". |
| Z4 | PASS in Zoya ("none the start of another on the row"). FAIL in sweep 3t, which has no such rule. |
| S1 | PARTIAL. "Key is still open" isn't defined in the sweep. |
| Done step leaves with its key | PASS in Zoya, calendar, host boards and sweep. FAIL in the inbox (B2 below). |
| Status-forward drop | Zoya, calendar and host boards have no guard |
| Inbox trims | PASS: each one repeats a rule the prompt still states |

## Blocking

**B1. A stale decision mail can go out.**
- The new FAST rule makes "Zoya: send the sponsored commercials / precall invite / decline ..." a decision action. With no "## Decision mail" section, it sends "the wording page's template for that decision".
- The superseded check compares the row's Tier, Your call and Status with "that section". On this path there is no section, so nothing gets compared.
- If Akshay changes his call after the step was written (Sponsored to decline, say), the old mail still goes to the guest.
- **Fix:** with no section, the check compares the segment's decision with the row's current Tier, Your call and Status. If they don't match, or it's unclear, send nothing and drop the step.

**B2. The inbox can't remove a key.**
- The inbox's NEXT ACTION rule says "a done or superseded step leaves with its key". But the inbox prompt never names the Action keys field (0 mentions) or puts it in its write path, so the key line stays behind.
- Zoya matches a segment to the key line whose short name its step starts with. A leftover line can match a later step with the same opening words and mark it done, or make her rebuild against a dead key.
- **Fix:** name the field, as calendar and host boards do: "removes it and its Action keys line in the same write".

## Should fix in round 3

1. **Sweep 3t short names.** Add the Zoya rule, "no short name the start of another on the row". Define "key still open" as "its Action keys line is there and its step is not done".
2. **Status-forward drop guard.** In Zoya, calendar and host boards, add the sweep's guard: never drop a step whose key is still open or that waits on a decision. Otherwise a Status write can silently drop an Akshay ask.
3. **Sweep and Zoya's lock.** 3t writes the same Next action and Action keys fields Zoya writes. Have 3t skip rows Zoya touched in the last hour, or run 3t outside :38 to :45.

## Notes (not blocking)

- **Deploy pin.** zoya-slow-pin is still at f70901f. At deploy, push 39a5cce90dfd468ecd3bdfe413e5ef9981b4313d to `refs/heads/zoya-slow-pin`, read it back, then deploy zoya-one. Create the Action keys field before any prompt goes live.
- **Inbox base.** Build the inbox on Cleanup's msgid rev (430ceefd above), not on rev 2.
- **README.** It says 39 bytes under the limit; the inbox is now 30 under (36 on the Cleanup rev).
- **Backfill plan.** Accepted as written: read-only first, a drift check before each write, and a window that avoids :38 to :45.
