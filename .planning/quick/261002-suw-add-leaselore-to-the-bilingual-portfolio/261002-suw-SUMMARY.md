---
quick_id: 261002-suw
title: Add LeaseLore to the bilingual portfolio
date: 2026-10-02
status: complete
commit: none
---

# Outcome

LeaseLore is the fourteenth portfolio product and fifth app. Both homepages include its original local icon, product-network tile, Apps-filter card and official website link. The shared menu and both indexes link to `/products/leaselore/` and `/tr/urunler/leaselore/`.

The localized detail pages describe address-level resident reviews, scores and confidence, saved homes and moderation. They clearly separate the available Android release from the iOS early-access request. Google Play, iOS request and support links use the official destinations. SoftwareApplication metadata identifies Android without implying a released iOS app.

Statistics, README, indexes, sitemap, registry, requirements and regression expectations are synchronized: 14 products, 5 apps, 5 games, 4 platforms/publications, 32 canonical hub routes. The last map row now shares space between Mintropolis and LeaseLore without adding another row. Existing uncommitted Mintropolis content and assets were preserved.

# Sources

- https://leaselore.com/ retrieved successfully via read-only HTTP after the web tool could not open it.
- https://leaselore.com/support.html for moderation, support and Buhane ownership.
- https://play.google.com/store/apps/details?id=com.buhane.leaselore returned the LeaseLore listing through read-only HTTP. No rating, install count or price was copied.
- The local `apps/LeaseLore/www/assets/apple-touch-icon-v2.png` was copied unchanged to `images/products/leaselore.png`; the live homepage references this original asset path.
- The live landing/support pages describe five app languages and nine listed markets. This current public evidence takes precedence over older four-language/England-first README wording.
- Public robots.txt was reachable; sitemap.xml returned 404, so the registry does not claim a sitemap URL. Product-source changes and deployment remain outside this task.

# Verification

- `python3 -m unittest discover -s scripts/tests`: 58 tests passed. Expected timeout-fixture messages do not fail the suite.
- Bundled Node `--check script.js`: passed.
- `git diff --check`: passed.
- Registry validation: no findings (`/tmp/buhane-leaselore-registry.json`).
- Buhane source validation: the same nine existing signature/Google Play banner metadata findings before and after, confirmed by exact findings comparison. Reports: `/tmp/buhane-leaselore-source-before.json` and `/tmp/buhane-leaselore-source-after.json`.
- Playwright/Chrome: English and Turkish at 1440x1000 and 390x844 passed. Verified counts 14/5/5/4, Apps/Game/SaaS filters, preservation of Mintropolis, non-overlapping map tiles, menu/index navigation, local image loading, localized canonical URLs, Android-only application metadata and install URL, iOS request link, FAQ expansion, reciprocal language switching and no horizontal overflow.
- Desktop hero/detail and mobile card/detail screenshots were visually inspected. Evidence: `/tmp/buhane-leaselore-browser/results.json` and sibling PNGs. The temporary server and browser were closed after verification.

# Scope

No unrelated changes were reverted, and no LeaseLore product-source files, external accounts or deployment settings were modified. No commit or push was performed. Existing banner metadata findings remain out of scope.
