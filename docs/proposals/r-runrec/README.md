# R-runrec: a run record for every routine (decision 419)

**Why.** The 12:03 JST inbox run on 28 Oct hit "Resource has been exhausted" on Gmail and logged nothing, yet the scheduler marked it SUCCEEDED. Only Zoya kept a run record, so failures elsewhere stayed hidden.

**What changes:** one minimal patch per live prompt, made by `build.py`.
- **Every routine** gets the same RUN RECORD block, shaped like Zoya's:
  - Kind Note; Source ID `run:<routine>:<session id>`, or a synthetic `syn-...` id when the session id is empty.
  - Summary `Run <routine> <YYYY-MM-DD HH:MM> JST: Started`, then `<Completed|No-op|Partial|Failed>`.
  - Body: the report, the end time, counts, errors as the tool gave them, and what was skipped and why.
  - The record is created before any other Notion write and updated last.
  - A connector, quota or rate-limit error that leaves work undone makes the run Failed, never Completed.
  - A run that stops for a missing tool still writes its record if Notion works.
- **Inbox only:**
  1. A Gmail quota, "exhausted" or 429 error: sleep 30 seconds and retry, then 60 seconds and retry once more. Still failing: no more Gmail calls, finish what needs no Gmail, end Failed.
  2. A narrower read. The start is 30 minutes before the start of the newest inbox run record that ended Completed or No-op. With no such record yet, it falls back to the old rule (one day before the newest Gmail Activity).
     - It doesn't anchor on the newest Gmail Activity, as the CTO's brief put it. Zoya and the sweep also log Activities with Source Gmail, so that anchor can sit after the inbox's last full read and skip mail.
     - A Failed or Partial run is followed by a re-read from the last Completed run, which covers "unless that day hasn't been processed".
  3. "End with a short report, nothing else written anywhere" now reads "written only to the run record".
- **Daily sweep:** its own per-part report Activity (`sweep:<A|B>:<date>`) *becomes* the run record (`Run sweep <A|B> ...`, `run:sweep:<id>`), so each run has one record, not two. The look-up of the previous part's skipped steps reads the new record, falling back to the old Source ID before 29 Oct.

## Coverage and sizes

The cap is 65,536 bytes; the build refuses anything over 65,336 (the cap less 200).

| Routine | Trigger | Input (bytes / sha256) | Output (bytes / sha256) | Headroom |
|---|---|---|---|---|
| Inbox | trig_0189eZvAD8x4357cfevgZ3No | 61,957 / aed0215a8bdf6a26 | 64,109 / 050b0b5fc982106f | 1,227 |
| Calendar | trig_01Voiz5YsK2SnVf2STF8PoSH | 55,082 / 8fb664a1c94776b5 | 56,470 / dae2ee89414b02c6 | 8,866 |
| WhatsApp (live) | trig_01MnmJYorWrd61K7b5BCqXr1 | 26,007 / 9e8b9f4891e9c03d | 27,395 / 092f2daf888ed22d | 37,941 |
| WhatsApp (on B2) | same | 27,969 / 1afc777019d1aefd | 29,357 / 9acff90418414406 | 35,979 |
| Host boards | trig_01K8bueCr2xsPkbgQzjeRKsz | 8,474 / 5819ccf7528ca16f | 9,871 / f9b368bec256b20d | 55,465 |
| Daily sweep | trig_01MdfUFg2qrebDWgiHwncgnd | 33,824 / 7af60faaa021fa64 | 35,171 / 34cfd56fd1d27b52 | 30,165 |
| Evals | trig_01R1yHgEztVEo832zMwUugBr | 14,795 / 1d87f124107a06c6 | 16,174 / 8d10fa55ba5c1cca | 49,162 |
| Dossiers | trig_01WfLf8Zx9c34fSzfrTeUY5M | 5,487 / 68e94cb7d30ca645 | 6,875 / 2be7fcea23ab3d88 | 58,461 |

**The inbox fits with no cut.** 61,957 + 2,152 = 64,109, which leaves 1,227 under the build's limit. That headroom is thin, and the next inbox change will need a cut.

Not covered: Zoya (already has a record), the FT Community directory sync (weekly, not in the brief) and the CTO's own rounds.

## Input provenance: what the CTO confirms at deploy

- **Exact, from the live trigger on 28 Oct:**
  - Inbox and Calendar, from list_triggers.
  - WhatsApp: read back at ea4c8c5. Trigger updated 26 Oct 03:18Z and unchanged since.
- **From the repo copy, matched to live text by distinctive passages, not byte for byte:**
  - Host boards: the prompt block in routines/host-boards.md.
  - Daily sweep: the block in routines/daily-sweep.md, equal to the 25 Oct deploy copy.
  - Evals: routines/cowork-evals.md.
  - Dossiers: routines/cowork-dossiers.md, without its final newline.
  - For these four, the CTO checks the live hash equals the input hash above before deploying. If it differs, `build.py` refuses to run (it asserts the input hash), and the patch is rebuilt on the live text. The anchors are exact-count, so a rebuild is mechanical.
- **WhatsApp ordering:** deploy B2 first, then this patch on top (the "on B2" row). Or apply this to the live prompt if R-runrec goes first.

## Tests

The scenarios are in scenarios.md (R1 to R11). Results are in runA.json and runB.json, two independent offline replays with no MCP calls.
