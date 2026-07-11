# Nom Nom City — Design Spec (2026-07-11)

## Concept

Hole.io formula, WoopKid-ified. The player drags a cute hungry hole (with googly eyes) around a bright toy town. Anything smaller than the hole tips in and falls with a satisfying spin-and-shrink. Every bite makes the hole bigger, unlocking bigger prey: candy → cones → cars → trees → houses → the ferris wheel. Timed 2-minute run; eat the whole town for a CLEARED celebration.

Chosen because it is the only top-10 viral mechanic (Hole.io, ~500M installs class) not yet covered by the 20-game catalog, it is a pure kid power fantasy, and it satisfies the radical-simplicity rule: one screen, one gesture, no instructions.

Alternatives considered and rejected: Doodle Jump vertical jumper (feel overlaps wing-it / tap-rush), Helix Jump (feel overlaps speed-slope / sky-stack).

## Core loop

1. Drag anywhere = hole moves (relative steering so the finger never covers the hole). Mouse drag and arrows/WASD on desktop.
2. Object edible when its footprint radius ≤ ~90% of hole radius. Edible objects near the rim get pulled, tilt, fall in: pull to center + spin + shrink + pop sound + score float.
3. Hole radius grows with area eaten (sqrt curve, capped). Bigger hole = bigger prey = bigger points.
4. Combo: eats within 1.2s chain a multiplier (up to x5), rising-pitch pops.
5. Run ends at 2:00 or when the town is 100% eaten (big bonus + confetti).

## Content

~220 objects in 6 size tiers laid out on a generated toy town (road grid, blocks with buildings, props): candy/flowers/cones (1pt) → bushes/mailboxes (3) → cars/benches/trees (8) → trucks/kiosks (20) → houses (50) → tower/ferris wheel (150).

## Compliance

Follows docs/game-design/00-cross-game-standards.md: single index.html, vanilla JS, canvas 2D (alpha:false, DPR≤2), dt-clamped rAF loop, state machine, procedural Web Audio, localStorage `woopkid_nomnomcity` (high score, best bite, mute), Nunito, back/pause/mute buttons, game over with NEW BEST + instant restart, JSON-LD VideoGame + FAQ schema.

Registration: games.json, homepage (ItemList, static link, GAMES array with isNew), sitemap.xml, llms.txt, llms-full.txt.

## Perf notes

Ground (grass/roads/sidewalks) pre-rendered once to an offscreen canvas; per-frame draws only objects in view + hole + particles (pooled, cap 120). No shadowBlur/filter in loop.
