# 07 - Progression, Economy, Retention

## Currencies - one faucet, one sink each

| Currency | Main faucet | Main sink | Feel |
|---|---|---|---|
| **Woops** (coins) | Battle wins (`20 + 8·rung`; losses 40%) | Eggs, Snacks | Abundant, always flowing |
| **Eggs** | Bought with Woops; ~35% win drop; streak chest | Hatching | The "what's inside" pull |
| **Fusion Cores** | Every 2-3 wins; streak chest; sticker milestones | Fusion (1/fuse) | Scarce-ish, each one an event |

### Egg pricing (Woops)

```
eggCost(n) = round(30 · 1.15^floor(n/5))     // n = lifetime eggs bought
```

First eggs cost 30, creeping to ~60 by egg 25, ~120 by egg 50. Battle rewards grow with rung at a similar slope, so the *time per egg* stays roughly constant (~1.5-2 wins) - steady drip, no grind wall. **Snack** (feed for +15 XP): flat 10 Woops, the small always-available sink.

### Fusion Core pacing (open question #2 from README)

Target **3-6 fuses per session**. Proposed: core drop on win with probability `0.4`, +1 guaranteed in the daily streak chest, +1 per boss. Tune in playtest: if players hoard cores, raise fusion's spotlight (pulse the Lab); if they starve, raise drop to 0.5. Never sell cores for Woops at launch (would collapse the two-currency tension); revisit if pacing feels bad.

## The unlock ladder (long-term carrot)

Driven by battle-ladder rung - every few rungs opens something visible:

| Rung | Unlock |
|---|---|
| 1 | (start) Basic Eggs, 3 starter species pool |
| 4 | Ladder gets real (rungMult ≥ 0.95) |
| 5 | Boss #1 → **Ember Eggs** |
| 8 | Battle 2× speed toggle |
| 10 | Wild beast joins (guaranteed drop) → **Tide Eggs** |
| 15 | Boss → **Bloom Eggs** + Merge-5 hint quest |
| 20 | **Spark Eggs**; opponent squads start using fusions |
| 25 | **Frost Eggs** |
| 30 | **Stone Eggs**; bosses become fusion bosses |
| 40 | **Gloom Eggs** (exotic tease) |
| 50 | **Gleam Eggs** - full element roster open |
| 50+ | Endless ladder; rung milestones every 10 pay cores + eggs |

Next unlock is ALWAYS visible on the victory screen ("2 wins → Frost Eggs ❄️").

## Woopdex - the collection spine

- Every species ever created gets a permanent entry: portrait, player-given name, elements, best stats reached, family tree (lineage), date discovered.
- **Woopdex count is THE score** (hub `bestLabel: 'Beasts'`) - reported via `WoopProfile.reportRun('woop-beasts', dexCount, thresholds)`.
- Silhouette teasers: undiscovered starter species show as "?" silhouettes (open loops). Fusion space shows "∞ - what will you make?"
- Dex milestones (10/25/50/100 species) pay cores + a fanfare.

## Stickers (WoopProfile standard: bronze/silver/gold)

| Sticker | Threshold (score = Woopdex count) |
|---|---|
| Bronze | 10 species discovered |
| Silver | 30 species discovered |
| Gold | 75 species discovered |

Plus in-game (non-profile) badge wall: First Fusion, First Merge, First Boss, Chimera (gen-3 fusion), Mythic (first T5), Full Rainbow (all 8 elements owned at once).

## Daily streak & idle return

- **Streak:** uses WoopProfile's shared `streak`. Daily chest on first session of the day: Woops + 1 egg + 1 core; chest visuals upgrade at 3/7/14-day streaks (bigger chest, more confetti - contents grow mildly: never punishing to break a streak, only nicer to keep it).
- **Idle return:** reuse pets-clicker's `lastSeen` pattern - "Your beasts trained while you were away!" pays `min(hours, 12) · (5 + rung)` Woops on return. Capped so play always beats idling.

## The dopamine map (explicit)

Every action's reward, its sensory payload, and its schedule:

| Action | Reward | Sensory payload | Schedule |
|---|---|---|---|
| Tap egg (×3) | Anticipation ratchet | Crack SFX pitch rises, shell chips fly | Fixed |
| Hatch | New beast | POP + confetti + bounce-in + name card | Fixed |
| Hatch duplicate | Merge progress | "2/3!" chip glow | Variable |
| Merge | Tier-up | Blast ring, size-up squash-stretch, deeper drum | Player-timed |
| Chain merge | Combo | Rising pitch per link, "CHAIN ×2!" | Variable (jackpot) |
| Fusion preview flip | Curiosity | Silhouette morph + stat bars slide | Player-timed |
| FUSE | Reveal | 1.5s shake-build → flash → creature + ability card | Player-timed |
| First-ever species | **DISCOVERY** | Full fanfare, "NEW SPECIES!", naming ceremony, dex +1 | Variable (the big one) |
| Battle hit | Ticks of progress | Damage floats, squash, element SFX | ~1/sec ambient |
| POW! (super-effective) | Competence | 2× number size, "POW!" callout | Variable |
| Ability fires | Spectacle | Telegraph + unique VFX per element | ~2-3/battle |
| Win | Loot | Coin fountain, egg/core drops, XP bars filling | Every 30-60s of play |
| Near-miss loss | "SO CLOSE!" | Sliver-HP highlight + one tip | On loss within 20% |
| Unlock | New toy | Ladder banner + new egg wobbles in Hatchery | Every 2-5 rungs |
| Return next day | Streak chest + idle pay | Chest burst, counter ticks up | Daily |

Design rule: **fixed rewards teach, variable rewards hook.** The three variable-schedule jackpots (chain merge, new-species discovery, rare drops) are the retention engine; everything else is steady, predictable competence-feeding.

## Session-end hook

On back-button / visibility loss, save immediately (standard), and the next session's opening frame is the return reward - the game always opens with a gift, never a menu.
