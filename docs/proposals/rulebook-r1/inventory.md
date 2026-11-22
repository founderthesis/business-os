# Rulebook r1: who reads what (inventory, 22 Nov)

Read only. Scheduled tasks were read with list_triggers; none was changed. "Staged" means a cleaned copy is in this folder; "live" means what runs today.

## Workers and their sources

| Worker | Started by | Reads today (live) | Reads after cutover (staged) | Stale policy found |
|---|---|---|---|---|
| Zoya day chat (tag zoya-day; Sun: session_019pwcV47pR4nRjvAtP1Hk1b) | daily trigger "Zoya day wake (<day>)", prompt "Wake: run what is due now per routines/zoya-day.md"; seeded by the CTO each evening | CLAUDE.md, routines/zoya-day.md (working tree), prompts at 83e8fb0, SLOW work at 63d63ec (via composers), Rules for Zoya and subpages, Cadences, Client show mails, wording | routines/zoya-day.md (staged), prompts/ at RELEASE, upkeep.txt | The override layer; S1 to S9 |
| Capture composer | day chat, each wake (653) | docs/composer-seed.md, inbox-capture.txt at 83e8fb0 | seeds/composer-seed.md, prompts/inbox-capture.txt | Seed points at the override section; capture's ad@ loop-in has no sender (S12) |
| SLOW composer | day chat, 11:08 and 17:08 weekdays | composer seed, zoya-slow.txt at 83e8fb0, work file at 63d63ec | prompts/zoya-slow.txt, prompts/zoya-slow-work.txt (pinned by hash at RELEASE) | Six old slots in the prompt; Mamatha transcripts; owner mail; sponsored nurture |
| Engagement chats (tag bos-engagement) | day chat (593) | docs/engagement-chat-seed.md, routines/cowork-evals.md, routines/cowork-dossiers.md, the show's skills | same seed; routines/cowork-evals.md (staged trim) | cowork-evals TEAM ROLES history line (fixed in staged copy); 654 already in it |
| Blurb chats (tag ft-blurb-standing) | CTO round 2c, day chat Saturday | docs/blurb-chat-seed.md, skills/ft-community-blurb | unchanged | none found |
| Editing-doc chats (tag editing-doc) | Sarika's editing asks | brief written by the editing asks session | brief from the staged routines/editing-checks.txt | Transcript ask to Mamatha; Mamatha in the share list |
| Sarika's editing asks (session_019pwcV3jbCtwb56pcVB3o6J) | 3 triggers: trig_01SXrnWJb2iz5Q3zts34VZu4, trig_0177CBiFc4zP8SGCaVip97Gc, trig_01AU4fQevmq39TDZX6LvC4cq | stored prompt (same text in all three; source routines/editing-checks.txt) | routines/editing-checks.txt (staged); CTO updates all three stored prompts and byte-compares | Mamatha (456) |
| Host boards (trig_01K8bueCr2xsPkbgQzjeRKsz, Sonnet, fresh session) | own schedule, 08:15, 12:15, 16:15, 20:15 JST | stored prompt (source routines/host-boards.md) | routines/host-boards.md (staged) | Waiting on Mamatha/Chaandini branch; "until 19 Oct" history |
| FT Community directory sync (trig_01EoP9zjHnaAeyKthSWdcums) | Saturdays 09:47 JST | stored prompt (source routines/community-directory.md) | unchanged | none found |
| Zoya day monitor (session_019pwcV3kwZU8vnV3UmQq6wR, Sonnet) | trig_01VX6YtwUQ1jBMx23kMjnxM4 (weekdays hourly :55), trig_012eTmTgQcdecGs94PYjPuje (weekends) | stored prompt "Check"; its instructions live in the session's own history, not in the repo | unchanged | Not inspectable from the repo. Its context is at about 700k of 1M tokens and its last summary still says "watching Wednesday chat" (CTO to check) |
| CTO coordination round (trig_019sfzEHt9djonNhbxcATgYA) | 08:45 and 20:45 JST | stored prompt (CTO's own) | CTO's call | Quiet hours "00:30 to 07:30" (now 01:30, decision 547); blurb comments say chats relay through the CTO (fine) |
| CTO one-shot reminder (trig_01LMdiJAHLPZFDxjc2iLhQsJ) | 22 Nov 20:50 JST | stored prompt | n/a | "SLOW and the sweep back on" (against 657); reported to the CTO |
| Evals standing session, FT guest enrichment, older day-wake triggers | disabled | n/a | n/a | none acted on |

## Repo skills and their installed copies

Installed cloud skills can't be read from here, so every installed copy is unverified. The repo copy is the source to upload.

| Repo skill | Used by | Stale policy | Installed copy |
|---|---|---|---|
| ft-guest-eval, un-guest-eval, bts-guest-eval, hbd-guest-eval, pathfinders-guest-eval | engagement chats | none found (654 lives in cowork-evals.md) | unverified |
| ft-host-dossier, bts-host-dossier, hbd-host-dossier, pathfinders-host-dossier, un-dossier | engagement chats | none found | unverified |
| ft-community-blurb | blurb chats | none found | unverified (installed list shows it) |
| ft-lower-thirds, ft-episode-titles, thumbnail-copy, episode-tightener | editing-doc chats | none found | unverified |
| ft-precall-feature | nothing references it; draft (46773ea) | none found | not in the installed list |
| notion-business-os | nothing references it; not installed | Mamatha examples, Deals (retired, 518), Next date for Zoya steps (against 637) | not installed: delete at cutover |
| carousel, carousel-light, pitch-builder, podcast-intro-voiceover, podcast-trailer-montage, shorts-finder, ft-working-doc, un-newsletter, x-comment-sri | Akshay by hand | none found | unverified |

## Notion reading paths

| Page | Read by | Staged |
|---|---|---|
| Rules for Zoya (3f719a301a7f81a09de3ee3ad6ad98a3) | FAST, SLOW, calendar, composers, chat sessions | notion_edits.py |
| Mail and WhatsApp wording (3fa19a301a7f81b6a807d0f01847dae7) | every sender | notion_edits.py |
| Rules for Zoya: follow-ups (40b19a301a7f81999c1acd8350d59a54) and its nine routine pages | SLOW | page staged; the nine child pages not yet read (batch 3) |
| Cadences (3ff19a301a7f8143aa95cd89bd6519ec) | FAST, SLOW | notion_edits.py |
| Client show mails (3fc19a301a7f817588e2d081af825f8a) | client-show mail | not yet edited: C15 to C17 are replaced by Release v3 on un# (decision 638) |
| Routines (3fb19a301a7f813b949cf28cc0993541) | people; the CTO | notion_edits.py (runtime inventory) |
| Rules for Zoya history child pages: Background 12 to 14 Oct, Mail feedback 15 Oct, Routine audit 16 Oct, Mock follow-ups | linked from Rules for Zoya's Related pages | cutover: move them under an archive page first (removing a page link from the content would trash the page), then they drop out of the reading path |
| Inbox and Your call rules (3ff19a301a7f8148993ccea78fc66428), Calendar rules, WhatsApp templates | inbox actions, calendar, WhatsApp | not yet read (batch 3) |
