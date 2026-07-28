# External Integrations

**Analysis Date:** 2026-07-28

## APIs & External Services

**Analytics:**
- Google Analytics - page analytics on both language pages.
  - SDK/Client: remote `gtag.js` script in `index.html` and `tr/index.html`.
  - Auth: public measurement ID configured inline; no secret is required in this codebase.

**Fonts:**
- Google Fonts - Inter font family for all site text.
  - SDK/Client: stylesheet link in `index.html` and `tr/index.html`.
  - Auth: none.

**Customer Communication:**
- OpenWidget - embedded communication widget loaded on both pages.
  - SDK/Client: inline loader in `index.html` and `tr/index.html` injects `https://cdn.openwidget.com/openwidget.js`.
  - Auth: none visible in source.

**External Product Links:**
- THECOSMICMETA.com - platform link in `index.html` and `tr/index.html`.
- U2M.io - platform link in `index.html` and `tr/index.html`.
- HiveDue - platform link in `index.html` and `tr/index.html`.
- Vynix, MoodJot, AstralPost, Gridzle, Glow Spin, and Swipe Slip - app/game portfolio links in `index.html` and `tr/index.html`.

## Data Storage

**Databases:**
- Not detected.
  - Connection: not applicable.
  - Client: not applicable.

**File Storage:**
- Static local filesystem only. Assets are committed under `images/`.
- Remote icon URLs are used for `https://vynix.app/icon-192.png`, `https://moodjot.app/icon-512.png`, and `https://gridzle.app/assets/icons/apple-touch-icon.png`.

**Caching:**
- No application-level caching is implemented.
- Browser and hosting cache behavior depends on the static host.

## Authentication & Identity

**Auth Provider:**
- Not detected.
  - Implementation: no login, session, cookie, or identity code exists in `index.html`, `tr/index.html`, `script.js`, or `styles.css`.

## Monitoring & Observability

**Error Tracking:**
- Not detected.

**Logs:**
- No explicit application logging is present.
- Browser console output is not used by `script.js`.

## CI/CD & Deployment

**Hosting:**
- Static hosting is implied, but no deployment configuration is present in this directory.
- `app-ads.txt` and `yandex_abc334285efd6c2e.html` indicate domain-level hosting requirements.

**CI Pipeline:**
- Not detected. No GitHub Actions, Bitbucket Pipelines, Netlify, Vercel, or package scripts are present.

## Environment Configuration

**Required env vars:**
- None detected.

**Secrets location:**
- No secrets files were detected in the working tree.
- Do not add API keys or private tokens to `index.html`, `tr/index.html`, `script.js`, `styles.css`, or `.planning/codebase/`.

## Webhooks & Callbacks

**Incoming:**
- None detected.

**Outgoing:**
- Browser requests go to Google Analytics, Google Fonts, OpenWidget, external product links, remote product icon URLs, LinkedIn, Twitter/X, and `mailto:info@buhane.com.tr`.

---

*Integration audit: 2026-07-28*
