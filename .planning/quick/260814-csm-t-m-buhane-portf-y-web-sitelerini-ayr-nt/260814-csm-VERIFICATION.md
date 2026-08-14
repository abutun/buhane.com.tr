---
quick_task: 260814-csm
title: Portfolio-wide website audit and verified improvements
status: passed
verified_at: 2026-08-14
verification_scope: source-and-release-contract
source_commits:
  astral_post:
    - 8cc4344
    - e19d6d1
  hive_due:
    - c8aeadcf
    - 30edca9e
release_state: local source and release-contract checks passed; production deployment was not verified or performed
---

# Independent verification

## Result

**Passed.** The two source fixes, their post-review follow-ups, the portfolio report, and the central source contract all match the quick-task plan. This result verifies local repository source and generated-artifact contracts only. It does **not** claim that any revision is deployed, published, or live.

## Must-have evidence

| Requirement | Evidence | Result |
|---|---|---|
| Astral Post external privacy new-tab links are opener-safe | `www/privacy/index.html` contains exactly seven external HTTP(S) `target="_blank"` links; each has both `noopener` and `noreferrer`. `node scripts/verify-content-hub.mjs` passed. | Passed |
| The Astral verifier covers HTTP as well as HTTPS external links | Commit `e19d6d1` introduces an `https?://` selector and deterministic HTTPS/HTTP/local-link fixtures; the privacy-route assertion checks both required rel tokens. | Passed |
| Hive Due / Site Hesap unavailable store surfaces are honest | `AppStoreBadges.astro` and `Footer.astro` contain no `href="#"`; mobile-store surfaces are non-interactive localized coming-soon content, while the web-app CTA remains an anchor. | Passed |
| One shared regional artifact is the release contract | Fresh `npm test` rebuilt one `www/dist/`: Turkish root, `/en/`, one top-level `_astro/`, no `dist/hivedue` or `dist/sitehesap`, and the four host-qualified discovery files. The 26-test suite passed. | Passed |
| Nginx maps each discovery endpoint to the matching shared-root backing file | `deployment/nginx-hivedue-sitehesap.conf.example` uses exactly two marketing roots at `/var/www/hivedue/www/current` and aliases both hosts' `robots.txt` and `sitemap.xml` with explicit plain-text/XML types. | Passed |
| Operator probes are country-aware | `www/DEPLOY.md` requires confirmed non-Türkiye egress for direct Hive Due probes, Türkiye egress for Site Hesap probes, preserves raw redirect headers, and marks unconfirmed-egress direct validation incomplete. | Passed |
| Audit report is complete and release-safe | The report contract found all 13 exact registry display names once, allowed states only, the exact Cosmic Meta blocker verbatim, and no local-revision deployment claim. | Passed |

## Commands rerun

```text
AstralPost/www: node scripts/verify-content-hub.mjs
  PASS — 9 locales, 90 articles, 135 glossary terms, 112 canonical sitemap URLs, 112 JSON-LD blocks.

AstralPost/www: focused privacy HTTP(S) new-tab scan
  PASS — 7 external links, 0 unsafe links.

HiveDue/www: npm run check
  PASS — 0 errors, 0 warnings, 0 hints.
HiveDue/www: npm test
  PASS — fresh single-artifact build; 5 files / 26 tests passed.
HiveDue/www: npm run verify:regional-assets
  PASS — 85 HTML files, 26 unique local assets through both Host headers; missing asset is a non-HTML 404.
HiveDue/www: focused component scan
  PASS — no `href="#"` in either shared store component.

buhane.com.tr: python3 scripts/validate_portfolio.py --mode registry
  PASS — 0 findings.
buhane.com.tr: python3 scripts/validate_portfolio.py --mode source --timeout 180
  PASS — high/medium/low/info: 0/0/0/0.
buhane.com.tr: python3 -m unittest discover -s scripts/tests -p 'test_*.py'
  PASS — 55 tests. The printed `GEN.COMMAND_TIMEOUT` lines are expected timeout-handling fixtures, not validation findings.
buhane.com.tr: audit-table contract scan
  PASS — 13 exact rows; allowed states; exact Cosmic Meta blocker; no false local-deployment claim.
```

## Review follow-up resolution

Both findings in `260814-csm-REVIEW.md` are resolved by the recorded follow-up commits:

- **P2 country-aware Hive Due probes:** `30edca9e` documents the required egress split and treats the Türkiye redirect as expected regional behavior rather than a discovery-file failure.
- **P3 HTTP external-link coverage:** `e19d6d1` expands the native AstralPost selector from HTTPS-only to HTTP(S) and tests the selector behavior.

## Source and release state

- Astral Post and Hive Due were clean after the verification commands. Each local `develop` branch is two commits ahead of `origin/develop` at verification time; this is a source-control observation, not a deployment result.
- The current quick-task directory in `buhane.com.tr` remains uncommitted task documentation. No product source was changed by this verification pass.
- Production server/Nginx, GeoIP, symlink, DNS/CDN, cache, search-account, and store-listing actions remain operator-owned and were not performed. The Cosmic Meta remains blocked until its verified WordPress/source/deployment authority is supplied.
