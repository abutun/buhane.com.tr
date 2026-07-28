# Codebase Concerns

**Analysis Date:** 2026-07-28

## Tech Debt

**No Git metadata in workspace:**
- Issue: The working directory is not a Git repository.
- Files: `.planning/codebase/`, `index.html`, `tr/index.html`, `styles.css`, `script.js`.
- Impact: GSD commit steps and user-requested commit/push operations cannot complete from this directory.
- Fix approach: Restore or clone the correct repository, or initialize Git only after confirming the intended remote.

**Manual bilingual duplication:**
- Issue: `index.html` and `tr/index.html` duplicate the full page structure.
- Files: `index.html`, `tr/index.html`.
- Impact: Product links, stats, analytics snippets, and footer entries can drift between languages.
- Fix approach: Introduce a simple data source or template generation step before adding more language variants.

**No build or validation pipeline:**
- Issue: There is no formatter, linter, HTML validator, test runner, or CI.
- Files: `styles.css`, `script.js`, `index.html`, `tr/index.html`.
- Impact: Broken links, unbalanced markup, missing localized updates, or JS regressions can ship unnoticed.
- Fix approach: Add a lightweight static validation script and optional Playwright smoke checks.

## Known Bugs

**Potential JS crash on pages without `#header`:**
- Symptoms: `handleHeaderScroll()` calls `header.classList` without checking `header`.
- Files: `script.js`.
- Trigger: Any future page loading `script.js` without an element with `id="header"`.
- Workaround: Keep `#header` on every page that loads `script.js`, or guard `handleHeaderScroll()`.

**Root-relative Turkish paths require HTTP root:**
- Symptoms: Opening `tr/index.html` directly as a file may not resolve `/styles.css`, `/script.js`, or `/images/...`.
- Files: `tr/index.html`.
- Trigger: Local file-based preview instead of serving the directory as a web root.
- Workaround: Use a local static server from the project root.

## Security Considerations

**External scripts without CSP or SRI:**
- Risk: Third-party script compromise affects site visitors.
- Files: `index.html`, `tr/index.html`.
- Current mitigation: HTTPS is used for Google Analytics and OpenWidget.
- Recommendations: Add a Content Security Policy and review whether Subresource Integrity is feasible for static external assets.

**Some `_blank` links lack `rel`:**
- Risk: Links opened with `target="_blank"` without `rel="noopener noreferrer"` can expose `window.opener`.
- Files: `index.html`, `tr/index.html`.
- Current mitigation: Some recent product links include `rel="noopener noreferrer"`.
- Recommendations: Add `rel="noopener noreferrer"` to all external `_blank` anchors, including U2M, Vynix, MoodJot, social, and footer links.

**Local agent settings in project tree:**
- Risk: `.claude/settings.local.json` may expose local tool assumptions if published.
- Files: `.claude/settings.local.json`.
- Current mitigation: The file currently contains domain allowlist settings only.
- Recommendations: Decide whether local agent settings should be committed or ignored.

## Performance Bottlenecks

**Large hero image:**
- Problem: `images/hero_background.jpg` is about 1.5 MB and 2048x1536.
- Files: `images/hero_background.jpg`.
- Cause: Large JPEG asset served without detected responsive variants.
- Improvement path: Add optimized responsive image sizes or convert to modern formats where supported.

**Remote icon dependencies:**
- Problem: Some app icons are fetched from product domains at runtime.
- Files: `index.html`, `tr/index.html`.
- Cause: Vynix, MoodJot, and Gridzle icon `img` sources point to remote domains.
- Improvement path: Mirror stable icons into `images/` to reduce runtime dependencies and layout variance.

## Fragile Areas

**Product portfolio section:**
- Files: `index.html`, `tr/index.html`, `styles.css`.
- Why fragile: It is manually duplicated across language pages and mixes platform cards with app/game cards.
- Safe modification: Update both language files, preserve `.featured-products` for platform cards and `.apps-grid` for app/game cards, then verify link parity.
- Test coverage: No automated coverage.

**Animation behavior:**
- Files: `script.js`, `styles.css`.
- Why fragile: Multiple interactions alter `transform` on cards; CSS hover and JS tilt can compete.
- Safe modification: Test card hover and mouseleave behavior after changing transforms.
- Test coverage: No automated coverage.

## Scaling Limits

**More locales:**
- Current capacity: Two full HTML documents.
- Limit: Each additional locale multiplies maintenance work.
- Scaling path: Move product/service/about/footer content into structured data and generate pages.

**More products:**
- Current capacity: Manual cards in `index.html` and `tr/index.html`.
- Limit: Product card updates require repeated HTML edits and manual link checks.
- Scaling path: Create a product data file and render cards with a static generator or lightweight build script.

## Dependencies at Risk

**Google Fonts:**
- Risk: External font request failure changes typography.
- Impact: Site falls back to system fonts.
- Migration plan: Self-host Inter if strict availability or privacy requirements are introduced.

**OpenWidget:**
- Risk: External widget loader failure or behavior change affects contact experience.
- Impact: Communication widget may not load.
- Migration plan: Keep `mailto:info@buhane.com.tr` as the primary fallback, already present in `index.html` and `tr/index.html`.

## Missing Critical Features

**Automated smoke tests:**
- Problem: There is no automated check for link parity, asset existence, or script initialization.
- Blocks: Confident commit/push and deployment validation.

**Deployment metadata:**
- Problem: No repository remote, deploy config, or CI file is present in this directory.
- Blocks: Agent-driven commit, push, and production deploy from the current checkout.

## Test Coverage Gaps

**All user-facing behavior:**
- What's not tested: Navigation, responsive menu, product links, animations, counters, and third-party script loading.
- Files: `index.html`, `tr/index.html`, `script.js`, `styles.css`.
- Risk: High for regression during manual content updates.
- Priority: High.

---

*Concerns audit: 2026-07-28*
