# AR-20261018-8 run reporting pilot: walkthroughs (v2, CTO-20261018-4 identity fix)

The patch applies after p333 Stage B v2. It touches only the inbox and Zoya. Constructed cases, worked against the patched text. Nothing was deployed or run.

## Run identity

The run id is fixed once, before the first Notion write:
1. `printenv CLAUDE_CODE_REMOTE_SESSION_ID`: the provider's id for this run. It is a `cse_...` value, the same form as `last_run.session_id` on the scheduled task. The value was present in a cloud session on 18 Oct.
2. Else run once: `echo "syn-$(date -u +%Y%m%dT%H%M%SZ)-$(od -An -N4 -tx1 /dev/urandom | tr -d ' \n')"`, labelled synthetic. Two calls in the same second on 18 Oct gave `syn-20261018T123158Z-11514971` and `syn-20261018T123158Z-e3005a85`.

The Source ID is `run:<routine>:<run id>`. The start time is kept separately, in Date and the Summary. The id is never derived again in the same run, and it never replaces a send's idempotency key or any business dedupe.

## Cases

| Case | What happens | Result |
|---|---|---|
| Success | Started row created, steps run, same row updated | "...: Completed"; body is the report, end time, deployment reference or Unknown, counts, Activity links |
| No-op | Started, nothing to act on | "...: No-op" |
| Partial | One step fails, the others run | "...: Partial"; failed step and next owner in the body |
| Two independent runs in the same minute | Each has its own provider id (or its own random token) | Two rows with different Source IDs; neither overwrites the other; business dedupe untouched |
| Retry after an uncertain create response | The run queries its own Source ID before writing again | One row: reused if the create landed, created if it did not; no business step repeats |
| New run after a crash | The crashed run's row stays "Started" (unconfirmed); the new run has a new id | A new row; the old one is never reused or rewritten |
| Report write fails | Retried once, then carried on; failure in the chat report | No business action repeated; the record may be missing or stuck at Started |

Exclusions are unchanged:
- No People, Engagement, Deal or Episode link.
- The Summary starts "Run", so it is outside the "Zoya sent" and "Agent sent" cap counts.

The records show in Activities, view "Routine outcomes" (Kind Note, Source ID starts `run:`).

## Prompt bytes after Stage B v2 plus AR-8 v2

| Prompt | Bytes | sha256 | Spare to 65,536 |
|---|---|---|---|
| inbox | 64,607 | e8c4a6a298061e42 | 929 |
| zoya | 40,333 | c5de7652116d94c5 | 25,203 |

The inbox spare is tight. The simplification task (sender and eval context consolidation) is where it gets room back.
