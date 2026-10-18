# AR-20261018-8 run reporting pilot: walkthroughs

The patch applies after p333 Stage B v2. It touches only the inbox and Zoya. Constructed cases, worked against the patched text. Nothing was deployed or run.

Key: `run:<routine>:<YYYY-MM-DDTHH:MM> JST`, the start minute, a synthetic key because the runtime exposes no run id. The record is an Activity, Kind Note, Source empty, linked to no row.

| Case | What the run does | Record at the end |
|---|---|---|
| Success | Creates "Run inbox 2026-10-19 08:00 JST: Started" first, does its steps, then updates the same row | "...: Completed"; body is the STEP 8 report, end time, counts, links to the Activities it logged |
| No-op | Started row, nothing to act on | "...: No-op"; body says what was read |
| Partial | One step fails (say, a Notion write on one Engagement), the others run | "...: Partial"; the failed step and its next owner are in the body |
| Run dies mid-way | Started row only | Stays "Started"; read as unconfirmed, not as failed |
| Report write fails | First write fails: the run retries once, then carries on with business steps. A failed final update is retried once, then the failure goes in the chat report | No business action is repeated; the record may be missing or stuck at Started |
| Retry dedupe | The same run re-attempts the record create (a tool retry) | Same Source ID, so the existing row is reused, never a second |
| Next scheduled run | New start minute | New key, new row |

Exclusions:
- No People, Engagement, Deal or Episode link, so the Last activity, contact-date and per-row "Activity in the last N days" checks never see it.
- The Summary starts "Run", so the "Zoya sent" and "Agent sent" cap counts never count it.

Prompt bytes after Stage B v2 plus AR-8:

| Prompt | Bytes | sha256 | Spare to 65,536 |
|---|---|---|---|
| inbox | 64,164 | 86cb9037594ed26b | 1,372 |
| zoya | 39,890 | 79da558d5bb51565 | 25,646 |

Superseded text replaced:
- Inbox STEP 8 "nothing else written anywhere" now names the run record as the report's home.
- Zoya STEP 3 does the same.

Not in this pilot: sweep reconciliation of stale Started records (the contract leaves the sweep to verified schedules) and the other routines.
