# d420 deploy files (Cleanup-accepted, 26b3b60 and 759daf4)

Byte-exact copies of the accepted builds, for whoever deploys them. This builder session doesn't deploy (standing rule), so they're staged here.

| Routine | Trigger | File | Bytes / sha256 |
|---|---|---|---|
| Zoya | trig_01UPT8LDrBDL5JQqW91Awgbo | zoya-one.txt | 42,109 / 23551dc5bb4a0d12 |
| Calendar (B1 build only) | trig_01Voiz5YsK2SnVf2STF8PoSH | calendar-b1.txt | 57,968 / f6d140196f3b75b4 |
| Daily sweep | trig_01MdfUFg2qrebDWgiHwncgnd | sweep.txt | 35,047 / 06c4120b2cd48ef1 |

**Zoya's condition comes first.** Move `refs/heads/zoya-slow-pin` from e20647b to f70901f6f07d4a6610fda60132b4cdbb5ac43979:
- **It's a plain fast-forward:** checked with `git merge-base --is-ancestor`. Use `git push origin f70901f6f07d4a6610fda60132b4cdbb5ac43979:refs/heads/zoya-slow-pin --force-with-lease=refs/heads/zoya-slow-pin:e20647bc2da9d568dfec3787ff3e3a17fa101afb`.
- **Read it back:** `git ls-remote origin refs/heads/zoya-slow-pin` should show f70901f…, and `git show f70901f:routines/zoya/release/zoya-slow-work.txt | sha256sum` should start fae90990931445db.
- **Then deploy zoya-one, timed around the lock:** outside :38 to :45, so no run holds the lock, and before 07:38 JST.

**WhatsApp isn't here:** it isn't accepted. The rebuilt B2 goes back to Cleanup. B2 28,654 / 485a321070e05a3e, WhatsApp on B2 with the batch 29,662 / b668e57123cf0b6f.
