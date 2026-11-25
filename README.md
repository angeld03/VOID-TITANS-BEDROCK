# VOID TITANS — Minecraft Bedrock Add-on

An original dark-fantasy boss expansion for Minecraft Bedrock Edition.

## Project goal
Create colossal custom 3D bosses with detailed geometry, bespoke textures, skeletal animations, phase-based combat, particles, sounds, loot and summoning items.

## Current target
- Target game: Minecraft Bedrock 26.66 (minimum engine target: 1.26.0).
- Pack architecture: Behavior Pack + Resource Pack.
- Namespace: voidtitans.
- First boss: The Void Titan.
- First summon command: /summon voidtitans:void_titan.

## Repository layout
- behavior_pack/: entity logic, AI, loot, items, functions and scripts.
- resource_pack/: entity visuals, geometry, textures, animations, particles and sounds.
- docs/: design notes, compatibility notes and testing checklist.
- tools/: local validation and packaging helpers.

## Importing (once a release package is available)
1. Download the latest .mcaddon release from GitHub Releases.
2. Open it with Minecraft.
3. Activate both VOID TITANS — Behavior and VOID TITANS — Resources in a test world.
4. Enable experimental toggles only when a release explicitly requires them.
5. Use /summon voidtitans:void_titan to summon the first boss.

## Development policy
- Keep behavior and resource packs linked by manifest UUIDs.
- Validate all JSON files before committing.
- Never mark a build as game-tested unless it has actually been imported and tested in Bedrock.
- Keep release archives reproducible from source folders.
- Never commit API keys, access tokens, private data or credentials.

See PROJECT_STATUS.md for the implementation and verification state.
