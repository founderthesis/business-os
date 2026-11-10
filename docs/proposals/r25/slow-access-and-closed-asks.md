# Zoya SLOW access failure, and asks hidden on closed rows (r25, diagnose and propose only)

Main, 10 Nov ~14:50 JST, for the CTO's 14:40 ask. Read-only: nothing built, nothing deployed, no Notion write.

## 1. Zoya SLOW: ACCESS_DENIED at 08:08 and 11:08 JST

**r24 isn't the cause.** The r24 SLOW task (15,949 / 595f107f, live since 9 Nov 21:04) differs from r23 only in text:
- the pin and sha (1556243, b6d1c52b);
- the lock wording (decision 415 citation, "sleep 5" re-push);
- two shortened citations.

It names no model, connector, permission or account; its only mention of a model is PREFLIGHT's "the model you run on". The model is a trigger field (claude-opus-5-5, decision 450), and the prompt deploy didn't change it.

The failure also comes 7 seconds in, with "oauth_org_not_allowed" ("Your organization has disabled Claude subscription access for Claude Code"). That's before the prompt's first tool call, so it's refused at the account and model level. That fits an org setting that now blocks Opus under the subscription, while the routines on the default model run fine.

**Fallback, for Akshay's yes (it changes decision 450):**

> Zoya SLOW runs on the default model (Sonnet) until Opus access returns; the CTO switches it back the same day (decision 450 stands, suspended).

The CTO's single call once he says yes is `update_trigger trig_015i1JzfyNDoYfrgTfbqDSXu model=claude-sonnet-5-5`, with no prompt change. The SLOW task and file carry no Opus-only assumption. Its 22-minute stop, chunking and OUTCOME CHECK IN CODE are model-independent. The run record's PREFLIGHT line reports the model, so the switch shows in the first record.

Watch for one thing on Sonnet: the SLOW file is 93,319 bytes, loaded in 20,000-character slices. The first record's "slow file: <read> of <total>" line confirms the load completed.

Log it as a decision row ("SLOW on Sonnet while Opus access is off, <date>") and, once access returns, as its reversal.

## 2. Asks hidden on closed rows

**The cause:**
- Akshay's queue (the "AD: all shows" view and the WhatsApp brief's definition) excludes They declined, We declined, Parked and Unresponsive.
- A routine can add an "Akshay:" segment to a row at one of those statuses without moving its Status, and then he never sees it. That's what happened with Kuberns on 6 Nov.

**Today's rows** with Akshay in Waiting on and a closed Status (read 10 Nov, 13 rows; Kuberns is already fixed). I've sorted them by what the Next action says. The CTO decides each one.

**A real ask for Akshay that he can't see (Decision pending, as with Kuberns):**
- Chris George @ QubeHealth (FT, Parked): "Akshay: send Chris the India CHRO show proposal (promised 23 Oct...)". This is a PaaS-type promise; consider moving it to Show PaaS.
- Sukant Kumar @ Sunday Labs (FT, Parked): "Ask Akshay: verdict after the 27 Oct precall ..."
- Fisher Yu @ Babylon (un#, They declined): "Ask Akshay: Dillon Arace (M Group) asks for a date for Fisher ..." (26 Oct)
- Ramakant Yadav @ Scalar Field (FT, They declined): "Akshay: send Ramakant intros ... (asked on 6 Nov precall)"
- Sam Hallene @ CMT Digital (un#, We declined): "Akshay: Zoya has no un# decline for Sam Hallene ..."
- Gaurav Dagaonkar @ Hoopr.ai (Built to Share, Unresponsive): "Akshay to re-engage him on the Next date"
- Anuj Tandon @ BITKRAFT Ventures (FT, Parked): the open step is Sarika's edit change, and Akshay is one of four in Waiting on. Check whether anything of his is left.

**Leftovers: closed, with nothing of Akshay's left (take Akshay out of Waiting on, no status change):**
- Evan Cheng @ Mysten Labs (un#, We declined): "Sri's call on the board: eval says Decline"
- Konstantin Shulga @ Finery Markets (un#, We declined): "Declined by Ravi"
- Sergej Kunz @ 1inch (un#, We declined): "Ravi declined the guest"
- Ivan Titov @ University of Edinburgh (Human by Design, We declined): "Akshay: let the December check-in lapse with a thank-you". It's his only if he wants the thank-you; otherwise close it.

**Kind Task rows parked on purpose (leave them):**
- Task: invite Sri, Satish and Arjun to their host boards (Parked)
- Task: upload the un#, Built to Share and Human by Design eval skill zips (Parked)

**Proposed r25 rule. I'd do (a) and keep (b) as a guard:**

- **(a) Widen the queue, in one place.** Akshay's queue becomes "Waiting on contains Akshay, any Status" in the "AD: all shows" view and the WhatsApp brief's definition, with Kind Task rows at Parked left out. It's one view filter plus one definition, with no prompt in six routines to change, and it can't miss a writer we forget. The leftovers above would surface once and get cleaned. This needs a Notion view edit by the CTO.
- **(b) The CTO's rule, as a guard:** any routine that adds an "Akshay:" or "Ask Akshay" segment to a guest row at They declined, We declined, Parked or Unresponsive also sets Status to Decision pending in the same write, with a Claude note line "YYYY-MM-DD: <old status> -> Decision pending (Akshay ask added)". The writers are inbox actions (STEP 3's repeat pitch already does this; STEP 5's ask bullets don't), the sweep (STEP 4), WhatsApp 2b, host boards STEP 1 and the Zoya hourly and SLOW. That's about 150 to 200 bytes each. The hourly is 22 bytes under 63,000, so its share needs a cut.

With (a) alone, a closed row can still carry a live ask, but Akshay sees it. (b) also makes the Status say so. If only one gets built, (a) is cheaper and catches every writer.
