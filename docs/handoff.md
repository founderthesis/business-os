# Handoff (8 Oct 2026)

Open work for the next session. Read CLAUDE.md, docs/decisions.md (81 to 86 are the newest) and this file first.

## Urgent, before 23:25 JST tonight
- Push the rewritten prompts in routines/inbox.md, evals.md, calendar.md and daily-sweep.md (the ```text block of each) to their triggers with update_trigger: inbox trig_0189eZvAD8x4357cfevgZ3No, evals trig_01DbJZuBeC1TTven5wgjZxoA, calendar trig_01Voiz5YsK2SnVf2STF8PoSH, daily sweep trig_01MdfUFg2qrebDWgiHwncgnd. Only after the Engagements column "Waiting on" exists (check the data source schema). Schedules are already set (inbox 23:25, evals 23:50 Sun to Fri; sweep 13:10 Mon to Fri).

## Check what the background jobs finished in Notion
- "Waiting on" multi-select on Engagements and Deals, populated; views "Akshay: waiting on me" (Engagements and Deals), "Mamatha: waiting on me", "FT: Sponsored pipeline"; Waiting on added to FT: Today, un#: Today, All shows: Today. Precall done rows -> Waiting on Akshay (decision 86).
- Closures: open un# rows with Host verdict No -> We declined, except Luca Prosperi (verdict likely wrong; leave in Booking); Himanshu Joshi HBD row -> We declined; Alex Cutler duplicate merged (other row renamed "DELETE:").
- FT Network database (WhatsApp group members) and the page "Founder Thesis community: members" under the Business OS home. Built from data/raw/whatsapp/blurbs_2026-10-08.json via migration/whatsapp_network.py.
Both jobs were STOPPED part-way on 8 Oct (too many permission prompts in the old session). State when stopped: Waiting on was being filled in batches (was on the LT chase batch), so some open rows have it and some don't; views and closures may not exist yet. FT Network had started loading rows (first batch of 22). Check what exists, don't duplicate rows (match on Name + Migration batch "whatsapp-doc-2026-10-08"), and finish all of it. Batch writes where the tools allow.

## Waiting on Akshay
- Patron pitch paragraph for the thank-you mail: drafted in chat on 8 Oct, not live. On his go-ahead, add it to the calendar routine's thank-you draft step.
- Sri board (Business OS > Host boards > un# with Sri): check Luca Prosperi's verdict, the four stale "No" precall rows (Shevchenko, Meggs, Ober, Asher Tan), three thin short pitches, and eval/dossier links Sri can't open, before sharing.
- Scimplify: one guest or two (Salil Srivastava, Sachin Santhosh)?
- Transcripts: run routines/transcripts-backfill.md in Claude Code on his Mac (needs his folder paths); set up routines/transcripts-after-recording.md as a desktop scheduled task.
- Upload downloads/all-skills.zip skills in claude.ai.

## Next projects
- Make the daily sweep regenerate the public members page from FT Network (Membership = Added) and have the calendar routine write new blurbs to FT Network (To invite) instead of People.Blurb.
- Built to Share migration.
