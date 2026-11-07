# Replay 1 again: FAST twice with the keying migration applied (split26e), 26 Oct 12:45 JST

Two read-only FAST runs on build split26e (FAST 35,144 / 36ffead8fae85afa), each treating keys-migration.csv as applied. Nothing was sent or written.

| | Run A | Run B |
| --- | --- | --- |
| Sends | 1: Ankit Utreja, key `...813287bbf83d4112e716:decision:call-...:2026-10-19T00:00:00+09:00`, from ad@ on Gmail message 1a0f652340581599, To Devanshi, Cc Zoya | identical (same key, thread, recipients; body words differ slightly) |
| New keys | none | none |
| Completed by match | Ankush (decision mail 26 Oct), Sukant (Akshay's 25 Oct reply) | identical, same Activities and keys |
| Mekin | waits on Satish (host pick) | identical |
| Vishal Devanath | blocked (Charge Zone profile unknown) | identical |
| Release-date replies (Vineet, Srinivas, Anmol) | counted blocked | counted held |
| Run record | due 8, sent 1, matched 2, held 1, blocked 4 | due 8, sent 1, matched 2, held 4, blocked 1 |

**Verdict: PASS on keys and send lists.** Both runs keyed nothing new and sent the same single mail under the same key. They also completed the same two actions by matching Activities.

The only difference is how the run record labels the three release-date replies. A step waiting on a missing fact is a block under STEP 2's definition ("missing data"), so run A's count is the right one. The next text pass will add one clause so FAST uses the same words.

**Findings for the launch fixes (not part of the gate):**
1. Ankit Utreja's Next date is 3 Jan 2027, even though Akshay said "chase hard" on 19 Oct. After the send, no open segment has a date. Set Next date at launch, and have the send write the reply-wait segment with a date.
2. Sukant: completing his reply action also drops Akshay's "Zoya can follow up". The migration file should carry it as a SLOW follow-up segment dated 30 Oct.
3. Ankush: the run that sent the decision mail left its segment behind. The migration file should drop that segment, since its key is completed by match.
4. The release-date reply keys block on every hourly run, because they need a date Akshay hasn't confirmed. They should be keyed as SLOW follow-ups rechecked weekly, not as FAST replies.
5. Two Kind Task rows on the AD Personal show were keyed as decision, but FAST's scope never reaches them. Take them out of the migration file.
6. Zoya's Sent folder holds two copies of most sends, usually a second apart. The Ranjita pair was 15 seconds apart, so check that pair's Message-IDs before go-live.
