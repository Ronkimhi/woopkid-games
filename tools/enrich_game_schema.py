#!/usr/bin/env python3
"""Idempotently enrich every game page's VideoGame JSON-LD and add a noscript fallback.

Run from repo root after adding a game: python3 tools/enrich_game_schema.py
"""
import json
import re
import glob

MULTIPLAYER_SLUGS = {'bubble-tank-duel'}


def enrich(path):
    slug = path.split('/')[1]
    src = open(path).read()
    changed = False
    for pre, body, post in re.findall(
            r'(<script type="application/ld\+json">)(.*?)(</script>)', src, re.S):
        data = json.loads(body)
        t = data.get('@type')
        types = t if isinstance(t, list) else [t]
        if 'VideoGame' not in types:
            continue
        before = json.dumps(data, sort_keys=True)
        data.setdefault('inLanguage', 'en')
        data.setdefault('isAccessibleForFree', True)
        data.setdefault('contentRating', 'Everyone')
        data.setdefault('audience', {
            "@type": "PeopleAudience", "suggestedMinAge": 5, "suggestedMaxAge": 12})
        data.setdefault('playMode',
                        'MultiPlayer' if slug in MULTIPLAYER_SLUGS else 'SinglePlayer')
        data.setdefault('isFamilyFriendly', True)
        if json.dumps(data, sort_keys=True) != before:
            src = src.replace(pre + body + post,
                              pre + '\n' + json.dumps(data, indent=4) + '\n' + post)
            changed = True
    if '<noscript>' not in src:
        desc = re.search(r'<meta name="description" content="([^"]*)"', src)
        ns = ('\n<noscript><p>' + (desc.group(1) if desc else '') +
              ' This game needs JavaScript to run. '
              '<a href="https://woopkid.com/">See all the free ad-free games '
              'at WoopKid World</a>.</p></noscript>')
        src = re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + ns, src, count=1)
        changed = True
    if changed:
        open(path, 'w').write(src)
        print(slug, 'updated')


if __name__ == '__main__':
    for p in sorted(glob.glob('games/*/index.html')):
        enrich(p)
    print('done')
