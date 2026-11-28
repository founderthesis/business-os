# Cleanup verdict: decision 450 set (Zoya r15b, capture r12d, actions r11b), 3 Nov ~21:30 JST

The replays are in `cleanup/` (`a450.json`, `fast.json`, `inbox.json`).

| Build | Verdict |
|---|---|
| Actions r11b, 46,112 / 07832eb6 | **Accepted** |
| Zoya r15b: FAST 52,925 / 532e8ddb, SLOW task 11,420 / 253d9120, SLOW file 76,760 / e9c6dcb4 at 251388d | **Not accepted: two shared-text blockers.** The decision 450 structure itself passes, with two conditions |
| Capture r12d, 46,594 / 3d38d6f3 | **Not accepted: one blocker** in the forward quote |

All four fixes below are a clause each. With them, Main rebuilds, I re-check the diff, and the 07:38 and 08:08 targets still hold.

## Rebuilds and live bases

**Rebuilds.** Every file reproduces twice, byte-identical to the repo. The SLOW file equals `git show 251388d:...`. There are no em-dashes.

**Live bases:**
- Live actions is 4ac5406d (Cleanup's r10d), and r11b is built on it. All three REPAIR guards are present once each.
- Live capture is 043dbe3a (r11 plus the should-fix), and r12d asserts that base.
- Live Zoya is r11 by content ("zoya-one 1631a3d1dc25"). The tool returned it inline, so I didn't byte-hash it.
- The pin is at 63fcf669, and 251388d descends from it.

## Blockers

**Z1. The quoted chain can reach people who never had it** (decision 452). This answers the CTO's question.
- html_body quotes only the previous message, but that message's HTML carries its own nested chain.
- LEAK CHECK is switched off for the quote, on the grounds that its recipients "already had" it. That isn't always true. A PR writes to Zoya alone, then Zoya's reply puts the guest in To: the recording link (STEP 0r), the themes reply, or "To the guest ... PR goes in Cc". The guest gets the PR's note and everything nested under it, unchecked.
- In the shared LEAK CHECK, the FAST prompt and the SLOW file both read "on the text you write (the gmail_quote and MCP's plain-text quote are mail their recipients already had, decision 452, and aren't checked)".
- **Replace that with:**

  > on the text you write, and on the gmail_quote and MCP's plain-text quote with every nested part, unless every recipient outside the team was on the quoted message's own From, To or Cc (decision 452); a quote that fails goes, with the mail, to Akshay's list unsent

**Z2. The quote trips the link and show checks.**
- "Never a link outside the approved list ..." and SHOW CHECK ("every fact about a show ...") don't exempt the quote. Almost every quoted message carries signature or booking links, and a nested Founder Thesis mail on a client show names the wrong show.
- So a literal run blocks most replies, or logs "show check failed".
- **Add "(the gmail_quote and MCP's plain-text quote aside)" to both rules,** in the shared HARD RULES (FAST and SLOW file).

**C1. Capture: a nested forward leaks the forward note.**
- "Only the original message inside the forward" fails when Saurabh forwards to Akshay's other address and Akshay forwards that to ad@. The "original" inside Akshay's forward is Saurabh's forward, note and all, and it gets quoted to the PR.
- **Replace that with:**

  > only the innermost message from outside the team, with every forward layer and every note by Akshay, Saurabh or anyone tagged Team removed; unsure: no quote

## Decision 450: the five points pass

1. **Select first.** The "S<nn> <key>" lines are written before any send, and progress is saved after each chunk of 10.
2. **Code reconciliation.** A missing outcome, or an unproven cap or minute-22 claim, never comes out Completed. Keys with no outcome carry over.
3. **Shared lock.** The LOCK text is identical to FAST's except for the Summary: no "+" refspec, and `--force-with-lease` against the sha that was read. It's never forced.
4. **Caps.** 40 a run and 150 a day are shared, and SLOW stops 30 short of the daily cap as the FAST reserve. The Diwali pause holds chases only.
5. **No double SLOW work.** FAST r15 says "No run of yours does SLOW work".

**Two conditions:**
- **(a) Cutover order: paste FAST (A) first, then fire SLOW (B) by hand, then enable B.**
  - The r14 steps fire B before A is pasted. Until then, the hourly runs still do SLOW work at 10:38 and 16:38 with the 63fcf66 file, which keys payments, owner mail and feedback differently.
  - Only the Sent check stands between the two and a double, and WhatsApps to Jaya get no Sent check at all.
  - Deploy actions r11b in the same window, first: 446 and 448 need both actions and Zoya.
- **(b) No team WhatsApp before a team hour.**
  - The 08:08 JST run is 04:38 IST, and the SLOW file says team mail and WhatsApp "are never held".
  - Hold team WhatsApp until a team hour on Cadences, or skip team WhatsApp in the 08:08 run.

## Deploy gates

- **The draft test (D2).** Whether draft update keeps html_body is unproven, and the read-back's fallback ("the html_body you passed ends with it") checks itself. It isn't a leak: the worst case is no quote.
  - **This can be settled with no mailbox write:** read a recent Zoya sent mail that went through draft update, and check that its HTML survived.
  - For capture's loop-in, check one sent loop-in's plain-text quote too, to confirm MCP quotes only the message replied to.
- **Cadences.** The Diwali line and the FAST reserve need reading back before B is enabled (Fri 6 Nov is the first Diwali day).

## Should-fix (follow-ups)

**SLOW:**
- A run whose outcome check printed nothing must be Failed.
- Check `date -u` before each item, not only each chunk, so a late chunk can't run past :38.
- Owner mail on the 08:08 run.
- Feedback and vendor items get starved behind follow-ups.

**FAST:**
- The new-contact loop-in can quote a team-only message; use THREADING's outside-the-team filter.
- Same-day recording links: send in the first run after the link arrives.
- Say whether 453 or 448 wins on a themes ask that answers Akshay's own mail.
- A prep note with no "Themes we'll cover": Akshay's list.
- Cap the quoted HTML's size, and strip iframe, form, meta, link and on* handlers.
- FAST still loads the SLOW-only page, and "TEAM WHATSAPP" points to a section FAST no longer has.

**Capture:**
- Escape the name in the quote line.
- Say the quote is the only `<br>` block.
- Name the loop-in in decision 452, and give the order gate a decisions row.

**Actions:** state that the 443 slots step and the 379 close note aren't queued on a 448 mail, and that 6e's plain cancel still runs.

Nothing deployed by Cleanup.
