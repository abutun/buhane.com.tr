# Buhane.com.tr

## What This Is

Buhane.com.tr is Buhane's bilingual public company website for presenting services, platforms, apps, games, and contact paths. It serves prospective clients, partners, and product visitors who need to understand what Buhane builds and reach the right external product or contact destination.

## Core Value

Visitors can quickly understand Buhane's work and reach the correct product, service, or contact destination without stale content or broken links.

## Business Context

- **Customer**: Prospective software, AI, e-commerce, and digital marketing clients; product visitors exploring Buhane-owned products.
- **Revenue model**: Indirect lead generation, portfolio credibility, and product discovery.
- **Success metric**: Correct product/contact link engagement with no stale bilingual portfolio content.
- **Strategy notes**: No external strategy document is present in this workspace.

## Requirements

### Validated

- [x] English and Turkish landing pages exist and share the same CSS/JavaScript surface.
- [x] Public sections cover hero, services, products, about, contact, and footer content.
- [x] The portfolio includes platform cards and app/game cards with outbound product links.
- [x] Browser interactions cover mobile navigation, smooth scrolling, active nav state, reveal animations, stat counters, and card effects.
- [x] Google Analytics, OpenWidget, app advertising, and Yandex verification assets are present.

### Active

- [ ] Keep the current ten launched products synchronized across English and Turkish pages.
- [ ] Harden product, social, footer, and contact links so they are secure and correct.
- [ ] Add lightweight static validation for links, local assets, anchor targets, and language parity.
- [ ] Document repository, deployment, and content-update ownership so commit/push/deploy work is repeatable.

### Out of Scope

- Static site generator or framework migration - useful later, but v1 should stabilize the current static site first.
- CMS/admin editing - too much infrastructure for the current maintenance workflow.
- Backend services, auth, forms, or databases - the current site is a static public website.
- Visual redesign - not required to make current portfolio maintenance safe.
- New product launches - product creation is separate from this website maintenance milestone.

## Context

The codebase is a static HTML/CSS/JavaScript site with no package manager, build step, test runner, or deployment metadata. English content lives in `index.html`; Turkish content lives in `tr/index.html`; shared styling and behavior live in `styles.css` and `script.js`. A GSD codebase map exists under `.planning/codebase/` and identifies three important risks: no Git metadata in this workspace, manual bilingual duplication, and no automated validation pipeline.

Recent portfolio updates added Gridzle, AstralPost, HiveDue, Lastimo, THECOSMICMETA.com naming, local icons for AstralPost/Glow Spin/Swipe Slip/Lastimo, the Products Launched stat of 10, and corrected Glow Spin and Swipe Slip URLs.

## Constraints

- **Tech stack**: Stay in static HTML, CSS, and vanilla JavaScript for v1 - there is no build pipeline to absorb framework churn safely.
- **Localization**: Any user-facing content change must be mirrored in `index.html` and `tr/index.html` - the pages are manually duplicated.
- **Paths**: `tr/index.html` uses root-relative asset paths - local validation should use an HTTP server rooted at the project directory.
- **Git**: This workspace currently has no Git metadata or remote - commit/push/deploy tasks require repository ownership to be established.
- **External dependencies**: Google Fonts, Google Analytics, OpenWidget, and some product domains are runtime dependencies - document purpose and fallbacks before tightening policy.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Keep the site static for v1 | The current site is small and already works without a build step | Pending |
| Treat EN/TR parity as a first-class requirement | Manual duplication is the main regression risk | Pending |
| Track GSD docs in version control | The user has requested commit/push workflow, and planning docs should survive sessions | Pending |
| Use `AGENTS.md` for project guidance | Codex runtime expects this instruction file | Pending |
| Skip external research during init | The brownfield codebase map is current and enough for a maintenance roadmap | Pending |

---
*Last updated: 2026-08-03 after quick task 260803-s03*
