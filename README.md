# VOID TITANS — Minecraft Bedrock Add-on

An original dark-fantasy boss expansion for Minecraft Bedrock Edition.

## Current target
- Target: Minecraft Bedrock 26.66; pack engine baseline 1.26.0.
- Architecture: linked Behavior Pack + Resource Pack.
- Namespace: `voidtitans`.
- First boss: **The Void Titan** (`voidtitans:void_titan`).

## Current prototype features
- Articulated custom humanoid geometry and first-pass texture.
- Idle and walking animation sources.
- Boss health bar, hostile player targeting, melee damage and loot table.
- Additive purple core aura particle attached to a geometry locator.
- Spawn egg definition and English/Spanish entity names.

## Import
Open `VOID-TITANS-BEDROCK.mcaddon` with Minecraft Bedrock. Activate the Behavior and Resource packs in a test world. To summon the boss, use:

```mcfunction
/summon voidtitans:void_titan
```

## Important status note
This is a development prototype, not a finished/game-tested release. JSON syntax, pack linking, reference paths and archive integrity have been checked. It still needs import and in-game testing in the target Bedrock build. The model, texture, combat choreography, phases, attack effects and sounds are planned for further iterations.
