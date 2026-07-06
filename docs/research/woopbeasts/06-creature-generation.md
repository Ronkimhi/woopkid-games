# 06 - Creature Generation (the CreatureFactory seam)

**This is the key doc.** Every creature visual in the game (Ranch sprites, fusion previews, battle combatants, Woopdex portraits) is produced through ONE interface. The shipped game implements it procedurally (offline, instant, free). The future AI image engine implements the *same* interface later, without touching game logic. WoopKid's "zero external requests" standard stays intact because the AI backend is an optional online enhancement with a guaranteed procedural fallback.

## Art direction (revamped 2026-07-06): HERO PHYSIQUE + FUTURE TECH

Beasts are not cute blobs. They are **chunky cartoon powerhouses**: broad shoulders, flexed biceps, planted stances, plus **future body widgets** (energy cores, mech arms, jetpacks, visors, tesla coils). Think Saturday-morning superhero meets friendly robot lab. Still WoopKid: rounded shapes, thick dark-navy ink outlines, flat bright colors, big expressive eyes, zero scary content. The power fantasy is the point: a kid's beast should LOOK like it can win, and every stat gain should be visible on the body.

---

## 1. CreatureSpec - the single source of truth

A creature IS its spec. Game logic, the procedural renderer, and the AI backend all consume this one object:

```js
{
  id: 'b_000042',              // unique instance id
  name: 'Embertide',           // player-given (fusions) or species default
  species: 'emberling',        // species key; fusions: 'fx_emberling__tidepup' (ordered head__body)
  elements: ['ember','tide'],  // 1-2, primary first
  tier: 2,                     // 1-5
  level: 6,
  xp: 143,
  stats: { hp: 145, atk: 92, def: 61, spd: 74, spc: 58 },
  physique: 'tank',            // 'tank' | 'sprinter' | 'bruiser' (silhouette family, below)
  traits: ['horn_crest','core_reactor','mech_arm'],   // visual trait tags (vocabulary below)
  palette: ['#FF5757','#4CC9F0','#FFD93D'],           // primary / secondary / glow-accent
  seed: 812395,                // deterministic; drives ALL visual variation
  lineage: { head: 'b_000012', body: 'b_000031', gen: 1 },  // null head/body for hatched (gen 0)
  discovered: 1751812200000,   // first-created timestamp for Woopdex
  art: {
    mode: 'proc',              // 'proc' | 'ai'
    cacheKey: null,            // set when an AI image exists in the art cache
    prompt: null               // the generated prompt string (kept for regeneration/debug)
  }
}
```

Rules:
- **Determinism:** `(species, tier, physique, traits, palette, seed)` fully determine the procedural drawing. Same spec → same creature, every device, every session. No `Math.random()` at render time; a seeded PRNG (mulberry32) only.
- Stats sculpt the body (below), so the spec must be complete before first render.
- The spec is what's saved in localStorage; art is derived (proc) or cached (ai), never authoritative.

## 2. The interface

```js
const CreatureFactory = {
  // Synchronous, always works, always instant. THE game's renderer.
  drawCreature(ctx, spec, x, y, size, pose),   // pose: 'idle'|'attack'|'hurt'|'flex'|'portrait'

  // Asynchronous, optional, may fail/never resolve. The upgrade path.
  async requestArt(spec),      // → { ok, cacheKey } ; stores image in art cache
  getArt(spec),                // → ImageBitmap | null  (cache lookup, sync)

  buildPrompt(spec)            // → string (the AI prompt; §4)
}
```

Render rule everywhere in the game: `getArt(spec)` non-null → draw the cached AI image (with procedural FX layered on top: aura, particles, squash-stretch still apply); otherwise → `drawCreature(...)`. That's the entire integration; battle, ranch, and dex code never know which backend produced the pixels.

## 3. Procedural backend (ships with the game)

Assembled in layers, drawn as canvas paths: chunky, rounded, thick ink outlines `#2B2350`, WoopKid cartoon style, and now with real anatomy plus tech widgets.

### Layer stack (back to front)

1. **Back widget** (jetpack, wings, cannon barrels)
2. **Legs** (muscular thighs + boots/hover units)
3. **Torso** (physique-shaped, pecs and ab lines)
4. **Arms** (shoulder caps, flexed biceps, forearms, fists; mech arm replaces one side when the trait is present)
5. **Chest widget** (energy core, armor plates)
6. **Head** (per species: shape, eyes, brow, headgear)
7. **FX layer** (tier aura, glow seams, thruster flames)

### Physique families (the silhouette)

| Physique | Silhouette | Stat identity |
|---|---|---|
| `tank` | Massive torso, short thick legs, small head, shoulders 2.2× waist | HP/DEF species |
| `sprinter` | Lean V-taper, long legs, forward lean, thruster boots read natural | SPD species |
| `bruiser` | Gorilla frame: giant arms and fists, knuckle-forward stance | ATK species |

Every species belongs to one family; fusions inherit the **body parent's** physique.

### Trait vocabulary (slots × options)

| Slot | Options (initial library) |
|---|---|
| Headgear | `horn_crest`, `visor` (cyber eye band), `antenna_array`, `ears_tall`, `mohawk_fin`, *(none)* |
| Eyes | `hero_eyes`, `cyber_eye` (one glowing lens), `star_eyes`, `angry_brow`, `cool_shades` |
| Chest widget | `core_reactor` (glowing energy core), `armor_plate` (chest plate + rivets), `power_seams` (glow lines), *(none)* |
| Back widget | `jetpack`, `shoulder_cannon`, `holo_wings` (translucent energy wings), `spine_fins`, *(none)* |
| Arm widget | `mech_arm` (one robotic arm), `power_fists` (oversized glowing fists), `arm_blades`, *(none)* |
| Legs/boots | `hover_boots` (thruster flames), `power_boots` (armored), `raptor_legs` (digitigrade) |
| Tail | `plasma_tail`, `cable_tail` (segmented tech), `blade_tail`, `stub_tail`, *(none)* |
| Skin FX | `plain`, `circuit_lines`, `battle_stripes`, `crystal_studs` |

3 physiques × 6×5×4×5×4×3×5×4 trait combos = **432,000 silhouette combos** before palette, stat sculpting, and seed jitter. Visual variety is effectively infinite at kid-perception level.

### How the spec maps to the drawing (stats sculpt the body)

- **Species** fixes physique + a hand-picked trait set + palette (per species in `10`).
- **Fusion traits:** head-slots (headgear, eyes) from the head parent; body-slots (physique, chest/back/arm widgets, legs, tail, skin) from the body parent; palette = head primary + body primary + blended glow accent. Fusions *visibly* read as their parents, which is what makes the reveal legible.
- **Stats sculpt anatomy (the revamp's core rule):**
  - **ATK → muscle mass:** bicep radius, pec size, fist scale all lerp with ATK percentile. A maxed-ATK beast is visibly JACKED.
  - **HP → frame:** torso width and leg thickness.
  - **DEF → armor coverage:** armor plates grow and multiply (chest → shoulders → shins) as DEF climbs.
  - **SPD → stance and thrusters:** leg length, forward lean, and hover/thruster flame length.
  - **SPC → glow:** energy core radius, seam brightness, eye-lens glow.
- **Tier escalation:** T2 +10% scale +1 extra widget; T3 aura ring + power seams ignite; T4 particle trail + second back widget; T5 full animated aura, floating tech rings, cape-like energy field.
- **Seed jitter:** ±6% on every proportion via the seeded PRNG; no two instances identical.

Animation: no sprite sheets. Poses are parametric (idle = breathing chest + blink; **flex** = both arms up, biceps pop, used on level-up and victory; attack = lunge with `easeOutBack`; hurt = squash + 60ms white flash). Cheap, smooth, consistent across all combos. Portraits render once to an offscreen canvas and are reused.

## 4. AI backend (the "other AI" - contract)

**Input:** a CreatureSpec. **Output:** one square image (512×512 PNG/WebP, transparent background) that respects the spec.

`buildPrompt(spec)` produces a deterministic prompt so regeneration is stable:

```
"kids cartoon monster hero, chunky rounded shapes, thick dark-navy outlines,
 flat bright colors {palette}, {physique: 'massive tank build'|'lean sprinter build'|'gorilla bruiser build'},
 muscular arms and chest scaled to {ATK percentile}, {headgear}, {eyes},
 futuristic body widgets: {chest widget}, {back widget}, {arm widget}, {boots}, {tail},
 elements: {elements → 'flames' | 'water energy' | 'vines' | 'lightning' | ...},
 tier {tier} ({'rookie'|'kid'|'hero'|'mega'|'mythic'} size and grandeur, aura per tier),
 single creature, centered, heroic stance, transparent background, no text,
 style: friendly superhero-robot, ages 6-11, never scary, WoopKid palette cream/navy/orange"
```

Contract requirements for the AI service (build later):
1. **Style-locked:** every output must sit next to procedural art without clashing (the style clause above is non-negotiable; consider a LoRA/reference-image lock).
2. **Deterministic-ish:** same spec returns the cached image, not a new roll; the cache is the source of stability. Regeneration only on explicit "re-imagine" action.
3. **Kid-safe:** output must pass a safety filter server-side; muscles and tech read heroic, never grotesque or weaponized-realistic. The game never displays an uncached AI image without the filter.
4. **Fast or invisible:** target <4s; the game NEVER waits. Procedural art shows instantly and the AI portrait "develops" in when ready (Polaroid-style develop animation makes the swap a reward, not a glitch).
5. **Cheap:** generation fires only on *discovery* moments (new species, tier-up to T3+), not per-instance. Estimated calls per active player-day: 5-15.

### Caching & offline behavior

- Art cache in **IndexedDB** (`woopbeasts-art` store; localStorage's ~5MB quota is too small for images). Key = `hash(species + tier + palette + traits)`, shared across instances of the same species/tier, which massively cuts generation volume.
- On any failure (offline, quota, timeout, filter rejection): silently stay procedural. There is no error state visible to a kid, ever.
- A settings toggle ("magic pictures: on/off") lets parents disable network art entirely → the game is then 100% offline, standards-pure.

## 5. Why the seam is the product

- **Ships now:** the procedural backend alone is a complete, delightful game (432k combos, stat-sculpted muscle, tier-escalating tech).
- **Upgrades later:** the AI backend turns "new species discovered" into "an image no one has ever seen, made for you", which is Infinite Craft's proven magic applied to creatures.
- **Defines the AI project:** this doc IS the requirements spec for the future AI service: accept a CreatureSpec, honor the prompt contract, return a style-locked safe image, and let the cache do the rest.
