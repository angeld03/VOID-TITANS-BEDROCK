# VOID TITANS — Project status

_Last updated: 2026-11-25_

## Target
Minecraft Bedrock 26.66 with `min_engine_version` 1.26.0.

## M0 — Pack foundation
- [x] GitHub source repository connected and writable.
- [x] Behavior Pack and Resource Pack manifests linked by UUID.
- [x] Custom boss entity definition and summon identifier.
- [x] Initial articulated model, idle and locomotion animation sources.
- [x] Boss HUD, player targeting, melee damage and loot table.
- [x] Initial custom texture and pack icons.
- [x] Custom additive violet particle effect, texture and chest locator.
- [x] Local `.mcaddon` and individual `.mcpack` archives generated.
- [x] Eleven JSON documents parsed and cross-pack references checked.
- [x] Three archive files passed ZIP integrity checks.
- [ ] Import into Minecraft and confirm both packs load.
- [ ] In-game model / particle / combat validation.

## M1 — The Void Titan
- [ ] Refine silhouette, UV map and texture painting.
- [ ] Add telegraphed ground slam and impact ring.
- [ ] Add void projectile / ground pulse ability.
- [ ] Add health-threshold phase transition and attack variants.
- [ ] Add custom sound design.
- [ ] Add unique summon item and improved rewards.
- [ ] Survival and multiplayer tests.

## M2 — Additional Titans
- [ ] Abyssal King.
- [ ] Celestial Devourer.
- [ ] Shared progression and unique drops.

## Verification caveat
Local structural checks have passed. The add-on has not yet been imported into or visually tested in Minecraft. GitHub Actions runs currently terminate as failures without exposing step logs through the connected API; the installable archives have therefore been built and verified locally rather than claimed as CI artifacts.
