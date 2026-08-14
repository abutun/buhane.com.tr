---
review: 260814-csm
reviewed_at: 2026-08-14
status: issues_found
scope:
  - AstralPost 8cc4344 (parent comparison)
  - HiveDue c8aeadcf (parent comparison)
  - Root quick-task audit documentation
---

# Code review

## Findings

### P2 — Make the Hive Due production probes region-aware

`/Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/www/DEPLOY.md:108-118` presents direct `hivedue.com` canonical, robots, and sitemap checks as post-deployment assertions. The same document states that GeoIP `TR` selects `sitehesap.com`, and the authoritative Nginx example redirects every `hivedue.com` request whose host is not the selected regional host. Consequently, an operator in T\u00fcrkiye cannot make the listed Hive Due `grep` assertions: the current live probes return `301 Location: https://sitehesap.com/...` with `content-type: text/html`. This leaves the newly documented per-host discovery check unable to verify the Hive Due aliases from one of the supported regions. Require a non-TR egress/check location for the direct Hive Due assertions (and record the expected TR redirect separately), or provide an equivalent region-specific verification procedure.

### P3 — Cover every external new-tab protocol in AstralPost's regression guard

`/Users/ahmet/Documents/Workspaces/Buhane/apps/AstralPost/www/scripts/verify-content-hub.mjs:154-160` calls the checked links “external” but only selects `href=\"https://...\"`. A future `http://` external privacy-policy link with `target=\"_blank\"` bypasses the new `noopener noreferrer` assertion entirely. Broaden the selector to the external protocols the policy permits (at least `https?://`, or explicitly reject insecure `http://`) so the implementation matches the stated all-external-link guarantee.

## Evidence and passing checks

- AstralPost commit `8cc4344` changes exactly the seven existing privacy-policy new-tab links; the focused scan found `7` links and `0` without both rel tokens. `node www/scripts/verify-content-hub.mjs` passed with 112 canonical sitemap URLs and 112 JSON-LD blocks.
- Hive Due commit `c8aeadcf` removes all four source `href=\"#\"` store controls while keeping the real web-app CTA as an anchor. `npm --prefix www run check`, `npm --prefix www test` (5 files, 26 tests), and `npm --prefix www run verify:regional-assets` passed; the generated artifact keeps one shared root (85 HTML files, 26 local assets).
- The audit report correctly distinguishes source changes from a deployment and preserves The Cosmic Meta blocker. Its Table contains all 13 registry display names once and does not claim the commits are live.
- The current live evidence supports the report's Site Hesap deployment warning: on 2026-08-14, both `https://sitehesap.com/robots.txt` and `/sitemap.xml` returned `200 text/html`; direct Hive Due requests redirected to Site Hesap from this TR-region probe.

## Review result

The source fixes are otherwise scoped, localized, and build/test clean. Resolve the two documentation/coverage gaps above before treating the quick task as fully verified.
