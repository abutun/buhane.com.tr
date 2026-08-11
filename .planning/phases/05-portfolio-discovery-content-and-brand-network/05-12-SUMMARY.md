---
phase: 05-portfolio-discovery-content-and-brand-network
plan: 05-12
subsystem: u2m-public-route-contract
tags: [u2m, initial-html, vite, spring-security, nginx, noindex, sitemap]
execution_mode: repository_local_gsd
repository: /Users/ahmet/Documents/Workspaces/Buhane/u2m-api
repository_branch: main
repository_summary: /Users/ahmet/Documents/Workspaces/Buhane/u2m-api/.planning/phase-05-portfolio-execution-summary.md
repository_summary_commit: a8ca07ea5c978ccd594a93a186da5b34afeb12b4

requires:
  - phase: 05-portfolio-discovery-content-and-brand-network
    provides: Preferred U2M origin, product identity, owner graph, and central validation contract
  - commit: d6a382a367ee21d4c3300dbc9ef840615ff83cb2
    provides: Parent registry/validator alignment with the generated Vite publish artifact and seven canonical public routes
provides:
  - Seven crawlable U2M routes with useful initial HTML and one stable product identity
  - Explicit public, alias, auth, dashboard, profile, and private-route behavior across Vite, Spring, and three Nginx profiles
  - Deterministic public-page generation plus full frontend, E2E, backend, and central validation evidence
affects: [05-14]

tech-stack:
  added: []
  patterns: [source-driven static public pages, publish-artifact validation, explicit route matrix, defense-in-depth noindex and authentication]

key-files:
  created:
    - /Users/ahmet/Documents/Workspaces/Buhane/u2m-api/frontend/src/content/publicPages.js
    - /Users/ahmet/Documents/Workspaces/Buhane/u2m-api/frontend/scripts/build-public-pages.mjs
    - /Users/ahmet/Documents/Workspaces/Buhane/u2m-api/frontend/public/sitemap.xml
  modified:
    - /Users/ahmet/Documents/Workspaces/Buhane/u2m-api/frontend/vite.config.js
    - /Users/ahmet/Documents/Workspaces/Buhane/u2m-api/src/main/java/com/buhane/u2m/config/SecurityConfig.java
    - /Users/ahmet/Documents/Workspaces/Buhane/u2m-api/src/main/java/com/buhane/u2m/controller/FrontendController.java
    - /Users/ahmet/Documents/Workspaces/Buhane/u2m-api/src/main/java/com/buhane/u2m/controller/DashboardController.java
    - /Users/ahmet/Documents/Workspaces/Buhane/u2m-api/src/test/java/PublicFrontendRoutingTest.java
    - /Users/ahmet/Documents/Workspaces/Buhane/u2m-api/nginx/u2m-admin.conf

key-decisions:
  - "Central validation inspects frontend/dist, the Vite publish artifact, rather than the incomplete frontend source/input tree."
  - "The public discovery inventory is exactly / plus six generated canonical routes; aliases, auth, dashboard, profile, stats, tokens, and /frontend/** stay out of the sitemap."
  - "The legacy /dashboard/{token} route remains Spring-owned and public but noindex; account dashboard and profile routes remain authenticated."

requirements-completed: [DISC-02, ENT-01, TECH-01, CONT-01, LINK-01, AIPOL-01, MEAS-01, VAL-01]

coverage:
  - id: D1
    description: "Reviewed source generates six public content routes plus the initial-HTML home, all reusing the U2M product and Buhane publisher identities."
    requirement: ENT-01
    verification:
      - kind: integration
        ref: "npm run build:public-pages && npm run check:public-pages && npm run build"
        status: pass
      - kind: integration
        ref: "python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode source --site u2m"
        status: pass
    human_judgment: false
  - id: D2
    description: "Vite, Spring Security/controllers, and all three Nginx profiles enforce one tested public/auth/private route and noindex contract."
    requirement: VAL-01
    verification:
      - kind: test
        ref: "npm run test:unit (79/79) and npm run test:e2e (26/26)"
        status: pass
      - kind: test
        ref: "./gradlew test (411/411)"
        status: pass
    human_judgment: false

completed: 2026-08-11
status: complete
---

# Phase 05 Plan 12: U2M Crawlable Public Marketing and Documentation Surface Summary

**U2M now publishes seven crawlable initial-HTML routes backed by a deterministic generator and a tested cross-stack route, authentication, redirect, and noindex contract.**

## Repository-local execution

| Evidence | Result |
|---|---|
| Repository | `/Users/ahmet/Documents/Workspaces/Buhane/u2m-api` |
| Branch and starting HEAD | `main`; `09d9886` (`origin/main`, tag `v1.7`) |
| Implementation commit | `d5b4bbbdd6dbc988f83d61ae35df3f171d7b5dff` — `feat(05-12): add crawlable U2M public route contract` |
| Local summary commit | `a8ca07ea5c978ccd594a93a186da5b34afeb12b4` — `docs(05-12): record U2M execution evidence` |
| Parent registry/validator fix | `d6a382a367ee21d4c3300dbc9ef840615ff83cb2` — `fix(05-12): validate U2M Vite publish artifact` |
| Authoritative local summary | `/Users/ahmet/Documents/Workspaces/Buhane/u2m-api/.planning/phase-05-portfolio-execution-summary.md` |
| Starting and current status | Clean |

## Accomplishments

- Added reviewed source and deterministic generation for `/guides/`, `/guides/create-short-links/`, `/use-cases/`, `/use-cases/campaign-links/`, `/api/`, and `/privacy/`, alongside useful initial HTML at `/`.
- Published page-specific metadata, canonical URLs, Open Graph data, and JSON-LD that consistently reuse `https://u2m.io/#product` and the Buhane publisher identity.
- Generated a canonical-only seven-URL sitemap and robots declaration while excluding auth, password, stats, token dashboard, account dashboard, profile, legacy alias, and `/frontend/**` routes.
- Aligned Vue/Vite, Spring Security/controllers, and all three Nginx profiles on static-page precedence, exact 308 aliases, authenticated account routes, the Spring-owned legacy token route, response-header noindex rules, and unknown-alias 404 behavior.
- Added unit, Chromium E2E, controller, security, and Nginx-profile regression coverage for the complete route matrix.

## Non-human gate evidence

| Gate | Result |
|---|---|
| Gate 1 — generation/initial HTML | Generator wrote 8 discovery files; `--check` matched all 8; focused public-content/scaffold tests passed 15/15 |
| Gate 2 — route/security matrix | Unit suite passed 14 files and 79/79 tests; Chromium E2E passed 26/26; targeted DashboardController, FrontendController, PublicFrontendRouting, and Nginx routing Gradle suites passed |
| Gate 3 — complete repository | Generator/check/build passed; unit 79/79; E2E 26/26; full Gradle suite 411/411 |
| Central source validation after parent fix | Exit 0; high=0, medium=0, low=0, info=0 |
| Central inventory | 7 indexable routes, 7 sitemap URLs, 28 schema nodes, product entity `https://u2m.io/#product`, and zero identity mismatch findings |
| Diff hygiene | `git diff --cached --check` passed before the scoped implementation commit |

## Parent registry dependency and fix

The first central source run exposed a parent-only contract mismatch: the registry inspected `frontend/` instead of the deployable Vite output and still declared retired aliases. Parent commit `d6a382a367ee21d4c3300dbc9ef840615ff83cb2` moved `public_root` to `frontend/dist`, declared the exact seven canonical routes, removed the temporary pending-source exemptions, required sitemap URLs to remain inside the declared route contract, and added fail-closed tests. The unchanged U2M implementation then passed central validation with zero findings.

## Preservation, deviations, and follow-ups

- No pre-existing U2M worktree dirt was present or overwritten; current repository status is clean.
- `frontend/dist/**` was generated only by the build and remains ignored (`!! frontend/dist/`), unstaged, uncommitted, and absent from `git ls-files`. This is publish output, not hand-edited source.
- Early stale-generator enumeration, route-test expectation, legacy footer-test, and whitespace-only output defects were corrected before the atomic implementation commit; the complete Gate 3 command was rerun afterward.
- No push or deployment was performed. Production deployment must ship the Vite artifact, Spring application, and selected Nginx profile together, then verify the live status/header matrix and discovery files.

## Self-Check: PASSED

- Both exact U2M repository-local commits and the authoritative local summary are present on `main`.
- All three non-human gates pass with 79 unit, 26 E2E, 411 Gradle, seven-route/seven-sitemap, and zero-finding central evidence.
- The parent registry dependency/fix, ignored-dist boundary, clean repository status, no-push/no-deploy boundary, and deployment-only follow-ups are recorded explicitly.
