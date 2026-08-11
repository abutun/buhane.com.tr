# Phase 5 Context: Portfolio Discovery, Content, and Brand Network

**Captured:** 2026-08-11
**Source:** User portfolio brief plus Phase 5 research audit

<decisions>

## Locked owner decisions

- **D-01 — portfolio-scope:** Treat MoodJot, Vynix, Swipe Slip, Glow Spin, Hive Due / Site Hesap, Astral Post, Gridzle, Hoşkin, Lastimo, The Cosmic Meta, and U2M as the eleven Buhane products in scope. Treat `ahmet.sh` as Ahmet's personal site and `buhane.com.tr` as the authoritative company hub.
- **D-02 — regional-domain:** Treat `hivedue.com` as the rest-of-world Hive Due destination and `sitehesap.com` as the Türkiye destination. Preserve an explicit locale/region relationship instead of presenting the two domains as unrelated products.
- **D-03 — all-editable-sites:** Update every supplied local website source that can be changed safely. Do not pretend The Cosmic Meta is locally editable when the live WordPress source/admin path is absent.
- **D-04 — content-breadth:** Add or improve blogs, guides, glossaries, use cases, FAQs, app-context explanations, and company presentation where they add factual product-specific value; do not target a fixed page count or create near-duplicate portfolio content.
- **D-05 — cross-linking:** Make Buhane the central owner/publisher hub. Each editable product site should link visibly to Buhane; sibling-product links must be task-relevant and limited rather than a repeated all-products footer.
- **D-06 — search-ai-foundation:** Optimize for indexable visible HTML, canonical URLs, useful internal links, sitemaps, accurate structured data, and people-first content. Do not add hidden AI keywords, special AI schema, or treat `llms.txt` as a ranking requirement.
- **D-07 — product-truth:** Published copy and schema must stay within released, reviewable product capabilities. Where public claims contradict repository scope—especially Lastimo—remove or soften unsupported claims rather than expanding them.
- **D-08 — preferred-origins:** Use the final HTTPS product origins observed in current redirects and recorded in the registry. Keep legacy domains only as redirect aliases and never use them for new canonical/schema/sitemap/cross-link URLs.
- **D-09 — localization:** Preserve each site's current locale architecture. Add `hreflang` only for stable addressable localized pages; a JavaScript language switch on one URL does not become multiple indexed language pages.
- **D-10 — existing-changes:** Preserve unrelated user changes, including Vynix `www/admin/dist/index.html`, `ahmet.sh/.DS_Store`, and unrelated Cosmic Meta working-directory changes. Generated sites must be changed through their source/generator.

## Implementation discretion

- Choose the smallest useful page set per site based on current content gaps.
- Reuse each repository's current visual system and stack; no portfolio-wide framework migration or visual redesign.
- A dependency-free central registry/validator may live in the Buhane repository, while site-local source remains independently deployable.
- Search Console, Bing Webmaster Tools, IndexNow, crawler-policy, deployment, and analytics configuration that require account credentials may be delivered as exact follow-up documentation rather than fabricated or silently attempted.

## Deferred / externally blocked

- **D-11 — cosmic-meta-access:** Do not modify the older `cosmicmeta`, `cosmicmeta.ai`, or `cosmic-meta-api` directories as a substitute for the live `thecosmicmeta.com` WordPress site. Record the stale `cosmicmeta.ai` `llms.txt` issue and required admin/source access.
- Production deployment, DNS/CDN redirect changes, search-platform ownership verification, and analytics account mutations are outside local-source execution unless separately authorized.

</decisions>

## Portfolio paths

The authoritative path/origin inventory is in `05-RESEARCH.md`. The implementation must re-check every repository's `AGENTS.md` before editing and run its native generator/test/verification contract.

## Outcome boundary

Phase 5 is complete when all safely editable local sites have the highest-value truthful discovery and ownership improvements appropriate to their architecture, the Buhane hub represents all eleven products in English and Turkish, cross-links follow the approved graph, and validation plus blocked external follow-ups are documented. It is not complete merely because metadata was added.
