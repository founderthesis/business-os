# Cleanup on B2: Akshay's own "@zoya" in any chat (a80a824)

**Verdict: ACCEPTED for deploy.** WhatsApp prompt 27,969 B, sha256 1afc777019d1aefd.

## Reproduced

`d-wa-zoya-anywhere.py` on the base 26,007 / 9e8b9f4891e9c03d gives 27,969 / 1afc777019d1aefd. Two builds were byte-identical, the em-dash count is unchanged, and it's under the cap less 200.

The base came from the repo copy (routines/whatsapp.md), matched by hash. The live trigger (trig_01MnmJYorWrd61K7b5BCqXr1) was last updated 26 Oct 03:18Z, and its prompt reads as that text. The script asserts the base hash, and the CTO re-reads the live base before pushing.

## Why it's safe

- **Only Akshay can trigger it.** 0a1 takes only fromMe messages that start "@zoya", and drops Zoya's own fromMe posts ("zoya here", "Zoya ✨"). Nobody else's message in any chat can become an instruction.
- **Privacy holds.**
  - The cross-chat search returns only his matching messages.
  - A non-work chat is never named, and only his own words are used there, never the message he quotes.
  - Replies go only in the "Zoya" group.
- **Nothing is handled twice.**
  - Each message dedupes on `wa:<key>`, checked on Activities and Engagements.
  - STEP 2b no longer applies his "@zoya" text as a chat decision, so "@zoya book him" is applied once.
  - The "Zoya" group is excluded (0a has it).
- **Paging is bounded:** at most 5 searches, stopping when coverage doesn't move, and a gap is reported.
- **Tests:** rounds 1 to 3 pass. Round 3 covers A1 to A7 plus X1 to X4 (crash, "book" in a guest group, a family quote, the Zoya group overlap).

## Minor gaps, for the next change (none blocking)

1. **A crash between the reply and the Activity gives Akshay a second reply in the "Zoya" group.** Logging first, as 0d does, closes it. It affects only Akshay and is cosmetic, but it's one clause, so it should go first.
2. A bare "@zoya book him" names no one. 0a f's question settles it unless the chat name carries the guest.
3. STEP 2b's Scheduling and "ball moved" bullets can touch the same row in the same run. That's sequential, inside one run, so there's no double write.
4. 0a f's "best guess" question shouldn't draw on a family chat's quote. The rule already limits a non-work chat to his own words, and this should say so in 0a f too.
5. STEP 5's report doesn't name 0a1's items or its coverage line.

**Not testable offline:** whether `list_messages` with no chat_id honours the sender filter. The fromMe and "starts @zoya" checks guard it either way. The first live run's report should show 0a1's search and coverage.

The 26 Oct request handled by hand left the 48-hour window on 27 Oct 21:17Z, so no pre-seeded Activity is needed now.

Checks:
- Less text and fewer writers: +1,962 B, no new writer (it's the same routine).
- Selection by prefix or wording: one by design, his own "@zoya" prefix, which is the trigger Akshay asked for. It's bound to fromMe.
- Retry double-send: there's no outside send; the "Zoya" group reply is deduped (gap 1 aside).
- Bytes and hashes: above.
