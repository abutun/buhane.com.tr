---
quick_task: 260814-igz
title: Portfolio SEO, useful content, and AI discovery improvements
status: planned
must_haves:
  truths:
    - "The final Turkish discovery report treats visible, people-first HTML, accurate canonical URLs, sitemaps, structured data, and product-specific content as the portfolio's search and answer-engine foundation; it does not represent llms.txt as a ranking or citation requirement."
    - "OAI-SearchBot is already permitted by each editable source's User-agent wildcard; GPTBot, ClaudeBot, and Google-Extended remain an explicit per-origin owner decision rather than an implicit deployment change."
    - "No mass llms.txt files, generic AI landing pages, hidden AI text, keyword stuffing, special AI schema, query-variant articles, or unsupported editorial claims are added."
    - "Hive Due / Site Hesap is the sole urgent live discovery repair: publish the existing one shared dist artifact and activate its existing host-qualified Nginx aliases; do not create a second build or rewrite the application."
    - "The report distinguishes no-new-source-deploy results from Phase 05 deployment-pending evidence, lists every registered property as deploy-now, no-new-deploy, or externally blocked, and never claims a local revision is live."
  artifacts:
    - path: "/Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr/.planning/quick/260814-igz-t-m-buhane-portf-y-nde-seo-faydal-i-erik/260814-igz-AI-SEARCH-DISCOVERY-RUNBOOK.md"
      provides: "Compact Turkish per-site search/AI discovery report and deploy handoff grounded in the registry, fresh source validation, and primary Google/OpenAI guidance."
  key_links:
    - from: "Each editable public robots.txt source"
      to: "OAI-SearchBot"
      via: "existing User-agent: * / Allow: / policy, verified without redundant bot-specific rules"
    - from: "Hive Due / Site Hesap discovery endpoints"
      to: "one shared apps/HiveDue/www/dist release artifact"
      via: "the exact robots-hivedue/sitehesap and sitemap-hivedue/sitehesap aliases in deployment/nginx-hivedue-sitehesap.conf.example"
    - from: "Post-deploy review"
      to: "Google Search Console, Bing Webmaster Tools, and privacy-safe aggregate AI referral evidence"
      via: "the existing 0/28/90-day measurement contract; no account mutation in this task"
---

# Quick Task Plan: Portfolio SEO, useful content, and AI discovery improvements

## Scope and safety boundary

Base every conclusion on `260814-igz-RESEARCH.md`, `.planning/portfolio-sites.json`, and the Phase 05 release and measurement records. The latest strict source audit has zero findings and the existing content hubs are already substantive, localized only where independently addressable, and constrained to released product facts. This task therefore has a **zero-public-source-change** default: it must not manufacture a change simply because an SEO/AI tactic exists.

Do not modify production, deployment infrastructure, Nginx, GeoIP, CDN/WAF, DNS, Search Console, Bing, analytics, IndexNow, crawler policy, or the externally blocked Cosmic Meta property. Preserve every unrelated dirty path named in the research. Do not add `llms.txt`, hidden copy, an AI-only page, special AI markup, generic blog posts, unverified store/product claims, mechanical dates, or a crawler allow/block rule for GPTBot, ClaudeBot, Google-Extended, or advertising crawlers. `User-agent: *` already allows OAI-SearchBot in the source; do not add a duplicate rule just to make that fact visible.

### Task 1 — Produce the evidence-based Turkish search and AI discovery runbook

**Files**

- Create: `/Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr/.planning/quick/260814-igz-t-m-buhane-portf-y-nde-seo-faydal-i-erik/260814-igz-AI-SEARCH-DISCOVERY-RUNBOOK.md`
- Read-only evidence: `/Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr/.planning/quick/260814-igz-t-m-buhane-portf-y-nde-seo-faydal-i-erik/260814-igz-RESEARCH.md`
- Read-only evidence: `/Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr/.planning/portfolio-sites.json`
- Read-only evidence: `/Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr/.planning/phases/05-portfolio-discovery-content-and-brand-network/{05-RELEASE-VALIDATION.md,05-RELEASE-STATUS.json,05-MEASUREMENT-BASELINE.md,05-EXTERNAL-BLOCKERS.md}`

**Action**

1. Write one compact Turkish report with a plain-language executive result: Google AI Overviews/AI Mode rely on normal Search eligibility and quality, while ChatGPT Search needs public OAI-SearchBot access. Link only to the primary guidance already captured in research: Google AI optimization guide, AI-features/crawler controls, technical requirements, Organization structured data, and OpenAI Publishers/Crawler documentation. State explicitly that `llms.txt`, special AI schema, forced chunking, and keyword-oriented query variants are not requirements or proven ranking/citation levers.
2. Add one row for every exact registry display name — Buhane Bilgi Teknolojileri, ahmet.sh, MoodJot, Vynix, Swipe Slip, Glow Spin, Hive Due / Site Hesap, Astral Post, Gridzle, Hoşkin, Lastimo, The Cosmic Meta, and U2M URL Shortener. For each row, record: current verified source/content surface, a factual safe maintenance criterion (released capability + real user question/query/support evidence + a meaningful next link + maintainable locale), this task's deployment classification, and any current external/live qualification. Do not describe account data as zero when it is merely `not_verified`.
3. Make deployment classification unambiguous and exhaustive:
   - **Acil deploy / canlı düzeltme:** only Hive Due / Site Hesap. State that its source already produces one shared `apps/HiveDue/www/dist/` artifact, which must be published once to the configured current release root. The operator must activate the existing exact aliases: `/robots.txt` → `robots-hivedue.txt` / `robots-sitehesap.txt`, and `/sitemap.xml` → `sitemap-hivedue.xml` / `sitemap-sitehesap.xml`; test Hive Due from a non-Türkiye egress and Site Hesap from Türkiye. This is deployment/configuration drift, not a code rewrite or second regional build.
   - **Bu task için yeni kaynak deploy'u yok:** the other eleven editable properties. Also state their Phase 05 source is still `deployment_pending` until the owner can prove a traceable deployed revision; name the previously committed/unpublished-source note for Buhane, Astral Post, and Gridzle without staging or publishing anything here.
   - **Harici erişim engeli:** The Cosmic Meta. Quote the exact established blocker: “No verified local source, repository, build, deploy pipeline, or WordPress administration path has been shown to own `https://thecosmicmeta.com/`.”
4. Include a short crawler-policy decision template per public origin. Its default must preserve current Search access, record OAI-SearchBot as already covered by wildcard access, and require the legal/product/privacy owner to separately select and date allow/block decisions for GPTBot, ClaudeBot, and Google-Extended. Explain that Google-Extended is distinct from Googlebot and does not switch normal Google Search/AI Overview eligibility. List required proof before any future robots change: decision owner/date, source and CDN/WAF agreement, raw deployed response, and rollback point.
5. Include a usable post-deploy checklist: validate final 200/content type/canonical/robots/sitemap responses, sample the declared canonical routes and structured data, then use the existing Day 0/28/90 measurement contract for verified Search Console and Bing properties, sitemap submission/read evidence, representative indexed pages, aggregate `utm_source=chatgpt.com` referrals where present, and the approved six-event/five-property privacy-safe schema. Do not access any account or log user/product data.

**Verify**

```bash
cd /Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr
test -s .planning/quick/260814-igz-t-m-buhane-portf-y-nde-seo-faydal-i-erik/260814-igz-AI-SEARCH-DISCOVERY-RUNBOOK.md
rg -n -F 'OAI-SearchBot' .planning/quick/260814-igz-t-m-buhane-portf-y-nde-seo-faydal-i-erik/260814-igz-AI-SEARCH-DISCOVERY-RUNBOOK.md
rg -n -F 'one shared' .planning/quick/260814-igz-t-m-buhane-portf-y-nde-seo-faydal-i-erik/260814-igz-AI-SEARCH-DISCOVERY-RUNBOOK.md
rg -n -F 'No verified local source, repository, build, deploy pipeline, or WordPress administration path has been shown to own `https://thecosmicmeta.com/`.' .planning/quick/260814-igz-t-m-buhane-portf-y-nde-seo-faydal-i-erik/260814-igz-AI-SEARCH-DISCOVERY-RUNBOOK.md
python3 - <<'PY'
import json
from pathlib import Path

report = Path('.planning/quick/260814-igz-t-m-buhane-portf-y-nde-seo-faydal-i-erik/260814-igz-AI-SEARCH-DISCOVERY-RUNBOOK.md').read_text()
manifest = json.loads(Path('.planning/portfolio-sites.json').read_text())
expected = [
    item['display_name']
    for section in ('properties', 'products')
    for item in manifest[section].values()
]
missing = [name for name in expected if name not in report]
forbidden = ('llms.txt oluşturuldu', 'özel AI şeması eklendi', 'gizli AI metni eklendi')
present_forbidden = [item for item in forbidden if item in report]
if missing or present_forbidden:
    raise SystemExit(f'missing={missing}; forbidden={present_forbidden}')
PY
```

**Done**

The portfolio has a precise, owner-safe Turkish discovery/deployment handoff that tells future maintainers what is already effective, what cannot be truthfully added, which real evidence justifies future content, how crawler policy must be decided, and exactly why Hive Due/Site Hesap is the only urgent live recovery.

### Task 2 — Reconfirm the source contract and record the no-code decision

**Files**

- Modify after verification only: `/Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr/.planning/quick/260814-igz-t-m-buhane-portf-y-nde-seo-faydal-i-erik/260814-igz-AI-SEARCH-DISCOVERY-RUNBOOK.md`
- Read-only validation input: `/Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr/.planning/portfolio-sites.json`
- Read-only source contract: `/Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue/{www/dist,deployment/nginx-hivedue-sitehesap.conf.example}`

**Action**

1. Re-run the registry and strict source validators plus their dependency-free unit suite. Record the exact command/result/date in the runbook. If any new source finding appears, record it faithfully; do not bypass the validator, broaden scope, or add speculative SEO content. Only plan a narrow source fix if the finding demonstrates a factual, user-visible, source-level defect and the repository's own generator/localization contract can be honored.
2. Inspect the existing source robots contracts without modifying them: establish that every editable source remains reachable through public wildcard rules and therefore does not block OAI-SearchBot at source. Confirm no source `llms.txt` is required for the stated Search/ChatGPT outcomes. Document that The Cosmic Meta's live stale `llms.txt` can only be corrected or removed inside verified WordPress/hosting ownership.
3. Verify the Hive handoff against the existing artifact and Nginx example: one `dist` root and the four backing discovery filenames must exist in the source artifact; the example must name exact `location = /robots.txt` and `location = /sitemap.xml` aliases for both hosts. Add no deployment command that changes production and do not create a new variant output.
4. Add a short “Bu çalışmada kaynak değişikliği yapılmadı” conclusion only after these checks pass. It must say this is intentional evidence-based restraint, not that every live deployment has been verified.

**Verify**

```bash
cd /Users/ahmet/Documents/Workspaces/Buhane/buhane.com.tr
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode registry
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode source --timeout 180 --report /tmp/260814-igz-source.json
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s scripts/tests -p 'test_*.py'
python3 - <<'PY'
from pathlib import Path

hive = Path('/Users/ahmet/Documents/Workspaces/Buhane/apps/HiveDue')
dist = hive / 'www' / 'dist'
expected_artifacts = {
    'robots-hivedue.txt', 'robots-sitehesap.txt',
    'sitemap-hivedue.xml', 'sitemap-sitehesap.xml',
}
missing = sorted(name for name in expected_artifacts if not (dist / name).is_file())
nginx = (hive / 'deployment' / 'nginx-hivedue-sitehesap.conf.example').read_text()
required = (
    'location = /robots.txt', 'location = /sitemap.xml',
    'robots-hivedue.txt', 'robots-sitehesap.txt',
    'sitemap-hivedue.xml', 'sitemap-sitehesap.xml',
)
missing_nginx = [token for token in required if token not in nginx]
if missing or missing_nginx:
    raise SystemExit(f'missing artifact(s)={missing}; missing nginx contract={missing_nginx}')
PY
```

**Done**

Fresh validation either preserves the documented zero-finding source result or exposes an explicitly evidenced new defect. In the expected zero-finding case, no public website source is altered, the runbook records why, and only the internal planning handoff is eligible for the quick-task commit.

## Completion rule

Commit only the new GSD plan/runbook/summary/STATE artifacts in the Buhane repository. Do not stage a sibling repository, generated distribution output, unrelated dirt, or any production configuration. The final user handoff must point to the Turkish runbook and give a compact table of the 13 registry properties, with an explicit “redeploy now / no new deploy / external blocker” column.
