All research angles are now complete (schools, parents, SEO, social/PH/HN full reports; portals from salvaged verified notes plus direct verification of GameDistribution/GamePix/Coolmath/Lagged). Synthesizing the deliverable now.

# WoopKid World — 30-Day Distribution Playbook
*Research verified 2026-07-02. All URLs checked live unless marked UNVERIFIED.*

## ⚠️ Pre-flight blockers (fix before ANY promotion)

1. **The site is currently a 404.** https://ronkimhi.github.io/woopkid-games/ returns 404: the GitHub repo (`Ronkimhi/woopkid-games`) contains only `docs/` design files, Pages is configured to serve branch `main` root where no `index.html` exists. The playable site (with per-game pages and good title tags) lives only locally in `/Users/ronkimhi/Desktop/WoopKid-Games-Complete-Package/01-playable-site/`. Push the site files and fix the Pages source — nothing below works until this ships.
2. **Skip the github.io detour — launch straight on woopkid.com.** The domain is live on Vercel with the old 5-game version. Deploy the 15-game site to woopkid.com now and never market the github.io URL: (a) shared `*.github.io` is increasingly blocked wholesale by school filters and slow to rank vs. custom domains; (b) every backlink earned in the next 30 days should point at the permanent domain; (c) a github.io URL undercuts the press story. Set up Google Search Console + sitemap on woopkid.com on day 1.
3. **Rename "Tetris."** One game page is titled "Tetris — Free Online Block Puzzle Game | WoopKid." The Tetris Company is aggressively litigious. Rename to an original name ("Block Drop" etc.) before any submission, press, or portal upload — this is a rejection/legal risk everywhere.

---

## Top 10 actions, ranked by expected traffic per effort

### 1. Ship the SEO foundation on woopkid.com (Week 1; effort: 1-2 days; impact: compounds forever)
The core wedge SERPs are verifiably weak — no major portal owns "no ads" kids queries.
- **Homepage targets:** "free games for kids no ads" (current top results: kidsplay.now, kidmons.com, kidsearch.games — all small sites; winnable in months).
- **Per-game pages** (`woopkid.com/games/slug`): unique 150-300 word description, how-to-play as FAQ, controls, age range, screenshot.
- **Schema (copy Coolmath/CrazyGames exactly, verified from their live HTML):** co-typed `"@type": ["VideoGame","WebApplication"]` + `offers.price: 0` + `aggregateRating` + `FAQPage` + `BreadcrumbList`. Google explicitly won't show rich results for `VideoGame` alone — co-typing required per https://developers.google.com/search/docs/appearance/structured-data/software-app
- **Category + age pages:** `/2-player-games/`, `/puzzle-games/`, `/age-5/`…`/age-12/` (cokogames.com proves small sites win age queries via category pages; "browser games for 6 year olds" SERP is stale 2022 listicles).
- **Technical:** XML sitemap → Search Console; OG image per game; lazy-load the canvas bundle behind a Play click so LCP is the page shell, not the game.
- **Wedge keyword list (verified-weak SERPs):** free games for kids no ads · ad free games for kids online (a Quora thread ranks!) · kid safe browser games · safe online games for kids no sign up · browser games for 6 year olds (+5/7/8 variants) · two player games for kids no download · math games for kids no ads. **Never target "unblocked games"** — brand poison, signals filter-evasion to the school IT admins you need (see #8).
- **Risk:** none. Asset needed: copy + one screenshot per game.

### 2. r/WebGames weekly posting cadence (Weeks 1-4+; effort: 30 min/week; impact: hundreds-thousands of sessions per post + backlinks)
Best-fit community; rules verified from their wiki (via Wayback):
- **Rule P3.iii: link must NOT lead to collections/directories** — post one specific game's direct URL, never the homepage. Mention "14 more at woopkid.com" in a comment.
- Title must **begin with the game's name**, use category flairs ([HTML5], [PZL], [ARC]).
- Account must be **7+ days old with 10+ comment karma** — start commenting genuinely today.
- Own-games personal site cap: **1 post/week** → your 15 games = ~15 weeks of compliant content.
- Example: `Rocket Rescue [HTML5] [ARC] — a little arcade game I made for my kids (no ads, no signup)`
- **Risk:** collection-link rule violation gets removed (unban procedure involves drawing a dinosaur — really).

### 3. Show HN — one shot, done right (Week 2-3; effort: 2 hours; impact: 0-30K visits, high variance)
Verified precedents via HN Algolia: "Show HN: Tiny logic and number games I built for my kids" — **87 pts/37 comments** (Aug 2025); Summle math game — **189 pts**. But the near-identical comp "Show HN: GameZipper – 12 Free HTML5 Browser Games (No Ads, No Login)" got **1 point** (Feb 2026). Lesson: a generic catalog pitch fails; lead with one game adults will actually play + the dad story.
- Rules (https://news.ycombinator.com/showhn.html): title starts "Show HN:", instantly playable without signup (✓), stay in comments, never solicit upvotes (voting-ring detection).
- Title: `Show HN: I built 15 browser games for my kids — no ads, no accounts, no tracking`. First comment: why (ad-riddled kids sites), stack (single-file vanilla canvas), and "start with [best game]". Post Tue-Thu ~8-9am ET.
- **Risk:** one shot only; don't fire until woopkid.com is polished and the Tetris rename is done (HN will find it in minutes).

### 4. Publish all 15 games on itch.io (Week 1-2; effort: ~half day; impact: steady discovery + real dofollow-adjacent backlinks)
Cleanest portal, verified: **"Advertisements will never be placed on any of your pages"** (itch.io FAQ), no SDK, no exclusivity, free games fully supported, links to woopkid.com allowed and encouraged in descriptions. Upload each game as an HTML5 zip at itch.io/dashboard → "Create new project" → "played in browser". Asset: cover image (630×500) per game + description linking woopkid.com. Risk: none. Secondary: **Game Jolt** (https://gamejolt.com/dashboard/games/add) — same non-exclusive/no-ads-in-build/link-backs-allowed profile, but teen/FNAF-skewed audience; do it in week 3-4 if time allows.

### 5. Listicle-inclusion outreach (Weeks 2-4; effort: 1 day of emails; impact: referral traffic + the backlinks a zero-authority domain needs)
Getting INTO the pages that already rank beats out-ranking them. Verified targets currently ranking for your wedge terms: commonsensemedia.org/lists/free-online-games-for-kids · screentimelabs.com · arcadino.com/blog/best-free-browser-games-for-kids · twozygames.com/blog · mommypoppins.com · teachingexpertise.com · kidmons-style roundups. Pitch: "genuinely ad-free, no-tracking, free, browser-only, built by a dad — here's the privacy page." Also file a Common Sense Media review suggestion (help article: commonsense.my.site.com/membersupport — form contents UNVERIFIED; reviews are editorial/unpaid, low odds, free, durable if it lands). Asset: 3-sentence pitch + screenshots + privacy policy URL. Risk: slow, ignore-rate high — volume game.

### 6. Reddit story posts: r/daddit + r/SideProject + r/playmygame (Weeks 2-4; effort: 2 hours; impact: one good r/daddit post can spike thousands of visits)
- **r/daddit** (~1M members): most receptive big parenting sub to "dad built a thing." Story-first: "I got tired of every 'free kids games' site being an ad minefield, so I built 15 ad-free browser games for my kids." Link in comments. (Rules UNVERIFIED this session — Reddit blocks automated fetch; check reddit.com/r/daddit/about/rules first.)
- **r/SideProject:** required format `WoopKid World - 15 free ad-free browser games I built for my kids`.
- **r/playmygame** (131K members): [Web] flair, one game, max 1/month, don't post-and-ghost; avoid your most clone-like games (low-effort clones get removed).
- **Do NOT post:** r/InternetIsBeautiful — verified verbatim rule: "Webgames are not allowed." r/Parenting and r/Mommit — strict no-self-promo; comment-only presence.
- **Risk:** clumsy promo burns the account; follow 90/10 participation everywhere.

### 7. TikTok/YouTube Shorts pipeline (start Week 2, judge at Week 8; effort: high, 3-5 posts/week; impact: highest ceiling of any channel)
Verified: browser games go massively viral via short-form (Infinite Craft/neal.fun; "Spend Bill Gates' Money" did 80M+ views); TikTok's "games for school / best game websites" niche is large and actively promotes sites — WoopKid is a clean, safe entrant in a niche full of sketchy proxy sites. Formats: (a) dad-POV dev story, (b) 15-30s gameplay + beatable score challenge ("my 7-year-old scored 42"), (c) "5 free browser games for kids, no app, no ads", (d) parent-targeted "screen time you don't feel bad about." Asset: screen recordings + captions; power-law returns — most videos die, one hit outdelivers everything else in this playbook. Risk: time sink; audience skews 10-16 on the "for school" angle.

### 8. School-channel groundwork (Weeks 1-4; effort: 1-2 days; impact: zero traffic in 30 days, but unlocks the biggest long-term channel)
Key verified facts: **no public filter-recategorization form exists anymore** (Lightspeed's public tool retired; Securly/GoGuardian/Linewize are customer-console-only) — the only path is teachers/IT requesting allowlists. Also verified: **Common Sense Education paused all edtech reviews as of Jan 2026** (commonsense.org/education/reviews/FAQ) — skip. And the wedge: Coolmath was flagged by Internet Safety Labs for location-based ads/COPPA problems (internetsafetylabs.org) — "the ad-free alternative to Coolmath" is your pitch.
- Ship `/teachers` (grade bands + what each game practices — ABCya's grade/subject taxonomy is the proven model), `/privacy` (no ads/tracking/accounts, COPPA posture), `/for-schools` one-page PDF with the exact domain to allowlist.
- Recruit 3-5 real teachers (one each on Lightspeed/Securly/GoGuardian districts) to use it for indoor recess and submit in-console category-review + allowlist requests.
- TeachersPayTeachers freebie: "15 Free Ad-Free Chromebook Games for Indoor Recess" PDF linking woopkid.com; submit to TpT newsletter (1 free slot/week) + Pinterest. (Check TpT external-link policy first — UNVERIFIED.)
- Pitch We Are Teachers (verified pitch page: weareteachers.com/write-for-weareteachers) and Tech & Learning's monthly "Edtech Show & Tell".
- **Timeline honesty:** first district allowlists come months 2-6; adoption is seasonal (Aug/Sep and Jan windows).

### 9. Parent press + quote pipelines (Weeks 3-4; effort: half day; impact: slow-burn authority)
- Pitch order: Cool Mom Picks/Cool Mom Tech (indie-find friendly) → Techlicious (techlicious.com/contact-us) → Protect Young Eyes → Wait Until 8th → Bark blog. Angle: villain-first ("'free kids games' sites are ad minefields; a dad rebuilt the category ad-free"), not tech-first.
- Local news reliably bites on "[City] dad builds ad-free game site for kids" — pitch after woopkid.com cutover.
- Quote pipelines for authority (verified status): HARO died Dec 2024 → now run by **Featured.com**; better signal: **Qwoted** (qwoted.com) and **Source of Sources** (Peter Shankman's free digest). Register as a "screen time / kids online safety" source.
- Asset: 100-word boilerplate + founder photo + 3 screenshots + privacy one-liner.

### 10. Product Hunt launch (Week 4+, optional; effort: 1 day; impact: modest)
Weak-moderate fit; past kids-game launches (Kidy King Games, TomoClub, Rabbit Rescue) had no breakout. Verified mechanics: only ~10% of launches get "featured" (which drives ~70% of outcome); hunters no longer matter (self-hunt); day resets 12:01am PT; all recent top launches had demo videos. Do it after HN/Reddit for the backlink + gallery presence; expect 0-2K visits. Asset: tagline, 500-char description, 3-5 gallery images, 30-60s demo video.

---

## Game-portal matrix (submission channels)

| Portal | Submit at | Ads forced into game? | Exclusivity | Link back to woopkid.com? | Traffic to your domain | Verdict |
|---|---|---|---|---|---|---|
| **itch.io** | itch.io dashboard → Create new project | **Never** ("Advertisements will never be placed on any of your pages") | None | Yes, encouraged | Yes — ranked pages, real links | **USE (first)** |
| **Game Jolt** | gamejolt.com/dashboard/games/add | No SDK/no ad injection in build | None | Yes | Modest; teen-skewed audience | **USE (secondary)** |
| **Coolmath Games** | coolmathgames.com/submit-a-game / developers.coolmathgames.com | No — they **require** games be ad-free & free of external links | Non-exclusive license (they pay to host) | No external links allowed | None (plays on their site) — it's a **revenue** channel, not traffic | **USE for licensing $ if "thinking games" fit** |
| **Y8** | y8.com/upload (note: account.y8.com path is 404) | Ads **opt-in** via AdSense-for-Platforms; build untouched if you don't opt in | None found | Restricted ("no misleading links"); page itself is ad-framed | ~None | Use with caveats / low priority |
| **Poki** | developers.poki.com | **Yes — SDK "comes out of the box with advertisements"** | Preferred deal = 5-yr web-exclusive (conflicts with woopkid.com) | Prohibited; external requests blocked | None | **SKIP** |
| **CrazyGames** | developer.crazygames.com | Basic Launch build stays clean, but page/preroll around it is ad-monetized | None (optional 2-mo opt-in) | Dev-site link allowed **only if it doesn't lead to playable games** — i.e., useless | ~None | **SKIP** |
| **GameDistribution** | gamedistribution.com/developers | **Yes — mandatory SDK with preroll + midrolls**, 33% rev share | Non-exclusive | No | None (embeds on 3rd-party ad sites) | **SKIP** |
| **GamePix** | partners.gamepix.com/developers | **Yes — SDK handles ads**, 45% share | Non-exclusive | No | None | **SKIP** |
| **Lagged** | lagged.dev | **Yes — ad-rev-share model (interstitials/rewarded)** | UNVERIFIED | UNVERIFIED | None | **SKIP** |

The ad-supported portal ecosystem is structurally incompatible with the ad-free brand: every high-traffic portal (Poki/CrazyGames/GD/GamePix/Lagged) monetizes via ads in or around your game and blocks playable-site link-backs. Hosted copies there are not a marketing channel — only itch.io and Game Jolt allow "play more on our site" linking; Coolmath is a licensing-revenue option that happens to demand exactly what you already are (ad-free, no external links, thinking games).

## Channel matrix

| Channel | Effort | Expected impact (30 days) | Timeline to impact | Constraints / risks |
|---|---|---|---|---|
| SEO foundation + wedge keywords | Med (1-2 days) | Low now, compounding | 3-6 months to rank wedge terms | Must be on woopkid.com; never touch "unblocked" |
| r/WebGames weekly | Low | Med (100s-1000s/post) | Immediate | Direct game link only (no homepage); 7-day/10-karma account; 1/week |
| Show HN | Low | High variance (0-30K) | Immediate | One shot; needs a lead game adults enjoy; catalog pitch verified to flop |
| itch.io (+Game Jolt) | Low | Low-med steady + backlinks | 1-2 weeks | None (audience fit only) |
| Listicle inclusion outreach | Med | Med (links + referral) | 2-8 weeks | High ignore rate; CSM editorial/no guarantee |
| r/daddit + r/SideProject + r/playmygame | Low | Med (spiky) | Immediate | Verify rules manually (Reddit unfetchable); story-first, 90/10 |
| TikTok/Shorts | High (3-5/wk) | Power-law; highest ceiling | 4-8 weeks to judge | Time sink; "for school" audience skews older |
| Schools (teachers, allowlist kit, TpT) | Med | ~Zero in 30 days | 2-6 months; seasonal (Aug/Jan) | No public filter recat path; CS Education reviews paused Jan 2026 |
| Parent press + Qwoted/SOS | Med | Low-med | 4-12 weeks | Needs woopkid.com + polish first |
| Product Hunt | Med | Low (0-2K) | Day-of | Only ~10% get featured; demo video required |
| Ad-based portals (Poki etc.) | — | — | — | **Off-strategy: forced ads, exclusivity, no link-backs** |

## Week-by-week sequence
- **Week 1:** Fix deployment → cut woopkid.com over to the 15-game site → rename Tetris → per-game pages/schema/sitemap/Search Console → `/privacy` + `/teachers` pages → create Reddit account and start commenting → itch.io uploads begin.
- **Week 2:** First r/WebGames post → listicle outreach emails (7 targets) → CSM review suggestion → first TikTok/Shorts posts → TpT freebie drafted.
- **Week 3:** Show HN → r/daddit story post → r/SideProject → Coolmath submission → recruit teachers → We Are Teachers / Tech & Learning pitches.
- **Week 4:** r/playmygame → Game Jolt → parent-blog pitches (Cool Mom Tech, Techlicious, Protect Young Eyes) → Qwoted/SOS registration → assess Shorts data → optional PH prep.

**Verify manually before acting (couldn't be confirmed this session):** live Reddit rules pages for r/daddit/r/WebGames (archived versions used), Common Sense Media review-request form contents, TpT external-link policy, Lagged link-back terms, and current Vercel↔GitHub Pages cutover plan for woopkid.com (Vercel currently serves the old 5-game build — decide one canonical host before submitting the sitemap).