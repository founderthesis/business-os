# Zoya build for Akshay's 2 Nov list (CTOA-03): for Cleanup and the CTO, before the 16:38 JST run

## The build: items 1, 6, 7 and 8

| File | Bytes / sha256 | Reference |
|---|---|---|
| `zoya-one.txt` | 43,999 / 775b9ed879af33db | zoya-one 512ccf371522 |

**How it's built:**
- The base is the live Zoya, ec22d74d84be (42,109 / 23551dc5bb4a0d12), plus the rules-read patch of 1 Nov (`../zoya-rules-read`, 42,427 / b59636be). That patch was never deployed, and it's item 1's first half.
- It's built on a worktree at f70901f with `../zoya-rules-read/build_one.patch` and this folder's `build_one.patch`: `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin f70901f6f07d4a6610fda60132b4cdbb5ac43979`. Built twice, byte-identical.
- **The SLOW file and the pin don't change:** 63,617 / fae90990931445db at f70901f. No pin move is needed.

**What changes:** all edits are in the FAST prompt's VARIANT.

| Item | Change |
|---|---|
| 1 Rules and pre-send checks | THE RULES adds the follow-ups child page (40b19a301a7f81999c1acd8350d59a54, SLOW only) and "read each page in full" (an oversized fetch is read from its file in slices). HARD RULES gets PRE-SEND CHECKS, every send, FAST and SLOW, done fresh: 1/ rules pages read in full this run (one not loaded: the actions it governs are Blocked, the run Partial, never a send from memory); 2/ recipients from the latest inbound's own headers; 3/ bounced addresses dropped; 4/ the newest owner instruction followed; 5/ Sent in both inboxes; 6/ the action key. A failed check means no send, named in the report |
| 6 Sri left off the reply | The read-back's "on un#, Sri" exclusion now applies only when Sri didn't write on the thread himself. The un# scope line agrees: he stays in Cc when he wrote on the thread. The same holds for Satish and Arjun on their shows. Bounce, handover and privacy rules are unchanged |
| 7 Guest examples | HARD RULES gets GUEST EXAMPLES: only guests whose appearance on that show is on its Episodes row or podm.in/guest-list; never "recent" unless released in the last 90 days; ranked by relevance to the reader, then standing, then recency; none verified, none named |
| 8 Inline booking link | HARD RULES gets BOOKING LINKS: the link sits inside its sentence, in the same <p> and plain-text line: "any open slot here works: podm.in/30min". PLAIN ENGLISH's ban on "works" makes an exception for that phrase |

**SLOW work:**
- HARD RULES "always hold" and SLOW work follows the FAST prompt, so PRE-SEND CHECKS, GUEST EXAMPLES and BOOKING LINKS reach SLOW sends too.
- SLOW's own sending text still has the old "Sri is never in Cc" line, and "on SLOW work it wins". So for a SLOW follow-up on a thread where Sri wrote, the old text governs until the SLOW file is rebuilt and the pin moved. That's the follow-up, not today's deadline.

## Notion edits for the CTO (this session doesn't write to Notion)

- **Item 8:** on "Mail and WhatsApp wording", every booking line reads "any open slot here works: podm.in/30min" inside its paragraph, with no line break before the link.
- **Item 7:** on the wording page or Rules for Zoya, a small reference list of past guests by sector, verified against Episodes, with release month. Remove the "recent" wording for Hitesh Dhingra and Dhruv Madhok. Check Fable Street, Plum Goodness and Foxtale against Episodes.

## Items 2 to 5: data and send work, not a prompt build

These change Notion rows or send mail, which this session doesn't do without Akshay's go-ahead here. They're the CTO's or Main's to run:
- **2:** the six unresolved records (Team Nxt x5, Fully Vested/WisdomTree 17 Nov hold).
- **3:** the backlog inventory.
- **4:** Siddharth Chaturvedi/AISECT, 3 Nov first-half call: Zoya to coordinate today.
- **5:** Sujay K. Kar @ Commix Global.

Rule follow-ups if wanted in the prompts:
- **Item 4:** an inbound scheduling request should put "Zoya: reply to <who>: slots for <date>" first, whatever the chase Next date. This touches decision 81's three Next date cases, so it needs Akshay's word on whether a requested date may set Next date.
- **Item 5:** a new inbound on a closed row should go on Akshay's list, never be ignored.

## Replay (`replay.json`) and build b

The first replay passed the diff and most cases. Build b fixes what it found:
- **D8 (high):** check 5 had no rule for what counts as a match, so the ad@ loop-in could have blocked every mail it loops Zoya in for. It now uses ACTIONS' Sent check: your inbox, and ad@ without loop-ins.
- **D9:** a first mail or a chase has no latest inbound, so check 2 now uses the row and the thread's last message.
- **D3:** check 4 is now the row's Your call, Next action and Waiting on, not the Claude note or Akshay's mail.
- **D6:** a page that doesn't load leaves its actions blocked and named in the report. The run isn't forced to Partial, which the run record would contradict.
- **D7:** guest examples on a client show stay inside SHOW CHECK.
- **D2:** the booking phrase holds whatever PLAIN ENGLISH on Notion says.
- **D4:** Sri is added back if he wrote on the thread but isn't on the latest inbound.

**D1 (high, deferred):** the SLOW file still has the old Sri and "works" text, and it wins on SLOW work. This isn't a regression. The fix is the same edits in the shared parts, a new SLOW file and a pin move by the CTO, as a follow-up after 16:38.

**Status:** written. Not accepted, deployed or observed yet.

## Re-check of build b: go for FAST work at 16:38 (`replay.json`, section b)

Cases a, d, e and g pass. Checks 5 and 2 no longer block sends, and nothing new would block sends.

**Left for the SLOW rebuild (follow-up with the pin move):**
- **D1:** the SLOW file still drops Sri and the host, bans "works" and lacks the new hard rules on SLOW sends.
- Satish and Arjun aren't yet added back when the latest inbound dropped them (Sri is).
- Check 2 needs "if any" for a mail with no thread; only SLOW sends those.
- **D5 (low):** a host the guest copied but who never wrote is still dropped.

**Status:** written and replayed offline. Not yet accepted by Cleanup, deployed or observed.
