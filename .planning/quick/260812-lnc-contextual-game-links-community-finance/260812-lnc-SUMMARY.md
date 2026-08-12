---
quick_id: 260812-lnc
status: complete
completed: 2026-08-12
commits:
  buhane: 395788f
  gridzle: 555640b
  hoskin: b6528f8
  u2m: 0db49e8
---

# Contextual game links and Community Finance content

## Result

- Gridzle now introduces Hoşkin, Glow Spin and Swipe Slip in a contextual "More games from Buhane" section. Its public footer includes a direct link to Buhane.
- Hoşkin's content generator now produces localized Gridzle, Glow Spin and Swipe Slip footer links for all five public locales. Its existing localized Buhane attribution remains a footer link and is now verified there.
- U2M's public footer renders Stats as a working internal `/stats` RouterLink and gives every footer link a pointer cursor. The repair also fixes the lost dynamic RouterLink `to` prop, so Home and Stats no longer render as inert anchors.
- Buhane's EN/TR Hive Due / Site Hesap product details, product-index cards and home cards now describe the reviewed Community Finance Management context: community dues and shared expenses, manager/resident visibility, m² calculations, bulk import, advance balances, announcements, documents and reports. The public text retains the explicit boundary that this is not payment processing, banking execution or a guaranteed financial outcome.
- The private portfolio registry was updated only with those reviewed capabilities, matching direct evidence in Hive Due's owned public source.

## Commits

| Repository | Source commit | Supporting GSD commit |
|---|---|---|
| Buhane.com.tr | `395788f` — `feat(site): explain Hive Due community finance management` | this quick-task documentation commit |
| Gridzle | `555640b` — `feat(www): link Gridzle to Buhane game network` | `42e05c8` |
| Hoşkin | `b6528f8` — `feat(www): link Hoşkin to Buhane game network` | `ef056c1` |
| U2M | `0db49e8` — `fix(frontend): restore footer stats link behavior` | not needed; worktree clean |

## Verification

- Buhane registry validation: zero findings.
- Buhane source validation: zero findings.
- Buhane validator unit suite: 53/53 passed.
- Buhane EN/TR Hive Due JSON-LD parsed successfully; all touched static pages parsed with no duplicate IDs; `git diff --check` passed.
- Gridzle foundation and hosting validators passed, including footer-link coverage.
- Hoşkin generator build produced 80 indexable pages and five feeds; native validator passed for 80 pages, 10 × 5 articles, 40 glossary entries and 80 sitemap URLs. Post-build `git diff --exit-code -- www` passed.
- U2M focused Vitest: 8/8 passed; production frontend build passed; Playwright layout suite: 9/9 passed, including Stats target and computed pointer cursor across routes and breakpoints.

## Preservation and release boundary

- No repository was pushed or deployed.
- Gridzle's pre-existing `androidApp/src/debug/res/values/admob.xml`, `iosApp/iosApp/Info.plist` and `.gsd/` changes remain unstaged and untouched.
- No additional dirty paths remain in the Buhane, Hoşkin or U2M repositories.
