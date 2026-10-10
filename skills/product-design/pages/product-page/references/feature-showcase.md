# Feature Showcase Patterns — Product Page

> Source: 11 feature deep-dive observations + 7 product showcase observations across Product pages (Better Stack, ClickUp, Sana, Figma, Plain, Mixpanel, Twenty, Deel, Rox, incident.io, Intercom, Runway, Grain). All tokens validated against `shared/visual-style.md`.

---

## How Product Page Features Differ from Landing Page Features

| Dimension | Landing Page Features | Product Page Features |
|-----------|----------------------|----------------------|
| Depth per feature | Brief: heading + 1-2 sentence description | Deeper: heading + description + "Learn more" link (5/11) or expandable detail (3/11) |
| Feature count | 3-6 per section | 3-6 per section (same range, but with links to dedicated sub-pages) |
| Visual content | Optional icon or illustration | Product screenshot is dominant (8/11 use actual UI screenshots) |
| Screenshot prominence | Supporting element | Primary element — occupies 60%+ of card height in grid patterns |
| "Learn more" links | Rare | Common (5/11) — linking to individual feature sub-pages |
| Category labels | Rare | Present in 2/11 (e.g., "ADOPTION", "ANALYSIS") for capability grouping |

**Key insight**: Landing page features answer "what does it do?" Product page features answer "how does it work?" — with screenshots as proof and links to go deeper.

---

## Pattern 1: Feature Grid with Screenshots (5/11 — most common)

**When to use**:
- 3-6 features of roughly equal importance
- Each feature has a product screenshot that demonstrates the capability
- Users need to quickly scan the product's feature set
- Archetype A (Feature Showcase) — this is the default pattern

**Execution**:
- 3-col grid (3-6 features) or 2-col grid (2-4 features)
- Each card: product screenshot above (~60% of card height) + heading + description + optional "Learn more" link
- Screenshots show actual product UI, not illustrations
- Optional category label above heading (label tokens)

```css
.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;                           /* list card gap */
    max-width: 1080px;                   /* main grid max-width */
    margin: 0 auto;
    padding: 0 32px;                     /* grid side padding */
}

.feature-grid-section {
    padding: 180px 0;                    /* section rhythm */
}

.feature-grid-section-header {
    text-align: center;
    margin-bottom: 58px;                /* heading to content */
}

@media (max-width: 767px) {
    .feature-grid {
        grid-template-columns: 1fr;
        padding: 0 20px;                /* narrow: 32px -> 20px */
    }

    .feature-grid-section {
        padding: 96px 0;                /* narrow: 180px -> 96px */
    }

    .feature-grid-section-header {
        margin-bottom: 40px;            /* narrow: 58px -> 40px */
    }
}
```

**Feature card tokens**:
```css
.feature-card {
    background: var(--surface-1);
    border-radius: 8px;                 /* feature card radius */
    padding: 32px;                      /* card internal padding */
    /* zero shadow */
}

.feature-card-screenshot {
    width: 100%;
    border-radius: 16px;               /* content card radius for screenshot frame */
    background: var(--bg);             /* inside surface-1 parent → use --bg for contrast */
    margin-bottom: 24px;
}

.feature-card-label {
    font-family: var(--font-mono);
    font-size: 12px;                    /* label scale */
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;                       /* label opacity */
    margin-bottom: 8px;
}

.feature-card-heading {
    font-family: var(--font-display);
    font-size: 20px;                    /* card heading scale */
    font-weight: 500;
    letter-spacing: -0.4px;
    line-height: 1.3;
    color: var(--text);
    margin-bottom: 8px;
}

.feature-card-description {
    font-family: var(--font-body);
    font-size: 16px;                    /* body secondary scale */
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;                       /* subtitle/description opacity */
}

.feature-card-link {
    font-family: var(--font-display);
    font-size: 14px;                    /* button/nav scale */
    font-weight: 500;
    color: var(--text);
    text-decoration: none;
    margin-top: 16px;
    display: inline-block;
}
.feature-card-link::after {
    content: ' \2192';                  /* right arrow */
}
.feature-card-link:hover {
    opacity: 0.7;
}
```

**Section heading tokens**:
```css
.feature-section-heading {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px); /* section heading scale */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
}

.feature-section-subtitle {
    font-family: var(--font-body);
    font-size: 18px;                    /* body text scale */
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    max-width: 540px;                   /* subtitle max-width */
    margin: 24px auto 0;
}
```

**Variants**:
- **2-col grid** (Mixpanel, Deel): Use when features are fewer (2-4) or each needs more horizontal space. Change `grid-template-columns` to `repeat(2, 1fr)`
- **With category labels** (Mixpanel): Each card has an uppercase mono label above the heading ("ADOPTION", "ANALYSIS"). Use when features are grouped by capability area
- **Minimal / no card background** (Plain): Cards have no background, no border — just screenshot + text on the page background. Use for an extremely clean aesthetic. Remove `background: var(--surface-1)` from `.feature-card`

**When not to use**:
- Features require interactive exploration (accordion/tab pattern is better)
- One feature is dramatically more important than the others (single full-width showcase is better)
- 7+ features need to be shown (carousel or progressive disclosure is better)

**Evidence**: Better Stack (6 cards, 3-col, dark), Plain (6 cards, 3-col, minimal), Twenty (3 cards, 3-col), Mixpanel (2 cards, 2-col with labels), Deel (2 cards, 2-col with illustrations)
**Evidence status**: Cross-sample inference

---

## Pattern 2: Accordion/Tab + Screenshot (3/11)

**When to use**:
- 3-6 features where each has a different product screenshot to show
- Interactive exploration is desirable — user selects a feature, screenshot updates
- Space-efficient alternative to showing all features at once
- Archetype C (Product Deep-Dive) — this is the recommended pattern

**Execution**:
- 2-col split: text/accordion left (~40-45%), product screenshot right (~55-60%)
- Section heading above the split
- Left column: stacked accordion items, one expanded at a time
- Right column: product screenshot that corresponds to the expanded feature
- Expanded item shows: heading + description paragraph + optional "Learn more" link
- Collapsed items show heading only, with expand/collapse indicator

```css
.accordion-showcase {
    display: grid;
    grid-template-columns: 5fr 7fr;    /* ~42% text, ~58% screenshot */
    gap: 58px;                          /* heading-to-content gap */
    align-items: start;
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
}

@media (max-width: 767px) {
    .accordion-showcase {
        grid-template-columns: 1fr;
        gap: 40px;                      /* narrow: 58px -> 40px */
        padding: 0 20px;
    }
}
```

**Accordion item tokens**:
```css
.accordion-item {
    border-bottom: 1px solid var(--surface-2);
    padding: 16px 0;
    cursor: pointer;
}

.accordion-item-heading {
    font-family: var(--font-display);
    font-size: 16px;                    /* body secondary scale */
    font-weight: 500;
    color: var(--text);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.accordion-item-icon {
    font-family: var(--font-display);
    font-size: 14px;
    color: var(--text);
    opacity: 0.4;                       /* auxiliary opacity */
    transition: opacity 0.3s linear;
}
/* Use + / - characters or a chevron. Do not use colored icons. */

.accordion-item-body {
    font-family: var(--font-body);
    font-size: 16px;                    /* body secondary scale */
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    padding-top: 12px;
    display: none;                      /* hidden when collapsed */
}

.accordion-item.active .accordion-item-body {
    display: block;
}

.accordion-item-link {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    text-decoration: none;
    margin-top: 12px;
    display: inline-block;
}
.accordion-item-link::after { content: ' \2192'; }
```

**Screenshot panel tokens**:
```css
.accordion-screenshot {
    background: var(--surface-1);
    border-radius: 16px;               /* content card radius */
    overflow: hidden;
}

.accordion-screenshot img {
    width: 100%;
    display: block;
}
```

**JavaScript**: The accordion is implemented in vanilla JS. Clicking an accordion item expands it (shows `.accordion-item-body`, toggles `.active` class) and collapses the previously expanded item. Optionally, the right-side screenshot source updates to match the selected feature. No framework required.

**Variants**:
- **Stacked feature list** (incident.io): Instead of accordion expand/collapse, all features are visible simultaneously as a stacked list with icon + heading + description. The screenshot on the right may be static or may highlight on hover. Use when 3 features need equal visibility without interaction
- **Tab bar instead of accordion** (Figma): Horizontal tab bar above the screenshot, each tab is a feature name. Functionally similar to accordion but uses horizontal space. Use when feature names are short (1-2 words)

**When not to use**:
- 7+ features (accordion list becomes too long)
- No product screenshots available to differentiate features
- Features are of unequal importance (grid with size variation is better)

**Evidence**: Rox (6 features, accordion, dark), Intercom (3 features, accordion, light blue bg), incident.io (3 features, stacked list, dark)
**Evidence status**: Cross-sample inference

---

## Pattern 3: Carousel (2/11)

**When to use**:
- 5+ features that each deserve a full card with screenshot
- Horizontal browsing is appropriate (users explore features sequentially)
- Archetype A (Feature Showcase) with a large feature set

**Execution**:
- Horizontal scrolling carousel of feature cards
- Each card: large product screenshot + heading + description + "Learn more" link
- Navigation: left/right arrows + optional counter ("1/4") or pagination dots
- Cards peek from edges to signal scrollability
- Section heading above the carousel

**Card tokens follow Pattern 1** (feature card with screenshot). The carousel wrapper adds:

```css
.feature-carousel {
    display: flex;
    gap: 24px;                          /* list card gap */
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    -webkit-overflow-scrolling: touch;
    padding-bottom: 16px;              /* space for scrollbar if visible */
}

.feature-carousel-card {
    flex: 0 0 calc(33.333% - 16px);    /* 3 cards visible */
    scroll-snap-align: start;
    background: var(--surface-1);
    border-radius: 8px;                /* feature card radius */
    padding: 32px;                     /* card internal padding */
}

@media (max-width: 767px) {
    .feature-carousel-card {
        flex: 0 0 85%;                 /* single card visible on narrow */
        padding: 24px;                 /* narrow: 32px -> 24px */
    }
}
```

**Navigation tokens**:
```css
.carousel-nav {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 24px;
}

.carousel-counter {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    color: var(--text);
    opacity: 0.4;
}

.carousel-arrow {
    width: 32px;
    height: 32px;
    border: 1px solid var(--surface-2);
    border-radius: 2px;                /* button radius */
    background: transparent;
    color: var(--text);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    transition: border-color 0.3s linear;
}
.carousel-arrow:hover { border-color: var(--text); }
```

**When not to use**:
- 3 or fewer features (grid is simpler and shows everything at once)
- Each feature requires deep explanatory text (accordion is better)
- The page already has another carousel section (avoid carousel fatigue)

**Evidence**: ClickUp (7+ features, scrollable cards, pagination dots), Figma (4 features, counter "1/4", arrows)
**Evidence status**: Cross-sample inference — smaller sample (2/11), but pattern is well-established in product design

---

## Pattern 4: Single Full-Width Visual (1/11)

**When to use**:
- One product interface IS the feature — no additional explanation needed
- The product's visual complexity (dashboards, data views) communicates value better than text
- Archetype C (Product Deep-Dive) with a single standout feature

**Execution**:
- Single large product screenshot or video, occupying 80-100% of content width
- Minimal text: optional heading above, optional caption below
- Play button overlay if video
- The product UI tells the story — text serves as caption, not selling point

```css
.full-width-showcase {
    max-width: 1080px;
    margin: 0 auto;
    padding: 180px 32px;               /* section rhythm + side padding */
}

.full-width-showcase-visual {
    width: 100%;
    border-radius: 16px;              /* content card radius */
    background: var(--surface-1);
    overflow: hidden;
}

.full-width-showcase-caption {
    font-family: var(--font-body);
    font-size: 16px;                   /* body secondary */
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    text-align: center;
    max-width: 540px;
    margin: 24px auto 0;
}
```

**When not to use**:
- Multiple features of equal importance need representation
- The product UI is not visually impressive on its own
- A text explanation is necessary for users to understand the screenshot

**Evidence**: Sana (single analytics dashboard, play button, caption below)
**Evidence status**: Single observation — weakest evidence. Use only when the product visual is genuinely compelling.

---

## Screenshot Presentation Decisions

Based on 7 product showcase observations, the primary decision is how to **frame** screenshots:

| Frame type | When to use | Implementation |
|-----------|-------------|----------------|
| **Contained in card** (default) | Most cases | `background: var(--surface-1); border-radius: 16px; overflow: hidden` |
| **Browser chrome** | SaaS tools that run in a browser | Add 3 dots (8px circles in surface-2) at top-left inside a surface-2 title bar |
| **Flat/frameless** | Minimal aesthetic, screenshot edges blend with page | `border-radius: 16px` only, no background |

**Default**: Use "Contained in card" unless there is a specific reason to choose another option.

**Screenshot content**: Always show actual product UI with realistic data. Screenshots with empty states, placeholder text, or obviously fake data undermine credibility. Per visual-style.md design philosophy: "Content as decoration — Product screenshots/output serve as hero visuals and brand texture."
