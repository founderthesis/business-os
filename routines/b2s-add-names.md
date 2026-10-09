# B2S: add names to the pipeline

Chaandini pastes this into Notion AI (or Claude) with her list of names. It checks for duplicates before it creates anything, so the same founder never gets two rows. Decision 97 says new names go in through Claude; this is how.

## Prompt

```
Add these founders to the Built to Share pipeline in the ThePodium Business OS.

People: https://app.notion.com/p/f54094b86c3549dead74c0034afad86c
Organisations: https://app.notion.com/p/4e484b1c510b42ce9ea979307bff31e4
Engagements: https://app.notion.com/p/5e77c373909a4bf6b9195570de46c63b

For each name:
1. Find the person in People: by email first, then LinkedIn, then exact full name with the same company. If found, use that row and fill only empty fields. If not found, create one with Name, Email, LinkedIn, Role, Organisation, Tags = B2S guest pipeline, Source = Manual.
2. Find the company in Organisations by name or website domain. Create it only if it is not there (Type = Startup).
3. Check Engagements for a row with this person as Guest and Show = Built to Share. If one exists, do not create another: tell me its Status and Host verdict.
4. Otherwise create the Engagement: Name "<Person> @ <Company>, Built to Share", Guest, Organisation, Show = Built to Share, Direction = Outbound, Status = New, Host verdict = Not asked, Tier = Tier 1.5 (Tier 2 if the bucket is More of the same), Tags = the bucket I give, Source = Manual, Captured = today.
5. Also check FT: if the person already has a Founder Thesis Engagement or is an FT guest, say so next to their name.

At the end, list what you created, what already existed, and anything you could not match.

Bucket for this list: <Outlier / Recently IPO'd / Pre-IPO / Big Indian founder / Big global founder / Global unicorn / More of the same>
Names (one per line: name, company, email or LinkedIn if known):
<paste here>
```
