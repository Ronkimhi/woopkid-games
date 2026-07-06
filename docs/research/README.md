# WoopKid — Wave 3 Game Research (2026-07-06)

Research for **3 new viral games** to add to the roster, chosen specifically to fix the two problems with the last games: **they were too easy** and they **lacked that great-gameplay feeling**.

## The diagnosis

The current roster leans on shallow hypercasual loops where failure is rare and skill barely matters. That's *why* they feel too easy and flat. The fix isn't "add more particles" — it's picking genres whose entire reputation is built on **skill, depth, and physical feel**. Each pick below attacks the problem from a different angle.

## The three picks

| # | Game | Slug | Genre lane (proven viral source) | Fixes the problem via… |
|---|------|------|----------------------------------|------------------------|
| 17 | **Parkour Panic** | `parkour-panic` | Momentum platformer (OvO, Vex) | **Skill ceiling** — tight momentum tech, one-touch death, a live timer, speedrun mastery |
| 18 | **Woop Swarm** | `woop-swarm` | Bullet-heaven survivors-like (Vampire Survivors) | **Build depth** — 15–25 real choices per run, weapon evolutions, escalating power fantasy |
| 19 | **Rope Rush** | `rope-rush` | Grapple-swing physics (Stickman Hook) | **Physical feel** — one-button pendulum momentum + ragdoll, satisfaction in the motion itself |

All three are:
- **Free & wildly viral** on the exact platforms our audience uses (Poki, CrazyGames, Coolmath, Hooda Math, unblocked/Chromebook hubs).
- **Not already in the roster** — distinct new genres.
- **Low skill floor, high skill ceiling** — a 5-year-old can start, a 12-year-old can master. (Directly satisfies the standards' final checklist items.)
- **Buildable within WoopKid constraints** — single HTML file, vanilla JS + Canvas, procedural Web Audio, shared localStorage profile, retention recipe.

## Why these three specifically (vs. the alternatives)

Considered and set aside: more .io games (Hole.io/Paper.io — we already have Noodle Arena's io-feel), crowd runners (Count Masters — fun but shallow, same trap as before), 2-player physics (Basket Random — we already have Bubble Tank Duel in that lane). The three chosen each raise a *different* quality axis the roster is missing, rather than repeating a lane.

## The shared principle across all three

Every one of these games is built on **one perfected core mechanic** rather than a pile of features:
- Parkour Panic → *momentum preservation + feel-tech* (coyote time, input buffering).
- Woop Swarm → *the tension/power escalation rhythm*.
- Rope Rush → *the pendulum-swing-to-launch conversion*.

**The instruction for the build phase:** prototype and get the ONE core mechanic feeling *great* before building any content around it. That's the discipline the previous games skipped — and the reason they felt flat.

## Documents

- [`17-parkour-panic.md`](./17-parkour-panic.md) — momentum precision platformer
- [`18-woop-swarm.md`](./18-woop-swarm.md) — bullet-heaven survivors-like
- [`19-rope-rush.md`](./19-rope-rush.md) — grapple-swing momentum game

Each doc contains: why it's viral (with sources), the core gameplay loop, the core mechanic in depth, difficulty/skill design (the "too easy" fix), a game-feel/juice checklist (the "great feeling" fix), WoopKid kid-safe adaptation, technical notes for the single-file build, and risks.
