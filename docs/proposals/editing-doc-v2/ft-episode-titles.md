# Proposal: ft-episode-titles (editing doc v2, decision 602)

Target skill: ft-episode-titles

Why: on both docs Sarika uses (Redseer, Mandar) the standalone "YouTube title options" tab was dropped. Decision 602 puts titles after the thumbnail picks.

## Change: when the skill runs inside the editing doc
Before (Output):
> **8 titles.** For each, note which entities it carries and what search intent it serves. Then recommend one and say why.

After:
> Standalone use: unchanged (8 titles, entities, intents, one recommendation).
> Inside the editing doc: no standalone list. Write one title per thumbnail the editor picked (thumbnail-copy step 2), in the table `# | Picked thumbnail | YouTube title | Chars | Keyword it targets`. All title rules here still apply (guest and company, no number not in the transcript, do not repeat the thumbnail copy), with the length band tightened to 60 to 70 characters.
