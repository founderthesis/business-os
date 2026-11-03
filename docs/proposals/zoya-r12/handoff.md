# Zoya r12: decision 445, Zoya sends recording room links (3 Nov)

| File | Bytes / sha256 |
|---|---|
| `zoya-one.txt` (FAST, r12c) | 50,160 / 079b081a704907ef, pinned to cd9000f |
| `zoya-slow-work.txt` (SLOW, r12c) | 69,409 / 9ccf22ad32f4fa1e, at cd9000f |
| Actions r11 (`../inbox-split/r11/actions.txt`) | 45,775 / 794328afdc81758e, on the live 43,955 / 4ac5406d |
| `zoya-one-r12b.txt` (replaced) | 47,848 / 78e746d22d25bb4f |
| r12 (replaced, failed replay) | 46,635 / 41c6854a3f0164ca |

**How it's built:**
- On the live r11b FAST (44,839 / 264f69fc), from a worktree at f70901f with `build_one.patch`. The r12 edits are in the FAST-only variant.
- Command: `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 63fcf669014fe5c4eeff64c7fedbe6d1c85d926c`. Built twice, byte-identical.
- **The SLOW file and pin are unchanged.** The build reproduces 67,837 / 2cf5b7156ce80240 at 63fcf66, so there's no pin move. Deploying is one paste.
- **Diff against the live FAST:** only STEP 0r, the approved-links line, the two HARD RULES clauses (link list, invite edits), the one FAST queue line on rows waiting on Akshay, and the version string.

## What changes (FAST only)

This section describes r12 as first written. The r12b section below overrides it where they differ: Founder Thesis only, the done check, and the 24-hour ask.

**STEP 0r. RECORDING LINKS** is new, placed before INVITES. Every run:
- **Reading:** it reads Mamatha's mails in Zoya's inbox from the last 14 days that carry zencastr.app.link links.
- **Matching:** each link is matched by the guest and company on its line to one Engagement at Booked with a future recording on Akshay's calendar. No match, or two, means no send, and it's reported.
- **The key:** "<row id>:reply:call-recording-link-<event id>:<event start ISO>".
- **Already done:** a "Zoya sent: recording link to <guest>" Activity, or the link already in Zoya's Sent, ad@'s Sent or on the guest's thread, to anyone. Then it sends nothing and logs the Activity if missing. This covers today's hand sends, including Col. Sai's via Mitali.
- **When it sends:** in the first run after the link arrives (quiet hours aside), and never later than the day before.
- **What it sends:** the "Recording link" toggle, on the guest's own thread, To the guest (else their company-side contact), Cc their side and Akshay. The time is in the guest's zone (unknown: IST).
- **The invite add:** location set to the link if empty, plus the first description line "Recording link (Zencastr): <link>", notificationLevel ALL. Nothing is moved, removed or changed.
- **The log:** the Activity, with its Action key and a Claude note line.
- **No link within 24 hours:** once, "Akshay: no recording room for <guest> (<D Mon HH:MM JST>)".

**Approved links:** a zencastr.app.link room link is allowed only in that guest's recording-link mail and invite. The HARD RULES link clause matches.

## For the CTO (Notion): add the toggle before the deploy

Add a toggle on "Mail and WhatsApp wording" (3fa19a301a7f81b6a807d0f01847dae7) with this text:

> **Recording link**
>
> <b>From:</b> Zoya. <b>Status:</b> approved
>
> hey {first name},
>
> here's the recording link for your conversation with Akshay on {day date} at {time in their zone}: {link}
>
> 1/ open it in chrome on a laptop
> 2/ headphones on, in a quiet room
>
> see you then
>
> best,<br />Zoya ✨

## Not in this build

Decision 445 starts with "Zoya asks Mamatha for the room links (as on 1 Nov)". It isn't added here. The replay found it in neither prompt file (D13 below).

## r12b: replay fixes (3 Nov)

The r12 replay failed, with 2 high and 5 medium must-fixes (`replay.json`). r12b takes the replay's drop-in STEP 0r, plus two more one-line edits:
- **D1, a deadlock (high):** STEP 0r's own 24-hour ask put Akshay in Waiting on, and "Rows waiting on Akshay are never yours to mail" then blocked the link. Fixed:
  - Another ask on the row no longer holds the send. Only an Akshay hold on this recording does (a no-show, cancellation or reschedule).
  - The queue line now reads "(STEP 0r's recording link aside)".
  - A send clears the "no recording room" segment and Akshay's Waiting on entry.
- **D2, false asks to Akshay (high):** the 24-hour ask now fires only for a Founder Thesis recording with no room link anywhere: Mamatha's mails, the invite's location or description, or the row's Call link. A marker, the Claude note "recording room asked <event id>", stops repeats.
- **D3, wording missing:** with no "Recording link" toggle, Zoya sends nothing and reports "wording missing: Recording link". A recording within 48 hours goes on Akshay's list.
- **D4, quoted links:** a link counts as already sent only when it appears in our own Sent mail, in that mail's own text (not a quote), to the guest or someone on their side. Col. Sai via Mitali still counts. A hand send is logged with the real sender in the body.
- **D5, HARD RULES:** the calendar clause now allows "INVITES' adds and STEP 0r's link add". An event Zoya can't edit gets reported.
- **D6, the key's timing:** the Sent check runs from the arrival of Mamatha's mail, not from the key's future event time. In FAST ORDER these sends are replies and go first among replies, soonest recording first.
- **D7, Founder Thesis only:** a link for a client-show row is reported, and nothing is sent. **CTO to confirm:** Akshay's 445 may have meant all four shows. Widening it needs the client-show link lists and SHOW CHECK changed too.
- **Also folded in:**
  - D8, in part: Zoya sets the row's Call link.
  - D9: a past recording is skipped silently, and a no-match is reported once per link.
  - D11: a line with two links, or a host link, means no send.

**Needs doing outside this build:**
- **Before deploy (CTO, Notion):** add the "Recording link" toggle above. Add the same zencastr.app.link clause to the approved-links list on Rules for Zoya, and on Calendar rules if it lists links (D10). The page wins over the prompt, so a page list without the clause still blocks the link.
- **calendar.md (D8, a separate deploy):** recognise zencastr.app.link as a Zencastr link in STEP 1 and in audit rule 4. Until then, expect the calendar audit to raise a duplicate "no Zencastr link" ask.
- **The ask to Mamatha (D13):** it's in neither the FAST nor the pinned SLOW file. The CTO confirms whether it lives on Rules for Zoya; if not, it's one line in SLOW's team work later.
- **zencastr.com/z/ guest links (D11):** STEP 0r reads only zencastr.app.link. Say if the other form should count.

**r12b status:** r12b built twice, byte-identical. SLOW is unchanged (2cf5b715 at 63fcf66), so no pin move. No em dashes, and it's under the cap with 17.7k to spare. Ready for Cleanup. Nothing is deployed.

## r12c: decisions 446, 447 and 448 (3 Nov, the CTO's ask)

**The pin moves this time.** 446 and 447 edit parts FAST and SLOW share (SCOPE, INVITES, SENDING), so SLOW changes. The new SLOW is committed at cd9000f1773adc139a077c69edc7dcfb2e305422 (`routines/zoya/release/zoya-slow-work.txt`), and FAST is built against it: `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin cd9000f1773adc139a077c69edc7dcfb2e305422`. Built twice, byte-identical. Deploy step 1 is the pin move, then a sha256 read-back, then the FAST paste.

**446, client-show scheduling (shared; SCOPE's UN# section and INVITES):**
- On un#, Built to Share and Human by Design, Zoya never proposes, creates, moves or confirms a recording time on her own. C7, C8 and INVITES go only on Akshay's ok in Your call.
- Each scheduling turn (their windows or slots, a "can't do", a reschedule, the host's pick) becomes one Akshay segment: "Akshay: <guest> (<show>) scheduling: <what came in>. Recommend: <one step>, because <one line>. Write ok, not ok or a change in Your call. (<D Mon>)". There's only ever one per row, and a new turn updates it.
- Zoya sends only the holding reply. On Akshay's ok, she does the step; for un#, slots go to Sri's board as before.
- An instruction mail from Akshay ("block the 17th as well") is his ok: it's queued as a Zoya decision step, and she does it.
- B2S and HBD hosts pick slots only after Akshay's ok. INVITES on a client show needs his ok for that time.

**447, the subject follows the org (shared; SENDING's THREADING):**
- When the org a mail is about differs from the org in the thread's subject, the reply stays on the thread with In-Reply-To and References kept. Its subject becomes "<Org> <> Founder Thesis Podcast" (on a client show, the show's name from its pitch sheet), set with draft update's subject before the read-back.
- A Claude note line "subject: <it>" carries it, so later mails on the row, SLOW follow-ups included, keep it. The read-back checks the subject.

**448, replies on Akshay's own threads (FAST STEP 1 b; actions STEP 5 and 6e):**
- A reply to a mail Akshay wrote himself goes on his list with one recommendation, even a "will revert". Not a loop-in, the billing forward, an agent's send or a team mail.
- Zoya doesn't answer it. There's a holding reply only when it asks something.

**Actions r11** (`docs/proposals/inbox-split/r11/patch.py`, asserting the live 4ac5406d input):
- STEP 3's host-show slot bullet goes to Akshay first, with one recommendation (446, replacing decision 114 there). On his ok, the host-board step is as before.
- The decision 443 line now points to it.
- STEP 5 gets the 448 bullet, which wins over the Zoya, acknowledgement and ball-in-their-court bullets. 6e leaves those mails out of its buckets.
- It's 45,775 bytes, well under the cap, so no split was needed.

**Cases to replay:** Ryan Louvar (un#, booked for 16 Nov though Sri gave the 17th and 18th, and "block 17th as well" was never done); Commix on the Livlong 365 thread; Mike Cagney (Richard's "will revert" on Akshay's 1 Nov mail).

**Status:** r12c is built twice and byte-identical, and actions r11 is patched twice and byte-identical. The replay is running. Nothing is deployed, and the pin ref hasn't moved.
