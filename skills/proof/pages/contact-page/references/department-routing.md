# Department Routing Cards — Design Knowledge

> Source: Mobbin research synthesis from 10 Department Routing sections

---

## When to Use

Department routing cards are used in **Archetype B (Department Routing)** and **Archetype D (Support Hub)**. Use them when the product has 2+ distinct contact entry points (Sales / Support / Partnerships, etc.).

**Do not use for**: Archetype A (a single general form is sufficient) and Archetype C (the Sales form occupies the entire page).

---

## 1. Card Count

| Count | Frequency | Typical scenario |
|-------|-----------|-----------------|
| 2 | 4/10 (most common) | Sales vs Support binary split (Zendesk, GitBook, Workable, Linear) |
| 3 | 3/10 | + Partnerships or Press (Customer.io, TravelPerk) |
| 4 | 1/10 | Sales / Support / Partners / Press (Sprout Social) |
| 6 | 1/10 | Most complex routing (Mews: demo + sales + partnerships + login + help + emergencies) |
| 1+3 (hierarchical) | 1/10 | Support Hub pattern (Framer: featured Product Support + 3 smaller cards) |

**Recommendation**: Default to 2–3 cards. More than 4 — reconsider whether each truly needs a standalone entry, or whether some can be merged.

---

## 2. Card Layout

### 2.1 Equal-Width Grid (Default, 8/10 samples)

```css
.department-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 24px;
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
}
```

**2 cards**: `grid-template-columns: repeat(2, 1fr)` — don't use `auto-fit`; 2 cards with auto-fit would be too wide.

**3 cards**: `grid-template-columns: repeat(3, 1fr)` — three columns on desktop.

**4 cards**: `grid-template-columns: repeat(4, 1fr)` — four columns on desktop. Folds to 2×2 on narrow screens.

### 2.2 Hierarchical Layout (Archetype D Support Hub)

```css
.department-cards-hierarchical {
    display: grid;
    gap: 24px;
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
}

.department-card-featured {
    grid-column: 1 / -1;              /* spans full width */
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 32px;
}

.department-cards-secondary {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}
```

**When to use**: There is one clear "primary" entry (e.g., Product Support) and multiple secondary entries.

---

## 3. Card Content Structure

### Required Elements

```
Icon + Title + Description + CTA
```

8/10 samples include an icon. All samples include title + description + CTA.

### Card Token

```css
.department-card {
    background: var(--surface-1);
    border-radius: 8px;               /* functional card border-radius */
    padding: 32px;
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.department-card .card-icon {
    width: 40px;
    height: 40px;
    color: var(--text);
    opacity: 0.5;
}

.department-card h3 {
    font-family: var(--font-display);
    font-size: 20px;                  /* card title */
    font-weight: 500;
    letter-spacing: -0.4px;
    line-height: 1.3;
    color: var(--text);
}

.department-card p {
    font-family: var(--font-body);
    font-size: 16px;
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    flex-grow: 1;                     /* push CTA to bottom for alignment */
}
```

### Icon Handling

- **Do not** wrap icons in colored circular/square backgrounds (see the absolute prohibitions in visual-style.md)
- **Use** monochrome icons: `color: var(--text); opacity: 0.5`
- Uniform icon size of `40px`
- Can use inline SVG or icon font

---

## 4. CTA Differentiation Strategy

**Core rule**: 80% of observed samples use differentiated CTA copy. Don't use the same "Contact Us" for all cards.

### CTA Copy

Each card's CTA should reflect the specific action for that department:

| Department | CTA copy | CTA link behavior |
|------------|----------|------------------|
| Sales | "Contact Sales" / "Talk to Sales" | Navigate to sales form or Calendly |
| Support | "Get Support" / "Visit Help Center" | Navigate to help center or support form |
| Partnerships | "Explore Partnerships" / "Partner with Us" | Navigate to partnerships form |
| Press / Media | "Email Press Team" / "Get Brand Assets" | mailto: link or press page |

### CTA Button Style Hierarchy

```css
/* Primary department (usually Sales) — solid button */
.department-card.primary .card-cta {
    background: var(--accent);
    color: var(--accent-text);
    border: none;
    border-radius: 2px;
    padding: 8px 16px;
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: transform 0.2s ease-in-out;
}

.department-card.primary .card-cta:hover {
    transform: translateY(-1px);
}

/* Secondary departments — outline button */
.department-card .card-cta {
    background: transparent;
    color: var(--text);
    border: 1px solid var(--surface-2);
    border-radius: 2px;
    padding: 8px 16px;
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: transform 0.2s ease-in-out;
}

.department-card .card-cta:hover {
    border-color: var(--text);
    transform: translateY(-1px);
}
```

**Selection rules**:
- Sales / "Book a demo" uses solid `.btn-dark` — this is the most important entry point
- Others use outline `.btn-outline`
- Don't use solid buttons for all cards (no priority distinction)
- Don't use outline buttons for all cards either (no call-to-action pull)

---

## 5. Responsive Behavior

```css
@media (max-width: 767px) {
    .department-cards {
        grid-template-columns: 1fr;   /* single column on narrow screens */
    }

    .department-cards-secondary {
        grid-template-columns: 1fr;
    }
}
```

**2 cards** can maintain two columns on narrow screens (`minmax(240px, 1fr)`) because content is limited.
**3–4 cards** must collapse to single column on narrow screens.

---

## 6. Common Routing Dimensions

Basic binary split: **Sales vs Support** (the starting point for almost all samples)

Extended dimensions (by frequency):
1. Partnerships (collaboration / integrations)
2. Press / Media (brand assets, media contacts)
3. Help Center / Knowledge Base (self-service entry)
4. Emergencies / Critical Issues (urgent contact)
5. Billing (invoice / payment issues)

**Don't fabricate departments**: Only show departments the product actually has people responsible for. 3 genuine cards are more valuable than 6 hollow ones.
