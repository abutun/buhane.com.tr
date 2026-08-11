# Discovery, Crawler, and Measurement Contract

Search discovery, answer-engine citation, and customer acquisition share one foundation: useful visible HTML, stable canonical URLs, crawlable internal links, canonical-only sitemaps, accurate structured data, clear ownership, and current product facts. No special AI optimization layer replaces those fundamentals.

## Shared search and answer-engine foundation

Every indexable page should:

- answer a real product, use-case, support, or evaluation need in visible HTML;
- use one absolute HTTPS canonical on the registry's preferred origin;
- be reachable through useful internal links and included once in a canonical-only sitemap;
- use a page-specific title, description, primary heading, and social URL;
- describe the visible page with parseable, truthful structured data and stable entity IDs;
- identify the responsible organization or author and provide a clear next destination;
- maintain addressable, reciprocal localized URLs before publishing `hreflang`;
- omit admin, auth, recovery, dashboard, redirect-only, and `noindex` routes from sitemaps.

The portfolio must not add hidden AI keywords, special AI schema, query-fan-out doorway pages, fabricated reviews/ratings, generated update dates, or repeated reciprocal footer portfolios. `llms.txt` is optional and non-authoritative. It is not an indexing or ranking requirement and does not replace HTML, `robots.txt`, canonicals, or sitemaps. If a property keeps one, every URL and description must be accurate and reviewed like other public content.

## Crawler policy state

Search/citation access and model-training access are separate owner choices. `robots.txt`, CDN, WAF, and origin behavior must agree; a permissive robots rule does not help if infrastructure blocks the agent.

### Search/citation crawlers

The intended discovery/citation set is:

- `Googlebot` — Google Search crawling and indexing.
- `Bingbot` — Bing Search crawling and indexing.
- `OAI-SearchBot` — OpenAI search discovery and citations.
- `Claude-SearchBot` — Anthropic search discovery.
- `PerplexityBot` — Perplexity search/indexing.

Allowing these agents does not guarantee crawling, indexing, ranking, or citation. Validate their deployed response status and content independently. User-requested fetch agents should be assessed separately when the platform documents them.

### Training crawlers

Training and non-search use is not inferred from the desire to appear in search or citations. The decision state is:

```text
training_policy: owner_decision_required
```

The owner must explicitly allow or block, per property:

- `GPTBot` — OpenAI model-training crawler.
- `ClaudeBot` — Anthropic model-training crawler.
- `Google-Extended` — Google control for certain Gemini training/grounding uses; it is separate from ordinary Google Search inclusion.

Until that decision is recorded, do not publish portfolio-wide allow/block rules on the owner's behalf. Document the final choice, date, affected origins, CDN/WAF settings, and verification evidence.

## Ownership and cross-link policy

- Buhane is the authoritative company and portfolio hub at `https://buhane.com.tr/#organization`.
- Each editable product site exposes one natural, visible “product by/published by Buhane” link.
- Ahmet's personal site uses `https://ahmet.sh/#person` and states the founder relationship factually; it is not a second complete portfolio directory.
- Sibling product links appear only when a page explains a genuine task, comparison, or workflow and the relationship is in `approved_contextual_links`.
- A global footer must not repeat a list of sibling properties. Paid or sponsored relationships use the appropriate link attributes; ordinary factual ownership does not need `nofollow` solely because the company controls both sites.

## Privacy-safe event contract

The portfolio uses the same event names and property vocabulary across sites. Implement only events needed for a real product funnel.

| Event name | When it fires |
|---|---|
| `portfolio_product_click` | A visitor leaves Buhane or an approved contextual page for an official product destination |
| `store_click` | A visitor opens a verified App Store or Google Play destination |
| `support_click` | A visitor opens a verified support route or destination |
| `contact_start` | A visitor deliberately begins the contact path |
| `contact_submit` | A contact action completes; do not include message content |
| `signup_start` | A visitor begins a public product signup flow |

Only these properties are allowed:

| Property | Contract |
|---|---|
| `product_id` | Stable registry product ID, not a user-generated label |
| `source_site` | Stable property ID where the event occurred |
| `source_page_type` | Small controlled value such as `home`, `product_detail`, `guide`, `article`, or `glossary` |
| `destination_type` | Small controlled value such as `official_site`, `store`, `support`, `contact`, or `signup` |
| `locale` | Reviewed page locale code, not a browser fingerprint |

Do not send journal text, personal documents, shortened target URLs, invoices, auth identifiers, email addresses, contact-message bodies, mood entries, tracker values, uploaded media, IP-derived profiles, or any other product user content as event names, properties, paths, or report evidence. Do not place secrets or stable account identifiers in campaign parameters. A completed contact event records that a submission occurred, not what the visitor wrote.

## Evidence schedule

Code completion is not ranking or citation proof. Record a baseline and two follow-ups without assuming Search Console, Bing, analytics, or AI-reporting account access is already available.

For each property and review window (`day_0`, `day_28`, `day_90`), record:

```text
property_id
review_window
evidence_collected_at
collector
access_status
deployment_revision
preferred_origin
sitemap_submitted
sitemap_read_status
indexed_preferred_pages
excluded_or_duplicate_pages
canonical_selection_issues
search_impressions
search_clicks
search_queries_and_locales
bing_ai_cited_pages
bing_ai_citation_count
ai_referral_sessions
chatgpt_referral_sessions
portfolio_product_clicks
store_clicks
support_clicks
contact_starts
contact_submits
signup_starts
conversion_notes
open_actions
```

Use `access_status` values such as `available`, `not_configured`, `access_requested`, or `not_offered_for_account`. A missing account or product-specific report is an explicit follow-up state, never fabricated zero data.

At day 0:

1. Record deploy revision, preferred-origin response, canonical, robots, sitemap, and representative indexed-page status.
2. Capture current Search Console and Bing baselines where access exists.
3. Confirm first-party event names/properties in a test session without transmitting user content.
4. Record known AI referrals and citation-report availability without treating absence as failure.

At day 28 and day 90:

1. Compare discovery/indexing errors, canonical selection, impressions, clicks, queries, countries, and locales.
2. Review Bing AI cited pages/counts where the report is offered.
3. Review identifiable AI referral sessions, including ChatGPT referral attribution when present.
4. Compare portfolio, store, support, contact, and signup events with real conversions.
5. Audit stale claims, broken destinations, expired pricing, mismatched locale content, and thin taxonomy pages.
6. Record actions and owners; do not attribute changes to Phase 5 without a plausible time window and baseline.

## External follow-ups

The following require credentials, deployment ownership, DNS/CDN control, or the actual source and therefore remain documented until separately authorized:

- Google Search Console and Bing Webmaster Tools ownership verification and sitemap submission.
- IndexNow key and deployment integration.
- DNS, CDN, WAF, and permanent legacy-origin redirect changes.
- Analytics account/property changes and cross-domain configuration.
- Rich Results and rendered live-page inspection after deployment.
- The Cosmic Meta WordPress administration or real deploy source, its stale domain references, taxonomy review, and optional `llms.txt` correction/removal.

For every follow-up, distinguish `source_complete`, `deployed`, `live_verified`, and `external_blocked`. A local metadata change alone is not a completed discovery outcome.
