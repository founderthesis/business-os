# Canonical wording for the CTO's Notion edits (Akshay, 2 Nov, items 7 and 8)

Read-only check on 2 Nov, around 17:00 JST. "Rules for Zoya: follow-ups" and "2. Precall requested, then nurture" already carry the CTO's 16:58 rules: "The link stays inside its sentence" and "Peers". This note gives the exact template text that's left to change.

## Item 8: booking link inline

**Where the MakersHive mail came from:** "2. Precall requested, then nurture" (3fa19a301a7f8197be92d74c8f8e0660), Chain 2, Mail 2. It also breaks PLAIN ENGLISH ("Circling back") and uses " - " as a dash.

| Template | Old | New |
|---|---|---|
| Chain 2, Mail 2 | Circling back on the prelim call for {guest} - any open slot works: podm.in/30min | any update on the prelim call for {guest}? any open slot here works: podm.in/30min |
| Chain 1, Mail 2 | Circling back on {guest} - Akshay's really keen on this one. Whenever {guest} has 30 minutes for the planning call, we'll make it work: podm.in/30min | any update on {guest}? Akshay would really like to have {guest} on. any open slot here works: podm.in/30min |
| Chain 1, Mail 4 and Chain 2, Mail 7 | ... Any slot here works: podm.in/30min | ... any open slot here works: podm.in/30min |
| Chain 2, Mail 4 | We'd love to hear {guest}'s story too, any open slot here works: podm.in/30min | We'd love to hear {guest}'s story too. any open slot here works: podm.in/30min |

In each new line the link stays in the same paragraph as its sentence: one `<p>` in HTML and one line in plain text.

**Also on these pages:**
- Chain 1 Mail 2 uses "keen", and Chain 1 Mail 4 and Chain 2 Mail 7 use " - " as dashes. PLAIN ENGLISH bans "keen".
- Suggested for Chain 1 Mail 4: "Akshay asked me to check in about the planning call. He was just reading about {one public detail} and wants to get {guest}'s story on the show. any open slot here works: podm.in/30min".

**"Mail and WhatsApp wording"** (3fa19a301a7f81b6a807d0f01847dae7): no change needed.
- "Commercials asked before the precall" already has "any open slot here works: [podm.in/30min]" as one paragraph.
- Every other approved toggle with a booking link already has it inside its sentence: "FT precall invite to PR", "FT precall, PR wants to talk first", "Recording slot request", "Reschedule from our side", "Declined invite", "Sponsored: detailed package questions", "What the prelim call covers" and "Editorial or commercial?".

The forced break was in rendering, which the Zoya build fixes: BOOKING LINKS, one `<p>` per paragraph.

## Item 7: the reference guest list

**Where:** a new toggle "Reference guests (verified)" on the wording page, or a small table on Rules for Zoya: follow-ups, above "The nine routine pages". The guest-example rule in the Zoya build reads it, and checks names against Episodes and podm.in/guest-list.

**Format:** one row per guest, about 20 to 30 rows, enriched once:

| Guest | Company | Sector | Show | Released (month) | Standing | Use for |
|---|---|---|---|---|---|---|
| Hitesh Dhingra | The Man Company | D2C, grooming | Founder Thesis | <month from Episodes> | <1 to 3> | D2C, consumer brands |

**Rules for the list:**
- Released comes from the Episodes row. Never write "recent" past 90 days.
- Standing: 1 means a household name or category leader, 2 a well-known founder, 3 other.
- Use for: the sectors a mail may cite this guest to.
- A guest goes on only after their Episodes row is checked.
- **To check before listing:** Fable Street, Plum Goodness and Foxtale (Akshay, item 7). Remove the "recent" wording for Hitesh Dhingra and Dhruv Madhok wherever it's in a template.

Picking, as the rule says: sector match to the reader first, then standing, then recency.
