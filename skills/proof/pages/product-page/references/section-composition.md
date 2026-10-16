# Product Page — Section Composition

> Source: ~51 section observations across ~44 unique products. All spacing/color tokens validated against `shared/visual-style.md`.

---

## Default Section Order by Archetype

### A. Feature Showcase (8-12 sections)

```
Nav
Hero (centered or 2-col split, product video/screenshot, dual CTA)
Logo Wall (grayscale customer logos, trust signal)
Feature Grid Primary (3-col or 2-col cards, 3-6 features, screenshot + heading + description)
Feature Grid Secondary (optional: "...and more" framing, 3-6 additional features)
Use Cases (optional: 3-4 persona/industry cards)
Integrations (optional: 3-6 featured cards + API section)
Social Proof (optional: customer testimonials)
CTA (dual: "Start free" + "Request a demo")
FAQ (optional, shared pattern)
Footer
```

**Optional additions** (insert at marked positions):
- Use Cases: after Feature Grid, before Integrations (only when product serves distinct personas or industries)
- Integrations: after features/use cases, before CTA (only when integration ecosystem is a selling point)
- FAQ: before CTA (only when product has common objections to address on the product page)

### B. Platform Overview (7-10 sections)

```
Nav
Hero (dark common, heading + capabilities or stats)
Logo Wall (enterprise trust signal)
Capability Pillars (2x3 or 3-col grid with mono labels)
Architecture Section (card-based component layout)
Platform Stats (optional: large numbers as proof points)
Integrations (required: categorized cards + API/developer CTA)
CTA (dual: "Get started" + "Book a demo")
Footer
```

**Optional additions**:
- Platform Stats: after Architecture, before Integrations (include when impressive scale numbers exist)
- Social Proof: after Stats, before CTA (enterprise logos or case study)

### C. Product Deep-Dive (6-9 sections)

```
Nav
Hero (2-col split: heading + CTA left, video/screenshot right)
Logo Wall (optional)
Feature Deep-Dive 1 (2-col: text + accordion left, screenshot right)
Feature Deep-Dive 2 (2-col: screenshot left, text + accordion right)
Feature Deep-Dive 3 (optional, alternating sides)
Social Proof (optional: customer testimonial)
CTA (dual: "Start free" + "Request a demo")
Footer
```

**Notes**:
- 2-4 deep-dive sections; each covers one major capability
- Alternate the text/screenshot sides for visual rhythm
- No separate Use Cases or Integrations section needed — depth per capability replaces breadth

---

## Section Rhythm and Spacing

All spacing values from `shared/visual-style.md` section 3.

### Section Padding

```css
.section {
    padding: 180px 0;                 /* section rhythm baseline */
}

.product-hero {
    padding-top: 128px;               /* hero top whitespace */
    padding-bottom: 180px;            /* section rhythm */
}
```

### Internal Spacing

```css
.section-heading {
    margin-bottom: 58px;              /* heading-to-content distance */
}
```

### Narrow Screen (< 768px)

```css
@media (max-width: 767px) {
    .section {
        padding: 96px 0;              /* 180px -> 96px */
    }
    .product-hero {
        padding-top: 80px;            /* 128px -> 80px */
        padding-bottom: 96px;         /* 180px -> 96px */
    }
    .section-heading {
        margin-bottom: 40px;          /* 58px -> 40px */
    }
    .container {
        padding: 0 20px;              /* 32px -> 20px */
    }
}
```

---

## Background Alternation Rules

The Product page follows the same background rules as all page types (`shared/visual-style.md` section 8).

| Section | Background | Rationale |
|---------|-----------|-----------|
| Hero | `var(--bg)` | Always page background |
| Logo Wall | `var(--bg)` | Same as Landing logo wall |
| Feature Grid | `var(--bg)` | Default |
| Feature Grid Secondary | `var(--surface-1)` (optional) | May use surface-1 to visually separate from primary grid. At most 1 feature section uses this |
| Use Cases | `var(--bg)` | Default |
| Capability Pillars | `var(--bg)` | Default |
| Architecture | `var(--surface-1)` (optional) | Technical sections may use surface-1 as a differentiated band |
| Platform Stats | `var(--bg)` | Default |
| Integrations | `var(--bg)` | Default |
| Social Proof | `var(--bg)` | Default |
| CTA | `var(--bg)` or dark band via `class="section-dark"` | Dark band: add `class="section-dark"` to the `<section>` — sets `background: var(--text)` and inverts all text/button colors automatically (see `shared/visual-style.md §8`). Do NOT set background manually without the class — buttons become invisible |
| FAQ | `var(--bg)` | Default |

**Rules**:
- At most 1-2 sections use `var(--surface-1)` background. The rest use `var(--bg)`
- No colored backgrounds, no gradients, no photographic backgrounds
- All neutral colors must be pure achromatic (zero hue shift)
- Evidence: only 2/44 products (Tines, Kajabi) use colored section backgrounds, and both reserve them for CTA/demo sections exclusively

---

## Nav and Footer

Reuse shared components without modification:
- **Navigation**: `shared/navigation.md` + `sections/navigation/SKILL.md`
- **Footer**: `shared/footer.md` + `sections/footer/SKILL.md`

Nav height is `68px` (`var(--nav-h)`). When using `position: fixed`, add `body { padding-top: var(--nav-h); }` to prevent the hero heading from sitting under the nav.

---

## Product Hero

Product page heroes differ from Landing page heroes in three ways:

1. **Video is nearly universal**: 8/8 product hero observations include video or video-like content. Landing heroes often use static screenshots. Product heroes should default to a product screenshot with an optional play button overlay
2. **"Demo" framing replaces "Sign up" framing**: "Request a demo" / "Book a demo" / "Watch product tour" (3/8 hero observations) instead of "Get started" / "Sign up"
3. **2-col split is equally common as centered**: 3/8 use 2-col (text left ~40-45%, visual right ~55-60%). 3/8 use centered (heading above, visual below). Choose based on content density

### Hero Layout Options

**Centered (heading above, visual below)** — use when the product visual is the primary message:
```
[Heading]
[Subtitle]
[CTA buttons]

[Product screenshot / video]
```

**2-col split (text left, visual right)** — use when heading + description need more space:
```
[Heading]              [Product screenshot /
[Subtitle]              video with play button]
[CTA buttons]
```

### Hero CTA Pattern

Product page hero CTAs lean toward demo-oriented language. Evidence: 3/8 include "Request a demo" / "Book a demo"; 4/8 use a play button as the primary CTA.

**Default dual CTA**:
- Primary: `.btn-dark` "Start free trial" / "Get started free"
- Secondary: `.btn-outline` "Request a demo" / "Watch demo"

**Typography** (from frozen tokens):
- Heading: `clamp(48px, 7vw, 80px)` / `500` / `-0.02em` / `1.05`
- Subtitle: `18px` / `400` / `normal` / `1.6` / `opacity: 0.5` / `max-width: 540px`
- Button: `16px` / `500` / `padding: 12px 24px` / `border-radius: 2px` (btn-lg)

---

## CTA Section

### Dual CTA Pattern (Default for Product Pages)

Evidence: 4/6 CTA observations use dual CTA with both self-serve and sales-assisted paths.

**Default layout** (centered):
```
[Heading — value proposition restatement]
[Subtitle — 1 sentence]
[Primary CTA: "Start free trial"]  [Secondary CTA: "Request a demo"]
```

**Heading examples** (from observations):
- "Try [Product] today" (Contra)
- "The [category] your [audience] will love" (Twingate)
- "Let's bring [product] to your [domain]" (Robot.com)

**Implementation**:
```css
.cta-heading {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);   /* section heading scale */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
}

.cta-subtitle {
    font-family: var(--font-body);
    font-size: 18px;
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    max-width: 540px;
    margin: 24px auto 0;
}

.cta-buttons {
    display: flex;
    gap: 12px;
    justify-content: center;
    margin-top: 48px;
}
```

### When to Use a Dense CTA (Demo Request Form)

Evidence: 1/6 CTA observations (Robot.com) uses a 2-col split with benefit list + demo form. This pattern is appropriate for enterprise/sales-heavy products.

**Do not default to this pattern.** Use it only when the user explicitly requests a demo request form in the CTA section. The simple dual-button pattern is the default.

---

## Reusable Section Knowledge

The following sections reuse existing Skill knowledge without modification:

| Section | Source file | Notes |
|---------|------------|-------|
| Logo Wall | `pages/landing-page/references/social-proof.md` | Same logo wall pattern; grayscale, the style's logo-wall opacity |
| Social Proof | `pages/landing-page/references/social-proof.md` | Customer quotes pattern |
| FAQ | `pages/landing-page/references/faq.md` | Same accordion pattern |
| Navigation | `shared/navigation.md` | Shared component |
| Footer | `shared/footer.md` | Shared component |

**Product-page-specific sections** (new knowledge, not reusable from existing Skills):
- Feature Grid / Cards (see `feature-showcase.md`)
- Use Cases (see `use-cases.md`)
- Integrations (see `integrations.md`)
- Capability Pillars / Architecture (Archetype B only, see `archetypes.md`)

---

## Total Page Length by Archetype

| Archetype | Section count | Relative length | Comparison to Landing |
|-----------|:------------:|:---------------:|----------------------|
| A. Feature Showcase | 8-12 | Longest | Longer than Landing (6-8) |
| B. Platform Overview | 7-10 | Medium | Similar to Landing |
| C. Product Deep-Dive | 6-9 | Shortest | Similar to Landing |

Product pages are generally longer than Landing pages because they show more features. The Feature Showcase archetype is the longest, with 1-2 feature grid sections plus optional use cases and integrations.

### Narrow Screen Behavior

All sections stack naturally in a single column. No section reordering is needed on narrow screens. The only adjustments are the spacing reductions defined in the narrow screen table above.

Grid-based sections collapse to fewer columns:
- 3-column feature grid: 1 column on narrow screen (cards stack vertically)
- 2-column feature grid: 1 column on narrow screen
- 2-col hero split: single column (heading above, visual below)
- 3-4 column use case cards: 1-2 columns on narrow screen
- Integration card grid: 2 columns on narrow screen
- 2x3 capability grid: 1 column on narrow screen
