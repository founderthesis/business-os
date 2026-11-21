# Decision 409 across calendar, sweep and WhatsApp: smallest edit set (Cleanup, 5 Nov)

Cleanup proposal for the next build of each routine. Built and checked, not deployed. Nothing was written to Notion.

**Build:** `python3 patch.py <cal|sweep|wa> <live prompt> <out>`. Each run asserts the live hash and each edit once, adds no em dash, and leaves no "precall:<event id>" key. I built each twice and got byte-identical output.

| Routine | Live input | Output |
|---|---|---|
| Calendar sync | e4b39d67 (454c plus the AD Tasks rename) | 59,871 / 27d7bdf6dec91582 |
| Daily sweep | 76b49956 (463c) | 42,455 / 191497f311e79f1d |
| WhatsApp to Business OS | 8628f42a (465.2) | 27,545 / b8b7c3122e63b6ee |

## The edits (6)

1. **The exemption, in all three:** "(transcript:, precall:) stay Kind Task rows." becomes "(transcript:) stay Kind Task rows; precall promises go on the guest's own row (decision 409)."
2. **Calendar 4a, new actions:**
   - **Format:** each promise is a Next action segment on the guest's row: "<owner>: <the promise> (precall <D Mon>, by <date>)", with the owner added to Waiting on.
   - **The owner:** Akshay for his own promises, Guest or PR for their side's, Zoya for a routine mail.
   - **The date:** it goes in the segment, because 4a never changes Next date. A segment with the same owner and promise isn't added twice.
   - **A community add:** the one "Akshay: invite <first name> to the FT Community" segment, the same one sweep 3k and WhatsApp e0 use.
3. **Calendar 4a, WhatsApp invite:** "the add itself is its own Task row" now points to the segment.
4. **Calendar 4a, the Claude note line:** "precall <date> actions checked (<event id>), <n> promises: <owner>: <promise>; ...". The event id moves here from the old Task key, so WhatsApp can still find it.
5. **WhatsApp 0b:** it finds new precalls by that Claude note line instead of "precall:" Task rows. The "promises:<event id>" dedupe Activity stays as it is.
6. The sweep needs only edit 1. It has no precall step.

## Not covered by the edits: open precall Task rows to fold (the CTO, as the one Notion writer)

Nine are open now:
- Mekin (21 Oct).
- Alouk Kumar, two rows (22 Oct).
- Six created today, 5 Nov 10:38 JST, by the calendar: Prasanna Rao, two rows; Ankit Kedia, two rows; Rajmohan Krishnan, two rows.

For each:
- Carry it to the guest's Engagement as its segment, with the owner and the date in the text.
- Read the row back.
- Set the Task row to Done, then move it to Trash (decision 416).
- Report it.

Done rows from 22 to 23 Oct can stay as history or go to Trash.

Until the calendar edit is live, every precall makes new Task rows. Deploy edit 2 first.

## Also

- The WhatsApp exemption line still says "transcripts to Ranjita" (decision 456: Mamatha), and STEP 0 still says "AD Personal" (decision 460). Neither is in this set. Carry both on the WhatsApp build after this one.
- Per the CTO's note, new decisions now go in the Notion Decisions database (decision 357), not docs/decisions.md.
