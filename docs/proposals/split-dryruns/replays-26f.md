# Replays C, G, H, D and E on split26f, 26 Oct (read-only)

**Build:** split26f (FAST 35,262 / 4d493ffe6f7f888d, SLOW 64,996 / 7730656105c89751).

**Assumed:** keys-d992814.csv applied, and an "Action key" property on Activities.

| Replay | Verdict | Cause |
| --- | --- | --- |
| C contact holds | FAIL | Amit passes, except AFTER SEND said a deferral moves only Next date, which would undo the hold. Ronit has a same-day contradiction: ONE PERSON's 7-day rule against LIMITS' weekly limit. Vijay was read as both a hold and a block, and his hold had no segment to date. |
| G same-minute start | FAIL | FAST's "Sponsored yes: next steps" and SLOW's billing ask could both go out, under different keys. |
| H overlapping writes | PARTIAL FAIL | Restore covered segment and owner but not the note line. FAST couldn't clear SLOW's step that the same inbound completes. FAST had no 25-minute guard. |
| D capped leftovers | FAIL | The per-run cap was counted from the day's sends, so after 40 a day every run was "capped". Rules for Zoya 5a said a cap moves Next date. Leftover nurture rows could wait indefinitely. |
| E one mail, several asks | PARTIAL FAIL | FAST can't name an inbound the inbox hasn't logged. WRITE PATH blocked completing the other asks. The -2 key wasn't stored. |

**Fixed in text by d-split26g, plus four Rules for Zoya edits:**
- quiet hours now match decision 393
- two guests share one mail only if both are one company
- a cap changes nothing
- hold notes use "held:"

**Residual risk, unchanged:**
- Notion has no conditional write. A third-party segment or note line lost in a two-way race can't be restored by either run.
- Row-level fields (Status, Chase step, Last activity) are last-writer-wins.

**Data to fix at launch:**
- Vijay: Waiting on empty.
- Akshat: Next date is later than his earliest open segment.
- Mekin: no Next date.
- Payal Dash has two People rows. Flag it as a possible duplicate; merging is Akshay's call.
