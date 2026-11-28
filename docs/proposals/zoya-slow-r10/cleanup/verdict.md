# Cleanup verdict: Zoya SLOW r10d and FAST (8bf34ea, 4a6ac8c), 2 Nov ~18:30 JST

This covers the changed behaviour only.

**Accepted. No blocker.** Deploy in the handoff's order:
1. Move `refs/heads/zoya-slow-pin` to 8bf34eacda40afc723083d6888e5db1706414762 and read it back.
2. Paste `zoya-slow-r10/zoya-one.txt`, **44,075 / a61097095c2e3070**, and byte-compare it.

The replay is in `replay-cleanup.json`.

## Rebuild

- **Build:** a worktree at f70901f with `zoya-slow-r10/build_one.patch` alone (it already holds the rules-read hunk), then `build_one.py <dir> refs/heads/zoya-slow-pin 8bf34eacda40afc723083d6888e5db1706414762`, twice. Both builds were byte-identical:
  - zoya-one.txt: 44,075 / a61097095c2e3070, the same as the repo file;
  - zoya-slow-work.txt: 66,441 / 0283994c454d1d42, the same as `git show 8bf34ea:routines/zoya/release/zoya-slow-work.txt`.
- **FAST against the live 775b9ed8:** it differs only in the host add-back wording, "if any", the pin commit and hash, and the version string.
- **SLOW against f70901f:** it differs only in the intended edits.
- **The deploy order is safe.** f70901f is an ancestor of 8bf34ea. The live FAST fetches the ref, then reads the file by its hard-coded sha, so moving the pin first doesn't change today's runs. The new FAST checks for the prefix 0283994c454d1d42 at 8bf34ea.

## Changed behaviour: OK

- **Sri and the host** are kept or added back in SLOW's own sending text. PRE-SEND CHECKS (with "if any"), GUEST EXAMPLES and BOOKING LINKS are in the SLOW file too, so "on SLOW work it wins" no longer undoes them. D1 is closed.
- **SLOW BATCH:**
  - It writes an eligible list with keys, and one outcome line per item.
  - It records "elapsed <n> min" from `date -u`, and keys under "carryover:".
  - It stops only on the per-run or daily cap, the 40 minutes, or a tool error. Anything else is "stopped early", a defect.
- **The caps still bind.** The per-run cap counts "this run's own sends", shared with FAST's. The daily cap is unchanged. No cadence limit is lifted ("within every limit there; no cadence changes").
- **Holds don't weaken any person-wide stop.** A hold or a group limit "defers those items only", but each item is still checked fresh against no-contact, ONE PERSON, ONE ASK and Akshay's holds.
- **No resend of carryover.** Each carried item is worked again through the ACTIONS key lookup, the Sent check and the idempotency_key, so nothing is resent.

## Should-fix (follow-ups)

1. **Where carryover goes.**
   - "carryover ... goes first, then SLOW ORDER's groups" is meant within STEP 2. That's how it reads in place: the paragraph sits after "STEP 0 ..., STEP 1b, the team work above, then STEP 2", and the eligible list is STEP 2's items.
   - A literal run could still send carried follow-ups before STEP 0's feedback and bounce scan.
   - **Fix:** "carryover first within STEP 2, after STEP 0, 1b and team work; a carried key not in this run's eligible list is dropped".
2. **"A tool error" is undefined.**
   - One passing failure could end the batch.
   - **Fix:** "a call that fails after one retry; it stops only the work that needs that tool; a failed PRE-SEND check blocks that item only".
3. **The host isn't in the read-back exclusion list** (older than r10, FAST too). The list names only "on un#, Sri", while SCOPE keeps the Built to Share and Human by Design hosts out of Cc unless they wrote. **Fix:** add the host to that list.
4. **FAST's LIMITS wording reaches SLOW sends.**
   - "Everything this run sends ... the 7-day limit, ONE PERSON, ONE ASK ... don't hold it" also covers SLOW's sends; only "SLOW wins" saves it.
   - **Fix:** "Everything FAST work sends".
5. **Snooze keys can collide.**
   - "snooze:<row id>:<its date>" has no year, and two snoozes on one row on the same day share a key. Being worked twice is harmless.
   - **Fix:** use YYYY-MM-DD plus the segment number.
6. **Lock risk on longer runs.** A crash before RELEASE leaves the lock held. **Watch the first SLOW run (10:38 tomorrow).** Its record should show "eligible <n>:", outcome lines, "elapsed <n> min", "carryover:", a named stop reason, and the lock freed.

Nothing deployed or moved by Cleanup. The pin move is the CTO's.
