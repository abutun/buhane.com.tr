# Requirements: Buhane.com.tr

**Defined:** 2026-07-28
**Core Value:** Visitors can quickly understand Buhane's work and reach the correct product, service, or contact destination without stale content or broken links.

## v1 Requirements

### Operations

- [ ] **OPS-01**: Local-only desktop and agent files are excluded without hiding GSD planning documents.
- [ ] **OPS-02**: The existing static source files and current codebase map are captured as the project baseline.
- [ ] **DEP-01**: Repository ownership, remote status, and deployment ownership are documented before commit, push, or deploy work is attempted.

### Portfolio Content

- [ ] **PORT-01**: The English page lists the current nine launched products: THECOSMICMETA.com, U2M.io, HiveDue, Vynix, MoodJot, AstralPost, Gridzle, Glow Spin, and Swipe Slip.
- [ ] **PORT-02**: The Turkish page exposes the same nine products with localized copy and the same target URLs.
- [ ] **PORT-03**: Product cards use stable local assets where practical and document any deliberate remote icon dependencies.

### Localization

- [ ] **LOC-01**: English and Turkish nav, section, CTA, product, contact, and footer structures stay in sync for shared content.
- [ ] **LOC-02**: The Products Launched stat and related portfolio counts remain consistent across both pages after product updates.

### Security and Dependencies

- [ ] **SEC-01**: Every external link opened with `target="_blank"` uses `rel="noopener noreferrer"`.
- [ ] **SEC-02**: Third-party scripts and external resource dependencies are documented with purpose, owner, and fallback expectations.

### Quality

- [ ] **QA-01**: A repeatable static validation command checks required files, local image paths, anchor targets, outbound product URLs, and basic HTML structure.
- [ ] **QA-02**: A manual smoke checklist covers desktop/mobile rendering for English and Turkish pages plus core browser interactions.
- [ ] **QA-03**: `script.js` tolerates optional or missing DOM nodes on future static pages that reuse the shared script.

### Documentation

- [ ] **DOC-01**: A content-update workflow documents how to add or update products in both languages without link or asset drift.
- [ ] **DEP-02**: Domain verification and app advertising files remain present in every release checklist.

## v2 Requirements

### Maintainability

- **DATA-01**: Move product/service/footer content into structured data and generate both language pages from one source.
- **TEST-01**: Add browser-based smoke tests across desktop and mobile viewports.
- **PERF-01**: Add responsive or modern-format variants for large images, starting with the hero background.
- **CMS-01**: Provide an authenticated content editing surface if manual HTML updates become too costly.

## Out of Scope

| Feature | Reason |
|---------|--------|
| Static site generator migration | Deferred until v1 proves validation and content workflow needs |
| Admin/CMS | Current change volume does not justify backend infrastructure |
| Backend contact form | The current mail and widget contact paths are sufficient for v1 |
| Visual redesign | Current risk is correctness and maintainability, not brand direction |
| New product creation | This roadmap covers the company website, not product development |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| OPS-01 | Phase 1 | Pending |
| OPS-02 | Phase 1 | Pending |
| DEP-01 | Phase 1 | Pending |
| PORT-01 | Phase 2 | Pending |
| PORT-02 | Phase 2 | Pending |
| PORT-03 | Phase 2 | Pending |
| LOC-01 | Phase 2 | Pending |
| LOC-02 | Phase 2 | Pending |
| SEC-01 | Phase 2 | Pending |
| QA-01 | Phase 3 | Pending |
| QA-02 | Phase 3 | Pending |
| QA-03 | Phase 3 | Pending |
| SEC-02 | Phase 4 | Pending |
| DOC-01 | Phase 4 | Pending |
| DEP-02 | Phase 4 | Pending |

**Coverage:**
- v1 requirements: 15 total
- Mapped to phases: 15
- Unmapped: 0

---
*Requirements defined: 2026-07-28*
*Last updated: 2026-07-28 after GSD new-project initialization*
