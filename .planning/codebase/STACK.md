# Technology Stack

**Analysis Date:** 2026-07-28

## Languages

**Primary:**
- HTML5 - User-facing pages in `index.html` and `tr/index.html`.
- CSS3 - Shared presentation layer in `styles.css`.
- Vanilla JavaScript - Shared browser interactions in `script.js`.

**Secondary:**
- Plain text - Ad network declaration in `app-ads.txt`.
- Static verification HTML - Yandex verification file in `yandex_abc334285efd6c2e.html`.

## Runtime

**Environment:**
- Browser runtime only. The site is served as static assets and has no detected server runtime.
- Modern browser APIs are required for `IntersectionObserver`, `scrollTo({ behavior: 'smooth' })`, CSS custom properties, CSS gradients, and DOM event handling in `script.js`.

**Package Manager:**
- Not detected.
- Lockfile: missing. No `package.json`, `package-lock.json`, `yarn.lock`, or `pnpm-lock.yaml` is present.

## Frameworks

**Core:**
- No application framework detected. Pages are hand-authored static HTML in `index.html` and `tr/index.html`.
- No component framework detected. Product, service, about, contact, and footer markup is duplicated directly in each language page.

**Testing:**
- Not detected. No Jest, Vitest, Playwright, Cypress, or other test runner config is present.

**Build/Dev:**
- Not detected. No bundler, transpiler, static site generator, minifier, or local dev server config is present.
- The production artifact is the repository working tree itself: `index.html`, `tr/index.html`, `styles.css`, `script.js`, and `images/`.

## Key Dependencies

**Critical:**
- Google Fonts Inter - loaded from `https://fonts.googleapis.com` and `https://fonts.gstatic.com` in `index.html` and `tr/index.html`.
- Google Analytics gtag.js - loaded from `https://www.googletagmanager.com/gtag/js?id=G-0G426EWLRW` in both pages.
- OpenWidget - loaded dynamically from `https://cdn.openwidget.com/openwidget.js` by inline snippets near the end of `index.html` and `tr/index.html`.

**Infrastructure:**
- Static image assets - brand, service, product, and social assets live under `images/`.
- External product icons - Vynix, MoodJot, and Gridzle cards load remote images directly in `index.html` and `tr/index.html`.
- Local product icons - AstralPost, Glow Spin, and Swipe Slip cards use `images/astralpost_icon.png`, `images/glow_spin_icon.png`, and `images/swipe_slip_icon.png`.

## Configuration

**Environment:**
- No environment variables are required by local source files.
- `.claude/settings.local.json` contains local tool permission settings for prior agent workflows, not site runtime configuration.

**Build:**
- No build config files are present.
- Shared paths differ by language page: `index.html` uses relative paths like `styles.css`, `script.js`, and `images/logo.png`; `tr/index.html` uses root-relative paths like `/styles.css`, `/script.js`, and `/images/logo.png`.

## Platform Requirements

**Development:**
- A text editor and browser are sufficient.
- Optional local preview can be done with any static HTTP server if root-relative paths in `tr/index.html` need to resolve correctly.

**Production:**
- Static hosting that serves `index.html`, `tr/index.html`, `styles.css`, `script.js`, `images/`, `app-ads.txt`, and `yandex_abc334285efd6c2e.html`.
- The host should preserve root-relative paths used by `tr/index.html`.

---

*Stack analysis: 2026-07-28*
