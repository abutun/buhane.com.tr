# Portfolio SEO and AI Discovery Research

**Date:** 2026-08-14
**Scope:** Buhane, ahmet.sh, MoodJot, Vynix, Swipe Slip, Glow Spin, Hive Due / Site Hesap, Astral Post, Gridzle, Hoşkin, Lastimo, U2M, and The Cosmic Meta.
**Method:** Read-only review of the portfolio registry, Phase 05 release evidence, current editable source, native strict source validation, representative live discovery endpoints, repository status, and current primary Google/OpenAI documentation. No public source, deployment, crawler policy, account, or DNS/CDN state was changed during research.

## Decision summary

The editable portfolio is already unusually complete at the source level: the fresh strict source validator passed with **zero findings** and executed the declared native content/generator contracts. The current source already provides canonical URLs, canonical-only sitemaps, descriptive metadata, truthful schema, visible Buhane ownership, contextual (not sitewide reciprocal) links, and substantial product-specific content.

Do **not** add a portfolio-wide `llms.txt` layer, hidden AI keywords, special AI schema, generic keyword articles, invented author/review claims, or generated timestamps. Those would either not help the requested discovery channels or risk creating thin/unsupported content. The one material live discovery failure is Hive Due / Site Hesap: both public `robots.txt` and `sitemap.xml` endpoints currently serve HTML instead of their required text/XML files. This must be fixed by deployment of the existing shared-dist artifact and Nginx alias configuration, not by creating a second regional build.

## What primary guidance supports

| Source | Applicable conclusion |
|---|---|
| [Google: optimizing for generative AI Search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | Google AI Overviews/AI Mode use normal Search eligibility and quality signals. Prioritize crawlable, useful, people-first HTML and technical SEO; Google explicitly says `llms.txt`, special markup, forced chunking, and query-variant content are not required and do not improve Google visibility. |
| [Google: AI features and websites](https://developers.google.com/search/docs/appearance/ai-features) | Googlebot controls Search/AI-feature access. `Google-Extended` is separate from Search and controls some Gemini training/grounding uses. It is not an SEO ranking switch. |
| [Google: technical requirements](https://developers.google.com/search/docs/essentials/technical) and [technical SEO](https://developers.google.com/search/docs/fundamentals/get-started) | A page needs public access, a successful response, indexable content, consistent canonicals, crawlable resources, and an accurate sitemap to be eligible. Eligibility is not an indexing or ranking guarantee. |
| [Google: Organization markup](https://developers.google.com/search/docs/appearance/structured-data/organization) | Accurate Organization information on the company home/about page helps disambiguation; add only applicable, visible, verified properties. Existing Buhane source already uses its legal name, email, logo, URL, and verified `sameAs` records. |
| [OpenAI publishers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) and [OpenAI crawler docs](https://developers.openai.com/api/docs/bots) | `OAI-SearchBot` access is the relevant control for ChatGPT Search. It is independent of `GPTBot` model training. ChatGPT referral URLs add `utm_source=chatgpt.com`; accessibility/ARIA improve user-requested agent interactions. Neither document establishes `llms.txt` as a ChatGPT discovery mechanism. |

## Current source audit

### Technical and content baseline

- Fresh command: `PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode source --timeout 180 --report /tmp/260814-igz-source-audit.json`
- Result: `PASS [source] no findings`.
- Every editable public root has a source `robots.txt` (Hive generates host-qualified robots files), canonical sitemap data, and no images missing an `alt` attribute in its public HTML.
- All ordinary source robots rules already have `User-agent: *` / `Allow: /`, so **OAI-SearchBot is not blocked by the source**. This already satisfies the essential ChatGPT Search crawl-access prerequisite at the source level.
- No editable source currently has an `llms.txt`. This is appropriate: the sites already expose better-maintained human HTML plus sitemaps, and neither Google nor OpenAI primary guidance says such a file gains the requested discovery.
- Existing content is product-specific rather than generic: MoodJot has 10 translated editorial routes in 8 locales, Vynix has 10 editorial routes in 5 locales, Swipe Slip has 10 game guides, Glow Spin has 10 guides, AstralPost has 10 reflection guides across its supported route scope, Hoşkin has 10 guides in 5 locales, and Lastimo has 8 guides across its 12 addressable locales. Buhane has its bilingual company/portfolio/product-detail hub; Hive has resources/blog/guides/docs; Gridzle has an FAQ/HowTo guide; U2M has public guides/use cases/API documentation.

### Training and grounding policy is intentionally unresolved

The present source uses a permissive wildcard group, but does not publish separate `GPTBot`, `ClaudeBot`, or `Google-Extended` rules. The portfolio contract explicitly records:

```text
training_policy: owner_decision_required
```

Do not silently add an allow/block rule for those training/grounding agents. In particular, `Google-Extended` affects certain Gemini Apps training/grounding uses, while normal Google Search/AI Overview eligibility remains governed by Googlebot. The requested goal of reaching ChatGPT/Gemini users authorizes search-discovery analysis; it does not itself choose a model-training/grounding policy. Once the owner records a choice, rules must be added consistently to each public origin and verified after deployment.

## Live discovery finding: Hive Due / Site Hesap

On 2026-08-14, live header checks showed:

| URL | Live result | Expected contract |
|---|---|---|
| `https://hivedue.com/robots.txt` | GeoIP redirect to `sitehesap.com`, then `200 text/html` | Host-qualified `text/plain` robots content |
| `https://sitehesap.com/robots.txt` | `200 text/html` (home-page fallback) | `text/plain` `robots-sitehesap.txt` alias |
| `https://hivedue.com/sitemap.xml` | GeoIP redirect to `sitehesap.com`, then `200 text/html` | Host-qualified XML sitemap |
| `https://sitehesap.com/sitemap.xml` | `200 text/html` (home-page fallback) | `application/xml` `sitemap-sitehesap.xml` alias |

The maintained source already builds one shared `www/dist/` artifact with `robots-hivedue.txt`, `robots-sitehesap.txt`, `sitemap-hivedue.xml`, and `sitemap-sitehesap.xml`. Its documented Nginx configuration at `apps/HiveDue/deployment/nginx-hivedue-sitehesap.conf.example` has the exact `location = /robots.txt` and `location = /sitemap.xml` aliases. Therefore this is an **urgent deployment/configuration drift**, not a reason to create different locale artifacts. Deploy that one artifact to the configured release location and activate the documented exact aliases; then verify from a non-Türkiye egress for the Hive Due host and from Türkiye for Site Hesap.

## `llms.txt` audit

| Property group | Source state | Live observation | Action |
|---|---|---|---|
| All editable properties | No source `llms.txt` | Most hosts return their SPA/static home document with `200 text/html` for `/llms.txt`; this is a soft fallback, not a maintained LLM reading map. | Do not add mass `llms.txt` files. If a host needs strict 404 behavior for unknown files, make that a hosting rule, independently of SEO. |
| The Cosmic Meta | No verified local source | A Yoast-generated `llms.txt` is live but points to stale `cosmicmeta.ai` URLs. | External blocker: correct/remove it only in verified WordPress/hosting source after access is supplied. |

## Per-property matrix

| Property | Source state | Search/AI source opportunity | Deployment / external status |
|---|---|---|---|
| Buhane Bilgi Teknolojileri | Pass: 26 canonical EN/TR hub/detail routes, Organization schema, factual company links | No new content/markup needed; training decision is conditional | `main` is ahead 1; Phase 05/current source remains deployment-pending |
| ahmet.sh | Pass: single factual Person/Organization site and selected work links | No new content needed; do not invent language URLs | Source clean; deployment-pending from Phase 05 evidence |
| MoodJot | Pass: multilingual editorial/glossary generator contract | Keep non-medical/released-feature boundary; no mass articles | Source clean; live `/llms.txt` is a harmless but non-document fallback |
| Vynix | Pass: localized guides/glossary/docs and deterministic generator | Add new content only after verified feature/release evidence | Pre-existing `www/admin/dist/index.html` dirt; do not touch; source clean otherwise |
| Swipe Slip | Pass: ten factual game guides, glossary, FAQ/schema | Content taxonomy is sufficient; only enrich from real player/support questions | Source clean |
| Glow Spin | Pass: game guide/glossary/public-route contract | Content taxonomy is sufficient; only enrich from real player/support questions | Source clean |
| Hive Due / Site Hesap | Pass: one shared-dist regional source, resources/blog/guides/docs | No second build and no new generic content | **Urgent live robots/sitemap deployment drift**; `develop` ahead 2 |
| Astral Post | Pass: reflection guides, glossary, localized contract, responsible claim boundary | Preserve actual language scope and safety boundary; no invented wellness claims | `develop` ahead 2; source needs deployment |
| Gridzle | Pass: HowTo/FAQ and five canonical routes | Add new guides only from real gameplay/release evidence | `develop` ahead 5; pre-existing Android AdMob/XML + `.gsd` dirt is unrelated and must remain untouched |
| Hoşkin | Pass: five addressable locales, rules guides/glossary/feed | Store links remain “coming soon” until verified; no speculative launch content | Source clean |
| Lastimo | Pass: 12 localized public sets and strict product-truth constraints | Do not add history, analytics, custom-tracker, or medical claims | Source clean |
| U2M | Pass: public docs/use cases/API pages; private/token routes are excluded | Keep public AI-safe docs separate from authenticated/token paths | Source clean |
| The Cosmic Meta | No editable source | Existing live `llms.txt`/sitemap references are stale | **Externally blocked** pending real WordPress, hosting, SEO, media, analytics, and DNS/CDN access |

## Exact maintainable work items (maximum three)

### 1. Conditional crawler-policy implementation — do only after owner decision

**No implementation is approved yet.** Record a dated per-origin choice for `GPTBot`, `ClaudeBot`, and `Google-Extended` first. Then update the source of truth, not generated copies:

- `buhane.com.tr/robots.txt`
- `ahmet.sh/robots.txt`
- `apps/MoodJot/www/robots.txt`
- `apps/Vynix/www/robots.txt`
- `games/Swipe-Slip/www/robots.txt`
- `games/Glow-Spin/www/robots.txt`
- `apps/AstralPost/www/robots.txt`
- `games/Gridzle/www/robots.txt`
- `games/Hosgin/www/robots.txt`
- `apps/Lastimo/www/robots.txt`
- `u2m-api/frontend/public/robots.txt` (then regenerate `frontend/dist/robots.txt`)
- `apps/HiveDue/www/astro.config.mjs` (the host-qualified generated robots text, then build the one shared `dist`)

The only search-discovery rule that is already safe and active is `OAI-SearchBot: Allow` through the existing wildcard. If the eventual policy makes it explicit, retain that same access and prove the deployed file, CDN/WAF, and status code do not block it. Do not add advertising crawler rules or purchase/configure ads as part of this work.

### 2. Release correction — Hive Due / Site Hesap (required)

Deploy the current single shared Hive `apps/HiveDue/www/dist/` artifact once, with the exact host aliases from `apps/HiveDue/deployment/nginx-hivedue-sitehesap.conf.example`. No source rewrite is necessary. Validate each external discovery path with its required content type and correct hostname/locale canonical:

- `https://hivedue.com/robots.txt`, `https://hivedue.com/sitemap.xml` (non-Türkiye egress)
- `https://sitehesap.com/robots.txt`, `https://sitehesap.com/sitemap.xml` (Türkiye egress)

### 3. Evidence-led editorial maintenance — schedule after deployment, not before

Use the existing `docs/portfolio/DISCOVERY_AND_MEASUREMENT.md` day 0/28/90 contract to select the next *one or two* pages per product from real query, referral, support, and conversion evidence. Each candidate must state a released capability, a user problem, an owner/publisher, and a relevant next link; it must be locally addressable and localized only where a translation can be maintained. Do not manufacture content merely to expand a keyword list.

Required non-code setup after every deployment: verify the preferred origin in Google Search Console and Bing Webmaster Tools, submit/confirm the existing sitemap, use URL Inspection/Rich Results on representative pages, and capture `utm_source=chatgpt.com` referrals in the approved privacy-safe measurement contract. These are account actions and were not attempted.

## Repository preservation notes

- Buhane `main` is ahead 1 and contains the active quick-task planning directory as untracked work.
- Hive Due `develop` is ahead 2; AstralPost `develop` is ahead 2; these are the preceding audit corrections and have not been pushed/deployed.
- Vynix has pre-existing `www/admin/dist/index.html` modification.
- Gridzle is ahead 5 and has unrelated `androidApp/src/debug/res/values/admob.xml` modification plus untracked `.gsd/`.
- The unrelated Cosmic Meta repositories remain outside the authorized source boundary: `cosmicmeta` has a deleted `test.txt` plus `.DS_Store`; `cosmicmeta.ai` is not a Git repository; `cosmic-meta-api` has pre-existing Java/IDE/DS_Store dirt. Do not stage, restore, or deploy them as The Cosmic Meta's website source.

## Redeploy implications

1. **Immediately redeploy / repair:** Hive Due shared `dist` and active Nginx mapping on both hostname routes. This is the only new, high-severity live correction found.
2. **Deploy previously committed source before claiming current live SEO:** Buhane, Hive Due, AstralPost, and Gridzle have local commits ahead of their upstream branches; all twelve editable properties still have Phase 05 `deployment_pending` evidence rather than a verified released revision.
3. **If the owner later approves crawler-policy files:** redeploy every editable public property listed in work item 1, including the freshly built U2M and Hive artifacts. No `llms.txt` deployment is recommended.
4. **Cannot redeploy from this workspace:** The Cosmic Meta, until verified source/hosting access is provided.

RESEARCH COMPLETE

Artifact: `.planning/quick/260814-igz-t-m-buhane-portf-y-nde-seo-faydal-i-erik/260814-igz-RESEARCH.md`
