# Buhane.com.tr Design System

Hallmark source of truth for the 2026 redesign.

## Position

Buhane is an independent product foundry. The site must not read as a generic software agency, a client-services landing page, or a SaaS template. Its primary evidence is the portfolio itself: multiple real products, each with its own identity, connected through one disciplined company system.

## Audience

Prospective partners, product visitors, search visitors, and people evaluating Buhane as a technically credible product company.

## Macrostructure

Home: Map / Diagram. The product network is the hero surface, with varied product nodes, category relationships, and direct routes to each product.

Product index: Ecosystem Index. The index organizes the portfolio by product identity and job, not by identical cards alone.

Product detail pages: Long Document. Each detail route presents purpose, capabilities, operating boundaries, facts, FAQ, and a verified next step.

## Genre And Theme

Genre: modern-minimal with editorial product-foundry discipline.

Theme: warm paper, strong ink, fine rules, modular grid, and a restrained Buhane signal orange. Buhane's system stays neutral so product logos and product colors can enter locally without repainting the whole company site.

## Navigation And Footer

Navigation: N11 Mega-menu. The primary product route opens a grouped product network menu with Apps, Games, and Platforms / Publications.

Footer: Ft5 Statement. The footer behaves as a company statement and compact route index, not a generic four-column marketing footer.

## Typography

Display: Space Grotesk, used for page titles and statement-scale text.

Body: IBM Plex Sans, used for prose, navigation, controls, and cards.

Mono: JetBrains Mono, used sparingly for numerals, labels, product counts, and system tags.

No heading italics. No gradient text. Letter spacing stays at zero except small-caps mono labels where a tiny positive value is used deliberately.

## Color Tokens

All implementation colors are consumed through `tokens.css`. Neutral colors carry a warm chroma. Product colors are also tokenized so product identity can appear in cards and map nodes without mid-render improvisation.

```css
:root {
  --color-paper: oklch(97% 0.012 76);
  --color-paper-2: oklch(94% 0.014 76);
  --color-paper-3: oklch(90% 0.016 76);
  --color-ink: oklch(17% 0.01 70);
  --color-accent: oklch(63% 0.22 35);
}
```

## Spacing

Spacing follows a 4 px scale from `--space-3xs` to `--space-5xl`. Large sections use full-width bands and rules. Cards are used for product nodes, repeated product records, factual panels, and contact modules only.

## Motion

Motion is limited to purposeful product discovery:

- product menu open / close
- CTA press and hover feedback
- product filter changes
- one-shot stat number reveal

Reduced motion collapses transitions and skips number animation.

## Product Identity

Apps, Games, SaaS, and Publications are visually distinct through product-level color tokens, compact type labels, and node/card rhythm. Product logos remain local assets under `images/products/` where available.

## Page Rules

The home page makes the product network the first-viewport signal.

Index pages should feel like a cataloged ecosystem, with enough identity to scan quickly.

Detail pages should feel factual, quiet, and specific: no fabricated proof metrics, no testimonials, no fake screenshots, no fake browser or device chrome.
