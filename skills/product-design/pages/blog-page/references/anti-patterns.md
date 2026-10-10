# Blog Page Anti-Patterns & AI Convergence Traps

> Source: Mobbin research synthesis across 55+ blog index pages (2026-10-02). Every rule is grounded in observed product behavior.

---

## 1. The Three-Column Uniform Grid Trap

**Wrong**: Every blog defaults to 3 equal-width cards, each with 16:9 thumbnail + category pill + title + excerpt + date + author. The grid looks like a cookie-cutter template.

**Right**: Column count and card density are driven by content volume and type. 2-col works when cards have 3+ line excerpts (Basedash, Aboard). 3-col works for compact cards with title + date only (Paraform, WhatsApp). Mixed column sizes (B archetype) work when editorial hierarchy is the goal. Minimal list (C archetype) uses a single column with no grid at all.

**Evidence**: Framer uses 2+3 mixed grid with varied thumbnail sizes to create rhythm. Legora uses portrait thumbnails (not landscape) — the grid adapts to content, not the other way around.

**Check**: Can you justify the column count based on the content's information density? If no, reduce to 2-col or question whether grid is right at all.

---

## 2. Colorful Category Tags

**Wrong**: Each category tag has a distinct background color (blue for Engineering, green for Design, orange for Product). The category pill on the card thumbnail uses the category's signature color.

**Right**: Category labels use the mono-uppercase `.label` style: `font-family: var(--font-mono); font-size: 12px; letter-spacing: 0.72px; text-transform: uppercase; color: var(--text); opacity: 0.4`. No background colors, no colored pills.

**Why the wrong pattern exists**: Aboard and OpenSea use colored category pills — these are counterexamples, not the norm. 4/8 first-round samples show categories, and most use text labels (Framer: text label, Epidemic Sound: mono uppercase, Windsurf: text label). Colored pills violate the `--accent` allowed-use list in `shared/visual-style.md` §1 — icon backgrounds and badge fills are explicitly forbidden.

**Exception**: If the user provides a brand color and explicitly requests colored category pills, apply `--accent` to the active/selected filter tab only — not to all category labels on all cards.

---

## 3. Card Shadow and Border Decoration

**Wrong**: Each article card has `box-shadow: 0 4px 20px rgba(0,0,0,0.1)` or a visible `1px solid #E5E5E5` border. Cards "lift" off the page with heavy shadows.

**Right**: Zero shadows across the entire page (see `shared/visual-style.md` §5). Card hierarchy is established through background color steps (`var(--bg)` → `var(--surface-1)`) and `border-radius: 16px` (content card). On a `var(--bg)` page, cards on `var(--surface-1)` background are visually distinct without any border or shadow.

**Evidence**: Paraform, folk, Framer — all use borderless, shadow-free cards. Luma AI uses light gray page background with white cards, creating contrast without shadows.

---

## 4. Fabricated Article Content

**Wrong**: Generating article titles like "10 Ways to Improve Your Workflow", "The Future of AI in 2024", "How We Built Our Data Pipeline", fake author names like "Sarah Johnson", fake publication dates like "January 15, 2024".

**Right**: Use the titles the user gave. Otherwise write sample articles (master `SKILL.md` Design Rules → *Sample content*): specific titles about the product's own domain (not generic listicles), fictional authors, recent dates, each card tagged `data-sample` and listed in the QA report. Never real people as authors.

**Why this matters**: A blog page without real content must signal that the titles are placeholders — not generate content that looks like real editorial decisions. Fake article titles will be taken as proposed real content by the user.

**Evidence**: This is a content integrity rule, not a visual rule. Applies to all page types with content (also documented in `pages/about-page/references/anti-patterns.md`).

---

## 5. Newsletter After Every Section

**Wrong**: Newsletter email capture appears at the bottom of the Blog Header, inline between featured and grid, after every 6 cards, and again above the footer. Multiple newsletter prompts on one page.

**Right**: At most one newsletter section on the blog index. Position: bottom of page, above footer (3/8 samples). The inline placement between header and grid (Clockwise) is valid but unusual — use it only when the newsletter is the primary conversion goal of the blog page.

**Evidence**: Most blog pages have zero newsletter sections — they link to a separate newsletter page or rely on article-level CTAs. The newsletter section is an optional element, not a required one.

---

## 6. Sidebar on Every Blog

**Wrong**: Every generated blog gets a right-side sidebar with: "Popular Posts", "Categories", "Tags", "Newsletter Signup", "Recent Comments", "About the Author". This is a 2005 WordPress pattern.

**Right**: Sidebar is rare in current SaaS blog design. Cursor uses a LEFT sidebar for category filtering only (no content sidebar). Sprig uses a newsletter sidebar, but this is on the article page, not the blog index. The blog index page uses the full content width for article cards.

**Evidence**: 0/55+ observed blog index samples use a traditional right-side content sidebar. The sidebar is dead in modern SaaS blogs.

---

## 7. Gradient Overlays on Thumbnails

**Wrong**: Article card thumbnails have a dark gradient overlay at the bottom with white text overlaid on the photo, creating a magazine-photo-card effect across all cards.

**Right**: Text overlay on thumbnails is an Archetype B editorial pattern, used sparingly. Performance Lab uses it for ALL cards, but this is a design-first brand with full editorial photography. For standard SaaS blogs (Archetype A), text sits below the thumbnail, not on top. Overlay requires careful contrast control — it fails when photos are light or colorful.

**Use text overlay only when**: the product has professional photography, a dark editorial aesthetic, and the developer controls image selection (not user-provided content where image contrast cannot be guaranteed).

---

## 8. The "Featured" Label Trap

**Wrong**: Large text "FEATURED ARTICLE" above the hero card, or a badge on the card saying "Featured Post". The featured status is explicitly declared in the UI.

**Right**: 5/7 featured article patterns imply featured status through SIZE alone — no label. Only Mural and Duolingo use explicit "Featured post" / "FEATURED" labels. Size and position communicate hierarchy better than a label.

**Implementation**: Let the featured card's `grid-template-columns: 2fr 1fr` or full-width `width: 100%` do the work. Do not add a "Featured" badge or heading.

---

## 9. Pagination Style Mismatch

**Wrong**: Using numbered pagination with 100+ pages (produces `/1/2/.../97/98/99/100` — unnavigable). Using "Load More" when total article count is small (< 20) — unnecessary click.

**Right**:
- Numbered pagination: when total page count is bounded and visible (3–30 pages). Show ellipsis when 5+ pages exist.
- Load More button: when content is open-ended or when an editorial aesthetic matters more than navigation precision (Archetype B, Archetype C).
- Text-based ("Page 1 of 7", "OLDER POSTS >"): minimal lists with modest page counts.

**Evidence**: Harvest uses numbered pagination (26 pages, branded orange circles). Performance Lab uses "SHOW MORE ARTICLES" button. OpenAI uses "Page 1 of 7 / OLDER POSTS >".

---

## 10. Excerpt Truncation Inconsistency

**Wrong**: Some cards have 2-line excerpt, some have 1-line, some have none — because text content varies and `-webkit-line-clamp` is not applied. The grid looks ragged.

**Right**: Make a binary decision per archetype:
- **Include excerpts**: apply `-webkit-line-clamp: 2` consistently on all cards (16px, opacity 0.5)
- **Omit excerpts**: don't add the excerpt element at all

**Evidence**: Paraform, folk, Dropbox all omit excerpts entirely — clean and consistent. Basedash and Luma AI include excerpts with consistent truncation. Mixed approaches (some cards with, some without) were not observed in any sample.

---

## 11. Minimal List Layout Anti-Patterns

Archetype C-specific:

**Wrong (too heavy)**: Giving Archetype C blogs 16:9 landscape thumbnails, 3-column grid layout, and colored category pills — this turns a minimal list into an Archetype A. Archetype C is distinctly text-dominant.

**Wrong (too stripped)**: Generating a `<ul>` with `<li>Title</li>` and no visual structure — no date, no spacing, no dividers. This is technically minimal but looks broken.

**Right**: The minimal list has a clear typographic structure. Date is always present. Title is larger than grid cards (24–28px vs 20px). Divider lines (`border-top: 1px solid var(--surface-2)`) or generous margin (`margin-bottom: 32px`) separate entries.

**Evidence**: Plain uses `date-margin | title + hashtag-tag` layout. Family uses `date | title | excerpt` in 3 columns. Lemon Squeezy uses `title · · · · date` on the same line.

---

## 12. Brand Color Reconciliation

How `--accent` applies to blog elements:

| Element | Correct use of --accent | Forbidden |
|---------|------------------------|-----------|
| Newsletter CTA button | `background: var(--accent)` — allowed | Color the button border, not the background |
| Active category tab | `background: var(--text)` (default) or `var(--accent)` (brand override, 1 element) | Using --accent for all tabs or ALL category labels |
| Pagination active page | `background: var(--text)` (default) or `var(--accent)` (brand override — Harvest orange, Anchor green) | Coloring all page numbers |
| Category tags on cards | Never use --accent — use `color: var(--text); opacity: 0.4` | Colored tag pills |
| Article card hover border | `border-color: var(--text)` — use text, not accent | Accent-colored card borders |

Total chromatic area on blog pages must be <10% of visible page area — the same rule as all other page types.

---

## Verification Checklist

Before delivering the generated blog page, confirm:

1. **No shadow**: Does any card, thumbnail, or form element use `box-shadow`? Remove all.
2. **No colorful category tags**: Are category labels mono-uppercase with opacity 0.4, not colored pills?
3. **Excerpt consistency**: Are all cards either all-with or all-without excerpts? No mixed states.
4. **Placeholder content integrity**: Are article titles clearly placeholder text, not fabricated real-sounding content?
5. **Pagination matches volume**: Does the pagination style match the implied content volume?
6. **At most one newsletter**: Is the newsletter section present at most once, and only if the brief calls for it?
7. **Section backgrounds**: Is the page using `var(--bg)` throughout with at most one `var(--surface-1)` break for the newsletter?
