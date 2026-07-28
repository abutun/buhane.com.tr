# Buhane.com.tr Agent Guide

<!-- GSD:project-start source:PROJECT.md -->
## Project

Buhane.com.tr is a static bilingual public company website for Buhane. Its core value is that visitors can quickly understand Buhane's services and products, then reach the correct product, service, or contact destination without stale content or broken links.

Read `.planning/PROJECT.md`, `.planning/REQUIREMENTS.md`, `.planning/ROADMAP.md`, and `.planning/STATE.md` before starting GSD-managed work.
<!-- GSD:project-end -->

<!-- GSD:stack-start source:STACK.md -->
## Technology Stack

- HTML5 documents: `index.html` and `tr/index.html`
- Shared CSS: `styles.css`
- Shared vanilla JavaScript: `script.js`
- Static assets: `images/`
- No package manager, build step, test runner, or server runtime is currently present.
<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->
## Conventions

- Update both `index.html` and `tr/index.html` for shared content changes.
- Keep product links, product names, stats, and footer entries synchronized across languages.
- Use local assets under `images/` for stable product icons where practical.
- Preserve static hosting files such as `app-ads.txt` and `yandex_abc334285efd6c2e.html`.
- Keep edits scoped; do not introduce a framework or build step unless a GSD phase explicitly calls for it.
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->
## Architecture

The site is two complete localized HTML documents sharing one stylesheet and one browser script. JavaScript behavior depends on stable IDs/classes such as `#header`, `#hamburger`, `#nav-links`, `.stat-number`, `.product-card`, and `.app-card`. Turkish page paths are root-relative, so local preview should serve the project directory as an HTTP root.
<!-- GSD:architecture-end -->

<!-- GSD:skills-start source:skills/ -->
## Project Skills

No project-local skills are defined. Use installed GSD skills when the user invokes them.
<!-- GSD:skills-end -->

<!-- GSD:workflow-start source:GSD defaults -->
## GSD Workflow Enforcement

Before file-changing work, prefer a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `/gsd:quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd:debug` for investigation and bug fixing
- `/gsd:execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->

<!-- GSD:profile-start -->
## Developer Profile

Profile not configured. Run `/gsd:profile-user` if project-specific collaboration preferences are needed.
<!-- GSD:profile-end -->
