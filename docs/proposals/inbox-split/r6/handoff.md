# Capture r6b: for the CTO to paste and relay to Cleanup (2 Nov)

**Ready for the 09:02 JST run.** The offline replay passes (`replay6.json`, sections r6 and r6b).

| File | Bytes / sha256 |
|---|---|
| capture.txt | 37,954 / 9b55110e2cead4c2 |

- **Base:** the live r5, 36,666 / 405a30d3.
- **Build:** `patch.py`, built twice, byte-identical.
- **Diff:** only the listed edits, no em dash. `README.md` has the table.
- **Unchanged:** actions (39,354 / 19701651) and the sweep (6783dd01).

**What r6b does:**
- **1. Duplicates:** STEP 0 runs STEP 2's full lookup before any re-key, and any hit folds the row. This is the 108855 case.
- **2a. Early stops:** the run works to the cap or STOP TIME. Stopping early is Partial, "stopped early".
- **2b. Reads:** bodies are read with read_batch (20 a call, 2,000 characters). Truncated forwards, pitches and edit notes are read in full.
- **2c. Stakeholders:** the full get_thread sweep runs only for a new pitch, a new thread, or an address not yet in People.
- **2d. Message-IDs:** a Message-ID taken from References or In-Reply-To is used only if the HEADER query returns that same message. Otherwise the raw fetch runs as before.
- **2e. BACKLOG:** with more than 15 due at the start, the cap is 25.
- **2f. Stop times:** both count from the run's start. No new message after 18 minutes, and no STEP 0 row after 8.
- **OVERLAP:** if another capture record is still Started and under 30 minutes old, the run writes No-op and stops.

**One departure from the ask:** in BACKLOG, STEP 0's rows don't count toward the 25. STEP 0 runs first and could take 15 of them, leaving new mail fewer slots than a normal run (replay R6-2). It shares only the time window.

**Hand runs:** never between :35 and :50, because the overlap guard doesn't cover Zoya's :38 run. Never within 30 minutes of another capture run.

Nothing was deployed by this session.
