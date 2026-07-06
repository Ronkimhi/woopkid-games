# 05 - Battle

Full-screen auto-battler. Strategy happens **before** the fight (which beasts, which fusions, which elements); the fight itself is a 20-40 second spectacle the kid watches - winnable by a 6-year-old, optimizable by an 11-year-old. Skeleton inherited from `games/merge-squad/index.html`.

## Setup

- **Squad = 4 beasts** chosen from the Ranch (squad picker remembers last squad; one tap to fight again).
- Opponent squad is procedurally generated (below). Player squad lines up on the left, opponent on the right, side-view, big sprites.
- One button: **FIGHT**. No mid-battle input required. (Optional spice: tapping your own beast during battle gives a tiny +5% attack-speed cheer for 2s, with a cooldown - keeps hands busy, never required. "Cheering" not "controlling.")

## Resolution model: real-time ticks (not turns)

Every beast attacks on its own clock, so SPD is *visible* as attack frequency:

```
attackInterval(beast) = 2.2 − (SPD / 999) · 1.4        // seconds: 2.2s slow … 0.8s fast
```

The battle sim runs on the standard delta-time loop; each beast accumulates time and fires when its interval elapses. Target selection: attack the opposing beast with the **lowest current HP** (simple, legible, creates satisfying finish-him focus).

### Damage (canonical)

```
dmg = max(ceil(ATK · 0.08), round(ATK · typeMult · comboMult − DEF · 0.5))
```

- **Chip floor `ceil(ATK · 0.08)`** (added 2026-07-06 after the mockup reproduced a tank-vs-tank stall): a high-DEF wall can slow a fight, never freeze it. Minimum damage scales with the attacker, so an ATK 30 beast still chips 3 per hit into DEF 54 instead of 1. Sudden Woop (below) stays as the hard backstop.
- `typeMult`: 2 (super effective, "POW!" callout), 1 (neutral), 0.5 (resisted, "meh" puff). For dual-element defenders, multiply the multiplier vs each element (max 4, min 0.25).
- `comboMult = 1 + 0.1 · consecutiveHitsOnSameTarget` (cap ×1.5) - rewards focus fire, makes numbers climb during the fight.
- Every hit: damage number floats (size ∝ dmg), target squashes, attacker lunges with ease-out, procedural hit SFX with element-flavored waveform (Spark = buzzy square wave, Tide = filtered noise splash, Ember = crackle).

### Element chart (canonical, full matrix)

Each element is strong vs 2 and weak vs 2. Rows attack columns; `2` = super, `.5` = resisted, blank = neutral.

| atk\def | Ember | Tide | Bloom | Spark | Frost | Stone | Gloom | Gleam |
|---|---|---|---|---|---|---|---|---|
| **Ember** | | .5 | 2 | | 2 | .5 | | |
| **Tide** | 2 | | .5 | .5 | | 2 | | |
| **Bloom** | .5 | 2 | | | .5 | 2 | | |
| **Spark** | | 2 | | | | .5 | .5 | 2 |
| **Frost** | .5 | | 2 | | | | 2 | .5 |
| **Stone** | 2 | .5 | .5 | 2 | | | | |
| **Gloom** | | | | 2 | .5 | | | 2 |
| **Gleam** | | | | .5 | 2 | | 2 | |

Design notes: the six "nature" elements form classic readable triangles (Ember>Bloom>Tide>Ember; Stone>Spark, Tide>Stone); **Gloom and Gleam are mutually super-effective** - dramatic glass-cannon matchups, and they only interact with the nature elements through Spark/Frost, making them feel exotic (they're also the last two egg unlocks).

Kid legibility: no chart to memorize in-game - pre-battle screen shows a simple "POW!" ⚡ icon next to your beasts that counter the enemy, and super-effective hits shout "POW!" in-fight. The chart is *learned by watching*.

### Abilities (SPC stat)

Each beast has one ability determined by its primary element. The ability meter fills at `(4 + (SPC/999) · 8)%` per second (base 4%/s so even low-SPC beasts fire roughly once per battle; SPC pushes it to 12%/s, about every 8s). At 100% it auto-fires with a big telegraphed animation. (Design bug fixed 2026-07-06: the earlier pure `SPC/999 · 12%` rate meant a starter with SPC 28 would need ~5 minutes to fire, so abilities would never appear in a 20-40s battle.)

| Element | Ability | Effect |
|---|---|---|
| Ember | Flame Burst | Hit ALL enemies for 0.6·ATK |
| Tide | Healing Wave | Heal lowest ally 25% max HP |
| Bloom | Vine Wrap | Slow target's attack interval +50% for 4s |
| Spark | Overcharge | Own attack interval −40% for 4s |
| Frost | Ice Block | Shield lowest ally (absorbs 0.8·SPC dmg) |
| Stone | Boulder Slam | 2.2·ATK to one target + brief stun (1.5s) |
| Gloom | Spook | Target deals −30% dmg for 4s |
| Gleam | Rally | All allies +20% ATK for 4s |

Dual-element fusions use the head's ability but charge 15% faster - one more reason fusion choice matters.

## Opponent generation (no multiplayer)

Opponent squads are generated to a **target power** so difficulty is controlled precisely:

```
playerPower = Σ squad (HP + ATK + DEF + SPD + SPC)
targetPower = playerPower · rungMult(rung)
```

- Battle ladder rungs 1-3: `rungMult` = 0.60/0.75/0.90 (tutorial-safe, effectively unlosable).
- From rung 4: `rungMult = 0.95 + 0.05·(rung−4)`, softcapped at 1.35 - always beatable by growing/merging/fusing, never by grinding the same fight.
- Generator picks 4 species (biased toward elements that *don't* hard-counter the player's squad at low rungs, neutral later), distributes targetPower using the species' base stat shape, and renders them through the same CreatureFactory - **opponents are beasts the player could make**, which quietly advertises fusion combos ("wait, you can fuse THAT?").
- Every 5th rung is a **Boss**: one giant T+1 beast with 3× HP instead of a squad - a spectacle fight and a guaranteed egg + core drop.

## Win/lose flow

**Win:** slow-mo on the final KO → victory screen: coin fountain (`reward = 20 + 8·rung`), ~35% egg drop, core drop every 2-3 wins, XP to all four squad members, sticker check, **NEXT BATTLE** button glowing. Rung increments.
**Lose:** never punishing - partial coins (`round(reward·0.4)`), full XP, and the near-miss framing from the WoopKid retention contract: if the enemy's remaining HP was <20%, show "SO CLOSE! Their last beast had a sliver left!" + a tip ("Try a Tide beast - POW! against Ember"). Rung does not reset; retry is one tap.

**Duration guardrail:** if a battle passes 45s, a "Sudden Woop" ramp multiplies all damage ×1.5 every 5s until someone drops. No stalemates, ever.

## Legibility rules (age 6 floor)

- Max 8 sprites on screen; one ability animation at a time (queued).
- Health bars are chunky, green→yellow→red.
- Damage numbers are the *only* floating text during fights (plus POW!/meh callouts).
- Battle speed toggle (1×/2×) for impatient veterans - persisted preference.
