# 02 - Core Loop

## The loop, one line

**Hatch → Grow → Fuse/Merge → Battle → Collect** - then battle rewards buy more eggs and cores, which feed more creation. Every arrow pays into the next.

```
        eggs                 XP, duplicates
   ┌──── Hatch ────► Grow ───────┐
   │                             ▼
 Woops ◄── Battle ◄── Squad ◄── Fuse / Merge
   │          │                  ▲
   │          └── drops (eggs, cores)
   └── buy eggs & cores ─────────┘
                 all of it ──► Woopdex (permanent collection)
```

## Second-to-second (active play)

| Time | Player does | Game gives |
|---|---|---|
| 0-5s | Taps an egg | Crack-crack-POP hatch reveal, new beast bounces out |
| 5-20s | Drags beasts around the Ranch, spots 3 of a kind | Merge glow highlights the trio automatically |
| 20-30s | Drops third onto the pair | Merge blast, bigger shinier beast, combo check |
| 30-60s | Opens Fusion Lab, picks head + body, watches preview flip | Suspense reveal → possibly "NEW SPECIES!" + naming |
| 60-100s | Taps FIGHT | 20-40s auto-battle spectacle, damage numbers, KOs |
| 100-110s | Victory screen | Coin burst, egg drop, sticker check, "next battle" tease |

A discrete reward fires every 20-40 seconds. No dead time: whenever the player has nothing to do, exactly one thing on screen is glowing (an affordable egg, a ready merge, a fightable battle) - the **"one glowing thing" rule**, enforced in `08-ux-fullscreen-mobile.md`.

## Session loop (3-15 min)

1. **Return reward:** "Your beasts trained while you were away!" → coins + maybe an egg (idle income, `07`).
2. **Spend:** hatch 1-3 eggs, do 1-3 merges/fusions.
3. **Prove:** 2-5 battles on the battle ladder.
4. **Progress ping on exit:** Woopdex count + next unlock tease ("2 more wins → Frost eggs!").

## The one big number

WoopKid standard: one pure score a kid can say out loud. Ours is **Woopdex count** - "I've discovered **47** beasts!" Always visible in the top bar on every screen. Hub `bestLabel: 'Beasts'`; `WoopProfile.reportRun` reports Woopdex count as the score.

## First-session script (target: fused + battled + won inside 3 minutes)

Scripted beats, no text walls - the tutorial is the UI glowing in sequence:

1. **0:00** - Game opens on a single giant wobbling egg. Everything else hidden. Tap-tap-tap → hatches your starter (guaranteed T1, element themed to a fun default). *Reward #1: a creature is born, confetti.*
2. **0:20** - Two more free eggs drop in. Hatch → now 3 beasts, two are the same species. *(Rigged: the duplicates guarantee the first merge.)*
3. **0:45** - A third duplicate egg drops. The trio glows. Drag together → **first merge**, T2 evolution blast. *Reward #2.*
4. **1:15** - Fusion Lab button pulses. Kid drags 2 beasts into the pods, sees the head/body preview flip, smashes FUSE. **First fusion → "NEW SPECIES DISCOVERED!"** → name it (tap-to-pick from generated names, or type). *Reward #3, the big one.*
5. **2:00** - FIGHT button pulses. Battle 1 is tuned to be unlosable (opponent power = 60% of player squad). Kid watches their invented creature win. *Reward #4: coins + egg + bronze sticker progress.*
6. **2:45** - Victory screen shows Woopdex "4 / ∞", next unlock tease, PLAY AGAIN glowing. Hooked.

Losses in battle 1-3 are impossible by tuning; from battle 4 the ladder is real (see `05`).

## Loop integrity checks (design-time invariants)

- Every currency has exactly one main faucet and one main sink (table in `07`).
- No action is ever punished: a lost battle still pays partial coins and shows "SO CLOSE!" near-miss framing when within 20% (WoopKid retention contract).
- Fusion is never a downgrade trap: preview shows the outcome before commit, and unfuse exists (returns both parents, consumes the fusion - see `04`).
- The loop closes offline: nothing in Hatch/Grow/Fuse/Merge/Battle/Collect requires the network. The AI art backend only *upgrades pictures* (see `06`).
