# Cleanup verdict: Zoya r11b (63fcf66, c5663a4, 9c8bc0c), 3 Nov ~12:55 JST

This covers the changed behaviour only.

**Accepted. No blocker.** Deploy in the handoff's order:
1. Move `refs/heads/zoya-slow-pin` to 63fcf669014fe5c4eeff64c7fedbe6d1c85d926c and read back the file's sha256 (2cf5b7156ce80240).
2. Paste `zoya-r11/zoya-one.txt`, **44,839 / 264f69fc3ae384c2**, and byte-compare it.

## Rebuild

- **Build:** a worktree at f70901f with `zoya-r11/build_one.patch`, then `build_one.py <dir> refs/heads/zoya-slow-pin 63fcf669014fe5c4eeff64c7fedbe6d1c85d926c`, twice. Both builds were byte-identical:
  - FAST: 44,839 / 264f69fc3ae384c2, the same as the repo file;
  - SLOW: 67,837 / 2cf5b7156ce80240, the same as `git show 63fcf66:routines/zoya/release/zoya-slow-work.txt`.
- **FAST against the live a6109709:** it differs only in RULES LOAD, check 1, "Everything FAST work sends", the pin commit and hash, and the version string.
- **The pin** is at 8bf34ea now, which is an ancestor of 63fcf66. Moving the pin first is safe: the live FAST reads its SLOW file by its hard-coded sha.

## The fix for Auditor finding 1: OK

- **RULES LOAD** reads every required page in full every run.
  - A fetch saved to a file is loaded in python as one string ("its text field when it is JSON") and printed in slices of 20,000 characters to its end. Then it logs "<page>: <read> of <total> characters".
  - **Checked against a real saved fetch** (Rules for Zoya, 1 Nov): the file is JSON with `metadata`, `title`, `url` and `text`, and `text` is 63,744 characters. So the recipe's total is well defined, and a full read is 4 slices.
- **Check 1** blocks every send that uses wording or rules when any required page is short or unread, with no "the part I need was loaded" exception. That's exactly the 07:38 failure: 21k of 62k, then 3 sends.
- **A short page ends the run Partial** ("rules not loaded: <page> <read> of <total>"), so a fully blocked run can no longer read as Completed (D1).
- **SLOW-only pages** (follow-ups and the routine pages it links) never block FAST sends (D2, D5). That fixes the 10:38 skip from the FAST side.
- **No resend of the morning's 3 mails.** ACTIONS' key and Sent check are unchanged.

## My SLOW should-fix 1 to 5: in

- Carryover goes first within STEP 2, after STEP 0, 1b and team work, and a non-eligible carried key is dropped and logged.
- "A tool error" is a call that fails after one retry, and it stops only the work needing that tool.
- The Built to Share and Human by Design hosts are in the read-back exclusion unless they wrote.
- FAST's LIMITS says "Everything FAST work sends".
- The snooze key carries the full date and a segment marker.

## Follow-ups (low; Main's queued four plus one)

- **N1:** "the run ends Partial" should say it carries on with work no short page governs.
- **N2:** fetch the follow-ups page only in runs with SLOW work, so an outage there doesn't mark every hourly run Partial.
- **N3:** name ACTIONS and STEP 2 in the "writes nothing" override.
- **D5:** name the routine pages in RULES LOAD.
- **New:** a page Notion itself truncates server-side (the fetch's `truncated` or `unknown_block_count`) would show read = total but still be incomplete. Today's Rules for Zoya fetch has no such field. Add "and the fetch reports no truncation" to "loaded".

**Watch the first run after deploy:** one "<page>: <read> of <total>" line per required page, read = total. For Rules for Zoya, expect about 63,744.

Nothing deployed or moved by Cleanup.
