---
name: "ft-community-blurb"
description: "Write the welcome blurb that introduces one new member of the Founder Thesis WhatsApp community (a founder or investor Akshay Datt has interviewed), in Akshay's voice, from the call transcripts, the episode transcript, LinkedIn via Reach MCP and Tracxn. Trigger on \"write the blurb for Ankur\", \"community blurb for a guest\", \"blurb with skills/ft-community-blurb\", or a comment asking to change an existing blurb. Returns DRAFT, SOURCES and NOTES FOR AKSHAY. Writes nothing to Notion and sends nothing."
---

# ft-community-blurb

Akshay welcomes new members of the Founder Thesis community in a WhatsApp post: one blurb per person, read by several hundred founders and investors. He has spent an hour or two talking to each guest, and the best blurbs pass on what he learnt. The reader should come away knowing something about an industry, not just a CV.

Read `examples.md` in this folder before you write anything. Those are his real blurbs, and they are the style guide.

## Research

Do this once per guest and keep it in this chat as a research file (`research-<guest-slug>.md` in your scratchpad, or one block in the chat): every fact on its own line with its source. A later edit reuses it and only looks up what the edit needs. If a source can't be reached, say so in the file and carry on.

1. **Notion** (ToolSearch "+Notion"). The guest's Founder Thesis Engagement (Engagements, collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5, search the name): its page body holds the precall notes and the eval. Its Episode (collection://5d250752-6db8-4ab6-8467-c68f5838278a): download the Transcript file and read all of it, keeping timestamps. The guest's People row has the LinkedIn URL. Not recorded yet: say so and work from the precall.
2. **Call notes.** Search Google Drive and Gmail for the guest's name. Precalls and some recordings leave a "Notes by Gemini" doc (title "<Guest> and Akshay Datt ...", also mailed from gemini-notes@google.com). Read its Transcript tab, not just the summary. Pick up any backgrounder, deck or PR note filed under their name too.
3. **LinkedIn via Reach MCP** (ToolSearch "Reach_MCP"; list_accounts gives the account id). scrape_profile reads the profile; list_user_posts reads recent posts. No URL yet: scrape_search on name plus company, then confirm with scrape_profile. Read only: never visit_profile, message, invite, comment or react. Confirm the profile is this person's, then note role, career and what they're pushing now.
4. **Tracxn** (call `load_prompt` first). Funding, investors, revenue, headcount, valuation, acquisitions. Cite it as "Tracxn".
5. **Web**, for anything else. Keep the URL.

Anything the guest said off the record, or asked not to share, stays out of the blurb; list it in the notes as withheld.

## Angle

Before writing, put three short answers at the top of the research file.

- **What did Akshay learn?** Find the moments in the transcript where he is surprised, pushes back, or asks a follow-up because he's working something out, and where the guest explains how the industry really works. That is usually the strongest point in the blurb: teach the group what he learnt.
- **The big picture.** The industry stack and where this company sits in it, why the space is hard or unusual, and why this founder has the right to win.
- **Something people already know.** A place, a brand, a product they've used, a story they've heard, that makes the business click.

Then the shape: open with the big picture or the thing worth learning, then zoom into the company, its model, its numbers and the founder's journey. Big deals, exits and funding come later, not in the opening line. The examples show how much he varies this, so treat it as a direction, not a template.

## Write

Write as Akshay. Pick the examples closest to this guest (an investor, a deep-tech company, a consumer brand, a bootstrapped services firm) and write the way he does there.

Akshay is the thought leader here, sharing his own take, not a reporter describing the guest's views. Ideas are his to state, in first person where it helps: what he believed going in, where he pushed back, what changed his mind. His own rewrite of an opening, 23 Nov:

> When Ankur told me that Rio is a pharma quick comm business, I spent a lot of time pushing back: why wouldn't a Blinkit rule this market too, given they already have density and distribution? By the end of our conversation Ankur had changed my mind. You see, the consumer behaviour quick commerce runs on is totally different from how pharma retail works. For one, the consumer is not brand agnostic. They don't search for oat biscuits, they search for the specific brand their doctor prescribed. That means the basic quick commerce Pareto rule (20% of the assortment covers 80% of the demand) breaks. The business breaks if you don't stock the long tail.

- **Length.** Let the examples set it. Most run 120 to 200 words.
- **Name.** First mention is the full name followed by `(<LinkedIn URL> - @{WhatsApp handle})`, as in his recent blurbs. Leave the handle as that placeholder; Akshay tags the person in WhatsApp.
- **Numbers.** Figures the guest gave on the call can go in as stated. They are self-reported, so say that in the notes, not in the blurb.
- **No em dashes, ever.** Short varied sentences, contractions, specifics over generalities.

## Return

```
BLURB <guest> v<n>

DRAFT:
<the blurb>

SOURCES:
<fact> | "<transcript quote>" [hh:mm:ss]
<fact> | Tracxn
<fact> | <URL>

NOTES FOR AKSHAY:
- <numbers that are self-reported, and where Tracxn or the web disagrees>
- <framings that are yours rather than the guest's, such as an analogy or a "right to win" claim>
- <anything unverified, left out, or withheld as off the record>
```

One SOURCES line per fact. No fact without a source; never guess a number. If Akshay's comment asks for a fact the sources don't support, flag it in the notes instead of writing it.

For an edit, keep what he didn't comment on, change what he asked, and return the next version in the same format.

This skill writes nothing to Notion and sends nothing. Whoever asked for the blurb places it.
