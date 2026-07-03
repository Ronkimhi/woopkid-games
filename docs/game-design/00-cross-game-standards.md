# WoopKid Games — Cross-Game Standards

> These standards apply to ALL five WoopKid games. Every game must comply with every item below. No exceptions.

---

## 1. Brand Promise

- **No mid-game ads.** Ever. This is WoopKid's core brand differentiator. Games are pure, uninterrupted play experiences.
- **No pay-to-win.** All unlockables are earned through play. No premium currency, no gates.
- **Kid-safe.** No violence beyond cartoon reactions, no dark themes, no external links except the woopkid.com back button.

---

## 2. Platform & Technology

| Requirement | Specification |
|-------------|---------------|
| **Format** | Single HTML file with embedded CSS and JS |
| **Libraries** | None. Pure vanilla JS. No CDN dependencies. |
| **Rendering** | HTML5 Canvas (2D context) |
| **Target FPS** | 60fps via `requestAnimationFrame` |
| **Movement** | Delta-time based (`dt` clamped to 50ms max) |
| **Storage** | `localStorage` for high scores, unlocks, preferences |
| **Font** | Google Fonts: Nunito (Bold 700, ExtraBold 800). Loaded asynchronously with fallback to system sans-serif. |

### Canvas Setup

```javascript
const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d', { alpha: false });
```

- `alpha: false` — skip compositing with page background (significant perf gain)
- Cap `devicePixelRatio` at 2 on mobile to balance quality vs. performance
- Responsive sizing: fill viewport, maintain aspect ratio where needed

---

## 3. Input Handling

### Touch (Primary)
- Listen to `touchstart`, `touchmove`, `touchend` on the canvas
- Always use `e.touches[0]` — ignore additional touch points (kids grab phones with both hands)
- Call `e.preventDefault()` on all touch events to prevent scrolling
- Respond on `touchstart` (NOT `touchend`) for actions — eliminates 50-150ms of latency

### Mouse (Desktop Fallback)
- `mousedown`, `mousemove`, `mouseup` mapped to same handlers as touch
- No hover-dependent mechanics

### Keyboard (Desktop Enhancement)
- Game-specific keys (spacebar for jump, arrows for movement, etc.)
- Never required — all games must be fully playable with touch only

### Input Latency Target
- < 16ms (1 frame) from input to visual response
- < 40ms maximum acceptable latency

---

## 4. UI Screens

### Start Screen
- Game name in large Nunito ExtraBold
- Visual hint of the game mechanic (animated preview or static illustration)
- "TAP TO PLAY" or "CLICK TO START" — large, centered, pulsing animation
- No menus, no options, no clutter. One tap to play.

### In-Game HUD
- Score: top-center, Nunito Bold, large enough to read at a glance
- Game-specific indicators (combo, level, next piece, etc.): positioned per game spec
- Pause: tiny icon (48x48px) in top-right corner. Tap to pause, tap again to resume.
- No other buttons during gameplay

### Game Over Screen
- **Score** — current run, prominently displayed
- **High Score** — personal best from localStorage
- **"NEW BEST!"** indicator when high score is broken (animated, celebratory)
- **Game-specific stats** (distance, level, merges, etc.)
- **"PLAY AGAIN"** — big button, centered, impossible to miss. Minimum 60x60px touch target.
- **Instant restart** — tap PLAY AGAIN → playing within 500ms. Zero friction.

### Back Button
- Top-left corner of every screen (start, in-game, game over)
- Links to `https://woopkid.com`
- Simple "←" or "✕" icon, 48x48px touch target
- Does NOT interrupt gameplay without confirmation if in-game

---

## 5. Performance Standards

### Frame Budget (16.67ms at 60fps)
| Phase | Budget |
|-------|--------|
| Update logic | < 4ms |
| Render | < 8ms |
| Overhead | < 4.67ms |

### Optimization Techniques (Required)
- **Object pooling**: Pre-allocate all particles, projectiles, obstacles. Never create/destroy during gameplay.
- **Integer coordinates**: `x = x | 0` before all `ctx` draw calls (avoids sub-pixel anti-aliasing)
- **Batch draw calls**: Group by `fillStyle`/`strokeStyle`, minimize `beginPath()` calls
- **Layered canvases**: Separate slow-updating backgrounds from fast-updating game objects
- **Avoid expensive operations**: No `shadowBlur`, no `filter`, no complex gradients in the game loop
- **Delta-time clamping**: `dt = Math.min(0.05, (now - last) / 1000)` — prevents physics explosion on tab-resume

### Game Loop Pattern

```javascript
let last = performance.now();

function loop(now) {
    const dt = Math.min(0.05, (now - last) / 1000);
    last = now;
    
    update(dt);
    render();
    
    requestAnimationFrame(loop);
}

requestAnimationFrame(loop);
```

---

## 6. Audio Standards

### Technology
- **Web Audio API only** — no audio files, no `<audio>` elements
- All sounds procedurally generated using `OscillatorNode`, `GainNode`, and noise generators
- Zero download size for audio

### Browser Autoplay Policy
- `AudioContext` must be created/resumed on first user interaction (tap/click)
- Store a single shared `AudioContext` instance
- Resume context on each user interaction: `if (audioCtx.state === 'suspended') audioCtx.resume()`

### Sound Design Principles
- **Pitch randomization**: ±5% on all repeated sounds to prevent robotic repetition
- **Concurrent sound limit**: Max 4-6 simultaneous sounds to prevent cacophony
- **Volume**: Moderate default. Kids play in public. Include a visible mute button.
- **Tone**: Upbeat, satisfying, never scary. Death sounds are "sad trombone," not horror.
- **No music loops**: Procedural sound effects only. Background music is optional and secondary.

### Mute Control
- Mute icon in the pause menu or HUD corner
- Persist mute preference in localStorage
- Default: sound ON

---

## 7. Visual Design Standards

### Color Principles
- **High contrast**: All interactive elements clearly distinguishable from background
- **Bold, saturated colors**: Kids respond to vibrancy
- **Dark backgrounds**: `#1a1a2e` or similar deep navy as default
- **Accessibility**: Never rely on color alone for game mechanics. Add shapes, patterns, or size as secondary indicators.

### Typography
- **Font**: Nunito (Google Fonts)
- **Weights**: Bold (700) for body text, ExtraBold (800) for titles and scores
- **Loading**: Async with system sans-serif fallback

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@700;800&display=swap" rel="stylesheet">
```

### Animation Principles
- **Easing**: Nothing starts or stops instantly. Use easing functions (easeOutBack, easeOutBounce, easeOutQuad)
- **Squash & stretch**: Apply to characters and objects on impact/launch
- **Particles**: Every significant action produces particles. Pool them. Cap at 50-100.
- **Screen shake**: Use trauma system (intensity = trauma², decay over time). Always subtle for kids. Optional disable.

---

## 8. Retention Design

### Personal Best (Every Game)
- Store high score in localStorage
- Display prominently on game over
- Show "NEW BEST!" with celebration animation when broken
- Show comparison: "Your best: X — This run: Y"

### Near-Miss Psychology
- When the player dies close to their personal best, emphasize proximity: "SO CLOSE! Only 58 points away!"
- When close to a milestone, show progress: "47/50 coins to unlock!"

### Instant Restart
- Death → game over screen → PLAY AGAIN → playing in < 1 second total
- The game over screen is a speed bump, not a wall

### Session Design
- No natural stopping points during gameplay (no level-end screens, no loading)
- Each game's "run" lasts 2-15 minutes — short enough for one more
- The game over screen is the only break point

---

## 9. SEO & Metadata (Every Game)

### Required HTML Tags

```html
<title>Game Name — WoopKid</title>
<meta name="description" content="Play Game Name free online! [2-3 sentence description]. No ads, kid-safe.">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<link rel="canonical" href="https://woopkid.com/games/game-slug">
```

### JSON-LD Schema (Every Game)

```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "VideoGame",
    "name": "Game Name",
    "description": "Game description",
    "url": "https://woopkid.com/games/game-slug",
    "genre": "Casual",
    "gamePlatform": ["Web Browser", "Mobile Web"],
    "applicationCategory": "Game",
    "operatingSystem": "Any",
    "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
    },
    "author": {
        "@type": "Organization",
        "name": "WoopKid",
        "url": "https://woopkid.com"
    }
}
</script>
```

### Mobile Meta Tags

```html
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="theme-color" content="#1a1a2e">
```

---

## 10. localStorage Schema

Each game stores data under a namespaced key:

```javascript
const STORAGE_KEY = 'woopkid_gamename';

const defaultData = {
    highScore: 0,
    totalPlays: 0,
    totalCoins: 0,
    unlocks: [],
    muted: false,
    lastPlayed: null,
};

function loadData() {
    try {
        return JSON.parse(localStorage.getItem(STORAGE_KEY)) || { ...defaultData };
    } catch {
        return { ...defaultData };
    }
}

function saveData(data) {
    try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    } catch {
        // localStorage full or unavailable — fail silently
    }
}
```

---

## 11. State Machine Pattern

Every game uses a simple state machine:

```javascript
const State = {
    MENU: 'menu',
    PLAYING: 'playing',
    PAUSED: 'paused',
    GAME_OVER: 'gameOver',
};

let currentState = State.MENU;

function update(dt) {
    switch (currentState) {
        case State.MENU: updateMenu(dt); break;
        case State.PLAYING: updateGame(dt); break;
        case State.PAUSED: break;
        case State.GAME_OVER: updateGameOver(dt); break;
    }
}

function render() {
    switch (currentState) {
        case State.MENU: renderMenu(); break;
        case State.PLAYING: renderGame(); break;
        case State.PAUSED: renderPause(); break;
        case State.GAME_OVER: renderGameOver(); break;
    }
}
```

---

## 12. File Structure

```
woopkid-games/
├── docs/
│   ├── game-design/
│   │   ├── 00-cross-game-standards.md    ← This document
│   │   ├── 01-tap-rush.md
│   │   ├── 02-merge-drop.md
│   │   ├── 03-drift-collect.md
│   │   ├── 04-color-pop.md
│   │   └── 05-tetris.md
│   └── research/
│       └── (research findings per game)
├── games/
│   ├── tap-rush/
│   │   └── index.html               ← Single-file game
│   ├── merge-drop/
│   │   └── index.html
│   ├── drift-collect/
│   │   └── index.html
│   ├── color-pop/
│   │   └── index.html
│   └── tetris/
│       └── index.html
└── README.md
```

---

## 13. Quality Checklist (Before Shipping Any Game)

- [ ] Runs at 60fps on a mid-range Android phone (Samsung Galaxy A series)
- [ ] All inputs work: touch, mouse, keyboard
- [ ] No input lag perceptible to the player
- [ ] Sound works on first interaction, mute toggle works
- [ ] High score persists across browser sessions
- [ ] Game over → Play Again → playing in < 1 second
- [ ] Back button navigates to woopkid.com
- [ ] No console errors
- [ ] No memory leaks (play 20+ rounds without degradation)
- [ ] SEO tags present and correct
- [ ] Font loads gracefully with fallback
- [ ] Looks good in portrait AND landscape on phone
- [ ] No ads, no tracking, no external requests (except Google Fonts)
- [ ] A 6-year-old can figure out how to play without instructions
- [ ] A 12-year-old finds it challenging enough to keep playing
