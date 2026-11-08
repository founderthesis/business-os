# Cleanup delta verdict: decision 523 (routine 5 rework) at f069257, pin 7358ad9

Cleanup session, 8 Nov 2026, about 21:00 JST. Read-only.

## Verdict: accepted with one condition (C1: never resume after the two-week stop). Fold it into Main's item-11 should-fix commit.

### Builds (each twice, byte-identical, equal to the commit; no new em dash)

| Routine | Bytes / sha256 |
|---|---|
| Inbox actions | 47,952 / 980fe680470dfd64 (the 523 citation only) |
| Zoya SLOW file at pin 7358ad95d163a0855654be74fe77669af4bd0420 | 92,791 / b5b7da4fe144640a (92,787 characters) |
| Zoya SLOW task | 15,949 / 3ff0271b93ff5e8d |
| Zoya hourly | 62,978 / 459d1dd19f1b4d8a (22 bytes under 63,000) |

The SLOW task fetches 7358ad95d163a0855654be74fe77669af4bd0420, expects sha prefix b5b7da4fe144640a and 92,787 characters, all matching the file at 7358ad9.

The hourly's only behaviour change is that an image from their side on an open seq-5 row is SLOW's (FORM PHOTO), so the hourly doesn't reply. The rest is citation cuts and the version reference.

## The CTO's four points

1. **One Guest forms row, no confirmation mail: mostly.**
   - FORM PHOTO is one item per "formphoto:<Message-ID>". Once it has filed one, the seq-5 segment is gone, so a later photo mail no longer qualifies.
   - "never a mail saying the form was filled in" is explicit. A too-small photo gets one reply asking for a hi-res one.
   - **Should-fix S1:** a crash between creating the Guest forms row and removing the segment would let the retry create a second row. Before creating, look for a Guest forms row Filled by "Zoya" linked to this Engagement and reuse it. Put the "formphoto:<Message-ID>" key in the Claude note line.
2. **Photo width in code, never LinkedIn: holds.**
   - "In a Bash python step, decode it and check it is at least 1000 px wide (from the image header, never by eye)".
   - "Never a LinkedIn or web photo".
   - Only an image attachment from their side counts.
3. **"After 5 chasers" gone: holds** in every r24 build and the SLOW file. Decision 386's count is gone; mail n goes on its Cadences day (7, 14, 21, 28, then every 14) and there's no last mail. The "after the last" left in the SLOW file is the payment reminders'. I didn't re-read the routine 5 page or Cadences in Notion: the CTO says both are updated.
4. **Stop two weeks before release, never resume: the stop holds, never-resume doesn't. C1.**

## C1: never resume after the stop

At two weeks before release with no form and no photo, the SLOW file says "no more chasers; one segment 'Ask Akshay: ...'". It doesn't say what happens to the open seq-5 segment.

If that segment leaves (removed, or superseded under NEXT ACTION SIZE), the row is Recorded with no form and no seq-5 segment. That's exactly the trigger for:
- the sweep's Form backstop, which adds seq-5-1 at the next working day;
- inbox actions 2b c, on Akshay's next mail to the guest.

Either one restarts the chain. A Planned release that slips later would also reopen it.

Fix, in the same commit as the item-11 should-fixes:
- **SLOW routine 5:** at the stop, remove the seq-5 segment and add the Claude note line "YYYY-MM-DD: form chasers stopped (decision 523, two weeks before release <D Mon>)". A row with that line never gets another routine 5 mail, whatever the release date does later.
- **Sweep Form backstop and inbox actions 2b c:** also skip a row whose Claude note has "form chasers stopped".

## Still to come

Main's commit with the item-11 should-fixes:
- S1: Next date at the earliest open segment, in inbox actions 2b c and the sweep backstop;
- S2: no catch-up burst: each rung dated from the previous actual send, at most one form chaser per row per run, a past D moved to the next working day.

I'll review it, with C1 above, as the last delta and then give the one final deploy table for all of r24.
