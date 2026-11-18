# Deploy: editing checks, rough-cut test (18 Nov 2026)

- Source: routines/editing-checks.txt at commit 70a99f3, 7,601 bytes, sha256 f6bdcdb7e054a90b...
- Change: part C skips an episode when a rough-cut Team task (Task type Rough cut, or Video on older rows) is allocated. Sarika added Rough cut, Main Epi, Clip, Short and Promo task types on 18 Nov; Main Epi is the full edit.
- Deployed by the Episode editor chat (the routines post into it, so only it can change their prompts), at the CTO's request.
- Triggers: trig_0177CBiFc4zP8SGCaVip97Gc, trig_01AU4fQevmq39TDZX6LvC4cq, trig_01SXrnWJb2iz5Q3zts34VZu4. Each live prompt byte-compared with the file: equal.
- Not deployed: the editing doc v2 brief (decision 602, proposal 4), waiting on Akshay's A10.

## Second deploy: editing doc v2 brief (decision 602, A10 approved by Akshay 18 Nov)

- Source: routines/editing-checks.txt at commit e530cdd, 8,792 bytes, sha256 3815506e7b551524...
- Change: part C only. The 9-tab editing doc, the brief rules (brief wins over skill rules, every list a real table, a self-check) and counts in the hand-back. The Rough cut test is unchanged.
- Deployed by the Episode editor chat to the same three triggers; each byte-compared with the file: equal.
- Skill zips for Akshay to upload: docs/proposals/editing-doc-v2/zips/ (ft-lower-thirds, ft-episode-titles, thumbnail-copy).
