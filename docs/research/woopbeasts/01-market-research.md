# 01 - Market Research

What already works out there, what we borrow, what we deliberately drop. Researched 2026-07-06.

---

## 1. Pokémon Infinite Fusion (fangame)

**What it is:** the definitive fusion game - any two Pokémon combine into one of 250,000+ species. A fusion item lets you pick which creature is the **head** and which is the **body**, with live previews of both outcomes.

**Mechanics worth stealing:**
- **Head/body asymmetry.** Fusing A+B ≠ B+A. Stats are a weighted average biased **body → physical** (ATK/DEF/SPD) and **head → special** (HP/SPA/SPD-spec). Typing = head's primary type + body's secondary (fallbacks if duplicated). This one rule creates enormous strategy from a single interaction.
- **Preview before commit.** Showing both possible outcomes before fusing turns the decision itself into gameplay.
- **Reversibility.** Fuse/unfuse/re-fuse freely → players experiment without fear. Experimentation IS the game.
- **Fusions are first-class citizens:** own stats, own dex entry, own name.

**What we drop:** the full RPG (routes, gyms, HMs, 400-move system). We keep the fusion math and the reveal; battles become an auto-battler (below).

Sources: [Fusion FAQs - Infinite Fusion Wiki](https://infinitefusion.fandom.com/wiki/Fusion_FAQs), [pokemoninfinitefusion.net/gameplay](https://pokemoninfinitefusion.net/gameplay/), [Differences with the official games](https://infinitefusion.fandom.com/wiki/Differences_with_the_official_games)

## 2. Infinite Craft (neal.fun, 2024)

**What it is:** drag two elements together; an LLM (Llama 2) invents the result in real time. Theoretically infinite combinations.

**Mechanics worth stealing:**
- **The unknown-result pull.** Because the outcome is genuinely novel, every combine is a curiosity slot machine. Our fusion reveal must preserve suspense: hold → shake → flash → reveal.
- **"First Discovery."** If nobody ever made this thing before, the game says so and your name sticks to it. Single-player translation: first time YOU create a species → "NEW SPECIES DISCOVERED!" + you name it + it's permanently yours in the Woopdex. Naming = ownership = attachment.
- **The collection panel.** Everything you've ever made stays usable. Nothing is consumed by discovery.
- **AI as content engine.** Proof that "AI invents the content per-player" is a shippable, viral mechanic - this is the exact pattern our future AI art backend follows (their loading animation literally means "the AI is thinking").

**What we drop:** pure sandbox with no goals. Kids 6-11 need a purpose for creations → battles give every creation a job.

Sources: [Infinite Craft - Wikipedia](https://en.wikipedia.org/wiki/Infinite_Craft), [Infinite Craft Wiki](https://infinite-craft-nealfun.fandom.com/wiki/Infinite_Craft_(Neal.fun)_Wiki), [TV Tropes entry](https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/InfiniteCraft)

## 3. Merge Dragons and the merge genre (2017→)

**What it is:** the genre-defining merge-3: place 3 identical objects adjacent → they fuse into one higher-tier object. 500+ items, dragons evolve through stages. Massive long-tail retention (600+ quests, still growing).

**Mechanics worth stealing:**
- **Merge-3 = visible power.** The result is physically bigger/shinier - a tactile "level up" no number can match. Our tier-ups (Baby→Kid→Hero→Mega→Mythic) grow the sprite and add visual traits (glow, aura, extra horns).
- **Merge-5 bonus.** Merging 5 instead of 3 yields TWO results - rewards hoarding patience. We adopt this exactly.
- **Idle return reward.** Squad "trains while you're away" → coins waiting on return (Merge Monsters pattern). Pets Clicker already does idle income; we reuse its `lastSeen` implementation.
- **Chain merges.** A merge that creates a third-identical triggers a cascade → combo fanfare.

**What we drop:** land-unlocking map sprawl, energy caps, the entire IAP economy. WoopKid = no monetization pressure, ever.

Sources: [Merging - Merge Dragons Wiki](https://mergedragons.fandom.com/wiki/Merging), [A (Not So) Brief History of the Merge Genre](https://pratama-naufal.medium.com/a-not-so-brief-history-of-the-merge-genre-b28136f33d22), [Merge Monsters: Idle RPG](https://apps.apple.com/us/app/merge-monsters-idle-rpg/id1524975344)

## 4. Auto-battlers (TFT, Squad Busters, Merge Squad)

**What it is:** you build/arrange the team; the fight resolves itself. Strategy lives *before* the fight; the fight is a spectacle you watch.

**Why it's right for 6-11:** no execution skill or reflexes required, so a 6-year-old wins battles - but team composition (elements, fusion choices, who's in the squad) gives an 11-year-old real decisions. Battles are also short (20-40s), which fits the reward cadence.

**We already own the skeleton:** `games/merge-squad/index.html` (116 KB) ships drag-to-merge + auto-battle + coins + auto-save. WoopBeasts extends that proven pattern with elements, fusion, and the Woopdex.

**What we drop:** synchronous PvP, positioning grids, item builds. Opponent squads are procedurally generated at a target power (see `05`).

## 5. Game feel ("juice") - cross-cutting

Standard indie juice stack, already mandated by WoopKid standards: layered feedback per action - particles + squash-and-stretch + pitch-varied procedural SFX + subtle screen shake + easing on everything. Key kid-specific constraints from the cross-game standards: **no full-screen flashes** (eye strain), shake stays subtle, max 4-6 simultaneous sounds.

## Synthesis - the borrow table

| Source | We take | We leave |
|---|---|---|
| Infinite Fusion | Head/body fusion math, typing inheritance, preview, reversibility | The whole RPG shell |
| Infinite Craft | Unknown-result suspense, first-discovery naming, everything-stays collection, AI-as-content pattern | Goal-less sandbox |
| Merge Dragons | Merge-3/merge-5, visible tier-ups, chains, idle return | Map sprawl, energy, IAP |
| Auto-battlers | Watchable fights, pre-fight strategy, short battles | PvP, positioning depth |
| Merge Squad (ours) | Drag-merge code pattern, auto-battle loop, coin economy, auto-save | - (direct ancestor) |

**The gap nobody fills:** no browser game combines *infinite creature invention* (Infinite Craft's magic) with *creature raising and battling* (Pokémon's magic) in a kid-safe, ad-free, offline package. That's the slot WoopBeasts takes.
