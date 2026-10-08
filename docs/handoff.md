# Handoff (8 Oct 2026, updated end of day)

Open work for the next session. Read CLAUDE.md, docs/decisions.md (81 to 88 are the newest) and this file first.

## Done
- 8 Oct: the rewritten prompts (decisions 81 to 86) are live on all four routines, verified with get_trigger.

## Finished 8 Oct (second session)
- Waiting on: views "Akshay: waiting on me" and "Mamatha: waiting on me" (Engagements and Deals), "FT: Sponsored pipeline"; Waiting on on FT: Today, un#: Today, All shows: Today. Closures confirmed. No bulk backfill (decision 87): routines fill Waiting on as they touch rows. Deals have none yet.
- FT Network: all 469 rows loaded (436 Added), views All / To invite / Needs review, page "Founder Thesis community: members" under the home page. 149 rows need review (first names only, missing or ambiguous People matches). Counts in docs/notion.md.

## Waiting on Akshay
- FT Network Needs review: 149 rows (view "Needs review"). Biggest groups: first-name-only members (Vishal, Jag, Tarun, Sanchit, Saurabh, Siddharth, Madhusudhan, Deep, Ram, Ranjeet, Bhanu, Preksha and others), two People rows each for Abhinav Jain, Manish Gupta and Rahul (Zebpay), and People duplicates Rahul Pagadipati / Pagidipati and Ramanathan RV.
- Members page: 13 Added members have no one-liner (doc-list rows with no intro blurb); fill them or leave the cell blank. Share the page with the group when happy.
- .claude/settings.json: the "mcp__Claude_Code_Remote" allow rule does not match the server name (claude-code-remote).
- Patron pitch paragraph for the thank-you mail: drafted in chat on 8 Oct, not live. On his go-ahead, add it to the calendar routine's thank-you draft step.
- Sri board (Business OS > Host boards > un# with Sri): check Luca Prosperi's verdict, the four stale "No" precall rows (Shevchenko, Meggs, Ober, Asher Tan), three thin short pitches, and eval/dossier links Sri can't open, before sharing.
- Scimplify: one guest or two (Salil Srivastava, Sachin Santhosh)?
- Transcripts: run routines/transcripts-backfill.md in Claude Code on his Mac (needs his folder paths); set up routines/transcripts-after-recording.md as a desktop scheduled task.
- Upload downloads/all-skills.zip skills in claude.ai.

## Next projects
- Make the daily sweep regenerate the public members page from FT Network (Membership = Added) with migration/ft_network_members_page.py and have the calendar routine write new blurbs to FT Network (To invite) instead of People.Blurb.
- Built to Share migration.
