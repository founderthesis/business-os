# Zoya r12: decision 445, Zoya sends recording room links (3 Nov)

| File | Bytes / sha256 |
|---|---|
| `zoya-one.txt` (FAST) | 46,635 / 41c6854a3f0164ca |

**How it's built:**
- On the live r11b FAST (44,839 / 264f69fc), from a worktree at f70901f with `build_one.patch`. The r12 edits are in the FAST-only variant.
- Command: `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 63fcf669014fe5c4eeff64c7fedbe6d1c85d926c`. Built twice, byte-identical.
- **The SLOW file and pin are unchanged.** The build reproduces 67,837 / 2cf5b7156ce80240 at 63fcf66, so there's no pin move. Deploying is one paste.
- **Diff against the live FAST:** only STEP 0r, the approved-links line, the HARD RULES link clause and the version string.

## What changes (FAST only)

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

Decision 445 starts with "Zoya asks Mamatha for the room links (as on 1 Nov)". That ask is already a Zoya step from the 1 Nov work, so it isn't added here. If it isn't, it's one more line.

**Status:** written. Replay pending (`replay.json`). Nothing is deployed.
