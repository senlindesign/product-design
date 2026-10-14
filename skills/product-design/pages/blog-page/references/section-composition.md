# Blog Page Section Composition Rules

> Source: Mobbin research synthesis across 55+ blog index pages (2026-10-02)

---

## Key Structural Principle

Blog pages are content navigation interfaces, not persuasion funnels. The ordering logic is:

```
orient → filter → browse → discover → subscribe
```

Section rhythm is NOT based on background color alternation (unlike landing pages). Content is the rhythm — the article cards and their visual density provide spatial variation. Blog sections default to `var(--bg)` throughout; only the newsletter section may use `var(--surface-1)` as a visual separator.

---

## 1. Section Order by Archetype

### Archetype A: Grid Index

```
Navigation (fixed, frosted glass)
    ↓
Blog Header (page title — "Blog" / "Articles" / heading + optional subtitle)
    ↓
Category Filter Tabs (horizontal, above grid — "All" + categories)
    ↓
[Featured Article] (optional — omit if < 10 articles or no clear editorial pick; sits inside the filtered area, so it hides while a specific category is active)
    ↓
Article Card Grid (2–3 columns, main content area)
    ↓
[Pagination] (numbered or load-more — only when the blog has 10+ articles)
    ↓
[Newsletter Section] (optional — above footer)
    ↓
Footer
```

**Minimum viable (< 10 articles)**: Navigation → Blog Header → Category Filter → Article Grid → Footer

**Standard (10–50 articles)**: Navigation → Blog Header → Category Filter → [Featured Article] → Article Grid → Pagination → Footer

**Full (50+ articles or with newsletter)**: Navigation → Blog Header → Category Filter → Featured Article → Article Grid → Pagination → Newsletter → Footer

---

### Archetype B: Editorial

```
Navigation (fixed, frosted glass)
    ↓
Featured Article Hero (large hero — the content IS the header; no separate "Blog" title required)
    ↓
[Category Filter Tabs] (optional — directly below featured hero; omit if nav carries filtering. Filtering affects only the grid below — the featured hero stays visible)
    ↓
Article Grid (varied card sizes — 2-col or 3-col; featured cards span full width; when filtering empties a row, collapse that row)
    ↓
[Load More Button] (preferred over numbered pagination for editorial — only when the blog has 10+ articles)
    ↓
[Newsletter Section] (optional)
    ↓
Footer
```

**Note**: In Archetype B, the featured article IS the page orientation — it replaces the blog header. Only add a separate "Blog" heading if the featured article layout does not make the page purpose obvious on its own. Dropping the header does not drop the h1: keep exactly one h1 naming the blog, rendered as a label directly above the featured block (see SKILL.md Implementation Principles).

**Filter behavior**: Because B's filter bar sits below the featured hero, the featured hero is never hidden by filtering (hiding content above the clicked control makes the page jump). Contrast Archetype A, where the featured block sits below the filter bar and hides on a specific category.

---

### Archetype C: Minimal List

```
Navigation (fixed, frosted glass)
    ↓
Blog Header (larger heading than A — "Blog" / "Journal" / "Changelog"; may include search input)
    ↓
[Category Filter] (compact pills centered below heading, OR left sidebar — 3–5 categories max)
    ↓
Article List (full-width single column; each row: date + title + optional excerpt; thin dividers between entries)
    ↓
[Pagination] (text-based "← Older posts" or "Page X of Y"; or Load More button — only when the blog has 10+ articles)
    ↓
[Newsletter Section] (optional — compact inline form, not a full section)
    ↓
Footer
```

**Sidebar filter variant** (Cursor pattern): Category list in a left column (~200px); article list in right column (~880px). Only use when the content volume is high enough that filtering is a primary action.

---

## 2. Blog Header Tokens

The blog header is simpler than landing page heroes — no CTA button, no subheading describing product value, no screenshot.

```css
.blog-header {
    padding-top: 128px;       /* 128px from nav to heading (hero top whitespace rule) */
    padding-bottom: 58px;     /* spacing from heading to filter/content below */
    /* Do NOT use padding shorthand: 'padding: 128px 0 58px' resets left/right to 0,
       which overrides the .container class's padding: 0 32px on the same element */
}

.blog-header h1 {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);   /* section heading scale — not hero scale */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
}

.blog-header .subtitle {
    font-family: var(--font-body);
    font-size: 18px;
    font-weight: 400;
    color: var(--text);
    opacity: 0.5;
    max-width: 540px;     /* §7 subtitle measure */
    margin-top: 24px;
}

/* Search input (Archetype C / high-volume blogs) */
.blog-search {
    width: 100%;
    max-width: 480px;
    padding: 8px 16px;
    font-family: var(--font-display);
    font-size: 14px;
    border: 1px solid var(--surface-2);
    border-radius: 160px;   /* search bar pill shape */
    background: var(--bg);
    color: var(--text);
    margin-top: 32px;
}
```

**Heading text observations**: 3/5 index headers use a simple word ("Blog" or category name). 2/5 use a branded heading ("Life Inside Dropbox", "Upwork Engineering Blog"). 3/5 have subtitles. Only 1/5 includes search input (Better Stack). The simpler the product, the simpler the header.

---

## 3. Category Filter Layout

Category filters are the primary navigation mechanism in Archetype A and B. They are optional in C (high-volume C blogs may use them; low-volume ones omit them entirely).

### Horizontal filters (most common — 7/8 samples use horizontal format)

See `blog-header.md` Category Filter Integration for full CSS implementations of all three styles:
- **Style 1: Text tabs** (underline active) — 3/8 samples, default for Archetype A
- **Style 2: Pill chips** (filled active) — 4/8 samples (OpenSea, Cohere, Performance Lab, Granola), works for all archetypes
- **Style 3: Sidebar list** — 1/8 samples, Archetype C only

Shared layout wrapper:
```css
.category-filter {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 58px;    /* heading-to-content spacing before the grid */
}
```

**Category count guidance**: 3–6 categories optimal (observed range: 3–8). When 7+ categories exist, consider grouping or using a dropdown. "All" is always the first tab and defaults to active state.

### Left sidebar (Archetype C variant — Cursor pattern)

```css
.blog-layout-sidebar {
    display: grid;
    grid-template-columns: 200px 1fr;
    gap: 58px;
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
}

.sidebar-filter {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.sidebar-filter a {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    opacity: 0.5;
    text-decoration: none;
    transition: opacity 0.3s linear;
}

.sidebar-filter a:hover,
.sidebar-filter a.active {
    opacity: 1;
}
```

---

## 4. Article Card Grid

### Grid structure

```css
.article-grid {
    display: grid;
    gap: 24px;                    /* grid gutter from §3 */
    max-width: 1080px;            /* main grid max-width from §7 */
    margin: 0 auto;
    padding: 0 32px;
}

/* 3-column (Archetype A default — Paraform, Luma AI, Cohere, Windsurf, WhatsApp) */
.article-grid--3col {
    grid-template-columns: repeat(3, 1fr);
}

/* 2-column (2-col works well for larger cards with excerpts — folk, Basedash, Aboard) */
.article-grid--2col {
    grid-template-columns: repeat(2, 1fr);
}

/* Narrow screens */
@media (max-width: 767px) {
    .article-grid--3col,
    .article-grid--2col {
        grid-template-columns: 1fr;
        gap: 24px;      /* keep unchanged per narrow-screen spacing table */
    }
}
```

**Column choice guidance**: 3-col for dense index pages (many short articles, title + date only). 2-col when cards have excerpts (2–3 lines need horizontal room). Mixed (B archetype) creates editorial hierarchy with featured cards spanning full width.

### Article card tokens

```css
.article-card {
    background: var(--surface-1);
    border-radius: 16px;     /* content card radius from §4 */
    overflow: hidden;
    cursor: pointer;
    transition: transform 0.2s ease-in-out;
}

.article-card:hover {
    transform: translateY(-4px);    /* card hover lift from §6 */
}

/* Thumbnail */
.article-card__thumb {
    width: 100%;
    aspect-ratio: 16/9;         /* most common observed ratio — Paraform, Cohere */
    object-fit: cover;
    background: var(--bg);          /* placeholder fill: one step from the surface-1 card — visual-style.md §8 Surface nesting rule */
    display: block;
}

/* 4:3 variant (Aboard, Luma AI) */
.article-card__thumb--4-3 { aspect-ratio: 4/3; }

/* Card body */
.article-card__body {
    padding: 32px;     /* card internal padding — from visual-style.md §3 */
}

/* Category label (above title) */
.article-card__category {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;          /* label opacity from §1 */
    margin-bottom: 8px;
}

/* Title */
.article-card__title {
    font-family: var(--font-display);
    font-size: 20px;       /* card heading scale from §2 */
    font-weight: 500;
    letter-spacing: -0.4px;
    line-height: 1.3;
    color: var(--text);
    margin-bottom: 12px;
}

/* Excerpt (optional — omit when grid is 3-col with tight card widths) */
.article-card__excerpt {
    font-family: var(--font-body);
    font-size: 16px;        /* body secondary from §2 */
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    margin-bottom: 16px;
}

/* Metadata row (date + optional author + optional reading time) */
.article-card__meta {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
}
```

**Metadata guidance** (from round-1 summary): Date shown in 5/8 samples. Author shown in 3/8. Reading time shown in only 2/8. Category filter already handles category navigation — avoid redundant category tags on cards unless the tag is the primary hierarchy signal. Never show all four metadata fields simultaneously.

---

## 5. Featured Article Patterns

Featured articles are optional in Archetype A and required in Archetype B.

### Pattern 1: Asymmetric grid (1 large + 2 small) — most common (4/7 featured samples)

Used by: Teachable, Farm Minerals, Webflow, Mural

Canonical values match `featured-article.md` Pattern 1 (full CSS there):

```css
.featured-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 24px;
    margin-bottom: 58px;
}

.featured-card--large {
    border-radius: 16px;
    overflow: hidden;
}

.featured-card--small {
    border-radius: 16px;
    overflow: hidden;
}

/* Small cards stack vertically */
.featured-aside {
    display: flex;
    flex-direction: column;
    gap: 24px;
}
```

Featured article hero content (title-dominant — strip excerpt, keep category + title + date):

```css
.featured-card__label {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    margin-bottom: 12px;
}

.featured-card__title {
    font-family: var(--font-display);
    font-size: 27px;      /* feature heading scale from §2 */
    font-weight: 500;
    letter-spacing: -0.54px;
    line-height: 1.2;
    color: var(--text);
}
```

### Pattern 2: Full-width hero (3/7 featured samples)

Used by: Superhuman, Duolingo, Performance Lab

Canonical values match `featured-article.md` Pattern 2 (full CSS there):

```css
.featured-hero {
    width: 100%;
    margin-bottom: 58px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 58px;
    align-items: center;
}

/* When using a dark background band */
.featured-hero--dark {
    background: var(--surface-1);
    padding: 58px 32px;     /* heading-to-content — visual-style.md §3 (80px is narrow-screen only) */
}

.featured-hero__title {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
}
```

**Key observation**: 0/7 featured heroes include excerpts — title + category + date is the standard. Only 1/7 (Duolingo) adds an explicit CTA button. The rest use the entire featured card as a clickable link.

---

## 6. Pagination Patterns

Three patterns observed (round-7 data):

### Numbered pagination (4/7 samples — most common)

```css
.pagination {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    margin-top: 58px;      /* heading-to-content gap — visual-style.md §3 (narrow: 40px) */
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
}

.pagination__item {
    width: 32px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid var(--surface-2);
    border-radius: 4px;
    color: var(--text);
    opacity: 0.5;
    cursor: pointer;
    text-decoration: none;
    transition: opacity 0.3s linear, border-color 0.3s linear;
}

.pagination__item:hover {
    opacity: 1;
    border-color: var(--text);
}

.pagination__item.active {
    background: var(--text);
    color: var(--text-inverse);
    border-color: var(--text);
    opacity: 1;
}

.pagination__ellipsis {
    color: var(--text);
    opacity: 0.3;
}
```

When to use: when total pages > 3 and knowing total page count is useful to the reader. Ellipsis (`...`) for gaps when 5+ pages exist (Harvest: 26 pages, Paraform: 13 pages).

### Load More button (2/7 samples)

```css
.load-more {
    display: block;
    margin: 58px auto 0;    /* visual-style.md §3 (narrow: 40px) */
    padding: 8px 24px;      /* slightly wider than default btn for a standalone control */
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    border: 1px solid var(--surface-2);
    border-radius: 2px;
    background: transparent;
    color: var(--text);
    cursor: pointer;
    transition: border-color 0.3s linear;
}

.load-more:hover { border-color: var(--text); }
```

When to use: editorial blogs (Archetype B) and minimal lists (Archetype C). Keeps page simple — no need to expose total page count.

### Text-based navigation (1/7 samples — OpenAI)

```css
.pagination-text {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 58px;                  /* visual-style.md §3 (narrow: 40px) */
    border-top: 1px solid var(--surface-2);
    padding-top: 24px;
}

.pagination-text__indicator {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
}

.pagination-text__link {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.5;
    text-decoration: none;
    transition: opacity 0.3s linear;
}

.pagination-text__link:hover { opacity: 1; }
```

When to use: very minimal blogs where numbered pagination feels too heavy (Archetype C).

---

## 7. Newsletter Section

Newsletter sections are optional on the blog index — not every blog needs one. When included, position it between the article grid/pagination and the footer.

**Position findings** (round-4 data): Bottom of page before footer (3/8), inline between header and grid (1/8, Clockwise), within grid as a card (1/8, Apollo), sidebar on article page (2/8 — not applicable to index page). For the blog INDEX page, bottom placement is the standard.

### Standard bottom placement

```css
.newsletter-section {
    padding: 180px 0;       /* section rhythm from §3 */
    background: var(--surface-1);   /* visual separation from article grid */
    text-align: center;
}

.newsletter-section h2 {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);
    font-weight: 500;
    letter-spacing: -0.02em;
    color: var(--text);
    margin-bottom: 24px;
}

.newsletter-section .subtitle {
    font-family: var(--font-body);
    font-size: 18px;
    font-weight: 400;
    color: var(--text);
    opacity: 0.5;
    max-width: 540px;
    margin: 0 auto 48px;
}

.newsletter-form {
    display: flex;
    gap: 8px;
    justify-content: center;
    max-width: 480px;
    margin: 0 auto;
}

.newsletter-form input {
    flex: 1;
    padding: 8px 16px;
    font-family: var(--font-display);
    font-size: 14px;
    border: 1px solid var(--surface-2);
    border-radius: 4px;         /* input border-radius from §4 */
    background: var(--bg);
    color: var(--text);
}

.newsletter-form button {
    padding: 8px 16px;
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    background: var(--accent);
    color: var(--accent-text);
    border: none;
    border-radius: 2px;         /* button border-radius from §4 */
    cursor: pointer;
    transition: transform 0.2s ease-in-out;
}

.newsletter-form button:hover { transform: translateY(-1px); }
```

**Heading copy observations** (round-4): "Subscribe to [newsletter]" (3/8), "Sign up for [benefit]" (2/8), "Get insights/updates" (2/8), creative brand-specific (1/8 — OpenTable "Hungry for more?"). Use a simple functional heading unless the brand has a strong editorial voice.

**Single email field**: 5/8 samples use a single email field. Avoid multi-field forms (first name, last name, company) on the blog index — that is a lead-gen pattern, not a newsletter pattern.

**Privacy note**: 4/8 include a short privacy note below the form. Include it: "No spam. Unsubscribe at any time."

---

## 8. Spacing Summary

All values quoted verbatim from `shared/visual-style.md`:

| Context | Value |
|---------|-------|
| Section padding (top and bottom) | 180px |
| Hero top whitespace (nav to blog header heading) | 128px |
| Blog header heading to category filters | 58px |
| Category filters to article grid | 58px (or 0 if filters are part of the header block) |
| Grid gutter | 24px |
| Card internal padding | 32px |
| Pagination / load-more margin-top | 58px (narrow: 40px) |
| Narrow screen: section rhythm | 96px |
| Narrow screen: hero top whitespace | 80px |
| Narrow screen: heading to content | 40px |
| Narrow screen: card padding | 24px |

---

## 9. Background Alternation Rule

Blog pages deviate from landing page background alternation because **content is the rhythm**:

- Default: `var(--bg)` for Navigation, Blog Header, Category Filters, Article Grid, Pagination
- Exception: Newsletter Section may use `var(--surface-1)` as a visual separator
- Exception: Featured Article Hero may use `var(--surface-1)` for a dark/band treatment (full-width B patterns)
- **Never**: alternating section backgrounds per section (no landing-page rhythm here)
- **Never**: more than 2 distinct background values on the page
