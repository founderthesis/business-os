# Inbox actions r9: decisions 443 and 444 (Akshay, 2 Nov)

**Base:** the live r8e, `../r8e/actions.txt`, 39,935 / 1d483cbd.
**Build:** `patch.py`, each edit asserted once, built twice, byte-identical.

| File | Bytes / sha256 |
|---|---|
| `actions.txt` | 40,922 / 467583c5fc53bf32 |

The prompt is over the 40 KB target but well under the 65,536 cap.

| Decision | Change |
|---|---|
| 443, scheduling request | NEXT DATE AND WAITING ON now has four cases. The fourth: a guest or their team asks for a call on a date or window, and Next date = that date, replacing any chase date. STEP 3 gets a bullet: at once, whatever the chase step or Next date said, Zoya is added to Waiting on and "Zoya: reply to <who>: slots for <date>" goes first in Next action, other segments kept. A recording on a host show stays the host's pick. The Slots bullet's "never changes Next date" makes 443 its exception, and "Also on every Engagement" reads "four cases" |
| 444, closed row | STEP 3 gets a bullet: a fresh pitch or ask from their side on a row at They declined, We declined, Parked or Unresponsive (a blank Kind is a guest row) is never left. Read the history, keep Status, add Akshay to Waiting on, and put first in Next action "Akshay: <who> wrote again about <what>; earlier <how it closed>. Re-open, or have Zoya reply?", once per inbound. A sponsored no or a plain thanks isn't a fresh ask |

## Where else the rule appears

- **Capture (r8h)** repeats decision 81's "three cases" for the new leads it creates. Capture never handles a scheduling request (that's actions' STEP 3), so it stays as it is. It can say "four" at its next rebuild.
- **The calendar routine** sets Next date only from the calendar, so it doesn't conflict.
- **Zoya** sets Next date from her own segments' dates (WRITE PATH), so a "slots for <date>" step is consistent with 443.

**Status:** written. Replay to follow, then Cleanup, then the CTO deploys.
