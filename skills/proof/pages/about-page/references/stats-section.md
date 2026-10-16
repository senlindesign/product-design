# Stats Section — Company Numbers and Metrics

> Source: Mobbin research synthesis from 5 unique stats observations (6 screenshots) across Intercom (2 variants), Webflow, Customer.io, Deel.

---

## Default Pattern: Horizontal Row, 3-4 Stats

The horizontal row is the dominant layout (3/5 samples). Stats are large, text-only numbers meant to impress at a glance. Icons are uncommon (1/5: Deel) — the majority are pure number + label.

### Section Heading (Optional)

A heading is not always present above stats. When used:

```css
.stats-heading {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);   /* section heading — type scale */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
    margin-bottom: 58px;                  /* heading-to-content — spacing system */
}
```

Common heading text: "By the Numbers" (Webflow), or none — stats often stand alone as a visual break between narrative sections.

---

## Stats Row Implementation

```css
.stats-row {
    display: flex;
    justify-content: space-between;
    max-width: 1080px;                    /* system grid max-width */
    margin: 0 auto;
    padding: 0 32px;                      /* system side padding */
    text-align: center;
}

.stat-item {
    flex: 1;
}

.stat-number {
    font-family: var(--font-display);
    font-size: clamp(36px, 5vw, 56px);   /* page-specific: between section heading and hero heading */
    font-weight: 500;
    letter-spacing: -0.02em;              /* system negative tracking rule */
    line-height: 1.1;
    color: var(--text);
}

.stat-label {
    font-family: var(--font-display);
    font-size: 14px;                      /* button/nav — type scale */
    font-weight: 500;
    color: var(--text);
    opacity: 0.5;                         /* subtitle hierarchy */
    margin-top: 8px;                      /* spacing scale */
}
```

**HTML structure**:
```html
<div class="stats-row">
    <div class="stat-item">
        <div class="stat-number">600+</div>
        <div class="stat-label">Team members</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">2013</div>
        <div class="stat-label">Year founded</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">3.5M+</div>
        <div class="stat-label">Users</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">35</div>
        <div class="stat-label">Countries</div>
    </div>
</div>
```

---

## Stat Count

- **3 stats**: acceptable minimum (1/5: Intercom row)
- **4 stats**: most common (3/5: Webflow, Customer.io, Deel) — recommended default
- **More than 5**: risks visual crowding in a single row — consider a 2x2 grid instead

---

## Recommended Stat Categories

A consistent pattern emerges across observations (most common categories):

| Category | Frequency | Example formats |
|----------|-----------|----------------|
| Team size / employees | 4/5 | "600+", "2,200", "900+" |
| Year founded | 3/5 | "2013", "2019", "2011" |
| Customers / users | 3/5 | "25k+", "3.5M+", "7,600+" |
| Geography (countries/offices) | 2/5 | "35 Countries", "88 Countries", "5 Offices" |
| Funding / valuation | 2/5 | "$335M", "$12B" |

The 4-item set of **team size + year founded + customer count + geography** covers "how big, how old, how many customers, how global" — a complete company snapshot.

Do not fabricate statistics. Use placeholder values like "XX+" with a note if real numbers are unavailable.

---

## Number Formatting

- Use `+` suffix for growing metrics: "600+", "25k+"
- Use `k` / `M` / `B` abbreviations for large numbers: "3.5M+", "$12B"
- Use `$` prefix for monetary values: "$335M"
- Year values are plain four-digit numbers: "2013"
- Use multiplier format for repeated achievements: "6x" (Intercom: "6x Forbes Cloud 100")
- Comma-separate thousands only when not abbreviated: "2,200" (not "2.2k" for precision)

---

## Optional: Surface-1 Background Band

A full-width background band visually separates the stats row from surrounding content (1/5: Intercom with light blue band). In this system, use `var(--surface-1)` — not a colored background.

```css
.stats-section--banded {
    background: var(--surface-1);         /* emphasis section bg — system limit: at most 1-2 per page */
    padding: 128px 0;                     /* large breathing space — spacing system */
}
```

Use this variant sparingly — visual-style.md allows at most 1-2 sections with `var(--surface-1)` background per page. If another section (e.g., Social Proof) already uses it, keep stats on `var(--bg)`.

---

## 2x2 Grid Variant

**When showing 4 stats and the page width feels too spread -> 2x2 grid (1/5: Webflow)**

```css
.stats-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 32px 24px;                       /* 32px vertical (card padding), 24px horizontal (grid gutter) */
    max-width: 540px;                     /* subtitle measure — keeps grid compact */
    margin: 0 auto;
    padding: 0 32px;
    text-align: center;
}
```

This variant is also useful when stats appear as a sidebar alongside narrative text (2/5: Customer.io, Intercom cards).

---

## Narrow Screen (< 768px)

The horizontal row wraps to a 2x2 grid on narrow screens.

```css
@media (max-width: 767px) {
    .stats-row {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 32px 24px;
        padding: 0 20px;                  /* narrow side padding */
        text-align: center;
    }

    .stats-section--banded {
        padding: 80px 0;                  /* large breathing narrow */
    }
}
```

---

## When NOT to Use

- Do not add icons above numbers (only 1/5 samples had icons) — the large number itself is the visual element
- Do not use colored or accent-styled numbers — stat numbers use `var(--text)` at full opacity, not `var(--accent)`
- Do not add box-shadow to stat items — zero shadows (design system rule)
- Do not use serif or italic number styling (Customer.io pattern) — this system uses `var(--font-display)` for stat numbers
- Counter animation (count-up) is optional — see `shared/interaction-patterns.md §5` for the implementation. Use `data-count-to` attributes; initial text should equal the final display value. Trigger on scroll-into-view (IntersectionObserver, not DOMContentLoaded — stats sections are below the fold)
- Do not fabricate statistics — use placeholder format like "XX+" if real numbers are unavailable
