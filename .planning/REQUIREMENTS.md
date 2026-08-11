# Requirements: Buhane.com.tr

**Defined:** 2026-07-28
**Core Value:** Visitors can quickly understand Buhane's work and reach the correct product, service, or contact destination without stale content or broken links.

## v1 Requirements

### Operations

- [ ] **OPS-01**: Local-only desktop and agent files are excluded without hiding GSD planning documents.
- [ ] **OPS-02**: The existing static source files and current codebase map are captured as the project baseline.
- [ ] **DEP-01**: Repository ownership, remote status, and deployment ownership are documented before commit, push, or deploy work is attempted.

### Portfolio Content

- [ ] **PORT-01**: The English page lists the current eleven launched products: The Cosmic Meta, U2M, Hive Due, Vynix, MoodJot, Astral Post, Lastimo, Gridzle, Glow Spin, Swipe Slip, and Hoşkin.
- [ ] **PORT-02**: The Turkish page exposes the same eleven products with localized copy and the same preferred target URLs.
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

### Portfolio Discovery Network

- [x] **DISC-01**: A private portfolio registry records every brand's owner, lifecycle state, preferred and legacy origins, locales, approved destinations, and reviewed product claims.
- [x] **DISC-02**: Canonical, sitemap, social, structured-data, and portfolio-link URLs use each product's preferred HTTPS origin; legacy domains are treated only as redirects.
- [x] **HUB-01**: Buhane provides substantial crawlable English and Turkish company, portfolio, and product-detail content for all eleven products.
- [x] **ENT-01**: Buhane, Ahmet, and product sites expose truthful, consistent visible ownership relationships and stable structured-data entity identifiers.
- [x] **TECH-01**: Every editable public site has page-specific titles and descriptions, canonical metadata, appropriate structured data, robots rules, and a canonical-only sitemap for its public architecture.
- [x] **LOCALE-03**: Only stable, independently addressable localized pages receive reciprocal self-referential `hreflang`; client-side language states are not presented as separate indexed documents.
- [x] **CONT-01**: Guides, use cases, FAQs, glossaries, and editorial pages are factual, attributable, useful in product context, and constrained to reviewed released capabilities.
- [x] **LINK-01**: Every editable product site visibly identifies Buhane as owner or publisher, while sibling links are contextual and allowlisted instead of repeated portfolio-wide footer exchanges.
- [x] **AIPOL-01**: Search/citation crawler access and model-training crawler policy are documented separately; any optional `llms.txt` is accurate and is not treated as an indexing requirement.
- [x] **MEAS-01**: A privacy-safe measurement contract defines search, AI-referral, portfolio-click, and conversion signals without transmitting product user content.
- [x] **VAL-01**: Central source/live validation and each repository's native generator, test, or verification commands catch canonical, sitemap, locale, schema, link, asset, and product-truth regressions.
- [x] **EXT-01**: The Cosmic Meta is not edited through an unrelated local directory; the stale live-domain discovery data is documented as blocked until the real WordPress administration or deploy source is available.

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
| DISC-01 | Phase 5 | Complete |
| DISC-02 | Phase 5 | Complete |
| HUB-01 | Phase 5 | Complete |
| ENT-01 | Phase 5 | Complete |
| TECH-01 | Phase 5 | Complete |
| LOCALE-03 | Phase 5 | Complete |
| CONT-01 | Phase 5 | Complete |
| LINK-01 | Phase 5 | Complete |
| AIPOL-01 | Phase 5 | Complete |
| MEAS-01 | Phase 5 | Complete |
| VAL-01 | Phase 5 | Complete |
| EXT-01 | Phase 5 | Complete |

**Coverage:**

- v1 requirements: 27 total
- Mapped to phases: 27
- Unmapped: 0

---
*Requirements defined: 2026-07-28*
*Last updated: 2026-08-11 for Phase 5 portfolio discovery network*
