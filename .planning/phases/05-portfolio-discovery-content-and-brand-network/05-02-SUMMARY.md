---
phase: 05-portfolio-discovery-content-and-brand-network
plan: 05-02
subsystem: bilingual-company-hub
tags: [static-html, portfolio, seo, structured-data, hreflang, sitemap]

requires:
  - phase: 05-portfolio-discovery-content-and-brand-network
    provides: Private eleven-product registry, preferred origins, stable product IDs, reviewed claims, and source validator
provides:
  - Authoritative bilingual Buhane company and eleven-product discovery hub
  - Two portfolio indexes and eleven substantial EN/TR product-detail pairs
  - Canonical, hreflang, Open Graph, JSON-LD, robots, and sitemap discovery network
  - Strict Buhane source validation with hub route and product-identity evidence
affects: [05-03, 05-04, 05-05, 05-06, 05-07, 05-08, 05-09, 05-10, 05-11, 05-12, 05-13, 05-14]

actuals:
  tokens: 82507
  tasks: 3
  commits: 3

tech-stack:
  added: []
  patterns: [paired static locale routes, registry-derived product identity, page-local JSON-LD graph, canonical-only sitemap]

key-files:
  created:
    - products/index.html
    - products/*/index.html
    - tr/urunler/index.html
    - tr/urunler/*/index.html
    - robots.txt
    - sitemap.xml
  modified:
    - index.html
    - tr/index.html
    - styles.css
    - script.js
    - scripts/validate_portfolio.py
    - scripts/tests/test_validate_portfolio.py

key-decisions:
  - "Buhane is the authoritative organization and discovery hub; every product detail retains its registry product @id and preferred product-origin URL."
  - "The bilingual public inventory is exactly 26 routes: two company roots, two portfolio indexes, and eleven EN/TR product pairs."
  - "Hive Due and Site Hesap use separate ROW/Türkiye destinations while both locale pages retain the one https://hivedue.com/#product identity."
  - "The static verification HTML is excluded from the indexable source inventory while remaining byte-for-byte preserved at the hosting root."

patterns-established:
  - "Locale pair contract: Every public page has one canonical, reciprocal absolute en/tr alternates, and x-default to English."
  - "Hub detail schema: Organization, WebPage, BreadcrumbList, and registry-typed product nodes keep page and product identities separate."
  - "Substantial detail template: Each product explains audience, job, released capabilities, steps, facts, boundaries, privacy/safety, ownership, FAQs, and next destination."

requirements-completed: [DISC-02, HUB-01, ENT-01, TECH-01, LOCALE-03, CONT-01, LINK-01, AIPOL-01, MEAS-01, VAL-01]

coverage:
  - id: D1
    description: "The EN/TR company roots present Buhane's legal/brand identity and expose the same eleven reviewed products through crawlable portfolio navigation."
    requirement: HUB-01
    verification:
      - kind: integration
        ref: "python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode source --site buhane --allow-pending --report /tmp/buhane-05-02-home.json"
        status: pass
      - kind: manual_procedural
        ref: "Rendered 1440x900 and 390x844 EN/TR root checks with no overflow, broken images, or console errors"
        status: pass
    human_judgment: true
    rationale: "Company presentation and responsive visual quality were inspected in a rendered browser in addition to mechanical validation."
  - id: D2
    description: "Exactly eleven substantial EN/TR product pairs preserve registry origins, stable product IDs, product-specific claims and boundaries, reciprocal alternates, and owner context."
    requirement: CONT-01
    verification:
      - kind: integration
        ref: "Strict Buhane source validation plus route/product/entity/alternate assertions"
        status: pass
      - kind: manual_procedural
        ref: "Rendered app, SaaS, game, Hive Due, Lastimo, and The Cosmic Meta pages in both locales"
        status: pass
    human_judgment: true
    rationale: "Representative pairs were reviewed for product-specific content and responsive presentation; all pairs were mechanically checked for metadata and identity contracts."
  - id: D3
    description: "Robots declares one preferred sitemap and the sitemap lists exactly the 26 canonical public routes while strict source validation records schema and identity evidence."
    requirement: DISC-02
    verification:
      - kind: integration
        ref: "python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode source --site buhane --report /tmp/buhane-05-02-final.json"
        status: pass
      - kind: integration
        ref: "python3 -m unittest scripts.tests.test_validate_portfolio (22 tests)"
        status: pass
    human_judgment: false

duration: 23min
completed: 2026-08-11
status: complete
---

# Phase 05 Plan 02: Buhane Bilingual Company Hub and Product Network Summary

**A crawlable bilingual Buhane company hub now connects eleven truthful product overviews to their preferred official destinations with canonical locale metadata and strict discovery validation.**

## Performance

- **Duration:** 23 min
- **Started:** 2026-08-11T16:00:02Z
- **Completed:** 2026-08-11T16:22:49Z
- **Tasks:** 3
- **Files modified:** 32

## Accomplishments

- Rebuilt the English and Turkish company roots as synchronized organization hubs with clear company positioning, 11-product navigation, legal/brand context, Open Graph metadata, and stable Organization/WebSite JSON-LD.
- Added English and Turkish portfolio indexes plus 22 product-specific detail pages covering audience, job, released capabilities, use path, platform and locale facts, privacy or safety context, boundaries, lifecycle review, Buhane ownership, FAQs, and registry-approved CTAs.
- Published a canonical-only 26-URL sitemap and a robots policy that declares it once, then integrated the complete route and product-identity contract into strict source validation.
- Made shared navigation JavaScript safe on pages without optional home-only controls and added responsive, accessible portfolio/detail styles without introducing a build step or framework.

## Task Commits

Each task was committed atomically:

1. **Task 1: Establish bilingual company identity and crawlable portfolio navigation** - `edcc870` (feat)
2. **Task 2: Add substantial EN/TR portfolio and eleven product-detail pairs** - `fec99f4` (feat)
3. **Task 3: Publish canonical discovery files and preserve static-host invariants** - `687a98a` (feat)

## Files Created/Modified

- `index.html`, `tr/index.html` - Synchronized bilingual company roots and eleven-product navigation.
- `products/index.html`, `tr/urunler/index.html` - Localized canonical portfolio indexes.
- `products/*/index.html`, `tr/urunler/*/index.html` - Eleven substantial product-detail pairs.
- `styles.css`, `script.js` - Reusable portfolio/detail presentation and optional-DOM-safe shared behavior.
- `robots.txt`, `sitemap.xml` - Public crawl policy and 26-route canonical inventory.
- `scripts/validate_portfolio.py`, `scripts/tests/test_validate_portfolio.py` - Derived Buhane source contract, detail schema/identity checks, evidence totals, verification-file exclusion, and regression coverage.

## Discovery Evidence

| Evidence | Result |
|---|---|
| Canonical origin | `https://buhane.com.tr/` |
| Indexable routes | 26 |
| Sitemap URLs | 26 unique canonical URLs; no `lastmod` |
| Parsed schema | 98 nodes; `BreadcrumbList`, `CollectionPage`, `Organization`, `SoftwareApplication`, `VideoGame`, `WebApplication`, `WebPage`, `WebSite` |
| Owner link target | `https://buhane.com.tr/#organization` |
| Product identities | All eleven registry IDs reported; zero product-identity findings or cross-site reuse conflicts |
| EN/TR alternates | All 13 route pairs reciprocal with self-reference and English `x-default` |
| Static validator | Zero high, medium, low, or info findings; exit status 0 |
| Preserved hosting files | `app-ads.txt` SHA-256 `70eb5a14f5e5a0c76c1b956de3ea980bb0e5c54f9e37f6103d6809d800f50a4a`; Yandex file SHA-256 `2be724383356e1309bc989604bc7850a1a2462ebf38aed2f87d5cfd74a91c565` |
| Deployment-only actions | Deploy public files, confirm live redirects/canonicals, submit sitemap/search-console properties, and configure privacy-safe measurement in later plans |

Expected product IDs reported by the validator:

- `https://moodjot.app/#product`
- `https://vynix.app/#product`
- `https://swipeslip.app/#product`
- `https://glowspin.app/#product`
- `https://hivedue.com/#product`
- `https://astralpost.app/#product`
- `https://gridzle.app/#product`
- `https://hoskin.app/#product`
- `https://lastimo.app/#product`
- `https://thecosmicmeta.com/#product`
- `https://u2m.io/#product`

## Decisions Made

- Kept product entities anchored to their preferred official origins while using Buhane routes as the explanatory WebPage identity; no route-local replacement product IDs were minted.
- Presented Hive Due and Site Hesap as one regional product with explicit rest-of-world and Türkiye destinations instead of implying two products.
- Kept The Cosmic Meta's relationship statement limited to the verified public publication and avoided inaccessible implementation claims.
- Constrained Lastimo copy to its six presets, current-time logging, and hide/restore/delete controls; no excluded history, statistics, analytics, past-log, past-date correction, or custom-tracker feature was claimed.
- Used visible, product-specific support content instead of hidden keywords or a generic blog/glossary batch.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Integrated the authoritative Buhane route and detail-identity contract into source validation**

- **Found during:** Incremental Task 1 validation and strict Task 3 preparation
- **Issue:** The Phase 05-01 validator treated the root Yandex verification HTML as an indexable page, did not know the hub's 26 canonical routes or 22 detail-to-product identity mappings, and rejected the authoritative company's own crawlable product links.
- **Fix:** Derived the private-registry-backed Buhane source contract inside the validator, excluded only the preserved verification HTML from indexable discovery, enforced exact product schema type/origin/publisher and WebPage canonical on all detail pages, and reported route/schema/product-identity evidence.
- **Files modified:** `scripts/validate_portfolio.py`, `scripts/tests/test_validate_portfolio.py`
- **Verification:** All 22 validator tests pass and strict Buhane source mode reports zero findings with 26 routes, 98 schema nodes, and all eleven expected product IDs.
- **Committed in:** `687a98a`

---

**Total deviations:** 1 auto-fixed (1 bug). **Impact:** Made the plan's strict discovery and product-identity acceptance criteria executable without publishing or modifying the private registry.

## Issues Encountered

- `git diff --check` caught one extra blank line at the end of each new discovery file before Task 3 was committed; both files were normalized and revalidated.
- The first browser screenshot was taken before the existing hero entrance animation completed; the settled 390×844 viewport showed the full mobile hero without overflow or console errors.
- Requirement checkboxes remain pending because these requirement IDs are shared across unfinished Phase 5 plans; this plan's completion is recorded in summary coverage and plan progress only.

## Verification

- `python3 -m unittest scripts.tests.test_validate_portfolio` - 22 tests passed.
- `python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode source --site buhane --report /tmp/buhane-05-02-final.json` - zero findings, exit status 0.
- Custom inventory assertions confirmed exactly 26 HTML canonicals equal the sitemap set, 11 EN plus 11 TR detail directories, reciprocal alternates, exact primary product IDs/types/origins, safe new-tab relations, Hive Due regional destinations, and excluded Lastimo claims absent.
- JSON-LD parsing succeeded across all pages; `node --check script.js` passed; the shared script ran against a mocked document without optional page controls.
- HTTP preview returned 200 for roots, indexes, representative product pairs, CSS, JavaScript, robots, and sitemap.
- Rendered 1440×900 and 390×844 checks covered EN/TR roots and representative app, SaaS, game, Hive Due, Lastimo, and The Cosmic Meta pairs with no horizontal overflow, broken images, or browser console errors; the mobile navigation opened and reported `aria-expanded=true`.
- `git diff --check` passed, and preserved hosting-file hashes match the task-start values.

## User Setup Required

None for source completion. Deployment, live redirect/canonical verification, search-console sitemap submission, crawler-policy owner decisions, and measurement configuration remain later-plan or deployment actions.

## Next Phase Readiness

- Plan 05-03 can consume the stable company publisher identity, product route pairs, shared presentation system, and stricter source validator.
- Plan 05-14 can run live-mode release checks after the public outputs are deployed; no phase-wide completion has been recorded by this plan.

## Self-Check: PASSED

- Both roots, two portfolio indexes, all 22 detail pages, robots, and sitemap exist.
- All three atomic task commits are present in history.
- Exact strict source validation, 22 tests, route/schema/entity assertions, HTTP smoke checks, and responsive browser checks pass.
- `app-ads.txt`, `yandex_abc334285efd6c2e.html`, and pre-existing planning artifacts retain their task-start content.
- No framework, build step, private public link, blanket reciprocal footer, hidden keyword copy, or generic content batch was introduced.

---
*Phase: 05-portfolio-discovery-content-and-brand-network*
*Completed: 2026-08-11*
