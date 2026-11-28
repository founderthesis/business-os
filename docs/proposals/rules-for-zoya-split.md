# Rules for Zoya: a page Zoya can read in full every run

**Measured on 1 Nov, read only.** The page 3f719a301a7f81a09de3ee3ad6ad98a3 returns 82,341 characters from Notion fetch. Its content is 80,035 bytes. The fetch overflows a session's tool-result limit: this session's own fetch of it was cut off the same way. That's why Zoya's 13:38 run said "too large to read in full".

**Sections by size (bytes):**

| Section | Bytes | Read every run? |
|---|---|---|
| System-audit corrections, 25 Oct 2026 | 6,937 | no: corrections, already folded into the sections or the prompts |
| 1. Who sends what | 7,630 | yes |
| 2. Rules for every mail | 13,881 | yes |
| 3. Fresh inbound pitches | 3,448 | yes |
| 4. Replies to mail that comes in | 4,887 | yes |
| 5. Follow-up routines | 21,243 | SLOW work only |
| 5a. Nurture and revival | 7,440 | SLOW work only |
| 6. WhatsApp | 1,299 | yes |
| 7. Never followed up, and when Akshay is pulled in | 981 | yes |
| 8. Wording | 243 | yes (a pointer) |
| 9. Adding Zoya to older threads (one-time plan) | 2,322 | no: done |
| 10. Go-live: what changes in the live routines | 1,476 | no: history |
| 11. Mail issues | 298 | yes (a pointer) |
| Waiting on Akshay | 7,336 | no: a status list, not rules |

## Proposal: split by who reads what, with no rule rewritten

1. **"Rules for Zoya" (Controls) keeps sections 1 to 4, 6, 7, 8 and 11: about 32,700 bytes.** Every Zoya run reads it, and FAST work needs no more.
2. **A new child page "Rules for Zoya: follow-ups" (Controls) takes sections 5 and 5a: about 28,700 bytes.** Only the 10:38 and 16:38 runs that do SLOW work read it.
3. **Move out of the Controls page:**
   - the 25 Oct corrections: check each is in its section, then archive them under the developer page's Change log;
   - section 9: done;
   - section 10: history;
   - "Waiting on Akshay": a status list, which belongs on the CTO state page or `docs/akshay-pending.md`.

   That's about 18,100 bytes out of the read path.
4. **The size target:** each Controls page stays under 40,000 bytes. On a later edit that crosses it, the section moves to its own child page, not the page growing.

Each Zoya run then reads about 32.7 KB. A SLOW run reads about 61.4 KB, over two fetches that each fit. That's down from one 80 KB fetch that doesn't fit.

## The prompt change this needs (after the CTO moves the pages)

- **THE RULES list** in `routines/zoya/parts/` (the line naming Rules for Zoya) gains one more entry: "Rules for Zoya: follow-ups <new page id> (SLOW work only)". It goes in FAST's list so SLOW work fetches it, about 90 bytes.
- **A cut-off read is an error:** "Read every page in full; a fetch that comes back cut off is an error: say so in the run record and end Partial." That's about 110 bytes.
- **The build:** both sentences go in the next Zoya build once the page ids exist. This builder can make that build within the hour of getting the id.

Nothing was written to Notion.
