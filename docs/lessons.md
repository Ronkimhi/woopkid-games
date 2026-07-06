# Lessons

## Rope Rush Swing Physics And Fairness

- One-button swing games live or die on the pendulum: fixed-timestep physics (120Hz), a one-sided rope constraint (constrain only when taut), slow reel-in for energy, and momentum-conserving tangential release. Tune these before building any levels.
- A swing "auto-pump" must amplify the player's current swing direction (fall back to forward push only from a dead hang). Naively pushing along the "forward" tangent fights the upswing on the launch side and caps swing energy — the game feels dead and nobody can tell why.
- Guard against degenerate input states explicitly: dead-hang (no way to build a swing), release-then-instant-regrab of the same anchor (kills every launch), and hesitation at spawn (dead before touching anything). Each needs its own mechanic: pump, per-anchor regrab cooldown, home pad.
- Never leave early-level safety to random generation. A "pad desert" rolled by RNG made level 3 brutally unfair while the same seed a week earlier was fine. Guarantee the safety rhythm structurally (pad under every saw-less gap early; runway pad before the flag) and let scarcity be an authored difficulty knob.
- Verify clearability with in-page bots driving the game's real input functions, but know their limits: a fixed-policy bot failing a level usually means the level needs adaptive timing (human skill), not that it's broken. Validate geometry invariants (max hook gap < grab range, hazards clear of anchors) across all levels programmatically instead of trusting any bot.
- An exception thrown inside render kills the rAF loop silently — the game freezes with no console spam. Negative arc radii from modulo on negative world coordinates was the culprit; abs() indices derived from world positions.

## Color Pop Pop Effects

- Avoid full-screen white flashes for routine positive feedback. They can feel harsh and obscure the board during play.
- For satisfying match/pop feedback, prefer local effects at the interaction point: colored rings, sparkles, shards, glints, particles, subtle shake, and sound.
- When aiming for "Candy Crush" style juice, make the reward colorful and object-local instead of washing out the entire screen.
- "Candy Crush-like" means layered feedback, not just more particles: soft halo, expanding shockwaves, radial rays, chunky candy shards, star glints, and a floating score label should all happen together.

## Color Pop Progression And Feel

- If a puzzle game feels too easy and long, verify the pressure mechanic is tied to the core loop. In Color Pop, row advancement must count every shot, not only misses.
- Progress should be visible during play, not only inferred from score. Show immediate counters like shots until row drop and pops until next level.
- For bubble shooter smoothness, avoid hard visual jumps on snap/cascade. Use short tweened settling, projectile substeps, and falling drift/rotation.
- Reward moments need to be reachable, not just impressive when they happen. Bias board generation and next-piece selection toward near-match opportunities so players can trigger big effects frequently.
