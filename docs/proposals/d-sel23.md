# Codex finding 1: missed follow-ups (CTO, 23 Oct)

## Root cause

STEP 2 lists each routine's rows but never says how to pick candidates. Routine 1 already says "whatever Next action says", yet the runs pulled rows by Waiting on (Zoya's queue). So a row Waiting on "Guest or PR" whose Next date had passed was never a candidate. That's the normal state of a row after we send a mail and wait, so every chase on those rows stalled. Zoya's 12:38 run on 23 Oct reported nothing due while 29 such rows were overdue.

## Fix (`d-sel23.py`, not deployed)

The delta adds a SELECT BY STATUS AND DATE paragraph at the top of STEP 2:

- Candidates are in-scope rows at Sponsored offered, Precall requested, Booking, Recorded or LT chase with Next date today or earlier, plus routine 4, 6 and 8 rows.
- That holds whoever Waiting on names (Guest, PR, Zoya, Chaandini or no one).
- Then the existing skips and holds apply.
- An old plan naming a step its routine page no longer has (step R) is worked from Chase step and the thread.
- The report's due count is this selection.

Sizes:

| Prompt | Before | After |
| --- | --- | --- |
| Zoya | 64,340 / 6a82808cd870fbae | 64,959 / 6cd33a24fa8ab061 |

That leaves 377 B under the 65,336 working ceiling.

The same paragraph is in `routines/zoya/parts/followups.txt`. The split rebuilds to:

| Prompt | Bytes / sha256 (first 16) |
| --- | --- |
| FAST | 32,463 / 27ffbf84c540e360 |
| SLOW | 60,668 / 521a2b21c66bb777 |

## The 29 rows (read 23 Oct, Next date on or before 23 Oct, Waiting on Guest or PR)

These are the outcomes the rules give once the fix is live. Zoya's first follow-up run after deploy works them, oldest due first, at most 10 a run (RUN ORDER). Cleanup checks each against its run record.

Expected outcomes:
- **Due:** the 7-day rule and ONE PERSON, ONE ASK are clear on the row, so Zoya sends the next step unless the thread shows otherwise.
- **Hold:** dated.
- **Blocker:** names its owner.

### Precall requested (12)

| Row | Last ask | Expected outcome |
| --- | --- | --- |
| Saurabh Kapoor (Wellbeing Nutrition) | podm.in/30min to Kanika, 15 Oct | Due: precall step |
| Vishal Gupta (MaxVolt) | precall booking to Prity, earlier | Due, but one mail with Mukesh Gupta's row (same PR, ONE PERSON, ONE ASK) |
| Ramakant Yadav (Scalar Field) | podm.in/30min to Chirag, 15 Oct | Due, one mail with Hemant Sood's row (same PR) |
| Hemant Sood (Findoc) | podm.in/30min to Chirag, 15 Oct | Held behind Ramakant's mail to Chirag |
| Ishan Talathi (CloudPe) | podm.in/30min to Suhasha, 15 Oct | Due |
| Sakshi Sukhlecha (Artha) | Zoya replied 22 Oct on the Anirudh Damani row | Hold: ONE PERSON, ONE ASK, recheck 29 Oct |
| Arpit Mittal (SpeakX.ai) | Mamatha chased 22 Sep and 5 Oct (Chase step 2) | Due: step 3 |
| Abhilash Maurya (Naxatra Labs) | dates asked of Kashish | Due |
| Narendra Sen (RackBank) | chased 5 Oct (Chase step 1) | Due: step 2 |
| Ankit Kedia (Capital A) | Ishita to book | Due |
| Mokksh Sani (Living Liquidz) | podm.in/30min to Chaitanya, 15 Oct | Due |
| Gulab Patil (Lemma) | precall on the calendar 23 Oct 22:00 JST | Not due (routine 2 needs no precall on the calendar); Next date moves past the call |

### Sponsored offered (17)

| Row | Last ask | Expected outcome |
| --- | --- | --- |
| Karl Floersch (OP Labs, un#) | unhashed.co/sponsored to Hugh, 12 Oct | Due |
| Pragati Varshney (Brand Buzz) | old "step R" plan | Staleness gate: no step R on sponsored, so it goes to nurture |
| Pavan Kumar (White Lotus) | old "step R" plan | Same as Pragati: nurture |
| Mithun Pangal (VYE) | step 4 needs the due-diligence story | Blocker: Akshay (confirm the story); Akshay goes in Waiting on |
| Mukesh Gupta (MaxVolt) | sponsored-only answer to Prity, 15 Oct | Due, one mail with Vishal's row |
| Vivek Kaimal (Macros) | offer to Kriti, 15 Oct | Due |
| Varun Khare (thumpN) | offer to Manvi, 15 Oct | Due |
| Ajay Gupta (Perceptive Ideas) | offer to Prachi, 15 Oct | Due |
| Sharmishtha Lad (CCCo.) | offer to Divyanshi, 15 Oct | Due |
| Gagandeep Singh (TIC) | commercials, 15 Oct | Due (nurture per decision 158 if the thread says so) |
| Kevin Lepsoe (ETHGas, un#) | Akshay offered 22 Oct | Hold: 7-day rule, recheck 29 Oct |
| Alouk Kumar (Inductus) | Akshay's mail after the 22 Oct precall | Hold: 7-day rule, recheck 29 Oct |
| Bharat Agarwal (AURUS) | negotiation reply to Mahima (Chase step 1) | Due: negotiation follow-up |
| Sunith Reddy (Beforest) | billing details to Siddhi | Due: billing chase (payments) |
| Carson Cook (Membrane Labs, un#) | offer from Mamatha, 16 Oct | Due |
| Mauricio Zolliker (XMAQUINA, un#) | offer from Mamatha, 16 Oct | Due |
| Sushil Patil (Eximple) | covered by Vishesh Jain's row | Not a separate pursuit: skip (Vishesh's row carries it). Cleanup to decide whether to Park it |

Count:

| Outcome | Rows |
| --- | --- |
| Due | 21 (one shared send for Vishal + Mukesh and one for Ramakant + Hemant) |
| Dated hold | 3 |
| Nurture | 2 |
| Blocker | 1 |
| Not due | 1 |
| Duplicate | 1 |

The exact lines come from the run records after deploy.
