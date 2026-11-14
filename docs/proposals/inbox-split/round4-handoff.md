# Round 4: for Cleanup's re-review and for the CTO (1 Nov)

**Cleanup:** please re-review round 4. It fixes your round 3 verdict (`cleanup-verdict-round3.md`): R1 to R4 and should-fix items 1 to 8. My offline replays then found new holes in the joins. Those are fixed in 4b and 4c, and `README.md` has a table for each:
- `replay4.json`: A1, R1b, R3b;
- `replay4b.json`: B4 again, S-J1, S-J2, the Zoya prefix.

The final replay (`replay4c.json`) passes every case: R1 to R4, A1, B1 to B10, S1 to S9 and D1 to D9.

| File | Bytes / sha256 |
|---|---|
| capture.txt | 35,848 / 0c7cb3d1a16d13bd |
| actions-v2.txt | 39,354 / 19701651a6c0edf3 (646 B under 40,000) |
| yourcall-sections.md | 7,326 / a28b43da3b0aac36 (unchanged) |
| sweep.txt | 39,131 / 6783dd01e396e5ab (unchanged) |
| actions.txt (v1) | 45,753 / 00e79fa49a1102d6, not for deploy |

Each file was built twice, byte-identical, the same way as before. No em dashes were added.

**Two departures from your fix wording:**
- **A1 (late stamps).** Instead of widening actions' Captured window, which would fetch every row captured today on every run, capture lists each id it stamps late on its record's "stamped:" line. Actions reads only that line, from capture records of the last 24 hours.
- **Zoya's rows.** One rule in all three places: an Email out whose Summary starts "Zoya" is hers.

**Open, optional (left out so the build stays as replayed):** if capture crashes between stamping a row and listing its id, that row is never stamped again. Writing the id first closes it. Say if you want it.

**For the CTO, at cutover:**
- Paste sections 6 to 8 of `yourcall-sections.md` onto "Inbox and Your call rules", ending with the line "END OF INBOX ACTIONS SECTIONS 6-8". Read it back before actions is enabled.
- Enable capture on or after 2 Nov JST: "today" is now the JST date in both prompts.
- Before cutover, check one Notion row: does Zoya's routine log ad@ mail she's only Cc'd on? R1b assumes it can.
- Nothing is deployed, and this session doesn't deploy.
