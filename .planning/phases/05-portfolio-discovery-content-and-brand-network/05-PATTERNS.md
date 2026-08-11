# Phase 5 Pattern Map: Portfolio Discovery, Content, and Brand Network

**Mapped:** 2026-08-11  
**Scope:** The eleven Phase 5 properties plus the Buhane company hub and `ahmet.sh`  
**Purpose:** Give the Phase 5 planner exact edit boundaries, reusable implementation patterns, verification commands, collision risks, and plan-sized file clusters.

This is an implementation map, not a new product-truth source. The locked decisions in `05-CONTEXT.md` and the evidence and preferred origins in `05-RESEARCH.md` remain authoritative. In particular:

- Buhane is the central owner/publisher. Product sites should link naturally to Buhane, not become a sitewide directory of every sibling product.
- Search and AI discovery use the same crawlable, canonical, factual foundation. No invented AI-specific schema or unsupported `llms.txt` ranking claim belongs in the plans.
- Stable locale URLs may receive `hreflang`; client-side language switches on one URL may not.
- Lastimo claims must be reduced to the implemented v1 described by its repository instructions before its public pages are regenerated.
- The Cosmic Meta has no verified local source or admin access and is an explicit external blocker, not an invitation to edit similarly named legacy directories.
- User changes and current dirty files must be preserved. Generated-output tools must run only inside their documented boundary.

## 1. Repository and Publication Boundary Matrix

Paths below are exact local roots. “Tracked generated” means the files are committed but must be changed through their generator. “Ignored generated” means never patch or commit the output.

| Property | Repository / public root | Authoritative inputs | Generated or deployed outputs | Boundary and cautions |
|---|---|---|---|---|
| MoodJot | `/Users/ahmet/Documents/Workspaces/Buhane/apps/MoodJot` / `www/` | `www/**/*.html`, `www/styles.css`, `www/script.js`, `www/robots.txt`, `www/sitemap.xml`, local assets | None found; the public tree is hand-authored | Edit public files directly. Keep `www/admin/**`, referral routes, and app flows outside broad SEO rewrites. Client-side EN/TR/ES/RU/ZH/DE/FR/PT switching is one URL, not eight indexable locales. |
| Vynix | `/Users/ahmet/Documents/Workspaces/Buhane/apps/Vynix` / `www/` | Hand-authored `www/index.html`, legal/support/docs pages and assets; generated-content source is embedded in `www/scripts/build-seo-content.mjs` | **Tracked generated:** `www/blog/index.html`, `www/blog/*.html`, `www/glossary/index.html`, `www/robots.txt`, `www/sitemap.xml`. **Admin:** `www/admin/src/**` builds `www/admin/dist/index.html` separately. | Change generated SEO pages only through `build-seo-content.mjs`. Never let the public generator touch `admin/dist`; that tracked artifact is already dirty. The generator currently uses `https://www.vynix.app`; Phase 5 must choose one `www` policy and enforce it consistently. |
| Swipe Slip | `/Users/ahmet/Documents/Workspaces/Buhane/games/Swipe-Slip` / `www/` | `www/*.html`, `www/blog/*.html`, `www/styles.css`, `www/robots.txt`, `www/sitemap.xml`, assets | None found; hand-authored static files deploy directly | Edit directly. Existing public footer is copied across pages and contains blanket sibling links and a stale `cosmicmeta.ai` owner link. The public site shares a repository with application code, so path-scope all commits. |
| Glow Spin | `/Users/ahmet/Documents/Workspaces/Buhane/games/Glow-Spin` / `www/` | `www/**/*.html`, `www/styles.css`, `www/robots.txt`, `www/sitemap.xml`, assets | None found; hand-authored static files deploy directly | Edit directly. Existing footer is repeated and links several siblings; replace with a focused Buhane owner relationship instead of expanding it. Home has no JSON-LD even though many secondary pages do. |
| Hive Due / Site Hesap | `/Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue` / `www/` | Astro inputs in `www/src/pages/**`, `src/layouts/**`, `src/components/**`, `src/data/**`, `src/i18n/{en,tr}.json`, `src/styles/**`; `www/public/**`; `astro.config.mjs` | **Ignored generated:** `www/dist/**`, `www/.astro/**`; dependency output `node_modules/**` | Never edit `dist`. Astro’s sitemap integration builds the sitemap. Current browser-time host rewriting in `BaseLayout.astro` and `RegionalBrandScript.astro` is not an acceptable canonical solution: metadata must be correct in initial HTML for `hivedue.com` versus `sitehesap.com`. Default Turkish is unprefixed and English is `/en/`; preserve that route model unless the plan explicitly changes it. |
| Astral Post | `/Users/ahmet/Documents/Workspaces/Buhane/apps/AstralPost` / `www/` | Hand-authored home/legal/community pages and `content-hub.css`; content records in `www/content/catalog.mjs`; templates/generator in `www/scripts/build-content-pages.mjs` | **Tracked generated:** `blog/index.html`, `blog/*/index.html`, `glossary/index.html`, `sozluk/index.html`, `sitemap.xml`, `robots.txt`, `feed.xml` | Change article/glossary facts in `catalog.mjs` and structure in the generator, then regenerate. Do not patch generated article files. The generator’s publisher is currently Astral Post itself; Phase 5 should link it to the Buhane organization entity. |
| Gridzle | `/Users/ahmet/Documents/Workspaces/Buhane/games/Gridzle` / `www/` | Hand-authored `www/index.html`, support/privacy/terms, `www/assets/css/site.css`, assets, manifest, robots | Verification reports under `shared/build/reports/www/**` are ignored generated outputs | Edit public files directly. There is currently no sitemap even though `robots.txt` points to one. Canonicals and both verification scripts hard-code legacy `gridzle.com`; the preferred origin is `gridzle.app`, so HTML, robots, sitemap, and validator constants must move together. |
| Hoşkin | `/Users/ahmet/Documents/Workspaces/Buhane/games/Hosgin` / `www/` | `www/content/site.mjs`, `articles.mjs`, locale article modules, `glossary.mjs`; `www/scripts/build.mjs`; styles, script, source assets | **Tracked generated:** root redirects/legal routes, all `www/{tr,en,de,fr,ar}/**`, five feeds, `sitemap.xml`, `robots.txt` | Fully generator-owned. The build deletes and recreates each locale directory; never make durable edits in generated locale HTML. Existing schema graph mechanics are the strongest multilingual analog, but its organization node currently names the product and must be adapted to Buhane ownership. |
| Lastimo | `/Users/ahmet/Documents/Workspaces/Buhane/apps/Lastimo` / `www/` | `www/src/build.mjs`, `render-page.mjs`, `content-library.mjs`, `site-content*.mjs`, `locales.mjs`, `locale-routing.mjs`, store/media records; source media in `www/src/media/**`; icon source in repository `icons/web/**`; hand-maintained `www/assets/site.css` and `site.js` | **Tracked generated:** root and all locale HTML, EN content hub, robots, sitemap, feed, manifest, `assets/locales.js`, `assets/locale-routing.js`, `assets/media/**`, `assets/icons/**` | Fully generator-owned except the named hand-maintained assets. Do not patch output HTML. Repository truth explicitly excludes history, statistics, analytics, past logs, and custom trackers in v1, while current source copy advertises them; content truth correction is a prerequisite to generation, not a later polish pass. |
| Buhane Information Technologies | `/Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr` | `index.html`, `tr/index.html`, `styles.css`, `script.js`, `images/**` | None; direct static deploy | Update both language documents together. Preserve `app-ads.txt` and `yandex_abc334285efd6c2e.html`. There is no framework, package manager, metadata generator, sitemap, robots file, or validator. Product-detail routes added in this phase should remain static and share the existing CSS/JS. A portfolio registry/validator may be tracked here only if deployment explicitly excludes it. |
| U2M | `/Users/ahmet/Documents/Workspaces/Buhane/u2m-api` / `frontend/` | Vue/Vite inputs: `frontend/src/**`, `frontend/index.html`, `frontend/public/**`, `frontend/vite.config.js`, `frontend/src/router/index.js`, frontend tests; shell routes in `src/main/java/com/buhane/u2m/controller/FrontendController.java`; route contracts in `src/test/java/{PublicFrontendRoutingTest,NginxSpaRoutingConfigTest}.java`; `nginx/u2m-{admin-strict,admin,vpn-only}.conf` | **Ignored generated:** `frontend/dist/**` | Never edit `dist`. A metadata-only shell improvement can stay in `frontend/index.html`/`public`. Adding real crawlable routes or prerendering affects Vue router, Vite public-shell fallbacks, Spring controller mappings, all three Nginx configs, and both routing tests as one atomic cluster. Auth/dashboard/recovery routes must be omitted from sitemaps and marked non-indexable where applicable. |
| ahmet.sh | `/Users/ahmet/Documents/Workspaces/Buhane/ahmet.sh` | `index.html`, `style.css`, `script.js`, `i18n.js`, images, manifest | None; direct static deploy | Edit directly. It is a personal/founder property, not a product site. It already introduces Buhane but has no description, canonical, social metadata, schema, robots, or sitemap. The client EN/TR switch shares one URL, so do not emit locale alternates. Update both language dictionaries for visible text. Existing portfolio claims also need the Phase 5 truth gate. |
| The Cosmic Meta | **No verified local live-site source** | External live WordPress/admin access only, currently unavailable | Unknown | Mark `external_blocked` in the registry and document the desired owner/canonical/content changes. Do not edit `/Users/ahmet/Documents/Workspaces/Buhane/cosmicmeta`, `cosmicmeta.ai`, or `cosmic-meta-api`; none is established as the source of `thecosmicmeta.com`. |

### 1.1 Repository instructions and target branches audited

Applicable `AGENTS.md` files were read before source inspection in MoodJot, Vynix, Swipe Slip, Glow Spin, Astral Post, Gridzle, Hoşkin, Lastimo, and Buhane. Hive Due, U2M, and `ahmet.sh` have no applicable repository instruction file; The Cosmic Meta has no verified repository. The app/game repositories are on `develop`; Buhane, U2M, and `ahmet.sh` are on `main`. Important plan constraints inherited from those instructions are:

- MoodJot and Vynix require all product-app translations when app-localized UI is changed, but Phase 5 public-site copy remains scoped to their public website architectures.
- Astral Post, Gridzle, Lastimo, and Buhane require GSD-managed file-changing work. Phase 5 execution plans should use their repository workflows rather than ad-hoc edits.
- Gridzle must remain dependency-free/build-free for its public web surface.
- Buhane must keep both complete language documents synchronized and preserve its static hosting verification files.
- Lastimo’s instructions are the decisive capability source: v1 does not support history, statistics/analytics, past logs, or custom trackers.
- Swipe Slip and Glow Spin target `develop`; public-site commits should remain path-scoped away from application code.

## 2. Strongest Existing Patterns to Reuse

The following are implementation analogs, not claim sources. Preserve each target repository’s own architecture.

### 2.1 Canonical, description, social metadata, and safe JSON-LD serialization

The most reusable generator head is Lastimo’s `www/src/render-page.mjs:61-89`. It centralizes URL construction, escapes visible metadata, and serializes schema rather than hand-concatenating JSON:

```js
const canonicalUrl = absoluteUrl(canonicalPath)
const schemaMarkup = schemas.length
  ? schemas.map((schema) => `<script type="application/ld+json">${jsonForHtml(schema)}</script>`).join('\n')
  : ''

return `<!doctype html>
<html lang="${escapeHtml(locale)}" dir="${escapeHtml(localeDirection(locale))}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${escapeHtml(title)}</title>
  <meta name="description" content="${escapeHtml(description)}">
  <link rel="canonical" href="${escapeHtml(canonicalUrl)}">
  ${renderAlternateLinks(alternates)}
  <meta property="og:title" content="${escapeHtml(title)}">
  <meta property="og:description" content="${escapeHtml(description)}">
  <meta property="og:url" content="${escapeHtml(canonicalUrl)}">
  ${schemaMarkup}
```

For a smaller hybrid generator, Astral Post’s `www/scripts/build-content-pages.mjs:78-110` is the best analog. For direct HTML, MoodJot’s `www/index.html:4-39` is the clearest existing canonical/Open Graph/SoftwareApplication block. The planner should still require unique page title, description, canonical, Open Graph URL/title/description, and one truthful primary entity on every indexable route.

### 2.2 Stable entity graph and Buhane publisher ownership

Hoşkin’s `www/scripts/build.mjs:363-388` shows the useful mechanics: stable fragment IDs, a shared `@graph`, page/product linkage, and page-type-specific nodes. Its ownership value must be changed when reused. The intended portfolio graph is:

```js
const organizationId = 'https://buhane.com.tr/#organization'
const productId = `${canonicalUrl}#softwareapplication` // or #videogame

const graph = [
  {
    '@type': 'Organization',
    '@id': organizationId,
    name: 'Buhane Bilgi Teknolojileri',
    url: 'https://buhane.com.tr/'
  },
  {
    '@type': productSchemaType,
    '@id': productId,
    name: productName,
    url: canonicalUrl,
    publisher: { '@id': organizationId }
  }
]
```

Use `SoftwareApplication` for apps/SaaS and `VideoGame` for games only when the visible page supports those identities. Article/BlogPosting nodes should use `publisher: { "@id": "https://buhane.com.tr/#organization" }`. Do not copy the current self-publisher values in Astral Post, Hoşkin, or Lastimo.

Swipe Slip’s `www/index.html:34-59` is a useful direct-HTML `WebSite` plus `VideoGame` example, but its `Cosmic Meta` author/publisher value is stale and must not be propagated.

### 2.3 Visible owner links without a link-farm footer

U2M already exposes ownership in `frontend/src/components/SiteFooter.vue:13-30`, though the owner text is not linked. It is the closest structural analog:

```vue
<footer class="site-footer">
  <p>&copy; {{ currentYear }} Buhane Bilgi Teknolojileri</p>
</footer>
```

Convert this and comparable product footers to one natural, localized relationship, for example:

```html
<p>A product by <a href="https://buhane.com.tr/">Buhane Information Technologies</a>.</p>
```

Turkish pages should use the Turkish company name/text and may link to `https://buhane.com.tr/tr/`. `ahmet.sh` already has an appropriate founder/company section at `index.html:130-138` and Buhane portfolio card at `index.html:497-530`; it needs factual synchronization rather than a product-owner footer. Remove or narrow the blanket sibling-product footers in Swipe Slip (`www/index.html:282-301`) and Glow Spin (`www/index.html:140-156`). Cross-link siblings only inside a genuinely relevant use case, guide, or comparison.

### 2.4 Content generation patterns

Choose by target architecture:

- **Small hybrid content hub:** Astral Post. `www/content/catalog.mjs` is the editable record source; `www/scripts/build-content-pages.mjs:328-346` writes blog, glossary/dictionary, feed, sitemap, and robots. Its separate `verify-content-hub.mjs` is the cleanest “content source → generated pages → crawl artifacts” plan shape.
- **Hybrid generator with stale-output check:** Vynix. `www/scripts/build-seo-content.mjs:543-578` supports build and `--check`, making it the best analog for deterministic tracked output without a package wrapper.
- **Full multilingual static generation:** Hoşkin. `www/scripts/build.mjs:460-494` owns five locale trees, feeds, sitemap, and robots. Its validator checks every locale, alternate, schema block, link, and sitemap URL.
- **Full generated site with compiled browser locale data:** Lastimo. `www/src/build.mjs:74-128` defines output and asset-copy boundaries; `:151-206` provides build/check CLI behavior. Reuse its boundary discipline, not its unsupported claims.

Astral Post’s explicit write list is the clearest small-site source/output contract:

```js
await writePublicFile("blog/index.html", renderBlogIndex());
await writePublicFile("glossary/index.html", renderGlossary());
await writePublicFile("sozluk/index.html", renderTurkishGlossary());
for (const article of articles) {
  await writePublicFile(`blog/${article.slug}/index.html`, renderArticle(article, articlesBySlug));
}
await writePublicFile("sitemap.xml", sitemap());
await writePublicFile("robots.txt", `User-agent: *\nAllow: /\n\nSitemap: ${urlFor("/sitemap.xml")}\n`);
await writePublicFile("feed.xml", atomFeed());
```

For hand-authored sites, avoid introducing a framework merely to add several high-value pages. A small repository-native generator is justified only when repeated pages, route inventories, or locale alternates would otherwise drift.

### 2.5 Localization and regional-domain patterns

- **Two complete static documents:** Buhane (`index.html` and `tr/index.html`). Every shared product name, preferred URL, owner label, navigation entry, and footer entry must be updated in both.
- **Full stable locale URLs:** Hoşkin’s locale loop and validator are the strongest analog. It emits all locale alternates plus `x-default` and verifies reciprocity.
- **Twelve stable locale URLs:** Lastimo’s `www/src/locales.mjs:136-157`, `locale-routing.mjs:51-60`, and `render-page.mjs:133-138` demonstrate a registry-driven route map and alternate rendering.
- **Astro locale routes:** Hive Due’s source route model (Turkish unprefixed, English under `/en/`) is valid; `BaseLayout.astro:29-35` is structurally useful for link tags. Its current assumption that both hosts share `hivedue.com` canonical metadata and can be repaired after load is an anti-pattern. Produce host-correct initial HTML or separately deployed host-aware builds.
- **Single-URL client switches:** MoodJot, Vynix, and `ahmet.sh` must keep one canonical and must not add EN/TR/etc. `hreflang` entries until distinct crawlable URLs exist.

Lastimo’s route-driven alternate builder (`www/src/render-page.mjs:133-138`) is the concise positive analog:

```js
function localizedAlternates(routeId) {
  if (globalContentRouteIds.has(routeId)) return [];
  return [
    ...SUPPORTED_LOCALES.map((locale) => ({ hrefLang: locale.lang, href: buildLocalePath(locale.key, routeId) })),
    { hrefLang: "x-default", href: buildLocalePath("en", routeId) }
  ];
}
```

Hive Due’s current `BaseLayout.astro:29-35` demonstrates exactly why the regional-domain plan needs a publishing decision: every URL derives from one build-time `Astro.site`, so a browser script cannot retroactively make the initial metadata correct on a second host.

```astro
const siteOrigin = (Astro.site ?? new URL('https://hivedue.com')).origin
const canonical = `${siteOrigin}${locale === 'tr' ? trPath : enPath}`
const trAlt = `${siteOrigin}${trPath}`
const enAlt = `${siteOrigin}${enPath}`
```

### 2.6 Robots, sitemap, feeds, and route inventory

Generate discovery artifacts from the same route records that generate pages whenever possible:

- Hoşkin `www/scripts/build.mjs:460-494` and validator are the strongest multilingual route-inventory pattern.
- Lastimo `www/src/build.mjs:74-91` is the strongest full-site route-output pattern.
- Astral Post `www/scripts/build-content-pages.mjs:328-346` is the simplest hybrid pattern.
- Hive Due should continue using `@astrojs/sitemap` configured by `astro.config.mjs`, with host/domain behavior made explicit.

For hand-authored properties, maintain one small canonical-route inventory and have a dependency-free validator compare it against HTML canonicals and sitemap entries. Sitemap inclusion should be limited to canonical, indexable public pages. Admin, dashboard, authentication, recovery, redirect-only, and noindex routes must be excluded.

Current high-risk gaps to encode into acceptance criteria:

- Gridzle’s robots file advertises a missing sitemap and legacy origin.
- Buhane, U2M, and `ahmet.sh` have no robots/sitemap foundation.
- Vynix generator and some live/public references differ on `www` policy.
- Hive Due’s built metadata is not inherently correct for both regional hosts.

### 2.7 Factual content and safety pattern

MoodJot’s `www/blog/what-is-mood-tracking/index.html:4-12` is a good `Article` metadata example, and the visible wellness disclaimer around line 39 is a useful safety pattern for mental-wellness content. Article/schema presence is not enough: page copy must answer the query, identify the product relationship, avoid medical or outcome promises, and link to the relevant product action.

Hoşkin’s validator is the best mechanical quality floor: minimum article/glossary counts, substantive text, JSON parsing, local-link integrity, canonical uniqueness, sitemap coverage, and no TODO/rating placeholders. Counts should be adapted per product value rather than copied as a portfolio-wide quota, consistent with D-04.

Lastimo is a negative claim-source example. Its generators and validators are mechanically strong, but existing content records mention history, statistics, analytics, past logs, and custom trackers that its repository instructions explicitly exclude from v1. No plan may treat a passing build as proof of product truth.

## 3. Exact Existing Validation and Build Commands

These are the commands already supported by the repositories. This mapping did not execute output-writing builds; pass statements below come from `05-RESEARCH.md`. Plans should run commands after scoped edits and review `git status` immediately afterward.

| Property | Working directory | Exact commands | What they cover / side effects |
|---|---|---|---|
| MoodJot | `.../apps/MoodJot/www` | No repository validation command exists | Add a lightweight Phase 5 HTML/canonical/schema/link check or cover it from the portfolio validator. |
| Vynix | `.../apps/Vynix/www` | `node scripts/build-seo-content.mjs`<br>`node scripts/build-seo-content.mjs --check` | First command rewrites tracked content pages, sitemap, robots. Second checks determinism/staleness. Neither should touch `admin/dist`. |
| Swipe Slip | `.../games/Swipe-Slip/www` | No repository validation command exists | Use the portfolio validator plus local link/schema parse checks. Do not include unrelated repository audio changes in the website commit. |
| Glow Spin | `.../games/Glow-Spin/www` | No repository validation command exists | Use the portfolio validator plus local link/schema parse checks. |
| Hive Due | `.../apps/HiveDue/www` | `npm run check`<br>`npm test`<br>`npm run build` | Astro diagnostics, 12 tests, and production build. Build writes ignored `dist`. Research reports zero Astro diagnostics and passing tests before Phase 5. |
| Astral Post | `.../apps/AstralPost/www` | `node scripts/build-content-pages.mjs`<br>`node scripts/verify-content-hub.mjs` | Regenerates tracked hub/discovery files, then verifies canonicals, schemas, sitemap, robots, feed, article metadata. Research reports current verification passing. |
| Gridzle | `.../games/Gridzle/www` | `python3 ../tools/verify_www_foundation.py --root . --output ../shared/build/reports/www/www-foundation.json`<br>`python3 ../tools/verify_www_hosting.py --root . --output ../shared/build/reports/www/www-hosting-smoke.json` | Writes ignored JSON reports. Both scripts currently hard-code `gridzle.com`; update their expectations in the same plan as the preferred-origin migration. Research reports current legacy contract passing. |
| Hoşkin | `.../games/Hosgin/www` | `node scripts/build.mjs`<br>`node scripts/validate.mjs` | Build deletes/recreates all five locale output trees and discovery files. Validator checks 80 indexable pages, locale alternates, schemas, links, sitemap, and five feeds. Research reports current validation passing. |
| Lastimo | `.../apps/Lastimo/www` | `npm run build`<br>`npm run check`<br>`npm test`<br>`npm run verify` | Build rewrites all tracked output; check detects stale output; tests cover routing/contracts; verify is the full project verification. Research reports 17 tests and existing checks passing, which does **not** resolve the content-truth conflict. |
| Buhane | `.../Buhane/buhane.com.tr` | No validation command exists. Preview only: `python3 -m http.server 8000` | Add a dependency-free portfolio/HTML validator. Preview is not validation and keeps a process running. |
| U2M frontend | `.../Buhane/u2m-api/frontend` | `npm run build`<br>`npm run test:unit`<br>`npm run test:e2e` | Build writes ignored `dist`. Browser tests may require their documented environment/browser setup. |
| U2M routing/backend, if touched | `.../Buhane/u2m-api` | `./gradlew test` | Required when public routes, Spring shell mappings, Nginx route lists, or their contract tests change. Pay particular attention to `PublicFrontendRoutingTest` and `NginxSpaRoutingConfigTest`. |
| ahmet.sh | `.../Buhane/ahmet.sh` | No repository validation command exists | Use the portfolio validator plus local link/schema parse checks. |
| The Cosmic Meta | N/A | No local command; source/admin access blocked | Validation is external HTTP inspection only after access and deployment exist. Do not substitute a legacy local directory. |

Cross-repository manual or new-validator acceptance should include:

1. Parse every JSON-LD script as JSON.
2. Require exactly one final absolute canonical per indexable page and compare it with sitemap URL.
3. Require unique, useful title and description; validate Open Graph URL against canonical.
4. Crawl internal links and asset references from built/deployed output.
5. Validate reciprocal `hreflang` only for stable locale URLs, including self and `x-default` where the route model uses it.
6. Check preferred-origin redirects separately from source metadata; do not assume a canonical tag creates a redirect.
7. Confirm robots does not block indexable content and sitemap excludes admin/auth/dashboard/recovery/redirect-only routes.
8. Validate the visible Buhane owner link and matching Organization `@id` on product pages.
9. Compare product names, category, regional destination, public capability claims, and store/web CTA against the private portfolio registry.
10. Re-run `git status --short` in every touched repository and review only scoped files before commits.

## 4. Dirty-File and Collision Warnings

This is the live mapping snapshot from 2026-08-11. Recheck immediately before every plan begins; do not assume it remains current.

### Confirmed dirty repositories

- **Buhane hub (`main`):** `.planning/REQUIREMENTS.md`, `.planning/ROADMAP.md`, `.planning/STATE.md` are modified and `.planning/phases/` is untracked. These are active GSD artifacts. Phase execution must not reset, blanket-stage, or overwrite them. This `05-PATTERNS.md` is part of that planning work.
- **Vynix (`develop`):** `www/admin/dist/index.html` is modified. It is a tracked generated admin artifact outside the public SEO generator. Never stage it with Phase 5 public-site changes and verify the SEO generator leaves it byte-for-byte untouched.
- **ahmet.sh (`main`):** untracked `.DS_Store`. Leave it untouched and unstaged.
- **Legacy Cosmic directories:** `/cosmicmeta` has a deleted `test.txt` and untracked `.DS_Store`; `/cosmic-meta-api` has untracked `.DS_Store` files. These directories are not verified live-site sources and must not be touched.

Swipe Slip had unrelated audio-source changes during the initial inspection, but its final status check was clean. That status transition indicates concurrent/recent work in the shared repository; recheck its HEAD and worktree immediately before planning or staging even though there is no final dirty-file collision to preserve.

### Clean at mapping time

MoodJot, Swipe Slip, Glow Spin, Hive Due, Astral Post, Gridzle, Hoşkin, and Lastimo were clean in the final check. U2M was clean. Clean status is not permission to mix application code with public-site changes; follow each repository’s branch and commit conventions.

### Collision-prone generated paths

- Do not allow two agents/plans to run a generator in the same repository concurrently.
- Vynix plans that change `build-seo-content.mjs` own all generated blog/glossary/sitemap/robots paths for that run.
- Astral Post plans that change catalog/templates own every output enumerated at `build-content-pages.mjs:328-346`.
- Hoşkin generation deletes all five locale directories before rebuilding; it must be a single repository-exclusive execution window.
- Lastimo generation rewrites all locale/content output and copies icons/media; it must be a single repository-exclusive execution window and start only after the truth audit.
- Hive Due and U2M builds produce ignored `dist`; do not stage it if local ignore configuration changes or tooling exposes it.
- Gridzle verification writes report JSON under `shared/build/reports/www`; do not stage those ignored artifacts.

## 5. Suggested Independent Execution Plan Clusters

The smallest safe parallel unit is generally one repository. The following clusters minimize generated-output overlap and isolate blockers.

### Plan 05-01 — Portfolio truth registry and validation contract

**Files:** a tracked, explicitly non-deployed registry and dependency-free validation tool in the Buhane repository; Phase 5 documentation only.  
**Responsibilities:** eleven property records, preferred origins, aliases, owner identity, type/schema type, locale architecture, regional routing, supported claims, CTA destinations, source root, generation model, validation command, dirty-path exclusions, external-blocked status. Define validator output without modifying public pages.  
**Dependencies:** none.  
**Gate:** Lastimo allowed-capability record must follow repository truth; The Cosmic Meta must be `external_blocked`. Deployment configuration must exclude the private registry if the repository root is served directly.

### Plan 05-02 — Buhane bilingual company hub and product detail network

**Files:** `index.html`, `tr/index.html`, new static EN/TR product detail routes, `styles.css`, possibly `script.js`, `robots.txt`, `sitemap.xml`, and validator route inventory.  
**Responsibilities:** canonical/alternate/schema foundation, coherent company story, all eleven products, regional Hive destinations, factual detail pages, owner entity, navigation/footer consistency.  
**Dependencies:** 05-01 registry.  
**Collision:** protect active `.planning/**`; preserve static verification files.

### Plan 05-03 — Lastimo truth correction and deterministic regeneration

**Files:** `www/src/site-content*.mjs`, content/article/glossary records, schemas/footer in `render-page.mjs`, then all generator-owned output.  
**Responsibilities:** remove or soften history/stats/analytics/past-log/custom-tracker claims; add focused owner link and Buhane publisher node; improve useful content only within supported v1; regenerate and run all four commands.  
**Dependencies:** 05-01 truth record.  
**Gate:** no public generation before claim inventory is reconciled. This cluster is repository-exclusive.

### Plan 05-04 — Hive Due dual-domain regional publication

**Files:** `astro.config.mjs`, `src/layouts/BaseLayout.astro`, `RegionalBrandScript.astro`, footer, page/data/i18n source, `public/robots.txt`, tests.  
**Responsibilities:** correct initial HTML canonicals, sitemap/robots and identity for `hivedue.com` versus `sitehesap.com`; preserve TR/EN route model; add regional owner relation and useful content.  
**Dependencies:** 05-01 regional records.  
**Gate:** the deployment architecture must support host-correct HTML; client-side mutation alone fails acceptance.

### Plan 05-05 — Vynix hybrid content and preferred-origin cleanup

**Files:** hand-authored home/docs/legal/footer; `www/scripts/build-seo-content.mjs`; generated blog/glossary/sitemap/robots.  
**Responsibilities:** settle `www` policy for `vynix.app`, add primary app/owner entity, correct generator publisher/footer, add only useful records, regenerate/check.  
**Dependencies:** 05-01 origin and claims.  
**Collision:** explicitly exclude dirty `www/admin/dist/index.html`.

### Plan 05-06 — Astral Post content hub ownership pass

**Files:** hand-authored public pages/footer, `content/catalog.mjs`, generator and verifier, generated outputs.  
**Responsibilities:** Buhane publisher/owner relationship, canonical/schema consistency, useful factual content records, discovery artifacts, verifier expectations.  
**Dependencies:** 05-01.  
**Collision:** repository-exclusive during regeneration.

### Plan 05-07 — Hoşkin multilingual generator pass

**Files:** `content/*.mjs`, `scripts/build.mjs`, `scripts/validate.mjs`, shared assets, then all five generated locale trees and discovery outputs.  
**Responsibilities:** replace self-organization schema with Buhane publisher relationship, localize visible owner link, add/adjust high-value content without breaking reciprocal alternates.  
**Dependencies:** 05-01.  
**Collision:** generator deletes locale trees; repository-exclusive execution.

### Plan 05-08 — MoodJot direct-static discovery pass

**Files:** public non-admin HTML, styles/script if necessary, robots/sitemap, new focused guides/FAQ/glossary routes and validation inventory.  
**Responsibilities:** consistent canonical/metadata/schema/owner relation, query-useful wellness content and disclaimers, one-URL locale discipline.  
**Dependencies:** 05-01.  
**Exclusions:** admin, referral, and product app flows unless a concrete broken public link requires a scoped fix.

### Plan 05-09 — Swipe Slip direct-static ownership cleanup

**Files:** `www/**/*.html`, `styles.css`, sitemap/robots and route validator.  
**Responsibilities:** replace stale Cosmic Meta and blanket sibling footer links, preserve/repair VideoGame schema, add useful game guides/FAQ/content and consistent discovery metadata.  
**Dependencies:** 05-01.  
**Collision:** stage only website files; application/audio work shares the repository and was active during pattern mapping.

### Plan 05-10 — Glow Spin direct-static ownership and schema pass

**Files:** `www/**/*.html`, styles, sitemap/robots and route validator.  
**Responsibilities:** focused Buhane owner link, home entity schema, metadata consistency, useful gameplay guides/FAQ, removal of blanket sibling-link treatment.  
**Dependencies:** 05-01.

### Plan 05-11 — Gridzle origin migration and missing discovery artifacts

**Files:** all four public HTML pages, `robots.txt`, new sitemap/content routes, `assets/css/site.css`, both `tools/verify_www_*.py` scripts.  
**Responsibilities:** migrate every source and validator expectation from `gridzle.com` to `gridzle.app`, add entity/owner metadata and a real sitemap, expand useful content within the build-free architecture.  
**Dependencies:** 05-01 preferred origin.  
**Gate:** source, robots, sitemap, and validator constants must land together.

### Plan 05-12 — U2M crawlable public marketing surface

**Files:** initially `frontend/index.html`, `frontend/public/**`, public Vue views/footer/router and tests. If adding crawlable routes: Vite fallback list, Spring `FrontendController`, Nginx configs, and routing contract tests.  
**Responsibilities:** descriptive public shell, canonical/owner entity, focused use cases/guides/FAQ, sitemap/robots, explicit noindex/exclusion for private/auth routes.  
**Dependencies:** 05-01.  
**Gate:** decide whether Phase 5 uses static/prerendered public routes or only improves the SPA shell; do not claim CSR-only routes are crawlable without rendered-output verification.

### Plan 05-13 — ahmet.sh founder/portfolio synchronization

**Files:** `index.html`, `i18n.js`, style/script if needed, robots/sitemap.  
**Responsibilities:** personal-site metadata and Person schema, factual founder→Buhane relationship, synchronized portfolio cards and supported claims, one-URL locale discipline.  
**Dependencies:** 05-01.  
**Collision:** leave `.DS_Store` untouched.

### Plan 05-14 — External blocker dossier and portfolio-wide release validation

**Files:** registry status/evidence and validator reports/documentation; no unverified Cosmic source.  
**Responsibilities:** document exact The Cosmic Meta admin/source access needed and proposed edits; run the central source/build checks; inspect final origins and redirects after deployment; record remaining external redirect/DNS/Search Console/analytics actions without performing them absent authorization.  
**Dependencies:** all implemented repository plans.  
**Gate:** release report must distinguish source complete, deployed/verified, and externally blocked rather than treating them as one status.

## 6. Planner-Level Dependency and Acceptance Notes

1. Start with the registry/contract, because origin, product type, regional link, and truthful capability records feed every repository plan.
2. The Buhane hub can proceed immediately after the registry. Repository-specific plans can then run in parallel, one executor per repository.
3. Lastimo must start with content truth; Hive Due must start with a host-aware publishing decision; U2M must start with a rendering/route decision. These are gates inside their plans, not reasons to block unrelated repositories.
4. Generated repositories need their source records, generator/template, output, and validator changes in one plan. Never split “edit source” and “regenerate output” across concurrent plans.
5. Each plan should leave an evidence table: changed canonical origin, indexable route count, sitemap count, parsed schema count/types, owner link target, locale/alternate result, generator/check result, and remaining deployment-only actions.
6. Phase 5 is not complete merely because local HTML validates. Preferred-host redirects, final HTTPS canonical responses, robots/sitemap reachability, and rendered metadata require post-deployment HTTP verification. External account actions remain documented until explicitly authorized.
