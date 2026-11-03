# Calendar sync, decision 454 and related edits (4 Nov)

| File | Bytes / sha256 |
|---|---|
| `calendar.txt` (new) | 58,676 / a06a8b37924c60ad |
| Live input (trig_01Voiz5YsK2SnVf2STF8PoSH, read back ~01:30 JST 4 Nov; not committed, because it carries the house mail addresses) | 57,968 / f6d140196f3b75b4 |

**Build:** `python3 patch.py <live calendar prompt> <out>` asserts the live hash f6d14019 and each of 7 edits exactly once. Patched twice, byte-identical, no em dashes.

**Before pasting:** byte-compare the live prompt against f6d14019. If it moved, re-run the patch on the new text.

## Edits

1. **Decision 454, the prep event links (STEP 3).**
   - **Why Sameet's event stayed stale:** the old rule updated a private "Prep:" event only when a link was "new or has changed since". A run can't tell that, so the 30 Oct prep event never got the dossier added later.
   - **The new rule:** every run compares the event's description, line by line, with the row's Eval, Dossier, Prep note and LinkedIn links. A missing or different one rewrites the description only, with the "Dossier:" and "Prep note:" lines first, notificationLevel none. It's private with no guests, so it's an add, never a move.
2. **Decision 453, the day-before note (STEP 3b fill).**
   - **The hold:** the note no longer holds for the recording link. With no recording link on the row or the invite, the run drops the sentence that carries {call link} and sends or drafts the note anyway; the link goes in Zoya's recording-link mail (445).
   - **Where it comes from:** the live prompt has no literal "cannot be filled" hold. The hold came from the {call link} fill, so the fix is in the fill.
3. **Decision 445, r12b's D8 (zencastr.app.link links).**
   - **Recognised everywhere:** zencastr.app.link now counts as a Zencastr link in STEP 1's recording classification and Call link, audit rule 4 and STEP 4e's recording test. That last one decides whether a transcript row gets made.
   - **Rule 4's no-link case:** it's now a Claude note only. Zoya's STEP 0r asks Mamatha, and puts it on Akshay's list within 24 hours, so this no longer raises a duplicate "Akshay: no Zencastr link" ask.

Nothing else changed.

**Status:** built, not replayed. Ready for Cleanup. Nothing is deployed. The CTO deploys.
