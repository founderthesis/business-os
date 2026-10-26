# Keying migration dry run (decision 394), 26 Oct 2026

Read-only. Nothing was sent, drafted or written to Notion. Output: `keys-migration.csv` (155 segments on 155 rows). Generated twice from the same data by one script; the two files are byte-identical.

## Procedure (re-runnable)

1. Read `docs/proposals/d394-migrate.md` and the key format in `routines/zoya/parts/actions.txt`.
2. Select Engagements (collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5) by SQL: Status not in They declined, We declined, Parked, Unresponsive (empty Status kept); Task state not Done or On hold; Next action LIKE '%Zoya%' OR Waiting on LIKE '%Zoya%'. Page with LIMIT/OFFSET ordered by url. Result: 163 rows.
3. Split Next action on " | ". A segment starting "Zoya: " is a Zoya segment. Any other segment that contains a Zoya step ("then Zoya tells", "Zoya chases", "Zoya reconnects", "Zoya follows up there") is a rule 7 case.
4. Apply the rules in order, first match wins:
   - Rule 1: "Zoya: back to Akshay on" keeps its form, no key.
   - Rule 2: "<routine> step n", "sponsored step", "precall step", "recording step", "form chaser n". Routine from the wording (sponsored 1, precall 2, recording 3, form 5). n from the wording, else Chase step + 1 (empty Chase step counted as 0). Date: the segment's "on <D Mon>" (year 2026, or 2027 for Jan), else "original due", else the row's Next date.
   - Rule 3: segment wording contains "nurture". n = "Zoya sent: nurture" Activities linked to the row dated on or after the "(since <date>)" start, plus 1. Date as rule 2 (d394 gives no date source for rule 3).
   - Rule 4: a reply owed to an inbound. Find the inbound Activity (Kind Email in, Source ID gmail:<id>), fetch it with Gmail get_message RAW, decode the Message-ID and Date headers, convert Date to +09:00. Message-ID stored without angle brackets.
   - Rule 5: a step that comes from an "Akshay's call" line in Claude note. Origin call-<Activity id>, else call-<row id>. Raised = that Claude note line's date.
   - Rule 6: anything else. Origin call-<row id>; raised = the newest Claude note line's date.
   - Rule 7: split the Zoya step into its own segment, key it by rules 1 to 6, flag for review.
5. Activities checked: every "%nurture%" Summary (7 rows; 4 are "Zoya sent: nurture 1", on Annanya, Manoj Meena, Akshit Chaudhary, Patrik Antoni), and all Activities on the 5 rule 5 rows and the 6 rule 4 rows. No Activity records an Akshay decision, so every rule 5 origin is call-<row id>.
6. Write the CSV with `scratchpad/build_keys.py` (the classification table is in the script), run it twice, `cmp` the outputs, and grep the file for address and phone patterns (only Message-IDs match).

## Counts

163 rows selected. 155 carry a Zoya segment or a rule 7 Zoya step (one each). 8 rows matched only because "Zoya" appears as a name, not a step, and are not in the CSV: Sumit Gupta FT (3f019a301a7f8176b083da416ac23077), Pritesh Mohite (3f019a301a7f8197949de4a246ea8ea1), Curious Junior (40119a301a7f81d5b6cffbd9517e0a57), transcript rows for Matthew Spacie, Sanjay Varnwal and Rohan Ganapathy (Waiting on Ranjita; "Zoya" is who asked), and the two Builder tasks (3fc19a301a7f8181b57ddf15e17b362d, 3ff19a301a7f81719cc7dfed5358c0f9; the 360 task describes a future Zoya behaviour, not an open step).

By type: followup 107, nurture 20, team 7, reply 5, decision 5, unkeyed 11 (9 snoozes, 2 review). 144 keys, all unique.

By rule:

| Rule | Segments |
| --- | --- |
| 1 snooze | 9 |
| 2 literal | 88 |
| 2 by extension | 16 |
| 3 literal | 13 |
| 3 over 2 (Rakshith) | 1 |
| 3 by extension | 4 |
| 4 | 5 |
| 5 | 5 |
| 6 | 7 |
| 7 then 2 (extension) | 3 |
| 7 then 3 (extension) | 2 |
| 7 then 4 (unkeyed) | 1 |
| 7 pointer (unkeyed) | 1 |

Rule 4 Message-IDs resolved first try for 5 of 6; the sixth (Pragatti, Mandar's row) was raised on WhatsApp and has no Message-ID.

## Review list (34)

- Mandar Dandekar @ Sorin Investments, Founder Thesis (3ed19a301a7f81249675cb216e4325bb), rule 7 then 4: (unkeyed): rule 7, Zoya step inside Sarika's segment; rule 4 reply owed to Pragatti, but her ask came on WhatsApp 21 Oct (Activity wa:...:2026-10-21), so there is no Message-ID. Waiting on lacks Zoya.
- Shruthi Cauvery Iyer @ Vaia, Founder Thesis (3f019a301a7f810989d7e64802788b69), rule 7 then 2 (extension): rule 7, Zoya step inside Divyanshi's segment (edits another owner's text). 'chases' is not rule 2 wording; routine 2 from the precall; Chase step empty so n=1; 'from 24 Oct' is not 'on <D Mon>', so date is Next date.
- Paritosh Ladhani and Alka Ladhani @ Taj Agra, Founder Thesis (3f019a301a7f81168d30c7a24f81bf14), rule 2 (extension): precall booking chase without rule 2 wording; routine 2; Chase step empty so n=1; no 'on' date, so Next date.
- Sinduri Reddy @ Premia Academy, Founder Thesis (3f019a301a7f81178bd4ea089dfa2cf2), rule 6: check-in to PR about billing details (invoice hold); no rule 2 wording, not a reply owed (Zoya replied 22 Oct), so rule 6 team (actions.txt lists billing asks as team). Could be read as routine 4 misc chase.
- Nikita Kumawat @ Brandworks Technologies, Founder Thesis (3f019a301a7f812291c7e824de67fbc0), rule 7 then 3 (extension): rule 7, Zoya step inside the Waiting on Ria segment. LT chase row; revisit/check-in/chase wording is not rule 3's 'nurture' wording; keyed as nurture (routine 7) by extension, n from 'Zoya sent: nurture' Activities + 1. Literal reading drops it to rule 6 team. No 'on' date, so Next date.
- Ankush Tiwari @ pi-labs.ai, Founder Thesis (3f019a301a7f812d8f24e8b4b7dbec9a), rule 5: generic step; the decision mail it follows was sent 26 Oct (msgid 70008c86...), so it may already be complete. Two 'Akshay's call' lines dated 25 Oct; date is the same either way.
- Ankit Utreja @ WebEngage, Founder Thesis (3f019a301a7f813287bbf83d4112e716), rule 5: chase wording (could be rule 2 by extension, routine 2) but the wording names Akshay's call, which literally matches rule 5.
- Naresh Kumar Kumawat @ Internationally Acclaimed Sculptor, Founder Thesis (3f019a301a7f8143ad15c89c1bcd4418), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1.
- Navneet Chitkara @ Vyasa Astro, Founder Thesis (3f019a301a7f8145b49fec5f61d1beb6), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1.
- Rakshith Rangarajan @ Inviga Healthcare Fund, Founder Thesis (3f019a301a7f81579a79c1503c3e4ed5), rule 3 (over 2): the segment literally contains 'precall step 3' (a step already sent, in parentheses), which rule 2 checks first and would key as seq-2-3; keyed as nurture because the step itself is the move to nurture.
- Arushi Kapoor @ The Agency Art House, Founder Thesis (3f019a301a7f815d93a8efad4fbeffac), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1.
- Shekar Swamy and Srinivasan K. Swamy @ R K Swamy, Founder Thesis (3f019a301a7f8161b326f5f8ff5da05a), rule 2 (extension): 'follow-up' names no routine; routine 2 taken from Status Precall requested; Chase step empty so n=1.
- Praveen Gadelli @ STEMLearn.AI, Founder Thesis (3f019a301a7f8166bbd6ea76681505df), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1.
- Ishank Joshi @ Mobavenue, Founder Thesis (3f019a301a7f81688a10fb6d95f13243), rule 3 (extension): LT chase row; revisit/check-in/chase wording is not rule 3's 'nurture' wording; keyed as nurture (routine 7) by extension, n from 'Zoya sent: nurture' Activities + 1. Literal reading drops it to rule 6 team. Could instead be routine 2 (precall dates). 'next check-in 27 Oct' has no 'on', so Next date (same day).
- Madhu Sudan @ ShelfRadar AI, Founder Thesis (3f019a301a7f816f846df7e22a23f8ad), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1. No 'on' date, so Next date.
- Joseph Sudheer Reddy Thumma @ Magellanic Cloud Limited, Founder Thesis (3f019a301a7f8172b556c68bdac66799), rule 2 (extension): 'precall chase' names routine 2 but is not rule 2's 'precall step'; Chase step empty so n=1.
- Yash Varyani @ Drizz, Founder Thesis (3f019a301a7f8182b156dca9050b3659), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1.
- Mohit Bedi @ Kiwi, Founder Thesis (3f019a301a7f81c1b612e8d8fb17c27a), rule 3 (extension): LT chase row; revisit/check-in/chase wording is not rule 3's 'nurture' wording; keyed as nurture (routine 7) by extension, n from 'Zoya sent: nurture' Activities + 1. Literal reading drops it to rule 6 team. The wording says check-in 2 (the 16 Oct check-in was not logged as 'Zoya sent: nurture'), but rule 3 sets n from Activities, so n=1.
- Raj Gokal @ Solana, un# (3f119a301a7f81218259fc7549b9aad0), rule 3 (extension): LT chase row; revisit/check-in/chase wording is not rule 3's 'nurture' wording; keyed as nurture (routine 7) by extension, n from 'Zoya sent: nurture' Activities + 1. Literal reading drops it to rule 6 team.
- Director (name not given) @ Lighthouse Info Systems, Founder Thesis (3f119a301a7f8170bbcaef18f8050a0b), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1.
- George Kikvadze @ Bitfury, un# (3f119a301a7f81a697ddc3ae930bc422), rule 3 (extension): LT chase row; revisit/check-in/chase wording is not rule 3's 'nurture' wording; keyed as nurture (routine 7) by extension, n from 'Zoya sent: nurture' Activities + 1. Literal reading drops it to rule 6 team.
- Erik Voorhees @ Venice.ai, un# (3f119a301a7f81cba216d11b021aec16), rule 6: an outreach mail to the guest gated on Akshay's open ask; no follow-up or nurture wording, no inbound, no Akshay decision yet, so rule 6 team by fallback. Better fit may be nurture (LT chase) once Akshay answers.
- Kuberns founders (names not given) @ Kuberns, Founder Thesis (3f119a301a7f81cd9ca1ca1d4a159e78), rule 2 (extension): 'sponsored follow-up' names routine 1 but is not rule 2's 'sponsored step'; n = Chase step 1 + 1 = 2.
- Vivek Desai @ HOSMAC, Founder Thesis (3f219a301a7f815e8d20d3583af31ee2), rule 7 then 2 (extension): rule 7, Zoya step inside the Waiting on Hasti segment. 'chases' is not rule 2 wording; routine 2 (precall rebook); Chase step empty so n=1; no 'on' date, so Next date.
- Sonu Kumar Yadav @ Hospitalstore.com, Founder Thesis (3f319a301a7f8175b9a6f78f2d4a2d8a), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1.
- Nitin Kaushal @ SFK Group, Founder Thesis (3f319a301a7f81779aafea9e5cd2ed67), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1.
- Harpreet Singh and Abhinav Awal @ F2 Fintech, Founder Thesis (3f319a301a7f81ee896fecd3eb44cae4), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1.
- Pavan Kosaraju @ AquaExchange, Founder Thesis (3f419a301a7f8178ba37c93bbfc9615b), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1.
- Vaibhav Krishnaswamy @ TempeWala, Founder Thesis (3f719a301a7f811bb337cc7950096d8a), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1.
- Manan Thakkar @ Prozeal Green Energy, Founder Thesis (3fa19a301a7f81508e24e25202d1e571), rule 7 then 3 (extension): rule 7 (this is the rule's own example). LT chase row, so keyed as nurture by extension (chase wording, not 'nurture'); could equally be routine 2 seq-2-1 (an active precall-date ask). 'chases 29 Oct' has no 'on', so Next date (same day). Waiting on lacks Zoya.
- Anirudh Damani @ Artha Group, Founder Thesis (3fa19a301a7f81d1acc4c52ac663ef31), rule 7 then 2 (extension): rule 7, Zoya step inside the Waiting on Sakshi segment. 'chases' is not rule 2 wording; routine 2 (planning call rebook); Chase step empty so n=1; no 'on' date, so Next date. Waiting on lacks Zoya.
- Task: chase the deals pipeline (Manu Iyer, Shubham and Som) (3fc19a301a7f815aa863d9bb5772afcb), rule 6: chase wording on a Task row with no Status; no routine named, so rule 6 team by fallback. Could be routine 4 misc chase (no step number to key it).
- Sukant Kumar @ Sunday Labs, Founder Thesis (40419a301a7f8108a357cafb73469297), rule 4: Akshay's 25 Oct 22:44 JST mail (reverse proposal, booking link) may count as the answer to Sukant's next-steps ask; if it does, no reply is owed and the step falls to rule 2 extension or rule 6.
- Sumit Gupta @ CoinDCX, Built to Share (a7d41a8538394ec9b148c13aa4824052), rule 7: (unkeyed): rule 7, a Zoya step inside a pointer segment; it points to the FT row (3f019a301a7f8176b083da416ac23077), whose Next action has no Zoya segment (only 'Waiting on Sharjil ... Zoya on the thread'). Nothing to key on either row until someone writes the FT follow-up step. Waiting on is empty.

Rows marked "note:" in review_flag (14) are keyed by a literal rule match and need no decision; the note records context (Waiting on missing Zoya, a rule-order tie, a step that may already be done).

## Judgement calls

1. Follow-up wording outside rule 2's list. "sponsored chase" (11 rows), "sponsored follow-up", "precall chase", "follow-up", "get the precall booked", "chases" are keyed as rule 2 with the routine the wording names (or Status Precall requested for the bare "follow-up"), and flagged. Read literally they fall to rule 6 team, which would move live sponsored and precall chases into the team type.
2. LT chase revisits ("revisit", "re-approach", "LT check-in 2", "next check-in", "reconnects", "Zoya chases" on an LT chase row) are keyed as nurture seq-7 by extension and flagged. Rule 3 says only "nurture wording".
3. Rule 3 has no date source. I used rule 2's chain (segment "on" date, else original due, else Next date).
4. Mohit Bedi says "check-in 2"; rule 3 counts Activities, so n=1. Flagged.
5. Rakshith's segment contains "precall step 3" in a parenthetical about a sent step. Rule 2 would match first; keyed by rule 3 (the step is the move to nurture) and flagged.
6. Mukund Jha and Tanuj Shori carry both nurture wording and "(Akshay: chase)": rule order gives rule 3.
7. Mekin and Sukant also follow Akshay's calls; rule order gives rule 4. Release-date steps (Vineet, Anmol, Srinivas, Mandar) are replies owed: the earlier answers were holding replies, which answer nothing under actions.txt.
8. Sukant: Akshay's 25 Oct reverse-proposal mail may already answer the next-steps ask. Kept rule 4, flagged.
9. Rule 6 raised time uses the newest Claude note line's date (rule 6 doesn't say which line). Rule 5 uses the line recording Akshay's call.
10. Empty Chase step counted as 0 (n = 1).
11. Message-IDs are stored without angle brackets, as the bare header value.
12. Rule 7 rewrites keep the other owner's words as found, minus the Zoya clause; the Zoya clause becomes "Zoya [...]: <its own words>". Mandar's split is written unkeyed.
13. The "Zoya confirms the date in writing" inside Anil Kumar's snooze is part of the snooze text, not a rule 7 step.
14. Status-free Task rows: two rule 5 (Akshay's 18 Oct calls), two rule 6.
15. The key column holds the full key "<row id>:<type>:<origin>:<raised>"; new_segment carries the short form.
