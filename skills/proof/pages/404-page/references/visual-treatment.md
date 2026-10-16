# Visual Treatment — 404 Page

> Source: 45 unique products (32 well-known, 13 studio/niche). Covers how to carry the page visually within the system's constraints (no illustration, no stock photos).

---

## Core Insight

**39/45 pages carry the visual without illustration.** The system's "Content as decoration" principle (`shared/visual-style.md` Design Philosophy, item 4) aligns with majority practice. Illustration is the exception, not the norm.

Only 4/45 use a substantial illustration (Fauna, Shopify Editions, Deezer, Aave mascot). 2/45 use photography (Oura, Ada). These require custom assets and are outside V1 scope.

**Evidence status**: Observed.

---

## Visual Strategy Selection

Five strategies observed in the data, ranked by applicability to the system:

### Strategy 1: Typographic Display Numeral (Recommended Default)

**When to apply**: Any archetype. Works without user assets. The default visual strategy for this system.

**What it is**: "404" rendered at display scale (120–200px+), using the system display font. The numeral alone provides enough visual weight to fill a viewport-centered layout.

**Implementation**: See `error-display.md` §1.1 (full contrast), §1.2 (mono variant), or §1.3 (watermark).

**Opacity decision tree**:
- Numeral is the sole focal point (no text heading) → full opacity (1)
- Numeral coexists with a text heading → reduced opacity (0.10–0.15)
- Numeral sits behind content as texture → watermark opacity (0.08)

**Evidence**: 9/45 use a typographic display numeral as the primary visual — SpaceXAI, Public, Vucko, Aqua, Biograph, Butter, Slash, Parker, Fiasco. Plus 3/45 where the numeral is object/illustrated (Shopify Editions, Deezer, Flighty) — these are outside the system but confirm the numeral's visual strength.

**Evidence status**: Observed.

---

### Strategy 2: Oversized Heading

**When to apply**: Archetype C (Typographic sub-cluster). The product has a strong verbal identity. The heading text itself, at extreme scale, IS the visual.

**What it is**: The heading is rendered at ≥ 90px (hero scale or larger), dominating the viewport. No numeral, no image — the words fill the space.

**Implementation**:

```css
.error-heading-oversized {
    font-family: var(--font-display);
    font-size: clamp(64px, 12vw, 200px);  /* page-specific; exceeds hero max 80px */
    font-weight: 500;                      /* from shared/visual-style.md §2 */
    letter-spacing: -0.02em;               /* tracking rule: ≈ -2% of size */
    line-height: 1;                        /* tight for visual composition */
    color: var(--text);
}
```

**Copy**: Keep it short — 1–3 words work best. "Oh no." (GSAP, ~200px). "Sorry, we can't find this page." (Instrument, ~96px in a condensed face). Longer sentences at extreme scale create line-break problems.

**Evidence**: 2/45 — Instrument (~96px, condensed serif, one line), GSAP (~200px, heavy sans, gradient fill — within our system the fill would be `var(--text)` only). Both are Archetype C.

**Evidence status**: Observed.

**When NOT to apply**: When the heading is a full sentence (7+ words) — it won't read well at extreme scale. When the archetype is A or B — the heading should inform, not decorate.

---

### Strategy 3: Nothing / Whitespace as Design

**When to apply**: Ultra-minimal Archetype A. The product's brand is restrained. The 404 is treated as a quiet system message, not a design opportunity.

**What it is**: No visual element at all. The page is heading + body + button, centered in a sea of whitespace. The whitespace itself is the composition.

**Implementation**: No special tokens needed. Use the standard content block (`error-display.md` heading + body + button) centered via the viewport-fill layout (`section-composition.md` §2). The visual impact comes from the generous empty space.

**Evidence**: 9/45 use no visual element — Apple, Notion, Handshake, Orchid, Unify, Becane, AI Report, Phantom, SIGMA. These include major brands (Apple, Notion) and both well-known and studio products.

**Evidence status**: Observed.

---

### Strategy 4: Product-Content Reference

**When to apply**: Archetype C (Product-referential sub-cluster). The user describes their product's core output, and that output can be rendered as a visual.

**What it is**: The product's own UI, output, or domain visual is placed on the 404 page. The visual says "our product makes X, and even on our error page, you can see X."

**Implementation**: Reuse the **Synthetic Product Visual** recipe from `sections/hero/SKILL.md`. The recipe provides tokens for rendering product-UI mocks (outer frame, chrome bar, inner panels) without requiring a real screenshot.

**When the user provides a product description**:
- Document tool → show a grid of faint document tiles (Craft pattern)
- Design tool → show a vector-editing view of the numeral (Figma pattern)
- Code tool → show code-diff cards or terminal output (Greptile pattern)
- Flight/transport → show departure-board elements (Flighty pattern)

**Evidence**: 7/45 reference the product's own content — Craft (document tiles), Figma (vector path numeral), Greptile (code-review cards), Flighty (split-flap tiles), Zoox (vehicle on a track "0"), Firecrawl (scraper output), KÖPPEN (broken product photo).

**Evidence status**: Observed.

**When NOT to apply**: When the user provides no product description — the Agent cannot invent a product visual. Fall back to Strategy 1 (Typographic Numeral) or Strategy 3 (Nothing).

---

### Strategy 5: Brand-Mark Manipulation

**When to apply**: The user provides a logo or brand mark. The mark is rendered "broken," "incomplete," or "being repaired" to signal the 404 error.

**What it is**: The product's own logo, rendered in a way that suggests something is wrong — a piece missing, an editing UI visible, a puzzle with a gap.

**Evidence**: 4/45 — Vercel (triangle logo as an incomplete dashed outline), Mercury (logo as a sliding-tile puzzle with one tile missing), Mixpanel (3D brand shape with a piece broken off), Resend ("R" mark as a wireframe 3D object).

**Implementation**: This strategy requires the user to provide a logo asset. The Agent renders the logo in monochrome `var(--text)` and applies a visual treatment:
- **Dashed/incomplete outline**: draw the logo path with `stroke-dasharray`, omitting one segment
- **Missing piece**: show the logo with one part replaced by empty space
- **Editing UI overlay**: surround the logo with mock selection handles or anchor points (Figma style)

**CSS constraints**:
- Logo rendered in `color: var(--text)` — no brand colors in the mark itself (color silence)
- No box-shadow on the logo container
- Size: 100–200px, centered above the heading or beside it

**Evidence status**: Observed.

**When NOT to apply**: When no logo is provided. This strategy cannot be generated from text alone. Fall back to Strategy 1.

---

## Strategies Outside V1 Scope

These are observed in the data but require assets that cannot be generated offline:

| Strategy | Count | Why excluded |
|----------|-------|-------------|
| Illustration / 3D scene / mascot | 4/45 | Requires custom illustration assets (Fauna, Shopify Editions, Deezer, Aave) |
| Photography | 2/45 | Requires photography assets (Oura, Ada) |
| Animation | ≥1/45 | GSAP credits an animation the capture doesn't show; Flighty tiles may animate |
| Brand color field | 4/45 | Monte's full brand-color background, Stripe's diagonal bands, Mural's blue band, V7's accent graphics — outside the achromatic system |

---

## Strategy Selection Guide

```
1. Does the user provide a product description or visual concept?
   |-- Yes, product output can be visualized --> Strategy 4 (Product-Content Reference)
   |-- Yes, a logo/brand mark is provided --> Strategy 5 (Brand-Mark Manipulation)
   |-- No user assets available:
       |
       2. What archetype was selected?
          |-- A (Minimal Redirect):
          |   |-- Product is ultra-minimal (Notion, Linear style) --> Strategy 3 (Nothing)
          |   |-- Default --> Strategy 1 (Typographic Numeral, low-contrast or watermark)
          |
          |-- B (Navigational Recovery):
          |   --> Strategy 3 (Nothing) or Strategy 1 (small numeral)
          |   The destination list IS the visual weight; a large numeral competes
          |
          |-- C (Brand Moment):
          |   |-- Short heading (1-3 words) --> Strategy 2 (Oversized Heading)
          |   |-- Longer heading --> Strategy 1 (Typographic Numeral, full contrast)
```

---

## Small Spot Icons / Emoji

4/45 use a small spot icon or emoji (Jitter 🧐, Opennote compass, Linear computer, Tines UFO). These are not a "visual strategy" in the same way as the numeral or oversized heading — they add a small personality touch but do not carry the page.

**When acceptable**: A small monochrome SVG icon (20–48px) placed above the heading. Must be `color: var(--text); opacity: 0.4` — no colored icons, no circular backgrounds (per `shared/visual-style.md` "Absolutely Forbidden" list).

**Emoji**: A single emoji character at ~32–48px is acceptable as a lightweight personality signal. Do not use multiple emoji or emoji as the primary visual.

**Evidence status**: Observed.

---

## Dark Theme Considerations

13/45 samples use a dark theme. For the visual treatment:

- **Numeral**: `color: var(--text)` resolves to `#EDEDED` in dark theme. Low-contrast opacity (0.10–0.15) produces faint light-on-dark type — visually effective.
- **Backgrounds**: `var(--bg)` = `#0A0A0A`, `var(--surface-1)` = `#141414`. The three-step achromatic scale creates depth without shadows.
- **Terminal syntax colors** (page-specific — not defined in `shared/visual-style.md`): green #4ADE80, red #F87171, yellow #FBBF24, blue #60A5FA, cyan #22D3EE — used only inside code/terminal mocks if the product is developer-facing, never for UI elements. These are standard terminal palette values, not design system tokens.
- **Button on dark**: `.btn-dark` uses `var(--accent)` which defaults to `var(--text)` (#EDEDED) — a light button on a dark page. No special override needed for the default case.
- **Outline button on dark**: No override needed. On a dark-theme page, `var(--text)` resolves to `#EDEDED` (light) — `.btn-outline { color: var(--text); border: 1px solid var(--surface-2); }` produces light text and a visible border on the `#0A0A0A` background. **Do NOT add `class="section-dark"` to the 404 page section** — `.section-dark` is only for creating a dark-band section inside a light-theme page. Applied to an already-dark page's section, it would set `background: var(--text)` = `#EDEDED`, creating an unwanted light panel.

**Evidence status**: Cross-sample inference (dark theme token behavior derived from the system; individual dark samples observed).
