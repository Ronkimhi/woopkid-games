# Discoverability checklist: adding or renaming a game

LLM and search discoverability lives in several files. When a game ships, update ALL of these or crawlers see an inconsistent site.

## Files to update for every new game

1. `index.html` (hub)
   - `const GAMES` array (gameplay)
   - Static fallback `<a class="static-game">` links inside `#grid` (crawlers do not run JS; this is what they see)
   - JSON-LD `ItemList`: add ListItem, bump `numberOfItems`
2. `sitemap.xml`: add URL with `lastmod`
3. `llms.txt`: add to the games list; update the game count in the intro line
4. `llms-full.txt`: add a `### Game Name` section with description and genre; update both count mentions
5. `games.json`: add entry (slug, name, url, genre, categories, players, description)
6. The new game page itself: run `python3 tools/enrich_game_schema.py` (idempotent, safe on all pages). It adds contentRating, audience, playMode, inLanguage, isAccessibleForFree to the VideoGame JSON-LD and a `<noscript>` fallback paragraph
7. Landing pages: update the game-count mentions in `free-games-for-kids-no-ads/`, `chromebook-games-for-school/`, `games-for-5-year-olds/`, `ad-free-alternatives/` (search for the old count; do not touch `NNpx` font sizes)

## What happens automatically

- `.github/workflows/indexnow.yml` submits every sitemap URL to IndexNow (Bing, Copilot, ChatGPT search) on each push to main. No manual pinging needed.

## Rules

- Never remove the static `#grid` fallback links: the hub grid is JS-rendered and invisible to GPTBot/ClaudeBot/PerplexityBot without them
- Visible text and JSON-LD FAQ content must match (no schema for text that is not on the page)
- No hidden keyword text, no cloaking, ever
- No em dashes in copy
