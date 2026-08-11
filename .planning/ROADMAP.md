# Roadmap: Buhane.com.tr

## Overview

The first milestone stabilizes the existing static bilingual website rather than redesigning it. The path starts by establishing repository/deployment ownership, then hardens portfolio content and link safety, adds repeatable validation, and finishes with release documentation that makes future product updates safer.

## Phases

**Phase Numbering:**

- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions marked with INSERTED

- [ ] **Phase 1: Planning and Repository Baseline** - Establish the project baseline, local ignore policy, and repo/deploy ownership notes.
- [ ] **Phase 2: Link, Asset, and Localization Hardening** - Make portfolio links, assets, and bilingual content parity reliable.
- [ ] **Phase 3: Static Validation and Smoke Checks** - Add repeatable validation and a manual smoke checklist.
- [ ] **Phase 4: Deployment Readiness and Maintenance Docs** - Document release checks, external dependencies, and future product update workflow.
- [ ] **Phase 5: Portfolio Discovery, Content, and Brand Network** - Make Buhane's full portfolio a truthful, crawlable, mutually reinforcing company-and-product network.

## Phase Details

### Phase 1: Planning and Repository Baseline

**Mode:** mvp
**UI hint:** no
**Goal**: Establish a trustworthy baseline for the current static site and remove ambiguity around commit, push, and deployment ownership.
**Depends on**: Nothing (first phase)
**Requirements**: OPS-01, OPS-02, DEP-01
**Success Criteria** (what must be TRUE):

  1. Project metadata describes the current static site, bilingual structure, and known blockers.
  2. Local-only files are ignored without hiding `.planning/` documents.
  3. Repository and deployment ownership questions are documented before further commit/push/deploy work.

**Plans**: 2 plans

Plans:

- [ ] 01-01: Finalize baseline docs and local ignore policy.
- [ ] 01-02: Document Git remote and deployment ownership blockers.

### Phase 2: Link, Asset, and Localization Hardening

**Mode:** mvp
**UI hint:** yes
**Goal**: Ensure every portfolio, footer, contact, and social link is correct, secure, and mirrored across English and Turkish pages.
**Depends on**: Phase 1
**Requirements**: PORT-01, PORT-02, PORT-03, LOC-01, LOC-02, SEC-01
**Success Criteria** (what must be TRUE):

  1. Users see the same ten products in English and Turkish with matching destination URLs.
  2. External links that open new tabs include `rel="noopener noreferrer"`.
  3. Product icon sources are local unless a deliberate remote dependency is documented.
  4. Portfolio counts and product naming stay consistent across both language pages.

**Plans**: 3 plans

Plans:

- [ ] 02-01: Audit and normalize product, social, footer, and contact links.
- [ ] 02-02: Mirror or document remaining remote product icon dependencies.
- [ ] 02-03: Verify English/Turkish product and stat parity.

### Phase 3: Static Validation and Smoke Checks

**Mode:** mvp
**UI hint:** no
**Goal**: Add a lightweight validation path that catches common static-site regressions before release.
**Depends on**: Phase 2
**Requirements**: QA-01, QA-02, QA-03
**Success Criteria** (what must be TRUE):

  1. A repeatable command verifies required files, local asset references, anchor targets, key outbound URLs, and basic HTML structure.
  2. A manual checklist covers English/Turkish desktop and mobile rendering plus mobile nav, smooth scroll, counters, and card interactions.
  3. Shared JavaScript does not throw when optional DOM elements are missing on future pages.

**Plans**: 2 plans

Plans:

- [ ] 03-01: Add static validation tooling for links, assets, anchors, and HTML structure.
- [ ] 03-02: Harden shared JavaScript and write the manual smoke checklist.

### Phase 4: Deployment Readiness and Maintenance Docs

**Mode:** mvp
**UI hint:** no
**Goal**: Make future releases and product-content updates repeatable without relying on session memory.
**Depends on**: Phase 3
**Requirements**: SEC-02, DOC-01, DEP-02
**Success Criteria** (what must be TRUE):

  1. Third-party browser dependencies are documented with purpose and fallback expectations.
  2. The release checklist preserves `app-ads.txt` and `yandex_abc334285efd6c2e.html`.
  3. The product update guide tells maintainers exactly where to edit EN/TR content, links, images, stats, and validation checks.

**Plans**: 2 plans

Plans:

- [ ] 04-01: Document external dependencies and deployment/release checklist.
- [ ] 04-02: Write the product content-update guide.

### Phase 5: Portfolio Discovery, Content, and Brand Network

**Mode:** mvp
**UI hint:** no
**Goal**: Make Buhane and its eleven products a coherent, truthful, crawlable brand network that helps search engines, answer engines, and prospective customers understand ownership, product fit, and the correct next destination.
**Depends on**: Phases 1-4 foundations; Phase 5 plans may implement any still-missing prerequisite in the same touched surface.
**Requirements**: DISC-01, DISC-02, HUB-01, ENT-01, TECH-01, LOCALE-03, CONT-01, LINK-01, AIPOL-01, MEAS-01, VAL-01, EXT-01
**Success Criteria** (what must be TRUE):

  1. The private registry and validators agree on all eleven products, preferred origins, lifecycle states, locales, reviewed claims, and allowed relationships.
  2. Buhane has crawlable bilingual organization, portfolio, and product-detail content with correct canonical, language, social, and structured-data signals.
  3. Every editable product site visibly identifies Buhane and uses contextual—not blanket reciprocal—portfolio links.
  4. Canonicals, robots, sitemaps, schema URLs, and public links use preferred origins; auth, admin, redirect, and non-indexable shells are excluded correctly.
  5. Content changes describe released product reality, add specific user value, and preserve existing localization and generator contracts.
  6. Central and repository-native validation commands pass without overwriting pre-existing user changes.
  7. The Cosmic Meta source-access exception and crawler/measurement follow-up actions are documented precisely rather than silently skipped.

**Plans**: 14/14 plans executed

Plans:

- [x] 05-01-PLAN.md
- [x] 05-02-PLAN.md
- [x] 05-03-PLAN.md
- [x] 05-04-PLAN.md
- [x] 05-05-PLAN.md
- [x] 05-06-PLAN.md
- [x] 05-07-PLAN.md
- [x] 05-08-PLAN.md
- [x] 05-09-PLAN.md
- [x] 05-10-PLAN.md
- [x] 05-11-PLAN.md
- [x] 05-12-PLAN.md
- [x] 05-13-PLAN.md
- [x] 05-14-PLAN.md
- [ ] TBD (run /gsd-plan-phase 5 to break down)

## Progress

**Execution Order:**
Phases execute in numeric order: 1 -> 2 -> 3 -> 4 -> 5

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Planning and Repository Baseline | 0/2 | Not started | - |
| 2. Link, Asset, and Localization Hardening | 0/3 | Not started | - |
| 3. Static Validation and Smoke Checks | 0/2 | Not started | - |
| 4. Deployment Readiness and Maintenance Docs | 0/2 | Not started | - |
| 5. Portfolio Discovery, Content, and Brand Network | 14/14 | In Progress|  |
