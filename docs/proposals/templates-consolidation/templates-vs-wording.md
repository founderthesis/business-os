# Templates database vs Mail and WhatsApp wording page

Read-only comparison, 26 Oct 2026. Templates: collection b2976a03 (55 rows, not 56: a SQL COUNT returns 55). Wording page: 3fa19a301a7f81b6a807d0f01847dae7, fetched fresh at 14:57 UTC 26 Oct (73 h3 toggles, after the FT thank-you edit). T = Templates row, W = wording toggle. Addresses are redacted.

Counts: identical 20, minor 16, material 19, one-sided (toggle only) 17, Templates rows with no toggle 0.

Templates column: id prefix; Mode; Approved; Owner routine; Sender; Version; Last edited (2026, UTC).

| Message | Templates row | Wording toggle | Wording match | Differences |
|---|---|---|---|---|
| Admin ask: noted, added before release | 3f819a30; Send; Y; inbox; Akshay, reply-all; v1; 10-13 | yes; From: Zoya; Status: approved; dec: 166, 208 | material | T signed "Thanks & Regards, Akshay Datt" from Akshay (Send/inbox); W from Zoya, best/Zoya. Example promise line differs: T "We'll share the edited episode with you for... |
| B2S thank-you after recording | 94cea030; -; Y; -; Akshay; v2; 10-09 | yes; From: Akshay (Akshay's inbox); Status: approved; dec: - | identical | both Akshay |
| Decline with sponsored offer | a9c20e51; -; Y; -; Mamatha; v1; 10-09 | yes; From: Akshay (Akshay's inbox); Status: approved; dec: - | minor | body same; T signed Mamatha, W signed Akshay; W says retired 15 Oct (decision 197), replaced by Sponsored: no organic slot (via PR). T still Approved, Mode empty |
| Edit notes: noted with thanks | 3f519a30-8151; Send; Y; inbox; Akshay, reply-all; v1; 10-12 | yes; From: Zoya; Status: approved; dec: 125 | material | body same; T signed "Thanks & Regards, Akshay Datt", sender Akshay (Akshay's inbox) Mode Send inbox; W from Zoya (since 16 Oct), best/Zoya, plus [WhatsApp Sarika the... |
| Editorial decline, not a fit (non-founder or too early) | cd650e96; -; Y; -; Mamatha / Akshay; v1; 10-09 | yes; From: Zoya; Status: approved; dec: - | material | T "we can explore the sponsored route as well", Regards Mamatha; W "we can offer a sponsored appearance on the pod as well", best/Zoya; W From Zoya |
| Episode is live | 2c6b648b; -; Y; -; Mamatha (Akshay for HBD); v2; 10-09 | yes; From: Zoya; Status: approved; dec: - | minor | body same; T Regards Mamatha, W best/Zoya; HBD from Akshay in both |
| Eval ready, in the pitch thread | a572bab6; Off; Y; evals; agent, to Mamatha; v1; 10-16 | yes; From: nobody; Status: retired; dec: - | identical | W retired (decision 154); T Mode Off, Approved yes |
| Form received, release timeline | c7e86b1c; -; Y; -; Mamatha; v1; 10-09 | yes; From: Zoya; Status: approved; dec: - | material | T "8 to 10 weeks" vs W "10 to 12 weeks" (and FT thank-you now says ~12 weeks); T Regards Mamatha vs W Zoya |
| FT precall invite to PR | 2be21c9e; -; Y; -; Mamatha; v1; 10-09 | yes; From: Zoya; Status: approved; dec: - | material | T is Mamatha's old v1: alignment-check framing ("helps us decide ... whether we can offer them an organic appearance"), no Tier purpose lines, stats list with "{link:... |
| FT precall, PR wants to talk first | 298c2af2; -; Y; -; Mamatha; v1; 10-09 | yes; From: Zoya; Status: approved; dec: - | material | T long formal Mamatha version, Regards Mamatha; W short Zoya rewrite (decision 201). Same link podm.in/30min, same meaning |
| FT thank-you after recording | 6d04b9e3; Send; Y; calendar; Akshay; v4; 10-26 | yes; From: Akshay, as a draft in Akshay's inbox that he...; Status: approved (Akshay, 21 Oct); wording updated to his Entrust...; dec: 300, 374, 412 | minor | Wording the same (v4 Entrust draft) except: T bracket says "Leave the patron paragraph out" vs W "three patron paragraphs"; W keeps the bracketed transcript line "[Only... |
| FT thank-you, PR block variant | 888f5597; -; Y; -; Akshay; v1; 10-09 | yes; From: ; Status: retired; dec: - | minor | Body same idea; T last line "We will share an update on the likely release date once you have filled out the form." vs W "We'll share an update ... once the form is... |
| Guest review of final edit | 66238fdb; -; Y; -; Mamatha; v2; 10-09 | yes; From: Zoya; Status: only after Akshay says yes on the row (decision 208:...; dec: 208 | minor | body same; T Regards Mamatha (x2), W best/Zoya (x2). W status: only after Akshay says yes on the row (decision 208); T Notes "only sent when the guest or PR asked" |
| Mamatha added to a new FT pitch | c636bfe3; Off; Y; inbox; agent, Akshay's inbox; v1; 10-12 | yes; From: nobody; Status: retired; dec: - | identical | both retired/Off |
| Mamatha's daily list | 7d059952; Send; Y; daily sweep; agent, to Mamatha; v1; 10-09 | yes; From: agent, to Mamatha only; Status: approved; dec: - | material | T opens "{n} guests on FT: Today (...)" and ends "Open the list: {FT: Today link}"; W drops both and adds "[Founder Thesis rows aren't on her list: Zoya handles... |
| Paid fast-track out of the release queue | 9d39cbee; -; Y; -; Akshay; v1; 10-09 | yes; From: Akshay (Akshay's inbox); Status: approved; dec: - | identical | both Akshay, "Thanks & Regards, Akshay Datt" |
| Park until later (B2S, HBD) | e3c6d860; -; Y; -; Chaandini; v1; 10-09 | yes; From: Chaandini; Status: approved; dec: - | identical | both Chaandini |
| Post reminder after release | c56e4c93; -; Y; -; Mamatha; v1; 10-15 | yes; From: Zoya; Status: approved; dec: - | minor | body same; T signed "Regards, Akshay" (Sender field says Mamatha), W best/Zoya; W adds "Routine 6 checks with Akshay before this goes." |
| PR form chaser | 6246c007; -; Y; -; Mamatha; v1; 10-15 | yes; From: nobody; Status: retired; dec: - | identical | W retired (routine 5); T Approved, Mode empty, Sender Mamatha but signed Akshay |
| Pre-release ask (B2S) | 96e0740c; Off; Y; daily sweep; Akshay; v2; 10-12 | yes; From: Akshay (Akshay's inbox); Status: approved; dec: - | identical | both Akshay; T Mode Off, daily sweep |
| Pre-release ask (FT) | 3954df93; Off; Y; daily sweep; Akshay; v2; 10-12 | yes; From: Zoya (decision 235; was Akshay); Status: approved, with the 4th point and 10x line Akshay dictated...; dec: 235 | material | T is old Akshay v2 first-person (3 asks, "Repost/ comment on my post", "Do I have your buy in", Thanks & Regards Akshay Datt). W from Zoya (decision 235), third person,... |
| Pre-release ask (HBD) | 64b27494; Off; Y; daily sweep; Akshay; v2; 10-12 | yes; From: Akshay (Akshay's inbox); Status: approved; dec: - | identical | both Akshay; T Mode Off |
| Pre-release ask (un#) | 012579c0; Off; Y; daily sweep; Akshay; v2; 10-12 | yes; From: Akshay (Akshay's inbox); Status: approved; dec: - | identical | both Akshay; T Mode Off |
| Precall follow-up 1 | fab21328; -; Y; -; Mamatha; v1; 10-15 | yes; From: nobody; Status: retired; dec: - | identical | W retired (routine 2); T Approved, Mode empty, Sender Mamatha but signed Akshay |
| Precall follow-up 2 | 4d17f6e0; -; Y; -; Mamatha; v1; 10-15 | yes; From: nobody; Status: retired; dec: - | identical | W retired (routine 2) |
| Precall follow-up 3, close-out | fbe25437; -; Y; -; Mamatha; v1; 10-15 | yes; From: nobody; Status: retired; dec: - | identical | W retired (routine 2) |
| Recording calendar invite description | 122d46c6; -; Y; -; Akshay (calendar); v1; 10-09 | yes; From: Akshay (calendar invite); Status: approved; dec: - | identical | both Akshay (calendar); both cut off at the emergency contact line |
| Recording confirmed with AV check (B2S) | 7c7cdae0; -; Y; -; Chaandini; v1; 10-09 | yes; From: Chaandini; Status: approved; dec: - | minor | one word: T "a time that works for {guest name}" vs W "a time that suits {guest name}". Both Chaandini |
| Recording confirmed, link and prep note | 4e8e5dd6; -; Y; -; Mamatha; v1; 10-12 | yes; From: Zoya; Status: approved; dec: - | material | T: "Thanks for booking the slot for the recording. We've shared the updated recording link for {date}, from {start} to {end} {timezone}. Looking forward to connecting."... |
| Recording day check-in | c526bcf7; -; Y; -; Mamatha; v1; 10-09 | yes; From: Zoya; Status: approved; dec: - | minor | body same; T Regards Mamatha vs W best/Zoya |
| Recording follow-up 1 | 2313c66f; -; Y; -; Mamatha; v1; 10-15 | yes; From: nobody; Status: retired; dec: - | identical | W retired (routine 3) |
| Recording follow-up 2 | 42b24a11; -; Y; -; Mamatha; v1; 10-15 | yes; From: nobody; Status: retired; dec: - | identical | W retired (routine 3) |
| Recording follow-up 3, last check | 3c12f84b; -; Y; -; Mamatha; v1; 10-15 | yes; From: nobody; Status: retired; dec: - | identical | W retired (routine 3) |
| Recording slot request | 9f508edf; Send; Y; inbox; Mamatha (Akshay after a precall); v1; 10-12 | yes; From: Zoya; Status: approved; dec: - | minor | body same; T "Regards, Akshay" (Sender Mamatha/Akshay, Mode Send, inbox) vs W best/Zoya, From Zoya. Link podm.in/book in both: per decision 235 a link mail must come... |
| Recording tomorrow: looking forward, prep note | 3f519a30-818e; Send; Y; calendar; Akshay, new mail; v2; 10-13 | yes; From: Zoya (decision 235; was Akshay); Status: approved, with the setup checklist Akshay dictated on the...; dec: 126, 235 | material | T from Akshay (Akshay's inbox) (Mode Send, calendar; Notes "Always signed Akshay: it goes from his account"), opens "Hi {guest first name}, Looking forward to... |
| Release date confirmed, review copy coming | e219b204; -; Y; -; Mamatha; v1; 10-09 | yes; From: Zoya; Status: approved; dec: - | minor | body same; T Regards Mamatha vs W best/Zoya |
| Release-day post copies (un#) | 0c7ac82f; -; Y; -; Mamatha; v2; 10-09 | yes; From: Zoya; Status: approved; dec: - | minor | body same; T Regards Mamatha vs W best/Zoya |
| Release-day reminder with post copies | ab4356db; -; Y; -; Mamatha; v2; 10-09 | yes; From: Zoya; Status: approved; dec: - | material | T intro "Mamatha here from the {show name} team." vs W "Zoya here, I work with Akshay on the {show name} podcast." (decision 204); T Regards Mamatha vs W best/Zoya.... |
| Reschedule after guest cancels | e917f3e3; Send; Y; inbox; Mamatha; v1; 10-12 | yes; From: Zoya; Status: approved; dec: - | minor | body same; T "Regards, Akshay" (Sender Mamatha, Mode Send, inbox) vs W best/Zoya. Link podm.in/book so must be Zoya per 235 |
| Reschedule from our side | b92e4953; -; Y; -; Mamatha; v1; 10-09 | yes; From: Zoya; Status: approved; dec: - | material | T "As discussed, due to {reason}, Akshay won't be able to join ... We apologize for any inconvenience caused." Regards Mamatha. W rewritten 15 Oct (decision 208): never... |
| Short-form and collab answer | 48441c21; Off; Y; inbox; Mamatha; v1; 10-16 | yes; From: nobody; Status: retired 15 Oct (decision 208): reels, shorts, collab,...; dec: 208 | minor | body same; T "Regards, Akshay" (Sender Mamatha, Mode Off) vs W best/Zoya. W retired 15 Oct (decision 208: publishing asks go on Akshay's list). T Mode Off agrees |
| Show credentials: Founder Thesis | 3f519a30-814c; Off; Y; none; (snippet); v1; 10-15 | yes; From: reference block. Zoya's precall invite (section...; Status: approved; dec: 130 | material | T: numbered 1. 2. list, names Ashneer Grover and Amit Agarwal (NoBroker), "280k: total community of followers on LinkedIn, with more than 50k at VP or higher levels".... |
| Sponsored commercials (FT) | 3283f47a; Send; Y; inbox; Zoya, on the thread; v4; 10-18 | yes; From: Zoya, in her voice and third person (decision...; Status: approved; dec: 227 | material | T sign-off "Stay awesome ✨ / Zoya" (old decision 206) vs W "best, / Zoya ✨" (decision 345). T "sponsored feature" vs W "sponsored appearance". T bullet "50,000+ of our... |
| Sponsored commercials (un#) | cc727084; -; N; -; Mamatha; v1; 10-09 | yes; From: Akshay (Akshay's inbox); Status: not approved; dec: - | identical | both not approved placeholder; T Approved=NO, Sender Mamatha; W From Akshay [address] |
| Sponsored follow-up 1 | 6ac0d550; -; Y; -; Mamatha; v1; 10-09 | yes; From: nobody; Status: retired; dec: - | identical | W retired (routine 1) |
| Sponsored follow-up 2, close-out | ed47bf9c; -; Y; -; Mamatha; v1; 10-09 | yes; From: nobody; Status: retired; dec: - | identical | W retired (routine 1) |
| Sponsored follow-up 3, bump | ef51b532; -; Y; -; Mamatha; v1; 10-09 | yes; From: nobody; Status: retired; dec: - | identical | W retired (routine 1) |
| Sponsored turned down: close the thread | 3f719a30; Send; Y; inbox; Akshay, reply on thread; v1; 10-21 | yes, twice: same-name toggle is in Retired (From: nobody; Status: retired; dec: 145). Content matches 'Sponsored turned down: close note with the influencer line (new)' (From: Zoya, on the thread, in her voice (decision 379,...; Status: live from 15 Oct (decision 196): the Templates row...; dec: 196, 379) | material | Name matches the RETIRED toggle (whose body is the old "Noted, thanks ... we'll share the pricing available at that time"), but T body is the new influencer close note,... |
| Sponsored: founder wrote directly | 3f519a30-8103; Draft; Y; inbox; Akshay, reply in thread; v3; 10-22 | yes; From: Zoya, her voice, third person (decision 235); Status: approved (test, 16 Oct); dec: 235 | material | T from Akshay (Mode Draft): "Hi {guest}", "We love what you're building", "Think of it like", "iOS device (a premium, urban audience)", "Let me know if you need more... |
| Sponsored: no organic slot (via PR) | 3f519a30-81cc; Draft; Y; inbox; Akshay, reply in thread; v3; 10-22 | yes; From: Zoya, her voice, third person (decision 235); Status: approved (test, 16 Oct); dec: 235 | material | Same pattern: T Akshay Draft, "for the Founder Thesis podcast. We love what...", iOS device, "Let me know if you need more details.", Regards Akshay; W Zoya "for... |
| Tier 1.5: alignment check call | 3f519a30-8156; Draft; Y; inbox; Akshay, reply in thread; v3; 10-15 | yes; From: nobody; Status: retired 16 Oct (decision 235): Zoya's "FT precall invite...; dec: 235 | minor | Body same plus T bracket rule. Same control clash as Tier 1 |
| Tier 1: keen, ask for a pre-call | 3f519a30-815a; Draft; Y; inbox; Akshay, reply in thread; v3; 10-15 | yes; From: nobody; Status: retired 16 Oct (decision 235): Zoya's "FT precall invite...; dec: 235 | minor | Body same; T adds bracket rule (decision 198) and a full stop after "{him/her}". CONTROL: T Mode Draft, Approved, live in inbox routine from Akshay; W retired 16 Oct... |
| Tier 2: alignment check call, organic undecided | 3f519a30-81ac; Draft; Y; inbox; Akshay, reply in thread; v3; 10-15 | yes; From: nobody; Status: retired 16 Oct (decision 235): Zoya's "FT precall invite...; dec: 235 | minor | Body same plus T bracket rule. Same control clash |
| un# precall invite | 7356c347; -; Y; -; Mamatha; v1; 10-09 | yes; From: Zoya; Status: approved; dec: - | material | T Mamatha: "It's great to connect with you! We would love to schedule a quick pre-call with {guest} or someone from their team. Please select a time that works via:... |
| Vendor or service pitch redirect | 3d1123b7; Send; Y; inbox; Akshay; v1; 10-10 | yes; From: Zoya, right after Akshay's "thanks {first name},...; Status: approved (test, 16 Oct); dec: 235 | material | T (Mode Send, Akshay): "Hi {first name} - thanks for reaching out, could you fill this out: podm.in/pitch-to-us", Thanks & Regards Akshay Datt. W: from Zoya right after... |
| Holding reply to a fresh pitch (new) | none | yes; From: Akshay (Akshay's inbox); Status: live from 15 Oct (decisions 195, 199). One line, no...; dec: 195, 199 | one-sided | Wording toggle only; no Templates row |
| No-show note (from Zoya) | none | yes; From: Zoya, on the thread (decision 236; was Akshay); Status: v2 test sent 16 Oct after Akshay's edits (no flat decline:...; dec: 234, 236, 238 | one-sided | Wording toggle only; no Templates row |
| Acknowledgement (new) | none | yes; From: Akshay or Zoya; Status: live from 15 Oct; dec: 200 | one-sided | Wording toggle only; no Templates row |
| Where the episode is published: Founder Thesis | none | yes; From: Zoya; Status: approved by Akshay, 21 Oct; dec: 372 | one-sided | Wording toggle only; no Templates row |
| Sponsored: what's included (FT) | none | yes; From: Zoya, on the thread, her voice; Status: approved (Akshay, 18 Oct); dec: 332 | one-sided | Wording toggle only; no Templates row |
| Price negotiation: hold the price, offer The Spotlight Podcast | none | yes; From: Zoya, on the thread (decision 237, Akshay, 16 Oct); Status: approved (test sent 16 Oct, Bharat Agarwal case); dec: 237 | one-sided | Wording toggle only; no Templates row |
| Sponsored yes: next steps | none | yes; From: Zoya; Status: approved (sent to Siddhi, Media Mantra, 16 Oct); dec: 260 | one-sided | Wording toggle only; no Templates row |
| Payment reminder | none | yes; From: Zoya, on the invoice thread; Status: approved (decision 227); dec: 227 | one-sided | Wording toggle only; no Templates row |
| Payment received, thanks | none | yes; From: Zoya, on the invoice thread; Status: approved (decision 227); dec: 227 | one-sided | Wording toggle only; no Templates row |
| Sponsored for a repeat guest (FT and un#) | none | yes; From: Zoya, on the pitch thread; Status: approved (Akshay, 22 Oct 2026); dec: - | one-sided | Wording toggle only; no Templates row |
| Commercials asked before the precall | none | yes; From: Zoya, on the thread, Akshay in Cc; Status: approved (Akshay, 22 Oct, decision 396); dec: 396 | one-sided | Wording toggle only; no Templates row |
| Declined invite: is the call still on? | none | yes; From: Zoya (FT); Status: approved; dec: - | one-sided | Wording toggle only; no Templates row |
| Double booking check (new) | none | yes; From: Zoya (Zoya's inbox), sent by the calendar run; Status: approved (test, 16 Oct); dec: 209 | one-sided | Wording toggle only; no Templates row |
| Asks to see the video before release | none | yes; From: Zoya; Status: approved (Akshay's reply to Disha, Communicate India, 15...; dec: 210 | one-sided | Wording toggle only; no Templates row |
| Invoice to raise (to Jaya) | none | yes; From: Zoya, WhatsApp; Status: approved (sent 16 Oct); dec: - | one-sided | Wording toggle only; no Templates row |
| Confirm a payment (to Jaya) | none | yes; From: Zoya, WhatsApp; Status: approved (decision 227); dec: 227 | one-sided | Wording toggle only; no Templates row |
| Edit notes from a guest (to Sarika) | none | yes; From: Zoya, WhatsApp; Status: approved (decision 226); dec: 226 | one-sided | Wording toggle only; no Templates row |

## Material differences in detail

**Admin ask: noted, added before release** (Send / inbox)

T signed "Thanks & Regards, Akshay Datt" from Akshay (Send/inbox); W from Zoya, best/Zoya. Example promise line differs: T "We'll share the edited episode with you for review before it goes live" vs W "We'll send you the episode links the day it goes live". W trigger excludes cut review/mention/tag (decision 208, goes to Akshay's list); T trigger still includes "see the cut for review ... a mention or tag".

**Edit notes: noted with thanks** (Send / inbox)

body same; T signed "Thanks & Regards, Akshay Datt", sender Akshay (Akshay's inbox) Mode Send inbox; W from Zoya (since 16 Oct), best/Zoya, plus [WhatsApp Sarika the notes] instruction (decision 226).

**Editorial decline, not a fit (non-founder or too early)** (- / -)

T "we can explore the sponsored route as well", Regards Mamatha; W "we can offer a sponsored appearance on the pod as well", best/Zoya; W From Zoya.

**Form received, release timeline** (- / -)

T "8 to 10 weeks" vs W "10 to 12 weeks" (and FT thank-you now says ~12 weeks); T Regards Mamatha vs W Zoya.

**FT precall invite to PR** (- / -)

T is Mamatha's old v1: alignment-check framing ("helps us decide ... whether we can offer them an organic appearance"), no Tier purpose lines, stats list with "{link: past guests sheet}" (sheet link banned by decision 222), "One million + views", 280k "employer branding", Ashneer Grover and Amit Agarwal named, misspellings (Bhikhchandani, Paware), podm.in/note line, Regards Mamatha. W: Zoya voice, Tier 1/1.5/2 purpose lines, "never mention organic or sponsored", podm.in/guest-list, 1.25mn views, 50k+ director level, no podm.in/note line, best/Zoya.

**FT precall, PR wants to talk first** (- / -)

T long formal Mamatha version, Regards Mamatha; W short Zoya rewrite (decision 201). Same link podm.in/30min, same meaning.

**Mamatha's daily list** (Send / daily sweep)

T opens "{n} guests on FT: Today (...)" and ends "Open the list: {FT: Today link}"; W drops both and adds "[Founder Thesis rows aren't on her list: Zoya handles them.]". Signed Regards Akshay in both.

**Pre-release ask (FT)** (Off / daily sweep)

T is old Akshay v2 first-person (3 asks, "Repost/ comment on my post", "Do I have your buy in", Thanks & Regards Akshay Datt). W from Zoya (decision 235), third person, 4 asks incl. "Ask your team to like and comment", "as much as 10x the views" line, "Can we count on you", best/Zoya. T Mode Off, Sender Akshay.

**Recording confirmed, link and prep note** (- / -)

T: "Thanks for booking the slot for the recording. We've shared the updated recording link for {date}, from {start} to {end} {timezone}. Looking forward to connecting." Regards Mamatha. W: one line, no greeting or sign-off, "great, thanks for letting me know {first name}!" from Zoya (decision 208).

**Recording tomorrow: looking forward, prep note** (Send / calendar)

T from Akshay (Akshay's inbox) (Mode Send, calendar; Notes "Always signed Akshay: it goes from his account"), opens "Hi {guest first name}, Looking forward to {conversation} tomorrow", Regards Akshay. W from Zoya (decision 235; was Akshay), "Hey {guest first name}! Akshay's looking forward to the conversation tomorrow", prep note in third person, best/Zoya; W status mentions a setup checklist Akshay dictated (16 Oct) that is not in the W body either.

**Release-day reminder with post copies** (- / -)

T intro "Mamatha here from the {show name} team." vs W "Zoya here, I work with Akshay on the {show name} podcast." (decision 204); T Regards Mamatha vs W best/Zoya. Rest same.

**Reschedule from our side** (- / -)

T "As discussed, due to {reason}, Akshay won't be able to join ... We apologize for any inconvenience caused." Regards Mamatha. W rewritten 15 Oct (decision 208): never a specific reason, two variants (more than a day's notice: personal event clashing; same day: something personal came up, sorry for short notice), "Any slot next week is fine", best/Zoya.

**Show credentials: Founder Thesis** (Off / none)

T: numbered 1. 2. list, names Ashneer Grover and Amit Agarwal (NoBroker), "280k: total community of followers on LinkedIn, with more than 50k at VP or higher levels". W: 1/ 2/ format, drops Ashneer Grover and Amit Agarwal, "280k+: our followers on LinkedIn, 50k+ of them director level and above". Same links (podm.in/guest-list, podm.in/note).

**Sponsored commercials (FT)** (Send / inbox)

T sign-off "Stay awesome ✨ / Zoya" (old decision 206) vs W "best, / Zoya ✨" (decision 345). T "sponsored feature" vs W "sponsored appearance". T bullet "50,000+ of our LinkedIn followers (280k in all) are director level or above, including 11,000 VPs and 6,100 CXOs" vs W "50k+ director level and above folks follow us on LinkedIn (280k+ followers in all)". Close: T "lmk if {guest} is keen and I'll share what's included and how it works!" vs W "let me know if {guest} is interested and I'll share what's included and how it happens!". W adds instruction: "a conversation with Akshay", never "me"; discount asks get the Price negotiation mail (decision 237). Both Zoya, same price and link.

**Sponsored turned down: close the thread** (Send / inbox)

Name matches the RETIRED toggle (whose body is the old "Noted, thanks ... we'll share the pricing available at that time"), but T body is the new influencer close note, i.e. matches toggle "Sponsored turned down: close note with the influencer line (new)". Against that toggle: T "Think of me as a B2B influencer" vs W "Think of Akshay as a B2B influencer"; T "Thanks & Regards, Akshay" vs W "best, Zoya ✨"; T Sender Akshay (Akshay's inbox) (Mode Send, inbox, Notes "Mamatha in Cc") vs W From Zoya, To whoever said no, Cc rest of their side and Akshay (decision 379, 21 Oct). T last edited 21 Oct 23:47 UTC but still Akshay.

**Sponsored: founder wrote directly** (Draft / inbox)

T from Akshay (Mode Draft): "Hi {guest}", "We love what you're building", "Think of it like", "iOS device (a premium, urban audience)", "Let me know if you need more details.", Regards Akshay; T has bracket rules (decisions 198, 197, 203). W from Zoya, third person: "Hey {guest}!", "Akshay loves what you're building", "Think of it as", "iPhone (a premium, urban crowd)", "lmk if you'd like the details!", best/Zoya. Neither body carries a link though T Notes define {sponsored link}.

**Sponsored: no organic slot (via PR)** (Draft / inbox)

Same pattern: T Akshay Draft, "for the Founder Thesis podcast. We love what...", iOS device, "Let me know if you need more details.", Regards Akshay; W Zoya "for Founder Thesis. Akshay loves what...", iPhone, "lmk if you'd like the details!", best/Zoya. T Notes still "Mamatha sends the commercials if they reply keen" (now Zoya, decision 227).

**un# precall invite** (- / -)

T Mamatha: "It's great to connect with you! We would love to schedule a quick pre-call with {guest} or someone from their team. Please select a time that works via: unhashed.co/precall. Look forward to hearing from you." Regards Mamatha. W Zoya: "Lovely to connect. We'd love a quick pre-call with {guest} or someone from {his/her} team [purpose line for the row's Tier]. Pick any free slot here: unhashed.co/precall", best/Zoya.

**Vendor or service pitch redirect** (Send / inbox)

T (Mode Send, Akshay): "Hi {first name} - thanks for reaching out, could you fill this out: podm.in/pitch-to-us", Thanks & Regards Akshay Datt. W: from Zoya right after Akshay's holding line (decision 235: link goes from Zoya): "Hey {first name}! could you fill out this form so we can take a look at your offering? podm.in/pitch-to-us", best/Zoya.

## Control clashes worth fixing first

Rows the inbox, calendar and daily sweep routines still read for mail from Akshay's inbox, where the wording page has moved on:

- Mode Send, T sender Akshay or Mamatha, W sender Zoya: Admin ask, Edit notes, Recording slot request, Reschedule after guest cancels, Recording tomorrow, Sponsored turned down, Vendor redirect. Four of these carry a link (podm.in/book, podm.in/pitch-to-us, the call link), which CLAUDE.md says must come from Zoya.
- Mode Draft from Akshay, W from Zoya: Sponsored: founder wrote directly, Sponsored: no organic slot (via PR).
- Mode Draft, live in the inbox routine, but W retired 16 Oct (decision 235): Tier 1, Tier 1.5, Tier 2.
- FT thank-you after recording: Mode Send and Trigger "transcript is in Drive (decision 173)", while W and T Notes say it is a draft Akshay sends himself, drafted as soon as recording is confirmed, no transcript (decisions 300, 374, 412).
- Sponsored commercials (FT): both Zoya, but T still signs "Stay awesome ✨ / Zoya" (decision 206) instead of "best, / Zoya ✨" (decision 345) and uses older stats wording.
- Mamatha's daily list (Send, daily sweep): T still opens with the FT: Today count and link; W says FT rows are not on her list.
- Retired on W but still Approved with no Mode on T (harmless while Mode is empty): Decline with sponsored offer, FT thank-you PR block variant, PR form chaser, Precall follow-ups 1 to 3, Recording follow-ups 1 to 3, Sponsored follow-ups 1 to 3. Eval ready, Mamatha added and Short-form are retired on W and Mode Off on T.
- Pre-release ask (un#): W still says From Akshay, though un# moved to Zoya on 19 Oct (decisions 307, 313); T is Mode Off.

## Toggles with no Templates row

- Holding reply to a fresh pitch (new) (section 0; Status: live from 15 Oct (decisions 195, 199). One line, no greeting, no sign-off....)
- No-show note (from Zoya) (section 0; Status: v2 test sent 16 Oct after Akshay's edits (no flat decline: move them to...)
- Acknowledgement (new) (section 0; Status: live from 15 Oct)
- Where the episode is published: Founder Thesis (section 1; Status: approved by Akshay, 21 Oct)
- Sponsored: what's included (FT) (section 1; Status: approved (Akshay, 18 Oct))
- Price negotiation: hold the price, offer The Spotlight Podcast (section 1; Status: approved (test sent 16 Oct, Bharat Agarwal case))
- Sponsored yes: next steps (section 1; Status: approved (sent to Siddhi, Media Mantra, 16 Oct))
- Payment reminder (section 1; Status: approved (decision 227))
- Payment received, thanks (section 1; Status: approved (decision 227))
- Sponsored for a repeat guest (FT and un#) (section 1; Status: approved (Akshay, 22 Oct 2026))
- Commercials asked before the precall (section 2; Status: approved (Akshay, 22 Oct, decision 396))
- Declined invite: is the call still on? (section 2; Status: approved)
- Double booking check (new) (section 2; Status: approved (test, 16 Oct))
- Asks to see the video before release (section 3; Status: approved (Akshay's reply to Disha, Communicate India, 15 Oct; decision 210))
- Invoice to raise (to Jaya) (section 6; Status: approved (sent 16 Oct))
- Confirm a payment (to Jaya) (section 6; Status: approved (decision 227))
- Edit notes from a guest (to Sarika) (section 6; Status: approved (decision 226))

## Templates rows with no toggle

None. Every one of the 55 rows has a same-name toggle. One caveat: "Sponsored turned down: close the thread" matches a retired toggle by name, while its body is the live "close note with the influencer line (new)" toggle.

## Wording page intro, verbatim (addresses redacted)

> Every mail and WhatsApp wording the agents use, one toggle per mail, grouped by stage. This page replaces the Templates database. A new or changed template goes live only once Akshay replies "approved" to Zoya's "[Zoya test] <template>" mail; until then its Status says "test sent". A brand-new template isn't sent until then; one that was already live (re-voiced for Zoya on 16 Oct) keeps going out as is unless Akshay replies with edits (decision 238). Zoya's routine reads it every run, so a change here is live for her mails. The inbox and calendar routines still read the Templates database for the mails they send from Akshay's inbox until it's retired (Rules for Zoya, section 10).
>
> Placeholders in braces are filled from the row. A line in square brackets is an instruction to the agent and never goes out. Zoya's mails end with her sign-off, best, / Zoya ✨ (decision 345, replacing 206). Her voice is Akshay's: short and direct, occasional lowercase and natural fragments, numbered points as 1/ 2/ 3/, one ask, at most one emoji, never corporate, never a made-up typo (decision 345, replacing 201). <b>Since 16 Oct (decision 235), Akshay's account only sends the short, link-free lines in section 0</b>, through Gmail as replies inside the existing thread, so his inbox keeps the whole history. Every mail with a link or an attachment, including the ones that used to go in his name, comes from Zoya in her voice and the third person ("Akshay loved the conversation"). Akshay adds a personal line by hand whenever he wants. Every mail is sent as paragraphs and lists, with real links on approved short links only (decision 184). Keep mails short, fluid and human: people actually read short ones. Every mail is written from the whole thread and states only what the thread or calendar shows; never thank anyone for a call or meeting that didn't happen (decision 198).

> ## 0. From Akshay's account: short lines, no links (decision 235)

> ## 6. Team WhatsApp
>
> From Zoya on Akshay's WhatsApp, to Jaya and Sarika only (decision 226). Each line is one short message.

> ## Retired: do not send
>
> Kept only so nobody rewrites them by accident. Each is replaced by the routine named.
