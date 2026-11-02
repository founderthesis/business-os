# Inbox actions r9: decisions 443 and 444 (Akshay, 2 Nov)

**Base:** the live r8e, `../r8e/actions.txt`, 39,935 / 1d483cbd.
**Build:** `patch.py`, each edit asserted once, built twice, byte-identical.

| File | Bytes / sha256 |
|---|---|
| `actions.txt` | 41,584 / 9970262507a7141e |

The prompt is over the 40 KB target but well under the 65,536 cap.

| Decision | Change |
|---|---|
| 443, scheduling request | NEXT DATE AND WAITING ON now has four cases. The fourth: a guest or their team asks for a call on a date or window, and Next date = that date, replacing any chase date. STEP 3 gets a bullet: at once, whatever the chase step or Next date said, Zoya is added to Waiting on and "Zoya: reply to <who>: slots for <date>" goes first in Next action, other segments kept. A recording on a host show stays the host's pick. The Slots bullet's "never changes Next date" makes 443 its exception, and "Also on every Engagement" reads "four cases" |
| 444, closed row | STEP 3 gets a bullet: a fresh pitch or ask from their side on a row at They declined, We declined, Parked or Unresponsive (a blank Kind is a guest row) is never left. Read the history, keep Status, add Akshay to Waiting on, and put first in Next action "Akshay: <who> wrote again about <what>; earlier <how it closed>. Re-open, or have Zoya reply?", once per inbound. A sponsored no or a plain thanks isn't a fresh ask |

## Where else the rule appears

- **Capture (r8h)** repeats decision 81's "three cases" for the new leads it creates. Capture never handles a scheduling request (that's actions' STEP 3), so it stays as it is. It can say "four" at its next rebuild.
- **The calendar routine** sets Next date only from the calendar, so it doesn't conflict.
- **Zoya** sets Next date from her own segments' dates (WRITE PATH), so a "slots for <date>" step is consistent with 443.

## r9b (replay9.json)

| Defect | Fix |
|---|---|
| D1, high: 443 and 444 both fired on a closed row | 443 applies to open rows only. On a closed row the request is a 444 item for Akshay |
| D2: a calendar date could be overwritten | 443 replaces a chase date, never a calendar booking's date |
| D3: a stale chase segment survived | The chase or went-quiet segment for that person leaves; the rest are kept |
| Case f: a second "wrote again" ask | The segment ends "(<D Mon>)" and is kept with the others. If one is already open, it's updated, never added again |
| D5: Zoya could reply before Akshay chose | Until he chooses, STEP 5 and 6e queue no Zoya reply on that thread |
| D6: clash with decision 151 | On a revenue row the slots step goes first and his other items stay |
| D7: decision 425 | A Tier 1 guest, or a date today or tomorrow, gets "Akshay: <who> asks for a call on <date>: pick a slot", with Akshay instead of Zoya |
| D8, D9 | Next date is untouched on host shows. A window means its first day; a date already past means today |

**Status:** written. Re-replay to follow, then Cleanup, then the CTO deploys.
