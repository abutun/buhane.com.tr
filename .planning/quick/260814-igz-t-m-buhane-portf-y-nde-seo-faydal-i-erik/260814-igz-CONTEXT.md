# Quick Task 260814-igz: Portfolio SEO, useful content, and AI discovery improvements - Context

**Gathered:** 2026-08-14
**Status:** Ready for planning

## Task Boundary

Research and improve every editable Buhane public website's search-discovery, people-first content, and AI-search discovery surface. Make only high-confidence, truthful source changes, and produce a precise redeploy list.

## Implementation Decisions

### Search and AI discovery

- Follow current official Google Search and OpenAI crawler guidance: accessible, indexable public HTML; accurate sitemaps/structured data; unique, useful content; and non-blocking rules for search discovery where the public marketing surface is intended to be crawled.
- Do not claim that `llms.txt` improves Google ranking or AI answers. Add or revise it only where a short, accurate, maintained reading map is useful; it remains optional.

### Crawler policy

- Preserve the separate choice between search/indexing crawlers and model-training crawlers. Allowing search discovery must not silently opt the portfolio into unrelated model-training crawlers.
- Do not add ChatGPT advertising crawler rules, purchase ads, change search-console settings, modify WAF/CDN, or alter deployment/GeoIP infrastructure.

### Content enrichment

- Add only factual, product-contextual material that reflects released capabilities and existing product vocabulary. Prefer high-value page summaries, clear use-case/FAQ context, and navigable source documents over bulk generic articles or keyword stuffing.
- Respect every repository's locale and generator contract. Do not claim a locale is localized if only English content is available.

### Change and reporting boundary

- Audit every registered property. Modify only sites with a clear source-level opportunity and preserve existing unrelated dirt and generated-output contracts.
- Provide a Turkish report that separates changed-source redeploys from deploy verification, non-changing audited sites, and the externally blocked Cosmic Meta property.

## Specific Ideas

- Candidate tactics to evaluate: public robots rules for OAI-SearchBot, accurate llms.txt discovery maps, crawlable content hubs and contextual navigation, Organization/Product/WebSite schema completeness, descriptive metadata and sitemap inclusion.
- Final report must name each source repository that needs redeployment, plus the exact reason.

## Canonical References

- Google: AI optimization guide, technical SEO guidance, Organization structured-data documentation, crawler documentation.
- OpenAI: Publishers and Developers FAQ; advertiser crawler guidance (only as non-goal context).
- `.planning/portfolio-sites.json` and Phase 05 release/discovery evidence.
