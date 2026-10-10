# About Page — Section Composition

> Source: ~53 section observations across ~41 unique products. All spacing/color tokens validated against `shared/visual-style.md`.

---

## Default Section Order by Archetype

### A. Company Story (6-8 sections)

```
Nav
Hero (mission statement, text-only)
Story / Origin (founding narrative, 2-4 paragraphs)
Team (leadership grid, 3-4 columns)
Stats (4-stat horizontal row)
Values (3-5 values, list or definition list)
CTA (careers: "Join the team")
Footer
```

**Optional additions** (insert at marked positions):
- Timeline: after Story, before Team (only when 5+ milestones exist)
- Investor logos: after Stats, before Values (only when notable investors exist)

### B. Team-First (4-5 sections)

```
Nav
Hero (brief statement or "Who we are")
Team (full team grid, dominant section)
Values (brief, 3-4 items, inline or simple list)
CTA (careers or contact)
Footer
```

**Omit**: Story, Timeline, Stats, Investor logos. The team IS the story.

### C. Mission-Driven (5-7 sections)

```
Nav
Hero (belief/principle statement)
Values / Principles (dominant, 4-5 items with descriptions)
Stats (4-stat row, grounds the mission in evidence)
Team (leadership grid, secondary)
CTA (careers, framed as mission invitation)
Footer
```

**Optional additions**:
- Investor logos: after Stats, before Team
- Timeline: skip unless the company's history IS the mission story

---

## Section Rhythm and Spacing

All spacing values from `shared/visual-style.md` section 3.

### Section Padding

```css
.section {
    padding: 180px 0;                 /* section rhythm baseline */
}

.about-hero {
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
        padding: 96px 0;              /* 180px → 96px */
    }
    .about-hero {
        padding-top: 80px;            /* 128px → 80px */
        padding-bottom: 96px;         /* 180px → 96px */
    }
    .section-heading {
        margin-bottom: 40px;          /* 58px → 40px */
    }
    .container {
        padding: 0 20px;              /* 32px → 20px */
    }
}
```

---

## Background Alternation Rules

The About page follows the same background rules as all page types (`shared/visual-style.md` section 8).

| Section | Background | Rationale |
|---------|-----------|-----------|
| Hero | `var(--bg)` | Always page background |
| Story / Origin | `var(--bg)` | Default |
| Team | `var(--bg)` | Default |
| Stats | `var(--surface-1)` (optional) | Full-width band to visually separate stats from surrounding text sections. 2/5 stats observations use a differentiated background (both Intercom variants, using brand blue — not system surface-1; system surface-1 is the recommended alternative) |
| Values | `var(--bg)` | Default |
| Timeline | `var(--bg)` | Default |
| CTA | `var(--bg)` or dark band via `class="section-dark"` | Dark band: add `class="section-dark"` to the `<section>` — this sets `background: var(--text)` and inverts button/text colors automatically (see `shared/visual-style.md §8`). Without the class, buttons remain `var(--text)` on `var(--text)` and are invisible |
| Investor logos | `var(--bg)` | Same as Landing logo wall |

**Rules**:
- At most 1-2 sections use `var(--surface-1)` background. The rest use `var(--bg)`
- No colored backgrounds, no gradients, no photographic backgrounds
- All neutral colors must be pure achromatic (zero hue shift)

---

## Nav and Footer

Reuse shared components without modification:
- **Navigation**: `shared/navigation.md` + `sections/navigation/SKILL.md`
- **Footer**: `shared/footer.md` + `sections/footer/SKILL.md`

Nav height is `68px` (`var(--nav-h)`). When using `position: fixed`, add `body { padding-top: var(--nav-h); }` to prevent the hero heading from sitting under the nav.

---

## CTA Section

About page CTAs are fundamentally different from Landing page CTAs.

**Evidence**: 5/6 CTA observations link to careers ("Join the team" / "Open positions"). 0/6 link to product signup or trial. 1/6 links to multiple destinations (Customer.io: Sales + Press + Careers).

### Default: Careers CTA

**Heading**: "Join the team" / "Join us" / "Work with us" / "We're hiring"
**Body**: 1-2 sentences about the company culture or open roles
**Button**: `.btn-dark` linking to careers page — "See open positions" / "View careers"

### Alternative: Multi-Destination CTA

**When to use**: Large companies with distinct audience segments (customers, press, candidates). Evidence: Customer.io uses a 3-card grid with Sales + Press + Careers.

**Implementation**: 3-column grid, each card has a heading + brief description + `.btn-outline` button. No icons (the system does not use icon backgrounds).

### What NOT to do

- Do NOT use product conversion CTAs ("Start free trial", "Get started", "Sign up") on the About page
- Do NOT replicate the Landing page CTA section verbatim
- About page CTA is an invitation, not a conversion funnel

---

## Story / Origin Section

**When to include**: Archetype A (required), Archetype C (optional). Skip for Archetype B.

### Layout

Two-column (text occupies ~60-70% width) or single-column centered text.

**Content**: 2-4 paragraphs of founding narrative. Include: founding year, the problem that inspired the product, how the team grew, where the company is today.

```css
.story-section {
    padding: 180px 0;
}

.story-content {
    max-width: 720px;                 /* slightly wider than subtitle 540px, narrower than full grid 1080px */
}

.story-heading {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);   /* section heading scale */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
    margin-bottom: 58px;              /* heading-to-content */
}

.story-text {
    font-family: var(--font-body);
    font-size: 18px;
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;                     /* subtitle/description tier */
}

.story-text p + p {
    margin-top: 24px;                 /* paragraph spacing */
}
```

### Optional: Label Above Heading

"OUR STORY" / "HOW IT STARTED" — uses the standard `.label` token.

---

## Investor / Partner Logo Wall

**When to include**: Archetype A and C, only when notable investors exist.

Reuse the Landing page social proof logo wall pattern from `pages/landing-page/references/social-proof.md`. Same implementation: flex row, `58px` gap, logo text at `16px` / `opacity: 0.15`.

**Heading options**: "Backed by" (Webflow pattern) / "Our investors" / "Supported by"

---

## Total Page Length by Archetype

| Archetype | Section count | Relative length |
|-----------|--------------|-----------------|
| A. Company Story | 6-8 | Longest |
| B. Team-First | 4-5 | Shortest |
| C. Mission-Driven | 5-7 | Medium |

### Narrow Screen Behavior

All sections stack naturally in a single column. No section reordering is needed on narrow screens. The only adjustments are the spacing reductions defined in the narrow screen table above.

Grid-based sections (team grid, stats row) collapse to fewer columns:
- 4-column team grid: 2 columns on narrow screen
- 3-column team grid: 2 columns on narrow screen (last item full-width)
- 4-stat row: 2x2 grid on narrow screen
