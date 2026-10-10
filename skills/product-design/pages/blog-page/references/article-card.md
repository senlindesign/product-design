# Article Card — Design Knowledge

> Source: Mobbin research across 15 blog pages (Round 1: 8 article-card samples + Round 5: 7 minimal-list samples, 2026-10-02)

---

## Overview

Article cards are the repeating unit of blog index pages. They appear in grids, lists, or mixed-size editorial layouts. Card design signals the blog's editorial weight: heavy thumbnail treatment signals a content-marketing blog; text-only or small-thumbnail treatment signals a developer-focused or changelog blog.

**When to use article cards**: Archetype A (Grid Index) and Archetype B (Editorial). Archetype C (Minimal List) uses row entries instead — see Pattern 4.

---

## Pattern 1: Vertical Grid Card (Default — Thumbnail Top)

**When to use**:
- Archetype A (Grid Index) — the standard pattern
- 3-column or 2-column grids
- Blog has a strong visual identity through photography or product screenshots
- 7/8 samples in Round 1 use this orientation

**Layout**:
```
┌──────────────────────────────┐
│        Thumbnail             │  ← aspect ratio: 16:9 or 4:3
│  [CATEGORY PILL overlay opt] │
├──────────────────────────────┤
│  Date · Reading time (opt)   │  ← label row
│  Title                       │  ← card heading
│  Excerpt (optional)          │  ← body secondary
│  Author (optional)           │  ← label with avatar
└──────────────────────────────┘
```

**CSS tokens**:
```css
/* Card container */
.article-card {
    background: var(--surface-1);
    border-radius: 16px;             /* content card — from visual-style.md §4 */
    overflow: hidden;                /* clips the thumbnail at top */
    cursor: pointer;
    transition: transform 0.2s ease-in-out;
}
.article-card:hover {
    transform: translateY(-4px);     /* card hover lift — from visual-style.md §6 */
}

/* Thumbnail */
.card-thumbnail {
    width: 100%;
    aspect-ratio: 16 / 9;           /* most common — Paraform, Luma AI; use 4/3 for portrait-heavy content */
    object-fit: cover;
    display: block;
    background: var(--bg);          /* placeholder fill: one step from the surface-1 card, never surface-1 itself — visual-style.md §8 Surface nesting rule */
}

/* Card body */
.card-body {
    padding: 32px;                   /* card internal padding — from visual-style.md §3 */
}

/* Metadata row (date · reading time) */
.card-meta {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;                    /* auxiliary/label opacity — from visual-style.md §1 */
    margin-bottom: 12px;
    display: flex;
    gap: 8px;
    align-items: center;
}
.card-meta .dot::before {
    content: '·';
    opacity: 0.4;
}

/* Card title */
.card-title {
    font-family: var(--font-display);
    font-size: 20px;                 /* card heading — from visual-style.md §2 type scale */
    font-weight: 500;
    letter-spacing: -0.4px;
    line-height: 1.3;
    color: var(--text);
    opacity: 1;
    margin-bottom: 12px;
}

/* Excerpt (optional) */
.card-excerpt {
    font-family: var(--font-body);
    font-size: 16px;                 /* body secondary — from visual-style.md §2 */
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;                    /* subtitle/description opacity — from visual-style.md §1 */
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

/* Author row */
.card-author {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 16px;
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
}
.card-author-avatar {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: var(--surface-2);
    object-fit: cover;
}
```

**Metadata combinations (by frequency)**:
- **Minimal (date only)**: Date — 5/8 include date; omit everything else. Simple and scannable. (Paraform, Luma AI)
- **Standard (date + category)**: Category label on thumbnail overlay OR below thumbnail as mono label, plus date. (Paraform, Aboard)
- **Author-forward (title + author + date)**: No excerpt, prominent author attribution with avatar. (folk, Dropbox)
- **Rich (category + title + excerpt + date + reading time)**: All metadata. Use only when 2-column grid gives each card enough space. (Aboard, Luma AI, Basedash)

**Grid layout**:
```css
.article-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);   /* 3-col for more cards, less visual weight per card */
    gap: 24px;                               /* grid gutter — from visual-style.md §7 */
}

/* 2-column variant — use when excerpts are shown (Aboard, Basedash) */
.article-grid--2col {
    grid-template-columns: repeat(2, 1fr);
}
```

**Category pill overlay (optional)**:
```css
/* Avoid brand/accent colors — use achromatic surface-2 on thumbnail overlay */
.card-category-overlay {
    position: absolute;
    top: 12px;
    left: 12px;
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    background: rgba(255, 255, 255, 0.85);  /* light theme: translucent white */
    color: var(--text);
    padding: 4px 8px;
    border-radius: 4px;                       /* input radius — from visual-style.md §4 */
}
[data-theme="dark"] .card-category-overlay {
    background: rgba(10, 10, 10, 0.85);
    color: var(--text);
}
```

**Evidence**: Paraform (3-col), Luma AI (3-col), Dropbox (3-col), Aboard (2-col), folk (2-col)
**Evidence status**: Cross-sample inference

---

## Pattern 2: Horizontal Row Card (Thumbnail Left)

**When to use**:
- Archetype A with dark theme
- 2-column grid where horizontal orientation aids scanning
- When showing longer excerpts without making cards too tall

**Layout**:
```
┌──────────┬──────────────────────────┐
│Thumbnail │  Category (optional)     │
│ (square  │  Title                   │
│ or 4:3)  │  Excerpt (2-3 lines)     │
│          │  Date                    │
└──────────┴──────────────────────────┘
```

**CSS tokens**:
```css
.article-card--horizontal {
    display: grid;
    grid-template-columns: 240px 1fr;    /* fixed thumbnail width, text fills remainder */
    gap: 32px;                            /* card internal padding — from visual-style.md §3 */
    background: var(--surface-1);
    border-radius: 16px;                  /* content card — from visual-style.md §4 */
    overflow: hidden;
    padding: 0;
    align-items: stretch;
}

.article-card--horizontal .card-thumbnail {
    width: 100%;
    height: 100%;
    min-height: 180px;
    object-fit: cover;
    aspect-ratio: unset;
    border-radius: 0;
}

.article-card--horizontal .card-body {
    padding: 32px 32px 32px 0;           /* no left padding — thumbnail provides left edge */
}

/* Excerpt — horizontal cards can show more lines */
.article-card--horizontal .card-excerpt {
    -webkit-line-clamp: 3;
}
```

**Evidence**: Basedash (2-column dark theme, square-ish thumbnails)
**Evidence status**: Single source observation

---

## Pattern 3: Editorial Mixed-Size Grid

**When to use**:
- Archetype B (Editorial) — creates visual hierarchy and breaks the monotony of uniform grids
- 2 featured cards (wider) in top row + 3 standard cards in bottom row
- Or: 1 large card left + 2 smaller cards right (see also `featured-article.md`)

**Layout — 2+3 editorial**:
```css
/* Wrapper only — it must NOT be a grid itself, or each row container below
   would be placed into a single grid column. The rows carry the grids. */
.editorial-grid {
    display: block;
}

/* Top row: 2 featured cards, each half the content width (the visual equivalent of
   1.5 columns). A 3-column track cannot hold two equal halves, so do NOT span inside
   .editorial-grid — nest a 2-col row for the top and a 3-col row below. */
.editorial-top-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    margin-bottom: 24px;
}
.editorial-bottom-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}
```

**Row containers and filtering**: mark `.editorial-top-row` and `.editorial-bottom-row` with `data-filter-row`. When a category filter hides every card in a row, the stub in SKILL.md collapses that row so its `margin-bottom: 24px` does not leave an empty band.

**Top row cards (larger)**: larger thumbnail, same card-heading size (20px), excerpts optional
**Bottom row cards (smaller)**: same card structure as Pattern 1, no excerpt, truncated meta

**Evidence**: Framer (2+3 dark), Epidemic Sound (2 text-only + 3 photo)
**Evidence status**: Cross-sample inference

---

## Pattern 4: Minimal List Row (Archetype C)

**When to use**:
- Archetype C (Minimal List) — developer-focused, changelog, or content-first blogs
- No thumbnails, or very small square thumbnails (48-80px) as visual anchors only
- Title + date is the minimum viable row; add excerpt only when the entry is long-form

**Layout variants**:

**A. Title + date (same line)** — most minimal:
```css
.list-entry {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    padding: 16px 0;
    border-bottom: 1px solid var(--surface-2);
}
.list-entry-title {
    font-family: var(--font-display);
    font-size: 18px;                    /* compact same-line variant — from visual-style.md §2 body scale */
    font-weight: 500;                   /* use 24-28px for date-margin / standalone row variants */
    color: var(--text);
}
.list-entry-date {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    white-space: nowrap;
    margin-left: 24px;
}
```

**B. Date-margin layout** — date on left, content on right:
```css
.list-entry--margin {
    display: grid;
    grid-template-columns: 100px 1fr;
    gap: 24px;
    padding: 24px 0;
    border-bottom: 1px solid var(--surface-2);
}
.list-entry--margin .entry-date {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    padding-top: 4px;
}
.list-entry--margin .entry-title {
    font-family: var(--font-display);
    font-size: 24px;                    /* larger title compensates for no thumbnail */
    font-weight: 500;
    letter-spacing: -0.48px;
    line-height: 1.2;
    color: var(--text);
    margin-bottom: 8px;
}
.list-entry--margin .entry-excerpt {
    font-family: var(--font-body);
    font-size: 16px;
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
}
```

**C. Small-thumbnail rows** — thumbnail as visual anchor (48-80px square):
```css
.list-entry--thumb {
    display: grid;
    grid-template-columns: 64px 1fr;
    gap: 16px;
    padding: 16px 0;
    border-bottom: 1px solid var(--surface-2);
    align-items: center;
}
.list-thumb {
    width: 64px;
    height: 64px;
    border-radius: 8px;                /* feature card radius — from visual-style.md §4 */
    object-fit: cover;
    background: var(--surface-1);      /* list rows sit on var(--bg), so surface-1 is one step up — Surface nesting rule */
}
```

**When not to use**: If the product has strong visual content that differentiates articles, use Pattern 1 instead. Text lists fail when entries are not meaningfully distinct by title alone.

**Evidence**: Lemon Squeezy (title+date line), Plain (date-margin), Cursor (sidebar list + text), Height (small-thumb rows), Harvest (full-width text with excerpt)
**Evidence status**: Cross-sample inference

---

## Typography Tokens (Blog-Specific)

These supplement the type scale in `shared/visual-style.md §2`:

```
Article card title:      20px / weight 500 / tracking -0.4px / line-height 1.3
                         (card heading scale from visual-style.md — same as feature card headings)

List entry title:        18px (compact same-line) to 24–28px (date-margin / standalone rows) / weight 500 / tracking -0.48px / line-height 1.2
                         (higher than card title because no thumbnail shares visual weight)

Card excerpt:            16px / --font-body / weight 400 / line-height 1.6 / opacity 0.5
                         (body text role — uses --font-body at 400, not display at 500)

Card metadata:           12px / mono / weight 400 / tracking +0.72px / uppercase / opacity 0.4
                         (label scale from visual-style.md — all date, author, reading time labels)

Category pill text:      12px / mono / weight 400 / tracking +0.72px / uppercase
                         (same as label — do not invent a separate category font style)
```

---

## Spacing Tokens

```
Card internal padding:   32px               (from visual-style.md §3)
Card grid gap:           24px               (from visual-style.md §7 grid gutter)
Metadata-to-title gap:   12px               (from visual-style.md §3 base scale)
Title-to-excerpt gap:    12px               (from visual-style.md §3 base scale)
Excerpt-to-author gap:   16px               (from visual-style.md §3 base scale)
List entry divider gap:  16px–24px          (from visual-style.md §3 base scale)
```

---

## Responsive Behavior (≤767px)

```css
@media (max-width: 767px) {
    /* 3-column grid → 1 column */
    .article-grid {
        grid-template-columns: 1fr;
    }
    /* 2-column grid → 1 column */
    .article-grid--2col {
        grid-template-columns: 1fr;
    }
    /* Editorial 2+3 rows → 1 column */
    .editorial-top-row,
    .editorial-bottom-row {
        grid-template-columns: 1fr;
    }
    /* Horizontal card → vertical (thumbnail top) */
    .article-card--horizontal {
        grid-template-columns: 1fr;
    }
    .article-card--horizontal .card-thumbnail {
        aspect-ratio: 16 / 9;
        height: auto;
        border-radius: 16px 16px 0 0;
    }
    .article-card--horizontal .card-body {
        padding: 24px;                   /* reduced from 32px — from visual-style.md narrow-screen §3 */
    }
    /* Card internal padding reduction */
    .card-body {
        padding: 24px;                   /* from visual-style.md narrow-screen spacing table */
    }
}
```

---

## Evidence

| Pattern | Products | Archetype |
|---------|----------|-----------|
| Vertical grid (16:9) | Paraform, Luma AI | A |
| Vertical grid (4:3) | Aboard, folk, Legora | A |
| Vertical grid (illustration) | Dropbox | A |
| Horizontal row | Basedash | A (dark) |
| Editorial mixed-size | Framer, Epidemic Sound | B |
| Text list (title+date) | Lemon Squeezy, Family | C |
| Date-margin text list | Plain, Cursor | C |
| Small-thumbnail rows | Height, Shade | C |
