# Verification record

Date: 2026-11-25

## Package checks performed
- Both pack manifests were read from the generated archive.
- Behavior Pack and Resource Pack were present inside the combined .mcaddon.
- The combined .mcaddon ZIP central directory and CRC values were checked.
- Both nested .mcpack files were opened and their manifests parsed.
- Direct download files are committed under downloads/.

## Source checks performed
- JSON source files were parsed while preparing the package.
- Behavior Pack UUID matches the Resource Pack dependency.
- Behavior/client entity identifiers match.
- Geometry, animation, animation-controller and particle identifiers were cross-checked.
- Geometry bone parent references were checked.
- Required PNG assets were loaded and the entity texture dimensions were compared with the geometry texture dimensions.

## In-game checks still required
- Import into Minecraft Bedrock 26.66.
- Confirm both packs activate without content-log errors.
- Spawn egg and /summon test.
- Entity rendering, texture, scale and hitbox review.
- Idle / locomotion / attack transition and particle playback check.
- Ground-slam and void-pulse damage range / cooldown test.
- Loot, multiplayer and dedicated-server tests.

Passing JSON, reference and ZIP checks does not prove engine compatibility, balance or visual correctness. Do not call this release fully game-tested until the in-game checklist passes.

## GitHub Actions
The build workflow was committed, but its first run failed before a hosted runner started and exposed no step logs. The packages were therefore assembled directly from the repository content and committed as downloadable files; the automatic workflow remains to be diagnosed.
