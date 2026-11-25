# Verification record

Date: 2026-11-25

## Automated checks performed by tools/build.py
- Parse every JSON document in both packs.
- Confirm Behavior Pack UUID matches the Resource Pack dependency.
- Confirm entity identifiers match between server and client definitions.
- Confirm geometry, texture, animation, animation-controller and particle identifiers resolve.
- Confirm all referenced animation names exist.
- Confirm every geometry bone parent exists.
- Confirm required texture and pack-icon files exist and have valid PNG headers.
- Confirm generated .mcaddon and both .mcpack archives pass ZIP CRC checks.
- Confirm the combined .mcaddon contains both inner .mcpack packages.

## In-game checks still required
- Import into Minecraft Bedrock 26.66.
- Confirm both packs activate without content-log errors.
- Spawn egg and /summon test.
- Entity rendering, texture, scale and hitbox review.
- Idle / locomotion / attack transition and particle playback check.
- Ground-slam and void-pulse damage range / cooldown test.
- Loot, multiplayer and dedicated-server tests.

Passing JSON and ZIP checks does not prove engine compatibility, balance or visual correctness. Do not call this release fully game-tested until the in-game checklist passes.
