import csv, re, sys
from collections import Counter
OUT = sys.argv[1]
T = lambda d: f"{d}T00:00:00+09:00"
rows = []
def add(rid, name, seg, typ=None, origin=None, raised=None, rule='', flag='', step=None, new=None, woa='', nd='', wor=''):
    if typ:
        if step is None:
            assert seg.startswith('Zoya: '), seg
            step = seg[len('Zoya: '):]
        if new is None:
            new = f"Zoya [{typ} {origin} {raised}]: {step}"
        else:
            new = new.replace('{K}', f"Zoya [{typ} {origin} {raised}]")
        key = f"{rid}:{typ}:{origin}:{raised}"
    else:
        key = ''
        if new is None: new = seg
    rows.append([rid, name, seg, new, key, rule, flag, woa, nd, wor])
def S(rid, name, seg): add(rid, name, seg, rule='1')
def F(rid, name, seg, r, n, d, flag='', woa=''):  # literal rule 2
    add(rid, name, seg, 'followup', f'seq-{r}-{n}', T(d), '2', flag, woa=woa)
def FX(rid, name, seg, r, n, d, why):     # rule 2 by extension
    add(rid, name, seg, 'followup', f'seq-{r}-{n}', T(d), '2 (extension)', 'REVIEW: ' + why)
def N(rid, name, seg, n, d, flag='', rule='3'):
    add(rid, name, seg, 'nurture', f'seq-7-{n}', T(d), rule, flag)
def R(rid, name, seg, msgid, raised, flag=''):
    add(rid, name, seg, 'reply', f'msg-{msgid}', raised, '4', flag)
RECHECK = '2026-11-02'  # next Monday after the 26 Oct build; release-date steps are rechecked weekly
def RL(rid, name, seg, was, flag='', step=None, new=None, rule='2 (release, replay 1b)', woa=''):  # replay 1b: release date as SLOW follow-up
    if step is None:
        step = seg[len('Zoya: '):]
    step = step + ' (recheck weekly)'
    add(rid, name, seg, 'followup', 'seq-6-0', T(RECHECK), rule,
        flag or f"note: replay 1b: the release-date answer is a SLOW follow-up (routine 6 release, step 0), rechecked weekly; was {was}.",
        step=step, new=new, woa=woa)
def D(rid, name, seg, d, flag=''):
    add(rid, name, seg, 'decision', f'call-{rid}', T(d), '5', flag)
def TM(rid, name, seg, d, flag=''):
    add(rid, name, seg, 'team', f'call-{rid}', T(d), '6', flag)
DRIFT = 'REVIEW: rebuilt for drift 2026-10-26. '  # live row changed after the second build; rebuilt by the rules from the 26 Oct re-read
WOA_NOTE = "note: Waiting on lacked Zoya (re-read 26 Oct); waiting_on_add adds her (OWNERS)."

SPCH = "Zoya: sponsored chase (ask if they're open to it) on 27 Oct"
WHY_SPCH = "'sponsored chase' is follow-up wording naming routine 1 but not in rule 2's list ('sponsored step'); literal reading drops it to rule 6 team. n = Chase step + 1."
WHY_LT = "LT chase row; revisit/check-in/chase wording is not rule 3's 'nurture' wording; keyed as nurture (routine 7) by extension, n from 'Zoya sent: nurture' Activities + 1. Literal reading drops it to rule 6 team."

# ---- batch 1
S('1a7647877a0345b18a89d7af96f325fd','Sanjeev Bikhchandani @ Info Edge, Built to Share',"Zoya: back to Akshay on 2 Nov: Sanjeev Bikhchandani for Built to Share, Akshay asks him again (he said November), not a cold mail")
S('27542f7f2ea541ce984639b7f35bdf09','Aneesh Reddy @ Capillary, Built to Share',"Zoya: back to Akshay on 4 Jan 2027: Aneesh Reddy for Built to Share, Akshay asks him again (he declined this year), not a cold mail")
RL('3ed19a301a7f81249675cb216e4325bb','Mandar Dandekar @ Sorin Investments, Founder Thesis',"Sarika: confirm Mandar's release date; then Zoya tells Pragatti (Stratink)", '',
    rule='7 then 2 (release, replay 1b)',
    step="tell Pragatti (Stratink) Mandar's release date",
    new="Sarika: confirm Mandar's release date | {K}: tell Pragatti (Stratink) Mandar's release date (recheck weekly)",
    flag="REVIEW: rule 7, Zoya step inside Sarika's segment (edits another owner's text). The whole Zoya step is the release-date answer to Pragatti, so replay 1b's release ruling wins over Cleanup item 3: keyed as SLOW follow-up seq-6-0, rechecked weekly. The reply-key alternative would have been reply:call-40019a301a7f81aa9a8ede0756fb5c8e:2026-10-21T16:18:00+09:00 (Pragatti's WhatsApp Activity). Waiting on was Sarika only; Zoya added.",
    woa='Zoya')
S('3ed19a301a7f81669b4bf3a99355b53d','Ezhilarasan Natarajan @ CoreStack, Founder Thesis',"Zoya: back to Akshay on 8 Nov: send Ezhilarasan the links to shorter clips (promised 23 Oct on WhatsApp)")
S('3ed19a301a7f819284e7e17d698e55f2','Raghu Pareddy @ Wissen Technology, Founder Thesis',"Zoya: back to Akshay on 8 Nov: release date for Neha (Wissen PR) once the calendar is final, and her cut notes on the transcript")
S('3ed19a301a7f81a08e66d02c507e0813','Anil Kumar @ Redseer Startegy Consultants, Founder Thesis',"Zoya: back to Akshay on 8 Nov: call Aanshul (RedSeer) about the first cut, if not done yet (recommend call, then Zoya confirms the date in writing)")
RL('3ed19a301a7f81ad9d12dff4c0145076','Vineet Agarwal @ Transport Corporation of India Ltd., Founder Thesis',"Zoya: send Urbashree (PR Pundit) the release date once the calendar is updated (Akshay told her 23 Oct he will send a date; check the Episode for the planned release first)",
  'rule 4 reply msg-DB9PR05MB79803D8E37B4C6C88E3B747E8D642@DB9PR05MB7980.eurprd05.prod.outlook.com (2026-10-23T14:16:28+09:00)')
F('3f019a301a7f81049f5dec32e9181d52','Shai Coelho @ Vtrender, Founder Thesis',"Zoya: precall step 2 on 28 Oct",2,2,'2026-10-28')
F('3f019a301a7f8105bd90c184e3ec017d','Saloni @ DesiCrew, Founder Thesis',"Zoya: precall step 3 on 28 Oct (bypass skipped, Saloni wrote directly; then nurture)",2,3,'2026-10-28')
add('3f019a301a7f810989d7e64802788b69','Shruthi Cauvery Iyer @ Vaia, Founder Thesis',
  "Divyanshi (Deqollab) to book the Vaia precall via the link (Akshay told her on 17 Oct to go ahead); Zoya chases from 24 Oct if no booking",
  'followup','seq-2-1',T('2026-10-27'),'7 then 2 (extension)',
  "REVIEW: rule 7, Zoya step inside Divyanshi's segment (edits another owner's text). 'chases' is not rule 2 wording; routine 2 from the precall; Chase step empty so n=1; 'from 24 Oct' is not 'on <D Mon>', so date is Next date. Waiting on was Guest or PR only; Zoya added.",
  step='chase from 24 Oct if no booking',
  new="Divyanshi (Deqollab) to book the Vaia precall via the link (Akshay told her on 17 Oct to go ahead) | {K}: chase from 24 Oct if no booking", woa='Zoya')
F('3f019a301a7f810bab4be69843d40ccf','Smriti Tandon @ Online Chikitsa Mitra and 120by80 and Salubrious Technologies, Founder Thesis',"Zoya: sponsored step 4 (due diligence story) on 4 Nov",1,4,'2026-11-04')
N('3f019a301a7f810d9a3eff258a38bf93',"Aravind Sanka @ Rapido - Bike Taxi of India, Founder Thesis","Zoya: nurture Lakshashree (The Practice): Aravind's planning call (since 22 Oct 2026; PR asked to hold, multi-city launches)",1,'2026-11-23')
F('3f019a301a7f8111b5ebcc4d67721479','Pratiqk Jaani @ Dhrasti Method, Founder Thesis',"Zoya: sponsored step 4 (due diligence story) on 4 Nov",1,4,'2026-11-04')
FX('3f019a301a7f81168d30c7a24f81bf14','Paritosh Ladhani and Alka Ladhani @ Taj Agra, Founder Thesis',"Zoya: get the precall booked with Samiksha Dhoke (Taj Agra); held to the 23 Oct recheck",2,1,'2026-10-29',
  "precall booking chase without rule 2 wording; routine 2; Chase step empty so n=1; no 'on' date, so Next date.")
F('3f019a301a7f81178b42f7855fee34a6','Vishal Sanghavi and Venkatesh Mudragalla @ Jeh Aerospace, Founder Thesis',"Zoya: precall step 2 on 28 Oct",2,2,'2026-10-28')
TM('3f019a301a7f81178bd4ea089dfa2cf2','Sinduri Reddy @ Premia Academy, Founder Thesis',"Zoya: check with Sneha on 29 Oct if no confirmation has come",'2026-10-22',
  "REVIEW: check-in to PR about billing details (invoice hold); no rule 2 wording, not a reply owed (Zoya replied 22 Oct), so rule 6 team (actions.txt lists billing asks as team). Could be read as routine 4 misc chase.")
F('3f019a301a7f811bba3dced97384aed5','Vishal Virani @ Rocket, Founder Thesis',"Zoya: recording step 3 on 29 Oct",3,3,'2026-10-29')
F('3f019a301a7f811bbc5bc042f545d9c9','Sudhakar Chirra @ FreshBus, Founder Thesis',"Zoya: precall step 3 on 28 Oct",2,3,'2026-10-28')
F('3f019a301a7f811e824fc9131a063226','Nishchay Nath @ BondScanner, Founder Thesis',"Zoya: sponsored step 2 on 2 Nov",1,2,'2026-11-02')
F('3f019a301a7f8120be93f84d3ae3730f','Gautam Saraugi @ Go Colors, Founder Thesis',"Zoya: precall step 2 (dates check) on 28 Oct",2,2,'2026-10-28')
N('3f019a301a7f812291c7e824de67fbc0','Nikita Kumawat @ Brandworks Technologies, Founder Thesis',"Zoya: nurture Nikita Kumawat: PR (Ria, One Source) paused on 5 Oct, 'later stage', no date; reconnect on 3 Jan 2027 (since 5 Oct 2026)",1,'2027-01-03',
  DRIFT + "The rule 7 segment in the second build ('Waiting on Ria ...; Zoya reconnects on the revisit date') was rewritten live on 26 Oct as a plain nurture segment. Rule 3 literal: n = 0 'Zoya sent: nurture' Activities since 5 Oct + 1; date from the segment's own 'reconnect on 3 Jan 2027' ('paused on 5 Oct' is history, ruling 3), same as Next date. Waiting on has Zoya.")
D('3f019a301a7f8123b098f6522d5f6080','Vishal Devanath @ SMERGERS, Founder Thesis',"Zoya: create an Engagement for the Charge Zone profile Vishal shared (Akshay: nothing is pending on him here)",'2026-10-25',
  "note: internal step from Akshay's 25 Oct call; rule 5 precedes rule 6, so typed decision (FAST) though the work is internal.")
F('3f019a301a7f81249148d12f4439ede4','Aman Arora @ Magical Theatre, Founder Thesis',"Zoya: sponsored step 3 (audience seniority) on 30 Oct",1,3,'2026-10-30')
F('3f019a301a7f81249f57c4fedf5d4a7b','Neerja Hajela @ Yakult Danone India Pvt. Ltd, Founder Thesis',"Zoya: precall step 2 on 27 Oct",2,2,'2026-10-27')
F('3f019a301a7f8129b418f49170519e55','Beerud Sheth @ Gupshup, Founder Thesis',"Zoya: recording step 2 on 28 Oct",3,2,'2026-10-28')
add('3f019a301a7f812d8f24e8b4b7dbec9a','Ankush Tiwari @ pi-labs.ai, Founder Thesis',"Zoya: after your call, take the next steps with the pi-labs PR team (Ankita, Simran)",
  rule='done by match', new='',
  flag="note: replay 1b: completed by match. The decision mail this step follows went 26 Oct (msgid 70008c86...), so the Zoya segment is dropped and no key is written; the other two segments (Waiting on Simran, Akshay: Flock Safety info) stay. This was Zoya's last segment on the row, so waiting_on_remove drops her from Waiting on (live: Akshay, Guest or PR, Zoya).",
  wor='Zoya')
F('3f019a301a7f812ea2a8d1e74b88113c','Amit Das @ Think360.ai, Founder Thesis',"Zoya: form chaser 2 on 29 Oct",5,2,'2026-10-29')
D('3f019a301a7f813287bbf83d4112e716','Ankit Utreja @ WebEngage, Founder Thesis',"Zoya: chase Devanshi (SGA) hard for a pre-call date with Ankit, or ask for CEO Avlesh Singh instead (Akshay's call: chase hard)",'2026-10-19',
  "REVIEW: chase wording (could be rule 2 by extension, routine 2) but the wording names Akshay's call, which literally matches rule 5. Replay 1b: Next date was 3 Jan 2027 despite Akshay's 19 Oct 'chase hard'; the write also sets Next date 2026-10-27 (first working day after this migration).")
rows[-1][8] = '2026-10-27'  # next_date: replay 1b finding 1
F('3f019a301a7f8132aef2d103e29c7f81','Abhilash Maurya @ Naxatra Labs, Founder Thesis',"Zoya: precall step 2 on 30 Oct",2,2,'2026-10-30')
RL('3f019a301a7f8136b0bef362b06d0f8c','Anmol Madan @ RadiantGraph, Founder Thesis',"Zoya: send Erin (JRB) the release date once the Episode has a confirmed date (we told her 24 Oct we will come back once the release calendar is finalized)",
  'rule 4 reply msg-CAEx+WSJ9_98QWpX_8-8LDMPY-ExAZ_sXF1NNqZMC7SBo8ugTdw@mail.gmail.com (2026-10-24T02:44:23+09:00)')
F('3f019a301a7f8137871efc1e8cb64837','Amit Patni @ RAAY Global, Founder Thesis',"Zoya: form chaser 2 on 27 Oct",5,2,'2026-10-27')
F('3f019a301a7f81398033d155d0bbb727','Ashissh Raichura @ Scanbo, Founder Thesis',"Zoya: sponsored step 3 (audience seniority) on 30 Oct",1,3,'2026-10-30')
F('3f019a301a7f813a841ecd974cdbc9b6','Andrey Fedorov @ STON.fi, un#',"Zoya: sponsored step 2 on 28 Oct",1,2,'2026-10-28')
F('3f019a301a7f813da45bcf2728e7fbbb','Your Retail Coach (YRC) joint episode pitch, Founder Thesis',"Zoya: sponsored step 4 (due diligence story) on 4 Nov",1,4,'2026-11-04')
F('3f019a301a7f813e8e19f00fdd50f63a','Shilpi Goel @ Nutrishilp, Founder Thesis',"Zoya: sponsored step 3 (audience seniority) on 28 Oct (Zoya now on the thread; peers mail not yet sent, use as step 3 or fold in)",1,3,'2026-10-28')
F('3f019a301a7f813fa6c6f14289920f2a','Pranav Vempati @ MakersHive, Founder Thesis',"Zoya: precall step 2 on 2 Nov",2,2,'2026-11-02')
N('3f019a301a7f8140bb3dfcd3c30f2908','Pragati Varshney @ Brand Buzz Partners - PR Team, Founder Thesis',"Zoya: sponsored nurture (no step R on sponsored threads) on 29 Oct, after the 14 days since Akshay's 15 Oct loop-in",1,'2026-10-29',
  "note: the step is the move into nurture; n=1 (no 'Zoya sent: nurture' Activities).")
F('3f019a301a7f8141aa67c43e281122b7','Kashyap Reddy @ Metasports Interactive, Founder Thesis',"Zoya: precall step 2 on 29 Oct",2,2,'2026-10-29')
FX('3f019a301a7f8143ad15c89c1bcd4418','Naresh Kumar Kumawat @ Internationally Acclaimed Sculptor, Founder Thesis',SPCH,1,1,'2026-10-27',WHY_SPCH)
F('3f019a301a7f8144b162ea95b5a7db1b','Shailendra Bhadauria @ entrepreneur and institution builder, Founder Thesis',"Zoya: sponsored step 2 on 30 Oct",1,2,'2026-10-30')
# ---- batch 2
FX('3f019a301a7f8145b49fec5f61d1beb6','Navneet Chitkara @ Vyasa Astro, Founder Thesis',SPCH,1,1,'2026-10-27',WHY_SPCH)
F('3f019a301a7f814c94b7f12040f713b0','Saravana Maruthamuthu @ opto-ml, Founder Thesis',"Zoya: form chaser 2 on 2 Nov",5,2,'2026-11-02')
F('3f019a301a7f8151a27bc0f45e145a19','Rasika Prashant @ NSRCEL, Founder Thesis',"Zoya: precall step 4 on 16 Nov",2,4,'2026-11-16')
N('3f019a301a7f81579a79c1503c3e4ed5','Rakshith Rangarajan @ Inviga Healthcare Fund, Founder Thesis',"Zoya: move to nurture on 29 Oct (precall step 3 sent 21 Oct; close-out not sent; no move within 14 days of the 15 Oct loop-in)",1,'2026-10-29',
  "REVIEW: the segment literally contains 'precall step 3' (a step already sent, in parentheses), which rule 2 checks first and would key as seq-2-3; keyed as nurture because the step itself is the move to nurture.", rule='3 (over 2)')
FX('3f019a301a7f815d93a8efad4fbeffac','Arushi Kapoor @ The Agency Art House, Founder Thesis',SPCH,1,1,'2026-10-27',WHY_SPCH)
F('3f019a301a7f815e8a92fd94807b735b','Kunal Sehgal @ South Asia Producer, BBC, Founder Thesis',"Zoya: precall step 2 on 28 Oct",2,2,'2026-10-28')
FX('3f019a301a7f8161b326f5f8ff5da05a','Shekar Swamy and Srinivasan K. Swamy @ R K Swamy, Founder Thesis',"Zoya: follow-up on 27 Oct",2,1,'2026-10-27',
  "'follow-up' names no routine; routine 2 taken from Status Precall requested; Chase step empty so n=1.")
F('3f019a301a7f816580c1c65765fa601e','AJAY ASHAR @ Ashar group, Founder Thesis',"Zoya: precall step 2 (dates check) on 28 Oct",2,2,'2026-10-28')
FX('3f019a301a7f8166bbd6ea76681505df','Praveen Gadelli @ STEMLearn.AI, Founder Thesis',SPCH,1,1,'2026-10-27',WHY_SPCH)
RL('3f019a301a7f8166bed5e8a0c985c035','Srinivas Choudhary @ Alligator Automations, Founder Thesis',"Zoya: send Nivedita (PRtainment) the release date once the calendar is final (Akshay told her on 25 Oct it is not finalised and he will mail it; never give a date before the Episode has one)",
  'rule 4 reply msg-CALcgGRM+ty5Sd7Kv9=cDN3mmJsocuM1G3aPq5mZMadfVmYYayg@mail.gmail.com (2026-10-23T14:45:08+09:00)')
N('3f019a301a7f81688a10fb6d95f13243','Ishank Joshi @ Mobavenue, Founder Thesis',"Zoya: Waiting on Simran for Ishank's precall dates; next check-in 27 Oct",1,'2026-10-27',
  "REVIEW: " + WHY_LT + " Could instead be routine 2 (precall dates). 'next check-in 27 Oct' has no 'on', so Next date (same day).", rule='3 (extension)')
F('3f019a301a7f816d9919d82d4a41fd92','Gokul Cholaghar @ Libra AI, Founder Thesis',"Zoya: sponsored step 2 (peers) on 28 Oct",1,2,'2026-10-28')
S('3f019a301a7f816dabb6c6a374ba265e','Mohan Lakhamraju @ Great Learning, Founder Thesis',"Zoya: back to Akshay on 2 Nov: get Mohan himself on a call (Tier 1; Navami is Via, Zoya not on her 20 Aug thread). Earlier queued decision mail on hold while snoozed")
FX('3f019a301a7f816f846df7e22a23f8ad','Madhu Sudan @ ShelfRadar AI, Founder Thesis',"Zoya: sponsored chase to Bhoomika (Vicara) for Madhu. Not on the thread: send the one-line ad@ loop-in per Rules for Zoya section 5 (decision 368), \"Bhoomika, has Madhu had a chance to look at the sponsored feature? adding @Zoya to coordinate\". If that send is blocked again, send it instead as a new mail from your own inbox to Bhoomika (Cc Sejal and Akshay), same ask, and take the thread from there.",1,1,'2026-10-28',
  WHY_SPCH + " No 'on' date, so Next date.")
FX('3f019a301a7f8172b556c68bdac66799','Joseph Sudheer Reddy Thumma @ Magellanic Cloud Limited, Founder Thesis',"Zoya: precall chase to Betsy (Concept PR) on 27 Oct (podm.in/30min); no dates after the last step: Unresponsive",2,1,'2026-10-27',
  "'precall chase' names routine 2 but is not rule 2's 'precall step'; Chase step empty so n=1.")
F('3f019a301a7f817795e9e74559cda19e','G. K. Bindra @ NKG, Founder Thesis',"Zoya: sponsored step 2 (peers) on 28 Oct",1,2,'2026-10-28')
F('3f019a301a7f8177a804ed083e54f7a3','Rishwin Devaya @ Riverside Coffee, Founder Thesis',"Zoya: sponsored step 3 (audience seniority) on 27 Oct",1,3,'2026-10-27')
F('3f019a301a7f817aa441f45c4dae2253','Manohar Singh Charan @ ShareChat & Moj, Founder Thesis',"Zoya: precall step 2 on 29 Oct",2,2,'2026-10-29')
F('3f019a301a7f817b9f58dae46eec8b14','Manoj Dobhal @ Dish TV India, Founder Thesis',"Zoya: precall step 2 on 29 Oct",2,2,'2026-10-29')
F('3f019a301a7f817c8903e578bace1296','Navajith Karkera @ Rapture Innovation Labs (Sonic Lamb), Founder Thesis',"Zoya: precall step 4 on 29 Oct (silent after that: nurture, not Unresponsive)",2,4,'2026-10-29')
F('3f019a301a7f817cb277cc9bf85852bf','Shradha Chaturvedi @ UNDRESS and GetCompanion, Founder Thesis',"Zoya: sponsored step 2 on 29 Oct",1,2,'2026-10-29')
F('3f019a301a7f817fae25cc8414c31aa5','Devesh Taparia @ DriveX, Founder Thesis',"Zoya: sponsored step 2 on 9 Nov",1,2,'2026-11-09')
FX('3f019a301a7f8182b156dca9050b3659','Yash Varyani @ Drizz, Founder Thesis',SPCH,1,1,'2026-10-27',WHY_SPCH)
F('3f019a301a7f8187b754f7032dc59208','Navraj Bindra @ NKG Advisory, Founder Thesis',"Zoya: sponsored step 3 (audience seniority) on 30 Oct",1,3,'2026-10-30')
F('3f019a301a7f8188abeef7fe35482a8d','Ankit Wagh @ ITUS Sports & Safety Pvt. Ltd. and Indian Rescue Academy, Founder Thesis',"Zoya: sponsored step 2 (peers) on 29 Oct",1,2,'2026-10-29')
F('3f019a301a7f818ab683c3535af880ed','Devanshu Bansal @ UK Realty, Founder Thesis',"Zoya: sponsored step 2 (peers) on 29 Oct",1,2,'2026-10-29')
F('3f019a301a7f818b8346d80d49d115fa','Anand Balaji @ Xflow, Founder Thesis',"Zoya: sponsored step 4 (due diligence story) on 30 Oct",1,4,'2026-10-30')
F('3f019a301a7f818d9af3e4a84a11d4c8','Ashok Kumar @ RAH Infotech, Founder Thesis',"Zoya: precall step 2 (dates check) on 28 Oct",2,2,'2026-10-28')
TM('3f019a301a7f81929414d3601e5595e0','Col. Sai Shankar P @ QClairvoyance Quantum Labs, Founder Thesis',"Zoya: obtain the verified Zencastr guest link from Ranjita if the Mac task cannot prove success; ensure it is on the confirmed 5 Nov invite before recording",'2026-10-26')
F('3f019a301a7f8194b4f7d0e85fd3b2cd','Sparsh Gupta @ Wingify, Founder Thesis',"Zoya: recording step 2 on 28 Oct",3,2,'2026-10-28')
N('3f019a301a7f8196a5f1c6b2f911781d','Pavan Kumar @ White Lotus Group, Founder Thesis',"Zoya: sponsored nurture (no step R on sponsored threads) on 29 Oct, after the 14 days since Akshay's 15 Oct loop-in",1,'2026-10-29',
  "note: the step is the move into nurture; n=1 (no 'Zoya sent: nurture' Activities).")
N('3f019a301a7f8198a658d25c5ef71f4c','Annanya Sarthak @ Awign, Founder Thesis',"Zoya: nurture Annanya Sarthak: reconnect for a Founder Thesis recording (since 20 Oct 2026)",2,'2026-12-21')
F('3f019a301a7f81999073d3bd3b7bb44b','Rahul Chandola @ Institute of Heart Lungs Diseases Research Centre (IHLD), Founder Thesis',"Zoya: precall step 1 on 30 Oct (held for ONE PERSON, ONE ASK: Abhinav got the sponsored step 1 mail for Shailendra on 23 Oct)",2,1,'2026-10-30')
F('3f019a301a7f819a9d8cd6811838989b','Mithun Pangal @ VYE Manufacturer and Consultants Pvt. Ltd, Founder Thesis',"Zoya: sponsored step 4 (proof story) on 22 Oct; mail planned in the page body; blocked until the due-diligence story is confirmed (Akshay) and an ad@ send is allowed",1,4,'2026-10-22',
  "note: Waiting on lacked Zoya (re-read 26 Oct); waiting_on_add adds her (OWNERS). The step is blocked on Akshay; she holds it until he confirms.", woa='Zoya')
F('3f019a301a7f819ba6fbff3b6114faec','Stephen Somers and Lisa Somers @ Marketplace SuperHeroes, Founder Thesis',"Zoya: sponsored step 4 (questions) on 5 Nov",1,4,'2026-11-05')
F('3f019a301a7f819c9730ccc8067f0927','Sanjiv Bajaj @ BajajCapital Ltd, Founder Thesis',"Zoya: sponsored step 3 (access) on 2 Nov",1,3,'2026-11-02')
F('3f019a301a7f81a1b822cada647a9a47','Vijay Kumar @ Flexymanagers, Founder Thesis',"Zoya: sponsored step 4 on 29 Oct",1,4,'2026-10-29')
F('3f019a301a7f81aba7e9e79fd5b7dd8a','Arun Poddar @ Choice International, Founder Thesis',"Zoya: precall step 2 on 27 Oct",2,2,'2026-10-27')
# ---- batch 3
TM('3f019a301a7f81aca5ded32a046ad9c2','Siddhesh Ravindra Naik @ ULOOK, Founder Thesis',"Zoya: if no slot by 4 Nov, ask Akshay whether to park until ULOOK launches",'2026-10-22')
N('3f019a301a7f81af9229ee3cd1921e34','Patrik Antoni @ IKEA India, Founder Thesis',"Zoya: nurture Aastha (MSL): Patrik Antoni's call with Akshay (since 4 May 2026)",2,'2026-12-25')
F('3f019a301a7f81afb875e1fcf11f366a','Ujwal Sutaria @ Trillion Dollar Venture (TDV), Founder Thesis',"Zoya: sponsored step 2 on 30 Oct",1,2,'2026-10-30')
F('3f019a301a7f81b0b751cb90cf585011','Dhruv Atreja @ Fastino Labs, Founder Thesis',"Zoya: sponsored step 2 on 30 Oct",1,2,'2026-10-30')
F('3f019a301a7f81b28714f22c3d499471','IAS Balamurugan @ Anicut Capital, Founder Thesis',"Zoya: precall step 2 on 29 Oct",2,2,'2026-10-29')
F('3f019a301a7f81b29089e20c8aab1b3e','Raghav Mahajan @ BECOME TANK READY, Founder Thesis',"Zoya: sponsored step 4 (due diligence story) on 30 Oct",1,4,'2026-10-30')
F('3f019a301a7f81b498c2ec93a4c40b42',"Priya Kumar @ Priya Kumar's Training Systems, Founder Thesis","Zoya: sponsored step 1 on 29 Oct",1,1,'2026-10-29',WOA_NOTE,woa='Zoya')
N('3f019a301a7f81b7b36fcda18664be04','Kumar Abhishek @ ToneTag, Founder Thesis',"Zoya: nurture Kumar Abhishek: availability promised by Nikita (Adfactors) on 19 Aug, silent through 3 chases; consider a direct route if the PR stays silent (since 19 Aug 2026)",1,'2026-11-04',
  DRIFT + "Live Zoya segment missing from the second build (nurture started 26 Oct, daily sweep). Rule 3 literal: n = 0 'Zoya sent: nurture' Activities since 19 Aug + 1; no 'on <D Mon>' for the step ('promised ... on 19 Aug' is history), so Next date 4 Nov. Waiting on has Zoya.")
F('3f019a301a7f81bd92dcd5fcfcc17a98','Aayush Jindal @ Asian Footwears, Founder Thesis',"Zoya: precall step 3 on 2 Nov",2,3,'2026-11-02')
add('3f019a301a7f81bd9ed6c7020bf96f3d','Matthew @ Magic Bus India Foundation, Founder Thesis',"Zoya: form chaser 1 on hold until this is decided",
  'followup','seq-5-1',T('2026-10-29'),'2',
  DRIFT + "Live segment rewritten 26 Oct from 'form chaser 1 on 2 Nov (7 days after the 26 Oct heads-up)' to 'form chaser 1 on hold until this is decided' (Akshay's segment first: re-record Matthew?). Rule 2 literal: routine 5, n=1 from the wording; no 'on <D Mon>' ('on hold' is not a date), so Next date 29 Oct. Waiting on was Akshay, Guest or PR; Zoya added (OWNERS), though the step waits on Akshay's answer.",
  woa='Zoya')
F('3f019a301a7f81bf9f1ef006d096c482','Surya Khurana @ FlixBus India, Founder Thesis',"Zoya: sponsored step 3 on 29 Oct",1,3,'2026-10-29')
N('3f019a301a7f81c08f87ef4adba6e79e','Pravesh Dudani @ National Skill Development Corporation (NSDC), Founder Thesis',"Zoya: nurture Gyanaranjan Mantri (Dentsu): Pravesh Dudani's preliminary call (since 21 Oct 2026)",1,'2026-11-02')
N('3f019a301a7f81c1b612e8d8fb17c27a','Mohit Bedi @ Kiwi, Founder Thesis',"Zoya: LT check-in 2 on 14 Jan asks Devanshi (SGA) for the 30-min call; settle Mohit's role on that call",1,'2027-01-14',
  "REVIEW: " + WHY_LT + " The wording says check-in 2 (the 16 Oct check-in was not logged as 'Zoya sent: nurture'), but rule 3 sets n from Activities, so n=1. Cleanup ruling 4: n=1 stands.", rule='3 (extension)')
F('3f019a301a7f81cbbfbeeeedf10fc451','Raunak Bhinge @ Infinite Uptime, Founder Thesis',"Zoya: form chaser 2 on 28 Oct",5,2,'2026-10-28')
N('3f019a301a7f81cc80d1c7b2308fd780','Mukund Jha @ Emergent, Founder Thesis',"Zoya: nurture Naresh (Moes Art): Mukund Jha's call dates (check-in sent from ad@ 21 Oct with Zoya added; follow with the mail from my inbox once the thread shows there) (Akshay: chase)",1,'2026-10-28',
  "note: also carries Akshay's call ('chase'), rule 5; rule 3 comes first in order. The 21 Oct ad@ check-in is not a 'Zoya sent: nurture' Activity, so n=1.")
F('3f019a301a7f81cd9da9e84b67d7323e','Nupoor Mohan @ The Full Circle, Founder Thesis',"Zoya: sponsored step 3 (audience seniority) on 28 Oct",1,3,'2026-10-28')
TM('3f019a301a7f81d7beffc35bc93cab2b','Ryan Louvar @ WisdomTree, un#',"Zoya: fix: no email for the guest (Ryan Louvar's People row)",'2026-10-12',
  DRIFT + "Live Zoya segment missing from the second build. A data fix, not a send: no follow-up, nurture, reply or Akshay-call wording, so rule 6 team; dated by the newest Claude note line that mentions the step (12 Oct, ruling 4). The Sri segment stays. Waiting on has Zoya.")
F('3f019a301a7f81d88f11e41f19abe30a','Narendra Sen @ RackBank and NeevCloud, Founder Thesis',"Zoya: precall step 3 on 30 Oct",2,3,'2026-10-30')
N('3f019a301a7f81d98b02c0976a8f7152','Vandana Luthra @ VLCC, Founder Thesis',"Zoya: nurture Prerna (Group Teamwork): Vandana Luthra's precall availability (since 19 Oct 2026)",1,'2026-11-02')
N('3f019a301a7f81da9692d252d41f78a4','Betsy Atkins @ Google cloud advisory board, Founder Thesis',"Zoya: nurture Sophia: Betsy's precall dates (since 20 Oct 2026)",1,'2026-11-05')
N('3f019a301a7f81e49ee1c115db980a55','Manoj Meena @ ATOMBERG, Founder Thesis',"Zoya: nurture Manoj Meena (Atomberg): a Founder Thesis recording, after the IPO (since 20 Oct 2026)",2,'2026-12-21')
N('3f019a301a7f81eb88a2d0bf271b1f7f','Akshit Chaudhary @ BabyBillion, Founder Thesis',"Zoya: nurture Ananya (PrAndit): Dinesh's prelim call (since 6 Oct 2026)",2,'2026-12-25')
F('3f019a301a7f81ee9a33fb1f9b1b3b18','Nitya Yadav @ Integrow Asset Management, Founder Thesis',"Zoya: sponsored step 4 (questions) on 6 Nov",1,4,'2026-11-06')
F('3f019a301a7f81eea46bc1cd9209dee5','Arindam Ghosh @ Management Accountants, Founder Thesis',"Zoya: sponsored step 4 (questions) on 5 Nov",1,4,'2026-11-05')
N('3f019a301a7f81f7a0cce391f7419444','Tanuj Shori @ Square Yards, Founder Thesis',"Zoya: nurture Poorvi (SGA): Tanuj Shori's call with Akshay (check-in sent from ad@ 21 Oct with Zoya added; follow with the mail from my inbox once the thread shows there) (Akshay: chase)",1,'2026-10-28',
  "note: also carries Akshay's call ('chase'), rule 5; rule 3 comes first in order. The 21 Oct ad@ check-in is not a 'Zoya sent: nurture' Activity, so n=1.")
F('3f019a301a7f81f8bd99f895864aac42','Manish Chaudhary @ Flexprice, Founder Thesis',"Zoya: precall step 2 (dates check) on 28 Oct",2,2,'2026-10-28')
FX('3f119a301a7f81018735ed9be408e9e1','Robert Mitchnick @ BlackRock, un#',"Zoya: followup for precall",2,1,'2026-10-27',
  "rebuilt for drift 2026-10-26. Live Zoya segment missing from the second build. 'followup for precall' is follow-up wording naming the precall (ruling 1), so rule 2 wins over rule 3 though the row is LT chase (ruling 7); routine 2; Chase step empty so n=1; no 'on' date, so Next date. Waiting on has Zoya.")
F('3f119a301a7f8109b90bdcdb3f057999','Vadim Voss @ Next Level DeFi Academy, un#',"Zoya: sponsored step 3 on 28 Oct",1,3,'2026-10-28')
N('3f119a301a7f81218259fc7549b9aad0','Raj Gokal @ Solana, un#',"Zoya: revisit Raj via Hugh (Scrib3) on 3 Dec, after Breakpoint, with the topics list in place of a precall",1,'2026-12-03',
  "REVIEW: " + WHY_LT, rule='3 (extension)')
S('3f119a301a7f8130b2b5c4ee27753b9c','Alex Cutler @ Dromos Labs (Aerodrome), un#',"Zoya: back to Akshay on 2 Nov: eval re-run says Pre-call needed (Fit 6): precall to find the angle, or book the 26-29 Oct slot? (Sri's slot pick held until Akshay decides)")
N('3f119a301a7f813d9756f1dabef70a41','Martin Quensel @ Centrifuge, un#',"Zoya: nurture Keith (Chap PR): get Martin on un# (since 24 Oct 2026)",1,'2026-11-23')
FX('3f119a301a7f8170bbcaef18f8050a0b','Director (name not given) @ Lighthouse Info Systems, Founder Thesis',SPCH,1,1,'2026-10-27',WHY_SPCH)
F('3f119a301a7f817787cafe7723021e29','Karl Floersch @ OP Labs, un#',"Zoya: sponsored step 2 on 2 Nov",1,2,'2026-11-02')
FX('3f119a301a7f819f9a19f9f8a97ddb3e','Prashant Sachan @ AppsForBharat, Built to Share',"Zoya: chase Vineeta for the higher-resolution photo and transcript feedback (promised by 19 Oct)",4,1,'2026-10-16',
  "rebuilt for drift 2026-10-26. Live Zoya segment missing from the second build (daily sweep moved Waiting on to Zoya 26 Oct). Chase wording with no routine named, so ruling 1 takes the routine from Status Recorded: 5; Chase step 0 so n=1. 'promised by 19 Oct' is not 'on <D Mon>', so the date is Next date, which is the stale 16 Oct recording time. Cleanup 26 Oct: routine 4 misc chase, not 5 (seq-5-1 would send guest form chaser 1 for a photo and feedback ask; rule 9's fallback). Past date stands: the promise lapsed 19 Oct. The Chaandini segment stays. Waiting on has Zoya.")
N('3f119a301a7f81a697ddc3ae930bc422','George Kikvadze @ Bitfury, un#',"Zoya: re-approach George's EA at Bitfury on 30 Oct for a slot with George himself",1,'2026-10-30',
  "REVIEW: " + WHY_LT, rule='3 (extension)')
TM('3f119a301a7f81cba216d11b021aec16','Erik Voorhees @ Venice.ai, un#',"Zoya: send Erik the topics-list mail once those are in",'2026-10-26',
  "REVIEW: an outreach mail to the guest gated on Akshay's open ask; no follow-up or nurture wording, no inbound, no Akshay decision yet, so rule 6 team by fallback. Better fit may be nurture (LT chase) once Akshay answers.")
FX('3f119a301a7f81cd9ca1ca1d4a159e78','Kuberns founders (names not given) @ Kuberns, Founder Thesis',"Zoya: sponsored follow-up to Charan on 30 Oct",1,2,'2026-10-30',
  "'sponsored follow-up' names routine 1 but is not rule 2's 'sponsored step'; n = Chase step 1 + 1 = 2.")
F('3f119a301a7f81de9a40fba6f670a4c8','Zach Ipour @ MegPrime Pay, un#',"Zoya: sponsored step 4 on 4 Nov",1,4,'2026-11-04')
add('3f219a301a7f815e8d20d3583af31ee2','Vivek Desai @ HOSMAC, Founder Thesis',
  "Waiting on Hasti (PR): rebook via podm.in/30min when they're ready (bereavement); Zoya chases gently per Cadences (decision 398)",
  'followup','seq-2-1',T('2026-10-29'),'7 then 2 (extension)',
  "REVIEW: rule 7, Zoya step inside the Waiting on Hasti segment. 'chases' is not rule 2 wording; routine 2 (precall rebook); Chase step empty so n=1; no 'on' date, so Next date. Waiting on was Guest or PR only; Zoya added.",
  step='chase gently per Cadences (decision 398)',
  new="Waiting on Hasti (PR): rebook via podm.in/30min when they're ready (bereavement) | {K}: chase gently per Cadences (decision 398)", woa='Zoya')
F('3f319a301a7f8174be9eed8eef11ebad','Ankit Kedia @ Capital A, Founder Thesis',"Zoya: precall step 2 on 30 Oct",2,2,'2026-10-30')
FX('3f319a301a7f8175b9a6f78f2d4a2d8a','Sonu Kumar Yadav @ Hospitalstore.com, Founder Thesis',SPCH,1,1,'2026-10-27',WHY_SPCH)
FX('3f319a301a7f81779aafea9e5cd2ed67','Nitin Kaushal @ SFK Group, Founder Thesis',SPCH,1,1,'2026-10-27',WHY_SPCH)
FX('3f319a301a7f81ee896fecd3eb44cae4','Harpreet Singh and Abhinav Awal @ F2 Fintech, Founder Thesis',SPCH,1,1,'2026-10-27',WHY_SPCH)
# drift 26 Oct: removed 3f419a301a7f8159a4c5de09d3408489 (Gulab Patil @ Lemma): live Next action is now only Akshay's slot question and Waiting on is Akshay; no Zoya segment, out of scope
# ---- batch 4
FX('3f419a301a7f8178ba37c93bbfc9615b','Pavan Kosaraju @ AquaExchange, Founder Thesis',SPCH,1,1,'2026-10-27',WHY_SPCH)
F('3f619a301a7f810196b8c39a3525ff42','Alykhan Jetha @ Daylite (Marketcircle), Founder Thesis',"Zoya: sponsored step 2 on 30 Oct",1,2,'2026-10-30')
FX('3f719a301a7f811bb337cc7950096d8a','Vaibhav Krishnaswamy @ TempeWala, Founder Thesis',SPCH,1,1,'2026-10-27',WHY_SPCH)
F('3f719a301a7f814cbb41dabe6b033ea4','Mukesh Gupta @ MaxVolt Energy Industries, Founder Thesis',"Zoya: sponsored step 2 on 29 Oct",1,2,'2026-10-29')
F('3f819a301a7f8182b7aafacb6430deb6','Ramakant Yadav @ Scalar Field, Founder Thesis',"Zoya: precall step 2 on 30 Oct",2,2,'2026-10-30')
F('3f819a301a7f81beb909e905cf872e9e','Hemant Sood @ Findoc, Founder Thesis',"Zoya: precall step 2 on 30 Oct",2,2,'2026-10-30')
F('3f919a301a7f8108828be4b3348c5440','Vivek Kaimal @ Macros, Founder Thesis',"Zoya: sponsored step 2 on 29 Oct",1,2,'2026-10-29')
F('3f919a301a7f811faafde4207e938960','Carson Cook @ Membrane Labs, un#',"Zoya: sponsored step 2 on 30 Oct",1,2,'2026-10-30')
F('3f919a301a7f8136a9bce1a2a7e98c2a','Varun Khare @ thumpN, Founder Thesis',"Zoya: sponsored step 2 on 29 Oct",1,2,'2026-10-29')
F('3f919a301a7f815dad18ec15a1dd87b5','Mokksh Sani @ Living Liquidz, Founder Thesis',"Zoya: precall step 2 on 30 Oct",2,2,'2026-10-30')
F('3f919a301a7f817bbe0ae544a22d7dfa','Ajay Gupta @ Perceptive Ideas, Founder Thesis',"Zoya: sponsored step 2 on 29 Oct",1,2,'2026-10-29')
F('3f919a301a7f817e87f8ec7f57324ac6','Mauricio Zolliker @ XMAQUINA, un#',"Zoya: sponsored step 2 on 30 Oct",1,2,'2026-10-30')
F('3f919a301a7f8198b010e0a43ed836fc','Matthew Shaw @ OpenWorld, un#',"Zoya: sponsored step 2 on 2 Nov",1,2,'2026-11-02')
# drift 26 Oct: removed 3fa19a301a7f8118a06aea18fea5d7f9 (Subodh Bhardwaj @ Navaratna Concepts): Status They declined 26 Oct, Next action empty; out of scope
F('3fa19a301a7f814a83a8f28c4d25a7f1','Sandeep Shah @ Optimized Group, Founder Thesis',"Zoya: sponsored step 1 on 2 Nov",1,1,'2026-11-02')
F('3fa19a301a7f814a8bb4cb52070733a4','Gagandeep Singh @ TIC, Founder Thesis',"Zoya: sponsored step 2 on 29 Oct",1,2,'2026-10-29')
add('3fa19a301a7f81508e24e25202d1e571','Manan Thakkar @ Prozeal Green Energy, Founder Thesis',
  "Waiting on Vaibhav (Prozeal): a date and time for the informal precall with both co-founders (Zoya answered his process question 22 Oct; he asked for a week on 18 Oct); Zoya chases 29 Oct",
  'nurture','seq-7-1',T('2026-10-29'),'7 then 3 (extension)',
  "REVIEW: rule 7 (this is the rule's own example). LT chase row, so keyed as nurture by extension (" + "chase wording, not 'nurture'); could equally be routine 2 seq-2-1 (an active precall-date ask). 'chases 29 Oct' has no 'on', so Next date (same day). Waiting on was Guest or PR only; Zoya added.",
  step='chase on 29 Oct',
  new="Waiting on Vaibhav (Prozeal): a date and time for the informal precall with both co-founders (Zoya answered his process question 22 Oct; he asked for a week on 18 Oct) | {K}: chase on 29 Oct", woa='Zoya')
add('3fa19a301a7f81d1acc4c52ac663ef31','Anirudh Damani @ Artha Group, Founder Thesis',
  "Waiting on Sakshi (Artha) to rebook the planning call via podm.in/30min; Zoya chases per Cadences (decision 398)",
  'followup','seq-2-1',T('2026-10-29'),'7 then 2 (extension)',
  "REVIEW: rule 7, Zoya step inside the Waiting on Sakshi segment. 'chases' is not rule 2 wording; routine 2 (planning call rebook); Chase step empty so n=1; no 'on' date, so Next date. Waiting on was Guest or PR only; Zoya added.",
  step='chase per Cadences (decision 398)',
  new="Waiting on Sakshi (Artha) to rebook the planning call via podm.in/30min | {K}: chase per Cadences (decision 398)", woa='Zoya')
F('3fb19a301a7f816aa87ff74b7ed6e517','Srikanth Velamakanni @ Fractal Analytics, Founder Thesis',"Zoya: precall step 2 on 27 Oct (Tier 1 inbound, 3 working days)",2,2,'2026-10-27',
  "note: Status is Booking but the wording names the precall routine; keyed by wording.")
F('3fb19a301a7f817bab3df7c45662370b','Akshit Bansal @ Statiq, Founder Thesis',"Zoya: precall step 3 on 2 Nov",2,3,'2026-11-02',WOA_NOTE,woa='Zoya')
# replay 1b: removed 3fc19a301a7f8150b1ccf6c7949e6734 (Task: tier the FT backlog into FT1 and FT2, AD Personal); FAST's scope never reaches it
TM('3fc19a301a7f815aa863d9bb5772afcb','Task: chase the deals pipeline (Manu Iyer, Shubham and Som)',"Zoya: chase Manu Iyer (Bluehill-X call 10 Oct); find Shubham and Som on the Deals board and chase them; anything on price or a call goes to Akshay",'2026-10-21',
  "REVIEW: chase wording on a Task row with no Status; no routine named, so rule 6 team by fallback. Could be routine 4 misc chase (no step number to key it).")
# replay 1b: removed 3fc19a301a7f81e8b013e8fb2206e787 (Task: transcripts backlog on the Mac, AD Personal); FAST's scope never reaches it
F('3ff19a301a7f81a8a754c14597421e3e','Rick Yvanovich @ Business As UnUsual, Founder Thesis',"Zoya: sponsored step 1 on 29 Oct",1,1,'2026-10-29',WOA_NOTE,woa='Zoya')
F('3ff19a301a7f81a98224ee27aa4a5a7d','Matt Walker @ Lull, Founder Thesis',"Zoya: sponsored step 1 on 29 Oct",1,1,'2026-10-29')
F('40019a301a7f81449b93c57ac653185a','Dinesh Yadav @ Fine Acers, Founder Thesis',"Zoya: sponsored step 1 on 29 Oct",1,1,'2026-10-29',WOA_NOTE,woa='Zoya')
F('40019a301a7f8190a195f2310a805f5a','Peter Imburg @ Elfster, Founder Thesis',"Zoya: sponsored step 1 on 29 Oct",1,1,'2026-10-29')
add('40119a301a7f810e88a9ecb971df8966','Vivek Iyer @ D2L, Founder Thesis',
  "Waiting on Deepayan (Brand Compr): reply to the sponsored commercials (sent 26 Oct); Zoya: sponsored step 2 on 2 Nov",
  'followup','seq-1-2',T('2026-11-02'),'7 then 2',
  DRIFT + "Live Next action rewritten 26 Oct: the separate 'Zoya: sponsored step 1 on 2 Nov' segment is gone and the Zoya step now sits inside Deepayan's segment after '; ' (rule 7, edits another owner's text). Rule 2 literal: routine 1, n=2 from the wording, date 2 Nov. Waiting on was Guest or PR only; Zoya added (OWNERS).",
  step='sponsored step 2 on 2 Nov',
  new="Waiting on Deepayan (Brand Compr): reply to the sponsored commercials (sent 26 Oct) | {K}: sponsored step 2 on 2 Nov", woa='Zoya')
R('40119a301a7f812b8fb3f593ee961296','Mekin Maheshwari @ Udhyam Learning Foundation, Built to Share',"Zoya: update Satv by Wed 28 Oct (her holding reply) once Satish confirms the studio; Rainmatter studio in JP Nagar is the option, Mekin lives in Koramangala, office near Ulsoor Lake",
  'CAJTwtmP5jQ3f9fgb-be9bPN8dRc3O45cNr5X7-HaTQUzLnf4rQ@mail.gmail.com','2026-10-23T19:45:17+09:00',
  "note: Satv's 23 Oct ask (dates, studio location); Zoya's 24 Oct holding reply answers nothing, so the reply stays owed. The step also follows Akshay's 25 Oct call; rule 4 comes first.")
F('40119a301a7f8172995bef8144c91971','Rishabh Mishra @ RushDeploy, Founder Thesis',"Zoya: sponsored step 1 on 2 Nov",1,1,'2026-11-02')
F('40219a301a7f81748630fb58c879c687','Vidhatha Annamaneni @ Ironhill, Founder Thesis',"Zoya: precall step 2 on 29 Oct",2,2,'2026-10-29')
add('40419a301a7f8108a357cafb73469297','Sukant Kumar @ Sunday Labs, Founder Thesis',"Zoya: follow up with Sukant on Akshay's reverse proposal (Akshay mailed 25 Oct: he comes on Tech with Sukant as a collab with Founder Thesis; Sukant can book podm.in/30min). Sukant asked Zoya for next steps; answer only as that proposal settles. Eval Pre-call needed (page body).",
  'followup','seq-4-1',T('2026-10-30'),'2 (replay 1b)',
  "note: replay 1b: the reply (msg-MA0P287MB2024B2EE69BDB928CB7970E1CC622@MA0P287MB2024.INDP287.PROD.OUTLOOK.COM) is complete by Akshay's 25 Oct 22:44 JST mail; Akshay's 'Zoya can follow up' is carried as a SLOW routine 4 misc chase on 30 Oct.",
  step="follow up Sukant on Akshay's 25 Oct reverse proposal on 30 Oct")
TM('40419a301a7f814799cee941518d9582',"Task: leave Chaandini's chats with AD out of transcripts shared with hosts","Zoya: when sharing a transcript (e.g. the one sent to Mekin for the B2S pitch), leave out Chaandini's conversation with AD; Chaandini asked 24 Oct via @zoya",'2026-10-25',
  "note: a standing instruction, not a one-off step; keyed as team (Chaandini's ask).")
S('554c617ad3184a7a900f3b0588eb73cd','Noah Goodman @ humans&, Human by Design',"Zoya: back to Akshay on 1 Nov: Noah Goodman asked to revisit next year; eval now Decline, keep in LT chase or pass? Write ok, not ok or a change in Your call.")
S('8c56c98c92a64bcfa30f55ee53796327','Jaydeep Barman @ Rebel Foods, Built to Share',"Zoya: back to Akshay on 4 Jan 2027: Jaydeep Barman for Built to Share, Akshay asks him again (he declined this year), not a cold mail")
add('a7d41a8538394ec9b148c13aa4824052','Sumit Gupta @ CoinDCX, Built to Share',"Same thread as Sumit Gupta @ CoinDCX, Founder Thesis: Zoya follows up there for both shows (Akshay pitched both on 18 Oct)",rule='7',
  flag="REVIEW (unkeyed): rule 7, a Zoya step inside a pointer segment; it points to the FT row (3f019a301a7f8176b083da416ac23077), whose Next action has no Zoya segment (only 'Waiting on Sharjil ... Zoya on the thread'). Nothing to key on either row until someone writes the FT follow-up step. Waiting on is empty.")
TM('ff569bdb98dc4f84b22ac2b790348582','Karri Saarinen @ Linear, Built to Share',"Zoya: review the existing later-contact plan for Karri on 8 Dec; confirm the original reply and current Satish approval before contacting",'2026-10-20',
  "note: internal review step dated 8 Dec; rule 6 raised time is the Claude note date, not 8 Dec.")

with open(OUT,'w',newline='') as f:
    w=csv.writer(f); w.writerow(['row_id','row_name','old_segment','new_segment','key','rule','review_flag','waiting_on_add','next_date','waiting_on_remove'])
    w.writerows(rows)
ids=[r[0] for r in rows]
print('segments',len(rows),'rows',len(set(ids)))
print('keys',sum(1 for r in rows if r[4]), 'unique keys', len({r[4] for r in rows if r[4]}))
print('by rule',Counter(r[5] for r in rows))
print('by type',Counter(r[4].split(':')[1] if r[4] else 'none' for r in rows))
print('REVIEW',sum(1 for r in rows if r[6].startswith('REVIEW')),'notes',sum(1 for r in rows if r[6].startswith('note')))
print('waiting_on_add',[r[0] for r in rows if r[7]],'next_date',[(r[0],r[8]) for r in rows if r[8]])
print('waiting_on_remove',[r[0] for r in rows if r[9]])
print('drift',[r[0] for r in rows if 'rebuilt for drift' in r[6]])
