# Cowork scheduled tasks: FT evals and dossiers (decisions 146, 147)

These replace the cloud routines "FT guest evals" and "Dossiers" once a test run passes. Cowork scheduled tasks run in the cloud, can run account skills and can publish Claude pages, which cloud routines cannot (decision 141). Create each one in the Claude app: Cowork, Scheduled, New task, paste the prompt, connect Notion, Gmail and (dossiers) Google Drive.

Suggested schedules: evals at 00:25, 09:25, 16:25 and 21:25 JST daily (25 minutes after each inbox run, decision 202); dossiers at 06:50 JST daily.

After both pass a test run: disable trig_01DbJZuBeC1TTven5wgjZxoA (evals) and trig_01KaofxCHxvNUSL8ATpqFx1t (dossiers), and retire Eval slots and the session-start conversion in CLAUDE.md.

Prompts, one file each, paste the whole file as the task prompt:
- routines/cowork-evals.md
- routines/cowork-dossiers.md

Keep them in sync with routines/evals.md and routines/dossiers.md until the cloud routines retire.
