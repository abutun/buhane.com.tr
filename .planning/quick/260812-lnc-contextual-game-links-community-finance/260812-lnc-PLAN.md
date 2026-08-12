---
quick_id: 260812-lnc
description: Add contextual game links, a U2M footer pointer cursor, and bilingual Community Finance Management context for Hive Due / Site Hesap.
created: 2026-08-12
status: in_progress
---

# Contextual game links and Community Finance content

## Intended outcome

- Gridzle and Hoşkin visibly offer a small, relevant route to Buhane's other games and identify Buhane in their footers, using their owned source/generator paths.
- The U2M public footer's Stats destination exposes link affordance (`cursor: pointer`) without changing navigation behaviour.
- Buhane's English and Turkish Hive Due / Site Hesap detail pages describe the verified community-finance-management use case, regional destinations, roles, workflows, and boundaries accurately.

## Execution plan

1. Update Gridzle and Hoşkin web source through their native publication/generator contracts; retain existing user dirt, validate, and commit each repository atomically.
2. Fix the U2M public footer link affordance at the source level, test its frontend contract, and commit atomically.
3. Update Buhane's EN/TR Hive Due / Site Hesap product details and index/home summaries together. Align the private registry's reviewed product context only with capabilities directly evidenced by the owned Hive Due public source. Run static and central portfolio checks, then commit source changes.
4. Record final evidence in this quick task's SUMMARY and update the root STATE quick-task table without pushing or deploying any repository.

## Boundaries

- No deployment, DNS, CDN, analytics, or external account change.
- No hand-editing generator-owned game outputs.
- Do not alter pre-existing Gridzle mobile/config dirt or unrelated workspace modifications.
- Describe payment recording/tracking as product workflow only; do not claim payment processing, banking execution, or guaranteed financial outcomes.
