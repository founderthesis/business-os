# Handoff (8 Oct 2026, updated end of day)

Open work for the next session. Read CLAUDE.md, docs/decisions.md (81 to 89 are the newest, plus the 9 Oct override of 87) and this file first.

## For the FT eval refresh session (15 Oct, from the business-os session)
- FT Community cleanup is applied: Membership = Added is 511 (99 rows created with Needs review ticked, 33 set to Left, the other 412 already Added). Its own page could not take a comment (archived), so this note is the handoff.
- A data accuracy pass on FT Community (LinkedIn, company, one-liner, Person links) is running and writes only to FT Community. The Founder Thesis Community database and its page were not touched. Refill the directory after that pass lands (see docs/notion.md for its row).

## Done
- 8 Oct: the rewritten prompts (decisions 81 to 86) are live on all four routines, verified with get_trigger.

## Finished 8 Oct (second session)
- Waiting on: views "Akshay: waiting on me" and "Mamatha: waiting on me" (Engagements and Deals), "FT: Sponsored pipeline"; Waiting on on FT: Today, un#: Today, All shows: Today. Closures confirmed. Waiting on was then filled on 9 Oct by Notion AI (override of decision 87, see docs/notion.md); the Deals cold target list stays blank (decision 89).
- FT Network: all 469 rows loaded (436 Added), views All / To invite / Needs review, page "Founder Thesis community: members" under the home page. 149 rows need review (first names only, missing or ambiguous People matches). Counts in docs/notion.md.

## Waiting on Akshay
- FT Network Needs review: 149 rows (view "Needs review"). Biggest groups: first-name-only members (Vishal, Jag, Tarun, Sanchit, Saurabh, Siddharth, Madhusudhan, Deep, Ram, Ranjeet, Bhanu, Preksha and others), two People rows each for Abhinav Jain, Manish Gupta and Rahul (Zebpay), and People duplicates Rahul Pagadipati / Pagidipati and Ramanathan RV.
- Members page: 13 Added members have no one-liner (doc-list rows with no intro blurb); fill them or leave the cell blank. Share the page with the group when happy.
- .claude/settings.json: the "mcp__Claude_Code_Remote" allow rule does not match the server name (claude-code-remote).
- Patron paragraph: live in the calendar routine since 9 Oct (decision 95).
- Scimplify: one guest or two (Salil Srivastava, Sachin Santhosh)?
- Transcripts: run routines/transcripts-backfill.md in Claude Code on his Mac (needs his folder paths); set up routines/transcripts-after-recording.md as a desktop scheduled task.
- Upload downloads/all-skills.zip skills in claude.ai.

## Next projects
- FT Community directory split (decision 186): add the 66 members from the 14 Oct 511 list to the public database, link FT Community rows to their public row, drop Company, One-liner and LinkedIn from FT Community, retire People "In WhatsApp group", teach the WhatsApp routine to create and clear public rows, and set up the Saturday directory routine (routines/community-directory.md).
- Built to Share migration.

- Templates (decision 98): calendar and evals prompts read from Templates and are live (9 Oct). inbox.md and daily-sweep.md are updated in the repo but not yet pushed to their triggers (inbox trig_0189eZvAD8x4357cfevgZ3No, daily sweep trig_01MdfUFg2qrebDWgiHwncgnd); their template rows match the wording already live, so push them with the next change to either prompt.

## 15 Oct, inbox prompt (from the host-boards session)
- Decision numbers: 190 FT Community source of truth, 191 podm.in/community, 192 host boards never show Pre-call needed, 193 Saurabh-forwarded pitches (reply on the original pitch message when it also reached ad@).
- Live inbox prompt was pushed 09:18 UTC from the merged file (your community and guests-list changes included) and verified byte for byte, except that it still cites "decision 190" in STEP 7d c and "decisions 122, 192" in STEP 6c d. The next push from the repo fixes both.
- Size cap: update_trigger rejects prompts over 65,536 bytes. Inbox is at 64,764. Check `len(prompt.encode())` before pushing, and push from the main session, not a subagent (a subagent's push was cut off mid-prompt today and left a truncated live prompt).
- Re-pushed from 1e442a3 by the community session after its own stale push overwrote yours for a few minutes; live now equals the repo file, decisions 192 and 193 cited correctly. Before any push, fetch and compare the live prompt with origin first.
