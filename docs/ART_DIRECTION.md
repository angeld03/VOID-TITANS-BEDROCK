# Art direction — The Void Titan

## Silhouette
A towering humanoid colossus built from overlapping obsidian armor plates and fractured organic forms. Avoid a loose pile of disconnected cubes: armor, torso, limbs and spikes should read as one cohesive creature.

## Palette
- Near-black obsidian: #100D1C
- Deep violet: #291044
- Arcane purple: #7D36D6
- Hot amethyst: #C36BFF
- Core highlight: #F1C8FF

## Signature features
- Oversized shoulders and long forearms.
- A visible energy core recessed into the chest.
- Crown-like horns and a jagged spine silhouette.
- Thin glowing cracks painted into the texture.
- Purple emissive-looking details; emissive material setup will be implemented and tested separately.

## Animation language
- Idle: restrained weight shift and low-frequency energy pulse.
- Walk: heavy alternating leg and arm movement.
- Slam: wind-up, impact pose, recovery.
- Phase transition: core intensifies, armor cracks brighten, attack cadence increases.

## Technical art constraints
- Keep bone names stable once animations depend on them.
- Keep the model centered around X/Z = 0 and its feet close to Y = 0.
- Texture atlas target: 128x128 for the first pass; increase only when detail requires it.
- Check visible bounds and collision dimensions in-game. Geometry bounds are not proof of accurate collision.
