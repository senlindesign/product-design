# Blog Header — Design Knowledge

> Source: Mobbin research across 13 blog index pages (Round 3: 8 category-filter samples + Round 6: 5 relevant index samples, 2026-10-02)

---

## Overview

The blog header is the page-level title area that appears above the article grid. It establishes the blog's identity, provides navigation context, and — for Archetypes A and B — integrates category filtering.

Three header types emerge from the research:

1. **Classic heading** — simple "Blog" or branded name, optional subtitle, optional search. Most common. (Better Stack, Windsurf, Granola)
2. **Split hero header** — heading and description on left, visual element or sub-navigation on right. Editorial. (Dropbox, Dropbox WIP)
3. **No separate header** — featured article occupies the header position; the blog title appears only in navigation. (MOUTHWASH, Archetype B editorial)

---

## Pattern 1: Classic Heading with Category Filter

**When to use**:
- Archetype A (Grid Index) — the standard pattern
- Blog has 3–7 topic categories worth filtering
- Simple orientation: visitors see the blog title, then filter, then browse

**Layout**:
```
[ Blog ]                                    ← heading (centered or left)
[ Short description ]                       ← optional subtitle (centered or left)
[ All | Engineering | News | Company ... ]  ← category filter row
───────────────────────────────────────────
[ Article grid ]
```

**CSS tokens**:
```css
/* Header section container */
.blog-header {
    padding: 128px 0 58px;               /* hero top whitespace → heading-to-content gap */
    max-width: 1080px;                   /* from visual-style.md §7 main grid */
    margin: 0 auto;
    padding-left: 32px;
    padding-right: 32px;
}

/* Heading */
.blog-header-title {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);  /* section heading — from visual-style.md §2 */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
    margin-bottom: 16px;
}

/* Subtitle (optional) */
.blog-header-subtitle {
    font-family: var(--font-body);
    font-size: 18px;                     /* body text — from visual-style.md §2 */
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;                        /* subtitle opacity — from visual-style.md §1 */
    max-width: 540px;                    /* subtitle measure — from visual-style.md §7 */
    margin-bottom: 32px;
}

/* Filter bar container — sits between heading and grid */
.blog-filter-bar {
    margin-top: 32px;
    margin-bottom: 58px;                 /* heading-to-content gap before articles start */
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
}
```

**Category count rule**: Use 3–6 categories. At 7+ (Windsurf), the filter bar wraps on narrow screens and loses scannability. If there are more than 6 meaningful categories, consider grouping them into a dropdown ("More ▾").

**Evidence**: Luma AI, Legora, Cohere, Windsurf, Granola, Claude, Family
**Evidence status**: Cross-sample inference

---

## Pattern 2: Centered Minimal Header

**When to use**:
- Archetype C (Minimal List) — clean developer-focused aesthetic
- Heading centered, possibly with search input below
- No or few category filters (3–4 max)

**Layout**:
```
        [ Blog ]                          ← large heading, centered
   [ Short description ]                  ← optional subtitle, centered
     [ Search blog... ]                   ← optional search input
───────────────────────────────────────────
[ Article list ]
```

**CSS tokens**:
```css
.blog-header--centered {
    padding: 128px 32px 58px;            /* 128px top → standard large breathing space; 58px before content */
    text-align: center;
}

.blog-header--centered .blog-header-title {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
    margin: 0 auto 16px;
}

.blog-header--centered .blog-header-subtitle {
    font-family: var(--font-body);
    font-size: 18px;
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    max-width: 540px;                    /* from visual-style.md §7 */
    margin: 0 auto 32px;
}

/* Search input */
.blog-search {
    display: flex;
    max-width: 480px;
    margin: 0 auto;
    border: 1px solid var(--surface-2);
    border-radius: 160px;                /* search bar pill — from visual-style.md §4 */
    overflow: hidden;
    background: var(--bg);
}
.blog-search input {
    flex: 1;
    padding: 8px 20px;
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    border: none;
    background: transparent;
    color: var(--text);
    outline: none;         /* hides default ring — the wrapper .blog-search provides focus styling */
}
.blog-search:focus-within {
    border-color: var(--text);   /* wrapper border darkens when input has focus */
    outline: 2px solid var(--text);
    outline-offset: 2px;
}
.blog-search input::placeholder {
    color: var(--text);
    opacity: 0.4;
}
```

**Search note**: 3/13 products include search (Better Stack, Cohere, Claude). The keyboard shortcut hint "/" is worth adding — it signals discoverability to developer audiences (Better Stack). Omit for content-marketing blogs; developers find search more useful than topic browsing.

**Evidence**: Better Stack, Claude, Granola, Family (centered), Cursor (sidebar variant)
**Evidence status**: Cross-sample inference

---

## Pattern 3: Split Header (Editorial)

**When to use**:
- Archetype B (Editorial) when the blog has a distinct brand identity or sub-brand name
- Heading + description on left, optional visual element or navigation on right
- 2/5 index headers in Round 6 use this approach

**Layout**:
```
[ Blog (small label) ]  |  (navigation or visual)
[ Life Inside Dropbox ] |
[ Subtitle text...    ] |
```

**CSS tokens**:
```css
.blog-header--split {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 58px;                           /* standard title-to-content gap used for column gap */
    align-items: center;
    padding: 128px 32px 58px;            /* 128px hero top whitespace; 58px heading-to-content before the grid — visual-style.md §3 */
}

/* Label above heading */
.blog-header-label {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;                        /* label opacity — from visual-style.md §1 */
    margin-bottom: 12px;
}

.blog-header--split .blog-header-title {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
    margin-bottom: 24px;
}

.blog-header--split .blog-header-subtitle {
    font-family: var(--font-body);
    font-size: 18px;
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    max-width: 540px;
}
```

**When not to use**:
- Blog has more than 4 category filters — split layout has no room for a full filter row
- Archetype A or C — split headers are editorial in character

**Evidence**: Dropbox ("Life Inside Dropbox"), Dropbox WIP ("Work Culture" category view)
**Evidence status**: Single source observation (treat as starting point, not proven pattern)

---

## Category Filter Integration

### Filter Style Options

**Style 1: Horizontal text tabs (underline/bold active)** — 3/8 samples (Legora, Windsurf, Family):
```css
.filter-tabs {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}
.filter-tab {
    font-family: var(--font-display);
    font-size: 14px;                     /* navigation/button scale — from visual-style.md §2 */
    font-weight: 500;
    color: var(--text);
    opacity: 0.4;
    background: none;
    border: none;
    padding: 6px 0;
    cursor: pointer;
    border-bottom: 1.5px solid transparent;
    transition: opacity 0.3s linear, border-color 0.3s linear;
}
.filter-tab:hover { opacity: 1; }
.filter-tab.active {
    opacity: 1;
    border-bottom-color: var(--text);
}
```

**Style 2: Pill chips (filled active)** — 4/8 samples (OpenSea, Cohere, Performance Lab, Granola); Luma AI (Round 1) also uses pills:
```css
.filter-chips {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}
.filter-chip {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 160px;                /* pill shape — from visual-style.md §4 */
    border: 1px solid var(--surface-2);
    background: transparent;
    color: var(--text);
    opacity: 0.5;
    cursor: pointer;
    transition: opacity 0.3s linear, background 0.3s linear, border-color 0.3s linear;
}
.filter-chip:hover { opacity: 1; }
.filter-chip.active {
    background: var(--text);
    color: var(--text-inverse);
    border-color: var(--text);
    opacity: 1;
}
```

**Style 3: Left sidebar list** — 1/8 samples (Cursor), Archetype C only:
```css
/* Two-column layout: sidebar filter + main content */
.blog-layout--sidebar {
    display: grid;
    grid-template-columns: 180px 1fr;
    gap: 58px;
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
}

.sidebar-filters {
    position: sticky;
    top: calc(var(--nav-h) + 24px);     /* clear fixed nav — from visual-style.md §8 */
}
.sidebar-filter-item {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    opacity: 0.4;
    display: block;
    padding: 6px 0;
    cursor: pointer;
    transition: opacity 0.3s linear;
}
.sidebar-filter-item:hover { opacity: 1; }
.sidebar-filter-item.active {
    opacity: 1;
    font-weight: 500;
}
```

### Filter Rules

- **"All" option**: 6/8 samples include "All" as the default active filter. Always include it — some products use "Reset Filters" (Performance Lab) but this is worse UX.
- **Active state**: Bold/underline (text tabs) or filled background (pill chips). Do not use brand accent color for active state unless user provides a brand color — use `var(--text)` as fill.
- **Category count**: 3–5 is optimal (median from observations). At 6+, use horizontal scrolling or dropdown overflow.

---

## Optional Elements

### Search Input (Archetype A/C)

Position: inline with filter bar (Cohere), or below subtitle (Better Stack, Claude). Use `.blog-search` tokens from Pattern 2.

When to include: developer-focused blogs, high article volume (50+), or when the user explicitly requests it. Omit for under-30 article blogs — navigation and filters are sufficient.

### Subtitle/Description

- 3/5 blog index headers include subtitles (Better Stack, Windsurf, Claude)
- Use when the blog has a specific scope not obvious from "Blog" (e.g., "Read how we approach engineering", "Product news for teams building with Claude")
- Keep under 1 line on desktop. Use `max-width: 540px` to prevent overly long lines

### Article Count (rare)

Dropbox WIP shows "506 Articles — Page 1 of 57". Only useful for very high-volume archives (100+ articles). Omit for typical product blogs.

---

## Spacing Tokens

```
Header top padding:            128px (hero top whitespace — from visual-style.md §3)
Header-to-filter gap:          32px  (from visual-style.md §3 base scale)
Filter-to-article-grid gap:    58px  (heading-to-content gap — from visual-style.md §3)
Header subtitle max-width:     540px (from visual-style.md §7)
Filter tab gap:                8px   (from visual-style.md §3 base scale)
```

---

## Responsive Behavior (≤767px)

```css
@media (max-width: 767px) {
    .blog-header {
        padding-top: 80px;               /* 128px → 80px — from visual-style.md narrow-screen table */
        padding-bottom: 40px;
        padding-left: 20px;
        padding-right: 20px;
    }

    /* Split header → stacked */
    .blog-header--split {
        grid-template-columns: 1fr;
        gap: 24px;
        padding-top: 80px;               /* 128px → 80px — from visual-style.md narrow-screen table */
    }

    /* Sidebar layout → stacked (filter above content) */
    .blog-layout--sidebar {
        grid-template-columns: 1fr;
        gap: 32px;
        padding-left: 20px;
        padding-right: 20px;
    }
    .sidebar-filters {
        position: static;
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }
    .sidebar-filter-item {
        padding: 4px 12px;
        border: 1px solid var(--surface-2);
        border-radius: 160px;
    }

    /* Filter chips may overflow — allow horizontal scroll */
    .filter-chips {
        flex-wrap: nowrap;
        overflow-x: auto;
        padding-bottom: 8px;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
    }
    .filter-chips::-webkit-scrollbar { display: none; }
}
```

---

## Evidence

| Pattern | Products | Archetype |
|---------|----------|-----------|
| Classic heading + horizontal filter tabs | Windsurf, Cohere, Legora | A |
| Classic heading + pill chips | Luma AI, Granola, OpenSea | A |
| Centered minimal heading | Better Stack, Claude, Family | C |
| Centered + search | Better Stack, Claude | C |
| Split editorial header | Dropbox, Dropbox WIP | B |
| No header (featured article IS header) | MOUTHWASH | B |
| Sidebar filter + text list | Cursor | C |
