# 04 - Fusion & Merge (the heart)

Two distinct verbs, deliberately kept different in feel and purpose:

| | **FUSION** (2 beasts → new species) | **MERGE** (3 identical → next tier) |
|---|---|---|
| Emotion | Discovery, invention, "what will it BE?" | Power, growth, "it got HUGE" |
| Input | Any 2 beasts, any species | 3 same species, same tier |
| Output | ONE new-species beast | ONE beast, tier+1 |
| Where | Fusion Lab screen | Ranch (drag on the grid) |
| Cost | 1 Fusion Core | Free |
| Reversible | Yes (unfuse) | No |
| Source | Pokémon Infinite Fusion | Merge Dragons |

---

## FUSION

### Interaction

Fusion Lab: two pods (HEAD pod on top, BODY pod below) + a result chamber. Drag any two beasts in. A **swap button** flips head↔body - and the preview updates live, showing silhouette, element badges, and stat bars for the current arrangement. Choosing the arrangement IS the strategy (per Infinite Fusion: A+B ≠ B+A). Smash the big FUSE button → suspense sequence (chamber shakes, light builds, 1.5s) → reveal.

### Stat math (canonical)

Body biases the physical stats, head biases the vital/special stats, then a fusion bonus:

```
ATK = round((0.6·body.ATK + 0.4·head.ATK) · 1.10)
DEF = round((0.6·body.DEF + 0.4·head.DEF) · 1.10)
SPD = round((0.6·body.SPD + 0.4·head.SPD) · 1.10)
HP  = round((0.6·head.HP  + 0.4·body.HP ) · 1.10)
SPC = round((0.6·head.SPC + 0.4·body.SPC) · 1.10)
```

The ×1.10 bonus guarantees a fusion is never strictly worse than its parents' average - fusing always feels like progress. Level of the fusion = `max(1, round((head.level + body.level)/2))`; tier = `max(head.tier, body.tier)`.

### Element inheritance (canonical)

- Primary element = **head's** primary.
- Secondary element = **body's** primary; if that equals the head's primary, use body's secondary (fusions of fusions can carry one); if none, the fusion is mono-element.
- Dual-element beasts hit with their better multiplier and are hit at the *product* of multipliers against each of their elements (details in `05`).

### Species identity & naming

A fusion's **species** is the ordered pair `(headSpecies, bodySpecies)` - Emberling-head + Tidepup-body is a different species than the reverse. With 24 starter species that's 576 fusion species from generation 1 alone, and fusions can themselves be fused (see lineage), so the species space explodes - *infinite creation* in practice.

**First time a species is created → "NEW SPECIES DISCOVERED!"** full celebration + the player names it. Name UI offers 3 generated suggestions (portmanteau of parents + element syllables, generator in `10`) plus free typing. The name is permanent in the Woopdex and appears every time that species is made again. This is Infinite Craft's First Discovery, made personal.

### Lineage (fusing fusions)

CreatureSpec stores `lineage: {head: parentSpecRef, body: parentSpecRef, gen}`. Hatched beasts are gen 0; a fusion's `gen = max(parents) + 1`, **capped at gen 3** (deeper trees explode visual complexity and stat inflation; the cap is framed positively: gen-3 fusions get the "Chimera" badge and max visual flair). The Woopdex entry for a fusion shows its family tree - kids love tracing "his grandpa was my starter."

### Unfuse

From the beast's detail card: unfuse returns **both parents** (at the levels they went in with) and removes the fusion (its Woopdex entry stays - discovery is permanent). Costs nothing but the original Fusion Core is not refunded. Reversibility invites experimentation - the research shows experimentation is the engine.

### Fusion Cores (the pacing valve)

Fusions cost 1 Fusion Core. Faucets: battle victories (~every 2-3 wins), daily streak chest, milestone stickers. Target pace: **3-6 fusions per session** - scarce enough that each reveal stays an event, plentiful enough to never block a session. Tuning notes in `07`.

---

## MERGE

### Interaction

On the Ranch grid: drag one beast onto another identical one → they pulse as a pair; drag a third on → **MERGE BLAST**. (Same drag mechanics as `merge-squad`; reuse its pointer code.) The game auto-highlights any ready trio with a soft glow (the "one glowing thing" rule).

### Rules (canonical)

- 3 × same species, same tier → 1 × that species at **tier+1**, stats ×1.8, level = highest of the three, XP carries from the highest.
- **Merge-5:** 5 identical → TWO tier+1 beasts (Merge Dragons' hoarder reward). UI hints when 5 are held: "Merge 5 → get 2!"
- **Chains:** if a merge result creates a new trio (two T2s already present + this new T2), it auto-triggers after a 0.6s beat → cascade with rising combo pitch and "CHAIN ×2!" callout.
- Fusion species merge too (3 identical fusions → tier-up) - this makes re-creating your discoveries worthwhile.

### Tier ladder

T1 Baby → T2 Kid → T3 Hero → T4 Mega → T5 Mythic (×1.8 stats per step; visual escalation per tier in `03`/`06`). A T5 Mythic requires 81 T1s of one species if pure-merged - in practice players mix leveling, fusion, and merging; T5 is the months-horizon flex.

### Why both verbs (and not one)

Merge alone (Merge Dragons) grows power but invents nothing. Fusion alone (Infinite Craft) invents but doesn't give the "my thing got bigger" arc. Together they braid the two strongest reward curves - and they feed each other: merging demands duplicates (eggs), fusion demands variety (also eggs), battles pay for eggs. One economy, two dopamine flavors.

## Edge cases

- Merging/fusing a squad member: allowed; result auto-takes the squad slot.
- Fusing two identical beasts: allowed (mono-element, symmetric stats) - species `(X,X)`, usually a chunky "double" variant; fun, slightly suboptimal, never blocked.
- Ranch full when unfusing (needs +1 slot): blocked with the friendly "make room" prompt.
- All stats clamp to 999; combos of bonuses can't overflow.
