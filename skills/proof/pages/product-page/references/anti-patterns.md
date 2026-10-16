# Anti-Patterns — Product Page

> Source: ~51 section observations across ~44 unique products + lessons from Landing/Pricing/Contact/404/About/Section Skills practice. Every rule validated against `shared/visual-style.md`.

---

## 1. Visual Errors

### 1.1 Illustrations Instead of Product Screenshots

**Problem**: Feature sections use custom illustrations, abstract graphics, or conceptual diagrams instead of product UI screenshots.
**Why it's wrong**: Evidence: 8/11 feature deep-dive observations use actual product screenshots. Only 1/11 (Deel) uses illustrations. The design system's fourth principle is "Content as decoration" — product screenshots/output serve as hero visuals and brand texture; reject illustrations (`shared/visual-style.md` Design Philosophy, item 4). Product pages exist to SHOW the product.
**Correct approach**: Every feature card includes a product screenshot inside a `var(--surface-1)` container with `border-radius: 16px` (content card radius from system). If no screenshot is available, use the Synthetic Product Visual recipe from the Hero Skill.

```css
.feature-screenshot-frame {
    background: var(--surface-1);     /* #F5F5F5 light / #141414 dark */
    border-radius: 16px;              /* content card radius */
    overflow: hidden;
}

.feature-screenshot-frame img {
    width: 100%;
    display: block;
}
```

**Checklist item**: Does every feature card include a product screenshot (not an illustration)?

---

### 1.2 Colored Icon Backgrounds on Use Case Cards

**Problem**: Each use case or persona card has an icon on a colored circular or square background (e.g., green circle + chart icon for "Analytics", blue circle + people icon for "HR").
**Why it's wrong**: `shared/visual-style.md` section 1 explicitly prohibits icon backgrounds and badge fills. Evidence: 3/8 use case observations use no visuals at all (Mora, Vizcom, Intercom nav). 2/8 use photography (Slash, Shade). Only 1/8 (Grain) uses colored icons, and that is a brand-specific treatment. The system does not support per-card color differentiation.
**Correct approach**: Use case cards are text-only: heading + description. No icons. If a visual marker is needed, use the standard `.label` token above each card heading.

```css
.use-case-label {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    margin-bottom: 16px;
}
```

**Checklist item**: Do any use case cards have colored icon backgrounds? If yes, remove them.

---

### 1.3 Box-Shadow on Feature Cards

**Problem**: Feature cards or integration cards use `box-shadow` for depth or hover elevation.
**Why it's wrong**: The system uses zero shadows (`shared/visual-style.md` section 5: "No element on the entire site uses box-shadow"). Hierarchy is established through background color steps and borders.
**Correct approach**: Cards use `background: var(--surface-1)` with no shadow. For additional depth, use `border: 1px solid var(--surface-2)`. For hover feedback, use `transform: translateY(-4px)` per `shared/visual-style.md` §6 (card hover lift, not button micro-lift).
**Checklist item**: Does any card element use box-shadow? If yes, remove it.

---

### 1.4 Colored Section Backgrounds for Feature Areas

**Problem**: Feature sections use branded or tinted backgrounds (e.g., light blue for "Communication", light green for "Analytics").
**Why it's wrong**: `shared/visual-style.md` section 1 explicitly states: "Different background colors for different sections" is absolutely forbidden. Evidence: only 2/44 products (Tines, Kajabi) use colored section backgrounds, and both restrict them to CTA/demo sections, never feature sections.
**Correct approach**: Feature sections use `var(--bg)`. At most 1-2 sections on the entire page may use `var(--surface-1)`. No colored, gradient, or photographic backgrounds.
**Checklist item**: Are all feature sections on `var(--bg)` or `var(--surface-1)` (never colored)?

---

### 1.5 Serif or Italic Headings

**Problem**: Section headings use serif fonts, italic styling, or decorative typefaces.
**Why it's wrong**: The system locks display text to `var(--font-display)` (DM Sans) at weight 500 (`shared/visual-style.md` section 2). Evidence: while some product pages (Tines, incident.io) use serif headings, these are brand-specific choices. The system does not include serif in its three-font stack.
**Correct approach**: All headings use `font-family: var(--font-display); font-weight: 500`. No serif, no italic, no weight 700.
**Checklist item**: Are all headings in DM Sans at weight 500?

---

## 2. Content Errors

### 2.1 Feature Overload Without Grouping

**Problem**: Showing 10+ features in a single undifferentiated grid section without visual or categorical grouping.
**Why it's wrong**: Evidence: feature count per section ranges from 2-7, with 3-6 being the most common. No observation shows 10+ features in one flat grid. ClickUp (7 features) uses a carousel with pagination. Mixpanel groups features by category labels ("ADOPTION", "ANALYSIS"). Ungrouped feature dumps create cognitive overload.
**Correct approach**: Split into multiple sections (primary features + "...and more" secondary), use carousel for 7+, or add category labels. Maximum 6 features per grid section.
**Checklist item**: Does any feature section show more than 6 features without grouping or pagination?

---

### 2.2 Text-Only Feature Lists Without Screenshots

**Problem**: Features are presented as a bulleted list or text grid with no product visuals.
**Why it's wrong**: Evidence: 8/11 feature observations include product screenshots alongside text. Product pages exist to demonstrate the product visually. A text-only feature list belongs on a comparison table, not a feature showcase section.
**Correct approach**: Every feature card includes a product screenshot. The screenshot is the primary content element; text (heading + description) is secondary. Screenshot occupies ~60-65% of card height in grid layouts.
**Checklist item**: Does every feature in the primary feature section include a product screenshot?

---

### 2.3 Same CTA as Landing Page

**Problem**: Product page uses the same generic "Sign up" / "Get started" CTA without a demo option.
**Why it's wrong**: Evidence: 4/6 CTA observations on product pages include "Request a demo" or "Book a demo" alongside the self-serve option. Product page visitors have a different intent than Landing page visitors — they are evaluating specific capabilities and often need a guided demo, especially in B2B contexts.
**Correct approach**: Default to dual CTA: primary "Start free trial" (`.btn-dark`) + secondary "Request a demo" (`.btn-outline`). The demo option acknowledges that product page visitors may need sales assistance.
**Checklist item**: Does the CTA section include both a self-serve option and a demo/sales option?

---

### 2.4 Architecture Diagrams for Non-Platform Products

**Problem**: A feature-showcase SaaS product (Archetype A) includes an architecture diagram or system diagram section.
**Why it's wrong**: Evidence: architecture sections appear exclusively on infrastructure/platform products (Vercel, Cloudflare Workers, Shopify Commerce, Customer.io). Feature-showcase products (Figma, ClickUp, Grain) show the product, not its internals. Users of a task manager do not care about the backend architecture.
**Correct approach**: Archetype A and C should not include architecture sections. Archetype B (Platform Overview) should include them. If the user requests one for a non-platform product, steer toward a "How it works" process section instead (reuse `pages/landing-page/references/how-it-works.md`).
**Checklist item**: Is the architecture section present only for Archetype B (platform products)?

---

### 2.5 Too Many Use Case Segments

**Problem**: The use case section lists 8+ segments (industries or personas) in a flat grid.
**Why it's wrong**: Evidence: most common segment count is 3-4 (4/8 observations). Only 2/8 observations show 8+ segments (Heron AI 8, Shade 10), and both use accordion/interactive list patterns to compress them — not flat grids. A flat grid with 8+ segments is visually overwhelming and dilutes each segment.
**Correct approach**: 3-4 segments as cards. If the product serves 8+ segments, use a vertical list/accordion pattern (Shade, Heron AI) or show 3-4 primary segments with a "See all industries" link.
**Checklist item**: Does the use case section have 3-4 segments (or an accordion pattern for more)?

---

### 2.6 Fabricated Product Screenshots

**Problem**: Feature sections show invented UI that does not match the actual product.
**Why it's wrong**: Product page screenshots must represent the real product. Fabricated UI is deceptive and will be immediately recognized by users who try the product. Same principle as `shared/quality-checklist.md`: no fabricated metrics or testimonials.
**Correct approach**: Use actual product screenshots provided by the user. When screenshots are unavailable, use the Synthetic Product Visual recipe (surface-1 frame + structured inner panels) to communicate "screenshot goes here" without fabricating specific UI.
**Checklist item**: Are all product screenshots real (user-provided) or clearly marked as placeholders?

---

## 3. Structural Errors

### 3.1 Logo Wall as Integration Section

**Problem**: The integration section is just a logo grid (like a social proof logo wall) without descriptions or individual cards.
**Why it's wrong**: Evidence: 5/8 integration observations show individual cards with names and descriptions, not just logos. The integration section and the social proof logo wall serve different purposes: the logo wall says "trusted by these companies" (brand logos, grayscale, logo-wall opacity); the integration section says "connects with these tools" (tool logos, full detail, cards with descriptions).
**Correct approach**: Integration section uses cards: tool logo + name + 1-sentence description. 3-6 featured integrations. Full-color logos (not grayscale). Optional "View all integrations" link for the full directory.

```css
.integration-card {
    background: var(--surface-1);     /* #F5F5F5 light / #141414 dark */
    border-radius: 8px;               /* feature card radius */
    padding: 32px;                    /* card padding */
}

.integration-name {
    font-family: var(--font-display);
    font-size: 16px;                  /* body secondary scale */
    font-weight: 500;
    color: var(--text);
}

.integration-description {
    font-family: var(--font-body);
    font-size: 16px;                  /* body secondary scale */
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
}
```

**Checklist item**: Does the integration section use individual cards with descriptions (not a logo wall)?

---

### 3.2 Missing API/Developer CTA in Integration Section

**Problem**: The integration section shows third-party tool cards but has no "Build your own" or API section.
**Why it's wrong**: Evidence: 3/8 integration observations include a developer/API callout (Miro "Get started with API", Harvest "Build your own", Threads lists "Developer API" first). Platform products (Archetype B) should always include this; other archetypes should include it when the product has a public API.
**Correct approach**: Below the integration cards, add a simple row: heading ("Build your own integration" / "Developer API") + 1-sentence description + `.btn-outline` CTA ("View API docs" / "Get started with API").
**Checklist item**: Does the integration section include an API/developer CTA (required for Archetype B, recommended for others with public APIs)?

---

### 3.3 Alternating Section Background Colors

**Problem**: Sections alternate between white and gray backgrounds (hero white, features gray, use cases white, integrations gray).
**Why it's wrong**: `shared/visual-style.md` section 8: "Not allowed: different background colors for different sections." At most 1-2 sections use `var(--surface-1)`, the rest use `var(--bg)`.
**Correct approach**: Default all sections to `var(--bg)`. Optionally, 1 feature section or the architecture section can use `var(--surface-1)` as a full-width band. See `section-composition.md`.
**Checklist item**: Are at most 1-2 sections on `var(--surface-1)`, with the rest on `var(--bg)`?

---

## 4. When the User Provides a Brand Color

Adjustments when `--accent` is overridden with a brand color:

- **CTA button** changes from default (black/white) to the brand color via `var(--accent)` / `var(--accent-text)`. Standard `.btn-dark` behavior
- **1.2 does not relax**: No colored icon backgrounds, even in the brand color. The accent allowed-use list is exhaustive
- **1.3 does not relax**: Zero box-shadow, even for branded hover states
- **1.4 does not relax**: No colored section backgrounds, even in the brand color at low opacity
- **1.5 does not relax**: Headings stay DM Sans 500, not a brand serif
- **"Learn more" links**: May use `var(--accent)` on hover (allowed use in the exhaustive list)
- **Feature card screenshots**: Stay in `var(--surface-1)` frames, not brand-color-tinted frames
- **Integration logos**: Stay full-color (the tools' own logos), not recolored to the brand color
- **Chromatic area < 10%** does not relax. On a product page, the CTA buttons and optional link hovers are the primary chromatic elements

---

## 5. Verification Checklist

After generating the Product page, verify the following:

1. **Does every feature include a product screenshot?** No text-only feature cards in the primary grid
2. **Are screenshots actual product UI (or placeholders)?** No illustrations, no abstract graphics
3. **Does the CTA include a demo option?** Dual CTA: "Start free" + "Request a demo"
4. **Is the feature count per section 3-6?** No undifferentiated 10+ feature dumps
5. **Does any card use box-shadow?** If yes, remove it
6. **Are all headings in DM Sans at weight 500?** No serif, no italic, no weight 700
7. **Are at most 1-2 sections on `var(--surface-1)`?** No colored backgrounds
8. **Is the architecture section present only for Archetype B?** Not for feature-showcase products
9. **Does the integration section use cards with descriptions?** Not a logo wall
10. **Does the integration section include an API/developer CTA?** Required for Archetype B
11. **Is the use case segment count 3-4?** Or accordion for more
12. **Are all product screenshots real or clearly marked as placeholders?** No fabricated UI
13. **Is chromatic color area < 10%?** Only CTA buttons + optional link hover use `var(--accent)`
14. **Is the button border-radius 2px?** No pills (999px)
15. **Is the full site navigation present?** Missing nav = error
