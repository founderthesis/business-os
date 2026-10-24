# Handoff: Founder Thesis and email automation chat (9 Oct 2026)

Read CLAUDE.md, then this page, then docs/email-automation.md and docs/decisions.md (81, 86, 90 to 92, 95, 96, 98, 99, 102).

## Who works on what

| Chat | Owns |
|---|---|
| FT and email (new) | Founder Thesis guests end to end, the FT evals routine, the Templates database and the email learning loop (decision 102), Mamatha's dashboard |
| Main OS chat | un# and Sri's board, data migrations, People and FT Network, the home page, anything cross-cutting |
| V2 chat | Built to Share only |

The inbox, calendar and daily sweep routines serve every show. Before changing one: pull, edit routines/<name>.md, push the full prompt from that file with update_trigger, commit in the same task. The repo file is the source of truth; never push a prompt you didn't take from the current file, or you undo another chat's change.

## Live routines

| Routine | Trigger | Prompt file |
|---|---|---|
| Inbox (23:25 JST, Sun to Fri) | trig_0189eZvAD8x4357cfevgZ3No | routines/inbox.md |
| FT evals (23:50 JST) | trig_01DbJZuBeC1TTven5wgjZxoA | routines/evals.md |
| Calendar (07:35, 15:35, 21:35 JST) | trig_01Voiz5YsK2SnVf2STF8PoSH | routines/calendar.md |
| Daily sweep (13:10 JST, Mon to Fri) | trig_01MdfUFg2qrebDWgiHwncgnd | routines/daily-sweep.md |

All four run unattended in the cloud with their own Gmail and Notion connectors; no approvals. Routines created from a chat get no connectors, so new routines are made on the claude.ai Routines page.

## Email automation state (decision 102)

- Send: intro reply adding Mamatha, eval mail to Mamatha in the pitch thread, Mamatha's daily list.
- Draft: FT thank-you, pre-release asks for all four shows, vendor redirect.
- Learning: the inbox compares sent mail with drafts (Edit size, Edit note); Fridays the sweep writes "## Proposed" sections and mails a review. Ready to send = 8+ drafts sent, 80% clean. Only Akshay moves a template to Send.
- Not built yet: FT chasers, precall and recording invites as drafts; Holds are live (decision 104): LT chase, Next date = their date or 90 days out, Waiting on Guest or PR. Otherwise agents change Next date only for a new lead or a booked precall or recording.

## FT eval refresh (done 10 Oct, waiting on the Notion AI run)

Akshay, 9 Oct: re-run the eval for every open FT guest rated Strong consider or above whose eval is more than a month old, and run one for warm guests with none. Done 10 Oct for 61 rows (log in docs/notion.md, batch ft-eval-refresh-2026-10-10). Eval files are in data/review/ft_evals_2026-10-10/, one per guest; the two Notion AI prompts are data/review/ft_eval_refresh_2026-10-10_notion_ai_part1.md and _part2.md. Once Akshay has run both, check a few rows read-only (Eval verdict, the "## Eval (2026-10-10)" section, the Claude note line) and log it.

Lesson: research agents share one budget of 200 web searches per turn, and WebFetch to news sites fails DNS through the proxy. Give each agent an explicit search cap that sums to under 200, and expect snippets, not fetched pages.
