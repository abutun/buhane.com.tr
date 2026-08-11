# Phase 05 Privacy-Safe Measurement Baseline

**Baseline date:** 2026-08-11

**Evidence state:** local source validation is complete; production deployment revisions and credentialed search/analytics data were not supplied

**Account access state:** `not_verified` means no credentialed evidence was available to this plan. It is not a zero, an absent account, or a failed metric.

This baseline implements `docs/portfolio/DISCOVERY_AND_MEASUREMENT.md`. Day 0 records only evidence actually available. Day 28 and day 90 remain owner collection checkpoints; blank account-gated data must never be replaced with fabricated zeroes.

## Per-host 0/28/90-day register

Every review cell inherits the full field contract in the next section: Google Search Console/Bing verification; sitemap submission/read state; indexed canonical samples and exclusions; canonical-selection issues; supported structured-data reports; impressions, clicks, queries, country and locale; Bing AI citations; identifiable AI/ChatGPT referrals; portfolio/store/support/contact/signup events; real conversions; notes and open actions.

| Property ID | Preferred host | Day 0 — 2026-08-11 | Day 28 — due 2026-09-08 | Day 90 — due 2026-11-09 |
|---|---|---|---|---|
| `buhane` | `buhane.com.tr` | Local revision `3227c47`; `deployment_pending`. Search/Bing/analytics access `not_verified`; account metrics not collected. Raw live evidence belongs to `/tmp/buhane-05-14-live.json`. | Not due; owner collects all discovery, citation, referral, event, and conversion fields after deployment. | Not due; owner repeats all fields and records trend/action decisions. |
| `moodjot` | `moodjot.app` | Source complete; deployed revision not proven. Search/Bing/analytics access `not_verified`; all account metrics not collected, not zero. | Not due; collect after verified deployment. | Not due; repeat and compare. |
| `vynix` | `vynix.app` | Source complete; deployed revision not proven. Search/Bing/analytics access `not_verified`; all account metrics not collected, not zero. | Not due; collect after verified deployment. | Not due; repeat and compare. |
| `swipe-slip` | `swipeslip.app` | Source complete; deployed revision not proven. Search/Bing/analytics access `not_verified`; all account metrics not collected, not zero. | Not due; collect after verified deployment. | Not due; repeat and compare. |
| `glow-spin` | `glowspin.app` | Source complete; deployed revision not proven. Search/Bing/analytics access `not_verified`; all account metrics not collected, not zero. | Not due; collect after verified deployment. | Not due; repeat and compare. |
| `hive-due` | `hivedue.com` and regional `sitehesap.com` | Both source artifacts complete; neither deployed revision proven. Search/Bing/analytics access `not_verified`; collect per host without splitting the one product ID. | Not due; collect per host after verified deployment and retain one `hive-due` product ID. | Not due; repeat per host and compare. |
| `astral-post` | `astralpost.app` | Source complete; deployed revision not proven. Search/Bing/analytics access `not_verified`; all account metrics not collected, not zero. | Not due; collect after verified deployment. | Not due; repeat and compare. |
| `gridzle` | `gridzle.app` | Source complete; deployed revision not proven. Search/Bing/analytics access `not_verified`; all account metrics not collected, not zero. | Not due; collect after verified deployment. | Not due; repeat and compare. |
| `hoskin` | `hoskin.app` | Source complete; deployed revision not proven. Search/Bing/analytics access `not_verified`; country/locale reporting must retain TR/EN/DE/FR/AR aggregation safeguards. | Not due; collect after verified deployment. | Not due; repeat and compare. |
| `lastimo` | `lastimo.app` | Source complete; deployed revision not proven. Search/Bing/analytics access `not_verified`; locale reporting must use the reviewed 12-locale vocabulary. | Not due; collect after verified deployment. | Not due; repeat and compare. |
| `the-cosmic-meta` | `thecosmicmeta.com` | `externally_blocked`; WordPress/deploy revision and account ownership unavailable. Read-only public evidence only; no account metrics collected. | Blocked until exact access package and verified deployment are supplied. | Repeat only after the blocker is cleared; never backfill guesses. |
| `u2m` | `u2m.io` | Source complete; deployed revision not proven. Search/Bing/analytics access `not_verified`; shortened destination URLs are explicitly forbidden measurement data. | Not due; collect after verified deployment. | Not due; repeat and compare. |
| `ahmet-sh` | `ahmet.sh` | Source complete; deployed revision not proven. Search/Bing/analytics access `not_verified`; all account metrics not collected, not zero. | Not due; collect after verified deployment. | Not due; repeat and compare. |

## Review-window field contract

Use one record per property and review window. For Hive Due, attach a host dimension limited to `hivedue.com` or `sitehesap.com` while retaining `product_id: hive-due`.

| Field group | Day 0 | Day 28 | Day 90 |
|---|---|---|---|
| Record identity | `property_id`, `review_window: day_0`, `evidence_collected_at`, named `collector`, `access_status`, local source revision, proven deployed revision or `not_proven`, preferred origin | Same fields with `day_28` and the revision actually live | Same fields with `day_90` and the revision actually live |
| Search ownership | Google Search Console verification state; Bing Webmaster verification state; responsible owner | Recheck access/ownership changes | Recheck access/ownership changes |
| Sitemap discovery | Submitted URL and submission time where authorized; read/fetch status; last read; discovered/indexed count where offered | Compare fetch/read/error state | Compare fetch/read/error state |
| Indexed canonicals | Representative canonical sample URLs; indexed preferred pages; excluded/duplicate pages; canonical-selection issues | Reinspect the same sample plus newly material routes | Reinspect and record resolved/new exclusions |
| Structured data | Supported Google/Bing structured-data or rich-result report types, valid/invalid counts, representative URL and evidence time | Compare errors/warnings without treating eligibility as ranking proof | Compare and assign fixes for regressions |
| Search demand | Impressions, clicks, CTR where offered, reviewed query groups, country, and locale; never export identifiers | Compare to day 0 with a plausible time window | Compare to day 0/day 28 and record seasonality/claim changes |
| AI citation | Bing AI cited pages and citation count where the account offers it; availability state when it does not | Compare cited canonical pages and source accuracy | Compare and audit stale/thin cited pages |
| Referrals | Identifiable aggregate AI referral sessions, including ChatGPT referrals when present; source/medium rules documented | Compare aggregate sessions and landing pages | Compare and audit attribution drift |
| Portfolio CTA | Counts for the six approved event names only, segmented only by the five approved properties | Compare funnel steps and broken destinations | Compare, then retain or remove events based on usefulness |
| Real conversion | Completed contact/signup outcomes available in the responsible system, aggregate count only; conversion notes | Compare events to real outcomes without copying user data | Compare and record product-owner actions |
| Actions | Open deployment, indexing, crawler, redirect, claim, taxonomy, analytics, or access action; owner and due date | Close or reassign each action with evidence | Close, reassign, or carry forward with rationale |

## Approved analytics contract

Exactly these six event names are approved:

1. `portfolio_product_click`
2. `store_click`
3. `support_click`
4. `contact_start`
5. `contact_submit`
6. `signup_start`

Exactly these five event properties are approved:

1. `product_id` — stable registry product ID, never a user-generated label.
2. `source_site` — stable registry property ID.
3. `source_page_type` — controlled `home`, `product_detail`, `guide`, `article`, or `glossary` vocabulary.
4. `destination_type` — controlled `official_site`, `store`, `support`, `contact`, or `signup` vocabulary.
5. `locale` — reviewed page locale, never fingerprint-derived.

Event implementation or analytics-account changes were not authorized by this plan. A test session may be recorded only after consent/configuration ownership is established and payload inspection proves that only this allowlist is transmitted.

## Forbidden data

Never place any of the following in event names, properties, paths, campaign parameters, exports, screenshots, reports, validator evidence, or this baseline:

- journal text, mood entries, tracker values, or personal notes;
- personal documents, uploaded media, filenames, or document contents;
- shortened target URLs, expanded target URLs, redirect histories, or U2M user links;
- invoices, balances, building/site records, payment records, or Hive Due resident data;
- email addresses, auth identifiers, account IDs, tokens, cookies, contact-message bodies, or signup form contents;
- IP-derived profiles, device/browser fingerprints, stable advertising identifiers, or other user content.

`contact_submit` records only that a submission completed. It never records what the visitor wrote.

## Owner-gated follow-ups

| Follow-up | Owner | Current state | Completion evidence required |
|---|---|---|---|
| Deploy each reviewed source revision to only its registered host/output | Product publication owner | `owner_decision_required`; unperformed | Traceable deploy revision, allowlisted artifact inventory, rollback point, raw final response |
| Verify Google Search Console and submit/read the canonical sitemap | Search property owner | Account access `not_verified`; unperformed | Verified property, sitemap URL, submission/read timestamps, canonical sample |
| Verify Bing Webmaster Tools and submit/read the canonical sitemap | Search property owner | Account access `not_verified`; unperformed | Verified property, sitemap URL, submission/read timestamps |
| Add optional IndexNow support | Product/search owner | Optional `owner_decision_required`; unperformed | Reviewed key ownership, same-host key file, submitted canonical URL log without secrets |
| Configure first-party analytics and cross-domain rules | Analytics/privacy owner | `owner_decision_required`; unperformed | Consent decision, six-event/five-property payload audit, retention/access policy |
| Set training-crawler policy for GPTBot, ClaudeBot, and Google-Extended | Legal/product/privacy owner | `owner_decision_required`; unperformed | Per-origin allow/block decision, date, robots/CDN/WAF agreement, raw verification |
| Validate search/citation agents after deploy | Infrastructure/search owner | Pending deployment | Googlebot, Bingbot, OAI-SearchBot, Claude-SearchBot, and PerplexityBot raw 200 evidence |
| Change DNS/CDN/WAF or permanent legacy redirects | Infrastructure owner | Not authorized; unperformed | Approved change, one-hop redirect evidence, cache/TLS checks, rollback plan |
| Clear The Cosmic Meta blocker | WordPress/infrastructure owner | `external_blocked` | Full access package in `05-EXTERNAL-BLOCKERS.md`, scoped implementation, deployment, live recheck |

No Search Console, Bing, IndexNow, analytics, deployment, DNS, CDN, WAF, or account action was performed while creating this baseline.
