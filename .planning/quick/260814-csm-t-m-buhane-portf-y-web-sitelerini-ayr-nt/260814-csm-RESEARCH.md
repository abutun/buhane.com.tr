# Portfolio-wide website audit — research

**Date:** 2026-08-14
**Scope:** Buhane, ahmet.sh, MoodJot, Vynix, Swipe Slip, Glow Spin, Hive Due / Site Hesap, AstralPost, Gridzle, Hoşkin, Lastimo, The Cosmic Meta, and U2M.
**Boundary:** Read-only source and live HTTP audit. No product-source or deployment files were changed by this research pass.

## Executive result

The existing portfolio discovery work remains materially sound in editable source: all twelve editable properties have crawlable preferred roots, source `robots.txt`/sitemap artifacts, canonical metadata, HTTPS public links, and appropriate ownership/content surfaces. Sitemap inventories match the current intended public route counts:

| Property | Sitemap URL count | Result |
|---|---:|---|
| Buhane | 26 | Pass |
| ahmet.sh | 1 | Pass |
| MoodJot | 99 | Pass |
| Vynix | 74 | Pass |
| Swipe Slip | 13 | Pass |
| Glow Spin | 20 | Pass |
| Hive Due / Site Hesap | 42 + 42 host-qualified | Source pass; live deployment issue below |
| AstralPost | 112 | One safe source fix below |
| Gridzle | 5 | Pass |
| Hoşkin | 80 | Pass |
| Lastimo | 157 | Pass |
| U2M | 7 | Pass |

Static scans of public HTML (excluding dependency directories) found no `http://` asset/link URLs and no missing `alt` attributes outside a noindex admin page. Existing locale output uses regional tags where relevant (`pt-BR`, `zh-Hans`, `tr-TR`), rather than a localization regression. Root HTTP responses for all editable sites are currently HTTPS 200 and carry HSTS; this alone is not enough to change the registry's deliberate `deployment_pending` state to `deployed_verified`.

## Source fixes to make

### 1. AstralPost: secure every external privacy-policy tab

**State:** source gap — safe to fix.
**Evidence:** [`www/privacy/index.html`](../../../../../../apps/AstralPost/www/privacy/index.html) has seven external `target="_blank"` links (Firebase, OpenAI, RevenueCat, and Google policy references in English/Turkish) without `rel="noopener noreferrer"`; examples are lines 165, 167, 169, 171, 251, 253, and 255.
**Remedy:** Add `rel="noopener noreferrer"` to every one of these links. This is a direct static source file, so no generated editorial artifact needs hand-editing.

### 2. Hive Due / Site Hesap: prevent visible placeholder controls from navigating to `#`

**State:** source gap — safe to fix.
**Evidence:** [`src/components/AppStoreBadges.astro`](../../../../../../apps/HiveDue/www/src/components/AppStoreBadges.astro) lines 43 and 57 render Google Play/App Store badges as active `href="#"` anchors. [`src/components/Footer.astro`](../../../../../../apps/HiveDue/www/src/components/Footer.astro) lines 48 and 57 do the same. All labels say “Coming soon”/“Yakında”, so a click currently only changes the fragment or scroll position.

**Remedy:** Render unavailable store entries as semantic non-interactive text/badges (or disabled controls without an `href`) until a real store URL exists. Rebuild the single shared `www/dist/` artifact once; do not add separate Site Hesap/Hive Due distributions.

## Deployment / external follow-ups

### Hive Due / Site Hesap discovery endpoints are misconfigured live

**State:** deploy pending / live configuration failure; source contract is correct.
**Evidence:** On 2026-08-14, both `https://sitehesap.com/robots.txt` and `https://sitehesap.com/sitemap.xml` returned `HTTP 200` with `content-type: text/html` and the Turkish home document (`<!DOCTYPE html><html lang="tr" ...>`), not a robots or XML document. The shared artifact contains the correct host-qualified backing files: `dist/robots-sitehesap.txt` (67 bytes), `dist/sitemap-sitehesap.xml` (2938 bytes), `dist/robots-hivedue.txt` (65 bytes), and `dist/sitemap-hivedue.xml` (2980 bytes).

**Remedy:** Apply the existing authoritative [`deployment/nginx-hivedue-sitehesap.conf.example`](../../../../../../apps/HiveDue/www/deployment/nginx-hivedue-sitehesap.conf.example) mapping on the live server. It must expose host-local `/robots.txt` and `/sitemap.xml`, serve the one `current` shared artifact root, and keep Hive Due `/` host-locally redirecting to `/en/`. Validate from a non-TR region as well as Türkiye: the GeoIP contract intentionally sends Turkish traffic from `hivedue.com` to Site Hesap, so the observed root redirect from this Türkiye audit location is not itself a source defect.

### The Cosmic Meta remains externally blocked and does not express the portfolio owner relationship

**State:** external blocker.
**Evidence:** No approved source root exists in the registry. The live WordPress homepage is reachable and has Yoast canonical/schema/sitemap discovery, but presents its entity as “Cosmic Meta Digital”/“Cosmic Meta AI”; no visible or structured-data relationship to `https://buhane.com.tr/#organization` was found. The site only references the Buhane CDN in image URLs.

**Remedy:** Obtain the documented WordPress/admin/deploy/DNS access package before changing this property. Then decide the public naming, add a truthful Buhane publisher/owner relationship and a visible company link, and revalidate its Yoast schema/sitemap. Do not use the unrelated local `cosmicmeta*` directories as a proxy source.

## Per-property audit record

| Property | State | Evidence and next action |
|---|---|---|
| Buhane Bilgi Teknolojileri | Pass / deployment verification pending | 26 EN/TR hub/detail URLs; root metadata, canonical, robots, and XML sitemap return correctly. No safe source change found. |
| ahmet.sh | Pass / deployment verification pending | Single canonical Person/selected-work surface; root, robots, and sitemap return correctly. No safe source change found. |
| MoodJot | Pass / deployment verification pending | 99 sitemap routes; localized editorial routes and card surfaces are present. Public/referral/admin operational pages are noindexed as intended. |
| Vynix | Pass / deployment verification pending | 74 sitemap routes and localized docs/blog/glossary inventories are present. Preserve the pre-existing admin build dirt below. |
| Swipe Slip | Pass / deployment verification pending | 13 discovery URLs; preferred metadata and HTTPS store/cross-product links remain present. |
| Glow Spin | Pass / deployment verification pending | 20 discovery URLs; current compact store CTAs and metadata are present. |
| Hive Due / Site Hesap | Source gap + deploy pending | Replace the four `href="#"` placeholder store controls; deploy the already-documented host-qualified robots/sitemap mapping. Keep one shared `dist/`. |
| AstralPost | Source gap | Add secure `rel` values to seven privacy-page external links; 112 sitemap URLs otherwise align. |
| Gridzle | Pass / deployment verification pending | Five-route discovery surface is intact. Preserve active `.gsd/` work and do not include it in this task. |
| Hoşkin | Pass / deployment verification pending | 80 multilingual canonical routes and game-content output are present. No safe source change found. |
| Lastimo | Pass / deployment verification pending | 157 locale-aware public routes and truthful bounded product content are present. No safe source change found. |
| The Cosmic Meta | External blocker | Live site is active, but source access and ownership/entity alignment are unavailable. |
| U2M URL Shortener | Pass / deployment verification pending | Seven public landing/docs/use-case routes and discovery files are present. No regression found in the previous footer-link affordance change. |

## Protected concurrent/user changes observed

Do not stage, regenerate over, revert, or absorb these paths into this quick task:

- `buhane.com.tr/.planning/quick/260814-csm-t-m-buhane-portf-y-web-sitelerini-ayr-nt/` is the current GSD quick-task workspace.
- `apps/Vynix/www/admin/dist/index.html` is pre-existing modified output. It now references `index-CP0TUwsQ.js`; the admin asset directory is ignored/untracked, so it is not safe to normalize as part of website audit work.
- `games/Gridzle/.gsd/dispatch-isolation-sentinel.json` is untracked concurrent GSD state; its `develop` branch is also five commits ahead of `origin/develop`.

## Recommended validation after the two source fixes

1. Run the relevant native checks without rewriting unrelated generated artifacts: AstralPost content-hub verifier and Hive Due `npm run check`, `npm test`, and shared-artifact verification after the single build.
2. Recheck every changed page for external-link security and literal `href="#"` anchors.
3. After an authorized Hive server deployment, prove `sitehesap.com/robots.txt` is `text/plain`, `sitehesap.com/sitemap.xml` is XML, and the matching Hive Due endpoints resolve to the Hive-qualified files from an appropriate non-TR location.
4. Leave all other properties unchanged unless a native validation fails; the audit did not find a factual reason to add speculative content or redesigns.
