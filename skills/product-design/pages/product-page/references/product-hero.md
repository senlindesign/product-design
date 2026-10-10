# Product Page Hero Patterns

> Source: 8 hero observations across Product pages (Tines, Kajabi, SpaceXAI, Retool, Intercom, folk, Grain, Vanta). All tokens validated against `shared/visual-style.md`.

---

## How the Product Hero Differs from the Landing Hero

| Dimension | Landing Hero | Product Hero |
|-----------|-------------|--------------|
| Visual content | Static product screenshot | Video or video thumbnail (8/8 samples) |
| Primary CTA | "Start free trial" / "Get started" | "Request a demo" / "Watch demo" (or play button as CTA) |
| Layout bias | Centered with visual below (dominant) | Centered and 2-col split occur equally (3/8 each) |
| Brand color presence | Minimal — achromatic default | More prominent (2/8 use brand-colored section backgrounds) |
| CTA count | 1 primary + optional secondary | Dual CTA common: self-serve + demo (4/8) |
| Visual framing | Screenshot in surface-1 frame | Video thumbnail with play button overlay (5/8) |

**Key insight**: The Product hero prioritizes **demonstration over conversion**. Video replaces static screenshots; "see a demo" replaces "sign up now." Visitors on a Product page are evaluating, not impulse-buying.

---

## Pattern 1: Centered with Video Below (3/8)

**When to use**:
- Product has a compelling video demo or product tour
- Standard information flow: heading above, video below
- Single product with a unified story (not a multi-product platform)

**Execution**:
- Structure (top to bottom): Heading (centered) + Subtitle (centered) + Video thumbnail with play button
- Video thumbnail occupies 70-90% of content width
- Play button centered on thumbnail: 48px circle, dark background, white triangle icon
- Heading carries hero weight; subtitle provides the "what it does" explanation

```css
.product-hero-heading {
    font-family: var(--font-display);
    font-size: clamp(48px, 7vw, 80px);   /* hero heading scale */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.05;
    color: var(--text);
    text-align: center;
}

.product-hero-subtitle {
    font-family: var(--font-body);
    font-size: 18px;                      /* body text scale */
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;                         /* subtitle opacity */
    max-width: 540px;                     /* subtitle max-width */
    margin: 24px auto 0;                  /* hero heading to subheading: 24px */
    text-align: center;
}

.product-hero {
    padding-top: 128px;                   /* hero top whitespace */
    padding-bottom: 180px;               /* section rhythm */
}
```

**Video thumbnail tokens**:
```css
.product-hero-video {
    position: relative;
    width: 100%;
    max-width: 960px;                    /* within 1080px grid */
    margin: 48px auto 0;                 /* subheading to video */
    border-radius: 16px;                 /* content card radius */
    overflow: hidden;
    background: var(--surface-1);
    cursor: pointer;
}

.product-hero-video img {
    width: 100%;
    display: block;
}

.play-button {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: var(--text);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: transform 0.2s ease-in-out;
}
.play-button:hover { transform: translate(-50%, -50%) scale(1.05); }

/* Triangle icon inside play button */
.play-button::after {
    content: '';
    display: block;
    width: 0;
    height: 0;
    border-style: solid;
    border-width: 8px 0 8px 14px;
    border-color: transparent transparent transparent var(--text-inverse);
    margin-left: 2px;                    /* optical center correction */
}
```

**Variants**:
- **"Meet the product" framing** (Tines): heading uses product-introduction language ("Meet the product", "Take a product tour") rather than benefit language. Use when this is a dedicated product tour page or sub-page
- **Without subtitle** (folk): heading text overlaid directly on the video thumbnail. Use when the video content is self-explanatory. Requires sufficient contrast between heading text and thumbnail image

**When not to use**:
- Product requires side-by-side text and visual for comprehension (use Pattern 2)
- No video available — a static screenshot works but loses the Product hero's primary differentiator

**Evidence**: Tines, SpaceXAI, Retool
**Evidence status**: Cross-sample inference

---

## Pattern 2: Text Left + Visual Right (3/8)

**When to use**:
- Text description and product visual need equal simultaneous presence
- Product visual includes a person (testimonial video) or complex UI that needs context
- "Request a demo" is the primary CTA (enterprise/B2B products)

**Execution**:
- 2-col split: text ~40-45%, visual ~55-60%
- Text side: Heading + Description paragraph + Dual CTA buttons
- Visual side: Video thumbnail or product screenshot with play button
- Stacks vertically on narrow screens (text on top)

```css
.product-hero-split {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 58px;                           /* standard heading-to-content gap */
    align-items: center;
    padding-top: 128px;                  /* hero top whitespace */
    padding-bottom: 180px;              /* section rhythm */
}

@media (max-width: 767px) {
    .product-hero-split {
        grid-template-columns: 1fr;
        gap: 40px;                       /* narrow screen: 58px -> 40px */
        padding-top: 80px;              /* narrow screen: 128px -> 80px */
        padding-bottom: 96px;           /* narrow screen: 180px -> 96px */
    }
}
```

**CTA group tokens**:
```css
.product-hero-cta {
    display: flex;
    gap: 12px;
    margin-top: 48px;                    /* subheading to CTA */
}

/* Primary: "Start free trial" — uses .btn-dark .btn-lg */
/* Secondary: "Request a demo" or "Watch demo" — uses .btn-outline .btn-lg */
```

Both CTA buttons use `.btn-lg` (padding 12px 24px, font-size 16px) for visual balance under the hero heading. The secondary CTA often uses demo-oriented language ("Request a demo", "Book a demo", "Watch demo") instead of the Landing page's "Learn more."

**Variants**:
- **With logo bar below** (Vanta): Grayscale customer logos immediately below the 2-col hero, within the same section. Uses the standard logo wall pattern (flex, opacity 0.15)
- **Video shows a person** (Vanta, Kajabi): Video thumbnail is a testimonial/presenter, not a product screenshot. Adds human credibility. Combine with a separate product screenshot elsewhere on the page

**When not to use**:
- Product screenshot needs large-area display (centered layout Pattern 1 is better)
- The visual content is an abstract illustration, not product UI or a demo video

**Evidence**: Kajabi, Grain, Vanta
**Evidence status**: Cross-sample inference

---

## Pattern 3: Full-Width Visual with Overlay (2/8)

**When to use**:
- Video content is the entire story — minimal text needed
- Product page that functions as a demo/showcase rather than a traditional product description
- The video thumbnail communicates the product better than any heading could

**Execution**:
- Video thumbnail dominates the viewport (80-100% width)
- Heading text overlaid on the video or positioned as a small CTA link above
- Play button overlay centered on the video
- Minimal text — the visual IS the section content

**Implementation note**: This pattern requires high-quality video thumbnails with consistent lighting. If no video is available, default to Pattern 1 or Pattern 2 instead. Text overlay on video requires a semi-transparent dark gradient at the text position for contrast.

**When not to use**:
- No high-quality video thumbnail available
- Product requires explanatory text to be understood
- The page must convey multiple messages in the hero (use Pattern 1 or 2)

**Evidence**: folk, Intercom
**Evidence status**: Cross-sample inference — smallest sample (2/8), use with caution

---

## CTA Copy Patterns for Product Pages

Product page CTAs differ from Landing page CTAs. Observed patterns:

| CTA type | Frequency | When to use |
|----------|-----------|-------------|
| Play button as CTA (video play) | 4/8 | When the video itself is the primary conversion action |
| "Request a demo" / "Book a demo" | 3/8 | Enterprise/B2B products where sales involvement is expected |
| "Start free trial" / "Get started" | 1/8 | Self-serve products with freemium model |
| Dual CTA (free + demo) | 4/8 | When both self-serve and sales-assisted paths exist |

**Default recommendation**: Dual CTA with `.btn-dark .btn-lg` ("Start free trial") + `.btn-outline .btn-lg` ("Request a demo"). If only one CTA, choose based on the product's sales model.

---

## Narrow Screen Adjustments

```css
@media (max-width: 767px) {
    .product-hero {
        padding-top: 80px;              /* 128px -> 80px */
        padding-bottom: 96px;           /* 180px -> 96px */
    }

    .product-hero-heading {
        /* clamp() handles font size automatically */
    }

    .product-hero-subtitle {
        max-width: 100%;                /* remove 540px cap on narrow screens */
    }

    .product-hero-cta {
        flex-direction: column;
        gap: 12px;
    }
}
```
