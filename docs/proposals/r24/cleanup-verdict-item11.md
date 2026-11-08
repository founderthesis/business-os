# Cleanup delta verdict: r24 item 11 (missed form chasers), commits 83b49a4, b41e27a, a78f55a

Cleanup session, 8 Nov 2026, about 12:10 JST. Read-only. **Decision 523** (the routine 5 rework: weekly then fortnightly chasers, the hi-res photo fill-in, to Akshay two weeks before release) **isn't in any build yet**: no build mentions it, a photo check or the new schedule. I'll review it as its own delta when Main pushes it.

## Verdict: accepted as built, with two should-fixes. Not deployable as the final item 11 until 523 lands.

### Builds (each twice, byte-identical, equal to the commit; no new em dash)

Changed against my delta verdict (ef24819):

| Routine | Bytes / sha256 |
|---|---|
| Inbox actions | 47,952 / 96f0592910bf9719 |
| Daily sweep | 50,314 / afb7a2b426779bc6 |
| Zoya SLOW file (pin 83b49a41547da0c08d68fb0b6e95de74139ac4f1) | 91,217 / abf90f51139e4229 (91,213 characters) |
| Zoya SLOW task | 15,949 / 31ab7352e66c82bf |

The SLOW task's fetch, sha prefix and character total match the file at 83b49a4.

Unchanged:
- calendar c613af00
- capture f64eb54e
- WhatsApp bec8c1e1
- hourly e959b047
- host boards 7f5c87ab
- dossiers 67e07a00

### What it does (checked)

- **Inbox actions 2b c.** Akshay's own thank-you or form ask, sent to a Founder Thesis guest at Recorded with no form and no seq-5 segment, adds "Zoya [followup seq-5-1 <D>]: form chaser 1 on <D Mon>". D is his mail's date plus routine 5's first gap, read from Cadences, never from memory. If Cadences can't be read, there's no segment and it's reported. The segment replaces the stale "Waiting on <guest>: form" segment. This fixes hand-sent thank-yous that never started routine 5.
- **Sweep Form backstop.** A Founder Thesis row at Recorded with a thank-you Activity, no form and **no seq-5 segment** gets one seq-5-1 segment at the next working day, and is reported. **One chaser per row:** it never adds a second while any seq-5 segment exists, so it can't schedule a catch-up. Other shows keep the old reminder.
- **SLOW selection.** Every in-scope row with a keyed Zoya segment dated today or earlier is a candidate, whatever its Next date says ("a later date never hides a due one"). This is the Saket and Srinivas fix.

## The CTO's two checks

1. **Next date at the earliest dated segment everywhere it's written: partly.**
   - Zoya: yes. The SLOW file's shared rule says "a write that changes Next action sets Next date to the earliest open segment date", and SLOW now selects due keyed segments regardless of Next date.
   - Not the two new writers:
     - inbox actions 2b c adds a dated segment without touching Next date;
     - the sweep backstop can't, because sweep HARD forbids changing Next date outside its hold exception.
   - Chasers will still fire, thanks to the SLOW selection fix. But the row's Next date can stay later than a due chaser, which hides it from anything that reads Next date: the sweep's overdue count (4b), Akshay's views sorted by Next date, and the morning check. **S1.**
2. **Sweep backstop: one chaser per row, no burst: yes for the backstop itself.** The open risk is downstream in the chaser chain. **S2.**

## Should-fix

- **S1. Earliest-segment Next date everywhere a dated segment is written.**
  - In inbox actions 2b c, add: "and set Next date to the earliest open segment date, as Zoya's rule says".
  - In the sweep, allow one more Next date exception in HARD for the Form backstop: "Next date = the earliest open segment date when you add the seq-5 segment".
- **S2. No catch-up burst down the chain.**
  - A seq step's raised time is "the date the previous step set". If 2b c dates chaser 1 in the past (a recovered or REPAIR mail of Akshay's from days ago), chaser 2 counted from chaser 1's due date is in the past too, and the two go out on consecutive runs.
  - Add to routine 5 (or the shared ACTIONS seq rule): "the next rung is dated from the day the previous one was actually sent, never from its due date; at most one form chaser per row per run".
  - In 2b c, a D already past becomes the next working day.
- **S3 (decision 523, when it lands).** The CTO's four checks:
  - the fill-in creates exactly one Guest forms row and sends no confirmation;
  - the photo width check runs in code, never a LinkedIn photo;
  - the "after 5 chasers" rule is gone everywhere: the repo builds, the Rules for Zoya routine 5 page and Cadences;
  - chasers stop at two weeks before release and never resume.

  S2's "dated from the actual send" applies to the new weekly and fortnightly schedule too.
