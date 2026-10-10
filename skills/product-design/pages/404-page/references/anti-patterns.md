# Anti-Patterns — 404 Page

> Source: 45 unique products (32 well-known, 13 studio/niche) + lessons from Landing Page / Pricing Page / Contact Page / Section Skills practice. Every rule validated against `shared/visual-style.md`.

---

## 1. Visual Errors

### 1.1 Illustration or Stock Photo as the Visual

**Problem**: The 404 page uses a cartoon illustration, stock photo, or abstract graphic as its main visual element.
**Why it's wrong**: The design system's fourth principle is "Content as decoration" — product screenshots/output serve as visuals; reject illustrations, abstract gradients, stock photos (`shared/visual-style.md` Design Philosophy, item 4). Observation data: 39/45 pages carry the visual without illustration. Only 4/45 use a substantial illustration (Fauna, Shopify Editions, Deezer, Aave). The system's alternatives — typographic numeral, oversized heading, product-referential visual, or nothing — are better aligned.
**Correct approach**: Use one of the within-system visual strategies:
1. **Typographic numeral** (9/45): "404" at display scale, `var(--font-display)`, weight 500
2. **Oversized heading** (2/45): heading text at >= 90px
3. **Product-referential visual**: reuse the product's own UI/output (requires user input)
4. **Nothing** (9/45): plain typography + whitespace
**Checklist item**: Is the visual element illustration-free?

---

### 1.2 Pill-Shaped Button

**Problem**: The CTA button uses `border-radius: 999px` or any fully rounded shape.
**Why it's wrong**: The system button radius is `2px` (`shared/visual-style.md` section 4: "Button: 2px (sharp, authoritative)"). Although 14/25 observed 404 pages with buttons use pills, the system choice is **consistency across all page types** — 404 is not an exception to the design system. The reasoning is system consistency, not "pills look AI-generated."
**Correct approach**: `border-radius: 2px`. Button reuses `.btn-dark` verbatim: `padding: 8px 16px; font-size: 14px; font-weight: 500; font-family: var(--font-display); background: var(--accent); color: var(--accent-text); border: none; border-radius: 2px`.
**Checklist item**: Is the button border-radius 2px?

---

### 1.3 Box-Shadow on Any Element

**Problem**: Any element on the 404 page uses `box-shadow` — buttons, cards, the content container, input fields.
**Why it's wrong**: The system uses zero shadows (`shared/visual-style.md` section 5: "No element on the entire site uses box-shadow"). Hierarchy is established through background color steps (`var(--bg)` / `var(--surface-1)` / `var(--surface-2)`) and borders (`1px solid` surface-2 value).
**Correct approach**: Remove all `box-shadow` declarations. For focus states, use `outline: 2px solid var(--text); outline-offset: 2px` (outline is not shadow).
**Checklist item**: Does any element use box-shadow? If yes, remove it.

---

### 1.4 Colored Background

**Problem**: The 404 page uses a colored background — brand color fill, gradient, photographic background, or a tinted gray.
**Why it's wrong**: The system defines only achromatic backgrounds (`shared/visual-style.md` section 8: "Not allowed: colored backgrounds, gradient backgrounds"). Page background must be `var(--bg)` (#FFFFFF light / #0A0A0A dark). Evidence: Monte uses a full terracotta background — explicitly outside our system. All neutral colors must be pure achromatic (zero hue shift, `shared/visual-style.md` section 1: "no warm gray, cool gray, or blue-gray").
**Correct approach**: Background is `var(--bg)`. If a card or container needs visual separation, use `var(--surface-1)` (#F5F5F5 light / #141414 dark).
**Checklist item**: Is the page background `var(--bg)` with zero hue?

---

### 1.5 Multiple Font Weights for Emphasis

**Problem**: The 404 page uses bold/regular switching within the same text role — e.g., heading at weight 700, body at weight 400, then a bold inline word at weight 700.
**Why it's wrong**: The system locks weight at 500 (display) and 400 (mono/body) (`shared/visual-style.md` section 2: "Weight is locked at 500 (display) and 400 (mono/body) — do not use regular/bold within the same role for emphasis"). Hierarchy comes from font family switching and size, not weight variation.
**Correct approach**: Display text (headings, buttons, nav) uses weight 500. Mono text (labels, metadata) uses weight 400. Body text uses weight 400. No weight 600 or 700.
**Checklist item**: Are all weights either 500 (display) or 400 (mono/body)?

---

### 1.6 Decorative Border on Content Container

**Problem**: The error content container has `border-top: 3px solid var(--accent)`, a colored left border, or any decorative border treatment.
**Why it's wrong**: Based on Landing Page and Contact Page Skill practice, decorative borders are a high-frequency feature of AI-generated interfaces. Real product 404 pages do not use decorative borders on the content block — the block's visual hierarchy comes from its position (centered) and its typography, not from a color strip. Same pattern as Contact anti-pattern 1.4.
**Correct approach**: Content container has no decorative borders. If a visual wrapper is needed, use `background: var(--surface-1); border-radius: 8px; padding: 32px` (system `.card` token from `shared/visual-style.md` section 8).
**Checklist item**: Does the content container have a decorative border? If yes, delete it.

---

### 1.7 Colorful Numeral or Gradient Fill

**Problem**: The "404" numeral uses a chromatic color (mint green, brand color) or a gradient fill.
**Why it's wrong**: The system uses `var(--text)` + opacity for all text hierarchy (`shared/visual-style.md` section 1: "chromatic color only for narrow semantic signals, occupying <10% of visible page area"). A giant numeral occupies far more than 10% of visible area — coloring it violates color silence. Evidence: Greptile uses mint green, Butter has a multicolor glow — both are counterexamples to the system.
**Correct approach**: Numeral uses `color: var(--text)`. For a display-scale numeral alongside a heading, reduce opacity to 0.10-0.15 so it does not compete with the heading. For a standalone numeral (no heading), full opacity is acceptable.
**Checklist item**: Is the numeral color `var(--text)` with no chromatic fill?

---

## 2. Content Errors

### 2.1 Fabricated Humor

**Problem**: The 404 copy includes forced puns, jokes, or pop-culture references that do not relate to the product's domain.
**Why it's wrong**: Humor works when it references the product's core competence — "Pages are kind of our thing" (Craft, a document tool), "flawless navigation is kind of our thing" (Zoox, an autonomous vehicle company), "We haven't ghosted you!" (Phantom, whose brand identity uses a ghost). Without a domain anchor, humor degrades into generic puns ("Looks like you took a wrong turn!") that weaken professional tone. Evidence: 22/34 headings use literal tone; humor appears in only 6/34.
**Correct approach**: Default to literal tone ("Page not found" / "This page could not be found"). If the product has a natural domain reference, one product-referential line is acceptable in the body (not the heading). If no obvious angle exists, stay literal — forced puns are worse than plain copy.
**Checklist item**: If humor is used, does it reference the product's domain? If not, replace with literal copy.

---

### 2.2 Giant Numeral at Full Opacity Competing with a Heading

**Problem**: A display-sized "404" numeral (>= 100px) and a text heading both appear at full opacity, creating two competing focal points.
**Why it's wrong**: When both elements are at full contrast, the user's eye bounces between them with no clear hierarchy. Evidence: SpaceXAI uses a numeral at ~0.11 opacity (approximately #E5E5E5 on white), Biograph at ~0.10-0.15 on dark, Parker at ~0.06 — all demote the numeral to near-background contrast when a heading is also present.
**Correct approach**: If both numeral and heading exist, choose one hierarchy:
- **Numeral as texture**: opacity 0.10-0.15 (system logo-wall tier from `shared/visual-style.md` section 1), heading at full opacity
- **Numeral as heading**: numeral at full opacity, no separate text heading (Vercel, Butter, Slash pattern — the numeral replaces the heading)
**Checklist item**: If numeral and heading coexist, is the numeral at reduced opacity (0.10-0.15)?

---

### 2.3 Fabricated Error Details

**Problem**: The 404 page displays fabricated request paths, server names, stack traces, or technical error metadata (e.g., "GET /api/v2/users/undefined returned 404", "Server: nginx/1.22.1").
**Why it's wrong**: Fabricated technical details look plausible but are fiction. If deployed, they may confuse developers debugging real issues. The "developer flavor" in real products is expressed through small typographic signals — an HTTP status-line heading (Resend: "404: Not Found"), a mono label (Instrument: "ERROR CODE: 404"), or scrambled mono characters (Firecrawl) — not through fake server output.
**Correct approach**: For a developer-styled variant, use the mono/status-line format: "404: Not Found" set in `var(--font-mono)`, styled like the system `.label` or at a larger mono size. No fabricated paths, headers, or traces.
**Checklist item**: Does the page show any fabricated technical details? If yes, remove them.

---

## 3. Structural Errors

### 3.1 Removing the Navigation

**Problem**: The 404 page removes or hides the site navigation, leaving only the error content and a single "Go home" button.
**Why it's wrong**: The nav is the user's primary escape mechanism. A 404 with no nav and one button creates a funnel where the only option is the homepage — but the user may have been looking for docs, pricing, or support. Evidence: 13/17 samples where nav is observable keep the full site nav. 0/17 remove nav entirely.
**Correct approach**: Keep the site's standard navigation. Reuse `shared/navigation.md` without modification. The nav provides multiple exit paths; the in-page CTA button provides the default one.
**Checklist item**: Is the full site navigation present?

---

### 3.2 Using 160px Pill Radius for Search Input

**Problem**: The search input on a 404 page uses `border-radius: 160px` (the system search-bar pill token).
**Why it's wrong**: The system's 160px pill radius is defined for the Support Hub search bar (`shared/visual-style.md` section 4: "Search bar: 160px (pill shape)"). However, all 3/3 observed search inputs on 404 pages are rectangular with small radii (Apple ~4-6px, Deezer ~6px, Tines ~6px). The 404 search input is a form element, not a search-bar hero — it should use the system input token.
**Correct approach**: `border: 1px solid var(--surface-2); border-radius: 4px; padding: 8px 16px; font-family: var(--font-display); font-size: 16px`. Focus state: `border-color: var(--text)`.
**Checklist item**: If a search input exists, is the border-radius 4px (not 160px)?

---

### 3.3 Treating the 404 as a Landing Page

**Problem**: The 404 page includes multiple sections stacked vertically — features, social proof, newsletter signup, pricing teaser — turning the error page into a marketing surface.
**Why it's wrong**: A 404 page has one job: acknowledge the error and help the user recover. Adding marketing sections creates confusion ("Am I on the right page?") and dilutes the recovery message. Evidence: 0/45 samples stack more than 2 content areas (error block + destination list). Mural and Greptile include content-marketing elements, but even they are contained within one scrollable block, not multiple section-rhythm sections.
**Correct approach**: Maximum 2 content areas: the error block + an optional destination list (Archetype B). No newsletter signup, no testimonials, no feature showcases.
**Checklist item**: Does the page have more than 2 content areas?

---

## 4. When the User Provides a Brand Color

Adjustments to the rules above when `--accent` is overridden with a brand color:

- **CTA button** changes from default (black/white) to the brand color — normal `.btn-dark` behavior via `var(--accent)` / `var(--accent-text)`. No other changes needed
- **1.2 does not relax**: button radius stays `2px`, not pill
- **1.3 does not relax**: zero box-shadow, even for a branded button hover state. Use `transform: translateY(-1px)` + `filter: brightness(0.9)` (bright brand colors) or `filter: brightness(1.15)` (dark brand colors) per `shared/visual-style.md` section 10.1
- **1.4 does not relax**: background stays `var(--bg)`, not a light variant of the brand color
- **1.6 does not relax**: no decorative borders in the brand color
- **1.7 does not relax**: numeral stays `color: var(--text)`, not the brand color. The numeral occupies too much area for chromatic color
- **Chromatic area < 10%** does not relax. On a 404 page with one button, the CTA is the only chromatic element — this is correct
- Optional: link text hover color can use `var(--accent)` (allowed use from `shared/visual-style.md` section 1)

---

## 5. Verification Method

After generating the 404 page, verify the following 12 items:

1. **Is the full site navigation present?** Missing = error
2. **Is there at least one recovery action (button or link)?** No way out = error
3. **Is the button border-radius 2px?** 999px / pill = error
4. **Does any element use box-shadow?** Yes = delete
5. **Is the page background `var(--bg)` with zero hue?** Colored / gradient / tinted = error
6. **Is the numeral (if present) using `color: var(--text)` without chromatic fill?** Colored / gradient = error
7. **If numeral and heading coexist, is the numeral at reduced opacity (0.10-0.15)?** Both at full opacity = error
8. **Is all text using weight 500 (display) or 400 (mono/body)?** Weight 600/700/bold = error
9. **Is the visual element illustration-free?** Illustration / stock photo = error
10. **If humor is used, does it reference the product's domain?** Generic puns = replace with literal copy
11. **Are all fabricated details removed?** Fake paths / server names / stack traces = delete
12. **Is the content limited to 1-2 areas (error block + optional destinations)?** Multiple marketing sections = error
