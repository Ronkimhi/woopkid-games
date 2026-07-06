# 00 - Vision

## One sentence

WoopBeasts is a full-screen creature lab where kids invent monsters nobody has ever seen - hatch them, grow them, fuse them into new species, evolve them by merging, and prove them in battle - and the game remembers every creature they ever made.

## Why this game, why now

WoopKid's 18 games are mostly **runs**: 90-second arcade loops with a score. WoopBeasts is the site's first **world**: a persistent collection kids return to daily, the way they return to a Minecraft save. It fills the biggest gap in the roster (long-horizon retention) and it is the natural home for the AI creature-art engine Ron plans to build - the one game where "the AI drew a creature just for you" is the entire fantasy.

## Audience

- **Core:** ages 6-11 on phones/tablets. Playable by a 6-year-old without reading (icons + color carry every decision); deep enough that an 11-year-old theorycrafts fusion combos.
- **Secondary:** parents watching over a shoulder - the "watchable moment" is the fusion reveal ("what did you MAKE?!").

## The dopamine thesis

The genre research (see `01-market-research.md`) shows four proven reward engines. WoopBeasts stacks all four:

1. **Discovery** (Infinite Craft): combining two things into an *unknown* result is a slot-machine pull with zero cost of failure. Every fusion is a reveal. First time a species is created → big "NEW SPECIES!" fanfare + permanent Woopdex entry with the kid's chosen name.
2. **Collection** (Pokédex): the Woopdex fills forever. Empty silhouette slots are open loops the brain wants closed.
3. **Progression** (Merge Dragons): merge-3 tier-ups give a visible, physical "my thing got BIGGER and SHINIER" jolt.
4. **Spectacle/validation** (auto-battlers): battles are hands-off fireworks where *your creations* perform. Winning with a beast you invented is authorship pride, not just victory.

The loop is engineered so a reward fires **every 20-40 seconds** in active play (see the dopamine map in `07-progression-economy-retention.md`).

## What it is NOT

- Not Pokémon. Original creatures, original names, original element system. No Pokémon names, art, silhouettes, sounds, or the word "Pokémon" anywhere in the product. (Live public kids' site = takedown magnet; original IP = ownable brand.)
- Not a gacha. No real money, no ads, no timers that beg. Eggs and Fusion Cores are earned by playing, full stop - WoopKid brand promise.
- Not multiplayer. Opponents are generated squads (see `05`). No accounts, no chat, no PII - kids' site.
- Not a 90-second run. Sessions are 3-15 minutes; the save is forever.

## Name options (decide at build)

| Name | For | Against |
|---|---|---|
| **WoopBeasts** (working) | On-brand, says "creature," strong | Slightly generic |
| **Beast Lab** | "Lab" sells the invention fantasy | Weak tie to Woop brand |
| **Fusioo** | Ownable, fun to say, fusion-first | Doesn't say "creature" |
| **Woopimals** | Cute, young-skewing | Undersells battles for older kids |

Recommendation: ship as **WoopBeasts**; keep "Fusion Lab" as the in-game name of the fuse screen (best of both).

## Success criteria

- A first-time player hatches, fuses, and wins a battle inside **3 minutes** with zero instructions.
- Day-2 return rate visibly above the arcade games (streak + idle reward do the pulling).
- The fusion reveal makes a watching sibling grab the tablet.
- The full game runs offline, single HTML file, 60 FPS mid-range Android - and the day the AI art engine exists, it plugs in behind `CreatureFactory` without changing one line of game logic.
