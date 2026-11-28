# Daily sweep 463, plus the guest-list backfill check (4 Nov)

| File | Bytes / sha256 |
|---|---|
| `sweep.txt` (463c) | 42,406 / 76b49956eea00a03 |
| 463b (replaced) | 41,598 / 3af292b4c9b196ba |
| 463 (replaced) | 40,253 / f2a2b752d6a13d82 |
| Live input: Daily sweep, trig_01MdfUFg2qrebDWgiHwncgnd, read back 4 Nov (equals `../inbox-split/sweep.txt`) | 39,131 / 6783dd01 |

**Build:** `python3 patch.py <live sweep> <out>` asserts the live hash, each of 3 edits once, and no new em dash. Patched twice, byte-identical.

**The receipts r1b sweep was never deployed.** The live sweep is still round 4's (6783dd01), so these edits sit on that base. The receipts r1b sweep (40,914 / e5d2f31b) is a separate change that's still waiting.

## No Monday routine exists

The CTO's item 3 says "in the Monday routine", but none of the 11 enabled tasks runs on Mondays only: the only weekly task, FT Community directory sync, runs on Saturdays. The Founder Thesis guests list is kept by the Daily sweep's STEP 3g (decision 191), PART B, at 15:10 JST every weekday, Monday included. So 463.1 goes there, and it checks every weekday, not only Mondays.

## Edits

1. **463.1 (STEP 3g).** Before, 3g took only Founder Thesis Engagements at Recorded or Form filled. A guest whose row stayed at Booked after recording never got on the list. Now it also takes every Founder Thesis Episode whose Recording date is today or earlier, whatever the Engagement's Status. That puts a guest on the list in the week of the recording.
   - **Left out:** an Episode at Not releasing, as before, and one at Hold. A Hold guest is added once the Episode leaves Hold, and Magic Bus stays out.
   - **Report:** it names any recorded FT guest still missing.
2. **463.6 (STEP 4).** It's a new first flag, "No owner": an open guest Engagement (Kind empty, not closed or Published) with an empty Waiting on.
   - **Skipped:** an Outbound row at New, which waits on no one (decision 167).
   - **When the owner is plain:** a booked recording with nothing open is Guest or PR, and an unanswered mail from their side is Zoya's. The sweep sets it with a Claude note line.
   - **Otherwise:** a report line under For Akshay, and nothing changes.
   - Both counts go in the report.

## The backfill: 10 of the 15 are already on the list

Checked read-only in the guests database (collection://b460a8fa) on 4 Nov ~14:20 JST, by name, surname and company:

| Named as missing | Already on the list as |
|---|---|
| Sreepriya NS | Sreepriya N S (Entrust Family Office) |
| Shubham Garg | Shubham Garg (CodeVyasa) |
| Jaydeep (Rebel Foods) | Jaydeep Barman (Rebel Foods) |
| P. Venkatesh | P. Venkatesh (Maveric Systems) |
| Deepak Chand Thakur | Deepak Thakur (NPST) |
| Sri Misra | Srikumar Misra (Aarna Protocol) |
| Vinod K Singh | Vinod Singh (Concirrus) |
| Manu J. Nair | Manu Nair (EtherealX) |
| Sheetanshu Tyagi | Sheetanshu Tyagi (EMO Energy) |
| Vinay Kumar Sankarapu | Vinay Sankarapu (Arya.ai) |

**Truly absent (5):** Sameet Gupte (EvoluteIQ), Sandeep Bommireddi, Anjali Bansal, Pranav Dangi and Amit Koushal.

**Check:** if the 15 came from the public page (podm.in/guest-list), those 10 rows may exist but not show there. Look at their published state, Status, or a view filter, rather than adding duplicates.

**The one-time write is the CTO's** (one Notion writer). It's 5 rows, built as STEP 3g says:
- Guest, Company, Role and What the company does, from the eval and People;
- Tags from the field's options only;
- LinkedIn from People;
- no unverified values.

The new 3g would also add them at its first run.

**Co-guest:** Rajmohan Krishnan (Entrust, with Sreepriya) has no row of his own. 3g's co-guest rule adds him.

## 463b: the CTO's correction to 463.1 (4 Nov 15:14)

Item 1's "here" is the FT Community list (collection://aefa65ce, view "WhatsApp: to add"), not the guest list. The guest-list sync above stays.

**A new STEP 3k**, in PART B after 3g, applies the same rules as calendar STEP 4b, which covers only the last 14 days:
- **Who:** the guests of every Founder Thesis Episode whose Recording date has passed, except Not releasing and Hold. Magic Bus stays out.
- **Each guest has one FT Community row,** found by Person, else exact name plus company. A missing row is created with Name, Company, Person, Source FT guest, Type Founder or Investor, Membership To invite, and Captured today.
- **A row that's found** gets Person linked if it's empty. Membership is set to To invite only if it's empty, and nothing else changes.
- **An empty Blurb with the transcript in:** a report line under "For the blurb chat". With no transcript, a report line only.
- **Never:** writing Blurb, Blurb link or a "Blurb, <date>" section, or running founder-thesis-blurb (Akshay, 25 Oct: the Codex blurb chat writes blurbs). The CTO's "hand it to the blurb process" is therefore a report line for that chat, not a write.
- **At most 15 creates a run.**
- **Sameet:** his row already exists (Invited, no Blurb). 3k leaves Membership as it is and lists him as "blurb due" once his transcript is in.

**Also (Cleanup should-fix 5):** STEP 3i's transcript-row Next action and the decision 376 line now name Mamatha (decision 456), not Ranjita. The calendar routine got the same change in 454c.

## 463c: decision 465 (one after-recording process)

**Scope (3g's Episode trigger and 3k):** Founder Thesis Episodes recorded from 2026-09-01 to today, with a usable recording: not Not releasing, Hold or corrupted, so Magic Bus stays out. The cutoff keeps 600+ older episodes out. 3g's Engagement-based trigger (Recorded or Form filled) is unchanged.

**Matching, never by name prefix:**
- **The guest list (3g):** by the People row's LinkedIn, else exact full name plus company. Case and spacing are ignored, so "SREEPRIYA N S" matches "Sreepriya NS". Saket Saurabh at Nexla isn't Saket Saurav at Refit Global.
- **FT Community (3k):** by the Person relation to the guest's People row only. A name-only hit is reported, never linked.

**The invite ask (3k):** while Membership is To invite or Invited, the guest's Founder Thesis Engagement carries one "Akshay: invite <first name> to the FT Community" segment, with Akshay in Waiting on. It's added once, and never if "WhatsApp addition pending" is already there. Once Membership is Added, the WhatsApp routine's b2 clears it.

**The backfill (465.3)** is these steps' first runs, at most 15 Community creates a run. A read-only gap audit with "before" counts runs separately. The CTO verifies the "after" counts once this is live.

**Status:** built, not replayed. Ready for Cleanup. Nothing is deployed and nothing is written.

## The decision 465 backfill: "before" counts (read-only audit, 4 Nov ~15:50 JST)

The full audit is `audit465-before.json`: names, companies, statuses and Notion ids, with no contact details. It covers Founder Thesis episodes recorded from 1 Sep to 4 Nov: 29 episodes and 30 guests. Entrust has two guests.

**Excluded (2), both at Not releasing:**
- Karmendra Kohli (SecurEyes).
- Matthew Spacie (Magic Bus). Magic Bus is Not releasing, not Hold, so the rules' Not releasing exclusion already covers it.

| Gap | Before | Who | What fixes it |
|---|---|---|---|
| (a) Guest list missing | 1 | Sameet Gupte (EvoluteIQ) | 3g, now from Episodes |
| (b) Community row missing | 1 | Saket Saurabh (Nexla). The "Saket Saurav" row is Refit Global, a different person | 3k creates it, matched by Person |
| (c) Added but still asked | 0 | none | WhatsApp b2 |
| (d) Invited, but Akshay says added | 1 | Sankalp Arora (Gather AI): Your call 25 Oct "added to whatsapp group, remove from my queue" | WhatsApp 3a (3), from the Claude note copy |
| (e) Blurb due (transcript in) | 5 | Bhanu Pratap Singh Tanwar, Ashish Goel, Saravana Maruthamuthu, Srinivas Choudhary, Raunak Bhinge | 3k reports them for the blurb chat |
| (f) No invite ask while To invite or Invited | 1 | Sankalp Arora: clears once (d) sets him to Added | WhatsApp |

**Two more** had an empty Blurb with a transcript but are excluded from (e): Anmol Madan (Unresponsive) and Ramki Gaddipati (Declined). 3k now flags a blurb only while Membership is To invite, Invited or Added. That's sweep 42,406 / 76b49956.

**Expected "after" counts:** (a) 0, (b) 0, (c) 0, (d) 0 and (f) 0 after the first sweep run on 463c and the next WhatsApp run. (e) stays at 5 until the blurb chat writes them.

**Not gaps, but worth a look:**
- **Matched on name plus company, because People has no LinkedIn:** Gautam Rege, Anuj Tandon, Abhinav Parashar, Ankit Mehra and Sreepriya NS.
- **Matched with no Organisation either:** Amit Patni, Rohan Ganapathy, Rajmohan Krishnan and Saket Saurabh. Amit Patni's Community row says "Raay Neo Pharma", while the guest list says "RAAY Global".
- **Jayasimha Nuggehalli** is Published, but his guest-list row has no Episode link or Released date. 3g's "Episode now Published" rule should fill them.
- **Stale statuses:** several October recordings are still Episode Status Scheduled (Ankit Mehra, Raunak Bhinge, Amit Das).
- **The People "In WhatsApp group" checkbox** disagrees with Membership Added for many people. No routine owns that checkbox, so it's a candidate to retire or derive.
