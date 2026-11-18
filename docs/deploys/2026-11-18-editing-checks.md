# Deploy: editing checks, rough-cut test (18 Nov 2026)

- Source: routines/editing-checks.txt at commit 70a99f3, 7,601 bytes, sha256 f6bdcdb7e054a90b...
- Change: part C skips an episode when a rough-cut Team task (Task type Rough cut, or Video on older rows) is allocated. Sarika added Rough cut, Main Epi, Clip, Short and Promo task types on 18 Nov; Main Epi is the full edit.
- Deployed by the Episode editor chat (the routines post into it, so only it can change their prompts), at the CTO's request.
- Triggers: trig_0177CBiFc4zP8SGCaVip97Gc, trig_01AU4fQevmq39TDZX6LvC4cq, trig_01SXrnWJb2iz5Q3zts34VZu4. Each live prompt byte-compared with the file: equal.
- Not deployed: the editing doc v2 brief (decision 602, proposal 4), waiting on Akshay's A10.
