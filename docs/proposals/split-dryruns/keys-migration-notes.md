# Keying migration dry run (decision 394), 26 Oct 2026

Read-only. Nothing was sent, drafted or written to Notion. Output: `keys-migration.csv` (155 segments on 155 rows, third build). Generated twice from the same data by `docs/proposals/d394-migrate-build.py`; the two files are byte-identical (`cmp` clean, sha256 d837edb3...541b).

The second build folded in replay 1b (`fast-replay1b.md`) and Cleanup's five required changes (`zoya-split-cleanup.md`, last section) and added `waiting_on_add` (a Waiting on option the write adds) and `next_date` (a Next date the write sets). The third build (26 Oct, live re-read) makes the two open owner-field corrections from `d394-migrate.md` and rebuilds the rows that drifted; it adds a last column, `waiting_on_remove` (a Waiting on option the write drops). See "Changes in the third build".

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

Third build (live re-read 26 Oct): 165 rows selected by the same SQL. 151 of the second build's 153 rows are still in scope; Gulab Patil and Subodh Bhardwaj dropped out (see drift). 14 live rows are not in the CSV: the 8 name-only rows below, the 2 AD Personal Task rows (ruling 11), and 4 rows with a Zoya segment the second build lacked, now added (Kumar Abhishek, Ryan Louvar, Robert Mitchnick, Prashant Sachan). 151 + 4 = 155 CSV rows; 151 + 14 = 165.

By type (third build): followup 112, nurture 21, team 8, decision 2, reply 1, unkeyed 11. 144 keys, all unique. 38 REVIEW flags, 19 notes.

| Rule | Segments |
| --- | --- |
| 1 snooze | 9 |
| 2 literal | 85 |
| 2 by extension | 18 |
| 2 release (replay 1b, routine 6 step 0) | 3 |
| 2 replay 1b (Sukant, routine 4) | 1 |
| 3 literal | 15 |
| 3 over 2 (Rakshith) | 1 |
| 3 by extension | 4 |
| 4 | 1 |
| 5 | 2 |
| 6 | 8 |
| 7 then 2 (literal, Vivek Iyer) | 1 |
| 7 then 2 (extension) | 3 |
| 7 then 2 release (Mandar) | 1 |
| 7 then 3 (extension) | 1 |
| 7 pointer (unkeyed) | 1 |
| done by match (Ankush, unkeyed) | 1 |

Other columns: `waiting_on_add` = Zoya on 12 rows; `next_date` on 1 row (Ankit Utreja, 2026-10-27); `waiting_on_remove` = Zoya on 1 row (Ankush Tiwari).

Second build (for the record): 163 rows selected. 155 carry a Zoya segment or a rule 7 Zoya step (one each). 8 rows matched only because "Zoya" appears as a name, not a step, and are not in the CSV: Sumit Gupta FT (3f019a301a7f8176b083da416ac23077), Pritesh Mohite (3f019a301a7f8197949de4a246ea8ea1), Curious Junior (40119a301a7f81d5b6cffbd9517e0a57), transcript rows for Matthew Spacie, Sanjay Varnwal and Rohan Ganapathy (Waiting on Ranjita; "Zoya" is who asked), and the two Builder tasks (3fc19a301a7f8181b57ddf15e17b362d, 3ff19a301a7f81719cc7dfed5358c0f9; the 360 task describes a future Zoya behaviour, not an open step).

By type (second build): followup 112, nurture 20, team 7, decision 2, reply 1, unkeyed 11 (9 snoozes, Ankush done by match, Sumit Gupta BTS pointer). 142 keys, all unique. First build: followup 107, nurture 20, team 7, reply 5, decision 5, unkeyed 11; 144 keys.

Second build by rule:

| Rule | Segments |
| --- | --- |
| 1 snooze | 9 |
| 2 literal | 88 |
| 2 by extension | 16 |
| 2 release (replay 1b, routine 6 step 0) | 3 |
| 2 replay 1b (Sukant, routine 4) | 1 |
| 3 literal | 13 |
| 3 over 2 (Rakshith) | 1 |
| 3 by extension | 4 |
| 4 | 1 |
| 5 | 2 |
| 6 | 7 |
| 7 then 2 (extension) | 3 |
| 7 then 2 release (Mandar) | 1 |
| 7 then 3 (extension) | 2 |
| 7 pointer (unkeyed) | 1 |
| done by match (Ankush, unkeyed) | 1 |

Other columns: `waiting_on_add` = Zoya on 5 rows; `next_date` set on 1 row (Ankit Utreja, 2026-10-27).

## Changes in the third build (26 Oct, live re-read)

Every Engagement in scope was re-read live on 26 Oct (Next action, Waiting on, Next date, Status, Chase step, Claude note; `Zoya sent: nurture` Activities). `old_segment` was checked against the live Next action for all 153 second-build rows with SQL `instr`, plus a pass for empty Next action and closed Status.

### Correction 1: `waiting_on_remove`

New last column. "Zoya" where the migration removes her last segment on a row and no Zoya segment is left. Checked every row whose `new_segment` has no "Zoya" segment against live Next action and Waiting on:
- Ankush Tiwari (3f019a301a7f812d8f24e8b4b7dbec9a): new segment empty (done by match), live Waiting on Akshay, Guest or PR, Zoya, and his other two live segments are Simran's and Akshay's. Set to Zoya.
- Sumit Gupta BTS (a7d41a8538394ec9b148c13aa4824052): the unkeyed pointer stays, and Waiting on is already empty. Nothing to remove.
- The 9 snoozes keep their "Zoya: back to Akshay" segment, so Zoya stays.

### Correction 2: `waiting_on_add`

"Zoya" on every row whose `new_segment` carries a Zoya segment while live Waiting on lacks her (OWNERS). Checked live with SQL over all CSV rows (Waiting on null or without Zoya). 12 rows, 7 of them new in this build:
- Named in the open item: Mithun Pangal (3f019a301a7f819a9d8cd6811838989b), Priya Kumar (3f019a301a7f81b498c2ec93a4c40b42), Rick Yvanovich (3ff19a301a7f81a8a754c14597421e3e), Dinesh Yadav (40019a301a7f81449b93c57ac653185a). Gulab Patil (3f419a301a7f8159a4c5de09d3408489) was named too, but his row has drifted out of scope (no Zoya segment left live), so it is dropped, not added.
- Found by the live check: Akshit Bansal (3fb19a301a7f817bab3df7c45662370b, Waiting on Guest or PR), and two drift rebuilds: Matthew @ Magic Bus (3f019a301a7f81bd9ed6c7020bf96f3d, Waiting on Akshay, Guest or PR) and Vivek Iyer (40119a301a7f810e88a9ecb971df8966, Guest or PR).
- Kept from the second build (rule 7 rows): Mandar Dandekar, Shruthi Cauvery Iyer, Vivek Desai, Manan Thakkar, Anirudh Damani.
- Not added: Sumit Gupta BTS (pointer, no Zoya step). The 4 rows added for drift already have Zoya in Waiting on.

### Drift (live vs file)

`old_segment` no longer matches live Next action on 5 rows:
- Nikita Kumawat (3f019a301a7f812291c7e824de67fbc0), known: now "Zoya: nurture Nikita Kumawat: ... reconnect on 3 Jan 2027 (since 5 Oct 2026)". Rebuilt as rule 3 literal, `nurture:seq-7-1:2027-01-03T00:00:00+09:00` (0 nurture Activities since 5 Oct; date from the segment's "reconnect on 3 Jan 2027").
- Matthew @ Magic Bus (3f019a301a7f81bd9ed6c7020bf96f3d): "form chaser 1 on 2 Nov (7 days after the 26 Oct heads-up)" became "form chaser 1 on hold until this is decided", behind Akshay's re-record question. Rebuilt rule 2 literal, `followup:seq-5-1:2026-10-29T00:00:00+09:00` (no "on" date, so Next date); Zoya added to Waiting on.
- Vivek Iyer (40119a301a7f810e88a9ecb971df8966): the separate "Zoya: sponsored step 1 on 2 Nov" segment became "...; Zoya: sponsored step 2 on 2 Nov" inside Deepayan's segment. Rebuilt rule 7 then 2 literal, `followup:seq-1-2:2026-11-02T00:00:00+09:00`, split into its own segment; Zoya added.
- Gulab Patil (3f419a301a7f8159a4c5de09d3408489): no Zoya segment left (Akshay: Merlin's 6 Nov slot), Waiting on Akshay. Out of scope; removed from the file.
- Subodh Bhardwaj (3fa19a301a7f8118a06aea18fea5d7f9): They declined on 26 Oct, Next action empty. Out of scope; removed.

Live Zoya segments missing from the file:
- SREEPRIYA NS (3f019a301a7f8178a813c5ef91b8a76f), known: her Zoya segment has gone again (the 23 Oct recording was confirmed; Next action is now Akshay's review question, Waiting on Akshay). Out of scope; no row.
- Kumar Abhishek (3f019a301a7f81b7b36fcda18664be04), known: added, rule 3 literal, `nurture:seq-7-1:2026-11-04T00:00:00+09:00` (0 nurture Activities since 19 Aug; Next date).
- Ryan Louvar @ WisdomTree, un# (3f019a301a7f81d7beffc35bc93cab2b), new: "Zoya: fix: no email for the guest (Ryan Louvar's People row)". Added, rule 6 team, `team:call-<row id>:2026-10-12T00:00:00+09:00` (newest Claude note line naming the fix, ruling 4).
- Robert Mitchnick @ BlackRock, un# (3f119a301a7f81018735ed9be408e9e1), new: "Zoya: followup for precall". Added, rule 2 by extension (ruling 1), `followup:seq-2-1:2026-10-27T00:00:00+09:00`.
- Prashant Sachan @ AppsForBharat, BTS (3f119a301a7f819f9a19f9f8a97ddb3e), new: "Zoya: chase Vineeta for the higher-resolution photo and transcript feedback (promised by 19 Oct)". Added, rule 2 by extension, routine by Status Recorded (5), `followup:seq-5-1:2026-10-16T00:00:00+09:00`. The date is the stale Next date (the recording time); routine 4 misc may fit better. Both flagged.

All 7 rebuilt or added rows are flagged "REVIEW: rebuilt for drift 2026-10-26" and listed below. The other 148 rows match live text exactly.

## Changes in the second build (26 Oct)

Cleanup's five changes, applied in the generator and regenerated:

1. Replay 1b folded in.
   - (a) Sukant Kumar (40419a301a7f8108a357cafb73469297): the reply is complete by Akshay's 25 Oct mail. The segment is now `followup:seq-4-1:2026-10-30T00:00:00+09:00` (routine 4 misc chase), step "follow up Sukant on Akshay's 25 Oct reverse proposal on 30 Oct". Rule "2 (replay 1b)".
   - (b) Ankush Tiwari (3f019a301a7f812d8f24e8b4b7dbec9a): Zoya segment dropped. New segment and key empty, rule "done by match", flag notes the 26 Oct decision mail. His Waiting on still lists Zoya; with this segment gone she has no step on the row (see open items).
   - (c) Release-date steps as SLOW follow-ups `followup:seq-6-0:2026-11-02T00:00:00+09:00` (routine 6 release, step 0, next Monday, rechecked weekly), wording kept plus " (recheck weekly)": Vineet Agarwal (3ed19a301a7f81ad9d12dff4c0145076), Anmol Madan (3f019a301a7f8136b0bef362b06d0f8c), Srinivas Choudhary (3f019a301a7f8166bed5e8a0c985c035), and Mandar Dandekar (3ed19a301a7f81249675cb216e4325bb). Their old reply Message-IDs are kept in the flag.
   - (d) Removed the two AD Personal Kind Task rows keyed decision (show 3fa19a301a7f81638e55d12684ccad16): 3fc19a301a7f8150b1ccf6c7949e6734 (Task: tier the Founder Thesis backlog into FT1 and FT2, "mail Akshay the link to the view") and 3fc19a301a7f81e8b013e8fb2206e787 (Task: transcripts backlog on the Mac, "mail Akshay the mac-transcripts-v2 prompt"). FAST's scope never reaches them. Their Next action stays as it is.
   - (e) Ankit Utreja (3f019a301a7f813287bbf83d4112e716): decision key unchanged; `next_date` = 2026-10-27 (Akshay's 19 Oct "chase hard"; first working day after the migration). Live Next date is 2027-01-03.
2. `waiting_on_add` = Zoya on every rule 7 row whose live Waiting on (read 26 Oct) lacks her: Mandar Dandekar (Sarika), Shruthi Cauvery Iyer 3f019a301a7f810989d7e64802788b69 (Guest or PR), Vivek Desai 3f219a301a7f815e8d20d3583af31ee2 (Guest or PR), Manan Thakkar 3fa19a301a7f81508e24e25202d1e571 (Guest or PR), Anirudh Damani 3fa19a301a7f81d1acc4c52ac663ef31 (Guest or PR). Nikita Kumawat already has Zoya. Not added on Sumit Gupta BTS (a7d41a8538394ec9b148c13aa4824052, Waiting on empty): its segment is an unkeyed pointer with no Zoya step on either row, so Zoya in Waiting on would put a row with no step in her queue.
3. Mandar's WhatsApp-raised ask: the Activity is 40019a301a7f81aa9a8ede0756fb5c8e (Kind WhatsApp, Source ID wa:...:2026-10-21, linked to Mandar's Engagement; Pragatti asked when the episode goes live), Date 2026-10-21T16:18:00+09:00. Its reply key would be `reply:call-40019a301a7f81aa9a8ede0756fb5c8e:2026-10-21T16:18:00+09:00`. But the whole Zoya step is telling Pragatti the release date, with no separate reply part, so (1c) wins: keyed `followup:seq-6-0:2026-11-02T00:00:00+09:00`, and the WhatsApp key is recorded in the flag only.
4. Mohit Bedi (3f019a301a7f81c1b612e8d8fb17c27a): no change, stays `nurture:seq-7-1`. The unlogged 16 Oct check-in isn't evidence (Cleanup ruling 4).
5. d394-migrate.md Rulings: rulings 1 and 2 now carry Cleanup's wording ("sponsored chase", "sponsored follow-up", "precall chase", "chases" and bare "follow-up" (by Status) = rule 2; LT chase revisit wording = rule 3; rule 3's date from rule 2's chain). Ruling 5 now uses `reply:call-<WhatsApp Activity page id>:<Date>`. New rulings 8 to 12 cover replay 1b. The "Zoya action keys" Controls page in Notion was not edited (this pass was read-only on Notion); it still needs the same text.

## Review list (38)

- Mandar Dandekar @ Sorin Investments, Founder Thesis (3ed19a301a7f81249675cb216e4325bb), rule 7 then 2 (release, replay 1b): rule 7, Zoya step inside Sarika's segment (edits another owner's text). The whole Zoya step is the release-date answer to Pragatti, so replay 1b's release ruling wins over Cleanup item 3: keyed as SLOW follow-up seq-6-0, rechecked weekly. The reply-key alternative would have been reply:call-40019a301a7f81aa9a8ede0756fb5c8e:2026-10-21T16:18:00+09:00 (Pragatti's WhatsApp Activity). Waiting on was Sarika only; Zoya added.
- Shruthi Cauvery Iyer @ Vaia, Founder Thesis (3f019a301a7f810989d7e64802788b69), rule 7 then 2 (extension): rule 7, Zoya step inside Divyanshi's segment (edits another owner's text). 'chases' is not rule 2 wording; routine 2 from the precall; Chase step empty so n=1; 'from 24 Oct' is not 'on <D Mon>', so date is Next date. Waiting on was Guest or PR only; Zoya added.
- Paritosh Ladhani and Alka Ladhani @ Taj Agra, Founder Thesis (3f019a301a7f81168d30c7a24f81bf14), rule 2 (extension): precall booking chase without rule 2 wording; routine 2; Chase step empty so n=1; no 'on' date, so Next date.
- Sinduri Reddy @ Premia Academy, Founder Thesis (3f019a301a7f81178bd4ea089dfa2cf2), rule 6: check-in to PR about billing details (invoice hold); no rule 2 wording, not a reply owed (Zoya replied 22 Oct), so rule 6 team (actions.txt lists billing asks as team). Could be read as routine 4 misc chase.
- Nikita Kumawat @ Brandworks Technologies, Founder Thesis (3f019a301a7f812291c7e824de67fbc0), rule 3: rebuilt for drift 2026-10-26. The second build's rule 7 segment was rewritten live as a plain nurture segment; rule 3 literal, n=1, date 3 Jan 2027 from the segment.
- Ankit Utreja @ WebEngage, Founder Thesis (3f019a301a7f813287bbf83d4112e716), rule 5: chase wording (could be rule 2 by extension, routine 2) but the wording names Akshay's call, which literally matches rule 5. Replay 1b: Next date was 3 Jan 2027 despite Akshay's 19 Oct 'chase hard'; the write also sets Next date 2026-10-27 (first working day after this migration).
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
- Mohit Bedi @ Kiwi, Founder Thesis (3f019a301a7f81c1b612e8d8fb17c27a), rule 3 (extension): LT chase row; revisit/check-in/chase wording is not rule 3's 'nurture' wording; keyed as nurture (routine 7) by extension, n from 'Zoya sent: nurture' Activities + 1. Literal reading drops it to rule 6 team. The wording says check-in 2 (the 16 Oct check-in was not logged as 'Zoya sent: nurture'), but rule 3 sets n from Activities, so n=1. Cleanup ruling 4: n=1 stands.
- Raj Gokal @ Solana, un# (3f119a301a7f81218259fc7549b9aad0), rule 3 (extension): LT chase row; revisit/check-in/chase wording is not rule 3's 'nurture' wording; keyed as nurture (routine 7) by extension, n from 'Zoya sent: nurture' Activities + 1. Literal reading drops it to rule 6 team.
- Director (name not given) @ Lighthouse Info Systems, Founder Thesis (3f119a301a7f8170bbcaef18f8050a0b), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1.
- George Kikvadze @ Bitfury, un# (3f119a301a7f81a697ddc3ae930bc422), rule 3 (extension): LT chase row; revisit/check-in/chase wording is not rule 3's 'nurture' wording; keyed as nurture (routine 7) by extension, n from 'Zoya sent: nurture' Activities + 1. Literal reading drops it to rule 6 team.
- Erik Voorhees @ Venice.ai, un# (3f119a301a7f81cba216d11b021aec16), rule 6: an outreach mail to the guest gated on Akshay's open ask; no follow-up or nurture wording, no inbound, no Akshay decision yet, so rule 6 team by fallback. Better fit may be nurture (LT chase) once Akshay answers.
- Kuberns founders (names not given) @ Kuberns, Founder Thesis (3f119a301a7f81cd9ca1ca1d4a159e78), rule 2 (extension): 'sponsored follow-up' names routine 1 but is not rule 2's 'sponsored step'; n = Chase step 1 + 1 = 2.
- Vivek Desai @ HOSMAC, Founder Thesis (3f219a301a7f815e8d20d3583af31ee2), rule 7 then 2 (extension): rule 7, Zoya step inside the Waiting on Hasti segment. 'chases' is not rule 2 wording; routine 2 (precall rebook); Chase step empty so n=1; no 'on' date, so Next date. Waiting on was Guest or PR only; Zoya added.
- Sonu Kumar Yadav @ Hospitalstore.com, Founder Thesis (3f319a301a7f8175b9a6f78f2d4a2d8a), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1.
- Nitin Kaushal @ SFK Group, Founder Thesis (3f319a301a7f81779aafea9e5cd2ed67), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1.
- Harpreet Singh and Abhinav Awal @ F2 Fintech, Founder Thesis (3f319a301a7f81ee896fecd3eb44cae4), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1.
- Pavan Kosaraju @ AquaExchange, Founder Thesis (3f419a301a7f8178ba37c93bbfc9615b), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1.
- Vaibhav Krishnaswamy @ TempeWala, Founder Thesis (3f719a301a7f811bb337cc7950096d8a), rule 2 (extension): 'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1.
- Manan Thakkar @ Prozeal Green Energy, Founder Thesis (3fa19a301a7f81508e24e25202d1e571), rule 7 then 3 (extension): rule 7 (this is the rule's own example). LT chase row, so keyed as nurture by extension (chase wording, not 'nurture'); could equally be routine 2 seq-2-1 (an active precall-date ask). 'chases 29 Oct' has no 'on', so Next date (same day). Waiting on was Guest or PR only; Zoya added.
- Anirudh Damani @ Artha Group, Founder Thesis (3fa19a301a7f81d1acc4c52ac663ef31), rule 7 then 2 (extension): rule 7, Zoya step inside the Waiting on Sakshi segment. 'chases' is not rule 2 wording; routine 2 (planning call rebook); Chase step empty so n=1; no 'on' date, so Next date. Waiting on was Guest or PR only; Zoya added.
- Task: chase the deals pipeline (Manu Iyer, Shubham and Som) (3fc19a301a7f815aa863d9bb5772afcb), rule 6: chase wording on a Task row with no Status; no routine named, so rule 6 team by fallback. Could be routine 4 misc chase (no step number to key it).
- Matthew @ Magic Bus India Foundation, Founder Thesis (3f019a301a7f81bd9ed6c7020bf96f3d), rule 2: rebuilt for drift 2026-10-26. Form chaser 1 now on hold behind Akshay's re-record question; seq-5-1, Next date 29 Oct; Zoya added to Waiting on though the step waits on Akshay.
- Vivek Iyer @ D2L, Founder Thesis (40119a301a7f810e88a9ecb971df8966), rule 7 then 2: rebuilt for drift 2026-10-26. Zoya step now inside Deepayan's segment (edits another owner's text); seq-1-2 on 2 Nov; Zoya added.
- Kumar Abhishek @ ToneTag, Founder Thesis (3f019a301a7f81b7b36fcda18664be04), rule 3: rebuilt for drift 2026-10-26. Added; nurture n=1, Next date 4 Nov.
- Ryan Louvar @ WisdomTree, un# (3f019a301a7f81d7beffc35bc93cab2b), rule 6: rebuilt for drift 2026-10-26. Added; a data fix (no email on the People row), team, 12 Oct.
- Robert Mitchnick @ BlackRock, un# (3f119a301a7f81018735ed9be408e9e1), rule 2 (extension): rebuilt for drift 2026-10-26. Added; 'followup for precall' as routine 2, n=1, Next date 27 Oct (rule 2 before rule 3 on an LT chase row).
- Prashant Sachan @ AppsForBharat, Built to Share (3f119a301a7f819f9a19f9f8a97ddb3e), rule 2 (extension): rebuilt for drift 2026-10-26. Added; chase with no routine named, Status Recorded gives routine 5; date is the stale 16 Oct Next date. Routine 4 may fit better.
- Sumit Gupta @ CoinDCX, Built to Share (a7d41a8538394ec9b148c13aa4824052), rule 7 (unkeyed): rule 7, a Zoya step inside a pointer segment; it points to the FT row (3f019a301a7f8176b083da416ac23077), whose Next action has no Zoya segment (only 'Waiting on Sharjil ... Zoya on the thread'). Nothing to key on either row until someone writes the FT follow-up step. Waiting on is empty.

Rows marked "note:" in review_flag (19) are keyed by a literal rule match and need no decision; the note records context (Waiting on missing Zoya, a rule-order tie, a step that may already be done, a replay 1b change).

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

## Open items after the second build (items 1 to 3 closed by the third build)

1. Live drift since the first build (read 26 Oct, all three rows Claude-updated 26 Oct): Nikita Kumawat (3f019a301a7f812291c7e824de67fbc0) no longer has the rule 7 segment in the file. Her Next action is now "Zoya: nurture Nikita Kumawat: ... reconnect on 3 Jan 2027 (since 5 Oct 2026)" and Waiting on has Zoya, so the file's old_segment won't match at write time. Rebuild her row as a plain rule 3 segment before the write. Two live rows with Zoya segments aren't in the file: SREEPRIYA NS @ Entrust Family Office (3f019a301a7f8178a813c5ef91b8a76f, Booked, "Zoya: confirm with Stella ... whether the 23 Oct recording happened") and Kumar Abhishek @ ToneTag (3f019a301a7f81b7b36fcda18664be04, LT chase, "Zoya: nurture Kumar Abhishek ..."). Neither was changed here (outside Cleanup's five changes).
2. Non-rule-7 rows whose Waiting on lacks Zoya, still only noted: Mithun Pangal (3f019a301a7f819a9d8cd6811838989b), Priya Kumar (3f019a301a7f81b498c2ec93a4c40b42), Gulab Patil (3f419a301a7f8159a4c5de09d3408489), Rick Yvanovich (3ff19a301a7f81a8a754c14597421e3e), Dinesh Yadav (40019a301a7f81449b93c57ac653185a). Cleanup's item 2 says "and the rest the notes flag"; this build applied it to rule 7 rows only.
3. Ankush: Waiting on keeps Zoya while no Zoya segment remains.
4. Ankit: replay 1b also asks the send to write the reply-wait segment with a date; that is a FAST text change, not part of this file.
5. The "Zoya action keys" Controls page still needs rulings 1, 2, 5 and 8 to 12.

## Open items after the third build

1. Re-read at the write: rows keep moving (7 changed on 26 Oct after the second build). The drift guard in `d394-migrate.md` still applies.
2. Prashant Sachan: confirm routine 5 vs routine 4 and the date (the rule chain gives the stale 16 Oct Next date).
3. Matthew @ Magic Bus: Zoya goes into Waiting on for a step that is on hold until Akshay answers; Cleanup to confirm.
4. Ankit (replay 1b reply-wait segment) and the Controls page (rulings) are unchanged from the second build's items 4 and 5.
