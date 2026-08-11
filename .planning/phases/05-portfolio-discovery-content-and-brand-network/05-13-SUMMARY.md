---
phase: 05-portfolio-discovery-content-and-brand-network
plan: 05-13
subsystem: ahmet-sh-founder-selected-work
tags: [ahmet-sh, person-schema, founder, selected-work, bilingual-client-state, sitemap]
execution_mode: repository_local_gsd
repository: /Users/ahmet/Documents/Workspaces/Buhane/ahmet.sh
repository_branch: main
repository_summary: /Users/ahmet/Documents/Workspaces/Buhane/ahmet.sh/.planning/phase-05-portfolio-execution-summary.md
repository_summary_commit: b25ed203fa4d4f10291edd1a70eec5b6cdd5017c

requires:
  - phase: 05-portfolio-discovery-content-and-brand-network
    provides: Registry-approved contextual links, preferred origins, and the authoritative Buhane portfolio destination
provides:
  - Factual Ahmet Bütün Person/founder identity connected to Buhane
  - Six registry-approved selected-work links with localized full-portfolio handoff
  - Honest single-canonical EN/TR client-state discovery contract
affects: [05-14]

tech-stack:
  added: []
  patterns: [single-route client localization, Person/WebSite/Organization graph, curated contextual work links]

key-files:
  created:
    - /Users/ahmet/Documents/Workspaces/Buhane/ahmet.sh/robots.txt
    - /Users/ahmet/Documents/Workspaces/Buhane/ahmet.sh/sitemap.xml
  modified:
    - /Users/ahmet/Documents/Workspaces/Buhane/ahmet.sh/index.html
    - /Users/ahmet/Documents/Workspaces/Buhane/ahmet.sh/i18n.js
    - /Users/ahmet/Documents/Workspaces/Buhane/ahmet.sh/style.css
    - /Users/ahmet/Documents/Workspaces/Buhane/ahmet.sh/script.js

key-decisions:
  - "ahmet.sh remains one canonical URL; EN/TR are client-side states without fabricated locale routes or hreflang."
  - "The personal site presents exactly six approved examples of maker work and sends the complete portfolio to Buhane."
  - "Product destinations are contextual work links, not Person or Organization sameAs identities."

requirements-completed: [DISC-02, ENT-01, TECH-01, LOCALE-03, CONT-01, LINK-01, MEAS-01, VAL-01]

coverage:
  - id: D1
    description: "The canonical ahmet.sh document identifies Ahmet as a Person, states the factual Buhane founder relationship, and presents the same six approved work examples in both client-side language states."
    requirement: ENT-01
    verification:
      - kind: integration
        ref: "python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode source --site ahmet-sh"
        status: pass
      - kind: browser
        ref: "EN/TR render and console smoke check at http://127.0.0.1:3847/"
        status: pass
    human_judgment: true
  - id: D2
    description: "Robots and the one-URL sitemap preserve the single-route locale contract while the pre-existing untracked .DS_Store remains byte-for-byte and status-identical."
    requirement: VAL-01
    verification:
      - kind: integration
        ref: "custom static metadata, asset, robots, and XML sitemap audit"
        status: pass
      - kind: preservation
        ref: "git status plus SHA-256 before and after execution"
        status: pass
    human_judgment: false

completed: 2026-08-11
status: complete
---

# Phase 05 Plan 13: ahmet.sh Founder and Selected-Work Synchronization Summary

**ahmet.sh now presents a factual personal/founder identity, six registry-approved examples of selected work, and an honest single-canonical bilingual discovery contract.**

## Repository-local execution

| Evidence | Result |
|---|---|
| Repository | `/Users/ahmet/Documents/Workspaces/Buhane/ahmet.sh` |
| Branch and starting HEAD | `main`; `b131ec4` (`origin/main`) |
| Task 1 commit | `5e80d4c2391ad6293f0f9bd47312d0eb1be8934a` — `feat(05-13): establish personal founder identity` |
| Task 2 commit | `b040b1dc201dff5eaa6d3b21947dc709e857ea0f` — `feat(05-13): curate registry-backed selected work` |
| Factual-values fix | `d7b1fb2822726fc4a80f3e0405e955ab1000e393` — `fix(05-13): keep factual profile values stable` |
| Task 3 commit | `f212d0d5aa466f9d3e3c8013e3ccbe4fa0d9f4b7` — `feat(05-13): add single-route discovery files` |
| Local summary commit | `b25ed203fa4d4f10291edd1a70eec5b6cdd5017c` — `docs(05-13): record ahmet.sh portfolio execution` |
| Authoritative local summary | `/Users/ahmet/Documents/Workspaces/Buhane/ahmet.sh/.planning/phase-05-portfolio-execution-summary.md` |

## Accomplishments

- Added page-specific canonical/social metadata and a connected Person, WebSite, and Organization graph that identifies Ahmet Bütün and states the factual founder relationship to Buhane Bilgi Teknolojileri.
- Curated exactly six registry-approved work examples—Vynix, MoodJot, U2M URL Shortener, Lastimo, Swipe Slip, and Gridzle—using preferred origins and synchronized EN/TR card states.
- Added localized complete-portfolio CTAs to `https://buhane.com.tr/products/` and `https://buhane.com.tr/tr/urunler/` instead of duplicating Buhane's eleven-product directory.
- Kept `https://ahmet.sh/` as the sole canonical/indexable route, with EN/TR represented only as client-side interface states and no fabricated `/tr/` route or `hreflang`.
- Added an allow-all robots policy and a one-URL sitemap without mechanical `lastmod` values.

## Validation and render evidence

| Gate | Result |
|---|---|
| Plan Task 1/2 shell checks | Exit 0; required metadata, entity links, localized portfolio CTAs, and local icons present |
| JavaScript syntax | `node --check i18n.js` and `node --check script.js` exited 0 |
| Custom static audit | Exit 0 for title/H1/description/canonical/OG URL, JSON-LD references, six cards, local assets, safe `_blank` relations, robots, and XML sitemap |
| Local HTTP smoke | `/`, `/robots.txt`, and `/sitemap.xml` returned expected content with exit 0 |
| Browser EN/TR render | Same six card IDs and stable `2001`, `6`, `2`, and `11` values; translated identity/company copy, accessible language label, and localized portfolio destinations; no console warnings or errors |
| Central source validator | Exit 0; high=0, medium=0, low=0, info=0 |
| Independent central rerun at `f212d0d` | PASS; one indexable route and three schema nodes covering Organization, Person, and WebSite |
| Diff hygiene | `git diff --check` exited 0 |

## Deviations and follow-ups

- Local `AGENTS.md` was absent. `gsd-tools query init.quick --validate` exited 0 but reported no local roadmap, so execution followed the approved parent repository-local contract with scoped per-task commits.
- The factual-values fix removed content-changing counter/year animation so the visible start year and portfolio counts stay stable across both language states.
- No push or deployment was performed. Live discovery responses remain a deployment/release concern for Plan 05-14.

## Unrelated-dirt evidence

The only pre-existing and final ahmet.sh worktree entry was the untracked, unstaged `?? .DS_Store`. It was not edited, staged, deleted, ignored, or committed.

- Starting status: `?? .DS_Store`
- Final status: `?? .DS_Store`
- Starting SHA-256: `2a7cfd3fb555381cf70651c7a44ad09645875ed050501186c7773f4e015fee6d`
- Final SHA-256: `2a7cfd3fb555381cf70651c7a44ad09645875ed050501186c7773f4e015fee6d`

## Self-Check: PASSED

- All five exact repository-local commits are present on `main`, including the authoritative local execution-summary commit.
- Static, HTTP, browser, syntax, and central source gates pass with the recorded one-route and entity-graph evidence.
- The unchanged `.DS_Store` status/hash, no-push/no-deploy boundary, local summary path, and remaining release follow-up are recorded explicitly.
