# Daily sweep 463, plus the guest-list backfill check (4 Nov)

| File | Bytes / sha256 |
|---|---|
| `sweep.txt` (new) | 40,253 / f2a2b752d6a13d82 |
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

**Status:** built, not replayed. Ready for Cleanup. Nothing is deployed and nothing is written.
