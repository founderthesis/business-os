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

Views on the home page: Akshay's dashboard (Queue), Release calendar (Episodes), Team tasks (Tasks by owner), Pipeline (Engagements by stage), Network (People who are FT guests or in the WhatsApp group).

Shows seeded: Founder Thesis, alpha un#, Built to Share, Human by Design. Hosts get linked once their People rows exist.

Old tables are untouched until their data is migrated and checked.

## Imports

| Date | Batch | What | Result |
|---|---|---|---|
| 2 Oct 2026 | master-list-2026-10-02 | Founder_Thesis_Master_People_List (8 Sep copy) | 683 People and 654 Organisations created, counts reconciled (687 rows = 683 + 2 merged + 2 unnamed numbers held back). 10 wrong LinkedIn URLs corrected before import. Sridhar Muppid / Sridhar Muppidi flagged as a possible duplicate for Akshay. |
