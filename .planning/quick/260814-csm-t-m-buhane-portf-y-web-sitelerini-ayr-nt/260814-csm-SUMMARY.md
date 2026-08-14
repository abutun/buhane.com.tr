---
quick_task: 260814-csm
title: Portfolio-wide website audit and verified improvements
status: complete
completed_at: 2026-08-14
source_commits:
  astral_post: 8cc4344
  hive_due: c8aeadcf
review_followup_commits:
  astral_post: e19d6d1
  hive_due: 30edca9e
---

# Execution summary

## Completed source changes

1. **Astral Post** — commit `8cc4344 fix(www): secure privacy policy links`
   - Added `rel="noopener noreferrer"` to all seven external privacy-policy links that open a new tab.
   - Added a native content-hub regression guard for external privacy `target="_blank"` links missing either rel token.
   - Verification passed: content hub reported 9 locales, 90 articles, 135 glossary terms, 112 canonical sitemap URLs, and 112 JSON-LD blocks; the focused link command found 7 safe links and 0 unsafe links.

2. **Hive Due / Site Hesap** — commit `c8aeadcf fix(www): clarify unavailable store actions`
   - Replaced four unavailable App Store/Google Play `href="#"` surfaces with non-interactive localized coming-soon content. The real web-app CTA remains a link.
   - Added a publication-contract assertion covering both shared components.
   - Updated `www/DEPLOY.md` with the one shared release root, correct `../deployment/` Nginx-example path, four discovery aliases, host-local Hive Due `/` redirect requirement, exact MIME probes, and the separate operator-only infrastructure boundary.
   - Verification passed: `npm run check` (0 diagnostics), `npm test` (5 files / 26 tests), `npm run verify:regional-assets` (85 HTML / 26 local assets), and focused no-placeholder check.

## Post-review follow-up

1. **Astral Post** — commit `e19d6d1 fix(www): guard HTTP privacy links`
   - Broadened the privacy new-tab selector from HTTPS-only to HTTP(S), so an insecure `http://` external link cannot bypass the required `noopener noreferrer` check.
   - Added deterministic selector fixtures covering `https://`, `http://`, and a local path; the local path remains outside the external-link rule.
   - Post-review verification passed: `node www/scripts/verify-content-hub.mjs` (9 locales, 90 articles, 135 glossary terms, 112 canonical sitemap URLs, 112 JSON-LD blocks).

2. **Hive Due / Site Hesap** — commit `30edca9e docs(www): clarify regional deployment probes`
   - Made the deployment handoff country-aware: Türkiye egresses are expected to receive the regional `hivedue.com` to `sitehesap.com` redirect, while direct Hive Due discovery checks require a confirmed non-Türkiye egress.
   - Kept the exact raw canonical and discovery probes, grouped them by the required egress, and preserved the one-shared-root and no-production-mutation constraints.
   - Post-review verification passed: `npm run check` (0 diagnostics), `npm test` (5 files / 26 tests), and `npm run verify:regional-assets` (85 HTML / 26 local assets through both Host headers).

## Central audit verification

- `python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode registry` — exit 0, no findings.
- `python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode source --timeout 180 --report /tmp/260814-csm-source.json` — exit 0, high/medium/low/info 0/0/0/0.
- `python3 -m unittest discover -s scripts/tests -p 'test_*.py'` — exit 0, 55 tests passed. The suite intentionally printed two `GEN.COMMAND_TIMEOUT` fixture outcomes while testing timeout handling; they are not source-validation findings.
- `260814-csm-AUDIT-REPORT.md` table contract — passed: all 13 registry display names appear once, states are permitted, the exact Cosmic Meta blocker is preserved, and the report makes no false local-deployment claim.

## Portfolio states

| Property | Audit state |
|---|---|
| Buhane Bilgi Teknolojileri | Kaynak doğrulandı |
| ahmet.sh | Kaynak doğrulandı |
| MoodJot | Kaynak doğrulandı |
| Vynix | Kaynak doğrulandı |
| Swipe Slip | Kaynak doğrulandı |
| Glow Spin | Kaynak doğrulandı |
| Hive Due / Site Hesap | Kaynak düzeltmesi yapıldı |
| Astral Post | Kaynak düzeltmesi yapıldı |
| Gridzle | Kaynak doğrulandı |
| Hoşkin | Kaynak doğrulandı |
| Lastimo | Kaynak doğrulandı |
| The Cosmic Meta | Harici erişim engeli |
| U2M URL Shortener | Kaynak doğrulandı |

## Remaining operator/external follow-up

- Deploy verification remains separate from source verification for every editable property. No server, Nginx, GeoIP, symlink, DNS/CDN, cache, analytics, search-account, or store-listing action occurred.
- After an authorized Hive Due deployment, the operator must retain raw evidence that each host’s `/robots.txt` returns `text/plain`, each `/sitemap.xml` returns XML, and GeoIP redirect behavior retains the shared-root contract.
- The Cosmic Meta remains blocked until verified WordPress administration and authoritative source/deployment ownership are supplied. Exact blocker: No verified local source, repository, build, deploy pipeline, or WordPress administration path has been shown to own `https://thecosmicmeta.com/`.

## Preserved worktree state

- Astral Post and Hive Due were clean at task start; each is clean after its scoped source commits and is two commits ahead of `origin/develop` pending the orchestrator’s publish decision.
- Root `buhane.com.tr` intentionally has only this uncommitted quick-task directory, including the plan, context, research, audit report, and this summary. No root file was staged or committed.
- Previously reported unrelated state was untouched: Vynix `www/admin/dist/index.html` and Gridzle’s active `.gsd/` work; no Cosmic Meta local directory was edited.
