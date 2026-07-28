# Testing Patterns

**Analysis Date:** 2026-07-28

## Test Framework

**Runner:**
- Not detected.
- Config: not applicable.

**Assertion Library:**
- Not detected.

**Run Commands:**
```bash
# No project-specific test command is available.
# Manual browser inspection is currently the only validation path.
```

## Test File Organization

**Location:**
- No test files are present.

**Naming:**
- No established test naming convention.

**Structure:**
```text
buhane.com.tr/
└── No test directory or test files detected
```

## Test Structure

**Suite Organization:**
```javascript
// No existing suite pattern.
```

**Patterns:**
- No automated setup pattern.
- No automated teardown pattern.
- No assertion pattern.

## Mocking

**Framework:** Not detected.

**Patterns:**
```javascript
// No existing mocking pattern.
```

**What to Mock:**
- If tests are introduced, mock third-party browser services such as Google Analytics and OpenWidget.
- For link and DOM behavior tests, provide DOM fixtures for `#header`, `#hamburger`, `#nav-links`, `.stat-number`, and `.stagger-item`.

**What NOT to Mock:**
- Static HTML structure should be validated directly from `index.html` and `tr/index.html`.
- CSS path references and local image paths should be checked against files under `images/`.

## Fixtures and Factories

**Test Data:**
```javascript
// No existing fixtures.
```

**Location:**
- Not applicable.

## Coverage

**Requirements:** None enforced.

**View Coverage:**
```bash
# No coverage command is available.
```

## Test Types

**Unit Tests:**
- Not used.
- Candidate scope: pure DOM behavior in `script.js`, especially nav toggling, counter animation guards, and missing-element handling.

**Integration Tests:**
- Not used.
- Candidate scope: load `index.html` and `tr/index.html` in a browser and verify shared assets, language links, product links, and section anchors.

**E2E Tests:**
- Not used.
- Candidate framework: Playwright would be appropriate for a static site if a dev server is added.

## Common Patterns

**Async Testing:**
```javascript
// Future pattern: wait for IntersectionObserver-driven class changes or stub IntersectionObserver.
```

**Error Testing:**
```javascript
// Future pattern: load script.js against minimal DOM fixtures and assert no throw when optional elements are absent.
```

## Manual Verification Checklist

- Open `index.html` and verify home, services, products, about, contact, and footer render.
- Serve the directory over HTTP and open `/tr/index.html` so root-relative `/styles.css`, `/script.js`, and `/images/...` paths resolve.
- Verify product URLs for THECOSMICMETA.com, U2M.io, HiveDue, Vynix, MoodJot, AstralPost, Gridzle, Glow Spin, and Swipe Slip.
- Verify mobile nav by reducing viewport below the `@media (max-width: 768px)` breakpoint in `styles.css`.
- Verify `script.js` animations do not make content unreachable when reduced motion is enabled.

---

*Testing analysis: 2026-07-28*
