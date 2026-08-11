# Portfolio Validation and Publication Contract

This contract keeps Buhane's independently deployed sites aligned with the private portfolio registry. The registry at `.planning/portfolio-sites.json`, the validator, its tests, and generated reports are operational inputs. They are not public website content.

## Commands

Run commands from the Buhane repository root.

Registry-only validation checks product truth, origins, entity IDs, ownership, claim exclusions, publication variants, repository boundaries, and pending-rule safety:

```bash
python3 scripts/validate_portfolio.py \
  --manifest .planning/portfolio-sites.json \
  --mode registry \
  --report /tmp/buhane-portfolio-registry.json
```

Source validation runs declared variant builds and repository-native checks, then inspects each raw public output independently:

```bash
python3 scripts/validate_portfolio.py \
  --manifest .planning/portfolio-sites.json \
  --mode source \
  --report /tmp/buhane-portfolio-source.json
```

During an intermediate repository plan, repeat `--site` to limit source work and use `--allow-pending` only for registry-declared missing route, robots, or sitemap rules:

```bash
python3 scripts/validate_portfolio.py \
  --manifest .planning/portfolio-sites.json \
  --mode source \
  --site gridzle \
  --allow-pending \
  --report /tmp/buhane-gridzle-incremental.json
```

Release validation must omit `--allow-pending`. It is never allowed to suppress an existing-output, canonical, schema, product-truth, private-route, security, origin, or product-identity failure.

Live validation is for deployed preferred and legacy origins. It follows at most three redirects, applies per-request timeouts, and refuses URLs outside manifest origins before opening a connection:

```bash
python3 scripts/validate_portfolio.py \
  --manifest .planning/portfolio-sites.json \
  --mode live \
  --timeout 20 \
  --report /tmp/buhane-portfolio-live.json
```

Run the dependency-free test suite before changing registry or validation rules:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest scripts.tests.test_validate_portfolio
```

## Severity and exit semantics

| Severity | Meaning | Release action |
|---|---|---|
| `high` | Truth, security, identity, canonical, private-route, publication-variant, or discovery contract is broken | CLI exits nonzero; block commit/release until fixed or the plan records a genuine external blocker |
| `medium` | Material quality or maintainability concern that does not currently violate a fail-closed rule | Review and resolve or record an owner and due date |
| `low` | Limited-scope improvement | Triage without treating it as release proof |
| `info` | Evidence or context | No release block by itself |

The process exit status is `1` whenever at least one `high` finding exists and `0` otherwise. Manifest parse and CLI usage failures exit `2`. Human-readable findings and the JSON report describe the same run.

## Report contract

The top-level report contains:

- `mode`: `registry`, `source`, or `live`.
- `started_at`: UTC run timestamp.
- `sites`: object keyed by property ID. Each entry reports its preferred origin, expected product entity ID, and severity counts.
- `sites.<id>.publication_variants`: for multi-output products, an object keyed by variant ID with raw output root, preferred origin, inherited product entity ID, and independent severity counts.
- `findings`: deterministic finding records.
- `severity_counts`: portfolio totals for `high`, `medium`, `low`, and `info`.
- `skipped_pending_rules`: exact stable rule IDs skipped by an explicit `--allow-pending` run.
- `exit_status`: the CLI release decision.

Every finding contains exactly `finding_id`, `rule_id`, `property_id`, nullable `publication_variant`, `severity`, `message`, and non-secret `evidence`. `finding_id` derives from the property, publication variant, rule, and route so the same rule on different sites or outputs cannot be conflated.

Reports may contain local paths and public URLs, but must never contain credentials, cookies, authorization headers, user records, or product user content. Always pass a deliberate `--report` path outside a product public root. The validator does not choose or write a report path unless the caller supplies one.

## Product identity and schema rule

The registry's `product_entity_id` is the only product identity allowed in product and editorial schema:

- A home or product page's primary `SoftwareApplication`, `WebApplication`, or `VideoGame` node uses the exact registered `@id`.
- An `Article`, `BlogPosting`, `FAQPage`, `HowTo`, or other declared editorial node references that exact product ID through `about`, `mainEntity`, `isPartOf`, or the record's explicit product-reference property.
- Buhane product-detail pages reuse the same preferred-origin product ID used by the product site. A route-local identity such as `/guide/#product` is not allowed.
- `publisher` references `https://buhane.com.tr/#organization`; product websites are not added to the organization's `sameAs` list.
- Hive Due and Site Hesap are one product. Both `dist/hivedue` and `dist/sitehesap` use `https://hivedue.com/#product`, even though Site Hesap canonicals and discovery files use `sitehesap.com`.

Schema validity is not proof of a claim. Visible copy and JSON-LD must stay within `verified_features`, avoid `excluded_claims`, and agree with the responsible repository's product instructions.

## Source and generator ownership

- Direct-static sites may be edited in their public tree, but admin, referral, application, and unrelated shared-repository paths remain outside the plan boundary.
- Vynix blog/glossary/discovery output is owned by `www/scripts/build-seo-content.mjs`; `www/admin/dist/index.html` belongs to a separate admin build.
- Astral Post content pages, feed, sitemap, and robots are owned by `content/catalog.mjs` plus `scripts/build-content-pages.mjs`.
- Hive Due/Site Hesap outputs are ignored build artifacts under `dist`; edit Astro inputs and build each host variant.
- Hoşkin locale trees, feeds, sitemap, and robots are fully generator-owned by `scripts/build.mjs` and content modules.
- Lastimo public HTML, locale assets, feed, sitemap, and robots are fully generator-owned by `src/*.mjs`. Correct truth records before regeneration.
- Vue/Astro `dist`, Python verification reports, and comparable ignored output are not staged.
- The Cosmic Meta remains `external_blocked`. Do not substitute `cosmicmeta`, `cosmicmeta.ai`, or `cosmic-meta-api` for the unavailable live WordPress source.

Never split a generated site's source edit and regeneration across concurrent plans. After any generator or build, inspect `git status --short`, confirm only owned paths changed, and run both the native contract and central validator.

## Repository-native command matrix

| Property | Working directory | Required native commands after a scoped change |
|---|---|---|
| MoodJot | `apps/MoodJot/www` | No native website validator; use central source validation plus local preview |
| Vynix | `apps/Vynix/www` | `node scripts/build-seo-content.mjs` then `node scripts/build-seo-content.mjs --check` |
| Swipe Slip | `games/Swipe-Slip/www` | No native website validator; use central source validation plus local preview |
| Glow Spin | `games/Glow-Spin/www` | No native website validator; use central source validation plus local preview |
| Hive Due / Site Hesap | `apps/HiveDue/www` | `npm run check`, `npm test`, `npm run build:hivedue`, `npm run build:sitehesap` |
| Astral Post | `apps/AstralPost/www` | `node scripts/build-content-pages.mjs`, `node scripts/verify-content-hub.mjs` |
| Gridzle | `games/Gridzle/www` | `python3 ../tools/verify_www_foundation.py --root . --output ../shared/build/reports/www/www-foundation.json`, then `python3 ../tools/verify_www_hosting.py --root . --output ../shared/build/reports/www/www-hosting-smoke.json` |
| Hoşkin | `games/Hosgin/www` | `node scripts/build.mjs`, `node scripts/validate.mjs` |
| Lastimo | `apps/Lastimo/www` | `npm run build`, `npm run check`, `npm test`, `npm run verify` |
| Buhane | `buhane.com.tr` | Central validation and an HTTP-root preview covering `/` and `/tr/` |
| U2M frontend | `u2m-api/frontend` | `npm run build`, `npm run test:unit`, `npm run test:e2e`; also run `./gradlew test` from `u2m-api` if routing contracts change |
| ahmet.sh | `ahmet.sh` | Central validation plus local preview |
| The Cosmic Meta | Not locally available | External HTTP inspection only after the actual admin/deploy source is obtained |

## Dirty-path exclusions

Path-scoped staging is mandatory. Preserve and exclude:

- Buhane active planning state outside the current task, including `.planning/**`, plus `app-ads.txt` and `yandex_abc334285efd6c2e.html`.
- Vynix `www/admin/dist/index.html`.
- ahmet.sh `.DS_Store`.
- Gridzle `shared/build/reports/www/**`.
- Hive Due `www/dist/**` and `www/.astro/**` as ignored output.
- U2M `frontend/dist/**` as ignored output.
- The unrelated `cosmicmeta/**`, `cosmicmeta.ai/**`, and `cosmic-meta-api/**` directories.

Never use blanket staging across a shared app/game repository.

## Deployment separation and release allowlist

The Buhane repository root contains both public website files and private operational files. A repository-root static upload must use an explicit allowlist, not “upload everything.” The public Buhane deployment may include only reviewed public routes/assets such as:

```text
index.html
tr/**
products/**
styles.css
script.js
images/**
robots.txt
sitemap.xml
app-ads.txt
yandex_abc334285efd6c2e.html
```

The deploy job must deny at least:

```text
.planning/**
scripts/**
docs/portfolio/**
**/*portfolio*.json
**/*validation-report*.json
```

In particular, `.planning/portfolio-sites.json`, validator source/tests, and validator reports must never be linked from HTML, listed in a sitemap, copied into a public root, or published as generic repository artifacts. Before release, compare the staged deploy inventory against this allowlist and confirm `app-ads.txt` and `yandex_abc334285efd6c2e.html` remain present.
