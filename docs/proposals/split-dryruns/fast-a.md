# FAST dry run A (26 Oct 12:05 JST, read only, zoya-fast before d-split26b)

Same data as run B, started the same minute. Send list: none (decision mails for Visat Patel, Ankush Tiwari, Amit Chand
and Sandeep Shah already went this morning and are logged; no approved day-before drafts; no unanswered thread in Zoya's
445-message inbox; no new replies on loop-in threads).
Held reply actions: Todd McDonald (un#, slots ask, waits on Sri, holding reply 21 Oct), Mekin Maheshwari (B2S, Satish),
and three release-date asks waiting on Akshay (Srinivas Choudhary, Anmol Madan, Vineet Agarwal). Sukant skipped (answered
by Akshay 25 Oct; the follow-up left is SLOW's).
Run record: "No-op", due 5, sent 0, held 5.

Replay 1 comparison (runs A and B): same empty send list and same release-date and Mekin holds. Differences: A counted
Todd McDonald's held slots ask and skipped Sukant; B completed Sukant by match and missed Todd. Neither wrote keys (the
keying deadlock, fixed in d-split26b). Re-run after the fixes to compare keys.

Problems beyond run B's: INVITES and EDIT NOTES referenced but absent in FAST (INVITES now its own part in both prompts;
edit notes stay SLOW's); held actions vs No-op labelling (fixed: held or blocked counts as handled, Completed); the send
cap's SQL date filter must use datetime() (fixed in both LIMITS parts); the 72-hour-plus inbox sweep is unbounded on a
445-message inbox (open: for slimming, with source cursors).
