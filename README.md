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

## Download and install
- [Combined installer — VOID-TITANS-BEDROCK.mcaddon](https://raw.githubusercontent.com/angeld03/VOID-TITANS-BEDROCK/main/downloads/VOID-TITANS-BEDROCK.mcaddon)
- [Behavior Pack — VOID-TITANS-Behavior.mcpack](https://raw.githubusercontent.com/angeld03/VOID-TITANS-BEDROCK/main/downloads/VOID-TITANS-Behavior.mcpack)
- [Resource Pack — VOID-TITANS-Resources.mcpack](https://raw.githubusercontent.com/angeld03/VOID-TITANS-BEDROCK/main/downloads/VOID-TITANS-Resources.mcpack)

For the easiest install, download the combined .mcaddon and open it with Minecraft Bedrock. Then activate both VOID TITANS packs in the world settings. Enable cheats for the test world and summon the boss with:

    /summon voidtitans:void_titan

The spawn egg should also appear in the Creative inventory after enabling the add-on.

## Build from source
With Python 3.10+ installed:

    python tools/build.py

The script validates JSON, manifests, references, model bone parents and PNG headers, then creates the combined .mcaddon and individual .mcpack files in dist/.

A GitHub Actions workflow is configured to run this build on pushes to main. At the moment the first workflow run ended before its runner started, so prebuilt packages are also committed in downloads/ as direct downloads.

## Verification status
The downloadable archives are ZIP-integrity checked and contain both packs. The add-on still requires an in-game import and gameplay test on Bedrock 26.66 before it can be called fully game-tested.
