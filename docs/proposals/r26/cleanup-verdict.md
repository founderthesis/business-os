# r26 final (7bc9461): Cleanup verdict

Cleanup, 12 Nov. This review is read-only.

**Accepted. Deploy.**

I built every file twice and each pair was byte-identical. The builds match the repo copies and Main's table. Zoya came from a fresh worktree at f70901f with r26/zoya/build_one.patch, pinned at 63d63ec2ef9211dbc6a6b77b388aa57f96201d1f.

The SLOW task carries `git show 63d63ec…`, `must start 78332307d8ba3cfd` and `total = 94,829 characters`. All three match the file at the pin.

There's no new em dash anywhere.

## The two cuts the CTO asked about

### VOICE becomes a pointer

What the pointer keeps:
- the sign-off;
- never corporate;
- no em dashes;
- never describe herself;
- the 40% limit;
- whole-thread writing.

I checked every dropped line against the Rules for Zoya page as it reads today. The page has all of them:
- "hey <first name>,"
- fragments and "never a made-up typo";
- 1/ 2/ 3/;
- one ask, one link, one emoji (with the ✨ exemption);
- "kindly", "please find attached", "as per";
- the banned-word list, including "quick one" and "great question(s)";
- Plain English, with "a sponsored appearance on the pod" and all five idioms;
- polite to founders and CXOs.

RULES LOAD loads that page in full every run, a short read stops every send, and "where a page and this prompt differ, the page wins". So the cut loses no rule, and it removes a second copy that could drift (decision 357).

One gap: the page's "never corporate" list doesn't include "at your earliest convenience", which the old VOICE did. Add it to the page; no prompt change is needed.

### Engagements property list becomes "properties from its fetch"

NOTION DATA still says "Fetch each data source once to confirm property and option names", so every run reads the schema anyway. Nothing is lost.

## Size

| Build | Bytes | Under 63,000 target | Under 65,536 cap |
|---|---|---|---|
| Hourly | 62,996 | 4 | 2,540 |
| WhatsApp | 39,817 | | |
| Actions | 48,515 | | |
| SLOW task | 15,646 | | |

The SLOW file is 94,833 bytes, but it's read from git, not a prompt, so the cap doesn't apply.

The "21 bytes" was the hourly's margin under the 63,000 target at 2a1adc7, at 62,979 bytes. The gate took 17 of those, leaving 4. No build is anywhere near 65,536.

The next hourly addition needs its own cuts. It can go a little over 63,000, since the cap is 65,536, but 63,000 has been the working target.

## The rest of the delta, against the deployed r25

### Decision 555, in THREADING (hourly, SLOW file)

"Their side wrote on a newer chain: that one ... note 'thread moved to <subject> on <D Mon>'". This matches the ledger row. "Never a fresh mail" stays.

### Decision 557, in actions STEP 6c a0

| Eval verdict | Template |
|---|---|
| Book immediately or Strong consider | Tier 1 |
| Pre-call needed or Evaluate after call | Tier 1.5 |
| Anything else, or no eval | Tier 2 |

A named Tier still wins. This matches the ledger row, and "sponsored route" correctly falls to Tier 2.

### Decision 558, as amended

ROOM ASK is the hourly's alone, and the SLOW file now lists it with the things it never selects. It covers:
- Founder Thesis rows at Booking or Booked, with "date open" allowed;
- one WhatsApp to Mamatha per run, soonest first;
- one reminder after 24 hours;
- Akshay's list, once, within 48 hours of the recording;
- her link going to Recording link at once, and onto the invite once one exists.

This matches the ledger row. Founder Thesis only is right, because the other shows use fixed studio links.

TOOLS loads "+bluetick", and HARD allows ROOM ASK as the one FAST WhatsApp. The old 24-hour "no recording room" ask is replaced, not kept as a second copy.

### Early-exit gate

- **Hourly:** after the status script, "while it prints Failed and under 25 minutes since the start, write nothing final: go back to the first unfinished step". The 25 minutes bound it.
- **WhatsApp:** the same gate, plus four more changes:
  - at most 5 drafts a run, oldest tick first;
  - HIS OWN MESSAGE holds a draft: any message from his number in the chat since the draft, the draft's day included, not logged by a wa-send;
  - GREETING holds a draft that greets a name other than the recipient's;
  - the status line is "never rewritten or written by hand".

  All of these only hold or limit sends; none adds one.

### Citation and description trims

- "(decision 415: ...)" becomes "(decision 415)".
- "453, item 10" becomes "453", and "490, amending 448" becomes "490".
- The follow-ups page's summary is cut.
- Two example lists are shortened.

No rule is lost.

## Final deploy table (after r25, which is live)

| Order | File | Bytes | sha256 | Trigger |
|---|---|---|---|---|
| 1 | Inbox actions: r26/actions.txt | 48,515 | 2b894385566ff415cd406ad1920b6c7369859c34accc1619f43d0a38f979b49f | trig_012HbtmVKHUDeFZnFyooSgL3 |
| 2 | WhatsApp: r26/whatsapp.txt | 39,817 | c0ac14891bb14218739c72e5f620f82f5429ccd1ad12d0ad4aa52c4f89f72ead | trig_01MnmJYorWrd61K7b5BCqXr1 |
| 3 | Pin refs/heads/zoya-slow-pin to 63d63ec2ef9211dbc6a6b77b388aa57f96201d1f. The SLOW file there is 94,829 characters | 94,833 | 78332307d8ba3cfda5c02905c6718f6ce7ad4b00b23ff7f01165bfb0c787644b | ref move |
| 3 | Zoya SLOW task: r26/zoya/zoya-slow.txt | 15,646 | 4da2f1466a600967652e9336849fa11c2187962ed0d6816f2e6467bd2c4dd576 | trig_015i1JzfyNDoYfrgTfbqDSXu |
| 4 | Zoya hourly: r26/zoya/zoya-one.txt | 62,996 | b1b0b0acf5a1f9945a1db9099ac81cb3e3ab8e20222b4f650b0b097ebf810b23 | trig_01UPT8LDrBDL5JQqW91Awgbo |

Deploy rows 3 and 4 together. Capture and section 6 don't change.

Keep the SLOW trigger's seven-time cron from r25. Zoya episodes isn't live and isn't deployed.
