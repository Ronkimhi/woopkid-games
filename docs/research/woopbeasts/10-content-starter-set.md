# 10 - Content: Starter Set

The concrete launch content: elements, species, parts, names, stickers. All values are v1 proposals; tune in playtest, but ship something THIS shaped. Art direction (hero physique + future tech widgets) is defined in `06-creature-generation.md`.

## Elements (8)

| Element | Icon | Color | Personality | Ability (see `05`) |
|---|---|---|---|---|
| Ember | 🔥 | `#FF5757` | fierce, crackly | Flame Burst (AoE) |
| Tide | 🌊 | `#4CC9F0` | calm, unstoppable | Healing Wave |
| Bloom | 🌿 | `#6FDB6F` | grounded, wiry | Vine Wrap (slow) |
| Spark | ⚡ | `#FFD93D` | zippy, overclocked | Overcharge (haste) |
| Frost | ❄️ | `#9BD5FF` | cool, crystalline | Ice Block (shield) |
| Stone | 🪨 | `#C9A87C` | sturdy, chunky | Boulder Slam (nuke+stun) |
| Gloom | 🌑 | `#8B7FD4` | mischievous, stealthy | Spook (weaken) |
| Gleam | ✨ | `#FFC2E2` | radiant, proud | Rally (team ATK) |

Effectiveness matrix: canonical copy lives in `05-mechanics-battle.md`; do not duplicate-and-drift.

## Starter species roster (24 = 3 per element)

Base stat totals ≈ 150-210 at T1; shape = the stat the species skews toward, which also sculpts its body (`06`: ATK → muscle, HP → frame, DEF → armor, SPD → legs/thrusters, SPC → glow). Physique and traits use the vocabulary from `06`.

| Species | Element | Physique | Skew | HP/ATK/DEF/SPD/SPC | Signature traits (headgear / chest / back / arm / legs / tail) |
|---|---|---|---|---|---|
| Emberling | Ember | bruiser | ATK | 38/52/28/34/28 | horn_crest / power_seams / - / power_fists / power_boots / plasma_tail |
| Charbit | Ember | sprinter | SPD | 32/40/24/54/26 | mohawk_fin / - / jetpack / - / hover_boots / plasma_tail |
| Pyrogon | Ember | tank | DEF | 42/38/50/22/28 | horn_crest / armor_plate / spine_fins / - / power_boots / stub_tail |
| Tidepup | Tide | tank | HP | 60/30/32/30/28 | ears_tall / core_reactor / - / - / power_boots / cable_tail |
| Bubbin | Tide | sprinter | SPC | 40/26/26/32/52 | antenna_array / core_reactor / - / - / hover_boots / cable_tail |
| Waverex | Tide | bruiser | ATK | 36/50/30/36/26 | mohawk_fin / power_seams / spine_fins / power_fists / raptor_legs / blade_tail |
| Sproutle | Bloom | tank | DEF | 40/28/52/24/32 | horn_crest / armor_plate / - / - / power_boots / stub_tail |
| Petalpuff | Bloom | sprinter | SPC | 38/24/30/32/54 | antenna_array / power_seams / holo_wings / - / hover_boots / - |
| Thornick | Bloom | bruiser | ATK | 34/52/32/34/24 | mohawk_fin / - / spine_fins / arm_blades / raptor_legs / blade_tail |
| Zapling | Spark | sprinter | SPD | 30/38/22/60/28 | antenna_array / power_seams / jetpack / - / hover_boots / cable_tail |
| Voltibit | Spark | sprinter | SPC | 34/28/24/40/52 | visor / core_reactor / - / mech_arm / hover_boots / cable_tail |
| Staticub | Spark | tank | HP | 56/32/30/36/24 | ears_tall / core_reactor / shoulder_cannon / - / power_boots / stub_tail |
| Frostfin | Frost | tank | DEF | 38/26/54/26/32 | visor / armor_plate / spine_fins / - / power_boots / blade_tail |
| Chillit | Frost | sprinter | SPD | 32/36/26/54/28 | ears_tall / - / jetpack / - / hover_boots / stub_tail |
| Glacigon | Frost | tank | HP | 58/30/38/22/28 | horn_crest / armor_plate / spine_fins / power_fists / power_boots / - |
| Pebblit | Stone | tank | DEF | 40/28/58/18/30 | - / armor_plate / - / - / power_boots / stub_tail |
| Boulderox | Stone | bruiser | ATK | 44/54/40/18/20 | horn_crest / armor_plate / - / power_fists / power_boots / - |
| Cragpup | Stone | tank | HP | 62/32/38/24/20 | ears_tall / armor_plate / shoulder_cannon / - / power_boots / stub_tail |
| Shadewisp | Gloom | sprinter | SPC | 34/26/22/38/56 | - / power_seams / holo_wings / - / hover_boots / cable_tail |
| Grimble | Gloom | bruiser | ATK | 32/54/26/40/24 | horn_crest / - / - / arm_blades / raptor_legs / blade_tail |
| Mothra | Gloom | sprinter | SPD | 30/34/22/58/32 | antenna_array / - / holo_wings / - / raptor_legs / - |
| Lumibit | Gleam | sprinter | SPC | 36/24/28/34/56 | antenna_array / core_reactor / holo_wings / - / hover_boots / - |
| Shinepaw | Gleam | bruiser | ATK | 34/50/30/38/26 | ears_tall / power_seams / - / power_fists / raptor_legs / stub_tail |
| Radiglow | Gleam | tank | HP | 58/28/34/28/30 | visor / core_reactor / holo_wings / mech_arm / power_boots / - |

Eyes default by personality: bruisers `angry_brow`, sprinters `hero_eyes` or `cool_shades`, tanks `hero_eyes`; tech-heavy species (Voltibit, Radiglow, Frostfin) use `cyber_eye`/`visor`. Exact per-species eye picks are a build-time art pass.

Availability: 3 default species in Basic Eggs at start (Emberling, Tidepup, Sproutle); each element egg unlock (`07` ladder) adds its 3 species to the pool. Gloom/Gleam species are the late-game exotics.

**Fusion species space from this roster alone:** 24×24 = 576 ordered pairs, each with its own inherited physique, muscle scaling, and widget mix, plus a player-given name, before gen-2/gen-3 fusions multiply it further.

## Name generator (fusion suggestions)

Suggestion 1: **portmanteau** - first syllable(s) of head's name + last syllable(s) of body's name (`Ember|ling` + `Tide|pup` → "Emberpup", "Tideling").
Suggestion 2: **element mash** - element syllable + species syllable from the pools below.
Suggestion 3: **wildcard** - random prefix+suffix from the pools (seeded, so re-rolls are stable per creature).

| Element | Prefix pool | Suffix pool (shared) |
|---|---|---|
| Ember | Char, Pyro, Blaze, Sizz, Fla | ox, ling, bit, gon, pup, wisp, paw, puff, rex, tron, bot, zilla |
| Tide | Aqua, Bub, Wave, Drip, Splash | |
| Bloom | Sprout, Leaf, Fern, Moss, Petal | |
| Spark | Zap, Volt, Buzz, Jolt, Stat | |
| Frost | Chill, Glaci, Snow, Icy, Brrr | |
| Stone | Peb, Crag, Rock, Boulder, Rumble | |
| Gloom | Shade, Grim, Spook, Murk, Whisp | |
| Gleam | Lumi, Shine, Glow, Radi, Spark | |

(`tron` and `bot` suffixes added in the tech revamp; they pair naturally with widget-heavy fusions.)
Free-typing is always offered; profanity guard = a small denylist + max 12 chars (kid site, no chat, low risk).

## Sticker & badge definitions

WoopProfile stickers (score = Woopdex count): **bronze 10 / silver 30 / gold 75.**

In-game badge wall: First Hatch, First Merge, First Fusion, First Win, Boss Slayer (first boss), Chain Reaction (chain ×2), Hoarder's Wisdom (first merge-5), Chimera (gen-3 fusion), Hero Maker (first T3), Mythic (first T5), Full Rainbow (all 8 elements owned at once), Fully Loaded (a beast with 4+ widgets), Dex 100.

## Copy voice (all player-facing text)

≤5 words, exclamation-friendly, zero jargon: "NEW SPECIES!", "SO CLOSE!", "CHAIN ×2!", "Ranch full!", "POW!", "FULLY LOADED!", "Your beasts trained hard!". Never "error", "invalid", "insufficient"; blocked actions always name the fun fix ("Win battles to find Cores 💠").
