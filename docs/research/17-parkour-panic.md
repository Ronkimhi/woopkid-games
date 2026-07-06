# Research: Parkour Panic — Momentum Precision Platformer

> **Slug:** `parkour-panic`
> **Genre lane:** Momentum platformer / precision parkour (OvO, Vex, Vex Hyper Dash)
> **One-line pitch:** A one-character speed-parkour runner where *momentum is everything* — run, slide, wall-jump and dive through hand-built obstacle courses against a live timer.
> **Why this game, now:** This is the direct fix for "too easy / no great gameplay feel." Momentum platformers are the single most respected skill genre on Chromebook/unblocked culture. Their entire appeal is a **high skill ceiling with a low skill floor** — anyone can move, but mastery takes hundreds of runs.

---

## 1. Why It's Viral (the accurate research)

OvO and the Vex series are perennial top-10 games on Coolmath, Hooda Math, CrazyGames and every "unblocked games" hub. They dominate school Chromebooks because they run in-browser with no download and pass classroom filters. What makes them *spread*:

- **The timer turns every level into a personal duel.** Every level has a built-in clock. The game explicitly nudges you to beat your own time. This is the same loop as speedrunning — infinitely replayable content out of a finite number of levels.
- **"I almost had it" deaths.** You fail by a hair, restart instantly, and try the *exact same run* a smidge cleaner. This is the purest version of the "one more try" loop in the whole roster.
- **Braggable skill expression.** Kids film and share clean runs. A perfect slide-jump-wall-kick chain *looks* impressive. There's a visible gap between a beginner and an expert playing the same level — that visible mastery gap is what makes friends say "let me try."
- **Momentum tech is discoverable.** Players find advanced moves (dive-cancels, slide-jumps, wall-climbs) on their own or from friends. Discovery = word of mouth.

**Sources:** [OvO on Coolmath](https://www.coolmathgames.com/blog/how-to-play-ovo-run-jump-slide-to-the-flag) · [OvO on CrazyGames](https://www.crazygames.com/game/ovo) · [Vex series](https://vex.game/) · [How to Play OvO — ant.games](https://ant.games/blog/game-guides/how-to-play-ovo/) · [OvO Movement Wiki](https://ovo-dimensions.fandom.com/wiki/Movement) · [OvO speedrun guides](https://www.speedrun.com/ovo/guides/vvf5i)

---

## 2. Core Gameplay Loop

1. Spawn at the start of a single-screen (or short auto-scroll) obstacle course.
2. Move right (and up/down) using momentum-based platforming to reach the **flag/exit**.
3. Avoid spikes, saws, crushers, gaps, and moving hazards. One touch = death.
4. Death → **instant respawn at the level start** (< 250ms, no game-over screen for a normal death).
5. Reach the flag → level-complete flash with your **time** vs. your **best time** → next level auto-loads.
6. The run of levels is continuous; the "session" is a stream of attempts.

**Round length:** individual levels are 10–40 seconds when clean; a level might take 20–150 attempts to master. A play session is 3–15 minutes.

---

## 3. The Movement System (this is the whole game — get it perfect)

Everything below is the reason the genre *feels* incredible. **Do not simplify the movement to "arrow keys move a box."** The feel lives in these details:

| Move | Input | Behavior & feel |
|------|-------|-----------------|
| **Run** | Hold left/right (or tilt/hold-side on touch) | Acceleration ramp with a top speed. Never instant — you *build* speed. Friction on release, not a hard stop. |
| **Jump** | Tap up / spacebar / tap-screen | Variable height — hold longer = higher (short-hop vs. full jump). Apply gravity asymmetrically: fall faster than you rise (feels snappy, not floaty). |
| **Slide** | Down while grounded + moving | **The primary speed multiplier.** Lowers hitbox (slide under hazards) and *preserves/boosts* horizontal speed. |
| **Slide-jump** | Jump during a slide | Launches much farther horizontally than a standing jump. The signature "skill move." Bridges gaps a normal jump can't. |
| **Wall-slide** | Press into a wall midair | Slows your fall while touching a wall. |
| **Wall-jump** | Jump while wall-sliding | Kicks off in the opposite direction. Chain them to climb vertical shafts or cross wide gaps. |
| **Dive** | Down while airborne | Fast downward slam that *keeps* momentum on landing (auto-slide) — squeeze through low gaps, land running. |

### The invisible feel-tech (non-negotiable — this is what "great gameplay feel" MEANS here)

- **Coyote time (~80–100ms):** you can still jump for a few frames *after* walking off a ledge. Without this, precision platformers feel unfair. With it, they feel generous and skillful.
- **Jump input buffering (~100ms):** if the player taps jump slightly *before* landing, the jump fires the instant they touch ground. Same for slide-on-landing. Zero lost frames.
- **Corner correction / ledge nudge:** if a jump clips a corner by a pixel or two, nudge the player up/over instead of stopping them dead.
- **Momentum preservation across states:** transitioning run→slide→jump→dive must never silently drop speed. The whole thrill is *carrying* speed through a chain of moves.
- **Air control, but limited:** you can steer midair, but not fully reverse instantly — commitment matters.

> **Design rule:** if a death ever feels like the game's fault, the feel-tech is wrong. If a death always feels like *my* fault, it's right. That single distinction is the difference between this game and the "too easy, no feel" games before it.

---

## 4. Difficulty Design — directly fixing "it was too easy"

The previous games were too easy because failure was rare and shallow. Parkour Panic is built around *productive failure*:

- **One-touch death.** Hazards kill instantly. This creates real stakes on every jump.
- **Difficulty is authored, not random.** Hand-design ~20–30 levels on a tuned curve. Early levels teach one move at a time (jump → slide → wall-jump → dive → combos). Later levels demand chained tech under time pressure.
- **Mechanic-teaching ramp:** each new level introduces exactly one new idea, then the next combines it with the previous. No text tutorials — the level *is* the tutorial (Nintendo-style).
- **A hard "gate" level around level 8–10** that filters casual players and creates the brag ("did you beat level 9?").
- **Optional challenge layer for the top 10%:** a collectible token hidden on a hard-to-reach path in each level, and a per-level target ("gold time"). Casual kids finish the level; skilled kids chase the token + gold time. This widens the audience *without* dumbing down the core.

**The skill ceiling is the retention engine.** Finite levels + a timer + hidden tokens = effectively infinite replay for anyone who catches the bug.

---

## 5. Game Feel & Juice Checklist

The genre looks minimal but *feels* rich. Layer these:

- **Speed lines / motion streak** behind the character when above a speed threshold (the visual reward for maintaining momentum).
- **Squash on land, stretch on launch.** Every jump and landing deforms the character.
- **Dust puffs** on land, slide, and wall-kick. Slide leaves a short skid trail.
- **Screen-space micro-shake** on death and on hard landings (subtle — kids' game). Trauma-based, decays fast.
- **Chromatic speed tint / vignette** that intensifies slightly at max speed.
- **Death = a quick particle burst + freeze-frame (~60ms) + instant respawn.** No punishing pause. The freeze-frame sells the impact; the instant respawn keeps flow.
- **Flag reached = confetti burst, time stamp slams onto screen with easeOutBack, satisfying chime.**
- **Audio carries the momentum:** a rising "whoosh" pitch tied to speed, a punchy *thock* on wall-kick, a *whumph* on dive, a bright arpeggio on level clear. Procedural Web Audio, pitch-randomized ±5%.
- **Ghost replay (stretch goal):** a faint translucent "ghost" of your best run on that level races alongside you. This is the single highest-value retention feature in the genre — you're literally racing yourself. Store the input/position trace in localStorage.

---

## 6. WoopKid Adaptation

- **Kid-safe theming:** the character is a bouncy WoopKid blob/egg mascot. "Death" is a harmless *poof* into stars and an instant re-poof back — cartoon reaction, never gory. Hazards are cartoon spikes, gooey saws, bouncy crushers.
- **Touch-first controls (critical — this genre is keyboard-native, we must nail touch):**
  - Left third of screen = hold to run left, right third = hold to run right, tap anywhere = jump, swipe/hold down = slide/dive. OR
  - Auto-run right + tap-to-jump, hold-jump for height, tap-down for slide/dive (simpler, more mobile-native — **recommended for the WoopKid audience**).
  - Provide both a "manual" and "auto-run" scheme; auto-run lowers the floor for 5-year-olds while the timer keeps the ceiling high for 12-year-olds.
  - Keyboard (WASD/arrows + space) for Chromebook players — this is where the genre lives, so it must be first-class.
- **Shared profile stickers (`woopkid_parkour-panic`):**
  - 🥉 Bronze: clear level 5.
  - 🥈 Silver: clear level 15.
  - 🥇 Gold: collect 10 hidden tokens (or beat 5 gold times).
- **Braggable number:** total tokens collected, or best cumulative time across the first 10 levels ("speedrun %").
- **Streak hook:** any attempt today feeds the daily streak flame.

---

## 7. Technical Notes (single-file, vanilla, Canvas)

- Fixed-timestep physics recommended (accumulator, ~120Hz sub-steps) so momentum tech is frame-rate independent and deterministic — **essential** for a game where 2 pixels of momentum matter and for ghost replays to line up.
- Tile-based level definition: author levels as compact ASCII/array maps in the JS, rendered to an offscreen canvas once per level (static background layer) with the character/particles on the dynamic layer.
- AABB collision with swept resolution (check X and Y separately) to avoid tunneling at high speed. Never let a fast player clip through a spike unchecked.
- Object-pool particles (dust, death burst, confetti) — cap ~80.
- Ghost = array of {x,y,frame} sampled every N frames, replayed on next attempt. Tiny storage footprint.
- Respawn resets state instantly; keep level geometry cached so restart is a variable reset, not a reload.

---

## 8. Risks / Watch-outs

- **Touch momentum is genuinely hard.** Budget real tuning time. If touch feels bad, the whole game fails. Prototype touch *first*, not last.
- **Don't over-tutorialize.** Kids figure out momentum by feel. Teach through level design.
- **Keep death punishment near-zero (time only).** The stakes are "lose 15 seconds of progress," never "sit through a screen." Flow is sacred.
- **Level authoring is the real work.** The engine is a week; 25 great levels on a perfect curve is where the quality lives.

---

## 9. Verdict

Parkour Panic is the **highest-skill-ceiling** addition to the roster and the most direct antidote to "too easy." It trades procedural endlessness for authored, masterable challenge — the exact quality the last games lacked. Nail the movement feel-tech (coyote time, buffering, momentum preservation) and this becomes the game kids show their friends.
