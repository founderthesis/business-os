# r25 delta b85248e to 548588a (decisions 546 and 547): Cleanup verdict

Cleanup, 11 Nov. Read-only. I built every file twice and each pair came out byte-identical. I built Zoya from a fresh worktree at f70901f with build_one.patch, pinned at 12de32e1df2cb4ba70ab583fc97848872012500d.

**Accepted. Deploy it.**

## What changed

- **Quiet hours.** WhatsApp STEP 0w 3/ now reads "01:30 to 07:30 JST, decision 547". In capture, actions, the hourly and the SLOW file, the hard-coded "decision 393: 00:30 to 07:30 JST" or "07:30 to 00:30 JST" becomes "decision 547", and the times are read from Cadences.
- **Cadences page.** I read the page itself (3ff19a30…, edited 11 Nov). It already says "between 07:30 and 01:30 JST" and "no mail to anyone outside the team between 01:30 and 07:30 JST, decision 547". So the prompts that cite Cadences pick up the new hours.
- **SLOW task opening.** It runs at "00:08, 08:08, 11:08, 14:08, 17:08, 20:08 and 23:08 JST on weekdays (decision 546)". The hourly drops SLOW's times and cites decisions 449, 450 and 546.
  - Row 546 says six runs. Row 547 adds the 00:08 run. Together they make seven, which matches.
  - 00:08 and 23:08 both sit before the 01:30 quiet start.
- **SLOW task pin fields.** It names pin 12de32e, `must start 7e72f8ddb97fe0fd` and `total = 94,643 characters`. All three match the SLOW file at the pin.
- **Section 6.** Unchanged.
- **No other edits.** No rule was cut, deployment references updated, no new em dash, and the hourly is 62,951 bytes, under 63,000.

## Deploy note

Changing the SLOW task's text doesn't move its schedule. trig_015i1JzfyNDoYfrgTfbqDSXu's cron must also change to the seven weekday times in update_trigger, or the new runs won't happen. The prompt only describes the schedule. Use 8 0,8,11,14,17,20,23 * * 1-5 with CRON_TZ=Asia/Tokyo.

## Final r25 deploy table

| Order | File | Bytes | sha256 | Trigger |
|---|---|---|---|---|
| 1 | Section 6 paste: r25/section6-535.md | 6,426 | f827086c134895a3113306f1a4959122ea2ed5083c324829a2edd7bd4cda4c29 | pasted into inbox actions |
| 1 | Inbox actions: r25/actions.txt | 48,366 | d0a8c26a63ddb697c2d0edd2e6620e3f4be17240ff2097cc3a9d66e7230f94da | trig_012HbtmVKHUDeFZnFyooSgL3 |
| 2 | Inbox capture: r25/capture.txt | 50,812 | 41e188c51713d841523102214cab72045907748abae663c17b5205885bb47b0c | trig_0189eZvAD8x4357cfevgZ3No |
| 3 | WhatsApp: r25/whatsapp.txt | 39,065 | ddb69276381303f10bd16ba0440d0f123e3d83677635cf71e52cc2675c5369b7 | trig_01MnmJYorWrd61K7b5BCqXr1 |
| 4 | Pin refs/heads/zoya-slow-pin to 12de32e1df2cb4ba70ab583fc97848872012500d. SLOW file at the pin, 94,643 characters | 94,647 | 7e72f8ddb97fe0fdbf5ea3601dd02ae6a2627d4eb5af94dac8567bd4ba4ca212 | ref move |
| 4 | Zoya SLOW task: r25/zoya/zoya-slow.txt, with the cron change above | 15,683 | 825a3716cdf059b0bcfc9abd8e143017d3481b217e6dbc01a646129f80f948f8 | trig_015i1JzfyNDoYfrgTfbqDSXu |
| 5 | Zoya hourly: r25/zoya/zoya-one.txt | 62,951 | 821895c1d1a8a499fbfccf28558aeaf62cf8a4e855881b6d3b28631c9820f120 | trig_01UPT8LDrBDL5JQqW91Awgbo |

Deploy rows 4 and 5 together.
