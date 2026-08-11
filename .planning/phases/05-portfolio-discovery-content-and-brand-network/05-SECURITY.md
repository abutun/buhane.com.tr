---
phase: "05"
slug: portfolio-discovery-content-and-brand-network
status: verified
threats_open: 0
asvs_level: 1
block_on: high
register_authored_at_plan_time: true
created: 2026-08-11
verified: 2026-08-11
---

# Phase 05 — Security

> ASVS Level 1 verification of the threat models authored in all 14 Phase 05 plans. Every high-severity threat is mitigated; no risk was silently accepted or transferred.

## Trust Boundaries

| Boundary | Description | Data crossing |
|---|---|---|
| Private registry → public sources | Reviewed origins, claims, locales, ownership, link allowlists, and native validation commands drive public validation and generation. | Private planning metadata; no registry file may be deployed. |
| Validator → local repositories | The central validator reads public sources and runs exact native commands. | Repository paths, build/test output, and reports; commands are structured, code-approved argv/cwd with no shell. |
| Validator → public network | Live validation fetches allowlisted public origins. | Public HTTP metadata only; connections are no-proxy, pinned to prevalidated global IPs, TLS/SNI verified, redirect- and response-bounded. |
| Public sites → visitors/crawlers | Static pages expose company/product claims, canonical discovery data, contextual links, and privacy-safe measurement hooks. | Public content only; no journal text, tokens, target URLs, auth IDs, or other user content. |
| Product source → generated public tree | Several sites generate localized/editorial pages from reviewed catalogs. | Reviewed static copy and schema; generators/checkers enforce truth, locale, route, and link contracts. |
| Local worktrees → Phase 05 commits | Repositories contained unrelated or user-owned dirt. | Only path-scoped Phase 05 files were committed; named exclusions were hash/status preserved. |

## Threat Register

| Threat ID | Threat | Component | Severity | Disposition | Mitigation | Status |
|---|---|---|---|---|---|---|
| T-05-01-01 | Private registry disclosure | Central registry/validator | high | mitigate | Exclude `.planning/**` from deploy inventories and fail validation if linked or sitemapped. | closed |
| T-05-01-02 | SSRF/open redirect through live validator | Central live validator | high | mitigate | Code-owned origins, public-IP resolution, pinned no-proxy TLS transport, redirect caps, timeouts, and no credentials. | closed |
| T-05-01-03 | Claim or schema tampering | Central source validator | high | mitigate | Compare public claims/entity IDs to reviewed registry fields and fail closed. | closed |
| T-05-01-04 | Link-farm generation | Central link contract | medium | mitigate | Enforce per-page allowlists and reject repeated sibling portfolios. | closed |
| T-05-01-05 | Report path overwrite | Validator reporting | medium | mitigate | Caller-explicit report paths and validator-created temporary native reports outside public roots. | closed |
| T-05-02-01 | Misleading product claims/schema | Buhane hub | high | mitigate | Render only registry-reviewed claims and reject Lastimo exclusions. | closed |
| T-05-02-02 | JSON-LD/script injection | Buhane hub | high | mitigate | Static escaped strings/JSON serialization and parse every JSON-LD block. | closed |
| T-05-02-03 | Reverse-tabnabbing or unsafe outbound CTA | Buhane hub | medium | mitigate | HTTPS preferred origins and `rel="noopener noreferrer"` for new-tab links. | closed |
| T-05-02-04 | Private artifact exposure | Buhane hub | high | mitigate | Exclude planning/scripts from links, sitemap, and deploy allowlist. | closed |
| T-05-02-05 | Cross-language drift | Buhane hub | medium | mitigate | Exact route/product/CTA parity and reciprocal alternate validation. | closed |
| T-05-03-01 | Misleading health/personal tracking claims | Lastimo | high | mitigate | Repository v1 allowlist enforced before generation and in verifier fixtures. | closed |
| T-05-03-02 | Sensitive tracker data in analytics/examples | Lastimo | high | mitigate | No personal values, user content, analytics payloads, or realistic private fixtures. | closed |
| T-05-03-03 | Generated-source bypass | Lastimo | high | mitigate | Source-only edits, deterministic check, and generated-boundary review. | closed |
| T-05-03-04 | Schema/content mismatch | Lastimo | high | mitigate | Parse schema and reject excluded features, ratings, prices, and self-publisher nodes. | closed |
| T-05-03-05 | Locale drift | Lastimo | medium | mitigate | Twelve-locale reciprocity preserved; English-only editorial is not falsely localized. | closed |
| T-05-04-01 | Host/header poisoning | Hive Due/Site Hesap | high | mitigate | Two compile-time variants; metadata never derives from arbitrary request Host. | closed |
| T-05-04-02 | Canonical cloaking/client mutation | Hive Due/Site Hesap | high | mitigate | Raw HTML tests and no browser metadata mutation. | closed |
| T-05-04-03 | Duplicate regional indexing | Hive Due/Site Hesap | high | mitigate | Host-local sitemaps and canonical/noindex rules for noncanonical locale copies. | closed |
| T-05-04-04 | Misleading payment/integration claims | Hive Due/Site Hesap | high | mitigate | Registry/repository truth gate for copy and schema. | closed |
| T-05-04-05 | Build output collision | Hive Due/Site Hesap | medium | mitigate | Separate ignored variant outputs and repository-exclusive generation. | closed |
| T-05-05-01 | Unsupported AI/model marketing claims | Vynix | high | mitigate | Repository evidence; reject model counts, testimonials, ratings, and guarantees. | closed |
| T-05-05-02 | Dirty admin overwrite | Vynix | high | mitigate | Protected admin hash, generator exclusion, isolated fixes, and scoped staging. | closed |
| T-05-05-03 | Duplicate-host indexing | Vynix | high | mitigate | No-www preferred origin across source/generated discovery signals. | closed |
| T-05-05-04 | Generated-source bypass | Vynix | high | mitigate | Generator-owned edits, deterministic `--check`, and hardened anchor parser fixtures. | closed |
| T-05-05-05 | Client-language false indexing | Vynix | medium | mitigate | One canonical and no fabricated locale alternates. | closed |
| T-05-06-01 | Unsafe wellbeing/AI outcome claims | Astral Post | high | mitigate | Repository safety constraints and registry truth gate in catalog/schema. | closed |
| T-05-06-02 | Anonymous-community privacy overclaim | Astral Post | high | mitigate | Only evidenced privacy/moderation wording. | closed |
| T-05-06-03 | Generated-source bypass | Astral Post | high | mitigate | Catalog/template edits, exclusive regeneration, and verifier enforcement. | closed |
| T-05-06-04 | False locale coverage | Astral Post | medium | mitigate | No hreflang for client states; reciprocal paired glossary routes only. | closed |
| T-05-06-05 | Link-farm footer | Astral Post | medium | mitigate | One owner link and per-page allowlisted contextual links. | closed |
| T-05-07-01 | Incorrect game rules/store claims | Hoşkin | high | mitigate | Claims validated against repository/registry before regeneration. | closed |
| T-05-07-02 | Locale misinformation | Hoşkin | high | mitigate | Website translation distinguished from app-language availability. | closed |
| T-05-07-03 | Generated-tree overwrite | Hoşkin | high | mitigate | Exclusive execution, source-only edits, and post-build diff review. | closed |
| T-05-07-04 | Structured-data fabrication | Hoşkin | high | mitigate | Reject ratings, prices, reviews, and unverified availability. | closed |
| T-05-07-05 | RTL regression | Hoşkin | medium | mitigate | Preserve/test `dir="rtl"` and Arabic rendering. | closed |
| T-05-08-01 | Medical/wellness misinformation | MoodJot | high | mitigate | Visible non-medical boundaries; no diagnosis, treatment, or outcome promises. | closed |
| T-05-08-02 | Sensitive journal data in measurement/examples | MoodJot | high | mitigate | No journal text, personal values, email/auth IDs, or user content. | closed |
| T-05-08-03 | Admin/referral surface regression | MoodJot | high | mitigate | Admin/referral paths excluded from edits/sitemap and hash/status checked. | closed |
| T-05-08-04 | False locale indexing | MoodJot | medium | mitigate | One canonical and no hreflang for client language states. | closed |
| T-05-08-05 | Cross-site link spam | MoodJot | medium | mitigate | One owner link and contextual allowlisted siblings only. | closed |
| T-05-09-01 | Misleading game/level marketing | Swipe Slip | high | mitigate | Current 200-level and tap-gameplay contract enforced. | closed |
| T-05-09-02 | Cross-site link spam | Swipe Slip | high | mitigate | Repeated sibling footer removed; contextual allowlist only. | closed |
| T-05-09-03 | Stale identity propagation | Swipe Slip | high | mitigate | Cosmic ownership removed; stable Buhane publisher required. | closed |
| T-05-09-04 | Unrelated repository overwrite | Swipe Slip | high | mitigate | Website-only scope and preserved iOS-project hash/status. | closed |
| T-05-09-05 | Unsafe/fabricated schema | Swipe Slip | medium | mitigate | Parse JSON-LD and reject ratings, prices, reviews, and unsupported availability. | closed |
| T-05-10-01 | Misleading gameplay/wellbeing claims | Glow Spin | high | mitigate | Repository truth review; unsupported counts/outcomes rejected. | closed |
| T-05-10-02 | Cross-site link spam | Glow Spin | high | mitigate | One owner link and contextual allowlisted game links only. | closed |
| T-05-10-03 | Unrelated shared-project changes | Glow Spin | high | mitigate | Glow Spin `www/**` scope; Swipe Slip/Firebase excluded. | closed |
| T-05-10-04 | Structured-data fabrication | Glow Spin | medium | mitigate | Reject ratings, prices, reviews, downloads, and unsupported availability. | closed |
| T-05-10-05 | Sitemap/canonical drift | Glow Spin | medium | mitigate | Exact route, canonical, Open Graph, and sitemap comparison. | closed |
| T-05-11-01 | Mixed legacy/preferred origins | Gridzle | high | mitigate | Atomic migration to `gridzle.app` and zero public legacy-origin matches. | closed |
| T-05-11-02 | Misleading game/live-service claims | Gridzle | high | mitigate | Active release truth contract; unverified schema/offers rejected. | closed |
| T-05-11-03 | Missing/mismatched sitemap | Gridzle | high | mitigate | Native and central exact route-inventory comparison. | closed |
| T-05-11-04 | Dependency supply-chain expansion | Gridzle | medium | mitigate | Public site remains dependency-free Python/HTML/CSS and build-free. | closed |
| T-05-11-05 | Generated report staging | Gridzle | low | mitigate | Central commands use validator-created temporary reports; repo dirt stays unstaged. | closed |
| T-05-12-01 | Auth/private route indexing or data exposure | U2M | high | mitigate | Public allowlist, sitemap exclusion, noindex/auth tests, and private-route contract. | closed |
| T-05-12-02 | XSS in generated docs/content | U2M | high | mitigate | Escape HTML/attributes and JSON-serialize schema from reviewed static records. | closed |
| T-05-12-03 | User shortened-target/token leakage | U2M | high | mitigate | No target URLs/tokens/user IDs in public pages, schema, events, controller logs, or sensitive Nginx access logs. | closed |
| T-05-12-04 | Route-config divergence | U2M | high | mitigate | Spring, all three Nginx configs, Vue/Vite, Playwright, and Gradle contract tests. | closed |
| T-05-12-05 | Generated-source bypass | U2M | medium | mitigate | Generator/source edits, check mode, and ignored dist output. | closed |
| T-05-13-01 | Identity/founder misrepresentation | ahmet.sh | high | mitigate | Factual visible relationship and verified identity profiles only. | closed |
| T-05-13-02 | Unsupported portfolio claims | ahmet.sh | high | mitigate | Registry-derived names, origins, features, and lifecycle states. | closed |
| T-05-13-03 | Local user-file overwrite | ahmet.sh | high | mitigate | `.DS_Store` hash/status preserved and never staged. | closed |
| T-05-13-04 | False locale indexing | ahmet.sh | medium | mitigate | One canonical/sitemap URL and no client-state hreflang route. | closed |
| T-05-13-05 | Link-farm duplication | ahmet.sh | medium | mitigate | Six curated projects plus one full-portfolio CTA. | closed |
| T-05-14-01 | False release attestation | Release validation | high | mitigate | Source, deployed, account, and blocker states are separate and timestamped. | closed |
| T-05-14-02 | Live-validator SSRF/credential leakage | Release validation | high | mitigate | Code-owned host contract, pinned public-IP transport, no proxy/credentials, bounds, and adversarial tests. | closed |
| T-05-14-03 | External account mutation | Release validation | high | mitigate | Read-only checks only; deploy/DNS/Search/analytics/IndexNow remain owner follow-ups. | closed |
| T-05-14-04 | Cosmic proxy-source overwrite | Release validation | high | mitigate | Three unrelated Cosmic directories are immutable exclusions with pre/post evidence. | closed |
| T-05-14-05 | Analytics user-content leakage | Release validation | high | mitigate | Fixed six-event/five-property allowlist and explicit forbidden-data assertions. | closed |

## Closure Evidence

- [05-VERIFICATION.md](./05-VERIFICATION.md) independently verifies 12/12 requirements, 7/7 roadmap success criteria, and 14/14 plan must-have groups against actual sources.
- Fresh central gates passed: 53/53 unit tests, registry validation with zero findings, and strict source/native validation with zero findings across all 12 editable properties.
- [05-REVIEW-FIX.md](./05-REVIEW-FIX.md) records three review/fix iterations. Critical findings for shell execution, live-validator SSRF/proxy/rebinding, U2M token logging, and duplicate U2M origins were closed with code and regression tests.
- The final Vynix anchor-parser warning was closed by commit `89e20ff`; quote-aware tag scanning, numeric/named character-reference decoding, duplicate detection, and negative fixtures pass.
- [05-RELEASE-STATUS.json](./05-RELEASE-STATUS.json) preserves the non-live state: 12 `deployment_pending`, one `externally_blocked`, zero `deployed_verified`, and all 40 live findings mapped once.
- Protected Vynix, Swipe Slip, ahmet.sh, Gridzle, and Cosmic paths remain excluded/preserved; concurrent Gridzle Phase 50 work was not staged or rewritten by Phase 05.

## Accepted Risks Log

No accepted risks. Deployment, certificate/DNS, search-console, analytics, and other account-gated follow-ups are pending operational work, not accepted security exceptions.

## Security Audit Trail

| Audit Date | Threats Total | Closed | Blocking Open | Run By |
|---|---:|---:|---:|---|
| 2026-08-11 | 70 | 70 | 0 | Codex secure-phase, ASVS L1 |

The register was authored at plan time in all 14 plan threat models. With `asvs_level: 1`, `block_on: high`, and zero preliminarily open threats after independent verification and code-review remediation, the workflow's L1 short-circuit applies; no additional deep auditor was required.

## Sign-Off

- [x] All threats have a disposition.
- [x] No accepted risk is hidden or undocumented.
- [x] `threats_open: 0` confirmed.
- [x] `status: verified` set in frontmatter.

**Approval:** verified 2026-08-11
