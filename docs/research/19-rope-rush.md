# Research: Rope Rush — Grapple-Swing Momentum Game

> **Slug:** `rope-rush`
> **Genre lane:** Physics swing / grapple momentum (Stickman Hook by Madbox)
> **One-line pitch:** One button. Hold to grab a rope and swing, release to fly. Carry your momentum from swing to swing to sail across the level — a ragdoll physics playground where timing is everything.
> **Why this game, now:** This is the fix for "no great gameplay feel" via **pure physics-momentum satisfaction**. It's the most *tactile* genre — a single-input game whose entire depth lives in the feel of a well-timed release. Trivial to start, genuinely skillful to master, and endlessly clip-worthy.

---

## 1. Why It's Viral (the accurate research)

Stickman Hook (Madbox, 2018) is a **Poki exclusive with ~6.5 million upvotes** — one of the most-played browser games in the world, with 100+ levels and a mobile version with tens of millions of installs. Why it spreads:

- **One-tap depth.** Controls are trivial (hold to hook, release to launch) but mastery — timing the *release* to convert a swing into maximum distance — takes real feel. Lowest possible skill floor, surprisingly high ceiling.
- **Momentum physics = intrinsic satisfaction.** Ragdoll physics turn every swing into a smooth, readable arc. A clean release that sends the stickman soaring feels *physically good* in a way that shallow tap games never do. The satisfaction is in the motion itself.
- **Runs end in seconds → instant restart.** Most failures happen fast, so "one more go" is frictionless and irresistible. Classic viral retention loop.
- **Readable in seconds, watchable forever.** You understand it instantly by watching, and a graceful flawless run *looks* great — clip-and-share fuel.
- **Skins + progression** give a light collection meta on top of the physics core.

**Sources:** [Stickman Hook — Poki](https://poki.com/en/g/stickman-hook) · [Stickman Hook — Google Play (Madbox)](https://play.google.com/store/apps/details?id=com.mindy.grap1) · [Stickman Hook overview — Favo Games](https://favogames.com/post/learn-everything-about-play-stickman-hook) · [Stickman Hook — Kizi](https://kizi.com/games/stickman-hook)

---

## 2. Core Gameplay Loop

1. The character auto-moves / falls forward through a side-scrolling level dotted with **anchor points** (hooks).
2. **Hold** input → a rope attaches to the nearest anchor ahead; you **swing** around it under gravity like a pendulum.
3. **Release** → you let go and fly along your current velocity tangent (a ballistic arc).
4. Time your grab-and-release across a chain of anchors to carry momentum and cross gaps, dodge hazards, and hit **boost pads / trampolines**.
5. Reach the **finish line** → level clear → next level.
6. Fall into a pit / hit a hazard → instant restart of the level.

**Round length:** levels are ~15–45 seconds; a session is a stream of quick attempts. Failures are fast; restart is instant.

---

## 3. The Physics (this IS the game — the feel lives here)

The magic is a **pendulum + ballistic** momentum model with juicy ragdoll rendering. Get the physics honest and it feels amazing; fake it and it feels dead.

- **Swing = pendulum constraint.** While hooked, the character is a mass on a fixed-length rope anchored to a point. Gravity accelerates the swing; the rope constrains distance. Real angular momentum — the lower you are in the arc when you release, the more horizontal speed you carry.
- **Release = tangential launch.** On release, convert the pendulum's angular velocity into a linear velocity vector (tangent to the arc). Then it's simple projectile motion (gravity only) until the next hook. **Momentum is conserved** — this conservation is the entire skill expression.
- **Auto-attach targeting:** hold grabs the best anchor ahead (nearest within a forward arc). Keep it forgiving — the skill is *timing*, not *aiming*. (Optional advanced mode: aim the rope for expert players.)
- **Ragdoll body:** render the character as a few linked segments (torso, limbs) with light physics so it flails and trails naturally. This is cosmetic but it's **80% of the "feel"** — the flailing limbs sell every arc. Verlet-integrated 2–4 point ragdoll is enough.
- **The skill:** release at the *bottom/forward* of the arc to maximize distance; release too early or too late and you fall short or fling into a wall. Chaining swings to *build* speed (each swing adding to the last) is the mastery loop.

> **Design rule:** the difference between "good" and "amazing" is whether a perfectly-timed release *feels* like it launched you. Tune gravity, rope length, and the velocity-conservation multiplier until a clean release produces a genuinely thrilling soar. Prototype *only* the swing until it feels great before building any levels.

---

## 4. Difficulty & Skill Design — fixing "too easy"

- **Death has real stakes:** fall in a pit, hit spikes/saws, or run out of anchors → restart. Missing a release timing = failure. This makes each swing matter.
- **Authored level curve:** ~30–60 short levels, difficulty rising. Early levels: evenly spaced anchors, generous gaps — teach the rhythm. Later: sparse anchors, precise release windows, moving anchors, no-hook gliding sections, hazards, and speed-required jumps where you *must* carry momentum from several swings back.
- **Two mastery layers:**
  - **Completion** (finish the level) — accessible to everyone.
  - **Flawless / speed** — a per-level best time and/or a "no-touch, one-flow" bonus for the skilled. Add optional collectible **stars** (3 per level, placed on the high-skill line) — the classic mobile 3-star chase that makes kids replay a cleared level.
- **A momentum wall:** design a few levels that are impossible unless you've internalized momentum-carry (you literally can't reach the next anchor from a standstill swing). These gate-check skill and create brag moments.

---

## 5. Game Feel & Juice Checklist

- **The rope:** draw it taut and clean; a subtle stretch/twang on attach. A faint **trail** behind the character while flying at speed.
- **Ragdoll flail:** limbs trailing and swinging — the single biggest feel contributor. Do this well.
- **Speed feedback:** motion streaks + a slight FOV/zoom-out or camera lead when moving fast; a rising *whoosh* pitch tied to velocity.
- **Attach / release SFX:** a springy *boing/twang* on grab, a satisfying *whip* on release. Boost pads = a punchy *thwomp* + burst.
- **Landing/finish:** confetti + time slam on clear; a comedic ragdoll *splat* + quick respawn on death (funny, never grim — kids laugh and retry).
- **Camera:** smooth follow with slight lead in the direction of travel and a tiny shake on hard impacts. Never jerky — smoothness sells the physics.
- **Boost pads, trampolines, and moving anchors** as level-spice that create big satisfying launches.
- Procedural Web Audio throughout; upbeat, springy tones; pitch-randomized.

---

## 6. WoopKid Adaptation

- **Character:** the WoopKid mascot instead of a stickman — a bouncy blob swinging on a stretchy rope. Death = a harmless bounce-splat into stars, instant retry.
- **Controls (perfect for touch — one input):**
  - Hold anywhere on screen = grab/swing; release = launch. Spacebar / mouse-hold on desktop. This one-button design is *ideal* for the WoopKid audience and Chromebooks.
- **Shared profile (`woopkid_rope-rush`):**
  - 🥉 Bronze: clear level 5.
  - 🥈 Silver: clear level 20.
  - 🥇 Gold: collect 30 stars (or beat 5 flawless/gold times).
- **Braggable number:** stars collected, or total speedrun time across the first 10 levels.
- **Collection meta:** unlockable mascot skins earned by progression/stars (Stickman Hook has 23 skins — a proven, cheap-to-build retention layer; we do it *earned only*, no ads/purchases per WoopKid brand).
- **Streak hook:** any attempt today feeds the daily flame.

---

## 7. Technical Notes (single-file, vanilla, Canvas)

- **Fixed-timestep physics** (accumulator, ~120Hz) — pendulum + ragdoll stability and deterministic feel depend on it. Variable dt makes rope physics jitter.
- **Pendulum math:** while hooked, either (a) constrain via angle + angular velocity (clean, exact) or (b) Verlet particle + distance constraint to the anchor (also gives you the ragdoll for free). Verlet is recommended — one system does rope, swing, and ragdoll.
- **Ragdoll:** 3–5 Verlet points with distance constraints (head, torso, 2 limbs); 2–3 constraint-solver iterations per step is plenty.
- **Levels:** data-driven — arrays of {anchors[], hazards[], boosts[], start, finish, stars[]}. Author many small levels quickly. Render static level to an offscreen layer.
- **Camera:** world→screen transform with smooth lerp follow + velocity lead.
- Object-pool particles/trails; integer draw coords; no in-loop filters.

---

## 8. Risks / Watch-outs

- **The swing feel is the entire product.** If the pendulum-to-launch conversion isn't thrilling, nothing else matters. Prototype and tune *that one mechanic* before anything else — get sign-off on feel before building levels.
- **Auto-attach must feel fair.** If the rope grabs the wrong anchor or misses, players blame the game. Tune the targeting arc generously.
- **Ragdoll can look janky if under-damped.** Add light damping so limbs trail gracefully, not spastically.
- **Keep it forgiving early, brutal late.** The floor must be near-zero (a 5-year-old swings and giggles) while the ceiling (flawless star runs) satisfies a 12-year-old.

---

## 9. Verdict

Rope Rush is the **most tactile, most instantly-satisfying** addition and the lowest-input game in the roster — one button, deep feel. It's the best "great gameplay feeling" bang-for-buck: a single perfected mechanic (momentum swing + ragdoll) carries the whole game. Lower build risk than Woop Swarm, higher feel-payoff than most of the current roster. Prototype the swing first; if it soars, the rest is level design and skins.
