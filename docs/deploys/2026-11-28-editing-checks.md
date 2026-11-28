# Editing checks deploy, 28 Nov 2026

- File: routines/editing-checks.txt at 831f021, 10,004 bytes, sha256 f2efa466ebdcc564ff164657cee53b08745e3a207bd87929e0113400f0dbb11a, no trailing newline.
- Change: decision 693 (Akshay, 28 Nov: "30 days is good"). Part C starts an editing doc only when Planned release is 30 days away or less, unless Next action (Sarika) asks for the doc. A release further out is simply not picked yet, with no Zoya response line. Trigger: Beerud Sheth's doc was built on 27 Nov for a 15 Apr 2027 release.
- Tasks: trig_01SXrnWJb2iz5Q3zts34VZu4, trig_0177CBiFc4zP8SGCaVip97Gc and trig_01AU4fQevmq39TDZX6LvC4cq, prompt only.
- Verify: each update_trigger result's prompt compared with the file byte for byte; all three EQUAL on the first deploy (10:13 UTC), sha256 f2efa466...0dbb11a.
- Deployed by: Episode editor session (session_019pwcV3jbCtwb56pcVB3o6J); the CTO's update_trigger is refused for routines that post into another conversation.
- Rollback: e6cf0fa (9,812 bytes, sha256 043519846bec44be97f7abc5f0c247d79b56f2d64582a5823a7b481cc8185a43).
- Left alone: Beerud Sheth's editing doc (built 27 Nov, release 15 Apr 2027).
