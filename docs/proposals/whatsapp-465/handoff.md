# WhatsApp to Business OS, decision 465.2 (4 Nov)

| File | Bytes / sha256 |
|---|---|
| `whatsapp.txt` (new) | 27,361 / 8628f42a4f4803d4 |
| Live input: trig_01MnmJYorWrd61K7b5BCqXr1, read back 4 Nov ~15:30 JST (not committed, because it carries house addresses and chat names) | 26,336 / ca8009c24aaeda15 |

**Build:** `python3 patch.py <live prompt> <out>` asserts the live hash, each of 3 edits once, and no new em dash. Patched twice, byte-identical.

**Akshay's own word is a third "Added" signal** (after the group join event and the guest saying they joined):
1. **STEP 0a e1 (new), in the Zoya group:** a message from Akshay saying he added someone (for example "added sankalp to the FT group") sets their FT Community row to Added, with Added on set to the message date. It does this from To invite, Invited, Declined or Unresponsive, never from Left. The run then clears his asks as b2 does and replies "Zoya ✨ noted: <name> is in the FT Community".
2. **STEP 3a (3), on an Engagement:** Akshay's word in its Your call, or a Claude note line from the last 14 days that keeps one of his calls, saying he added the person. That covers Sankalp Arora's "added to whatsapp group, remove from my queue". It sets Added, with Added on set to the date he wrote it, and this runs every run, not only the first of the day.
3. **b2:** clears the invite and "WhatsApp addition pending" asks, and closes the Task row, for rows set Added by any of the three signals, **and for any row already Added that still carries one** (the "Added but still asked" gap).

**Sankalp Arora:** his row moves to Added on the first run after deploy, from the Claude note copy of his call. The gap audit names him if he's still Invited.

**Status:** built, not replayed. Ready for Cleanup. The CTO deploys.
