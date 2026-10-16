# Use Cases / "Who It's For" Patterns — Product Page

> Source: 8 use-case section observations across Product pages (Slash, Heron AI, Mora, Shade, Intercom, Grain, Ploy, Vizcom). All tokens validated against `shared/visual-style.md`.

---

## Segmentation Axes

The first decision is **what axis** to segment by. This fundamentally changes the section's purpose:

| Axis | Frequency | Purpose | Example |
|------|-----------|---------|---------|
| **Industry** | 4/8 | Target vertical expansion ("we serve your industry") | Slash, Shade, Vizcom, Heron AI |
| **Persona / Role** | 2/8 | Target horizontal adoption within a company ("your team uses us") | Mora, Grain |
| **Company size** | 1/8 | Target by organizational maturity ("we scale with you") | Ploy |
| **Multi-axis** | 1/8 | Comprehensive solution framing (use cases + industries + company size) | Intercom |

**Default recommendation**: Choose persona/role when the product serves multiple departments within one company. Choose industry when the product adapts to domain-specific workflows. Do not combine multiple axes in the same section — Intercom does this in a navigation dropdown, not a page section.

---

## Pattern 1: Card Grid (3/8 — most common)

**When to use**:
- 3-4 segments of equal importance
- Each segment can be explained with a heading + short description
- No need for deep detail per segment
- All three archetypes — this is the default pattern

**Execution**:
- 3-col or 4-col grid depending on segment count
- Each card: optional icon + heading + description + optional "Learn more" link
- Section heading centered above
- Optional label above heading only when it adds information (an audience such as "FOR FINANCE TEAMS"), never the section type name ("USE CASES"); at most 2 labels per page (`shared/copy.md` §5)

```css
.use-case-section {
    padding: 180px 0;                   /* section rhythm */
}

.use-case-header {
    text-align: center;
    margin-bottom: 58px;               /* heading to content */
}

.use-case-label {
    font-family: var(--font-mono);
    font-size: 12px;                    /* label scale */
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;                       /* label opacity */
    margin-bottom: 16px;
}

.use-case-heading {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px); /* section heading scale */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
}

.use-case-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;                          /* list card gap */
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;                    /* grid side padding */
}

@media (max-width: 767px) {
    .use-case-section {
        padding: 96px 0;               /* narrow: 180px -> 96px */
    }

    .use-case-header {
        margin-bottom: 40px;           /* narrow: 58px -> 40px */
    }

    .use-case-grid {
        grid-template-columns: 1fr;
        padding: 0 20px;               /* narrow: 32px -> 20px */
    }
}
```

**Use case card tokens** (two variants):

**Variant A: Minimal text-only (Mora pattern — default)**
```css
.use-case-card {
    /* No background, no border, no shadow — text only */
    padding: 0;
}

.use-case-card-heading {
    font-family: var(--font-display);
    font-size: 20px;                    /* card heading scale */
    font-weight: 500;
    letter-spacing: -0.4px;
    line-height: 1.3;
    color: var(--text);
    margin-bottom: 8px;
}

.use-case-card-description {
    font-family: var(--font-body);
    font-size: 16px;                    /* body secondary scale */
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;                       /* description opacity */
}

.use-case-card-link {
    font-family: var(--font-display);
    font-size: 14px;                    /* button/nav scale */
    font-weight: 500;
    color: var(--text);
    text-decoration: none;
    margin-top: 16px;
    display: inline-block;
}
.use-case-card-link::after { content: ' \2192'; }
.use-case-card-link:hover { opacity: 0.7; }
```

**Variant B: Card with background (when visual differentiation is needed)**
```css
.use-case-card-filled {
    background: var(--surface-1);
    border-radius: 8px;                /* feature card radius */
    padding: 32px;                     /* card internal padding */
    /* zero shadow */
}
```

**Choosing between Variant A and B**: Use Variant A (text-only) as the default — it is cleaner and matches more observations (Mora, Vizcom). Use Variant B only when the section needs visual weight to stand out from adjacent text-heavy sections, or when cards contain optional icons.

**Optional icon**: If using an icon per use case, keep it a small line-art icon with no colored background. Per visual-style.md: icon backgrounds and badge fills are forbidden for `--accent`. Icons should be 24px, matching `var(--text)` color at opacity 0.4.

**Variants**:
- **4-col grid** (Grain, Slash): Use when there are exactly 4 segments and headings are short. Change `grid-template-columns` to `repeat(4, 1fr)`. 4-col collapses to 2-col at 767px
- **With "Learn More" links** (Grain): Each card includes a link to a dedicated use-case page. Use when detailed per-segment content exists

**When not to use**:
- 5+ segments (too many cards; use accordion instead)
- Segments require deep explanation or expanded detail (use Pattern 2)
- Segments require a visual/photo per item (use photography cards, not covered in V1 due to "content as decoration" principle)

**Evidence**: Mora (3 personas, minimal), Grain (4 personas, icons), Slash (4 industries, photos — photography element excluded per design philosophy)
**Evidence status**: Cross-sample inference

---

## Pattern 2: Accordion / Interactive List (3/8)

**When to use**:
- 5+ segments that would overcrowd a grid
- Each segment has expanded detail (description, feature list, or dedicated CTA)
- Interactive exploration is desirable — user selects a segment to see detail
- Archetype B (Platform Overview) with multiple industries or personas

**Execution**:
- 2-col split: heading + accordion list (left ~45-55%), visual element (right ~45-55%)
- Or: full-width accordion list with no visual companion
- One item expanded at a time, showing description + optional CTA
- Collapsed items show name only

```css
.use-case-accordion-section {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 58px;                          /* heading-to-content gap */
    align-items: start;
    max-width: 1080px;
    margin: 0 auto;
    padding: 180px 32px;               /* section rhythm + side padding */
}

@media (max-width: 767px) {
    .use-case-accordion-section {
        grid-template-columns: 1fr;
        gap: 40px;                      /* narrow: 58px -> 40px */
        padding: 96px 20px;            /* narrow adjustments */
    }
}
```

**Accordion item tokens**:
```css
.use-case-accordion-item {
    border-bottom: 1px solid var(--surface-2);
    padding: 16px 0;
    cursor: pointer;
}

.use-case-accordion-name {
    font-family: var(--font-display);
    font-size: 16px;                    /* body secondary scale */
    font-weight: 500;
    color: var(--text);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.use-case-accordion-expand {
    font-size: 14px;
    color: var(--text);
    opacity: 0.4;                       /* auxiliary opacity */
}
/* Expand icon: use + / - characters. Do not use colored icons. */

.use-case-accordion-detail {
    font-family: var(--font-body);
    font-size: 16px;
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    padding-top: 12px;
    display: none;
}

.use-case-accordion-item.active .use-case-accordion-detail {
    display: block;
}
```

**JavaScript**: Vanilla JS. Clicking an item toggles `.active`, expanding its detail and collapsing the previously active item. If a right-side visual is present, update its content (image source or highlighted state) to match the selected segment. No framework required.

**Variants**:
- **Oversized typography list** (Vizcom): Segment names displayed at large scale (section heading scale or larger) with reduced opacity (0.3-0.4), stacked vertically. No descriptions, no expansion — a typographic "claim" of industry coverage. Use for bold/editorial aesthetic when no detail is needed per segment
- **With CTA per segment** (Ploy): Expanded detail includes a CTA button ("Explore Enterprise" .btn-dark + "Book a demo" .btn-outline). Use when each segment has its own dedicated landing page or sales path
- **Full-width list** (no visual companion): Section heading above, full-width accordion below. Use when no per-segment visual content exists

**When not to use**:
- 3 segments or fewer (grid is simpler)
- All segments need equal visibility simultaneously (grid shows everything at once)
- The page already has another accordion section (e.g., FAQ) — avoid pattern repetition

**Evidence**: Heron AI (8 personas, accordion, editorial), Shade (10 industries, interactive list + photo), Ploy (3 company sizes, expandable cards with CTAs)
**Evidence status**: Cross-sample inference

---

## Segment Count Guidelines

| Segment count | Recommended pattern | Rationale |
|---------------|--------------------|-----------|
| 2 | Do not use a dedicated section | Too few to justify a section; mention in hero or features instead |
| 3-4 | Card grid (Pattern 1) | Clean, scannable, no interaction needed |
| 5-7 | Accordion / interactive list (Pattern 2) | Grid becomes crowded; accordion compresses space |
| 8+ | Accordion required (Pattern 2) | Grid at 8+ items overwhelms the user; progressive disclosure is necessary |

**Most common count observed: 3-4 segments** (4/8 samples). When in doubt, start with 3 well-differentiated segments rather than exhaustively listing every possible audience.

---

## Content Fabrication Warning

Use case sections carry high content fabrication risk. Do NOT invent:
- Industry names the product does not actually serve
- Persona descriptions not provided by the user
- Specific ROI claims or statistics per segment

When user-provided content is insufficient, use placeholder labels (e.g., "[Industry 1]", "[Persona 1]") or omit the section entirely. A missing section is better than a fabricated one.
