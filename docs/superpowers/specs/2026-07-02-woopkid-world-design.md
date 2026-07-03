# WoopKid World: Site Rebuild + 15-Game Viral Roster

Date: 2026-07-02
Status: Approved by Ron (design approved same day)
Owner: Ron Kimhi

## 1. Vision

Rebuild woopkid.com's games experience from the ground up: an extraordinary landing site ("WoopKid World") plus a roster of 15 games engineered from virality research to make kids ages 5-12 come back daily and recruit their friends. Ad-free, kid-safe, zero tracking, zero servers.

Success criteria:
- The site feels like a playground, not a directory. A kid lands and wants to touch everything.
- Every game passes the "one more try" test: sub-second restart, one braggable number, near-miss deaths, 30-90 second rounds.
- The site remembers the player (sticker album, bests, streaks) with pure localStorage.
- Ships on GitHub Pages, loads fast on a school Chromebook.

## 2. Research Foundation (2026-07-02)

Synthesized from Poki, CrazyGames, Coolmath, and Chromebook "unblocked games" culture:

- Dominant genres kids spread peer-to-peer: Suika merge physics, meme clickers, troll platformers (Level Devil), Slope-likes, Crossy-likes, io-games, rhythm dashes.
- Underserved openings WoopKid can own: io-feel with client-only bots, same-device 2-player touch games, daily-streak puzzles for kids, persistent progression (games that remember you).
- Universal retention recipe (every game must implement): instant restart (<1s), one pure score number, near-miss engineering, 30-90s rounds, collection/unlock meta, heavy audiovisual juice, watchable/funny moments, streak hooks.

## 3. The Site: WoopKid World

Single index.html, no libraries, mobile-first.

- Hero: animated WoopKid mascot (canvas or CSS), bold headline, floating shapes, subtle parallax. Vibrant playground direction: saturated colors, chunky rounded shapes, bouncy easing (easeOutBack), Nunito ExtraBold.
- Game cards: each card has its own accent color, an animated micro-preview of the mechanic (CSS/canvas loop), a big PLAY button, and the player's personal best pulled from localStorage. Cards bounce on hover/touch.
- Sticker album strip: horizontal shelf showing earned stickers (one per game milestone) and silhouettes of unearned ones. Tapping a silhouette deep-links to that game.
- Category chips: Quick Play, Puzzle, Action, 2 Players, Chill. Filter is instant, no page reload.
- Footer: the brand promise. No ads. No tracking. Free forever.
- Performance: zero external requests except Google Fonts, total page weight under 200KB excluding fonts.

## 4. The Moat: Shared Player Profile (localStorage)

Key: `woopkid_profile`. Every game reads/writes it in addition to its own `woopkid_<game>` key.

```json
{
  "totalPlays": 0,
  "games": { "<slug>": { "best": 0, "plays": 0, "lastPlayed": null } },
  "stickers": ["<slug>-bronze", "<slug>-silver", "<slug>-gold"],
  "streak": { "current": 0, "best": 0, "lastDay": null }
}
```

- Stickers: each game defines 3 milestone thresholds (bronze/silver/gold). Earning one triggers an in-game celebration and appears on the hub shelf.
- Daily streak: any game played today increments the streak. Hub shows it with a flame icon.
- All client-side. No accounts, no network calls.

## 5. The Roster (15 games)

Five rebuilds of existing concepts, ten new games from research. All games: single-file HTML, vanilla JS + Canvas, procedural Web Audio, 60fps delta-time loop, touch-first with mouse/keyboard fallback, per the cross-game standards carried over from the previous package (docs/game-design/00-cross-game-standards.md).

| # | Slug | Name | Genre / Inspiration | Status | Complexity |
|---|------|------|--------------------|--------|------------|
| 1 | pets-clicker | Woop Pets Clicker | Meme clicker + idle, 12 silly original pets | New | Low |
| 2 | trap-land | Trap Land | Troll platformer (Level Devil lane) | New | Med |
| 3 | wing-it | Wing It | One-tap flyer (Flappy lane) | New | Low |
| 4 | speed-slope | Speed Slope | Endless downhill ball (Slope lane) | New | Med |
| 5 | road-hopper | Road Hopper | Endless crosser + character unlocks (Crossy lane) | New | Med |
| 6 | noodle-arena | Noodle Arena | Snake io arena vs smart bots, fake live leaderboard | New | Med |
| 7 | sky-stack | Sky Stack | Tap-timing tower stacker | New | Low |
| 8 | beat-bounce | Beat Bounce | Rhythm one-tap dash with % progress (Geometry Dash lane) | New | Med |
| 9 | slice-rush | Slice Rush | Satisfying physics slicer (Slice Master lane) | New | Med |
| 10 | bubble-tank-duel | Bubble Tank Duel | Same-screen 2-player maze duel, kid-safe paintballs | New | Med |
| 11 | merge-drop | Merge Drop | Suika physics merge | Rebuild | Med |
| 12 | tap-rush | Tap Rush | Endless runner | Rebuild | Med |
| 13 | drift-collect | Drift & Collect | Hold-to-steer racer | Rebuild | Med |
| 14 | color-pop | Color Pop | Bubble shooter | Rebuild | Med |
| 15 | block-stax | Block Stax | Falling blocks (renamed from Tetris; that name is trademarked and this repo is public) | Rebuild | Med |

Bench (wave 3 candidates, not in scope now): Pop-It Fidget, Daily Kids Puzzle, Rainbow Obby, Draw-Legs Racer, Blob Arena, Mini Mart Tycoon.

Rebuild policy: old game code in ~/Desktop/WoopKid-Games-Complete-Package is reference only. Rebuilds are rewritten to the new visual bar, new shared-profile integration, and the retention recipe, keeping the proven mechanics and the lessons in tasks/lessons.md (for example: local juice instead of full-screen flashes in Color Pop).

## 6. Per-Game Retention Contract

Every game must ship with all of these or it does not ship:

1. Restart in under 1 second from game over.
2. One primary score number, visible at all times, spoken size ("I got 47").
3. Near-miss feedback: show distance to personal best on death when within 20%.
4. Bronze/silver/gold sticker thresholds registered in the shared profile.
5. Juice pass: particles, squash and stretch, screen shake (subtle), procedural sound with pitch randomization.
6. A funny or watchable moment (death comedy, chaos physics, or celebration) that makes a spectator want a turn.
7. Playable by a 6-year-old without instructions; challenging for a 12-year-old.

## 7. Technical Standards

Carried over from the existing cross-game standards doc, which moves into this repo at docs/game-design/00-cross-game-standards.md. Key points: single HTML file per game, no libraries, Canvas 2D with alpha:false, 60fps delta-time clamped loop, object pooling, Web Audio only, localStorage persistence, SEO + JSON-LD tags per game, back button to hub (relative link, not hardcoded woopkid.com, so the GitHub Pages URL works before DNS moves).

Deviation from old standards: the back button targets the hub at ../../index.html (relative), and each game additionally writes the shared woopkid_profile key.

## 8. Repo and Deployment

- Local path: /Users/ronkimhi/Documents/woopkid-games/
- GitHub: Ronkimhi/woopkid-games (public), GitHub Pages from main branch root, same pattern as Ronkimhi/stavtheodor.
- Structure: index.html at root, games/<slug>/index.html per game, docs/ for specs and design docs.
- woopkid.com DNS can point at Pages later; nothing in the code depends on the domain.

## 9. Build Order

Wave 1 (ship, then Ron review): WoopKid World site + Woop Pets Clicker + Trap Land + Wing It.
Wave 2a: Speed Slope, Road Hopper, Noodle Arena, Sky Stack.
Wave 2b: Beat Bounce, Slice Rush, Bubble Tank Duel.
Wave 2c (rebuilds): Merge Drop, Tap Rush, Drift & Collect, Color Pop, Block Stax.

Each game: build, self-QA against the checklist in the standards doc plus the retention contract above, browser-verify, then commit.

## 10. Out of Scope

- Real multiplayer, accounts, server-side anything.
- Licensed IP names or assets.
- Ads, analytics, tracking of any kind on game pages (GA can be added to the hub later if Ron asks).
- App store packaging.
