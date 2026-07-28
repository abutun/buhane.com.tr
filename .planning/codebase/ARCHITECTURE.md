<!-- refreshed: 2026-07-28 -->
# Architecture

**Analysis Date:** 2026-07-28

## System Overview

```text
┌─────────────────────────────────────────────────────────────┐
│                    Static Site Documents                     │
├───────────────────────────┬─────────────────────────────────┤
│ English page              │ Turkish page                     │
│ `index.html`              │ `tr/index.html`                  │
└──────────────┬────────────┴───────────────┬─────────────────┘
               │                            │
               ▼                            ▼
┌─────────────────────────────────────────────────────────────┐
│              Shared Presentation and Behavior                │
│              `styles.css` + `script.js`                      │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│             Static Assets and External Browser Services       │
│             `images/`, Google Analytics, OpenWidget           │
└─────────────────────────────────────────────────────────────┘
```

## Component Responsibilities

| Component | Responsibility | File |
|-----------|----------------|------|
| English landing page | Main English content, portfolio, contact, footer, analytics and widget snippets | `index.html` |
| Turkish landing page | Turkish localized equivalent of the landing page | `tr/index.html` |
| Shared styling | Theme variables, layout, product cards, responsive breakpoints, animations | `styles.css` |
| Shared interaction layer | Header state, mobile menu, active nav, smooth scroll, scroll animations, counters, card tilt | `script.js` |
| Static assets | Logos, service images, social icons, app icons, hero image | `images/` |

## Pattern Overview

**Overall:** Static bilingual single-page marketing site.

**Key Characteristics:**
- Each language page is a full HTML document with duplicated section structure.
- Styling is centralized in `styles.css`.
- Client behavior is centralized in `script.js` and depends on shared IDs/classes.
- There is no data layer, template layer, API layer, or build step.

## Layers

**Document Layer:**
- Purpose: Defines semantic content, language copy, product cards, footer links, and third-party script tags.
- Location: `index.html`, `tr/index.html`.
- Contains: Header, hero, services, products, about, contact, footer, analytics loader, OpenWidget loader.
- Depends on: `styles.css`, `script.js`, remote Google/OpenWidget scripts, `images/`.
- Used by: Browser directly.

**Presentation Layer:**
- Purpose: Defines visual system and responsive layout.
- Location: `styles.css`.
- Contains: CSS custom properties, grids, cards, badges, button styles, animations, responsive breakpoints.
- Depends on: HTML class names and IDs in `index.html` and `tr/index.html`.
- Used by: Both language pages.

**Interaction Layer:**
- Purpose: Adds browser-side progressive behavior.
- Location: `script.js`.
- Contains: Event listeners, `IntersectionObserver` animations, mobile nav toggling, stat counters, tilt/ripple effects.
- Depends on: DOM elements with IDs `header`, `hamburger`, `nav-links` and classes such as `.fade-in`, `.stagger-item`, `.stat-number`.
- Used by: Both language pages.

**Asset Layer:**
- Purpose: Provides local media and icons.
- Location: `images/`.
- Contains: JPG service images, PNG logos, PNG app icons, social icons, favicon.
- Depends on: HTML references and CSS image sizing.
- Used by: HTML content and browser rendering.

## Data Flow

### Primary Page Load Path

1. Browser requests a language page: `index.html` or `tr/index.html`.
2. HTML loads shared stylesheet: `styles.css` for English, `/styles.css` for Turkish.
3. HTML loads shared script: `script.js` for English, `/script.js` for Turkish.
4. Browser fetches local assets from `images/` and remote assets from product domains where used.
5. Inline snippets load Google Analytics and OpenWidget.
6. `script.js` initializes after DOM readiness and attaches event listeners.

### Navigation and Animation Flow

1. Header scroll state is toggled by `handleHeaderScroll()` in `script.js`.
2. Anchor clicks are intercepted by the smooth-scroll block in `script.js`.
3. `IntersectionObserver` reveals `.fade-in`, `.fade-in-left`, `.fade-in-right`, and `.stagger-item` elements.
4. Product and stat cards receive tilt effects via `.service-card`, `.product-card`, `.app-card`, and `.stat-card` selectors.

**State Management:**
- DOM state only. Classes such as `.scrolled`, `.nav-active`, `.active`, and `.visible` are the state mechanism.
- No persistent storage, cookies, local storage, or server state is used by local code.

## Key Abstractions

**CSS Class Contracts:**
- Purpose: Keep JS and CSS behavior attached to semantic sections.
- Examples: `.nav-links`, `.stagger-item`, `.product-card`, `.app-card`, `.stat-number` in `index.html`, `tr/index.html`, `styles.css`, and `script.js`.
- Pattern: Shared class names are the integration boundary between HTML, CSS, and JS.

**Language Document Pair:**
- Purpose: Maintain English and Turkish variants.
- Examples: `index.html` and `tr/index.html`.
- Pattern: Manual duplication with localized text and path differences.

## Entry Points

**English page:**
- Location: `index.html`.
- Triggers: Request to site root.
- Responsibilities: English content, relative asset references, analytics/widget bootstrapping.

**Turkish page:**
- Location: `tr/index.html`.
- Triggers: Request to `/tr/index.html`.
- Responsibilities: Turkish content, root-relative shared asset references, analytics/widget bootstrapping.

**Shared JavaScript:**
- Location: `script.js`.
- Triggers: `<script src="script.js">` or `<script src="/script.js">`.
- Responsibilities: All local interactions.

## Architectural Constraints

- **Threading:** Single-threaded browser event loop.
- **Global state:** `window.dataLayer`, `gtag`, and `window.OpenWidget` are globals introduced by inline snippets in `index.html` and `tr/index.html`.
- **Circular imports:** Not applicable; there are no modules or imports.
- **Path model:** English page uses relative paths; Turkish page uses root-relative paths. Keep this split unless the site is refactored.
- **Localization model:** Text is duplicated manually across pages. Any content change must be applied to both `index.html` and `tr/index.html`.

## Anti-Patterns

### One-Language-Only Updates

**What happens:** A section is changed in `index.html` but not mirrored in `tr/index.html`.
**Why it's wrong:** The language variants drift and users see inconsistent product lists or stats.
**Do this instead:** Update the matching section in both `index.html` and `tr/index.html`.

### Script Selectors Without Markup Check

**What happens:** `script.js` assumes `header` exists before calling `header.classList.add()` in `handleHeaderScroll()`.
**Why it's wrong:** If a future page reuses `script.js` without `#header`, it will throw.
**Do this instead:** Either keep `#header` on every page that loads `script.js`, or guard `handleHeaderScroll()` before using `header`.

## Error Handling

**Strategy:** Minimal browser-side defensive checks.

**Patterns:**
- `script.js` checks for `hamburger` and `navLinks` before mobile menu setup.
- `initParallax()` returns early if `.hero-orb` is missing.
- Stat counters skip values that are time-like, such as `24/7`.

## Cross-Cutting Concerns

**Logging:** None in local code.
**Validation:** Not applicable; no form submission or user input processing exists.
**Authentication:** Not applicable; public static site.

---

*Architecture analysis: 2026-07-28*
