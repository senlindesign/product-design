# Featured Article — Design Knowledge

> Source: Mobbin research across 8 blog pages with featured/hero sections (Round 2, 2026-10-02)

---

## Overview

A featured article section promotes one or two recent posts above the regular article grid, establishing editorial hierarchy through size difference. It is the defining characteristic of Archetype B (Editorial) and is absent in Archetype C (Minimal List).

**Three layout families emerge from 8 samples**:
1. Split/asymmetric grid (4/8) — featured content-width, one large + smaller items side-by-side
2. Full-width/full-bleed hero (3/8) — featured occupies full page width or viewport
3. No featured section (1/8) — Archetype C, all articles treated equally (Claude)

**Content in featured heroes is title-dominant**: 7/7 featured heroes show title. 0/7 show full excerpts. 3/7 show author. 1/7 has an explicit CTA button (Duolingo). Strip everything except title + category + optional author.

---

## Pattern 1: Split Asymmetric Grid (Recommended for Archetype B)

**When to use**:
- Archetype B (Editorial) with 2+ recent articles worth featuring
- Most common pattern (4/8 samples)
- Creates hierarchy without requiring a full-width hero commitment

**Layout A — 1 large + 2 small stacked**:
```
┌─────────────────────────┬──────────────────┐
│                         │  Smaller card 1  │
│   Large featured card   ├──────────────────┤
│                         │  Smaller card 2  │
└─────────────────────────┴──────────────────┘
```

**CSS tokens**:
```css
/* Asymmetric split container */
.featured-split {
    display: grid;
    grid-template-columns: 2fr 1fr;      /* large card dominates left; proportional, no fixed px column (canonical — section-composition.md §5 and anti-patterns.md §8 match) */
    gap: 24px;                           /* grid gutter — from visual-style.md §7 */
    margin-bottom: 58px;                 /* space before regular grid — from visual-style.md §3 */
}

/* Large featured card */
.featured-card--large {
    background: var(--surface-1);
    border-radius: 16px;                 /* content card — from visual-style.md §4 */
    overflow: hidden;
}
.featured-card--large .card-thumbnail {
    width: 100%;
    aspect-ratio: 16 / 9;
    object-fit: cover;
    display: block;
    background: var(--bg);               /* placeholder fill: steps one level from the surface-1 card — visual-style.md §8 Surface nesting rule */
}
.featured-card--large .card-body {
    padding: 32px;                       /* card internal padding — from visual-style.md §3 */
}

/* Category label above title */
.featured-card-category {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;                        /* label opacity — from visual-style.md §1 */
    margin-bottom: 12px;
    display: block;
}

/* Featured card title — larger than regular card title */
.featured-card-title {
    font-family: var(--font-display);
    font-size: 27px;                     /* feature heading — from visual-style.md §2 */
    font-weight: 500;
    letter-spacing: -0.54px;
    line-height: 1.2;
    color: var(--text);
    margin-bottom: 16px;
}

/* Featured card metadata */
.featured-card-meta {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
}

/* Sidebar column — 2 smaller cards stacked */
.featured-sidebar {
    display: flex;
    flex-direction: column;
    gap: 24px;
}

/* Small horizontal cards in sidebar */
.featured-card--small {
    display: grid;
    grid-template-columns: 120px 1fr;
    gap: 16px;
    background: var(--surface-1);
    border-radius: 16px;
    overflow: hidden;
    padding: 0;
    flex: 1;
}
.featured-card--small .card-thumbnail {
    width: 100%;
    height: 100%;
    min-height: 100px;
    object-fit: cover;
    border-radius: 0;
    background: var(--bg);               /* placeholder fill inside surface-1 card — Surface nesting rule */
}
.featured-card--small .card-body {
    padding: 24px 24px 24px 0;
}
.featured-card--small .featured-card-title {
    font-size: 16px;                     /* body secondary scale for small card */
    font-weight: 500;
    letter-spacing: normal;
    line-height: 1.4;
    margin-bottom: 8px;
}
```

**Layout B — 2-column equal split**:
```
┌─────────────────────────┬───────────────────────────┐
│   Large photo (left)    │   Title + meta (right)    │
│   (60% width)           │   No excerpt, no CTA      │
└─────────────────────────┴───────────────────────────┘
```

```css
.featured-split--equal {
    display: grid;
    grid-template-columns: 3fr 2fr;      /* 60/40 — photo dominant */
    gap: 0;                              /* no gap; photo edge meets text area */
    border-radius: 16px;
    overflow: hidden;
    background: var(--surface-1);
    margin-bottom: 58px;
}
.featured-split--equal .card-thumbnail {
    width: 100%;
    height: 100%;
    min-height: 360px;
    object-fit: cover;
    background: var(--bg);               /* placeholder fill inside surface-1 container — Surface nesting rule */
}
.featured-split--equal .card-body {
    padding: 48px 32px;                  /* generous vertical padding for split alignment */
    display: flex;
    flex-direction: column;
    justify-content: flex-end;           /* title anchors to bottom, meta floats up */
}
```

**Evidence**: Farm Minerals (1 large + 2 small), Mural (split + text list), Webflow (1 large + 2 small), Teachable (equal split)
**Evidence status**: Cross-sample inference

---

## Pattern 2: Full-Width Hero

**When to use**:
- Archetype B (Editorial) when a single article deserves maximum visual impact
- Blog prioritizes magazine-like immersion over content density
- Dark theme blogs (Superhuman, Basedash)

**Layout A — Photo right, text left, dark background**:
```
┌────────────────────────────────────────────────────────┐
│  CATEGORY · AUTHOR                                      │  ← mono label row
│  Large Article Title                                    │  ← section heading scale
│  No excerpt — title does the work                      │  ← stripped-down
│                                              [photo]    │
└────────────────────────────────────────────────────────┘
```

**CSS tokens**:
```css
.featured-hero--dark {
    background: var(--surface-1);        /* dark theme: #141414 */
    padding: 58px 32px;                  /* heading-to-content spacing — from visual-style.md §3 (canonical; not 80px) */
    display: grid;
    grid-template-columns: 1fr 1fr;      /* visual-style.md §7 alternating rows: 2 columns / 58px gap / center */
    gap: 58px;
    align-items: center;
    max-width: 1080px;
    margin: 0 auto;
    margin-bottom: 58px;
}

/* Label row: CATEGORY · AUTHOR in mono uppercase */
.featured-hero-label-row {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.featured-hero-label-row .dot::before {
    content: '·';
    margin: 0 4px;
}

/* Hero title */
.featured-hero-title {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);  /* section heading scale — from visual-style.md §2 */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
}

/* Featured hero image */
.featured-hero-image {
    width: 100%;
    aspect-ratio: 4 / 3;
    object-fit: cover;
    border-radius: 16px;                 /* content card radius — from visual-style.md §4 */
    background: var(--bg);               /* placeholder fill inside the surface-1 band — Surface nesting rule */
}
```

**Layout B — Full-bleed photo with text overlay**:

Use only when image contrast is guaranteed (editorial photography with dark areas at bottom). Requires `text-shadow` for readability — this is an exception to the color silence principle justified by the editorial archetype.

```css
.featured-hero--bleed {
    position: relative;
    width: 100%;
    height: 520px;
    overflow: hidden;
    margin-bottom: 58px;
}
.featured-hero--bleed img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}
/* Gradient overlay for text legibility */
.featured-hero--bleed::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(
        to top,
        rgba(10, 10, 10, 0.75) 0%,
        rgba(10, 10, 10, 0) 50%
    );
}
.featured-hero--bleed .hero-overlay-text {
    position: absolute;
    bottom: 40px;
    left: 40px;
    right: 40px;
    z-index: 1;
    color: #EDEDED;
}
.featured-hero--bleed .hero-overlay-title {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);   /* section heading scale — from visual-style.md §2 */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.15;
    color: #EDEDED;
    margin-top: 8px;
}
```

**Do not use bleed layout when**: photos are low-contrast or user-submitted (no control over dark areas), or when the page is light theme (the overlay creates a visual conflict with the white body below).

**Evidence**: Superhuman (dark bg, text left + photo right), Duolingo (colored bg hero), Performance Lab (full-bleed photo + overlay)
**Evidence status**: Cross-sample inference

---

## Pattern 3: Featured Position Indicator (No Visual Hero)

**When to use**:
- Archetype B (Editorial) that wants article hierarchy without a heavy visual treatment
- Featured article is indicated by size alone within the grid (not a separate hero section)
- The featured article spans 2 columns in a 3-column grid

**CSS tokens**:
```css
/* Featured card spanning 2 columns within the article grid */
.article-grid .card--featured {
    grid-column: span 2;
}

/* Featured card body adjustments when larger */
.article-grid .card--featured .featured-card-title {
    font-size: 27px;                     /* feature heading — from visual-style.md §2 */
    letter-spacing: -0.54px;
}

/* Featured label (optional, rarely used) */
.featured-label {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.3;                        /* weakest opacity — purely decorative label */
    margin-bottom: 8px;
    display: block;
}
```

**Explicit "FEATURED" label note**: Only 2/7 products explicitly label the featured content (Mural: "Featured post", Duolingo: "FEATURED"). The rest rely on size and position to imply featured status. Prefer size-based hierarchy over an explicit label — it reads as more sophisticated.

**Evidence**: Mural (explicit "Featured post" label), Webflow (size alone)
**Evidence status**: Cross-sample inference

---

## Metadata Guidance

What to include in a featured article (stripped vs. standard card):

| Element | Standard card | Featured article |
|---------|--------------|-----------------|
| Category | Optional | Always include |
| Title | Always | Always (larger) |
| Excerpt | Often (2 lines) | Never — title does the work |
| Author | Optional | Optional (3/7 include it) |
| Date | Often (5/8) | Optional |
| Reading time | Rare (2/8) | Never |
| CTA button | Rare | Avoid (1/7 — Duolingo) |

**The featured hero is title-dominant.** Excerpts, reading time, and CTA buttons are all stripped to keep the visual weight on the title and image.

---

## Interaction with Category Filters

Whether the featured block hides on filter depends on its position relative to the filter bar (stub in SKILL.md Step 5):

- **Featured below the filter bar** (Archetype A) — it is inside the filtered area and spans several categories, so hide it while a specific category is active (`data-hide-on-filter`).
- **Featured above the filter bar** (Archetype B) — keep it visible; filter only the grid below. Hiding it shifts the page up under the cursor. Do not put `data-category` on its cards.

---

## Spacing Tokens

```
Featured section → article grid gap:   58px  (heading-to-content — from visual-style.md §3)
Featured card padding:                 32px  (card internal padding — from visual-style.md §3)
Featured hero top/bottom padding:      58px  (heading-to-content spacing)
Grid gap between featured items:       24px  (grid gutter — from visual-style.md §7)
Featured split column gap:             24px  (grid gutter — from visual-style.md §7)
Featured split columns:                2fr 1fr (proportional — no fixed px column)
Featured hero columns:                 1fr 1fr / 58px gap (visual-style.md §7 alternating rows)
Thumbnail placeholder fill:            one surface step from the container — var(--bg) inside var(--surface-1)
```

---

## Responsive Behavior (≤767px)

```css
@media (max-width: 767px) {
    /* Asymmetric split → single column stack */
    .featured-split {
        grid-template-columns: 1fr;
    }
    .featured-sidebar {
        flex-direction: column;
    }
    .featured-card--small {
        grid-template-columns: 100px 1fr;
    }

    /* Equal split → stacked (image top, text bottom) */
    .featured-split--equal {
        grid-template-columns: 1fr;
    }
    .featured-split--equal .card-thumbnail {
        min-height: 220px;
    }
    .featured-split--equal .card-body {
        padding: 24px;                   /* reduced from 48px — from visual-style.md narrow-screen table */
        justify-content: flex-start;
    }

    /* Dark hero → stacked */
    .featured-hero--dark {
        grid-template-columns: 1fr;
        padding: 40px 20px;
    }

    /* Full-bleed → shorter height */
    .featured-hero--bleed {
        height: 320px;
    }
    .featured-hero--bleed .hero-overlay-text {
        left: 20px;
        right: 20px;
        bottom: 24px;
    }

    /* Grid span featured card → full width */
    .article-grid .card--featured {
        grid-column: span 1;
    }
}
```

---

## Evidence

| Pattern | Products | Archetype |
|---------|----------|-----------|
| Asymmetric split (1 large + 2 small) | Farm Minerals, Webflow | B |
| Equal 2-column split | Teachable, Mural | B |
| Full-width dark hero | Superhuman | B |
| Full-bleed photo + overlay | Performance Lab | B |
| Colored hero (brand) | Duolingo | B (brand-heavy) |
| No featured section | Claude | C |
