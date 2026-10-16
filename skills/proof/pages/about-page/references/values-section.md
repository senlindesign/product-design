# Values Section — Principles and Beliefs Display

> Source: Mobbin research synthesis from 8 values/mission/principles observations across Toggl Track, Mews, Grain, Attio, Wispr Flow, Webflow, Serus, Vanta.

---

## Default Pattern: Numbered List with Horizontal Rules

No single layout dominates for values sections (the most visually diverse section type). The numbered list with horizontal rules (2/8 samples: Mews, Webflow) is the recommended default because it gives values a sense of priority, works with 3-5 items without visual clutter, and aligns with the design system's text-first, zero-decoration principles.

### Section Heading + Intro

```css
.values-heading {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);   /* section heading — type scale */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
    margin-bottom: 24px;                  /* heading to intro text */
}

.values-intro {
    font-family: var(--font-body);
    font-size: 18px;                      /* body — type scale */
    font-weight: 400;
    color: var(--text);
    opacity: 0.5;                         /* subtitle hierarchy */
    line-height: 1.6;
    max-width: 540px;                     /* subtitle measure — grid system */
    margin-bottom: 58px;                  /* heading-to-content — spacing system */
}
```

Common heading text: "Our Values", "What We Believe", "Core Values", "Principles". Framing varies — "Constitution" (Mews), "Behaviors" (Webflow), "Principles" (Vanta) carry different connotations. Choose based on brand tone.

### Numbered List Implementation (Default)

```css
.values-list {
    max-width: 1080px;                    /* system grid max-width */
    margin: 0 auto;
    padding: 0 32px;                      /* system side padding */
}

.value-item {
    display: grid;
    grid-template-columns: 48px 1fr;      /* number column + content */
    gap: 24px;                            /* grid gutter */
    padding: 32px 0;                      /* card padding for vertical rhythm */
    border-bottom: 1px solid var(--surface-2);  /* horizontal rule separator */
}

.value-item:first-child {
    border-top: 1px solid var(--surface-2);
}

.value-number {
    font-family: var(--font-mono);
    font-size: 12px;                      /* label — type scale */
    font-weight: 400;
    letter-spacing: 0.72px;
    color: var(--text);
    opacity: 0.4;                         /* label opacity */
    padding-top: 6px;                     /* align with title baseline */
}

.value-title {
    font-family: var(--font-display);
    font-size: 20px;                      /* card heading — type scale */
    font-weight: 500;
    letter-spacing: -0.4px;
    line-height: 1.3;
    color: var(--text);
    margin-bottom: 8px;                   /* spacing scale */
}

.value-description {
    font-family: var(--font-body);
    font-size: 16px;                      /* body secondary size */
    font-weight: 400;                     /* body paragraph weight */
    color: var(--text);
    opacity: 0.5;                         /* subtitle hierarchy */
    line-height: 1.6;
}
```

**HTML structure**:
```html
<div class="values-list">
    <div class="value-item">
        <span class="value-number">01</span>
        <div>
            <h3 class="value-title">Value Name</h3>
            <p class="value-description">One to two sentences explaining what this value means in practice.</p>
        </div>
    </div>
    <!-- repeat for each value -->
</div>
```

### Value Count

- **3-5 values recommended** (observed sweet spot)
- 3 values: minimal, focused (1/8: Grain)
- 4-5 values: most common (4/8 samples with countable values)
- More than 6: risks diluting impact — consider consolidation

---

## Layout Variants

### Variant A: Numbered List with Rules (default, described above)

**When to use**: Default choice. Works for any About page archetype. Gives values sequential weight and scannability.

### Variant B: Definition List — Title Left, Description Right (1/8: Attio)

**When to use**: When values have longer descriptions (2-3 sentences) and a two-column layout suits the page rhythm. Works well when the surrounding layout is also two-column.

```css
.value-item--definition {
    display: grid;
    grid-template-columns: 1fr 2fr;       /* ~33% title, ~66% description */
    gap: 24px;                             /* grid gutter */
    padding: 32px 0;                       /* card padding */
    border-bottom: 1px solid var(--surface-2);
}

.value-item--definition .value-title {
    font-family: var(--font-display);
    font-size: 20px;                       /* card heading — type scale */
    font-weight: 500;
    letter-spacing: -0.4px;
    line-height: 1.3;
    color: var(--text);
}

.value-item--definition .value-description {
    font-family: var(--font-body);
    font-size: 16px;                       /* body secondary size */
    font-weight: 400;
    color: var(--text);
    opacity: 0.5;
    line-height: 1.6;
}
```

### Variant C: 3-Column Grid (1/8: Grain)

**When to use**: When values are short (title only, no descriptions) and 3 values. The most compact layout.

```css
.values-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;                             /* grid gutter */
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
    text-align: center;
}

.values-grid .value-title {
    font-family: var(--font-display);
    font-size: 20px;                       /* card heading — type scale */
    font-weight: 500;
    letter-spacing: -0.4px;
    line-height: 1.3;
    color: var(--text);
}
```

Do not add icons to the grid variant. Icons were present in only 2/8 samples, and the design system prohibits colored circular/square backgrounds behind icons. If icons are used at all, they must be simple outlined shapes with no background fill.

### Variant D: Stacked Cards (1/8: Serus)

**When to use**: When each value has extended content (2-3 paragraphs). Rare — use only for manifesto-style brand pages.

```css
.value-card {
    padding: 32px;                         /* card padding — spacing system */
    background: var(--surface-1);          /* card bg */
    border-radius: 8px;                    /* feature card — radius system */
    /* zero shadow */
}

.value-card + .value-card {
    margin-top: 24px;                      /* card gap — list variant */
}
```

---

## Number/Index Styling

**Numbered format (recommended)**:

Use zero-padded two-digit numbers: `01`, `02`, `03`, etc. Rendered in the mono label style.

```css
.value-number {
    font-family: var(--font-mono);
    font-size: 12px;                       /* label — type scale */
    font-weight: 400;
    letter-spacing: 0.72px;
    color: var(--text);
    opacity: 0.4;                          /* label opacity */
}
```

Number position options:
- Left column, top-aligned (default — as in the numbered list implementation)
- Right-aligned within the left column (Mews pattern: `/ 01`, `/ 02`)

**No numbers**: acceptable for the definition list and grid variants, where the sequential order matters less.

---

## Icon Usage

Icons are uncommon in values sections (only 2/8 samples used them). When used:

- Small, outlined style — no filled shapes, no colored backgrounds
- Placed above the value title, not inline
- Must not use `var(--accent)` as icon fill or background (visual-style.md prohibition)
- If used, keep icon size to 24px or smaller, with no container background

**Recommendation**: Omit icons for the default implementation. The numbered list format provides sufficient visual structure without decoration.

---

## Narrow Screen (< 768px)

```css
@media (max-width: 767px) {
    .values-heading {
        margin-bottom: 16px;
    }

    .values-intro {
        margin-bottom: 40px;              /* heading-to-content narrow */
    }

    .value-item {
        grid-template-columns: 32px 1fr;
        gap: 16px;
        padding: 24px 0;                  /* card padding narrow */
    }

    .value-item--definition {
        grid-template-columns: 1fr;       /* stack title above description */
        gap: 8px;
    }

    .values-grid {
        grid-template-columns: 1fr;
        text-align: left;
        padding: 0 20px;                  /* narrow side padding */
    }

    .values-list {
        padding: 0 20px;                  /* narrow side padding */
    }
}
```

---

## When NOT to Use

- Do not use radial/circular layouts (Wispr Flow pattern) — requires SVG or absolute positioning, not responsive, not system-aligned
- Do not use colored value cards or accent-colored headings — violates accent color rules
- Do not fabricate values — use placeholder text like "Value statement to be provided" if real content is unavailable
- Do not use more than 6 values — diminishes impact; if the brand has many, consolidate the most important 4-5
- Do not add box-shadow to value cards — zero shadows (design system rule)
- Do not use italic for emphasis within value descriptions — the system uses font family switching, not style variation, for hierarchy
