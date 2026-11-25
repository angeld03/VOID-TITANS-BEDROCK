# Art direction — The Void Titan

## Silhouette
A towering humanoid colossus built from overlapping obsidian armor plates and fractured organic forms. Armor, torso, limbs and spikes should read as one cohesive creature rather than loose disconnected cubes.

## Palette
- Near-black obsidian: `#100D1C`
- Deep violet: `#291044`
- Arcane purple: `#7D36D6`
- Hot amethyst: `#C36BFF`
- Core highlight: `#F1C8FF`

## Signature features
- Oversized shoulders and long forearms.
- Visible energy core recessed into the chest.
- Crown-like horns and jagged spine silhouette.
- Thin glowing cracks painted into the texture.
- Additive violet spark aura orbiting the chest core.

## Animation language
- Idle: restrained weight shift and low-frequency energy pulse.
- Walk: heavy alternating leg and arm movement.
- Slam: wind-up, impact pose, recovery.
- Phase transition: core intensifies, armor cracks brighten, attack cadence increases.

## Technical constraints
- Keep bone names stable once animations depend on them.
- Keep the model centered around X/Z = 0 and feet close to Y = 0.
- Texture atlas target: 128x128 for the first pass.
- Locators are specified in model space and should be checked in-game.
