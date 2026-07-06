# 08 - UX: Full-Screen, Mobile-First

Primary target: a kid holding a phone/tablet in **portrait**. Landscape supported (battle looks great wide); portrait is the design driver. Full-bleed canvas, no browser chrome assumptions, `100dvh`, safe-area insets respected.

## Screen map

```
            ┌─────────────┐
   ┌───────►│    RANCH    │◄───────┐          RANCH = home. Everything is
   │        │  (home/hub) │        │          one tap from the Ranch.
   │        └──┬───┬───┬──┘        │
   ▼           ▼   ▼   ▼           ▼
 HATCHERY   FUSION  SQUAD ►────► BATTLE ──► RESULTS ─┐
 (eggs)      LAB    PICK         (fight)     (loot)  │
   ▲           │                                     │
   │           ▼                                     │
   └──────  WOOPDEX (collection, from top bar) ◄─────┘
```

Five real screens + a results overlay. No nested menus - every screen is one tap from the Ranch, and the top bar is persistent everywhere.

## Persistent top bar (all screens)

`[← back] [🪙 Woops] [🥚 eggs] [💠 cores] [📖 Woopdex 47]` - Woopdex count is the one big number, always on. On the Ranch, ← goes to `../../index.html` (hub); elsewhere it goes to the Ranch.

## Screen by screen

### RANCH (home)
- 4×5 grid of beast slots (20 capacity), big idle-animated sprites, name chips under each.
- **Drag to merge** right here (ready trios glow). Long-press a beast → detail card (stats, level, feed Snack, unfuse if fusion, release).
- Bottom dock, three fat buttons: `🥚 HATCHERY` `🧪 FUSION LAB` `⚔️ FIGHT`. The "one glowing thing" rule lives here: exactly one of dock/eggs/trios pulses at any moment (priority: ready merge > affordable egg > fightable battle).

### HATCHERY
- Horizontal shelf of egg types (locked ones as silhouettes + unlock hint), price tags in Woops.
- Bought eggs drop to the nest area; tap-tap-tap to hatch. Hatched beast bounces to the Ranch (auto-placed).

### FUSION LAB
- Two pods stacked vertically: **HEAD** (top) and **BODY** (bottom); beast picker shelf slides up from the bottom (thumb reach).
- Center: live preview silhouette + element badges + 5 stat bars that slide when arrangement changes. `⇅ SWAP` between pods.
- Giant `FUSE 💠1` button. Reveal sequence plays fullscreen. Naming ceremony: 3 suggestion chips + "type my own."

### SQUAD PICK (pre-battle)
- Your 4 squad slots + Ranch shelf; drag or tap to fill. "POW!" ⚡ badge shows on beasts that counter the upcoming enemy squad (enemy preview shown as silhouettes + element badges - informed picks without spoiling).
- One glowing `FIGHT` button. Remembers last squad → repeat fights are two taps total.

### BATTLE (the full-screen showpiece)
- Landscape-feel even in portrait: arena spans the full screen, player squad bottom-left arc, enemies top-right arc, big sprites (≥18% of screen height each).
- Chunky HP bars, ability meters as thin rings around each beast. Damage floats. 1×/2× speed toggle top-right. Optional tap-to-cheer (never required).

### RESULTS (overlay)
- Coin fountain onto the counter, egg/core drops slide into the top bar, XP bars fill per beast, sticker/unlock banners, then two buttons: `NEXT BATTLE ▶` (glowing) and `RANCH`.

## Touch standards

- Min tap target **64×64 px** (kids miss more than adults); dock buttons ~96 px.
- Drag threshold 8 px (below = tap); everything draggable is also tappable-to-select-then-tap-destination (fine-motor fallback for youngest players).
- No gesture requirements beyond tap and drag. No pinch, no swipe-to-navigate, no double-tap.
- Pointer events (`pointerdown/move/up`) exactly as merge-squad does; mouse + keyboard work on desktop (arrows + Enter navigate; Space = primary action) per cross-game standards.

## Full-screen behavior

- `100dvh` canvas, `DPR` capped at 2, resize handler identical to merge-squad's.
- Optional Fullscreen API button (📺) on the Ranch - nice on Android; iOS Safari fallback is simply the clean no-chrome layout (never rely on the API).
- Orientation: portrait = default layouts above; landscape = Ranch grid goes 5×4, battle spreads wider, Fusion Lab pods go side-by-side. Same components, two anchor layouts, no separate builds.

## Reading level & iconography

- A pre-reader must be able to play: every action has an icon; text is reinforcement, not requirement. Numbers, bars, glows, and color carry all decisions.
- All copy ≤ 5 words, Nunito 800, high contrast on cream (`#2B2350` on `#FFF6E9`).

## Accessibility & comfort

- `prefers-reduced-motion`: disables screen shake and particle bursts (kept: color flashes ≤ 60ms are already banned site-wide; slow fades only).
- Mute toggle persisted (standard); separate music/SFX not needed (no music at v1 - battles carry their own rhythm; revisit later).
- Color-blind safety: elements are never color-only - each has a fixed icon (🔥🌊🌿⚡❄️🪨🌑✨) shown beside every color use.
- Battle 2× speed doubles as a patience accommodation.

## Failure/empty states (all friendly)

- Ranch full → "Ranch full! Merge or fuse to make room" + the Lab button pulses.
- Can't afford egg → price tag wiggles, FIGHT button pulses ("go earn").
- No core → Lab shows "Win battles to find Fusion Cores 💠" + FIGHT pulses.
- Never a dead-end screen: every blocked action points at the action that unblocks it.
