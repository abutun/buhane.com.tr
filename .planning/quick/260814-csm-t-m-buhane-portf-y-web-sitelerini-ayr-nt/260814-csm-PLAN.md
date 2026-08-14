---
quick_task: 260814-csm
title: Portfolio-wide website audit and verified improvements
status: planned
must_haves:
  truths:
    - "Every external AstralPost privacy-policy link that opens a new tab protects the opener with both noopener and noreferrer."
    - "Hive Due and Site Hesap no longer present unavailable mobile stores as navigable # links, while real web-app CTAs remain links."
    - "Hive Due and Site Hesap continue to use exactly one shared www/dist release root; public robots.txt and sitemap.xml are mapped to the correct host-qualified backing files by the operator-owned Nginx contract."
    - "A concise Turkish audit table records all known portfolio properties without claiming that a locally verified revision has been deployed."
    - "The Cosmic Meta remains explicitly marked externally blocked until its verified WordPress/deployment source is supplied."
  artifacts:
    - path: "/Users/ahmet/Documents/Workspaces/Buhane/apps/AstralPost/www/privacy/index.html"
      provides: "Safe rel attributes on all seven external privacy-policy links that use target=_blank."
    - path: "/Users/ahmet/Documents/Workspaces/Buhane/apps/AstralPost/www/scripts/verify-content-hub.mjs"
      provides: "A regression check for unsafe external target=_blank links on the static privacy page."
    - path: "/Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/www/src/components/AppStoreBadges.astro"
      provides: "Non-interactive, accurately labelled coming-soon mobile-store badges."
    - path: "/Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/www/src/components/Footer.astro"
      provides: "Non-interactive coming-soon store entries in the shared bilingual footer."
    - path: "/Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/www/DEPLOY.md"
      provides: "An operator-facing, source-safe recovery checklist for the one shared release root and exact per-host discovery-file mappings."
    - path: "/Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr/.planning/quick/260814-csm-t-m-buhane-portf-y-web-sitelerini-ayr-nt/260814-csm-AUDIT-REPORT.md"
      provides: "The final Turkish per-site audit report, with source, deployment, and external-access states kept distinct."
  key_links:
    - from: "AstralPost privacy page"
      to: "Firebase, OpenAI, RevenueCat, and Google privacy-policy URLs"
      via: "target=_blank with rel=noopener noreferrer"
    - from: "Hive Due and Site Hesap public discovery endpoints"
      to: "one /var/www/hivedue/www/current release root"
      via: "deployment/nginx-hivedue-sitehesap.conf.example host-qualified aliases"
    - from: "sitehesap.com/robots.txt and sitemap.xml"
      to: "robots-sitehesap.txt and sitemap-sitehesap.xml"
      via: "Site Hesap server block"
    - from: "hivedue.com/robots.txt and sitemap.xml"
      to: "robots-hivedue.txt and sitemap-hivedue.xml"
      via: "Hive Due server block"
---

# Quick Task Plan: Portfolio-wide website audit and verified improvements

## Scope and safety boundary

Implement only the two source defects established in `260814-csm-RESEARCH.md`, plus the audit/release documentation needed to make the Hive Due live mismatch actionable. Do not redesign passing sites, invent product claims or editorial content, alter production hosting/DNS/CDN/analytics/search accounts, or edit the externally blocked Cosmic Meta property. Before and after each repository-local task, record `git status --short --branch`; preserve all unrelated and ignored work, especially Vynix admin output and Gridzle's active `.gsd/` state. Do not use `git add -A` or stage generated `dist/` output.

### Task 1 — Secure AstralPost privacy-policy new-tab links and prevent regression

**Files**

- Modify: `/Users/ahmet/Documents/Workspaces/Buhane/apps/AstralPost/www/privacy/index.html`
- Modify: `/Users/ahmet/Documents/Workspaces/Buhane/apps/AstralPost/www/scripts/verify-content-hub.mjs`

**Action**

1. Add `rel="noopener noreferrer"` to each of the seven external policy links in the English and Turkish privacy content that already uses `target="_blank"` (Firebase, OpenAI, RevenueCat, and Google).
2. Extend the existing static content-hub verifier so it fails when an external `target="_blank"` link on `privacy/index.html` lacks both required rel tokens. Keep the page's privacy copy, canonical, schema, language scope, and non-editorial route model unchanged.
3. Do not regenerate or hand-edit the generated multilingual journal/glossary output; this privacy page is an intentional direct static source file.

**Verify**

```bash
cd /Users/ahmet/Documents/Workspaces/Buhane/apps/AstralPost/www
node scripts/verify-content-hub.mjs
node --input-type=module -e 'import { readFileSync } from "node:fs"; const html = readFileSync("privacy/index.html", "utf8"); const links = [...html.matchAll(/<a\b[^>]*\btarget="_blank"[^>]*>/g)].map(([tag]) => tag); const unsafe = links.filter((tag) => !/\brel="[^"]*\bnoopener\b[^"]*\bnoreferrer\b[^"]*"/.test(tag)); if (links.length !== 7 || unsafe.length) throw new Error(`expected 7 safe privacy new-tab links; found ${links.length}, unsafe ${unsafe.length}`);'
```

**Done**

All seven privacy-policy links preserve their destinations and new-tab behavior while safely isolating the opener, and the native verifier prevents a future unsafe rel regression.

### Task 2 — Make unavailable Hive Due / Site Hesap store surfaces honest and document the shared-root discovery recovery

**Files**

- Modify: `/Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/www/src/components/AppStoreBadges.astro`
- Modify: `/Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/www/src/components/Footer.astro`
- Modify: `/Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/www/src/lib/publicationContract.test.ts`
- Modify: `/Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/www/DEPLOY.md`
- Read-only deployment authority: `/Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/deployment/nginx-hivedue-sitehesap.conf.example`

**Action**

1. Replace the four mobile-store `href="#"` controls (two visual badges and two footer entries) with non-interactive semantic text/badge containers. Retain the existing local SVGs, localized provider names, and localized `Coming soon`/`Yakında` notice; keep the actual web-app CTA as the only navigable primary CTA. Do not add invented App Store or Google Play URLs.
2. Add a focused publication-contract regression assertion that the two shared components contain no `href="#"` placeholder and retain the visible localized coming-soon state, so both the English Hive Due and Turkish Site Hesap variants are covered from their shared source.
3. Correct and strengthen `www/DEPLOY.md` as an operator handoff: reference the repository-root authoritative Nginx example with the correct relative path, require both marketing server blocks to serve `/var/www/hivedue/www/current`, require `hivedue.com` `/` to redirect locally to `/en/`, and name the four exact discovery aliases. Include raw response checks that require text/plain for each host's robots endpoint and XML content for each host's sitemap endpoint. State that the server, GeoIP, symlink, DNS/CDN, and cache changes are a separate authorized operator action — no production mutation belongs in this task.
4. Keep `deployment/nginx-hivedue-sitehesap.conf.example` as the authoritative source contract unless a test exposes a source discrepancy. Its existing two `root /var/www/hivedue/www/current;` declarations and four aliases are the required model; never create `dist/hivedue`, `dist/sitehesap`, or host-specific release directories.

**Verify**

```bash
cd /Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/www
npm run check
npm test
npm run verify:regional-assets
node --input-type=module -e 'import { readFileSync } from "node:fs"; const files = ["src/components/AppStoreBadges.astro", "src/components/Footer.astro"]; const placeholders = files.filter((file) => readFileSync(file, "utf8").includes("href=\"#\"")); if (placeholders.length) throw new Error(`placeholder store links remain: ${placeholders.join(", ")}`);'
```

After an independently authorized deployment, the operator must run these read-only probes without following the first country-dependent redirect and retain their headers/body evidence in the release record:

```bash
curl -sS --max-redirs 0 -D - -o /dev/null https://hivedue.com/
curl -sS --max-redirs 0 -D - -o /dev/null https://sitehesap.com/
curl -fsSI https://hivedue.com/robots.txt | grep -i '^content-type: text/plain'
curl -fsSI https://sitehesap.com/robots.txt | grep -i '^content-type: text/plain'
curl -fsSI https://hivedue.com/sitemap.xml | grep -i '^content-type: application/xml'
curl -fsSI https://sitehesap.com/sitemap.xml | grep -i '^content-type: application/xml'
```

**Done**

Neither regional site navigates a visitor to a fragment for an unavailable store, the one shared static artifact remains the only publishable artifact, and the deployment handoff makes the host-specific discovery mapping testable without treating local source verification as a live deployment.

### Task 3 — Publish the audit record and re-run the central source contract

**Files**

- Create: `/Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr/.planning/quick/260814-csm-t-m-buhane-portf-y-web-sitelerini-ayr-nt/260814-csm-AUDIT-REPORT.md`
- Read-only evidence: `/Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr/.planning/portfolio-sites.json`
- Read-only evidence: `/Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr/.planning/phases/05-portfolio-discovery-content-and-brand-network/05-RELEASE-VALIDATION.md`
- Read-only evidence: `/Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr/.planning/phases/05-portfolio-discovery-content-and-brand-network/05-EXTERNAL-BLOCKERS.md`

**Action**

1. Create one compact Turkish report table whose first column is the exact `display_name` of every registry property: Buhane Bilgi Teknolojileri, ahmet.sh, MoodJot, Vynix, Swipe Slip, Glow Spin, Hive Due / Site Hesap, Astral Post, Gridzle, Hoşkin, Lastimo, The Cosmic Meta, and U2M URL Shortener. Do not use aliases or omit a registry name.
2. For each row, use exactly one permitted state and no other label: `Kaynak doğrulandı`, `Kaynak düzeltmesi yapıldı`, `Dağıtım doğrulaması bekliyor`, or `Harici erişim engeli`. The report must distinguish passing source from a deployed revision, call out the two applied source fixes, list the Site Hesap/Hive Due Nginx follow-up as operator-owned, and quote The Cosmic Meta's exact external-access blocker verbatim: “No verified local source, repository, build, deploy pipeline, or WordPress administration path has been shown to own `https://thecosmicmeta.com/`.”
3. Include a short audit method/source list, exact commands and results from this task, a concise changes summary, and a strict non-goals section. Do not claim a live deploy, a search-console update, or a Cosmic Meta implementation.

**Verify**

```bash
cd /Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr
python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode registry
python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode source --timeout 180 --report /tmp/260814-csm-source.json
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
rg -n -F 'The Cosmic Meta' .planning/quick/260814-csm-t-m-buhane-portf-y-web-sitelerini-ayr-nt/260814-csm-AUDIT-REPORT.md
rg -n -F 'Hive Due / Site Hesap' .planning/quick/260814-csm-t-m-buhane-portf-y-web-sitelerini-ayr-nt/260814-csm-AUDIT-REPORT.md
python3 - <<'PY'
import json
import re
from pathlib import Path

manifest = json.loads(Path(".planning/portfolio-sites.json").read_text())
report = Path(".planning/quick/260814-csm-t-m-buhane-portf-y-web-sitelerini-ayr-nt/260814-csm-AUDIT-REPORT.md").read_text()
expected = [
    item["display_name"]
    for section in ("properties", "products")
    for item in manifest[section].values()
]
allowed_states = {
    "Kaynak doğrulandı",
    "Kaynak düzeltmesi yapıldı",
    "Dağıtım doğrulaması bekliyor",
    "Harici erişim engeli",
}
rows = []
for line in report.splitlines():
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    if len(cells) >= 2 and cells[0] in expected:
        rows.append((cells[0], cells[1]))
row_names = [name for name, _ in rows]
missing = [name for name in expected if row_names.count(name) != 1]
unexpected = [name for name in row_names if name not in expected]
invalid_states = [(name, state) for name, state in rows if state not in allowed_states]
if missing or unexpected or invalid_states or len(rows) != len(expected):
    raise SystemExit(
        f"invalid audit table: missing/duplicate={missing}, unexpected={unexpected}, invalid states={invalid_states}"
    )
blocker = "No verified local source, repository, build, deploy pipeline, or WordPress administration path has been shown to own `https://thecosmicmeta.com/`."
if blocker not in report:
    raise SystemExit("The Cosmic Meta exact external-access blocker is missing or altered")
forbidden_local_deploy_claims = (
    r"(?is)\b(?:yerel\s+)?(?:kaynak|source)\s+(?:revizyon|revision).{0,120}\b(?:deployed|published|live|dağıtıldı|yayınlandı|canlı(?:ya)?\s+alındı)\b",
    r"(?is)\b(?:deployed|published|live|dağıtıldı|yayınlandı|canlı(?:ya)?\s+alındı)\b.{0,120}\b(?:yerel\s+)?(?:kaynak|source)\s+(?:revizyon|revision)\b",
)
if any(re.search(pattern, report) for pattern in forbidden_local_deploy_claims):
    raise SystemExit("audit report falsely claims a local source revision is deployed")
PY
```

**Done**

The audited portfolio has one evidence-backed Turkish handoff document, every known site is represented, source and deployment state are never conflated, and the central registry/unit/source checks pass without absorbing unrelated worktree changes.
