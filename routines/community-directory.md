# FT Community directory sync

Scheduled routine "FT Community directory sync" (trig_01EoP9zjHnaAeyKthSWdcums), Saturdays at 09:47 JST, with the Notion and Apollo connectors (decision 186).

It keeps the public members directory (Notion database "The Founder Thesis Community") in step with FT Community (decision 190). FT Community is the single source of truth: people edit only FT Community, and the public database is a locked, read-only copy that agents regenerate. A published view of FT Community itself would expose every column and every row (Notion has no row-level security), so the copy is generated instead. The WhatsApp routine mirrors three times a day; this Saturday run also fills missing cities.

Public fields only: Name, LinkedIn, Company, What they do (the FT Community One-liner), City, Type. Never an email, phone, WhatsApp id, blurb, review note, Person link or any other Business OS link.

City is stored on FT Community and comes from Apollo's free people search, by LinkedIn URL plus a location filter, one metro at a time; Apollo's paid enrichment is never used for this. Metro labels group a region so it works for meetups (Delhi NCR covers Delhi, Gurugram, Noida, Faridabad and Ghaziabad).

## Prompt

```text
You run the weekly sync of the Founder Thesis Community directory. No human is watching this run: never stop to ask a question.

TOOLS: Notion and Apollo connectors (ToolSearch "+Notion", "+Apollo" if deferred). If Notion is missing, stop and say so. Without Apollo, skip STEP 1 and say so in the report.
APOLLO: use ONLY apollo_mixed_people_api_search, which is free. Never call apollo_people_match, apollo_people_bulk_match, any reveal or waterfall, or any other tool that spends credits.

SINGLE SOURCE OF TRUTH (decision 190): FT Community is the only place member details live and are edited. The public database is a read-only copy for the web: never edit it except to mirror FT Community.

NOTION
- FT Community (source of truth): collection://aefa65ce-8b38-40cb-8ef2-19d167adeea0 (Name, Company, One-liner, Type, LinkedIn, City, Membership, Person)
- People: collection://e6c44319-7f81-4da6-8b80-8441a4875d7a (LinkedIn, used when the FT Community row has none)
- Public directory (copy): collection://2ecb2b1f-6524-4a03-9f3b-87e5a365ef9b (Name, Company, What they do, City, Type, LinkedIn)
Fetch each data source once to confirm property and option names. Never read or write the Credentials page.

STEP 1. CITY (FT Community rows with Membership Added and City empty)
LinkedIn = the row's LinkedIn, else the linked People row's LinkedIn, as https://www.linkedin.com/in/<slug>. For each batch of up to 100 LinkedIn URLs, call apollo_mixed_people_api_search with person_linkedin_urls and person_locations set to one metro at a time, per_page 100, and give every returned person that metro (match back by first name plus organization or title; if unsure, narrow the batch until certain). Metros, in order, with the location strings to send:
Delhi NCR [Delhi, New Delhi, Gurgaon, Gurugram, Noida, Faridabad, Ghaziabad]; Bengaluru [Bengaluru, Bangalore]; Mumbai [Mumbai, Navi Mumbai, Thane]; Pune [Pune]; Hyderabad [Hyderabad]; Chennai [Chennai]; Kolkata [Kolkata]; Ahmedabad [Ahmedabad, Gandhinagar]; Jaipur [Jaipur]; Chandigarh [Chandigarh, Mohali, Panchkula]; Kochi [Kochi, Cochin]; Indore [Indore]; Singapore [Singapore]; Dubai [Dubai, Abu Dhabi]; SF Bay Area [San Francisco, San Jose, Palo Alto, Mountain View, Menlo Park, San Mateo, Sunnyvale, Oakland]; New York [New York]; Seattle [Seattle, Bellevue, Redmond]; London [London].
Still unplaced: country filter [India] gives "Other India", [United States] gives "Other USA", any other country Apollo returns gives "Elsewhere". Not found at all: leave City empty. Never guess a city.
Write each City found to the member's FT Community row. Never change any other FT Community field.

STEP 2. MIRROR (same rules as the WhatsApp routine's STEP 4)
- Source: FT Community rows with Membership Added. The public value of each field: Name = Name; Company = Company; What they do = One-liner (empty if it holds an email, phone number, handle or money figure); Type = Type; LinkedIn = LinkedIn, else the linked People row's LinkedIn; City = City.
- Read both sides with one SQL query each. Match by Name (case and accents ignored); if a name repeats, by LinkedIn.
- No public row for a member: create it (batches of up to 100 pages per call). A public row whose six fields differ from the member's values: update it to the FT Community values (an empty FT Community field clears the public one). Write only rows that differ.
- A public row with no matching member, not already named "REMOVE: ...": if an unmatched member has the same LinkedIn, it was renamed: rename the public row and update it. Otherwise rename it "REMOVE: <Name>" and clear every other field, for Akshay to delete.
- Write nothing else there: never an email, phone number, WhatsApp id, Blurb, review note, Person link or link into the Business OS.

STEP 3. REPORT
Plain and short, no em dashes: members (Added), cities found this run (counts per city), members still without a city, public rows created, updated and marked REMOVE (names), rows already waiting as REMOVE, Apollo calls made, and confirm no credit-spending Apollo tool was called.
```
