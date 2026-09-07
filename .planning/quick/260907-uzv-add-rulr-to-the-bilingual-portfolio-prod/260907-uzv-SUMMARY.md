---
quick_id: 260907-uzv
title: Add RULR to the bilingual portfolio
date: 2026-09-07
status: complete
commit: none
---

# Outcome

RULR is the twelfth portfolio product and fifth game. Both homepage languages now include its verified local icon, product-network tile, Games-filter card and preferred official destination, https://rulr.lol/.

The shared menu and both portfolio indexes link to `/products/rulr/` and `/tr/urunler/rulr/`. The new localized pages include reciprocal language links, canonical URLs, VideoGame structured data, capabilities, participation boundaries and FAQs grounded in the official home and FAQ pages. Content describes fictional game status without implying real-world country ownership or investment returns.

README, homepage metadata, product statistics, sitemap, central registry and test expectations were synchronized. The current hub inventory is 28 canonical routes: two roots, two indexes and twelve bilingual product pairs. RULR's sitemap URL remains null because the public `/sitemap.xml` returns 404; its robots URL is reachable.

# Verification

- `python3 -m unittest discover -s scripts/tests`: 57 tests passed. Timeout findings printed by two intentional failure-path fixtures are expected; the suite exits successfully.
- `node --check script.js`: passed.
- `git diff --check`: passed.
- Registry validation: passed with no findings (`/tmp/buhane-rulr-registry.json`).
- Buhane source validation: the same nine pre-existing banner metadata findings before and after this change, with no new findings. Baseline and final evidence: `/tmp/buhane-rulr-source-before.json` and `/tmp/buhane-rulr-source-after.json`.
- Playwright/Chrome checks at 1440x1000 and 390x844 for English and Turkish: passed. Checked 12 cards/map tiles, totals 12/4/5/3, five visible Games cards, no map-tile overlap, RULR menu and index navigation, localized canonical URLs, reciprocal language navigation, local image loading, FAQ expansion and no detail-page horizontal overflow. No local HTTP or JavaScript failures.
- Screenshots visually checked for map, card and detail layout; browser evidence is in `/tmp/buhane-rulr-browser/`, with `results.json` recording four successful locale/viewport combinations. The temporary server and browser were closed after verification.

# Scope And Remaining Issues

Existing uncommitted redesign, signature and Google Play banner work was preserved. The nine existing source findings concern missing metadata in `email-signature/` and `google-play-developer/`; they were not hidden or modified by this task. No RULR product-source code, external account, deployment or remote Git state was changed. This request did not include committing or pushing.
