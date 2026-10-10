# Add guest names to a show's pipeline

Chaandini (or anyone booking guests) pastes this into Notion AI or Claude with a list of names. It checks People and Engagements before creating anything, so the same person never gets two rows. Works for any show; new names land at Tier 1.5, Not asked, so they show up in "Chaandini 3: needs the host's yes" (decisions 101 and 104).

## Prompt

```
Add these guests to the pipeline in the ThePodium Business OS.

Show: <Built to Share / Human by Design>
Bucket (optional): <for example Outlier, Pre-IPO, AI researcher>

People: https://app.notion.com/p/f54094b86c3549dead74c0034afad86c
Organisations: https://app.notion.com/p/4e484b1c510b42ce9ea979307bff31e4
Engagements: https://app.notion.com/p/5e77c373909a4bf6b9195570de46c63b

For each name:
1. Find the person in People: by email first, then LinkedIn, then exact full name with the same company. If found, use that row and fill only empty fields. If not found, create one with Name, Email, LinkedIn, Role, Organisation, Source = Manual.
2. Find the company in Organisations by name or website domain. Create it only if it is not there.
3. Check Engagements for a row with this person as Guest and the same Show. If one exists, do not create another: tell me its Status and Host verdict.
4. Otherwise create the Engagement: Name "<Person> @ <Company>, <Show>", Guest, Organisation, Show, Direction = Outbound, Status = New, Host verdict = Not asked, Tier = Tier 1.5, Tags = the bucket if given, Source = Manual, Captured = today.
5. If the person is already a guest or in the pipeline on any other show, say so next to their name.

At the end, list what you created, what already existed, and anything you could not match.

Names (one per line: name, company, email or LinkedIn if known):
<paste here>
```
