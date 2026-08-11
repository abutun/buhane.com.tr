---
phase: 05-portfolio-discovery-content-and-brand-network
plan: 05-01
subsystem: discovery-validation
tags: [portfolio-registry, seo, structured-data, validation, crawler-policy, measurement]

requires:
  - phase: 05-portfolio-discovery-content-and-brand-network
    provides: Phase 5 context, research, preferred-origin audit, and repository boundary map
provides:
  - Private eleven-product truth and publication registry
  - Dependency-free registry, source, and live validation CLI with JSON reports
  - Deployment separation, crawler policy, and privacy-safe measurement contracts
affects: [05-02, 05-03, 05-04, 05-05, 05-06, 05-07, 05-08, 05-09, 05-10, 05-11, 05-12, 05-13, 05-14]

actuals:
  tokens: 40588
  tasks: 3
  commits: 4

tech-stack:
  added: []
  patterns: [private JSON truth registry, Python-standard-library validator, deterministic finding IDs, fail-closed live request boundary]

key-files:
  created:
    - .planning/portfolio-sites.json
    - scripts/validate_portfolio.py
    - scripts/tests/test_validate_portfolio.py
    - docs/portfolio/VALIDATION.md
    - docs/portfolio/DISCOVERY_AND_MEASUREMENT.md
  modified: []

key-decisions:
  - "Vynix uses https://vynix.app/ without www; all recorded preferred origins are HTTPS and legacy hosts remain aliases only."
  - "Hive Due and Site Hesap are two publication variants of one product and always reuse https://hivedue.com/#product."
  - "Only missing route, robots, and sitemap rules can be pending during incremental plans; security, truth, canonical, schema, product-identity, and existing-output findings remain fatal."
  - "Search/citation crawling and model-training policy are separate; training access remains owner_decision_required."

patterns-established:
  - "Registry authority: Later plans consume preferred origins, product IDs, verified features, excluded claims, link allowlists, and dirty-path exclusions from one private manifest."
  - "Variant accounting: Multi-host output is built and inspected independently while inheriting one product identity."
  - "Fail-closed validation: Any high-severity finding makes registry, source, or live mode return nonzero."

requirements-completed: [DISC-01, DISC-02, ENT-01, TECH-01, LOCALE-03, CONT-01, LINK-01, AIPOL-01, MEAS-01, VAL-01, EXT-01]

coverage:
  - id: D1
    description: "A private registry covers exactly eleven products plus the Buhane and ahmet.sh properties with approved origins, identities, claims, locales, variants, and exclusions."
    requirement: DISC-01
    verification:
      - kind: integration
        ref: "python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode registry"
        status: pass
      - kind: other
        ref: "python3 -m json.tool .planning/portfolio-sites.json"
        status: pass
    human_judgment: false
  - id: D2
    description: "The standard-library CLI validates registry, source output, and live deployments with deterministic JSON findings, product-identity reuse, pending-rule boundaries, and request-origin safety."
    requirement: VAL-01
    verification:
      - kind: integration
        ref: "python3 -m unittest scripts.tests.test_validate_portfolio (21 tests)"
        status: pass
      - kind: integration
        ref: "python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode registry"
        status: pass
    human_judgment: false
  - id: D3
    description: "Operational policy documents define private deployment separation, product schema identity reuse, crawler categories, owner-decided training access, six privacy-safe events, and 0/28/90-day evidence fields."
    requirement: AIPOL-01
    verification:
      - kind: manual_procedural
        ref: "Required heading, event/property, forbidden-data, command, and deploy-exclusion assertions"
        status: pass
    human_judgment: true
    rationale: "Crawler training consent and final analytics/deployment configuration require owner and deployment review even though document tokens are mechanically verified."

duration: 28min
completed: 2026-08-11
status: complete
---

# Phase 05 Plan 01: Portfolio Truth Registry and Validation Contract Summary

**Eleven-product truth authority with deterministic source/live validation, dual-host entity reuse, private deploy separation, and privacy-safe discovery measurement**

## Performance

- **Duration:** 28 min
- **Started:** 2026-08-11T15:24:00Z
- **Completed:** 2026-08-11T15:52:00Z
- **Tasks:** 3
- **Files modified:** 5

## Accomplishments

- Encoded exactly eleven Buhane products plus the Buhane company hub and Ahmet's personal property, including preferred/legacy origins, stable product IDs, factual claims, locale architecture, contextual-link allowlists, dirty paths, and external blockers.
- Added a dependency-free CLI for registry, source, and live checks with deterministic finding records, independent Hive Due/Site Hesap output accounting, strict pending-rule boundaries, safe live requests, and 21 passing fixtures.
- Documented generator ownership, repository-native checks, deploy exclusions, schema identity reuse, search/citation versus training crawler policy, six allowed measurement events, forbidden user data, and 0/28/90-day evidence collection.

## Task Commits

Each task was committed atomically:

1. **Task 1: Encode the eleven-product truth and publication registry** - `0c026c1` (feat)
2. **Task 2: Implement deterministic registry, source, and live validation** - `8cfbe97` (feat)
3. **Task 3: Document deployment separation, crawler policy, and privacy-safe measurement** - `250c795` (docs)

Plan verification correction:

- `c62f7e5` (fix) - require permanent legacy redirects and inspect live sitemap pages/indexes.

## Files Created/Modified

- `.planning/portfolio-sites.json` - Private owner, origin, identity, claim, locale, link, variant, command, and exclusion authority.
- `scripts/validate_portfolio.py` - Standard-library registry/source/live validation CLI and JSON report generator.
- `scripts/tests/test_validate_portfolio.py` - Temporary static-site, dual-host, truth, schema, sitemap, link, locale, redirect, and request-boundary fixtures.
- `docs/portfolio/VALIDATION.md` - Commands, severity/report contract, repository matrix, generator ownership, dirty paths, entity reuse, and deploy allowlist.
- `docs/portfolio/DISCOVERY_AND_MEASUREMENT.md` - Search/AI foundation, crawler decision split, event privacy rules, evidence schedule, and external follow-ups.

## Decisions Made

- Treated preferred origins and exact stable product IDs as hard registry invariants rather than suggestions inferred from page content.
- Modeled Hive Due and Site Hesap as independent publication outputs sharing one product identity; variants cannot override `product_entity_id`.
- Limited `--allow-pending` to three missing route/discovery rules and kept all truth, security, identity, canonical, schema, private-route, existing-output, and variant failures fatal.
- Kept the manifest inside tracked planning state but made explicit deployment allowlisting mandatory so `.planning/**`, `scripts/**`, and reports never reach a public root.
- Left model-training crawler access as `owner_decision_required`; desire for search/citation visibility does not imply training consent.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Completed live sitemap and permanent redirect validation**

- **Found during:** Final plan verification after Task 3
- **Issue:** The initial live validator capped redirect counts and checked discovery responses, but did not preserve redirect status codes or fetch sitemap-listed pages to verify direct 200 HTML, matching canonicals, and absence of `noindex`.
- **Fix:** Recorded redirect status chains, required a one-hop `301` or `308` for legacy origins, recursively inspected bounded sitemap indexes, and validated each sitemap page response/canonical/indexability.
- **Files modified:** `scripts/validate_portfolio.py`, `scripts/tests/test_validate_portfolio.py`
- **Verification:** Full suite passes with 21 tests, including a temporary-redirect rejection fixture.
- **Committed in:** `c62f7e5`

---

**Total deviations:** 1 auto-fixed (1 bug). **Impact:** Closed a live-release validation gap without changing architecture or public-site scope.

## Issues Encountered

- The first passing Hive fixture removed its guide output while retaining the home-page guide link. The fixture was corrected before the Task 2 commit; the complete suite then passed.
- Running Python's exact unittest command created untracked `__pycache__` output. The generated bytecode was removed after verification and no ignore or product file was changed.
- The installed GSD fallback lacks `requirements.ready-ids`; requirement checkboxes remain pending because these IDs are shared with unfinished Phase 5 plans, while plan progress was updated to 1/14 through GSD state/roadmap tooling.

## Verification

- `python3 -m unittest scripts.tests.test_validate_portfolio` - 21 tests passed.
- `python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode registry` - zero findings, exit status 0.
- `python3 -m json.tool .planning/portfolio-sites.json` - parsed successfully.
- CLI help exposes `--help`, `--manifest`, `--mode`, repeatable `--site`, `--timeout`, `--report`, and `--allow-pending`.
- Documentation assertions confirmed all three modes, literal deploy exclusions, crawler split, `owner_decision_required`, six event names, five allowed properties, and the forbidden-data list.
- `git diff --check e0928a0..HEAD` passed.
- The production commit range contains only the registry, validator/tests, and two policy documents; `index.html`, `tr/index.html`, shared CSS/JavaScript, `app-ads.txt`, and the Yandex verification file were untouched.

## User Setup Required

None - no external service configuration is required for this plan. Account- and deployment-dependent actions remain explicit follow-ups in the measurement contract.

## Next Phase Readiness

- Plan 05-02 can consume exact product IDs, preferred origins, claims, locale contracts, and deploy exclusions when building the Buhane bilingual hub.
- Repository-specific plans can select one property with `--site`; strict portfolio release validation remains reserved for Plan 05-14 after public outputs are implemented.
- The Cosmic Meta remains correctly `external_blocked` until the actual WordPress administration or deploy source is available.

## Self-Check: PASSED

- All five key files exist.
- All four production/fix commits are present in history.
- All task acceptance and plan-level verification commands pass.
- No public-site or sibling-product repository file was modified.

---
*Phase: 05-portfolio-discovery-content-and-brand-network*
*Completed: 2026-08-11*
