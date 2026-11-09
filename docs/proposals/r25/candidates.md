# r25 candidates (parked, nothing built)

- **TOP: calendar sync quits early** (CTO, 9 Nov 23:35 JST). The 22:36 and 16:35 runs both stopped after the heavy reads. The diagnosis and proposed fix are in calendar-early-exit.md. Waiting on the CTO's yes.

- **Decision 526, rename:** the Episodes property "Working doc" is now "Copywriting doc" (CTO, 9 Nov; links kept). The only repo file that names it is docs/proposals/r24/zoya/zoya-episodes.txt, the episodes build, which isn't live. Rename it there the next time that build is touched. No live routine references it.
- **Decision 526, archive mail:** after the last Team tasks step (publish Insta), Zoya mails Sarika so she can decide on Archived. It's a candidate for r25 and isn't built yet.
- **Decision 521, stage 3:** drop the old "Dossier link" name from the dual wording once the CTO's stage 2 rename is done and checked.
- **Cleanup r24 item 9, minor:** say that " || " splits only a WhatsApp draft Zoya wrote, so a quoted text from Akshay that contains it goes as he wrote it.

## Added 9 Nov (CTO)

- **Run records for WhatsApp, calendar and the sweep.** Give each one a RUN RECORD like Zoya's: a "Run <routine> <start> JST: Started" Activity, then its status from STATUS IN CODE. Today a check can only see each routine's last run. The WhatsApp 17:47 run on 9 Nov ended "Failed: early exit: 0w, 2b, 3, 3d, 4"; STATUS IN CODE caught it, but nothing shows whether it repeats. Calendar would also need a status step, since it has none yet.
- **Zoya's note re-read must be a page fetch.** On 9 Nov, 5 of 6 Claude note checks re-read the note with SQL (the 11:09 SLOW run did the same). CLAUDE NOTE WRITES says to "re-fetch the row" for N2, which a run can read as SQL. Proposed wording, in the hourly, the SLOW task and the SLOW file: "after the write, re-read the row with notion-fetch (never SQL, rows mode or a preview: SQL drops rich text, so N2 would compare a flattened note) and assert ...". The hourly has 22 bytes to spare, so this has to come with a cut.
- **Evals must cite every figure.** The FT guest evals run at 09:25 said its figures came "from search-result titles and my own recall". The cause is the **ft-guest-eval skill**, not the Cowork task (routines/cowork-evals.md says nothing on sources and just runs the skill):
  - SKILL.md line 115 asks for "the source and year next to every number";
  - line 240 lets unverified figures through as "(uncertain)";
  - neither forbids search-result titles or memory.

  Proposed skill edit, built and uploaded like skills-521: every figure comes from a page opened in this run (Tracxn, a filing, the company's own site, a news article) and names it; a search-result title or snippet isn't a source, and memory never is; with no opened page, write "Not disclosed", never a recalled number marked "(uncertain)". Check un-guest-eval, bts-guest-eval and hbd-guest-eval for the same gap, and give the Cowork task a report line listing any figure left without a source.

## Added 9 Nov 21:30 JST (CTO; r24 deployed and byte-verified, docs/deploys/2026-11-09-r24.md, pin 1556243)

- **Rules for Zoya, section 3, Saurabh's forwards.** Two lines there are older than decision 517: "Thanks for sharing, SG", and Cc everyone except Saurabh. They contradict section 2's decision 517 exception, which keeps him in Cc on his own chain. In r25, write the replacement wording for section 3 so it matches: on a pitch Saurabh forwarded, the loop-in is "thanks SG, looping in Zoya" on his forward, and Zoya replies on his chain To the pitcher, with Saurabh and Akshay in Cc. On any other thread he's never copied. It's a Controls page edit for the CTO to paste, so no build.
