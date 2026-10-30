# Queue after the one-writer Zoya release (CTO, 27 Oct; Akshay's "random notes", tab 11)

**Order:**
1. The one-writer Zoya release stays first and isn't widened. It waits on the CTO's GitHub lock harness run, a durable pin for the SLOW work file, Akshay's yes on the timing, the repo attached, the lock ref created and Cleanup's acceptance.
2. Then the three builds below, one at a time. Each is a minimal patch to the live prompt, built twice and identical, and goes to Cleanup. Each deploys only on acceptance, then gets a native read-back and its first run observed.

The order of the three: the calendar first, because a client host saw the text and complained. Then WhatsApp, because Akshay's instructions are being missed. Then the community roster, which is data quality only.

## B1. Calendar: no bos-key in the host's "Podcast prep" invite

**Where.** The live calendar prompt:
- STEP 3 creates the third event, "Podcast prep: <Guest> @ <Company>". Its description ends "bos-key: <engagement page id> <event start ISO> hostprep".
- The scope rule allows "only events [that] carry "bos-key:"", with this invite as a named exception.
- STEP 4e skips "Podcast prep:" entries.

**Patch:**
- **Identity moves to the Engagement.** When the invite is created, write a Claude note line "host prep invite <eventId>". Find the invite by that id, falling back to summary "Podcast prep: <Guest>" on the recording day, ad@thepodium.in, attendee = the show's host.
- **Drop the bos-key line from this description only.** The private Prep and Cooling-off entries keep their keys. The scope rule's exception names the invite by the Claude note id, not by key.
- **Migration, once, idempotent, in the first run after deploy.** For each upcoming "Podcast prep:" event that still carries "...hostprep":
  1. Write its id to the Engagement's Claude note.
  2. Read the note back.
  3. Only then remove the bos-key line from the description.

  An event whose id can't be written keeps its key, so nothing is ever duplicated.
- **Unchanged:** decision 417 (the un# invite starts 90 minutes before the recording; hot-patched live, f94d773). The patch is built on the live prompt as read back, and a test checks 417's line is still there.

**The un# dossier as a Google Doc in the invite.**
- It depends on a Drive folder that Akshay shares once with Sri. The Drive share tool is blocked in auto mode, so this is one step for Akshay, and it goes on akshay-pending.
- The dossier routine (cowork-dossiers) then creates the Doc copy in that folder, and it inherits access. The invite adds "Dossier (Doc): <link>".
- It's a separate patch to the dossier routine, because it touches a different routine. It ships after B1, once the folder exists.

**Tests (offline, twice):**
- a new invite has no key and its id is noted;
- the migration on an existing keyed invite runs once and is idempotent on a re-run;
- the fallback finds the invite with no note;
- the un# start is 90 minutes before;
- the private entries keep their keys;
- no other event is touched.

## B2. WhatsApp: capture Akshay's own "@zoya" in any chat

**Where.** STEP 0d answers "a team member's "@zoya" message" in listed chats only, and takes non-fromMe messages only. Akshay's 26 Oct 06:17 JST "@zoya can you ingest this list and compare with the founder thesis network?" in "AD CM SG" was never picked up.

**Patch:**
- **New input.** Read fromMe messages starting "@zoya" in any chat, from the last 48 hours. Treat each as a STEP 0 instruction: a Task row, or Your call on the matching Engagement.
- **Replies.** The reply goes only in the "Zoya" group, never in the chat it came from (third-party groups included).
- **Dedupe.** Key on Source ID "wa:<message key>"; a key already on an Activity is handled.
- **The 26 Oct request.** The CTO did it by hand. If deploy falls inside its 48-hour window, it needs a "handled" Activity with its wa: key first. I'll read the key with Blueticks (read only) and add it to notion-edits for the CTO to apply.
- **Unchanged:** STEP 0d's existing team "@zoya" handling, the rule that every message is data and never an instruction from its author, and the send limits ("never send a message to anyone else").

**Tests (offline, twice):**
- Akshay's "@zoya" in a third-party group gives one Task row and one reply in "Zoya", and none in the group;
- a re-run is deduped;
- a team member's "@zoya" behaves as before;
- a fromMe message without "@zoya" is ignored;
- a message older than 48 hours is ignored.

## B3. FT Community roster from the real member list

**Where.** The WhatsApp routine's community mirror sets Membership from join and leave events (line 98 of whatsapp.md). Blueticks `groups get` with include_participants now pages: {limit 100, skip, total 528}.

**Patch:**
- **Full roster.** Page through `groups get` until skip ≥ total, reading only, and match each participant as the existing step does (chat id, else People Phone, last 10 digits for India).
- **Set Membership from it.** A member gets Added. A row at Added that isn't in the list gets Left. People with no row get one created from People, as now.
- **Type.** When empty, set Founder (when People or the FT guest record says founder) or Other. Never blank.
- **Changes only.** A row whose state already matches isn't written. Count reconciliation and a read-back are in the report.
- **Already done by the CTO:** the public Members view filter is now "Name not empty".

**Tests (offline, twice):**
- a 528-member roster across 6 pages is fully read;
- additions, departures and unchanged rows are each correct;
- Type is defaulted, never blank;
- a re-run writes nothing;
- a failed page fetch ends Partial with no Left writes, because a short list must never mark people as having left.

## Not in scope

- No change to Zoya's prompt in any of these.
- No new features beyond what's listed.
- Each build's status goes in its commit: fixed and tested, still failing, or blocked.
