# Coding Conventions

**Analysis Date:** 2026-07-28

## Naming Patterns

**Files:**
- Root HTML entry is `index.html`; localized Turkish entry is `tr/index.html`.
- Shared assets use lower snake_case names in `images/`, such as `digital_marketing.jpg` and `astralpost_icon.png`.
- Shared code files are plain names: `styles.css` and `script.js`.

**Functions:**
- JavaScript uses camelCase named functions inside an IIFE: `handleHeaderScroll()`, `setActiveNavLink()`, `initScrollAnimations()`, `animateCounters()`, and `initTiltEffect()` in `script.js`.

**Variables:**
- JavaScript uses camelCase constants and locals: `navLinks`, `navItems`, `scrollPos`, `targetElement`, `headerHeight`, `fadeObserver`, and `staggerObserver` in `script.js`.

**Types:**
- Not applicable. No TypeScript or explicit custom types exist.

## Code Style

**Formatting:**
- HTML, CSS, and JS use 4-space indentation in most source blocks.
- CSS groups sections with large comment banners in `styles.css`.
- HTML groups page sections with comments such as `<!-- Products Section -->` in `index.html` and `tr/index.html`.

**Linting:**
- No linting tool is configured.
- Preserve the current semicolon style in `script.js` and avoid introducing module syntax unless a build step is added.

## Import Organization

**Order:**
1. HTML head loads metadata and local CSS.
2. HTML head loads Google font preconnects and font stylesheet.
3. HTML head loads Google Analytics.
4. HTML body loads local `script.js`.
5. HTML body loads OpenWidget inline snippet near the end.

**Path Aliases:**
- Not applicable. There is no bundler or module resolver.
- English page uses relative asset paths: `styles.css`, `script.js`, `images/logo.png`.
- Turkish page uses root-relative asset paths: `/styles.css`, `/script.js`, `/images/logo.png`.

## Error Handling

**Patterns:**
- Guard optional feature setup where possible, as in `if (hamburger && navLinks)` and `if (!heroOrb) return;` in `script.js`.
- Skip invalid stat values in `animateCounters()` when parsing fails or the value contains `/`.
- Existing `handleHeaderScroll()` assumes `#header` exists; maintain `#header` on pages that load `script.js`.

## Logging

**Framework:** None.

**Patterns:**
- Do not add console logging to production interactions unless debugging a temporary issue.
- For persistent diagnostics, introduce a deliberate analytics or monitoring integration rather than ad hoc `console.log()`.

## Comments

**When to Comment:**
- Use short section comments for major HTML, CSS, and JS groups, matching existing style.
- Keep comments useful for orientation, such as `// Counter Animation for Stats` in `script.js`.

**JSDoc/TSDoc:**
- Not used.

## Function Design

**Size:** Keep browser behavior grouped by feature in `script.js`.

**Parameters:** Event handlers use standard DOM event parameters named `e`.

**Return Values:** Initialization functions mostly perform side effects and return nothing. Early returns are used for missing optional DOM elements.

## Module Design

**Exports:** Not applicable. `script.js` is an IIFE and exposes no local API.

**Barrel Files:** Not applicable.

## Change Guidance

**Bilingual Content:**
- Product, service, stat, footer, and link changes must be made in both `index.html` and `tr/index.html`.
- Keep external URLs synchronized across both language pages.

**Cards and Products:**
- Platform cards use `.product-card.featured` under `.featured-products`.
- App/game cards use `.app-card` under `.apps-grid`.
- App cards use `.product-badge.app`; game cards use `.product-badge.game`.

---

*Convention analysis: 2026-07-28*
