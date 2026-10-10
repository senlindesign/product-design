# Blog Page Archetypes & Selection Guide

> Source: Mobbin research synthesis across 55+ blog index pages (2026-10-02). Products observed include: Paraform, Luma AI, Dropbox, Basedash, folk, Legora, Cohere, Windsurf, WhatsApp, Framer, Epidemic Sound, MOUTHWASH Studio, The Performance Lab, Cursor, Plain, Harvest, Shade, OpenSea, Lemon Squeezy, Granola, Family, OpenAI, Better Stack, Teachable, Mural, Webflow, Superhuman Mail, Duolingo, Apollo, Hashnode, Height, Linear, Anchor, adidas, OpenTable, ClassPass, Clockwise, Sprig, ElevenLabs.

---

## Key Structural Principle

A blog page is a **content navigation interface**, not a persuasion funnel. The section ordering follows:

```
orient → filter → browse → discover → subscribe
```

Not: awareness → interest → trust → action. The page is not trying to convert visitors — it is helping them find articles to read.

---

## Archetype Definitions

### A. Grid Index (~35%)

**Typical products**: Paraform, Luma AI, Dropbox, Basedash, folk, Legora, Cohere, Windsurf, WhatsApp, Apollo, Anchor
**Core characteristic**: Standard SaaS blog. Article cards in a 2–3 column grid. Each card has thumbnail, title, date, and optional category tag. Category filter tabs above the grid. Optional featured article at top.

**When to use**:
- [ ] Product publishes diverse content types (Engineering, Product, Company, Customer Stories)
- [ ] Content includes images or screenshots that benefit from thumbnail display
- [ ] Publishing cadence is moderate to high (10+ articles visible)
- [ ] Audience is mixed (practitioners and decision-makers), not exclusively developers
- [ ] Default choice when no strong signal points to B or C

**Typical section composition**:
1. Navigation (fixed, frosted glass)
2. Blog Header (page title + optional subtitle)
3. Category Filter Tabs (horizontal tabs above grid, "All" + 3–7 categories)
4. [Featured Article] (optional — 1 large card or asymmetric 1+2 layout before the grid)
5. Article Card Grid (2–3 columns, thumbnail + title + date + optional excerpt)
6. [Pagination] (numbered or load-more at bottom — only when the blog has 10+ articles; fewer than 10 → show all, no pagination)
7. [Newsletter Section] (optional — bottom of page, above footer)
8. Footer

**Visual tendencies**:
- Light theme dominant (~70% of A archetype samples)
- Cards on `var(--bg)` or `var(--surface-1)` background, `border-radius: 16px`
- Thumbnails are landscape (16:9 or 4:3), not portrait
- Category tags as small mono-uppercase labels or inline pill on thumbnail, not colorful
- Card metadata: title (bold, 20px) + date + category; excerpt optional (2–3 lines max)
- Minimal chrome — cards have no visible borders, zero shadow
- Section background does NOT alternate per section (blog content provides its own rhythm)

**Evidence**: Paraform (3-col, numbered pagination, 13 pages), Luma AI (3-col, category pills, "Read article" CTA), Cohere (6 categories + search, featured + 3-col grid), Windsurf (7 categories, featured + 3-col grid, load-more), WhatsApp (3-col with excerpt + "Read more"), Legora (3-col, portrait thumbnails)

---

### B. Editorial (~30%)

**Typical products**: Framer, Epidemic Sound, MOUTHWASH Studio, The Performance Lab, Dropbox Work in Progress, Teachable, Mural, Webflow, Superhuman Mail, Duolingo, Hashnode
**Core characteristic**: Magazine layout. A large hero article dominates the first fold. Varied card sizes (large/medium/small) create visual rhythm. Emphasis on photography and typography. Often the featured article IS the page header — no separate "Blog" title.

**When to use**:
- [ ] Content marketing is a primary brand channel (design studio, media company, established product brand)
- [ ] Articles are image-rich (case studies, design process, long-form editorial)
- [ ] Publishing quality matters more than publishing frequency
- [ ] Brand identity is strong enough to carry a distinct visual voice in the blog

**Typical section composition**:
1. Navigation (fixed, frosted glass)
2. Featured Article Hero (large — either split/asymmetric grid, or full-bleed/full-width; NO separate "Blog" heading in many cases — the page still keeps exactly one h1, see SKILL.md Implementation Principles)
3. [Category Filter Tabs] (optional — horizontal below featured hero, or in nav. Because the filters sit below the featured hero, filtering never hides the hero — only the grid filters)
4. Article Grid (varied card sizes: 2-col or 3-col with featured spanning full width)
5. [Pagination] (load-more button more common than numbered pages — only when the blog has 10+ articles)
6. [Newsletter Section] (optional)
7. Footer

**Visual tendencies**:
- Dark theme appears more often in B than in A or C (Framer, Superhuman, Epidemic Sound). Dark theme also appears in Archetype A (Basedash, Shade)
- Featured hero may be full-width (extends to viewport edge) or content-width (stays in grid)
- Large featured hero shows: title (large, ~32-40px) + category label + author; no excerpt (0/7 featured heroes have excerpts — they are title-dominant)
- Smaller cards below the hero may have excerpts (1–2 lines)
- Featured hero does NOT use an explicit "Featured" label (only 2/7 do — Mural and Duolingo)
- Image-first: thumbnails dominate over text in card composition
- Mono uppercase for category labels and author attribution (Epidemic Sound, Superhuman)

**Archetype B without images**: B depends on real imagery. If the blog genuinely has no images (text posts, code, changelog), choose A with text-only cards or C instead — see the Decision Matrix row "No images". If the blog has images that were simply not supplied for this build, keep B with thumbnail placeholders that step one surface from their container (`var(--bg)` inside a `var(--surface-1)` card — `shared/visual-style.md` Surface nesting rule) plus a mono label, and do not use the full-bleed overlay hero (`featured-article.md` Pattern 2 Layout B), which needs real photo contrast. Text-only top-row cards (Epidemic Sound) are the one observed image-free B treatment — typography carries the hierarchy.

**Evidence**: Framer (2+3 mixed grid, dark, borderless thumbnails), Epidemic Sound (2 text-only cards + 3 image cards, dark), Superhuman (full-width dark hero with large photo right), Mural (featured card + text-only "New" list in right column), Performance Lab (full-bleed photo hero, text overlay on all cards)

---

### C. Minimal List (~35%)

**Typical products**: Cursor, Plain, Harvest, Shade, OpenSea (changelog), Lemon Squeezy, Granola, Family, OpenAI, Better Stack, Height, Linear (changelog section)
**Core characteristic**: Text-dominant. Title + date list, no or small thumbnails. Clean and scannable. Often used for changelogs, developer-focused blogs, or products where content is text-heavy.

**When to use**:
- [ ] Primary audience is developers or technical users
- [ ] High publishing frequency (changelogs, weekly updates) — scannability is the priority
- [ ] Content is text-heavy and doesn't benefit from thumbnail preview
- [ ] Brand aesthetic leans minimal/typographic (Cursor, Plain, Lemon Squeezy)
- [ ] Articles mix content types in one list (blog posts + changelogs + press releases)

**Typical section composition**:
1. Navigation (fixed, frosted glass)
2. Blog Header (prominent heading — "Blog" / "Journal" / "Changelog"; may include search input)
3. [Category Filter] (optional — compact pills or sidebar; 3–5 categories max)
4. Article List (full-width rows; each row: date + title + optional excerpt)
5. [Pagination] (text-based "Older posts" / "Page X of Y", or Load More button — only when the blog has 10+ articles)
6. [Newsletter Section] (optional — compact, bottom of page)
7. Footer

**Visual tendencies**:
- No thumbnails (4/7 C-archetype samples) or small thumbnails (~48–80px square, not dominant)
- Larger title sizes compensate for no thumbnails: 24–32px titles vs 20px in grid cards
- Date is universal (7/7 C samples) — often left-column or inline before title
- Two extremes for excerpts: full paragraph (Harvest, OpenSea) or none at all (Lemon Squeezy, Shade) — rarely 2-line truncated middle
- Thin divider lines between entries (Family, Lemon Squeezy) — the only decorative element allowed
- Search input in header is common (Better Stack, Claude) — helps navigation in high-volume lists
- Category sidebar (left column) is C-exclusive: Cursor uses a left sidebar with 5 categories
- Emoji prefix on titles is a personality variant (Granola: 🪄, Lemon Squeezy: 🍋) — use only if brand supports it

**Evidence**: Cursor (left sidebar categories, text list with excerpt + date), Plain (date-margin layout, "Journal" heading, hashtag pills), Harvest (full-width text, full excerpts, 26-page numbered pagination), Lemon Squeezy (title + date on same line, thin dividers, emoji prefix), OpenSea changelog (blue link titles, full descriptions)

---

## Decision Matrix

| Signal | → Archetype |
|--------|------------|
| Default SaaS blog with diverse content categories | A |
| Has product screenshots or photography worth showing | A |
| Mix of audiences (technical + business) | A |
| Design studio / media brand with strong visual identity | B |
| Publishes long-form, image-rich editorial content | B |
| Content marketing is a primary brand differentiator | B |
| Primary audience is developers | C |
| Changelog or high-frequency release notes | C |
| "No images" — content is text-only or code snippets | C |
| Brand aesthetic is typographic / minimal | C |

**Quick rule**: Start with A. If content is explicitly editorial and image-heavy → B. If audience is developers or content is changelog-style → C.

---

## Archetype Does NOT Override

The following inputs from the user or brand always take priority over archetype defaults:

- **Brand color** → override `--accent` and `--accent-text`; use on CTA button; keep <10% page area
- **Dark/Light theme** → any archetype can use either theme; dark is slightly more common in B and C
- **Page title text** → use the user-provided text verbatim ("Blog" / "Journal" / "Articles" / "Resources" / "Insights")
- **Category names** → use the user-provided category names exactly; do not invent categories
- **Article count** → if the user says 5 articles, do not generate 12 placeholder cards
- **Existing content** → if the user provides actual article titles and dates, use them; do not fabricate article titles
