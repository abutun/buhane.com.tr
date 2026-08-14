---
quick_task: 260814-igz
title: Portfolio SEO, useful content, and AI discovery improvements
status: complete
completed_at: 2026-08-14
source_change: none
---

# Quick Task Summary: Portfolio SEO, useful content, and AI discovery improvements

## Result

Created the evidence-based Turkish AI/search discovery runbook at:

`.planning/quick/260814-igz-t-m-buhane-portf-y-nde-seo-faydal-i-erik/260814-igz-AI-SEARCH-DISCOVERY-RUNBOOK.md`

The runbook covers all 13 registry properties, cites only the specified primary Google/OpenAI guidance, separates normal Search/ChatGPT Search access from model-training policy, records factual content-maintenance criteria, and gives Day 0/28/90 verification steps. It intentionally rejects mass `llms.txt`, special AI markup, hidden AI copy, generic keyword pages, and speculative content claims.

## Fresh evidence — 2026-08-14

- Registry validator: `PASS [registry] no findings`; exit `0`.
- Strict source validator: `PASS [source] no findings`; high/medium/low/info `0/0/0/0`; exit `0`.
- Dependency-free suite: `55` tests, `OK`; exit `0`. Its two visible `GEN.COMMAND_TIMEOUT` lines are expected synthetic timeout-fixture output asserted by the passing suite, not source findings.
- Crawler-source inspection: all 12 editable publications retain wildcard `User-agent: *` / `Allow: /`, so `OAI-SearchBot` is not source-blocked.
- `llms.txt` source inventory: none at the 12 editable public source/output roots; no such file is required for the stated Google or ChatGPT goals.
- Hive artifact/Nginx contract: `PASS [hive-artifact-nginx] one dist root, four discovery files, and both host aliases present`.

## Source-change decision

**Bu çalışmada kaynak değişikliği yapılmadı.** This is intentional evidence-based restraint: the source contracts and existing content hubs already passed strict validation. It does not claim that every local revision has been deployed or that all account/live verification is complete.

## Redeploy decision

| Classification | Properties | Exact next action |
|---|---|---|
| **Redeploy / live repair now** | Hive Due / Site Hesap | Publish the existing one shared `apps/HiveDue/www/dist/` artifact once and activate the documented host-specific `/robots.txt` and `/sitemap.xml` Nginx aliases. Verify Hive Due from a non-Türkiye egress and Site Hesap from a Türkiye egress. |
| **No new deploy from this task** | Buhane Bilgi Teknolojileri, ahmet.sh, MoodJot, Vynix, Swipe Slip, Glow Spin, Astral Post, Gridzle, Hoşkin, Lastimo, U2M URL Shortener | No public source changed in this task. Their Phase 05 status remains `deployment_pending` until the publication owner can associate a reviewed local revision with raw post-deploy evidence; this is separate from this task's deploy decision. |
| **External blocker** | The Cosmic Meta | No verified local source, repository, build, deploy pipeline, or WordPress administration path has been shown to own `https://thecosmicmeta.com/`. Obtain the documented WordPress/hosting access package before changing its stale live discovery output. |

## Repository safety

No public website source, generated output, Nginx/deployment configuration, crawler policy, account, DNS/CDN/WAF setting, or sibling repository was modified. No commit was created by this executor.
