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
- Not built yet: FT chasers, precall and recording invites as drafts; the "hold" mail handling (proposal in this chat: Waiting on Guest or PR plus a revisit date in Next action, and the sweep skips its quiet check until then; awaiting Akshay's yes). Mamatha's rule stands: agents change Next date only for a booked precall or recording.

## First task waiting for you: FT eval refresh

Akshay, 9 Oct: re-run the eval for every open FT guest rated Strong consider or above whose eval is more than a month old, and run one for warm guests with none. 60 rows, list in data/review/ft_eval_refresh_2026-10-09.tsv (3 more had evals this month and are skipped). Use skills/ft-guest-eval, research in the chat (read-only agents, never writing to Notion in parallel), then one Notion AI .md to apply: Eval verdict, a "## Eval (2026-10-09)" section in each Engagement page, a Claude note line "2026-10-09: eval refreshed, <old> -> <new>". Format used for un#: data/review/un_evals/*.md.
