# 03 - Creation & Growth

How beasts enter the game and how they get stronger *without* fusing/merging (those are `04`).

## Obtaining beasts

Three faucets, all earned in-game (no purchases, ever):

| Faucet | What you get | Pacing |
|---|---|---|
| **Eggs (main)** | Random T1 beast of the egg's element | Buy with Woops in the Hatchery; costs scale (see `07`). Battle victories also drop eggs (~35% of wins) |
| **Starter** | Guaranteed first beast, scripted hatch | Once, first session |
| **Rare battle drops** | Wild beast "joins you" after certain ladder milestones | Every 10th ladder rung - a guaranteed exciting drop |

**Egg types:** Basic Egg (any element, common species) unlocked from start; **element eggs** (guaranteed element, wider species pool) unlock along the battle ladder - the unlock ladder is the long-term carrot (`07`).

**Hatching interaction:** eggs must be *tapped* to crack (3 taps: crack → crack → POP). Never auto-hatch - the taps are the anticipation ritual, with rising pitch per tap and shell particles. Duplicates are good, not disappointing: duplicates feed merges, and the game says so ("2/3 for a merge!").

## The stat model

Five stats + element(s). Chosen so every stat is *visible in battle* - kids learn what stats do by watching, not reading.

| Stat | Range | What the kid SEES it do |
|---|---|---|
| **HP** | 1-999 | Length of the health bar |
| **ATK** | 1-999 | Size of damage numbers |
| **DEF** | 1-999 | "shrinks enemy numbers" - blocked-hit shield flash |
| **SPD** | 1-999 | How often the beast attacks (attack interval, `05`) |
| **SPC** | 1-999 | How fast the ability meter charges (`05`) |

**Elements:** 1 element for hatched beasts; fusions can hold 2 (see `04`). Full chart in `05`/`10`.

### Base stats at hatch

Each species has a base statline (T1 totals ≈ 150-210, defined per species in `10-content-starter-set.md`) with a personality skew - e.g. Emberling is ATK-heavy, Tidepup is HP-heavy. On hatch, each stat gets ±10% seeded jitter so two Emberlings are near-identical but not identical:

```
statAtHatch = round(base · (0.90 + 0.20 · rand(seed)))
```

The `seed` is stored on the CreatureSpec and also drives visual variation (`06`) - stats sculpt the body: a high-HP Emberling has a broader frame, a high-ATK one is visibly more muscular. Stats and looks agree.

## Leveling (XP)

**Earning XP:** every beast that participates in a battle earns XP (win: `25 + 5·rung`; loss: `10 + 2·rung`). Feeding also grants XP: any beast can be fed a **Snack** (minor Woops sink, `07`) for +15 XP - gives the "make my guy stronger NOW" button kids want.

**Curve:** XP to go from level L to L+1:

```
xpNext(L) = round(20 · L^1.5)
```

L1→2 = 20, L2→3 = 57, L5→6 = 224, L9→10 = 540. Early levels pop constantly (dopamine), later levels are real goals. **Level cap = 10 per tier** - the cap is the nudge toward merging/fusing: "Emberling is maxed! Merge 3 to evolve → Emberkid."

**Per level:** all five stats ×1.04 (compounding; L10 ≈ ×1.42 over L1). Level-up moment: beast squashes, stretches, flexes; "+LVL 6!" floats; ascending procedural arpeggio.

## Tiers (preview - mechanics in `04`)

| Tier | Name | Stat scale vs T1 | Visual (vocabulary in `06`) |
|---|---|---|---|
| T1 | Baby | ×1 | Rookie build, basic widget kit |
| T2 | Kid | ×1.8 | +10% scale, +1 extra widget |
| T3 | Hero | ×3.24 | Aura ring, power seams ignite |
| T4 | Mega | ×5.83 | Particle trail, second back widget |
| T5 | Mythic | ×10.5 | Full animated aura, floating tech rings, energy cape |

## Capacity

The Ranch holds **20 beasts** (grid slots). At capacity, hatching is blocked with a friendly prompt: "Ranch full! Merge or fuse to make room." - capacity pressure is a *design feature* that pushes players into the fun verbs instead of hoarding. The Woopdex (records, not live beasts) is unlimited.

## Anti-frustration rules

- No beast can die or be lost involuntarily. Battles KO, never kill.
- Releasing a beast (rare need) refunds Woops and keeps its Woopdex entry.
- Duplicates are always framed as merge progress, never "dupes."
- A new player's first 4 eggs are rigged (starter + 3 that guarantee one merge trio) - see first-session script in `02`.
