# WoopKid World Wave 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship the WoopKid World hub site plus three flagship games (Woop Pets Clicker, Trap Land, Wing It) to GitHub Pages.

**Architecture:** Static site, no build step. One index.html hub at repo root, one self-contained index.html per game under games/<slug>/. Games share a copy-pasted WoopProfile module (localStorage) that powers the hub's sticker album, bests, and daily streak. Spec: docs/superpowers/specs/2026-07-02-woopkid-world-design.md. Standards: docs/game-design/00-cross-game-standards.md.

**Tech Stack:** Vanilla JS, Canvas 2D, Web Audio API, localStorage, Google Fonts (Nunito). Nothing else.

**Verification:** No unit-test harness exists or is wanted for single-file canvas games. Every task verifies via: (1) `node --check` on extracted JS is impractical for inline scripts, so use `python3 -m http.server` + browser preview tools; (2) zero console errors; (3) the acceptance checklist in each task. Playwright/preview snapshot + click-through is the test.

**Global rules for every task:**
- No em dashes or en dashes anywhere, including code comments and UI strings.
- Mobile-first: touch handled on touchstart, e.preventDefault, works one-thumb portrait.
- 60fps loop: `dt = Math.min(0.05, (now-last)/1000)`, object pooling for particles.
- Back button top-left on every screen links to `../../index.html`.
- Commit after each task with a descriptive message.

---

## Shared Module: WoopProfile (copy into every game and the hub)

This exact code block is pasted into each game's script (and the hub uses the same key). It is the contract; do not rename keys.

```javascript
const WoopProfile = {
  KEY: 'woopkid_profile',
  load() {
    try { return JSON.parse(localStorage.getItem(this.KEY)) || this._blank(); }
    catch { return this._blank(); }
  },
  _blank() {
    return { totalPlays: 0, games: {}, stickers: [], streak: { current: 0, best: 0, lastDay: null } };
  },
  save(p) { try { localStorage.setItem(this.KEY, JSON.stringify(p)); } catch {} },
  // Call once per finished run. slug: game slug. score: the run's primary number.
  // thresholds: {bronze, silver, gold} score values for stickers.
  reportRun(slug, score, thresholds) {
    const p = this.load();
    p.totalPlays++;
    const g = p.games[slug] || (p.games[slug] = { best: 0, plays: 0, lastPlayed: null });
    g.plays++;
    g.lastPlayed = new Date().toISOString().slice(0, 10);
    if (score > g.best) g.best = score;
    const earned = [];
    for (const tier of ['bronze', 'silver', 'gold']) {
      const id = slug + '-' + tier;
      if (score >= thresholds[tier] && !p.stickers.includes(id)) { p.stickers.push(id); earned.push(tier); }
    }
    const today = new Date().toISOString().slice(0, 10);
    if (p.streak.lastDay !== today) {
      const y = new Date(Date.now() - 86400000).toISOString().slice(0, 10);
      p.streak.current = (p.streak.lastDay === y) ? p.streak.current + 1 : 1;
      if (p.streak.current > p.streak.best) p.streak.best = p.streak.current;
      p.streak.lastDay = today;
    }
    this.save(p);
    return earned; // array of tier names newly earned this run, show celebration per tier
  }
};
```

Idle-game exception (Pets Clicker): call `reportRun` on meaningful checkpoints (each new pet unlocked) rather than on a "game over" which never happens.

---

### Task 1: Repo scaffold + GitHub repo + Pages

**Files:**
- Create: `README.md`, `.gitignore`
- Repo: `Ronkimhi/woopkid-games` (public), Pages from main branch root

- [ ] **Step 1:** Write `README.md`: project one-liner, roster table from spec, local dev (`python3 -m http.server 8766`), deploy notes (Pages, main branch), no-build-step statement. `.gitignore`: `.DS_Store`.
- [ ] **Step 2:** `gh repo create Ronkimhi/woopkid-games --public --source=. --push` (verify gh auth as Ronkimhi first with `gh auth status`; this is Ron's personal account, same as stavtheodor).
- [ ] **Step 3:** Enable Pages: `gh api repos/Ronkimhi/woopkid-games/pages -X POST -f "source[branch]=main" -f "source[path]=/"` (or via PUT if exists).
- [ ] **Step 4:** Commit and push. Verify `https://ronkimhi.github.io/woopkid-games/` returns the README-era 404 or content within a few minutes (fine if it 404s until index.html lands in Task 2).

### Task 2: WoopKid World hub site

**Files:**
- Create: `index.html` (the entire hub: CSS + JS inline)

Design (vibrant playground, per spec section 3):
- Palette: deep sky `#4A2FBD` to `#7B4DFF` gradient background alternative REJECTED; use bright playground: background cream `#FFF6E9`, ink `#2B2350`, accents per game. Chunky rounded cards (border-radius 28px+), thick soft shadows, Nunito 800/900.
- Hero: "WoopKid World" wordmark with per-letter bounce-in (CSS animation, staggered delays), tagline "Free games. No ads. Just play." Floating background blobs/shapes drifting slowly (CSS keyframes, GPU-cheap transforms only). A simple canvas mascot: a round bouncing character with eyes that follow the pointer (one small canvas, <80 lines).
- Streak flame + total stickers count pill in the header, read from WoopProfile.
- Game grid: 15 card slots. Wave 1 games are playable; the other 12 render as "COMING SOON" cards with their name, genre, and a padlock that wiggles on tap. Each card: accent color, emoji-based icon (no image assets), animated micro-preview (tiny CSS animation suggesting the mechanic, for example a flapping wing for Wing It), personal best chip ("Best: 47") from WoopProfile, PLAY button.
- Category chips: All, Quick Play, Action, Puzzle, 2 Players, Chill. Instant JS filter, cards animate in/out with scale.
- Sticker shelf: horizontal scroll strip, gold/silver/bronze sticker circles for earned (emoji + tier ring), gray silhouettes for unearned. Tap silhouette navigates to that game.
- Footer brand promise + "Built with love, zero ads, zero tracking."
- SEO: title, description, canonical `https://woopkid.com/`, JSON-LD WebSite, theme-color, apple-mobile-web-app tags.

- [ ] **Step 1:** Build `index.html` per above. Card data as a JS array (slug, name, genre, category, accent, emoji, playable flag, milestone thresholds for the best-chip label).
- [ ] **Step 2:** Serve locally, verify with browser tools: snapshot shows all 15 cards, chips filter, no console errors, mobile viewport (375px) has no horizontal scroll, cards are tappable size.
- [ ] **Step 3:** Seed a fake profile in localStorage via console, reload, verify best-chips, streak flame, and sticker shelf render earned state.
- [ ] **Step 4:** Commit "Add WoopKid World hub".

### Task 3: Wing It (one-tap flyer)

**Files:**
- Create: `games/wing-it/index.html`

Mechanic spec:
- A round chick with tiny wings. Tap/click/space = flap (velocity = -320 px/s at 720-unit logical height). Gravity 1100 px/s^2. Max fall speed 620 px/s. Bird tilts with velocity (-25deg to +70deg).
- Obstacles: candy-striped pipes, gap 235 logical px shrinking to 190 by score 30 (never below). Horizontal speed 175 px/s rising to 240 by score 50. Spacing 300 px.
- Score +1 per pipe passed, big center-top number. Coins (optional star pickup between some gaps) worth nothing but a sparkle + sound, pure juice.
- Death: hit pipe or floor. Squash bird, feather-burst particles, slow-mo 250ms, sad-trombone-ish descending procedural blip. NEVER a harsh flash.
- Near-miss: if score within 20% of best (and best >= 5), game over shows "SO CLOSE! X away from your best".
- Ground scrolls; parallax clouds; day palette (sky `#8FD8FF`, grass `#7ED957`), accent orange `#FF8A3D`.
- Stickers: bronze 10, silver 25, gold 50. `WoopProfile.reportRun('wing-it', score, {bronze:10, silver:25, gold:50})` on death. Sticker earn = confetti burst + "STICKER EARNED!" banner on the game over panel.
- Start screen: bird idle-bobbing, "TAP TO FLAP". First tap starts play immediately (that tap is also the first flap). Game over panel: score, best, NEW BEST celebration, PLAY AGAIN (restart < 1s), back button.

- [ ] **Step 1:** Build the game per spec + cross-game standards (state machine, pooling, Web Audio helper with pitch randomization, mute toggle persisted, SEO tags, JSON-LD).
- [ ] **Step 2:** Browser-verify: play 3+ runs via preview tools (programmatic taps), confirm scoring, death, instant restart, no console errors, localStorage keys `woopkid_wing-it` + `woopkid_profile` update.
- [ ] **Step 3:** Verify hub integration: after a run, hub shows the best chip and any sticker.
- [ ] **Step 4:** Commit "Add Wing It".

### Task 4: Woop Pets Clicker (meme clicker + idle)

**Files:**
- Create: `games/pets-clicker/index.html`

Mechanic spec:
- Center stage: current pet, a big squishy tappable canvas character. Tap = +tapPower Woops (currency), pet squashes, floating "+N" text, particle pop, pitch-randomized boing. Rapid taps build a combo meter (x2 at 10 taps/2s, x3 at 25) shown as a rainbow bar.
- 12 original silly pets, unlocked in order by total Woops earned: Blobby (0), Speedy Snail (500), Disco Chick (2.5K), Moustache Fish (10K), Banana Cat (40K), Grandpa Frog (150K), Ninja Potato (600K), Space Slug (2.5M), Karate Cloud (10M), Robo Pug (50M), Golden Llama (250M), THE WOOP (1B). Each has a distinct canvas-drawn look (procedural shapes, no images), idle animation, and unique tap sound flavor.
- Shop panel (slide-up drawer): upgrades. Tap Power (+1, cost curve 15 * 1.6^n), Auto-Paw (1/s, 100 * 1.7^n), Pet Feeder (8/s, 1.2K * 1.75^n), Woop Machine (50/s, 15K * 1.8^n), Party Cannon (300/s, 200K * 1.85^n). Standard big-number formatting (1.2K, 3.4M, 1B).
- Offline earnings: on load, grant idleRate * min(elapsed, 8h) with a "While you were away" popup.
- Every pet unlock: full-screen confetti + fanfare + the pet struts in. `WoopProfile.reportRun('pets-clicker', totalWoopsEarned, {bronze:10000, silver:2500000, gold:1000000000})` called at each unlock and every 60s autosave.
- Persistence in `woopkid_pets-clicker`: woops, totalEarned, upgrade counts, unlocked pets, lastSeen. Autosave every 5s and on visibilitychange.
- No game over. Back button + mute. Number formatting everywhere. HUD: Woops count huge at top, per-second rate under it.

- [ ] **Step 1:** Build per spec (DOM+canvas hybrid allowed: canvas pet stage, DOM shop list for scrollability).
- [ ] **Step 2:** Browser-verify: tap grants and combo work, buy each upgrade type, rate ticks, reload preserves state, offline popup appears after faking lastSeen in localStorage, no console errors.
- [ ] **Step 3:** Commit "Add Woop Pets Clicker".

### Task 5: Trap Land (troll platformer)

**Files:**
- Create: `games/trap-land/index.html`

Mechanic spec:
- Side-view platformer, fixed single-screen rooms (no camera scroll), 12 handcrafted levels. Player: a marshmallow blob with worried eyes. Controls: left/right + jump. Touch: left half hold = walk toward touch side using two on-screen zones (left/right arrows bottom-left, jump button bottom-right, 64px+); Keyboard: arrows/WASD + space.
- Physics: run 220 px/s, jump velocity -520, gravity 1400, coyote time 90ms, jump buffer 120ms. Deaths are instant, respawn same level < 400ms, death counter per level shown cheekily ("Oops x7").
- THE POINT IS THE TROLLS. Each level contains 1-3 scripted betrayals: floors that vanish when approached, doors that slide away, fake exits, spikes that pop from safe-looking ground, a platform that flips, gravity reversal room, an exit that runs from you once. Traps must be FUNNY not unfair: telegraph 150ms before killing, cartoonish pop + "BONK" style wobble text on death, never repeat identical trap twice.
- Level select unlocks linearly; progress in `woopkid_trap-land` (levelsCleared, totalDeaths). Score for profile = levels cleared (max 12). `WoopProfile.reportRun('trap-land', levelsCleared, {bronze:3, silver:7, gold:12})` on every level clear.
- End screen after level 12: big celebration + total deaths stat ("You died 143 times and STILL won").
- Palette: sunny meadow that lies to you (bright green grass `#6FDB6F`, sky `#A8E4FF`, danger pink `#FF5FA2`).

- [ ] **Step 1:** Build engine: tile-free rect-based level format (arrays of platforms, spikes, triggers, exit), trap trigger system (proximity/timer/onLand hooks), player physics with coyote/buffer.
- [ ] **Step 2:** Build the 12 levels with escalating troll creativity. Level 1 is honest (teaches controls), level 2 first betrayal.
- [ ] **Step 3:** Browser-verify: complete levels 1-3 programmatically or via keyboard automation, verify respawn speed, death counter, trap telegraphs, profile updates, no console errors.
- [ ] **Step 4:** Commit "Add Trap Land".

### Task 6: Wave 1 QA + deploy

- [ ] **Step 1:** Full QA pass against the standards checklist (docs/game-design/00-cross-game-standards.md section 13) + retention contract (spec section 6) for all three games: mobile viewport, restart timing, mute persistence, SEO tags, sticker flow, back buttons.
- [ ] **Step 2:** Update hub: mark the three games playable (if not already), verify best-chips and stickers reflect real play.
- [ ] **Step 3:** Push to GitHub, verify Pages deploy live at `https://ronkimhi.github.io/woopkid-games/`, click through every game on the live URL.
- [ ] **Step 4:** Log the deliverable in `~/Documents/ron-brain/the-system-v8-ron/B-brain/06-deliverables/deliverables-index.md` per system rule.
- [ ] **Step 5:** Report to Ron: live URL, what shipped, what's next (Wave 2a).

---

## Self-review notes

- Spec coverage: site (Task 2), shared profile (module block, used Tasks 3-5), flagship trio (Tasks 3-5), deploy + Pages (Tasks 1, 6), retention contract enforced in Task 6 QA. Waves 2a-2c intentionally out of this plan (separate plans after Ron's Wave 1 review).
- No placeholders: every game task carries full tuning constants and content lists (12 pets, 12 levels, sticker thresholds).
- Naming consistency: slugs match spec table exactly (wing-it, pets-clicker, trap-land); WoopProfile key names match spec section 4.
