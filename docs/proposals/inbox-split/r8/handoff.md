# Capture r8d: for the CTO to relay to Cleanup and deploy (2 Nov)

**Ready.** The offline replay (`replay8.json`, sections r8 to r8d) passes. Nothing was deployed by this session.

| File | Bytes / sha256 | Base |
|---|---|---|
| capture.txt | 39,998 / 5ef8b9379a1591e4 | live r7, 39,522 / 3f08b76e |

Built twice, byte-identical, with `patch.py`. Actions, the sweep and Zoya are unchanged.

**What r8d does:**
1. **Link pass (LINK, a third STEP 0 class).**
   - **What it takes:** mail rows (msgid: or adid:) with no People and no Engagement, created since 2026-11-01T03:00Z, Captured before today, through 2026-11-05. It never takes Zoya's own Email out rows.
   - **What it does:** it links them as STEPS 2 and 3 do, creating the People or Engagement rows they would, with no loop-in. A row it finds keeps its Status, Waiting on and Next action.
   - **Limits:** STEP 0 takes up to 5 of each class, the others filling the rest. LINK sits inside STEP 0's 15, not the BACKLOG cap, so new mail keeps its 15 or 25 slots. This departs from your wording.
2. **Old allmail: rows** that are ad@-only and not sent from ad@ re-key to adid:<UID>, with no RAW, after MSGID FIND and STEP 2's lookup. An id outside All Mail is found there first.
3. **RAW returned inline** is written to a new file per message, `r<UID>`, 8,000 characters per heredoc. It's decoded after each chunk with newlines stripped, so chunk boundaries don't matter, and it stops once a complete id shows. A failure pends and never stops the run; a STEP 0 row gets the body line instead. This was tested in Bash with two messages in one run.

**Known limits:**
- Today's 14 unlinked rows link from 3 Nov, not today. Captured is STEP 0's only queryable "tried" mark, and Notion can't filter on body text.
- A repeat pitch that LINK finds is linked but not put on Akshay's list. That happens only for mail logged before r8, so it's low risk.
