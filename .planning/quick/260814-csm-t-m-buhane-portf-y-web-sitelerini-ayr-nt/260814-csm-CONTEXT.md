# Quick Task 260814-csm: Portfolio-wide website audit and improvements - Context

**Gathered:** 2026-08-14
**Status:** Ready for planning

## Task Boundary

Audit every known Buhane public website, then fix source-level issues that are factual, safe, and testable. Deliver a concise per-site table explaining what changed, what was added, and any deployment or source-access follow-up.

## Implementation Decisions

### Audit depth

- Review SEO/discovery metadata, structured data, canonical/sitemap/robots consistency, locale routing, link safety, content truthfulness, accessibility basics, and visible interaction defects.
- Use the central portfolio registry and each repository's native checks as the source of truth; do not invent released capabilities or mass-produce low-value content.

### Change boundary

- Correct only verified source issues in editable repositories. Preserve unrelated user changes and generated-output contracts.
- Do not change production hosting, DNS, analytics, search-console, store listings, or the externally blocked Cosmic Meta property.

### Presentation scope

- Improve utility and consistency within established visual systems; no speculative redesigns or unrelated feature work.

### Claude's Discretion

- Prioritize concrete user-facing or crawlability regressions found by fresh audits.
- If a site already passes its source and native validations, record it as verified instead of changing it cosmetically.

## Specific Ideas

- The final report must be a compact Turkish table covering every known portfolio property.
- Clearly distinguish source fixes from pending deployment verification and external-access blockers.

## Canonical References

- `.planning/portfolio-sites.json`
- `.planning/phases/05-portfolio-discovery-content-and-brand-network/05-VERIFICATION.md`
- Each repository's `AGENTS.md`, generator, and native validation scripts.
