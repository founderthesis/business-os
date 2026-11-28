# Cleanup verdict: inbox split round 3 (219d0ee), 1 Nov

**Not accepted.** Four items block it. Each is a short wording fix, so round 4 should be small. Nothing is deployed, and the live inbox stays disabled at 65,227 / 3bb46f9332241e3b.

Replays: `cleanup/round3/closure.json`, which runs one case per round 2 item, and `cleanup/round3/newholes.json`, which diffs round 2 against round 3.

## Rebuilt twice, byte-identical, hashes match

| File | Bytes / sha256 |
|---|---|
| capture.txt | 35,029 / 4cbe89dfde09147c |
| actions-v2.txt | 38,584 / b6e90754d9823051 |
| yourcall-sections.md | 7,326 / a28b43da3b0aac36 |
| sweep.txt (on d420 06c4120b) | 39,131 / 6783dd01e396e5ab |
| actions.txt (v1, not for deploy) | 45,117 / f404fa8f19d7ef16 |

There are no em-dashes in the prompts. Completeness: 35 source units are absent, against 25 in round 2. All 10 new absences are rewrites the README names. Five of section 8's six bullets are byte-exact. The sixth, recording logistics, was extended for S7, so "word for word" isn't literally true. That's fine, but the README should say so.

## Round 2 items

**Closed (14):** B1, B2, B3, B5, B6, B7, B8, B10, S3, S5, S6, S7, S8, S9.
- **B6:** the last line of `yourcall-sections.md` is exactly "END OF INBOX ACTIONS SECTIONS 6-8". The prompt requires that line and the three heading starts, and nothing else.
- **B1:** actions now reads "the newest inbox actions run record other than this run's that has a "worked to"".

**Partial (5):** B4, B9, S1, S2, S4. They're folded into the list below.

## Blocking

**R1. Zoya's own sends get worked by actions (round 2 S1 reopened, by D9b).**
- Capture's STEP 1 gives "a row without a "capture:" line (another routine logged it first)" that line, and STEP 0 does the same.
- Akshay is in Cc on every Zoya mail (decision 229), so all her sends land in ad@ and get stamped.
- **Failure:** Zoya sends a holding reply at 10:38. Capture stamps it at 11:02. At 11:25 actions' STEP 5 reads it as "a team member closed Akshay's ask" and takes Akshay off Waiting on, so a decision drops off his list. Actions also repeats Status and Waiting on moves Zoya already made, which puts two writers on her rows.
- The old inbox skipped every row whose msgid: was already held.
- **Fix:** the exception covers only Kind Email in rows, never a "Zoya sent:" row, in STEP 1 and STEP 0. Actions closes as n/a any Summary starting "Zoya sent:". That also makes replay3d's N2 nit optional.

**R2. Capture's first run re-stamps the old inbox's work (D3 reopened).**
- CURSOR reads "the newest inbox capture run record" (`run:inbox-capture:`). On the first run there isn't one, so T falls back to "3 days ago".
- D9b's stamps have no cap. Every row the old inbox logged in those 3 days gets "capture:". Those Captured 31 Oct and 1 Nov are inside actions' "Captured on or after the day before W's date" window, so actions works mail the old inbox already worked.
- STEP 1's own wording, "the newest inbox run record that has one", disagrees with CURSOR.
- **Fix:** both say "the newest record with Source ID run:inbox-capture:, else run:inbox: (the old inbox)". D9b's exception covers only rows created since 2026-11-01 12:00 JST.

**R3. A row that crashes the run freezes actions (B4 partial).**
- "actions: try <n>" is written only on a failure the run handles.
- A row whose thread read crashes or times out the run never gets counted. It holds W, and every run crashes on it again.
- **Fix:** write "actions: try <n> <run id>" on the row before starting it. At 3 tries it's stuck, as now.

**R4. "Today" has no timezone, and the cutover depends on it.**
- STEP 0's cut is "Captured before 2026-11-02", and new rows get "Captured: today". The only clock either prompt names is "Bash `date -u`".
- From 00:00 to 08:59 JST on 2 Nov, a literal reading stamps 2026-11-01. Capture's own new rows (created after 1 Nov 12:00 JST) then fall into STEP 0, and rows it stamped come back.
- **Fix:** in both prompts, today = `TZ=Asia/Tokyo date +%F`.
- **Without the fix:** enable capture at or after **2 Nov 09:00 JST**, not "on or after 2 Nov".

## Should-fix

1. **Overlap guard (S2 partial).**
   - "under 45 minutes old" never fires: the previous actions record is about 60 minutes old when the next run starts. Use "under 90 minutes".
   - Actions has no stop before Zoya's :38. Add "start no new mail after :35"; Your call still runs in full.
2. **WhatsApp lost on a crash (S4 partial).**
   - It's logged as "Zoya sent:" before the send, and a crash in between means "it went, don't resend", so it never goes.
   - Log it as "Zoya sending:" and rename it after the send. At the next run, a "sending" row is checked in Blueticks before any resend.
3. **Dead allmail: rows are re-read forever (B9 partial).**
   - "allmail: no Message-ID" rows have no Captured cut, so up to 8 a run come back for good and STEP 0 never ends.
   - Take a marked row at most 3 times, then leave it for the report.
4. **Captured is overwritten (provenance, CLAUDE.md).**
   - "Every row this step touches gets Captured today" loses each old row's capture date.
   - Keep the original date in the body line ("capture: <run id>, first captured <date>"), or select by the stamp instead of Captured.
5. **STEP 0 can use the whole capture slot.**
   - It runs first and STOP TIME is :20, so loop-ins and new mail can wait hours while old rows drain.
   - Add "STEP 0 starts no row after :10".
6. **Fetch cost of the Captured window.**
   - Actions fetches the body of every row Captured yesterday or today, every run.
   - Add "created before 2026-11-02" to that branch, which is the only rows it exists for.
7. **Folded rows re-worked.**
   - A folded row the old inbox already worked gets stamped.
   - Stamp only those created since 1 Nov 12:00 JST.
8. **Loop-ins in a thread.**
   - The loop-in Activity is closed as n/a, but when actions reads a pitch's THREAD, the loop-in message can still read as "our side replied" in STEP 5.
   - Add "a loop-in in a thread is never a reply".

## Cutover notes (the CTO's ask)

- **Actions fails closed without the end line:** confirmed. All three heading starts and the exact end line are required, or actions skips STEP 0 and every mail step and ends Failed.
- **Capture "on or after 2 Nov JST":** right in intent, not safe as worded. See R4: 09:00 JST, unless today is defined in JST.
- **Order:** paste sections 6 to 8 and read them back before actions is enabled.
