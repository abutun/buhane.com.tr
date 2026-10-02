---
quick_id: 260919-hlw
title: Add Mintropolis to the bilingual portfolio
date: 2026-09-19
status: complete
commit: none
---

# Outcome

Mintropolis is listed as the thirteenth product, in SaaS/Web discovery with explicit public-beta status. Both homepage languages include its original local logo, product-network tile, product card and official link to https://mintropolis.io/. Shared navigation and both indexes link to the new localized detail pages at `/products/mintropolis/` and `/tr/urunler/mintropolis/`.

The detail pages describe cities, community Embassies, official Drops and free wallet-linked Passport discovery. They explain the Cosmic Meta NFT connection without confusing cosmicmeta.io with the existing The Cosmic Meta publication at thecosmicmeta.com. Future governance, resources and token proposals are not presented as released features or financial benefits. Mint supply and participation totals were deliberately omitted.

Totals, README, sitemap, registry, requirements and validation expectations are synchronized: 13 products, 4 apps, 5 games, 4 platforms/publications and 30 canonical hub routes. Mintropolis is registered as a beta WebApplication with its preferred .io origin. Its local repository name does not establish a public .lol alias. A public sitemap was not verified (`/sitemap.xml` returned 404), so the registry leaves that value null.

# Sources

- https://mintropolis.io/ and https://mintropolis.io/drops for the public discovery purpose and official-source boundary.
- https://mintropolis.io/passport for the free wallet-linked profile and no-guaranteed-mint boundary.
- https://mintropolis.io/about for the Buhane and Cosmic Meta relationship.
- https://mintropolis.io/roadmap and https://mintropolis.io/release-notes for current beta scope versus future work.
- https://cosmicmeta.io/ for Cosmic Meta NFT and Mintropolis Genesis creative context.
- Original icon copied unchanged from `mintropolis.lol/web/public/assets/mintropolis-apple-touch-v1.png`, the same asset path referenced by the live site's apple-touch link.

# Verification

- `python3 -m unittest discover -s scripts/tests`: 58 tests passed, including a new bilingual inventory/count regression test. Deliberate command-timeout fixtures print findings but do not fail the suite.
- JavaScript syntax and `git diff --check`: passed.
- Registry validation: no findings (`/tmp/buhane-mintropolis-registry.json`).
- Buhane source validation: exactly the same nine pre-existing banner metadata findings before and after; no new findings. Reports: `/tmp/buhane-mintropolis-source-before.json` and `/tmp/buhane-mintropolis-source-after.json`.
- Playwright/Chrome: English and Turkish at 1440x1000 and 390x844 passed. Checked 13 cards/map links, totals 13/4/5/4, three SaaS/Web cards, five Games cards, filters, menu/index navigation, canonical URLs, local image loading, reciprocal language navigation, FAQ expansion, non-overlapping map tiles and horizontal overflow.
- Screenshots inspected for desktop hero and mobile card/detail layouts. Evidence: `/tmp/buhane-mintropolis-browser/results.json` and sibling PNGs. Temporary browser and HTTP server were closed.

# Scope

The worktree was clean at the start. No product-source repositories, hosting settings or external accounts were edited. The task is implemented locally; no commit, push or deployment was performed. Existing signature/Google Play banner metadata findings remain out of scope.

The system Homebrew Node executable failed due to a missing SQLite library. Syntax and browser checks used the bundled Codex Node runtime successfully without modifying the machine's Node installation.
