---
quick_task: 260815-sx4
title: Replace Buhane product-card initials with verified local product logos
status: complete
code_commit: 802b0f6
completed_at: 2026-08-15
---

# Product-card logo delivery

## Delivered

- Copied ten verified public PNG assets byte-for-byte into `images/products/` and
  replaced the corresponding one-letter card placeholders on both localized home
  pages.
- Preserved product names, links, ordering, card grid, and responsive breakpoints.
- Added meaningful English `logo` and Turkish `logosu` alt text plus fixed 56px
  intrinsic dimensions for all real logos.
- Added a shared contained `.product-logo` treatment so the landscape U2M wordmark
  remains uncropped, and a subdued empty `.product-logo--unavailable` slot for the
  blocked The Cosmic Meta record.
- Added `scripts/tests/test_product_card_logos.py` to protect EN/TR ordering, local
  paths, localized alt text, PNG signatures/dimensions, no remote images, no legacy
  monograms, and the one documented Cosmic Meta exception.

## Validation

- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s scripts/tests -p 'test_*.py'` — **57 tests passed**.
- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode registry` — **PASS, 0 findings**.
- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode source --site buhane --report /tmp/260815-sx4-buhane-logo-cards.json` — **PASS, 0 findings**.
- The plan's local-logo guard passed; all ten expected files exist and no
  `product-monogram` reference remains in either page or the stylesheet.
- `cmp -s` confirmed all ten copied PNGs match their approved provenance sources
  byte-for-byte; `git diff --check` passed.

## Visual smoke check

A temporary local HTTP server verified successful local asset requests for both
`/` and `/tr/`, then was stopped. Desktop EN (1440px) and TR (wide desktop), plus
EN and TR mobile (390px), rendered 11 cards with 10 loaded logo images and one empty
Cosmic Meta slot. No horizontal overflow occurred; all logo boxes retained 56px
dimensions, and U2M loaded at 500×347 with `object-fit: contain`.

## Documented exception and release

The Cosmic Meta remains `external_blocked` in the registry. Its card deliberately
uses an empty `aria-hidden` decorative slot, never a guessed mark, letter, remote
asset, or a logo from excluded similarly named directories.

Only **buhane.com.tr** needs redeployment after commit `802b0f6` is pushed. No
sibling product repository or product deployment was changed.
