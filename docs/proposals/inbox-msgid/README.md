# Inbox: Message-ID before any Activity, full steps for every capped message

Asked by the CTO (1 Nov, 12:35 JST). This is a patch on the live inbox, 65,325 / e6cf4db2bc37918b (the cap build).

| File | Bytes / sha256 |
|---|---|
| `inbox.txt` | 65,334 / 2f3250ed1d45e7db |

Built twice, byte-identical. 2 bytes under the build limit.

## What changes

1. **No Message-ID, no Activity.**
   - `original` is called one at a time and is never skipped to save load.
   - If there's still no Message-ID after one retry, error or not, the message isn't logged. It goes on pending as `mcp:<its id>`, retried by id, and the run doesn't end Failed for it.
   - The `allmail:` fallback is gone.
2. **Existing `allmail:` rows are repaired when re-read.**
   - The lookup now finds `allmail:<id>`.
   - A lone `allmail:` row is re-keyed to `msgid:` and worked as a new message (STEP 2's fields, then STEPS 3 to 6e), with no second row.
   - The "any hit means logged" sentence excludes it.
   - A row that also has a `msgid:` twin is left for the one-off reconciliation (`reconcile-allmail.md`).
3. **The cap limits messages, never steps.**
   - Each of the up to 15 messages gets STEPS 2 to 6e before the next.
   - STEP 2's "batch the creates (up to 50 per call)" becomes "batch one message's creates".
   - The cap is the approval: a backlog never means working none, skipping a step, or asking Akshay.

## Replay (`replayMID.json`) and round 2

**Round 1:** M6 (no provider-id key or skip-for-load left) and M7 (Zoya's mail found by its msgid:) passed. The rest needed fixes, all made in this build and not yet replayed again:

| Case | Problem found | Fix |
|---|---|---|
| M2 | An `original` error ended the run Failed, and a message without a Message-ID had no pending key | "error or not ... pend it as mcp:<its id>, not Failed", plus the pending retry by id |
| M5 | "any hit means it is logged" could stop the re-key | the sentence now excludes a lone `allmail:` row |
| M3 | "work it from STEP 3" skipped STEP 2's fields | "work it as new" |
| M4 | "report both" was ambiguous | removed; duplicates go to the reconciliation |
| M1 | cross-message batching broke "before the next" | "Batch one message's creates" |

**Not covered by the prompt:** most of the 12:12 `allmail:` rows are older than the next window and won't be re-read. `reconcile-allmail.md` covers them.
