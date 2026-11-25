# VOID TITANS — Minecraft Bedrock Add-on

An original dark-fantasy boss add-on for Minecraft Bedrock Edition.

## Target
- Target release: Minecraft Bedrock 26.66 (November 2026).
- Pack engine baseline: 1.26.0.
- Architecture: linked Behavior Pack + Resource Pack.
- Namespace: voidtitans.
- First boss: **The Void Titan** (voidtitans:void_titan).

## Current feature set
- Custom articulated humanoid geometry with horns, layered shoulders, claws, chest runes, back spines and orbiting void shards.
- Custom 128×128 entity texture and violet additive particles.
- Idle, locomotion, ground-slam wind-up/impact and void-pulse charge/burst animations.
- Boss health bar and darkened-sky encounter.
- 850 HP, hostile player targeting, heavy melee attacks and knockback resistance.
- Automatic special-attack cycle: a telegraphed ground slam or a larger-radius void pulse.
- Custom loot table and spawn egg localization in English and Spanish.

## Install
1. Download VOID-TITANS-BEDROCK.mcaddon from the latest GitHub Release.
2. Open the file with Minecraft Bedrock to import both packs.
3. Create or edit a world and activate **VOID TITANS — Behavior** and **VOID TITANS — Resources**.
4. Enable cheats for the test world and summon the boss with:

    /summon voidtitans:void_titan

The spawn egg is also available in the creative inventory after enabling the add-on.

## Direct download
- [Latest combined .mcaddon](https://github.com/angeld03/VOID-TITANS-BEDROCK/releases/latest/download/VOID-TITANS-BEDROCK.mcaddon)
- [Behavior Pack .mcpack](https://github.com/angeld03/VOID-TITANS-BEDROCK/releases/latest/download/VOID-TITANS-Behavior.mcpack)
- [Resource Pack .mcpack](https://github.com/angeld03/VOID-TITANS-BEDROCK/releases/latest/download/VOID-TITANS-Resources.mcpack)

## Build from source
With Python 3.10+ installed:

    python tools/build.py

The script validates JSON, manifests, references, model bone parents and PNG headers, then creates the combined .mcaddon and the individual .mcpack files in dist/.

GitHub Actions runs this build on every push to main, uploads a workflow artifact and publishes the three packages as the latest GitHub Release.

## Verification status
Automated structural validation and archive integrity checks are performed by the build script. **The add-on still requires an in-game import and gameplay test on Bedrock 26.66** before it can be called fully game-tested.
