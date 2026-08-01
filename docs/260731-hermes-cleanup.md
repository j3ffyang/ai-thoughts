# Clean Up Bloat Skills & Plugins in Hermes



6 hub-installed, 66 builtin, 28 local — 100 enabled, 0 disabled

hermes skills opt-out --remove
Already opted out — marker was already present.

6 hub-installed, 4 builtin, 28 local — 38 enabled, 0 disabled

jeff@debian-8gb-fsn1-1:~$ hermes skills opt-out --remove
Opted out of bundled skills. Future install / update / sync runs will not seed bundled skills into this profile.


If you ever want to revert a profile-wide opt-out and bring the core skills back, you can simply run hermes skills opt-in --sync to re-seed everything.