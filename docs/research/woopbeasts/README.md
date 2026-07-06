# WoopBeasts - Design & Research Set

**Status:** Design complete, not built. Created 2026-07-06.
**Working title:** WoopBeasts (final name TBD - see `00-vision.md` for options)
**Slug (reserved):** `woop-beasts`

## The pitch

A full-screen creature game where every beast you make is one of a kind. Hatch a beast, level it up, **fuse** two beasts into a brand-new creature nobody has ever seen, **merge** three of a kind to evolve them, then send your squad into auto-battles to win the stuff you need to make even weirder beasts. The Woopdex remembers every creature you ever invented. Infinite creation, infinite "one more fuse."

It is the most advanced WoopKid game to date: a persistent world you build over weeks, not a 90-second run. It is also the launch vehicle for the future **AI creature-art engine** - the whole design routes creature visuals through one pluggable interface (`CreatureSpec` → `CreatureFactory`) so the shipped game runs 100% offline with procedural art, and the AI backend can slot in later without touching game logic.

## Reading order

| File | What it covers |
|---|---|
| [00-vision.md](00-vision.md) | Concept, audience, dopamine thesis, name options, IP stance |
| [01-market-research.md](01-market-research.md) | Teardowns: Pokémon Infinite Fusion, Infinite Craft, Merge Dragons, auto-battlers |
| [02-core-loop.md](02-core-loop.md) | The loop: Hatch → Grow → Fuse/Merge → Battle → Collect. First-session script |
| [03-mechanics-creation-growth.md](03-mechanics-creation-growth.md) | Getting beasts, stats, XP, leveling |
| [04-mechanics-fusion-merge.md](04-mechanics-fusion-merge.md) | **The heart.** Fusion (2 → new species) and Merge (3 → next tier) |
| [05-mechanics-battle.md](05-mechanics-battle.md) | Full-screen auto-battler: ticks, damage, type chart, opponent AI |
| [06-creature-generation.md](06-creature-generation.md) | **Key doc.** CreatureSpec + CreatureFactory: procedural art now, AI art later |
| [07-progression-economy-retention.md](07-progression-economy-retention.md) | Economy, unlock ladder, stickers, streaks, the dopamine map |
| [08-ux-fullscreen-mobile.md](08-ux-fullscreen-mobile.md) | Screen map, wireframes, touch targets, accessibility |
| [09-tech-architecture.md](09-tech-architecture.md) | State schema, module plan, perf budget, hub registration, AI contract |
| [10-content-starter-set.md](10-content-starter-set.md) | Elements, starter roster, parts library, name generator, stickers |
| [mockup.html](mockup.html) | Clickable visual mockup: Fusion Lab + Battle screens |

## Canonical shared values (single source of truth)

Every doc uses these. If a doc contradicts this table, this table wins.

**Elements (8):** Ember 🔥, Tide 🌊, Bloom 🌿, Spark ⚡, Frost ❄️, Stone 🪨, Gloom 🌑, Gleam ✨
**Stats (5):** HP, ATK, DEF, SPD, SPC (spirit - powers abilities). Range 1-999.
**Tiers (5):** T1 Baby → T2 Kid → T3 Hero → T4 Mega → T5 Mythic
**Fusion stats:** ATK/DEF/SPD = `round(0.6·body + 0.4·head)`; HP/SPC = `round(0.6·head + 0.4·body)`; then ×1.10 fusion bonus.
**Fusion typing:** head's primary element + body's primary element (if equal, body's secondary).
**Fusion looks:** head parent gives headgear + eyes; body parent gives physique + all body widgets (see `06`).
**Art direction (2026-07-06):** hero physiques (tank / sprinter / bruiser) + future tech widgets; stats sculpt anatomy (ATK muscle, HP frame, DEF armor, SPD legs/thrusters, SPC glow).
**Merge:** 3 identical species+tier → one at next tier, stats ×1.8.
**Damage:** `dmg = max(ceil(ATK·0.08), round(ATK · typeMult · comboMult − DEF·0.5))`, typeMult ∈ {2, 1, 0.5}. Chip floor prevents tank stalls.
**Attack rate:** one attack every `2.2 − (SPD/999)·1.4` seconds.
**Ability charge:** `(4 + (SPC/999)·8)%` per second (base rate guarantees every beast fires ~once per battle).
**XP to next level:** `round(20 · L^1.5)`; each level: all stats ×1.04.
**Currencies:** Woops (coins), Eggs (new beasts), Fusion Cores (gate fusion pacing).
**Save keys:** `woopkid_woop-beasts` (game), `woopkid_profile` (shared WoopProfile).

## Open questions (decide at build time)

1. Final name: WoopBeasts vs Beast Lab vs Fusioo vs Woopimals (see `00-vision.md`).
2. Fusion Core faucet tuning - how many fuses per session feels generous but not infinite (see `07`).
3. ~~localStorage vs IndexedDB for AI art cache~~ RESOLVED: IndexedDB (`09`, 2026-07-06).
4. Portrait-only vs portrait+landscape battle layout (design covers both; portrait is primary).
5. Merge pacing: with 3+ species per egg pool, collecting 3 duplicates of one species takes ~7+ eggs (coupon-collector math). Likely fix at build: hatch odds gently biased toward species the player already owns 1-2 of ("pity weighting"), so a merge is always visibly close. Tune in playtest.

## Constraints inherited from WoopKid standards

Single self-contained HTML file; canvas 2D; vanilla JS; procedural Web Audio; localStorage; 60 FPS on mid-range Android; zero external requests except Google Fonts (the AI backend is an *optional online enhancement* behind the CreatureFactory seam); no full-screen strobe; back button → `../../index.html`. Full checklist in `docs/game-design/00-cross-game-standards.md`.
