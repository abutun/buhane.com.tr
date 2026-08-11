# Phase 5 Research: Portfolio Discovery, Content, and Brand Network

**Phase:** BUHANE-SITE-05 — Portfolio Discovery, Content, and Brand Network  
**Research date:** 2026-08-11  
**Scope:** Buhane's company site, eleven supplied product/site brands, and Ahmet's personal site  
**Mode:** Research only; no product or public-site source files were changed  

## Executive conclusion

The portfolio does not need a blanket increase in page count. It needs a trustworthy portfolio registry, corrected canonical domains, visible ownership, crawlable product-specific information, and a repeatable validation gate. Google explicitly says that its AI features use the same core Search requirements as ordinary Search and require neither special AI markup nor an AI text file. It also warns against scaled pages that add little value. The safest strategy is therefore **one coherent entity network with useful, maintained pages**, not a network of near-duplicate blogs and reciprocal footer links.

Phase 5 should proceed in this order:

1. Establish a private canonical portfolio registry and a product-claim truth gate.
2. Fix domain, canonical, sitemap, and indexing contradictions before adding content.
3. Turn `buhane.com.tr` into the authoritative bilingual portfolio hub, with substantial product pages.
4. Give every product site one clear owner/publisher link back to Buhane and a consistent entity reference.
5. Add or improve product-specific guides, use cases, glossaries, and FAQs only where the content can be factual, firsthand, and maintained.
6. Add contextual sibling links only when they help a user complete a related task; remove the current all-sibling footer pattern from affected game sites.
7. Validate source and live deployments centrally, then measure indexing, citations, referrals, and conversions.

Four issues should block broad publishing until resolved:

- **Lastimo product truth:** the public website markets history, custom trackers, and statistics, while the repository's `AGENTS.md` says v1 excludes history, stats/insights, custom trackers, past logs, and analytics.
- **Gridzle preferred host:** source canonicals and `robots.txt` use `gridzle.com`, but that host redirects to `gridzle.app`, which Buhane already treats as the product URL.
- **Hive Due regional identity:** runtime JavaScript rewrites host-sensitive metadata between `hivedue.com` and `sitehesap.com`; canonical and locale decisions should be correct in the HTML response, not repaired in the browser.
- **The Cosmic Meta source and identity:** no complete local source for the live WordPress site was found, and its live `llms.txt` points to stale `cosmicmeta.ai` URLs rather than `thecosmicmeta.com`.

## Decisions this research should drive

### 1. Search and AI discovery share the same foundation

Google's current guidance says pages shown in AI Overviews and AI Mode must already be indexable and eligible to appear with a snippet. It says there are no additional technical requirements, no special schema, and no AI-specific machine-readable file required. It recommends crawlable internal links, visible text, good page experience, accurate structured data, and current merchant/business information—the same fundamentals as Search. Google's July 2026 AI optimization guide is even more explicit that Google does not use `llms.txt`. ([Google: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features), [Google: AI search optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide))

Consequences for this phase:

- Prioritize indexable HTML, correct canonicals, sitemaps, helpful text, and stable internal links.
- Do not add “AI keywords,” hidden summaries, a special AI schema, or query-fan-out pages.
- Treat AI citations as a distribution outcome, not a feature that markup can guarantee.
- If an optional `llms.txt` is kept, treat it as a manually maintained navigation aid for third-party tools, never as an SEO requirement or replacement for HTML, `robots.txt`, or sitemaps.

### 2. Helpful content is the scaling constraint

Google's people-first guidance asks whether content provides original information, complete answers, firsthand expertise, a clear author or responsible organization, and a satisfying result. It recommends explaining **who** created content, **how** it was created where useful, and **why** it exists. Google separately warns that using generative AI to create many pages without added value can violate its scaled-content-abuse policy. ([Google: creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), [Google: generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content), [Google: spam policies](https://developers.google.com/search/docs/essentials/spam-policies))

Several repositories already contain batches of ten articles and glossary hubs. The next phase should improve evidence, specificity, ownership, accuracy, examples, screenshots, and maintenance—not automatically generate another identical content set for every brand. A smaller set of strong pages is safer than a portfolio-wide page-count target.

### 3. Each language needs a stable URL to be independently discoverable

Google recommends distinct URLs for localized versions, explicit links between languages, and reciprocal `hreflang` annotations. Each localized page must list itself and all alternates with fully qualified URLs; an `x-default` fallback is optional. Google also cautions against relying only on IP or browser-language adaptation. `hreflang` can connect pages on different domains, which is relevant to Hive Due and Site Hesap. ([Google: localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions), [Google: multilingual and multi-regional sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites))

Client-side language switches on one URL, as currently used by MoodJot, Vynix, Astral Post, and ahmet.sh, improve the interface for visitors but do not create separate localized documents for Search. Phase 5 should add localized URLs only for languages that can be translated, reviewed, linked reciprocally, and kept current. It should not claim SEO coverage for every in-app language merely because JavaScript swaps labels.

### 4. Structured data should describe visible truth

Google requires structured data to represent the main visible content and prohibits misleading, hidden, or fabricated information. Valid markup does not guarantee a rich result. Schema.org has a broader vocabulary than Google's supported rich-result features, so a semantically correct `DefinedTermSet` or `VideoGame` may still have no special Google presentation. ([Google: structured data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies), [Google: structured data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data))

Recommended entity pattern:

- Buhane: `Organization` with a stable `@id`, legal/brand name, URL, logo, contact points, and only genuine identity profiles in `sameAs`.
- ahmet.sh: `Person` with a stable `@id`, factual relationship to Buhane, and selected work/case-study links.
- SaaS/app sites: `SoftwareApplication` or the more specific [`WebApplication`](https://schema.org/WebApplication), with truthful category, operating system, offers, publisher, and store URLs.
- Game sites: [`VideoGame`](https://schema.org/VideoGame) and accurate software-app properties where applicable. A `VideoGame` declaration alone should not be assumed to qualify for Google's software-app result; Google's required properties and supported categories still apply. ([Google: software app structured data](https://developers.google.com/search/docs/appearance/structured-data/software-app))
- Editorial pages: [`Article`](https://schema.org/Article) or a more specific subtype, visible author/publisher, dates, headline, image, and breadcrumbs.
- Glossaries: [`DefinedTermSet`](https://schema.org/DefinedTermSet) and `DefinedTerm`, while recognizing that Google does not promise a special glossary rich result.
- Navigation: [`BreadcrumbList`](https://schema.org/BreadcrumbList) matching visible breadcrumbs.

Do not use aggregate ratings, review counts, prices, availability, founding claims, customer totals, or download totals unless they are verifiable and visible. Product URLs are not identity-equivalent pages of Buhane and therefore should not be placed in the organization's `sameAs` list.

FAQ content can still help users, but FAQ rich results are generally restricted to authoritative government and health sites. It should not be a primary SaaS rich-result tactic. ([Google: FAQ and HowTo rich-result changes](https://developers.google.com/search/blog/2023/08/howto-faq-changes))

### 5. Canonicals, robots, and sitemaps perform different jobs

- A canonical consolidates duplicate URL signals; it is a hint, and all signals should agree. ([Google: canonical URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls))
- `robots.txt` manages crawling, not removal from the index. A blocked URL can remain known, and Google must be allowed to crawl a page to see its `noindex`. ([Google: robots.txt introduction](https://developers.google.com/search/docs/crawling-indexing/robots/intro), [Google: robots meta directives](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag))
- A sitemap is a discovery hint, not an indexing guarantee. It should contain absolute preferred canonical URLs only and use `lastmod` only when it reflects a meaningful change. ([Google: build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap))
- Titles and descriptions should be unique, descriptive, concise, and page-specific; Google can still generate a different title or snippet when that better fits the query. ([Google: title links](https://developers.google.com/search/docs/appearance/title-link), [Google: snippets and meta descriptions](https://developers.google.com/search/docs/appearance/snippet))

### 6. Bing and answer-engine controls are complementary

Bing recommends crawlable links, sitemaps, useful content, and Webmaster Tools. IndexNow lets a site notify participating engines that URLs were added, updated, or deleted; it improves discovery speed but does not guarantee crawling, indexing, ranking, or citation. ([Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a), [Bing: sitemaps](https://www.bing.com/webmasters/help/sitemaps-3b5cf6ed), [Bing: IndexNow](https://www.bing.com/webmasters/help/indexnow-0z209wby))

Bing Webmaster Tools' AI Performance report can show when pages are cited across Microsoft's AI experiences, but it should be treated as measurement rather than proof of authority or a ranking signal. ([Bing: AI Performance public preview](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview))

Crawler policy should distinguish search/citation from model training:

- OpenAI documents `OAI-SearchBot` for ChatGPT search discovery/citations and `GPTBot` separately for training. Search inclusion is not guaranteed, and referrals can be measured with `utm_source=chatgpt.com`. ([OpenAI publisher FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq), [OpenAI: ChatGPT search](https://help.openai.com/en/articles/9237897-chatgpt-search))
- Anthropic documents separate `Claude-SearchBot`, `ClaudeBot`, and `Claude-User` agents. ([Anthropic crawler controls](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler))
- Perplexity documents `PerplexityBot` for search/indexing and `Perplexity-User` for user-requested fetches. ([Perplexity crawler documentation](https://docs.perplexity.ai/docs/resources/perplexity-crawlers))
- `Google-Extended` controls some use for Gemini training and grounding but does not affect inclusion or ranking in Google Search. ([Google crawler overview](https://developers.google.com/crawling/docs/about-crawling))

The owner must make an explicit training-policy decision. Phase 5 may recommend allowing citation/search agents while separately allowing or blocking training agents, but it must not infer consent. CDN/WAF bot controls also need checking because a permissive `robots.txt` is ineffective if the network blocks the bot.

## Portfolio audit snapshot

The following is a source-and-live audit performed on 2026-08-11. Git status is evidence for safe planning, not an invitation to clean or overwrite changes.

| Site | Stack and locales | Existing discovery/content | Repository state and safest integration point |
|---|---|---|---|
| **MoodJot** — preferred `moodjot.app`; legacy `moodjot.com` redirects | Handwritten static HTML/CSS/JS. Home has a client-side switch for EN/TR/ES/RU/ZH/DE/FR/PT on one URL; content hub is primarily English. | 18 HTML files; ten articles, blog index, glossary, legal pages. Most public content has titles, descriptions, canonicals, and JSON-LD (`SoftwareApplication`, `Article`, `DefinedTermSet`, `Organization`, `WebSite`). `robots.txt` disallows admin and names a 15-URL sitemap. No feed or `llms.txt`. No independent localized URLs or `hreflang`. | `develop`, clean. Direct HTML integration; add a small validator before broad edits. Preserve admin/referral flows. Health/wellbeing statements need a non-medical claim and sourcing gate. Current footer points to sibling media/games rather than clearly identifying Buhane. |
| **Vynix** — preferred `vynix.app`; legacy `getvynix.com` redirects | Static landing plus generated static content. Client-side home switch for EN/ES/TR/RU/ZH on one URL. | Ten English articles, 17-term glossary, docs, FAQ, legal; generated sitemap and robots. Blog/BlogPosting, DefinedTermSet, Organization, and WebPage markup; home lacks a primary application node. No feed or `llms.txt`; one isolated `hreflang` occurrence does not create a locale system. | `develop`; **dirty:** `M www/admin/dist/index.html` belongs to the user and must be preserved. Edit source and `scripts/build-seo-content.mjs`, then run its check mode; do not hand-edit generated SEO pages or admin dist. Verify model-count/testimonial claims before encoding them as facts. |
| **Swipe Slip** — `swipeslip.app` | Handwritten English static site. | 15 HTML files; ten articles and glossary; 13-URL sitemap, robots, and feed. Strong title/description coverage. JSON-LD includes WebSite, VideoGame, Blog/BlogPosting, BreadcrumbList, and DefinedTermSet. | `develop`, clean. Direct HTML integration and a new shared validator. Footer currently lists Cosmic Meta, MoodJot, Glow Spin, and Vynix on every page; replace the portfolio list with the owner link and keep only contextual sibling recommendations. |
| **Glow Spin** — `glowspin.app` | Handwritten English static site. | 20 HTML files; ten articles, four guides plus index, glossary, and legal. Sitemap and robots cover 20 URLs. BlogPosting and breadcrumb markup exist, but the home page lacks a primary WebSite/application/game entity. No feed or `llms.txt`. | `develop`, clean. Direct HTML integration plus shared validator. Footer currently lists Cosmic Meta, MoodJot, Swipe Slip, and Vynix sitewide; use the owner/contextual pattern instead. |
| **Hive Due / Site Hesap** — `hivedue.com` outside Türkiye; `sitehesap.com` for Türkiye | Astro 6 static output, Tailwind 4, TypeScript, `@astrojs/sitemap`. Stable TR `/` and EN `/en/` content. | Ten articles and 22 glossary terms per language plus guides, resources, pricing, FAQ, docs, and legal. `BaseLayout.astro` emits canonical, `hreflang`, social metadata, and schemas; sitemap index is generated; robots refers to the Hive Due sitemap. | `develop`, clean. `npm run check` and `npm test` passed (49 Astro files, zero diagnostics; 12 tests). Edit `src/data/resources.ts`, `src/i18n/*.json`, layouts, and components—not `dist`. Current browser scripts rewrite brand/canonical metadata and redirect by host. Use host-specific builds or edge/server routing so `sitehesap.com` Turkish pages and `hivedue.com` English pages return correct self-canonicals and reciprocal cross-domain `hreflang` in initial HTML. |
| **Astral Post** — preferred `astralpost.app`; legacy `astralpost.com` redirects | Static home with inline CSS/JS and a client-side EN/TR/DE/JA/ZH/ES/FR/PT/RU switch; generated English content hub plus Turkish glossary. | Ten English articles, 15 English glossary terms, Turkish `/sozluk`, 17-URL sitemap, robots, and feed. WebSite, SoftwareApplication, BlogPosting, breadcrumb, DefinedTermSet, and Organization markup. Most localized UI states are not separate indexable URLs; glossary language pair has limited `hreflang`. | `develop`, clean; project requires GSD workflow. Edit `content/catalog.mjs` and `scripts/build-content-pages.mjs`, then run `scripts/verify-content-hub.mjs` (currently passes). Footer names Ahmet but does not clearly link the company publisher. |
| **Gridzle** — live preferred appears to be `gridzle.app`; legacy `gridzle.com` redirects | Handwritten English static site. | Four pages: home, support, privacy, terms. Titles/descriptions/canonicals exist. No structured data, blog, glossary, or sitemap file. `robots.txt` advertises a missing `https://gridzle.com/sitemap.xml`; source canonicals also use the legacy host. | `develop`, clean; project requires GSD workflow. Resolve preferred-host registry first, then update direct HTML/robots and existing Python foundation/hosting validators. Both validators passed their current, incomplete contract. |
| **Hoşkin** — preferred `hoskin.app`; legacy `gethoskin.com` redirects | Dependency-free deterministic static generator. TR/EN/DE/FR/AR with proper RTL handling for Arabic; root is a `noindex,follow` language redirect to `/tr/`. | 80 validated indexable pages; ten articles per locale, 40 glossary terms, five feeds, 80 sitemap URLs, reciprocal `hreflang`. WebSite, SoftwareApplication, Blog/BlogPosting, breadcrumb, DefinedTermSet, and Organization schemas. | `develop`, clean. Edit `content/site.mjs`, localized article/glossary sources, and generator templates; run build and validator. Validator currently passes exactly 80 pages, 10 articles × 5 locales, 40 glossary terms, five feeds, and 80 sitemap URLs. Repository rules describe a Turkish-first app, so localized site feature claims still require product verification. |
| **Lastimo** — preferred `lastimo.app`; legacy `getlastimo.com` redirects | Dependency-free generated static site. Twelve localized home/legal sets: EN/TR/ES/PT-BR/PT-PT/FR/DE/IT/JA/KO/ZH-Hans/RU. English-only content hub. | 49 HTML files; ten articles, 18 glossary terms, feed, 48-URL sitemap. Full title/description/canonical/JSON-LD coverage; `hreflang` on locale home/legal pages. WebSite, SoftwareApplication, Blog/BlogPosting, breadcrumb, DefinedTermSet, and FAQPage schemas. | `develop`, clean. `npm run check`, tests (17 passing), and verifier pass. Edit `src/*.mjs`, rebuild, and verify. **Publication blocker:** repository scope excludes history/stats/custom trackers/analytics, while public content advertises them. Reconcile with shipped product before further marketing or schema work. |
| **Buhane Information Technologies** — `buhane.com.tr` | Two complete static documents: English `/` and Turkish `/tr/`, shared CSS and JavaScript; no build system. | Product cards and contact routes exist, but there are no canonicals, `hreflang`, JSON-LD, robots, sitemap, product detail pages, blog, glossary, or FAQ. Static verification files must remain. | `main`; dirty only in planning artifacts during this research. Update both localized documents for shared changes. Safest role is the authoritative bilingual organization/portfolio hub. Do not change the “ten products” statistic until Hoşkin's lifecycle status is confirmed; the user supplied eleven product brands in total. |
| **U2M URL Shortener** — `u2m.io` | Vue 3.5 SPA, Vue Router 5, Vite 8. Public marketing/API/stats/privacy routes plus auth and protected dashboard routes. | One HTML shell with a title only; no route-specific description/canonical/social/schema handling, robots, or sitemap. JavaScript routes are not prerendered. | `main`, clean. Keep the application SPA, but add crawlable/prerendered public marketing, guide, API-doc, privacy, and use-case output or a static content shell. Omit protected/auth routes from sitemaps; return `noindex` on public auth/recovery shells where appropriate. Add the existing visible Buhane attribution as a link. Run build, unit, and E2E suites. |
| **ahmet.sh** — `ahmet.sh` | Single-page static EN/TR site with client-side language switching. | Rich portfolio UI but only a title: no description, canonical, social metadata, schema, robots, or sitemap. The Turkish state is not independently addressable. | `main`; **dirty:** untracked `.DS_Store`, which must be preserved or ignored by its owner rather than silently deleted. Direct HTML/i18n integration. Add factual `Person` markup, a clear founder relationship to Buhane, and selected case studies; do not duplicate the entire company portfolio network in every footer. |
| **The Cosmic Meta** — `thecosmicmeta.com` | Live WordPress news/content site. A complete deployable source repository for the live site was not found locally. | Live WordPress/Yoast robots and sitemap index exist; homepage title is generic “Home.” The site has extensive post/tag taxonomies and theme schema. Live `llms.txt` exists but identifies/links `cosmicmeta.ai`, not the current domain. Large tag-sitemap inventory warrants a thin/archive crawl audit. | Closest local directories are not the live website: `cosmicmeta` is an older NFT-era GitBook repository (`main`, dirty `D test.txt`, untracked `.DS_Store`); `cosmicmeta.ai` contains WordPress config/cache exports and tools; `cosmic-meta-api` is a content API. Do not edit these as a proxy. Obtain WordPress admin/hosting or the actual source, then correct domain/entity data and `llms.txt` or remove the stale file. |

### Repository-rule implications

- MoodJot, Vynix, Swipe Slip, Glow Spin, Hive Due, Astral Post, Gridzle, Hoşkin, and Lastimo were observed on `develop`; do not implement this phase directly on `main` in repositories whose `AGENTS.md` explicitly requires `develop`.
- Buhane, Astral Post, Gridzle, and Lastimo explicitly require a GSD-managed workflow for source changes.
- Existing user changes (`Vynix/www/admin/dist/index.html`, `ahmet.sh/.DS_Store`, the unrelated `cosmicmeta` deletions/untracked file, and Buhane planning work) must not be cleaned, reverted, regenerated over, or committed accidentally.
- Static generated sites must be edited through their content source/generator and validated; generated HTML should not become the parallel source of truth.

## Canonical portfolio registry

Phase 5 should introduce one private, non-deployed registry used by planning and validation. It should not attempt to make all repositories depend on Buhane at runtime. Suggested fields:

```text
id
display_name
legal_owner
lifecycle_status        # live, beta, coming-soon, retired
category
source_root
preferred_origin
legacy_origins
default_locale
indexable_locales
canonical_routes
sitemap_url
robots_url
store_urls
support_url
contact_url
logo_source
publisher_entity_id
approved_contextual_links
verified_features
claim_reviewed_at
```

This registry resolves the present contradictions:

- User-supplied legacy domains can remain acquisition/redirect domains, while every canonical, sitemap, schema URL, Open Graph URL, and cross-link uses the final preferred origin.
- The company product count derives from `lifecycle_status`, rather than from an unverified hard-coded number.
- Content generators consume verified features rather than inventing or perpetuating marketing claims.
- Cross-links can be compared to an allowlist of genuine relationships rather than allowed to spread automatically.
- The same exact publisher identity can be used consistently across domains without treating products as `sameAs` identities.

Preferred-origin decisions indicated by the live redirect audit are:

| Legacy/user-entered URL | Preferred final URL observed |
|---|---|
| `moodjot.com` | `https://moodjot.app/` |
| `getvynix.com` | `https://vynix.app/` (choose and enforce one `www` policy) |
| `astralpost.com` | `https://astralpost.app/` |
| `gridzle.com` | `https://gridzle.app/` |
| `gethoskin.com` | `https://hoskin.app/` |
| `getlastimo.com` | `https://lastimo.app/` |
| `hivedue.com` from Türkiye | `https://sitehesap.com/`; regional architecture needs an explicit per-locale canonical contract |

Every legacy redirect should be permanent where the move is permanent, preserve the relevant path when possible, and reach the preferred HTTPS URL in one hop. Do not cross-link through a legacy domain.

## Recommended information architecture

### Buhane as the authoritative hub

Add substantial, bilingual product detail pages rather than relying only on compact home-page cards. A practical shape is:

```text
/
/products/
/products/{product-slug}/
/work/{selected-case-study}/
/about/
/contact/
/insights/                    # only when a sustainable editorial program exists

/tr/
/tr/urunler/
/tr/urunler/{product-slug}/
/tr/calismalar/{selected-case-study}/
/tr/hakkimizda/
/tr/iletisim/
/tr/yazilar/                  # only when maintained
```

Each product page should answer, in visible HTML:

- what the product is and is not;
- the audience and problem it serves;
- verified capabilities, supported platforms, locales, and regions;
- a short “how it works” path;
- privacy/security or data-handling facts appropriate to the product;
- support, official site, and store destinations;
- lifecycle status and a truthful update/review date;
- why Buhane built it or what was learned, when a factual founder/company perspective exists;
- a concise FAQ drawn from real support or onboarding questions.

This gives search and answer systems a credible organization-to-product relationship, while the product site remains the best source for detailed usage information.

### Product-site content model

Use a needs-based model rather than requiring “blog + guide + glossary + FAQ” on every site:

| Intent | Best page type | Quality requirement |
|---|---|---|
| Understand the product | Home/about/product page | Clear category, audience, differentiator, platform, verified feature list, owner, primary CTA. |
| Start successfully | Getting-started guide | Exact steps against the current release; screenshots/labels must match the app. |
| Solve a specific job | Use case | Real workflow, constraints, example input/output, when not to use it. |
| Understand domain language | Glossary | Original definition, product-context example, related concepts, reviewer/source; no one-sentence doorway pages. |
| Evaluate trust | Privacy/security/data page | Precise collection, processing, retention, deletion, third-party, and contact facts; legal review where needed. |
| Resolve objections | FAQ | Visible, concise answers derived from real questions; schema is optional and not the reason to create it. |
| Learn from the maker | Case study/engineering note | Firsthand decisions, tradeoffs, evidence, byline, and date. |

Content should be assigned to the site with the strongest firsthand authority. For example, a URL-shortening API implementation guide belongs on U2M; a portfolio-level “how Buhane ships multilingual static product sites” case study belongs on Buhane or ahmet.sh. Republishing the same article across multiple owned domains should be avoided; if legitimate syndication is necessary, use a clear original source and canonical strategy.

### Editorial truth and maintenance gates

Before an article, guide, FAQ, or schema node is publishable, require:

1. Feature claims map to a released build, public API, or owner-approved roadmap label.
2. Numbers, testimonials, reviews, pricing, and availability have an evidence URL or internal source and review date.
3. Health, wellbeing, finance, privacy, and security claims receive appropriate domain review and avoid unsupported outcomes.
4. The visible author or responsible organization is named; AI assistance is described when disclosure helps readers understand how the content was produced.
5. The page adds original examples, screenshots, data, or firsthand explanation—not only a generic definition available everywhere.
6. Dates reflect real publication and meaningful revision, not a generated timestamp.
7. A named owner is responsible for reviewing the page on product changes.

The existing Lastimo contradiction demonstrates why this gate belongs before generation. The safest initial action is to compare every public Lastimo claim to the shipping app and either remove unsupported copy or update the repository's authoritative scope only after the product owner confirms the feature exists.

## Brand/entity network and cross-link graph

### Recommended graph

```text
ahmet.sh (Person)
    │ founder / selected case studies
    ▼
buhane.com.tr (Organization + canonical portfolio hub)
    │ publisher/owner links to official preferred origins
    ├── MoodJot
    ├── Vynix
    ├── Swipe Slip
    ├── Glow Spin
    ├── Hive Due / Site Hesap
    ├── Astral Post
    ├── Gridzle
    ├── Hoşkin
    ├── Lastimo
    ├── The Cosmic Meta
    └── U2M

Each product site ── one visible “Built/published by Buhane” owner link ──► Buhane
Selected product pages ── only task-relevant editorial links ──► related products
```

Every product may link once from a global About/footer area to the company using a natural brand phrase such as “A product by Buhane Information Technologies.” That link explains provenance. It should not be followed by a global list of all sibling sites.

Potential contextual relationships, subject to editorial justification:

- **Reflection/personal-growth workflow:** MoodJot, Astral Post, and Lastimo may reference one another only on a comparison, workflow, or “when this is the better tool” page that explains the distinct job of each product.
- **Games:** Glow Spin, Swipe Slip, Gridzle, and Hoşkin may have a dedicated “More games by Buhane” page or a small relevant module. It should not appear as a twelve-link footer on every article.
- **Creative/media:** Vynix and The Cosmic Meta may cross-link around a concrete creation/publishing workflow, not merely because both involve media or AI.
- **Business tools:** U2M and Hive Due should cross-link only if there is a real integration or use case, such as sharing a verified invoice/payment link—not as a generic SaaS exchange.
- **Maker perspective:** ahmet.sh should link selected deep case studies, while Buhane owns the complete portfolio directory.

Google's spam policy identifies excessive reciprocal exchanges, partner pages made only for cross-linking, and widely distributed footer/template links as link-spam patterns. Owned-site links are not automatically problematic, but relevance and user value must determine placement. Paid or sponsored placements require appropriate `rel="sponsored"` or `nofollow`; ordinary factual editorial ownership links do not need `nofollow` merely because the same company controls both sites. ([Google: link spam policies](https://developers.google.com/search/docs/essentials/spam-policies#link-spam))

### Entity consistency rules

- Use one canonical organization name and URL in visible copy and JSON-LD.
- Give Buhane a stable `@id`, for example `https://buhane.com.tr/#organization`, and reference that exact ID as `publisher` from product/article schemas where legally true.
- Give Ahmet a stable `Person` ID at ahmet.sh and express the founder relationship once, consistently, and factually.
- Use `sameAs` only for pages representing the same person/organization identity, not product websites.
- Use preferred final HTTPS URLs for every logo, screenshot, canonical, Open Graph URL, publisher URL, sitemap entry, and internal link.
- Keep product name spelling and diacritics consistent: “Hoşkin” is display copy, while its URL slug can remain ASCII.
- Do not claim store/platform availability until the destination is live and the app status is confirmed.

## Site-specific Phase 5 recommendations

### MoodJot

- Keep and editorially improve the strongest existing articles rather than adding another bulk set.
- Add a visible publisher/owner relationship to Buhane and align `Organization` IDs.
- Decide whether Turkish or other localized content warrants distinct URL trees; do not add `hreflang` to one client-switched URL.
- Review wellbeing claims, references, and language for medical overreach.
- Add generator-independent validation for all public static pages and ensure the sitemap is complete.

### Vynix

- Add a truthful primary `SoftwareApplication`/`WebApplication` entity on the home page.
- Treat the build script as the only source of generated content and extend `--check` to metadata/domain/entity assertions.
- Verify quantitative/model/testimonial claims before publication or structured data.
- Pick one canonical host (`vynix.app` or `www.vynix.app`) and make redirect, canonical, sitemap, social metadata, and cross-links agree.
- Preserve the existing dirty admin build artifact.

### Swipe Slip and Glow Spin

- Replace current portfolio-wide sibling footers with a Buhane publisher link.
- Retain only contextual “more games” links on a dedicated or small relevant module.
- Add shared static validation; ensure every content page remains in sitemap/feed as appropriate.
- Give Glow Spin a primary home-page game/application and WebSite entity. Validate Swipe Slip's app/game markup against Google's supported software-app fields without fabricating rating data.

### Hive Due / Site Hesap

- Make the regional canonical contract explicit: for example, Turkish pages self-canonical on `sitehesap.com`, English pages self-canonical on `hivedue.com`, with reciprocal cross-domain `hreflang` and an appropriate fallback. The owner must confirm this mapping.
- Generate correct metadata at build/edge response time. Remove reliance on post-load JavaScript to repair canonical, Open Graph, schema, or locale URLs.
- Preserve visible language switches and offer deterministic links; do not rely only on IP redirect behavior.
- Continue using Astro data/i18n sources and its existing test/check/build gate.

### Astral Post

- Use `content/catalog.mjs` and the generator; do not hand-edit output.
- Add a clear Buhane publisher link and consistent entity ID.
- Decide which of the nine UI languages can support maintainable URL-addressable content; preserve the rest as UI convenience without SEO claims.
- Improve the English/Turkish glossary alternates only when translations are semantically equivalent and reciprocal.

### Gridzle

- Resolve `gridzle.app` as the preferred host in the registry and correct source canonicals/robots before creating a sitemap.
- Add a small, high-quality foundation: WebSite + game/application schema, sitemap, owner link, FAQ/support improvements, one getting-started/how-to-play guide, and a few real use cases or strategy guides.
- Extend the current Python validators instead of introducing a framework.

### Hoşkin

- Preserve the generator and strong five-locale/hreflang architecture.
- Review generated localized claims against the authoritative game rules and actual release/store status.
- Add Buhane provenance without disturbing localized page parity or Arabic RTL behavior.
- Prefer revising the best existing pages to increasing the already substantial 80-page footprint.

### Lastimo

- Stop new content generation until the repository-scope/public-marketing contradiction is resolved.
- Once approved truth is known, update source modules, rebuild all generated locales, and run the full check/test/verify gate.
- Keep English-only editorial content explicit; do not imply that article/glossary content is localized because home/legal pages are.
- FAQ schema may remain if it matches visible text, but it should not be considered a likely rich-result channel.

### Buhane

- Add bilingual organization, portfolio, about, and detailed product pages with reciprocal EN/TR links.
- Add canonical, `hreflang`, social metadata, `Organization`, `WebSite`, breadcrumbs, robots, and sitemap.
- Establish stable organization/person/product entity IDs and the internal portfolio registry.
- Replace the hard-coded product statistic only after lifecycle status is confirmed for Hoşkin and every other brand.
- Preserve `app-ads.txt` and search-verification files.

### U2M

- Preserve the Vue application but ensure public landing, API docs, privacy, and future guides are present as crawlable prerendered/static output with route-specific metadata.
- Keep login, registration, recovery, dashboard, and profile out of the sitemap; use `noindex` for publicly fetchable auth shells and authentication for private data.
- Add robots, sitemap, Organization/WebApplication/WebSite schema where visible, and a linked Buhane attribution.
- Keep API documentation factual and versioned; it is likely U2M's strongest original discovery content.

### ahmet.sh

- Add canonical, description, social cards, `Person` schema, and a factual founder relationship to Buhane.
- Convert only the Turkish material that can be maintained into a distinct `/tr/` URL if bilingual search discovery is a goal.
- Keep selected personal case studies here and direct visitors to Buhane for the full commercial portfolio.

### The Cosmic Meta

- Obtain the actual WordPress administration/deployment path before implementation.
- Correct the generic home title and align Organization/WebSite/publisher identity with the live domain.
- Audit tag/category archives for unique value and index only useful taxonomy pages; large thin tag inventories can dilute crawling and user experience.
- Correct or remove the stale `llms.txt`. The [`llms.txt` proposal](https://llmstxt.org/) is a voluntary proposal, while Google says it does not use the file; an inaccurate file is worse than no file.
- Keep current WordPress/Yoast sitemap and robots behavior only after verifying all sitemap URLs are canonical, valuable, and on `thecosmicmeta.com`.

## Measurement architecture

Phase 5 success should not be defined as “we added metadata” or “we rank first.” Measure:

- preferred pages discovered and indexed, with no duplicate-host or alternate-page surprises;
- sitemap submitted/read status and crawl/indexing errors in Google Search Console and Bing Webmaster Tools;
- valid structured data and enhancement reports where Google supports the feature;
- impressions, clicks, queries, and country/language performance for product and company pages;
- Microsoft AI citations/pages in Bing AI Performance where available;
- ChatGPT referrals (`utm_source=chatgpt.com`) and other identifiable AI referrals in first-party analytics;
- cross-domain visits carrying source site, source page, destination product, and CTA identifiers;
- clicks to official site/store/support, contact submissions, registrations, and other real conversion events;
- content maintenance failures: stale claims, broken external destinations, expired pricing, and mismatched locales.

Google began rolling out dedicated generative-AI performance reporting to a subset of Search Console users in June 2026; use it when present, but do not make the phase dependent on access. ([Google Search Central: generative AI performance reports](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports))

For privacy and maintainability, use consistent first-party event names rather than unrelated analytics configurations per site. A minimal event contract could include `portfolio_product_click`, `store_click`, `support_click`, `contact_start`, `contact_submit`, and `signup_start`, with `product_id`, `source_site`, `source_page_type`, `destination_type`, and locale. Do not send journal text, personal documents, shortened target URLs, invoices, or other user content as analytics properties.

## Validation Architecture

### Central validation contract to add in Phase 5

Introduce a dependency-free Python validator in the Buhane repository and a private, non-deployed manifest, for example:

```bash
cd /Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr
python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode source
python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode live --timeout 20
```

`--mode source` should fail when any of these criteria are violated:

1. Every intended indexable page has exactly one nonempty `<title>`, one primary `<h1>`, a page-specific meta description, an absolute HTTPS canonical, and no `noindex`.
2. Canonical URLs use the registry's preferred origin and normalized path; legacy origins appear only in the redirect registry or explanatory content.
3. Titles, descriptions, and canonical URLs are unique within a site except approved language/redirect shells.
4. Every JSON-LD block parses; required semantic types exist for each page class; URL/entity IDs use the preferred origin; claims match an approved visible-text field; ratings/reviews/prices are rejected unless evidence is recorded.
5. `robots.txt` parses, contains the correct preferred sitemap URL, does not accidentally block public assets/content, and is not treated as the mechanism for `noindex`.
6. Sitemap XML parses, contains only absolute preferred canonical indexable URLs, includes every intended public page exactly once, excludes auth/admin/redirect/noindex pages, stays within protocol limits, and does not contain future or mechanically false `lastmod` dates.
7. Every localized URL has a self-reference plus complete reciprocal `hreflang` alternatives; expected locale codes are valid and fully qualified; an `x-default` maps to a real fallback when the site uses one.
8. Internal links and local image/script/style references resolve; cross-domain links use HTTPS and the preferred host.
9. Each product has an approved visible owner/publisher link to Buhane. Sitewide sibling-portfolio lists and cross-links absent from the per-page allowlist fail validation.
10. Static-verification files, `app-ads.txt`, legal routes, and required support routes remain present.
11. Generated output matches its source generator where the repository has one.

`--mode live` should fail when:

1. A preferred origin does not redirect HTTP to HTTPS and return a final `200` response.
2. A permanent legacy origin needs more than one redirect hop, ends on the wrong host/path, or uses a temporary redirect for a permanent migration without an explicit exception.
3. A sitemap/robots/feed URL is not `200`, has the wrong content type, or refers to a different origin without an approved cross-domain contract.
4. Any sitemap URL redirects, errors, is `noindex`, or declares a different canonical.
5. A production page unintentionally carries staging/noindex metadata.
6. Search/citation agents chosen in the crawler policy are blocked by robots, CDN, WAF, or origin access.
7. Required social images, stores, support, privacy, contact, or ownership links are broken.

The validator should emit both human-readable output and a machine-readable JSON report so every repository can use it in CI without adopting a shared framework.

### Existing repository commands

Run each repository's own contract in addition to central validation. These commands are based on the audited repositories:

```bash
# Vynix generated SEO content
cd /Users/ahmet/Documents/Workspaces/Buhane/apps/Vynix/www
node scripts/build-seo-content.mjs --check

# Hive Due / Site Hesap
cd /Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/www
npm run check
npm test
npm run build

# Astral Post
cd /Users/ahmet/Documents/Workspaces/Buhane/apps/AstralPost/www
node scripts/verify-content-hub.mjs

# Gridzle
cd /Users/ahmet/Documents/Workspaces/Buhane/games/Gridzle/www
gridzle_foundation_report="$(mktemp)"
python3 ../tools/verify_www_foundation.py --root . --output "$gridzle_foundation_report"
gridzle_hosting_report="$(mktemp)"
python3 ../tools/verify_www_hosting.py --root . --output "$gridzle_hosting_report"

# Hoşkin
cd /Users/ahmet/Documents/Workspaces/Buhane/games/Hosgin/www
node scripts/build.mjs
node scripts/validate.mjs

# Lastimo
cd /Users/ahmet/Documents/Workspaces/Buhane/apps/Lastimo/www
npm run check
npm test
npm run verify

# U2M
cd /Users/ahmet/Documents/Workspaces/Buhane/u2m-api/frontend
npm run build
npm run test:unit
npm run test:e2e
```

MoodJot, Swipe Slip, Glow Spin, Buhane, and ahmet.sh currently have no site-specific SEO validator. Until the central validator exists, changes to those sites should receive at minimum HTML/XML parsing, local-link checks, and an HTTP-root preview. Turkish Buhane paths are root-relative, so preview from the project root:

```bash
cd /Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr
python3 -m http.server 4173
```

The acceptance criteria are not merely “command exits zero.” The preview must show correct layout and navigation at `/`, `/tr/`, product pages, content pages, language alternates, keyboard/mobile navigation, and error-free browser console/network behavior.

### Representative live checks

The future live validator should automate these, but individual incidents can be diagnosed with:

```bash
curl --fail --silent --show-error --location --max-redirs 3 --output /dev/null \
  --write-out '%{url_effective} %{http_code} %{num_redirects}\n' \
  https://gridzle.com/

curl --fail --silent --show-error https://gridzle.app/robots.txt
curl --fail --silent --show-error https://gridzle.app/sitemap.xml

curl --fail --silent --show-error --user-agent 'OAI-SearchBot' https://moodjot.app/ \
  --output /dev/null
```

For redirect migrations, the criterion is the correct final preferred URL, status `200`, and no more than one origin migration hop. For crawler tests, a `200` response alone is insufficient: inspect response body, headers, robots rules, and any CDN challenge behavior.

### Search-platform verification

After deployment, complete these non-code checks for every preferred origin:

1. Verify domain ownership in Google Search Console and Bing Webmaster Tools.
2. Submit the canonical sitemap and inspect live URL/canonical selection for a representative home, product/guide, article, glossary, and localized pair.
3. Validate supported markup with Google's Rich Results Test and inspect rendered HTML, while remembering that Schema.org-only types may not appear as Google enhancements.
4. Configure IndexNow per host or deploy pipeline and submit only added, meaningfully updated, or deleted URLs; keep sitemaps as the durable inventory.
5. Record baseline and 28-/90-day metrics before attributing a change to Phase 5.
6. Test cross-domain analytics without collecting product user content.

## Suggested Phase 5 requirement set

The phase planner can convert these into final requirement IDs:

- **REGISTRY:** A validated private registry defines every product's legal owner, lifecycle, preferred/legacy origins, locales, destinations, and approved claims.
- **DOMAIN:** All canonical, sitemap, social, structured-data, and cross-link URLs agree with the preferred-origin registry; permanent legacy hosts redirect in one hop.
- **HUB:** Buhane provides crawlable, bilingual, substantial company and product pages with reciprocal localized relationships.
- **ENTITY:** Buhane, Ahmet, and each product use stable, truthful, consistent entity IDs and visible publisher/founder relationships.
- **TECH:** Every public origin has appropriate canonical metadata, robots, sitemap, titles/descriptions, and schema; private/auth/redirect pages are excluded correctly.
- **LOCALE:** Only maintainable URL-addressable localized pages receive `hreflang`; all pairs are self-referential and reciprocal.
- **CONTENT:** Product content is useful, firsthand, attributable, current, and validated against released capabilities; bulk thin generation is prohibited.
- **LINKS:** Each product links visibly to Buhane; sibling links are contextual and allowlisted; portfolio-wide reciprocal footer lists are removed.
- **AI-POLICY:** Search/citation and training crawler choices are documented separately; `llms.txt` is optional, non-authoritative, and must be accurate if present.
- **MEASURE:** Search Console, Bing Webmaster Tools, analytics events, citations/referrals, and product conversions provide baseline and post-launch evidence.
- **VALIDATE:** Central source/live validation and every repository's native generator/test suite pass before deployment.
- **EXTERNAL:** The Cosmic Meta changes remain blocked until the live WordPress administration/source path is obtained.

## Recommended implementation waves

1. **Truth and registry:** confirm legal display name, Hoşkin lifecycle/store state, Lastimo feature scope, regional Hive Due/Site Hesap mapping, and every preferred canonical host.
2. **Buhane hub:** bilingual product/company pages, metadata/schema, robots/sitemap, owner entity, and validation tooling.
3. **Strong generated sites:** Vynix, Astral Post, Hoşkin, and Lastimo through their generators, after claim review.
4. **Handwritten static sites:** MoodJot, Swipe Slip, Glow Spin, and Gridzle, using the new central validator and contextual-link policy.
5. **Architecturally distinct sites:** Hive Due host-aware output, U2M crawlable public route output, and ahmet.sh Person/case-study architecture.
6. **External WordPress:** The Cosmic Meta only after access/source is identified.
7. **Submission and measurement:** sitemaps, IndexNow, Search Console/Bing inspection, analytics, and 28-/90-day review.

This sequence still covers the full portfolio, but it prevents domain mistakes and unsupported claims from being multiplied across every site.

## Source index

Primary references used in this research:

- [Google Search Central: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- [Google Search Central: AI search optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [Google Search Central: helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google Search Central: generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)
- [Google Search Essentials: spam policies](https://developers.google.com/search/docs/essentials/spam-policies)
- [Google Search Central: localized versions and `hreflang`](https://developers.google.com/search/docs/specialty/international/localized-versions)
- [Google Search Central: multilingual and multi-regional sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites)
- [Google Search Central: structured data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- [Google Search Central: software-app structured data](https://developers.google.com/search/docs/appearance/structured-data/software-app)
- [Google Search Central: sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google Search Central: robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
- [Google Search Central: robots meta directives](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)
- [Google Search Central: canonical URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google Search Central: title links](https://developers.google.com/search/docs/appearance/title-link)
- [Google Search Central: snippets](https://developers.google.com/search/docs/appearance/snippet)
- [Google crawler overview and Google-Extended](https://developers.google.com/crawling/docs/about-crawling)
- [Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)
- [Bing Webmaster Tools: sitemaps](https://www.bing.com/webmasters/help/sitemaps-3b5cf6ed)
- [Bing Webmaster Tools: IndexNow](https://www.bing.com/webmasters/help/indexnow-0z209wby)
- [Bing Webmaster Blog: AI Performance](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)
- [OpenAI: publishers and developers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq)
- [OpenAI: ChatGPT search](https://help.openai.com/en/articles/9237897-chatgpt-search)
- [Anthropic crawler controls](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
- [Perplexity crawler documentation](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)
- [Schema.org: Organization](https://schema.org/Organization), [Person](https://schema.org/Person), [SoftwareApplication](https://schema.org/SoftwareApplication), [WebApplication](https://schema.org/WebApplication), [VideoGame](https://schema.org/VideoGame), [Article](https://schema.org/Article), [DefinedTermSet](https://schema.org/DefinedTermSet), and [BreadcrumbList](https://schema.org/BreadcrumbList)
- [`llms.txt` proposed convention](https://llmstxt.org/) — included only to characterize its proposal status, not as a search requirement

