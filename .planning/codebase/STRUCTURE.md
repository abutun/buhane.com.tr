# Codebase Structure

**Analysis Date:** 2026-07-28

## Directory Layout

```text
buhane.com.tr/
├── index.html                         # English landing page
├── tr/
│   └── index.html                     # Turkish landing page
├── styles.css                         # Shared visual system and responsive layout
├── script.js                          # Shared browser interactions
├── images/                            # Logos, social icons, service media, app icons
├── app-ads.txt                        # Ad network declaration
├── yandex_abc334285efd6c2e.html       # Yandex verification file
├── .claude/
│   └── settings.local.json            # Local agent/tool settings
└── .planning/
    └── codebase/                      # Generated GSD codebase map
```

## Directory Purposes

**Root:**
- Purpose: Static site root and public production artifact.
- Contains: HTML entry point, shared CSS/JS, domain-level verification files.
- Key files: `index.html`, `styles.css`, `script.js`, `app-ads.txt`, `yandex_abc334285efd6c2e.html`.

**`tr/`:**
- Purpose: Turkish localized page.
- Contains: `tr/index.html`.
- Key files: `tr/index.html`.

**`images/`:**
- Purpose: Public static image assets.
- Contains: JPG service imagery, PNG logos, social icons, favicon, product icons.
- Key files: `images/logo.png`, `images/favicon.png`, `images/hero_background.jpg`, `images/astralpost_icon.png`, `images/glow_spin_icon.png`, `images/swipe_slip_icon.png`.

**`.claude/`:**
- Purpose: Local AI tool settings.
- Contains: `settings.local.json`.
- Key files: `.claude/settings.local.json`.

**`.planning/codebase/`:**
- Purpose: GSD-generated reference documents.
- Contains: `STACK.md`, `INTEGRATIONS.md`, `ARCHITECTURE.md`, `STRUCTURE.md`, `CONVENTIONS.md`, `TESTING.md`, `CONCERNS.md`.

## Key File Locations

**Entry Points:**
- `index.html`: English public entry point.
- `tr/index.html`: Turkish public entry point.

**Configuration:**
- `.claude/settings.local.json`: Local agent permissions, not production runtime config.
- `app-ads.txt`: Public advertising declaration.
- `yandex_abc334285efd6c2e.html`: Public site ownership verification.

**Core Logic:**
- `script.js`: Navigation, scroll, animation, counter, ripple, and tilt behavior.
- `styles.css`: All layout, theme, and responsive behavior.

**Testing:**
- Not detected. No test files or test config exist.

## Naming Conventions

**Files:**
- Public entry pages use `index.html`.
- Static assets use descriptive snake_case names, such as `hero_background.jpg`, `glow_spin_icon.png`, and `swipe_slip_icon.png`.
- Legacy/social assets use direct names such as `facebook_icon.png`, `twitter_icon.png`, and `linkedin_icon.png`.

**Directories:**
- Language directory uses a two-letter locale code: `tr/`.
- Asset directory uses generic plural noun: `images/`.

## Where to Add New Code

**New Product or Portfolio Item:**
- English markup: update the relevant products section in `index.html`.
- Turkish markup: mirror the change in `tr/index.html`.
- Local icon asset: add to `images/` and reference as `images/...` in `index.html` and `/images/...` in `tr/index.html`.

**New Section:**
- Markup: add matching sections to `index.html` and `tr/index.html`.
- Styling: add CSS to `styles.css`, grouped near the matching section if possible.
- Behavior: add JS to `script.js` only when CSS/HTML cannot handle it.

**Utilities:**
- Shared browser behavior belongs in `script.js`.
- Shared styles belong in `styles.css`.

## Special Directories

**`images/`:**
- Purpose: Public static media.
- Generated: No.
- Committed: Yes, expected to be deployed.

**`.planning/`:**
- Purpose: GSD project intelligence.
- Generated: Yes.
- Committed: Intended by GSD, but this workspace currently has no Git repository metadata.

**`.claude/`:**
- Purpose: Local tool configuration.
- Generated: Yes or agent-managed.
- Committed: Unknown; treat as local unless a repository policy says otherwise.

---

*Structure analysis: 2026-07-28*
