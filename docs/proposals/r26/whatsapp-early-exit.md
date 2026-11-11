# r26: WhatsApp STEP 0w has never sent (three early exits), plus two holds

Main, 11 Nov ~22:00 JST, for the CTO's ask. Built on the r25 WhatsApp (39,065 / ddb69276), not deployed.

## What the runs show

| Run | Length | What it did |
|---|---|---|
| 20:48 JST (cse_019pwcV2PbeFtMUDnyiU33m7) | 2 min, 160k context | ran 0, 1, 2, 2b; skipped 0d, 0w, 3, 3d, 4 |
| 21:46 JST (cse_019pwcUzzuMxCKXNfVSKKLJ6) | 2 min, 24 turns | listed 11 ticked drafts in 0w, sent none, ran no checks; wrote "Failed (early exit: 0w, 2b, 3, 3n, 3d, 4)" by hand, no status script |

I still can't read run events from this session; this rests on the CTO's reading of the 21:46 run and the session records.

**Diagnosis:**
- **The status is a label, not a gate.** The prompt says the first line is copied from the Bash step's output. The run skipped the step and wrote it itself. Nothing in the prompt makes "Failed before minute 25" send the run back.
- **0w is the heaviest step, and it comes first.** Each ticked draft needs a NO REPLY read across two inboxes, the WhatsApp chat and Activities, plus the number, cap and 7-day checks. That's 11 drafts at once, on the first live run after a backlog of ticks. The run listed them, saw the size of the job and stopped. That's the same shape as the hourly and calendar exits.

## The fix (built)

1. **GATE**, after the status rule: "never rewritten or written by hand. GATE: run that step before this report; while it prints Failed and `date -u` shows under 25 minutes since the start, report nothing: go back to the first step it names, work it, and run it again."
2. **0w takes at most 5 drafts a run, oldest tick first.** The rest wait, and the step line reads "cap: 5 a run", which the status script already accepts as Partial.
   - This makes the job small enough to finish. A backlog of 11 clears in three hourly runs.
   - It's still 5 sets an hour, well inside the 20-a-day cap.
3. **HIS OWN MESSAGE** (CTO gap 2, Chris George): if a message from his number is in that chat since the draft was written (that day counts), and no wa-send Activity logs it, the draft is held. Nothing is sent, the box is unticked, and his list gets "Akshay: you messaged <first name> since the draft; held (<D Mon>)". Our own sends are excluded because each one is logged in a wa-send Activity.
4. **GREETING** (CTO gap 1, Bhavin Turakhia's "hi Rohit"): if a greeting in the draft names someone other than the recipient, the draft is held, the box is unticked, and his list gets "Akshay: draft addressed to <name> but goes to <recipient> (<D Mon>)".

**WhatsApp is now 39,817 / c0ac14891bb14218.** Built twice, byte-identical, no new em dash. Build: `python3 docs/proposals/r26/patch.py wa docs/proposals/r25/whatsapp.txt <out>`.

## What I'd check on the first live run

- The run record's step lines come from the script, and the first line matches its output.
- 0w handles at most 5 drafts: sent, or held with a named reason.
- Bhavin and Chris are unticked now, so they won't test the holds. A fresh greeting mismatch is the cleanest test: a ticked draft saying "hi <someone else>" on a test row.

## Can r26 land before 08:00 JST tomorrow?

From Main's side, yes for WhatsApp, inbox actions (decision 557) and the Zoya decision 555 build: all are built and pushed. It then needs Cleanup's delta review and the CTO's deploy.

The one thing not built is the early-exit gate in the Zoya hourly (and SLOW's :30 stop). The hourly has 10 bytes to spare, so the gate needs about 230 bytes of cuts. On the CTO's yes I can build that within the hour, or it can ship as r26b without holding up WhatsApp.
