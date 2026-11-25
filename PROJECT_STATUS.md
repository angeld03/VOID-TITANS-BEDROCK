# VOID TITANS — Project status

_Last updated: 2026-11-25_

## Target
Minecraft Bedrock 26.66 (pack engine baseline 1.26.0).

## M0 — Pack foundation
- [x] GitHub source repository connected and writable.
- [x] Behavior Pack and Resource Pack manifests linked by UUID.
- [x] Custom boss entity, spawn egg and summon identifier.
- [x] Articulated custom model with horns, shoulder armor, claws, chest runes, back spines and orbiting shards.
- [x] Custom entity texture and pack icons.
- [x] Idle and locomotion animations.
- [x] Ground-slam and void-pulse attack animations connected to entity variants.
- [x] Boss HUD, hostile player targeting, melee damage and loot table.
- [x] Timed special-attack cycle with wind-up, impact and recovery windows.
- [x] Violet core aura and radial impact particle effect.
- [x] English and Spanish boss / spawn egg names.
- [x] Repeatable local build and structural validation script.
- [x] GitHub Actions workflow configured to package and publish the add-on automatically.
- [ ] Import into Minecraft Bedrock 26.66 and confirm both packs load.
- [ ] In-game model, particle, animation and combat validation.
- [ ] Dedicated-server / multiplayer test.

## M1 — The Void Titan polish
- [ ] Final texture paint pass and UV review in-game.
- [ ] Add sound design and layered audio cues.
- [ ] Add health-threshold phase transition and phase-two attack set.
- [ ] Add unique summon item / ritual and arena encounter.
- [ ] Balance damage against armor and multiplayer groups.
- [ ] Survival and dedicated-server tests.

## M2 — Additional Titans
- [ ] Abyssal King.
- [ ] Celestial Devourer.
- [ ] Shared progression and unique drops.

## Verification caveat
The source is structured and the automated validator checks JSON syntax, UUID linkage, entity/model/animation/particle references, geometry bone parents, required assets and archive integrity. A passing build does not replace importing and testing the add-on inside Minecraft Bedrock.
