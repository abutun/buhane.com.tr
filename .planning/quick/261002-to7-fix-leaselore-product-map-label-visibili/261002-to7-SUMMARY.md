---
quick_id: 261002-to7
title: Fix LeaseLore product-map label visibility
date: 2026-10-02
status: complete
execution: inline
source_commit: 7918a76
---

# Result

Both homepages request styles.css?v=20261002-leaselore so a cached pre-LeaseLore stylesheet no longer collapses the new map tile. Existing LeaseLore and App/Uygulama labels, icon, destinations, layout and portfolio counts are preserved.

## Evidence

- The live CSS response advertises Cache-Control: max-age=14400; current live and local CSS already contain the correct LeaseLore grid placement.
- A simulated older stylesheet with full-width Mintropolis and no LeaseLore placement reproduces the reported appearance: the tile is 68px wide and both label columns have zero width.
- This simulation supports the cache diagnosis; it is not a direct inspection of the user's browser cache.

## Verification

- 60 Python unit tests pass, including new bilingual map-label and shared CSS-version checks.
- git diff --check passes.
- Playwright/Chrome passes 14 locale/viewport combinations: EN/TR at 320, 390, 768, 1024, 1200, 1440 and 1920px.
- LeaseLore labels are fully visible, untruncated and inside the tile; all 14 map tiles have no overlaps; there is no horizontal page overflow or JavaScript error; the icon and detail links are correct.
- Cached unversioned CSS is simulated during the browser checks and is not requested by the updated homepages.
- Desktop and mobile map screenshots were visually reviewed.
- Evidence: /tmp/buhane-leaselore-label-check/results.json and adjacent PNGs.
- Temporary browser and HTTP server were closed.

## Publishing

Source commit: 7918a76. No push or deployment was performed.
