# Notion workspace map

Created 2 Oct 2026 under the private page **ThePodium Business OS**:
https://app.notion.com/p/3eb19a301a7f81469e8fe712af568c43

Data source IDs are what scripts and routines use.

| Table | Data source |
|---|---|
| People | `collection://e6c44319-7f81-4da6-8b80-8441a4875d7a` |
| Organisations | `collection://c43c280a-3b37-4821-96ef-dab688a53aea` |
| Engagements | `collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5` |
| Shows | `collection://ebca6861-4d71-4555-a6ec-6ed76cc0c733` |
| Episodes | `collection://5d250752-6db8-4ab6-8467-c68f5838278a` |
| Tasks | `collection://751c3aed-8d7c-4a35-85f3-3a7815f7209b` |
| Activities | `collection://290f715d-fd45-4203-ade6-3642c2326c6c` |
| Queue | `collection://af59132c-92cb-4e87-85f0-266bd07309c4` |
| Templates | `collection://b2976a03-9983-49e1-96cf-d237a395148d` |
| Credentials | `collection://e5ccd27a-cb8b-436e-8269-2dcd4210b1a7` (never read by routines) |

Akshay's dashboard (page 3ee19a301a7f81c58589cc9ce372f86e): agent switches (Mode, Sending, cap), morning brief, Decide, Reminders, Heads-up, My move, In production. Queue gained Thread ID and Sent.

Views on the home page: Akshay's dashboard (Queue), Release calendar (Episodes), Team tasks (Tasks by owner), Pipeline (Engagements by stage), Network (People who are FT guests or in the WhatsApp group). In Engagements: PaaS pipeline (board by stage) and US VC outreach (table by rank; quick filters on Tags so "No email" can be excluded).

Shows seeded: Founder Thesis, alpha un#, Built to Share, Human by Design. Hosts get linked once their People rows exist.

Old tables are untouched until their data is migrated and checked.

## Imports

| Date | Batch | What | Result |
|---|---|---|---|
| 2 Oct 2026 | master-list-2026-10-02 | Founder_Thesis_Master_People_List (8 Sep copy) | 683 People and 654 Organisations created, counts reconciled (687 rows = 683 + 2 merged + 2 unnamed numbers held back). 10 wrong LinkedIn URLs corrected before import. Sridhar Muppid / Sridhar Muppidi confirmed as one person by Akshay: kept row renamed and linked to both companies; the other row is marked "Merged into another row" for deletion in the Notion UI. |
| 2 Oct 2026 | blue-inflight-2026-10-02 | Blue in-flight FT and Spotlight episodes (Hold, Recorded, Slotted, Doc Ready, Video QC) | 31 Episodes created (Blue held 31, not the 28 in the audit: 4 new Recorded form submissions, and the Pant Project has moved to Published). People 683 to 692: 22 guests matched (19 by LinkedIn, 3 by exact name), 9 created. Planned release set from the Blue due date on 22. PR contacts not imported: Blue holds them as emails only, pending Akshay's call |
| 2 Oct 2026 | paas-leads-2026-10-02, us-vc-2026-10-02 | Notion PaaS Leads (15) and US VC Podcast Outreach (774 firms) | 789 Engagements (774 US VC, 15 PaaS), 780 Organisations, 2,944 People, 8 call-note Activities. 55 contacts matched existing People (LinkedIn, email, or name plus organisation); 4 existing guests got their organisation linked. SilverX founder resolved to Ajay Jain and Silverneedle renamed "SilverX (formerly Silverneedle)"; the duplicate SilverX organisation is named "DELETE: ..." for deletion in the UI. Trackerwave founder is Pradeep Vadakkekhatt. People total also reflects Akshay deleting the merged Sridhar row |
| 2 Oct 2026 | episodes-2026-10-02 | Episode Inventory (582), Article Queue (439), all Blue guest cards (FT, alpha un#, Hissa, FastCode), Blue inventory tiers, PR contacts from Blue guest forms, Inner Journeys guests (People only) | 680 Episodes (582 inventory + 21 Article Queue only + 77 Blue only), 228 Engagements (one per Blue guest card, 385 stakeholder links), 466 People (guests and PR contacts, names guessed from the address and tagged "Name guessed"), 115 Organisations (22 PR agencies). 553 guests matched existing People. 120 Blue FT cards merged into their inventory episode; 15 Blue inventory cards for repeat guests not attached (links already on the episodes). Design jobs and prompts not migrated (Akshay) |
| 3 Oct 2026 | episodes-2026-10-02 (fix) | Duplicate episode check after Akshay spotted three CleverTap rows | An archived Blue card with no video (recorded 27 Oct 2024) had been created as a third CleverTap episode. Its engagement now points at "Building a $100mn ARR SaaS company" (Outcome Done, recording date set) and the extra row is titled "DELETE: ...". Two Article Queue rows that were Shorts, not episodes, are also titled "DELETE: ...". All appear in the Episodes "To delete" view. Script fixed so a re-run does neither |
| 3 Oct 2026 | episode-names | Episode naming and re-upload merge (decisions 51, 52); People dedupe applied (decision 53) | Episodes renamed "Guest @ Company - Show" (684), old titles moved to "YouTube title" for inventory and Article Queue rows only (Blue placeholder titles cleared on 75). 22 re-uploads and Beyond Campus republishes merged; drops titled "DELETE: ...". People: 18 duplicate pairs merged per Akshay's comments and the web check, 19 rows marked "Merged into another row". Saurabh Garg B2S practice recording, its episode and engagement marked for deletion |
| 3 Oct 2026 | episode-names (answers) | Akshay's answers on repeat guests | Merged as one recording: Ankit Mehrotra, Nakul Kumar, Preksha Kaparwan, Bharat Sethi, Hitesh Dhingra (3 uploads), Bhavik Vasa. Second recordings kept as V1/V2: Amit Gupta, Ankit Mehta, Ashish Munjal (and Anand Jain). Three Roshan Abbas Spotlight clips marked for deletion as not episodes. Vijesh Sharma left as is |
