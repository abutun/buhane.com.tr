---
status: all_fixed
phase: 05
fixed_at: 2026-08-11T20:09:24Z
review_path: /Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr/.planning/phases/05-portfolio-discovery-content-and-brand-network/05-REVIEW.md
iteration: 3
findings_in_scope: 1
fixed: 1
skipped: 0
---

# Phase 05: Code Review Fix Report

**Iteration:** 3 (final automated fix pass)

**Findings in scope:** 1

**Fixed:** 1

**Skipped:** 0

## Iteration 3 Fix

### WR-01: Vynix `_blank` guard skipped browser-active attributes

**Repository:** `/Users/ahmet/Documents/Workspaces/Buhane/apps/Vynix`

**File:** `www/scripts/build-seo-content.mjs`

**Commit:** `89e20ff`

Replaced the anchor regex with a quote-aware opening-tag scanner so `>` inside a quoted attribute cannot truncate the tag before `target` or `rel`. Attribute names remain case-insensitive, quoted and unquoted values are parsed deterministically, and duplicate `target` or `rel` attributes continue to fail closed.

The validator now decodes decimal and hexadecimal numeric character references plus the relevant named HTML references before comparing `target` and splitting `rel` tokens. Browser-active `&#95;blank`, `&#x5f;blank`, and `&lowbar;blank` values therefore receive the same relation enforcement as literal `_blank`.

Negative regressions cover a prior quoted attribute containing `>`, decimal/hex/named encoded targets, an unquoted target, mixed-case markup, and duplicate `target`/`rel` attributes. A positive fixture verifies an encoded target with a named tab separator between both required relation tokens.

## Verification

- `node --check www/scripts/build-seo-content.mjs` — **passed** before and after commit.
- `node www/scripts/build-seo-content.mjs --check` — **passed** before and after commit; generated pages are current and the regression fixtures passed.
- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode source --timeout 180 --report /tmp/buhane-review-fix-iter3-source.json` — **zero findings**; the Vynix native command is check-only.
- The source report parses as JSON; scoped commit and repository `diff --check` checks passed.
- Generated Vynix blog, glossary, robots, and sitemap hashes are unchanged.
- Protected `www/admin/dist/index.html` dirt remains byte-for-byte unchanged and is the only Vynix worktree modification after the commit.
- The review and fix artifacts remain uncommitted. No push or deploy was performed.

## Prior Iteration History

### Iteration 2

- `98cd20a` — pin validated DNS addresses to the root HTTPS connection and harden timeout cleanup.
- `eb8338d` — suppress U2M token-bearing Nginx access logs.
- `b0665d0` — parse unquoted and duplicate Vynix link attributes.

### Iteration 1

- Root validator/registry: `85ad3db`, `2d2de47`, `c72a54b`, `9144089`, `fad1bdc`.
- U2M: `4f1072a`, `7707674`, `a68a8f1`.
- Vynix: `e335712`.

## Skipped Issues

None.

---

_Fixed: 2026-08-11T20:09:24Z_

_Fixer: Codex (gsd-code-fixer)_

_Iteration: 3 (cap reached; no further automated review/fix loop requested)_
