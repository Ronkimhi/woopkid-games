# 09 - Tech Architecture

How WoopBeasts fits the WoopKid single-file standard, plus the engineering restatement of the AI contract.

## Envelope

- One file: `games/woop-beasts/index.html`. Estimated **140-170 KB** (merge-squad, the current ceiling, is 116 KB; we add the Woopdex, fusion math, parts library, and generator tables).
- Canvas 2D (`{alpha:false}`), vanilla JS, no build step, no dependencies except Google Fonts (Nunito 700/800 async + fallback).
- Standard loop: `requestAnimationFrame`, dt clamped to 50 ms, update/render split.

## Module breakdown (sections within the single file)

| Module | Responsibility | Reuse from |
|---|---|---|
| `Boot/Resize` | canvas, DPR cap 2, orientation relayout | merge-squad verbatim |
| `SaveGame` | state schema below, auto-save, migration | pets-clicker pattern |
| `Rng` | mulberry32 seeded PRNG (specs & opponent gen) | new, ~10 lines |
| `Species` | 24 starter species table + element chart + abilities | data from `10` |
| `CreatureFactory` | `drawCreature`, `buildPrompt`, `requestArt`, `getArt`, art cache | **the seam** (`06`) |
| `FusionEngine` | stat/type/lineage math, species-pair keys, unfuse | formulas in `04` |
| `MergeEngine` | trio detection, merge-3/5, chains | merge-drop's mergeQ pattern |
| `BattleSim` | tick sim, targeting, damage, abilities, opponent gen | merge-squad auto-battle, extended |
| `Screens` | Ranch/Hatchery/Lab/Squad/Battle/Results state machine | merge-drop's State enum pattern |
| `Fx` | pooled particles, floats, shake, reveal sequences | shared pool, all games |
| `Sfx` | procedural Web Audio, element-flavored waveforms | pets-clicker `note()` extended |
| `Dex` | Woopdex data + portrait cache (offscreen canvas) | new |
| `ProfileBridge` | `WoopProfile.reportRun('woop-beasts', dexCount, {bronze:10, silver:30, gold:75})` | standard |

## localStorage schema

Key `woopkid_woop-beasts`:

```js
{
  v: 1,                              // schema version for migrations
  woops: 0, cores: 0,
  eggsBought: 0,                     // drives eggCost(n)
  rung: 1, bossesBeaten: 0,
  ranch: [ CreatureSpec, ... ],      // ≤ 20 live beasts (full specs)
  squad: ['b_000012', ...],          // 4 ids into ranch
  dex: {                             // permanent, unbounded
    'fx_emberling__tidepup': {
      name: 'Embertide', firstMade: 1751812200000,
      bestStats: {...}, lineageNames: ['Emberling','Tidepup'], count: 3
    }, ...
  },
  nextId: 43,
  unlockedEggs: ['basic','ember'],
  settings: { muted: false, speed2x: false, reducedFx: false, aiArt: true },
  lastSeen: 1751812200000            // idle income
}
```

Size guardrail: 200 dex entries + 20 full specs ≈ 60-80 KB JSON - comfortably inside localStorage. **AI images do NOT go in localStorage**; they go in IndexedDB (`woopbeasts-art` object store, keyed by art cacheKey) - resolves README open question #3: **IndexedDB, decided.**

## Performance budget (60 FPS mid-range Android)

- Ranch: 20 idle-animated sprites = 20 parametric draws/frame; each ≤ 30 canvas ops → well under 8 ms render. Portraits (dex, shelves) pre-rendered to offscreen canvases and blitted.
- Battle: max 8 sprites + pooled FX (100 particles, 20 floats, pre-allocated - standard). One ability animation at a time (queued) caps worst-case.
- All coords `| 0` before draw; batch by fillStyle; no shadows/filters/complex gradients (standard).
- Audio: ≤ 6 simultaneous voices, shared AudioContext unlocked on first interaction.

## The CreatureFactory seam - engineering restatement

The game calls exactly four functions (`drawCreature`, `getArt`, `requestArt`, `buildPrompt`); §2 of `06` is the authoritative signature list. Ship order:

1. **v1 (now):** `drawCreature` fully implemented; `getArt` returns null always; `requestArt` is a no-op returning `{ok:false}`. Game is 100% offline, standards-pure. Zero external requests.
2. **v2 (when the AI service exists):** `requestArt` POSTs `{spec, prompt}` to the service; response image → IndexedDB; `getArt` does the cache lookup. Fired ONLY on discovery moments (new species, T3+ tier-up) and only when `settings.aiArt && navigator.onLine`. Every failure path degrades silently to procedural.

**AI service requirements (the contract for "the other AI"):**
- `POST /generate` body: `{ spec: CreatureSpec, prompt: string }` → `200 {image: <bytes/url>, cacheKey}` in <4s p95.
- Style-locked to the WoopKid look (prompt clause in `06` §4; recommend a reference-image/LoRA lock server-side).
- Server-side kid-safety filter; the client trusts only filtered output.
- Idempotent per cacheKey (`hash(species+tier+palette+traits)`) - same key must return the same image.
- No PII: the spec contains nothing about the child. Names are the only free text; strip/never log them if not needed.

## Hub registration (documented, not performed now)

At ship time, three touchpoints:
1. Root `index.html` `GAMES` array: `{ slug:'woop-beasts', name:'WoopBeasts', genre:'Creature Fusion Battler', cat:['action','chill'], acc:'#B388FF', emoji:'🐲', desc:'Hatch, fuse and merge beasts nobody has ever seen, then battle!', live:true, bestLabel:'Beasts' }`
2. `games.json`: matching entry.
3. Standard per-game SEO block (title, meta, JSON-LD VideoGame, OG tags) inside the game file.

## Ship checklist deltas

Everything in `docs/game-design/00-cross-game-standards.md` applies unchanged. Additional WoopBeasts-specific checks:
- [ ] Save survives schema migration (`v` field respected)
- [ ] 20-beast Ranch + battle at 60 FPS on Galaxy A-series
- [ ] Deterministic rendering: same spec pixel-identical across reloads
- [ ] With network blocked, v2 build behaves exactly like v1 (no spinners, no errors)
- [ ] First-session script (`02`) completes in <3 min with a stopwatch
