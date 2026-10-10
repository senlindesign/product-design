# 404 Page Archetypes and Selection Guide

> Source: Mobbin research synthesis from 45 unique products (32 well-known, 13 studio/niche)

---

## Archetype Definitions

### A. Minimal Redirect

**Typical products**: Early-stage SaaS, single-product tools, developer platforms, marketing sites with simple IA
**Core characteristics**: Status code display (optional) + heading + 1-2 sentences + one CTA back to home. Nothing else.

**Selection conditions**:
- Product has a single main entry point (homepage or app dashboard)
- No need to guide users to multiple destinations — one link is enough
- 404 is a rare, low-stakes event for this audience
- When in doubt, choose this archetype (safest default)

**Typical page composition**:
1. Navigation (keep the site's standard nav)
2. Error Content Block (vertically centered in the viewport)
   - Optional: small label ("404" or "ERROR 404") or display numeral
   - Heading: "Page not found" or equivalent literal phrase
   - Body: 1-2 sentences explaining the cause
   - CTA: one `.btn-dark` button ("Go home" / "Back to homepage")
3. Footer (optional; below the fold in viewport-fill layouts)

**Visual treatment options** (choose one):
- **Nothing**: plain typography + whitespace. Evidence: 9/45 samples use no visual element at all (Apple, Notion, Handshake, Orchid, Unify, Becane, Phantom, SIGMA, AI Report)
- **Display numeral**: "404" at large scale (100-200px), using `var(--font-display)` at weight 500. Evidence: 12/45 samples use a display numeral >= ~100px
- **Low-contrast display numeral**: "404" at large scale alongside content, at opacity 0.10–0.15. The numeral is in normal document flow, demoted to texture so it doesn't compete with the heading. Evidence: SpaceXAI (~0.11), Biograph (~0.10–0.15)
- **Watermark numeral**: "404" absolutely positioned **behind** content at opacity 0.08. The numeral fills ~70% of the viewport width and content sits on top. Evidence: Parker (~0.06); footer giant-wordmark precedent (0.05–0.10)
- **Mono/status-line variant** (from the D reframing): heading formatted as "404: Not Found" using `var(--font-mono)`, styled like the system `.label` or at a larger mono size. Evidence: Resend uses the HTTP status-line format; Instrument uses a mono label "ERROR CODE: 404"; Aqua uses a mono-face numeral. Use `var(--font-mono)` for the code/label portion

**Heading tone**: Literal. Evidence: 22/34 headings with text use literal tone ("Page not found" / "This page couldn't be found"). Apologetic ("Sorry, we can't find...") is acceptable. Humor works only when the copy references the product's domain — do not fabricate puns.

**CTA copy**: Choose a destination that matches the most likely cause of the 404. Evidence: Vercel uses "Sign into Vercel" (audience = logged-out users hitting dashboard URLs); Mixpanel links to "Your Dashboard" (audience = existing users). Default: "Go home" / "Back to homepage". If the product has a more contextually useful destination, use that instead.

**Observed products**: Apple (also B), Notion, Stripe, Unify, Becane, Handshake, Jitter, Biograph, Opennote, Aqua, Butter, Slash, Parker, Fiasco (also C), Public, SIGMA, Monte, Linear, Vercel, Resend (also D), Phantom, AI Report

**Count**: 22/45 (including combo tags)

---

### B. Navigational Recovery

**Typical products**: Multi-product platforms, docs-heavy sites, content hubs, products where users navigate to specific subpages
**Core characteristics**: Error message + recovery mechanisms (suggested destinations, search, or both). The page helps users find where they meant to go.

**Selection conditions**:
- Product has multiple important destinations (docs, blog, pricing, help center, app)
- The 404 audience likely arrived via a broken link to a specific subpage, not the homepage
- Providing a list of destinations is more helpful than a single "Go home" button
- Product has enough pages to make a destination list meaningful (>= 4 notable pages)

**Typical page composition**:
1. Navigation (keep the site's standard nav)
2. Error Content Block
   - Optional: small label ("404 error") or display numeral
   - Heading: "Page not found" or equivalent
   - Body: 1-2 sentences + lead-in to destinations ("Try one of the links below:" or "You might be looking for:")
   - CTA: one `.btn-dark` button for home (secondary to the destination list)
3. Destination List (one of the formats below)
4. Footer (flows naturally after content)

**Destination formats** (choose one based on content available):

| Format | When to use | Evidence |
|--------|------------|----------|
| **List rows** (title + description + arrow, separated by 1px dividers) | 4-8 destinations with short descriptions | SpaceXAI: 6 rows with title + description + arrow |
| **Cards** (title + description, `var(--surface-1)` background, `border-radius: 8px`, `padding: 32px`) | 2-4 destinations that benefit from visual separation | Aave: 2-3 cards; Ada: 4 cards in 2x2 grid; V7: 3 cards |
| **Inline text links** (comma- or dot-separated in a single line) | 3-5 destinations, minimal presentation | Orchid: 4 underlined links; Mixpanel: 3 inline links after a colon |
| **Bulleted link list** (simple vertical list) | 5-8 destinations, no descriptions needed | Firecrawl: 8 bulleted text links |

**Lead-in pattern**: 6/9 samples with destinations use a label or sentence ending in a colon to introduce the list. Examples: "Helpful links" (SpaceXAI), "You might be looking for:" (Aave), "Try one of these instead." (Orchid), "Try one of the links below:" (Firecrawl).

**Search** (optional, uncommon): Only 3/45 samples include search. All 3 use a rectangular input with 4-6px radius (not pill). If implementing search, use the system input token: `border: 1px solid var(--surface-2); border-radius: 4px; padding: 8px 16px; font-size: 16px`. Placeholder should name the product's content types (e.g., "Search docs, blog, and help articles") rather than a generic "Search...". Evidence: Apple, Deezer, Tines.

**Destination types observed** (from 9 samples with >= 2 destinations): blog/news, docs, help center, pricing, community, product/app, case studies, careers, contact, changelog, GitHub.

**Layout note**: For B with a destination list or card grid, do not force viewport-fill layout. Content may exceed one screen — allow natural scrolling. Use `max-width: 1080px` (system `.container`) for card grids.

**Observed products**: Apple, Mural, Aave, V7, Ada, Greptile, Firecrawl, Orchid, Mixpanel (also C), SpaceXAI (also A), Tines, Deezer (also C)

**Count**: 12/45 (including combo tags)

---

### C. Brand Moment

**Typical products**: Design-driven brands, creative tools, consumer products, products with strong visual identity
**Core characteristics**: The visual element IS the page. Copy is minimal and often humorous. The 404 becomes an opportunity to express brand personality.

**Selection conditions**:
- Product has a strong visual identity or a recognizable visual language
- The brand benefits from showing personality on an error page
- The product's domain lends itself to product-referential humor (e.g., a flight tracker joking about departure, a document tool joking about pages)
- The user explicitly wants a more expressive 404 page

**Typical page composition**:
1. Navigation (keep the site's standard nav)
2. Visual + Content Block (vertically centered or top-offset)
   - The visual element dominates; copy is secondary
   - Heading: short, may be humorous or product-referential
   - Body: 1-2 sentences at most
   - CTA: one button or inline link back to home
3. Footer (optional; below the fold)

**Sub-clusters** (cross-sample inference):

**Typographic C** — the visual is pure type at extreme scale
- The heading itself (>= 90px) or a giant numeral (>= 200px) carries the page
- Works without any user assets — the default C for this system
- Evidence: Vucko (numeral pinned top-left, ~15-16vw), Fiasco (numeral at ~75% viewport width), Instrument (heading at ~96px), GSAP (heading at ~200px)
- Implementation: Use `var(--font-display)`, weight 500. For the giant heading, use `clamp(64px, 12vw, 200px)` or equivalent. For a giant numeral, use `font-size: clamp(120px, 20vw, 300px); color: var(--text); opacity: 0.10-0.15` as a background element

**Product-referential C** — the visual references the product's own output or domain
- Requires the user to provide or describe a product-specific visual concept
- Evidence: Figma (numeral drawn as a selected vector path), Craft (document-tile wall), Flighty (departure-board tiles), Zoox (vehicle on a track-shaped "0"), Vercel (incomplete logo), Mercury (logo as a sliding-tile puzzle), Greptile (product-output cards), KOPPEN (product shown broken)
- Humor pattern: name the product's core competence, then admit the irony. "Pages are kind of our thing" (Craft). "Flawless navigation is kind of our thing" (Zoox). "We haven't ghosted you!" (Phantom). Evidence: 10/45 samples use humor; product-referential humor works best

**Immersive C** — full-bleed scene or photo (OUT OF V1 SCOPE)
- Requires custom photography or 3D assets
- Evidence: Shopify Editions (3D water scene), Oura (lifestyle photograph)
- Not supported in V1 — cannot be generated offline without assets

**Default C for the system**: Typographic C. It works without user assets, stays within the achromatic system, and produces a strong visual with type alone.

**Observed products**: Vucko, Fiasco, Instrument, GSAP, Figma, Flighty, Zoox, Craft, Greptile, KOPPEN, Vercel, Mercury (also A), Mixpanel (also B), Deezer (also B), Shopify Editions, Oura

**Count**: 16/45 (including combo tags)

---

## Selection Flow

```
1. What is the product type?
   |-- Single-product SaaS / simple marketing site --> A. Minimal Redirect
   |-- Multi-product platform / docs-heavy site / content hub --> B. Navigational Recovery
   |-- Design-driven / creative / consumer brand --> C. Brand Moment
   |-- Unsure --> A. Minimal Redirect (safest default)

2. After selecting, verify with corrections:
   - Chose A but the product has 5+ important subpages?
     --> Consider upgrading to B (add a destination list)
   - Chose B but the product only has a homepage and one app?
     --> Downgrade to A (a destination list of 1-2 items is not useful)
   - Chose C (Product-referential) but the user provides no visual concept?
     --> Fall back to Typographic C (giant heading or numeral)
   - Chose C but the product has no personality or humor angle?
     --> Downgrade to A (forced humor is worse than literal tone)
```

---

## Cross-Archetype Common Rules

Regardless of which archetype is chosen:

1. **Keep the navigation**: 13/17 observable samples keep the full site nav. The nav is the user's primary escape from a 404 page — do not remove it
2. **One CTA button is enough**: 23/25 pages with buttons use exactly one. Two buttons (Mercury, Greptile) are the exception, not the norm
3. **Heading copy is literal by default**: "Page not found" / "This page could not be found" — 22/34 headings. Do not fabricate humor unless the product's domain provides a natural angle
4. **Home is the default recovery action**: 32/45 samples include a home link (71%). Use "Go home" / "Back to homepage" unless a more contextually useful destination exists
5. **The numeral is optional**: 15/45 samples (33%) show no "404" at all, relying entirely on heading copy. Showing the numeral is not required
6. **Viewport-fill layout for A and C**: `min-height: calc(100vh - var(--nav-h)); display: flex; align-items: center; justify-content: center;`. Evidence: 15/25 explicit samples are vertically centered. Exception: B with many links allows scrolling
7. **Do not fabricate contact information, product details, or error metadata**: Use placeholders and note them in delivery notes
