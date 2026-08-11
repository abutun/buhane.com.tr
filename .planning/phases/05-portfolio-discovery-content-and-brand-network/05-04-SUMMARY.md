---
phase: 05-portfolio-discovery-content-and-brand-network
plan: 05-04
subsystem: hivedue-regional-publication
tags: [astro, regional-builds, cross-domain-hreflang, hivedue, sitehesap]
execution_mode: repository_local_gsd
repository: /Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue
repository_branch: develop
repository_summary: /Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/.planning/phase-05-portfolio-execution-summary.md
repository_summary_commit: 5ca6aaeb239563b6b82a4bb244d5902a3f4927be

requires:
  - phase: 05-portfolio-discovery-content-and-brand-network
    provides: One-product/two-publication registry contract and stable Hive Due identity
provides:
  - Separate host-correct Hive Due and Site Hesap static publication artifacts
  - Reciprocal cross-domain EN/TR/x-default alternates with canonical noindex copies
  - Tested regional build and deployment mapping for one shared product identity
affects: [05-14]

tech-stack:
  added: []
  patterns: [build-time regional publication, cross-publication hreflang, canonical noindex copy]

key-files:
  created:
    - /Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/www/src/lib/publication.ts
    - /Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/www/src/lib/publicationContract.test.ts
  modified:
    - /Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/www/astro.config.mjs
    - /Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/www/src/layouts/BaseLayout.astro
    - /Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/www/DEPLOY.md

key-decisions:
  - "Hive Due and Site Hesap are separate regional publications of one product and both reuse https://hivedue.com/#product."
  - "Initial HTML owns canonical, social, schema, robots, sitemap, and alternate metadata; client JavaScript does not repair it."

requirements-completed: [DISC-02, ENT-01, TECH-01, LOCALE-03, CONT-01, LINK-01, VAL-01]

coverage:
  - id: D1
    description: "Both regional builds emit host-correct canonical content and one shared product identity."
    requirement: ENT-01
    verification:
      - kind: integration
        ref: "npm run check && npm test && npm run build:regional"
        status: pass
    human_judgment: false
  - id: D2
    description: "Canonical pages expose reciprocal cross-domain alternates while noncanonical copies remain noindex and canonicalized."
    requirement: LOCALE-03
    verification:
      - kind: integration
        ref: "python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode source --site hive-due"
        status: pass
    human_judgment: false

completed: 2026-08-11
status: complete
---

# Phase 05 Plan 04: Hive Due / Site Hesap Dual-Domain Regional Publication Summary

**Two tested regional artifacts now serve host-correct initial HTML for Hive Due and Site Hesap while preserving one Hive Due product identity.**

## Repository-local execution

| Evidence | Result |
|---|---|
| Repository | `/Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue` |
| Local GSD workflow | Quick task `260811-qcz` |
| Branch and baseline | `develop` from clean `9957e5eb` |
| Source commit | `eebe47e2` |
| Local summary commit | `5ca6aaeb239563b6b82a4bb244d5902a3f4927be` |
| Authoritative local summary | `/Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/.planning/phase-05-portfolio-execution-summary.md` |
| Current orchestration snapshot | Clean worktree on `develop` |

## Accomplishments

- Produced `dist/hivedue` and `dist/sitehesap` as separate 85-HTML-file artifacts mapped to their exact deployment hosts.
- Kept English `/en/` canonical on Hive Due and Turkish unprefixed canonical on Site Hesap, with reciprocal `en`, `tr`, and `x-default` links.
- Kept noncanonical cross-host copies `noindex,follow` and canonicalized to the peer while reusing `https://hivedue.com/#product` and the Buhane publisher.

## Validation evidence

| Gate | Result |
|---|---|
| Astro check before/after | 49 then 51 files; 0 diagnostics |
| Native tests before/after | 12 then 21 tests passed |
| Regional builds | 85 HTML files and 42 sitemap URLs per variant |
| Central source validation after parent cross-publication repair | Exit 0; high/medium/low/info all 0 in both variants |
| Central selected-site evidence | 42 indexable routes, 42 sitemap URLs, 151 schema nodes |

## Deviations and follow-ups

- The local execution initially exposed 84 `LOCALE.NONADDRESSABLE_HREFLANG` findings because the parent treated each publication's canonical locale as a single-URL architecture. Parent commit `528ef6d` added registry-driven cross-publication hreflang and required-noindex-copy contracts; both variants then passed without weakening their reciprocal alternates.
- Deployment must keep each artifact on only its named host. HTTPS, directory indexes, optional root redirect, DNS/CDN, live crawling, search-console, analytics, and IndexNow actions remain external.

## Unrelated-dirt evidence

The repository began clean and remains clean. Ignored `www/dist/**`, `www/.astro/**`, and `www/node_modules/**` output was never staged; the parent repository was read only during local execution.

## Self-Check: PASSED

- The regional source commit and local summary commit are present.
- Native checks, 21 tests, both builds, raw artifact audit, and repaired central validation pass.
- The wrapper preserves the exact repository, branch, summary path, commit hashes, build counts, validator deviation, and deployment boundary.

