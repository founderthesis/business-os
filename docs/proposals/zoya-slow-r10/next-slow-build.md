# Queued for the next Zoya SLOW build (Cleanup's should-fix on r10d, 2 Nov)

SLOW r10d is live: pin 8bf34ea, FAST 44,075 / a6109709, deployed 20:48 JST. These six items go into the next SLOW build. None is blocking.

1. **Carryover placement.** Say "carryover first within STEP 2, after STEP 0, 1b and team work". A carried key that's not in this run's eligible list is dropped.
2. **"A tool error".** Define it as "a call that fails after one retry". It stops only the work that needs that tool, and a failed PRE-SEND check blocks that one item only.
3. **The host in the read-back exclusion list** (FAST and SLOW sending). Add "on Built to Share and Human by Design, the host unless they wrote on the thread", next to "on un#, Sri".
4. **FAST's LIMITS wording reaching SLOW sends.** Change "Everything this run sends" to "Everything FAST work sends".
5. **Snooze keys.** Use "snooze:<row id>:<YYYY-MM-DD>:<segment n>".
6. **Watch the first SLOW run (Tue 3 Nov, 10:38 JST).** Its record should have:
   - "eligible <n>:";
   - outcome lines;
   - "elapsed <n> min";
   - "carryover:";
   - a named stop reason;
   - the lock freed.

   That's the CTO's check, not a build item.

**Build:** as r10, from f70901f's parts with `build_one.patch`, plus these edits. Then a new pin commit, and FAST rebuilt against it.
