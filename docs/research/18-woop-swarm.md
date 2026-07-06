# Research: Woop Swarm — Bullet-Heaven Survivors-like

> **Slug:** `woop-swarm`
> **Genre lane:** Bullet heaven / survivors-like / reverse bullet-hell (Vampire Survivors, Brotato, Survivor.io)
> **One-line pitch:** Move to dodge, auto-fire to fight. Survive escalating swarms of silly critters, level up, pick upgrades, and evolve your toys into screen-filling super-weapons.
> **Why this game, now:** This is the direct fix for "lacked depth / no great gameplay feel." The survivors-like is the most **build-deep, replayable, dopamine-dense** casual genre of the decade. It delivers the exact power-fantasy escalation the previous games never built toward.

---

## 1. Why It's Viral (the accurate research)

Vampire Survivors created a whole genre in 2022; in **May 2026 Valve officially named the category "Bullet Heaven"** on Steam. Survivor.io and dozens of free mobile/web clones have made it a mainstream casual staple. The genre is a proven, top-charting formula. What makes it *spread and retain*:

- **A power-fantasy arc every single run.** You start weak and vulnerable with one weak attack; 15 minutes later the whole screen is a firework of your projectiles and damage numbers. That transformation from fragile to unstoppable — *every run* — is the hook.
- **"Just one more run."** Runs are a fixed, digestible length (classic is ~15–30 min; a web/kid version should be **~5–8 min**). Each run is a fresh build gamble.
- **Gambling psychology, done cleanly.** Level-up offers you a *random choice of upgrades*. Choosing from randomized options each level is the same variable-reward loop that makes it BAFTA-winning-addictive — without any real-money gambling.
- **Build depth = infinite replay.** Dozens of weapon/passive combinations and **evolutions** (weapon + right passive → a transformed super-weapon). Discovering combos is the meta-game that outlives any single run.
- **Meta-progression between runs.** Collect currency during runs, spend it between runs on permanent boosts and unlocks. You get stronger even when you lose — nobody ever "wastes" a run.

**Sources:** [Vampire Survivors — Wikipedia](https://en.wikipedia.org/wiki/Vampire_Survivors) · [Bullet Heaven / survivors-like — Wikipedia](https://en.wikipedia.org/wiki/Vampire_Survivors%E2%80%93like) · [Evolution mechanic — VS Wiki](https://vampire.survivors.wiki/w/Evolution) · [Power-fantasy design analysis — kokutech](https://www.kokutech.com/blog/gamedev/design-patterns/power-fantasy/vampire-survivors) · [Gambling psychology — Univ. of Portsmouth](https://www.port.ac.uk/news-events-and-blogs/blogs/popular-culture/vampire-survivors-how-developers-used-gambling-psychology-to-create-a-bafta-winning-game) · [Free bullet-heaven games — BulletHaven](https://bullethaven.com/blog/BlogPost4_FreeBulletHeavenGames)

---

## 2. Core Gameplay Loop

1. Pick a character (each starts with a different signature weapon + stat bias).
2. Drop into an arena. **You only control movement.** Weapons fire automatically.
3. Enemies pour in from all edges in escalating waves. Dodge by weaving through gaps.
4. Killed enemies drop **XP gems** — walk over them to collect. Fill the XP bar → **LEVEL UP**.
5. Level-up **pauses the game** and offers **3 random upgrade cards** — pick one (new weapon, weapon upgrade, or passive item).
6. Repeat: get stronger, the swarm gets bigger, tension ramps, then a power spike lets you dominate — then the next tension wave hits.
7. Collect a passive's evolution partner + max the weapon → grab an evolution to transform it into a super-weapon.
8. Survive to the timer (win) **or** die (run ends). Either way, banked currency → meta-upgrades.

**Round length:** target **5–8 minutes** for the WoopKid audience (classic is 15–30; too long for kids and Chromebook sessions). A boss/finale at the timer's end gives a clean climax.

---

## 3. The Escalation Curve (this is the "great feel" — pacing IS the game)

The genius of the genre is a **breathe-in / breathe-out rhythm** that keeps players in flow:

- **Tension phase:** enemy count and toughness rise. The screen fills, gaps close, you're threading the needle, health matters.
- **Power phase:** you level up, add/evolve a weapon, and *suddenly* mow through the swarm you were just fleeing. Catharsis.
- Then the game raises the floor again and repeats — each cycle bigger than the last.

This oscillation is what keeps players in a *psychological flow state* — skill and challenge staying matched as both climb. **Getting this rhythm right is more important than any single weapon.** Author the spawn director around it:

- Minute 0–1: sparse, teach movement + first level-ups.
- Minute 1–4: steady ramp, first evolution should be reachable ~minute 3–4.
- Minute 4–6: density spikes, elite/mini-boss enemies appear.
- Minute 6–8: swarm climax → **boss** → win screen. (Or endless mode after, with a rising multiplier for score-chasers.)

Also include periodic **"treasure" moments** (a chest from an elite kill) that grant a random weapon-up or evolution — punctuation marks of joy in the ramp.

---

## 4. Build Depth (the antidote to shallow)

### Weapons (auto-firing toys — kid-safe theming)
Aim for **6–10 base weapons**, each with a distinct firing pattern:

- **Bopper Ball** — fires the nearest enemy (whip/knife analog). Reliable single-target.
- **Ring Pulse** — expanding rings around you (garlic/aura analog). Crowd control.
- **Bounce Disc** — ricochets between enemies. Fun chaos.
- **Star Spray** — random spread shots (magic wand analog). Volume.
- **Orbit Buddies** — pets that circle you and body-block/damage (King Bible analog). Defensive.
- **Boomerang Sock** — flies out and returns, pierces.
- **Puddle Bomb** — drops lingering goo pools (damage-over-time zones).
- **Lightning Zap** — random arcing strikes.

### Passives (stat/behavior items)
- Move speed, max HP, fire rate ("Cooldown"), projectile count ("+1 Projectile"), area size, projectile speed, XP magnet range, luck (better upgrade offers), armor, regen.

### Evolutions (the depth payoff)
Each weapon has a **passive partner**. Max the weapon (level ~8) **and** own the partner passive → an evolution card appears, transforming it into a super-weapon (bigger, pierces, adds an effect like knockback/homing/lifesteal-analog). Evolutions are the "aha, that's how it works" moment that fuels theorycrafting and word of mouth. Ship at least **4–6 evolutions** at launch.

> A run without an evolution is fun. A run *with* one is a story you tell a friend. That's the retention delta.

---

## 5. Difficulty & Depth Design — fixing "too easy" AND "no depth"

- **Real death stakes:** HP is finite; getting swarmed kills you. Early game *should* be losable if you play greedy. The dodge-weaving is a genuine skill.
- **Meaningful choices:** the 3-card level-up means players make ~15–25 build decisions per run. Bad picks = a weak run. This is the *depth* the previous games lacked — the player is authoring their power, not just tapping.
- **A difficulty selector / "curse" scaling:** an optional harder mode (faster/tougher enemies) for the 12-year-olds, plus meta-upgrades that let players opt into more challenge for more reward.
- **Score chase for mastery:** kills, survival time, and highest level reached feed a single braggable score. Endless mode after the boss with an escalating danger multiplier gives the top players an infinite ceiling.
- **Character unlocks** gated behind achievements (survive 5 min, reach level 20, evolve 3 weapons) — reasons to keep returning.

---

## 6. Game Feel & Juice Checklist

The genre is a *juice showcase* — the screen becoming chaos IS the reward. Layer aggressively (but pool everything and cap counts for 60fps):

- **Damage numbers** popping off every hit, floating up and fading. Crits bigger/gold. This is the core dopamine signal — never skip it.
- **Hit-flash:** enemies flash white on hit, squash on death, burst into a few particles + a coin/gem.
- **XP gems** with a satisfying magnet-suck + collect *ping* (rising pitch as you chain-collect — the "vacuum" feel).
- **Level-up:** screen dims, a bright banner slams in, cards deal out with easeOutBack, a triumphant chord. This pause is a *reward beat*, not an interruption.
- **Weapon evolution:** big screen flash, unique fanfare, the new weapon's first fire is oversized. Make it an event.
- **Screen shake** scaling with on-screen carnage (subtle, trauma-based, decays).
- **Enemy swarm rendering:** simple shapes, but *lots* of them, all bopping/wobbling. The visual density = the power fantasy.
- **Procedural audio:** layered zaps, pops, and collect-pings; a low pulsing tension bed that intensifies with enemy density; a boss horn. Cap concurrent sounds (~6) and pitch-randomize.

---

## 7. WoopKid Adaptation (kid-safe reskin)

- **No blood, no weapons-as-weapons.** You're a WoopKid mascot bopping silly **Goobers** (jiggly slimes), **Wobblers**, and **Puffs** with toys — paint splats, bubbles, socks, bouncy balls. Enemies "pop" into stars/confetti, not gore.
- **Theme the boss** as a giant goofy Mega-Goober, not a demon.
- **Controls:** virtual joystick (left thumb, floating — appears where you touch) on mobile; WASD/arrows on desktop. Movement-only makes this *extremely* touch-friendly — a major reason it fits kids and Chromebooks.
- **Shared profile (`woopkid_woop-swarm`):**
  - 🥉 Bronze: survive 3 minutes.
  - 🥈 Silver: reach level 20 / survive to the boss.
  - 🥇 Gold: evolve a weapon (or beat the boss).
- **Braggable number:** survival time + score (kills). Show "NEW BEST" with a big celebration.
- **Meta-currency:** collect **Woop Coins** in runs; spend between runs on permanent boosts (starting HP, magnet, luck) and character/weapon unlocks. Persisted in localStorage. *You always progress, even on a loss* — the anti-frustration core of the genre.

---

## 8. Technical Notes (single-file, vanilla, Canvas)

- **This is the most performance-critical game in the roster** — potentially hundreds of enemies + hundreds of projectiles + gems + particles + damage numbers on screen. Plan for it:
  - **Aggressive object pooling** for every entity type (enemies, projectiles, gems, particles, damage-number labels). Never allocate in the loop.
  - **Spatial hashing / uniform grid** for collision so it's not O(n²). Bucket entities into cells; only check neighbors.
  - **Cap enemy count** (e.g. ~300 on screen); when over cap, cull the furthest off-screen enemies. Kids' hardware/Chromebooks demand this.
  - **Batch draws by type/color**, integer coordinates, no shadowBlur/filters in-loop.
  - Damage numbers: cap active count, pool the label objects, fade fast.
  - Fixed-timestep update for deterministic spawn director + reproducible feel.
- **Spawn director** = a timeline/data table driving what spawns when + a difficulty multiplier ramp. Keep it data-driven so tuning is edits, not code.
- **Weapon system** = data-driven definitions (fire pattern, cooldown, damage, level scaling, evolution partner). Adding a weapon should be a data entry, not new plumbing.

---

## 9. Risks / Watch-outs

- **Scope.** This is the highest-complexity game in the roster. Ship a tight vertical slice first: 4 weapons, 3 passives, 2 evolutions, 1 boss, one 6-minute run. Expand after it feels great.
- **Performance is the make-or-break.** If it drops frames when the screen fills — the exact moment that's supposed to feel best — it fails. Profile with worst-case entity counts early.
- **Balance the level-up offers** so most builds are viable and evolutions are reachable in a normal run (~by minute 3–4). Frustration comes from never being offered your evolution partner — bias "luck"/offers so evolutions are attainable.
- **Keep the run short** for the audience. 15–30 min is too long for kids/Chromebook sessions; 5–8 is the sweet spot with an endless overtime for enthusiasts.

---

## 10. Verdict

Woop Swarm is the **deepest, most replayable** addition — the roster's answer to "lacked depth and that great gameplay feeling." Its power-fantasy escalation and build variety are a fundamentally richer loop than anything shipped so far. It's also the most ambitious build; treat performance and the escalation-pacing rhythm as the two things that must be perfect. Get those right and it's the flagship.
