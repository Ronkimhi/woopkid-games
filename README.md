# WoopKid World

Free browser games for kids ages 5-12. No ads. No tracking. No accounts. Just play.

Live: https://ronkimhi.github.io/woopkid-games/ (woopkid.com will point here)

## The Roster

| # | Game | Genre | Status |
|---|------|-------|--------|
| 1 | Woop Pets Clicker | Meme clicker + idle | Wave 1 |
| 2 | Trap Land | Troll platformer | Wave 1 |
| 3 | Wing It | One-tap flyer | Wave 1 |
| 4 | Speed Slope | Endless downhill ball | Wave 2a |
| 5 | Road Hopper | Endless crosser | Wave 2a |
| 6 | Noodle Arena | Snake arena vs bots | Wave 2a |
| 7 | Sky Stack | Tower stacker | Wave 2a |
| 8 | Beat Bounce | Rhythm dash | Wave 2b |
| 9 | Slice Rush | Physics slicer | Wave 2b |
| 10 | Bubble Tank Duel | 2-player same-screen duel | Wave 2b |
| 11 | Merge Drop | Physics merge puzzle | Wave 2c rebuild |
| 12 | Tap Rush | Endless runner | Wave 2c rebuild |
| 13 | Drift & Collect | Hold-to-steer racer | Wave 2c rebuild |
| 14 | Color Pop | Bubble shooter | Wave 2c rebuild |
| 15 | Block Stax | Falling blocks | Wave 2c rebuild |
| 16 | Merge Squad | Toy merge auto-battler | Wave 3 |
| 17 | Rope Rush | Swing & fly momentum | Wave 3 |
| 18 | Woop Swarm | Bullet-heaven survivors-like | Wave 3 |

## Principles

- No ads, ever. No pay-to-win. Kid-safe.
- No build step, no frameworks, no libraries. Each game is one self-contained HTML file.
- Mobile-first touch, 60fps on mid-range hardware.
- The site remembers you: personal bests, sticker album, and daily streak, all in localStorage. Nothing leaves the device.

## Local development

```bash
python3 -m http.server 8766
```

Open http://localhost:8766/

## Deploy

GitHub Pages serves the main branch root. Push to main and it ships.

## Docs

- Design spec: `docs/superpowers/specs/2026-07-02-woopkid-world-design.md`
- Cross-game standards: `docs/game-design/00-cross-game-standards.md`
- Implementation plans: `docs/superpowers/plans/`
