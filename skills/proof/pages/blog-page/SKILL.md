# Blog Page Skill

Generate a runnable blog index / listing page with professional visual quality. No Mobbin or external service required at runtime.

**Visual System**: see `shared/visual-style.md` — defines the default design tokens (colors, typography, spacing, components) for Light and Dark themes. Blog-specific component tokens (article cards, category filters, featured article, newsletter) are in `references/`. Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.

---

## When to Use This Skill

Use this Skill when the user asks you to create a blog index page, articles listing page, or content hub page for a website. This includes:
- "Make a blog page for [product]"
- "Create an articles listing page"
- "Build a changelog / updates page"
- "Design the blog for [tool/platform]"

Do NOT use this Skill for:
- Individual blog post / article pages (that is a separate Skill — article detail page)
- Landing pages (use Landing Page Skill)
- Documentation / help center pages
- News aggregator or RSS reader interfaces

---

## Workflow

### Step 1: Understand the Task

Gather these inputs from the user's request. Do not ask questions in this step — the master skill decides whether to ask (its Step 1). For each input the user does not give, use the default below; facts that are missing become labeled placeholders.

**Required** (must be clear from request or ask):
- Product name and one-line description
- Content type signal: what kind of content does this blog publish? (product updates, engineering posts, case studies, general company news, changelog)

**Use defaults if not provided**:
- Target audience → infer from description (mixed, developer-focused, content marketing)
- Number of articles to display → 6–9 for grid, 8–12 for list
- Categories → 3–5 generic categories (e.g., Product, Engineering, Company, Guides)
- Brand color → **default is the active style's own accent** (Minimal: no brand color, `--accent` = `--text`; Editorial: teal `#20808D`). Only override if user explicitly provides one — see the active style file's Brand Customization section (Minimal: `visual-style.md` §10.1)
- Display font → **default is the active style's display font** (Minimal: DM Sans). Only override if user provides a specific font name — see the active style file's Brand Customization section (Minimal: `visual-style.md` §10.2)
- Technology stack → single HTML file with inline CSS
- Theme → Light (default for most), Dark (for developer tools, dark-brand products)
- Featured article → include if Archetype A or B; omit for C
- Newsletter → include if user mentions subscriber capture; omit by default

**Brief context** (when called from the master skill):

When the master skill passes a project brief (audience, goal, barriers, evidence), use it in archetype selection (Step 2) and section composition (Step 3):
- Content type (marketing content, technical posts, changelog) → archetype and card style
- Audience (general visitors, developers, existing customers) → layout complexity and filter needs
- Publishing cadence and volume → whether search and pagination are needed
- Whether subscriber capture is a goal → newsletter section inclusion

### Step 2: Select Archetype

Read `references/archetypes.md` and classify the product:

| Signal | Archetype | Default Theme | Core Layout |
|--------|-----------|---------------|-------------|
| Diverse content categories, images/screenshots available, moderate publishing cadence | A. Grid Index | Light | Header → filters → [featured] → card grid → pagination |
| Design/creative brand, visually rich content, content marketing focus | B. Editorial | Light or Dark | [Featured hero] → mixed-size cards → pagination |
| Developer audience, high-frequency updates, changelog, text-heavy content | C. Minimal List | Light or Dark | Header → [filters] → text list → pagination |

**Default: A** (Grid Index). Choose B when the brand is visually rich and content is image-heavy. Choose C when the audience is developer-focused or the content is changelog-style.

**Brief-informed selection**: When a project brief is available, apply these rules. When a rule matches, it takes priority over the signal table above:
- Brief indicates developer-focused content or changelog → C. Minimal List (even if images are available)
- Brief indicates content marketing with rich visuals → B. Editorial
- Brief indicates subscriber growth as a goal → include newsletter section regardless of archetype

A blog page is a **content navigation interface**, not a persuasion funnel. The page flow is:
```
orient → filter → browse → discover → subscribe
```

### Step 3: Compose Sections

Based on the archetype, decide which sections to include. Read `references/section-composition.md` for ordering rules, then read the relevant `references/*.md` files for each selected section.

**Always include**:
1. Navigation (fixed, frosted glass)
2. Blog Header (page title, optional subtitle) — in Archetype B you can omit it and let the featured hero lead; the page still keeps exactly one h1 (see Implementation Principles)
3. Article listing (cards or list entries — the core of the page)
4. Footer

**Pagination rule (single source — applies to every archetype)**: include Pagination (numbered, load-more, or text-based — see `references/section-composition.md` §6) when the blog has 10 or more articles in total; the rendered cards are page 1. When the blog has fewer than 10 articles, render all of them and omit pagination. The count is the blog's total, not the number of cards on screen; if the user lists specific articles and says nothing about more, treat that list as the whole blog; only when the user gives neither a list nor a count, treat the blog as ongoing (10+) and include pagination. A "Load more" button counts as pagination.

**Add based on archetype and content**:
- Category Filter Tabs → Archetype A: include by default (3–7 categories). B: include when articles span 3+ categories. C: include when the blog has 10+ articles
- Featured Article → Archetype A: include when the user names a featured article (1 large card or split layout above the grid). B: include by default (large hero). C: omit
- Newsletter Section → All archetypes (optional, bottom of page above footer). Include only if user requests subscriber capture
- Search Input → Archetype C (optional, for high-volume developer blogs)
- Newsletter Section → if brief identifies subscriber capture as a goal, include regardless of archetype
- Search Input → if brief indicates high content volume (50+ articles), include for any archetype

**Remove if**:
- Fewer than 3 categories exist → skip category filter
- Fewer than 10 articles in total → skip pagination and show all (see Pagination rule above)
- No subscriber capture goal → skip newsletter section
- Archetype C with few articles → skip featured article
- Brief indicates the blog is a changelog or release notes → skip featured article, simplify to chronological list
- Brief indicates no images or thumbnails available → use Archetype C (Minimal List) or text-only cards for Archetype A. Do not pick Archetype B for an image-less blog — see "Archetype B without images" in `references/archetypes.md`

### Step 4: Generate Page Spec

Before writing code, produce a brief spec:

```
Page Spec:
- Product: [name] — [one-line description]
- Archetype: [A/B/C] — [name]
- Theme: Light / Dark
- Sections (in order): [list]
- Grid: [2-col / 3-col / list] — [with/without thumbnails]
- Categories: [list or "none"]
- Featured article: [yes/no]
- Pagination: [numbered / load-more / "Page X of Y" / none (fewer than 10 articles)]
- Newsletter: [yes/no]
- Brand color: none (default) / [color]
- Display font: default (DM Sans) / [font name]
- Not in scope: [real content filtering, server-side pagination, CMS integration]
```

### Step 5: Build the Page

**First**: Read the active style file in full — `shared/visual-style.md` (Minimal, the default), or `shared/visual-style-business.md` / `shared/visual-style-colorful.md` / `shared/visual-style-editorial.md` when the master skill selected another style. Every CSS value must come from its tokens.

**Then**: Read `shared/interaction-patterns.md` for animation recipes (scroll reveal, card stagger, hover lift).

For each section, read the corresponding `references/*.md` knowledge file, select the pattern that matches the archetype and content, implement strictly following design system tokens, and check against `references/anti-patterns.md`.

> **The token blocks below are Minimal defaults.** With another style active, apply *Style precedence* from the master `SKILL.md`: visual values (fonts, weights, colors, radius, shadow, spacing rhythm, button and card styling) come from the active style file; layout, structure, and content rules here still apply.

#### Design System Tokens (must follow)

```
Fonts:     var(--font-display) default DM Sans + var(--font-mono) default DM Mono + system sans (body)
Weights:   500 (display/nav/button) + 400 (mono/body) — no other weights
Colors:    Light: #FFF / #F5F5F5 / #E9E9E9 / #141414
           Dark:  #0A0A0A / #141414 / #1F1F1F / #EDEDED
           Text hierarchy via opacity (1 / 0.5 / 0.4 / 0.3 / 0.15), NOT different grays
Accent:    var(--accent) default = var(--text) + var(--accent-text) default = var(--text-inverse)
Spacing:   Section rhythm 180px, hero top 128px, title-to-content 58px
Radius:    Buttons 2px, feature cards 8px, content cards 16px
Shadows:   ZERO — depth via background color steps only
Motion:    scroll entrance 0.8s, card stagger 100ms, counter 2000ms (see shared/interaction-patterns.md)
Grid:      max-width 1080px, gutter 24px
```

#### Blog-Specific Tokens

```
Blog header:     padding-top 128px (hero top whitespace), heading clamp(32px, 4vw, 47px)
Article card:    16px radius, 32px card padding, thumbnail aspect-ratio 16/9 or 4/3
Card metadata:   12px mono uppercase, opacity 0.4, letter-spacing 0.72px
Card heading:    20px display weight 500
Card excerpt:    16px body weight 400, opacity 0.5, -webkit-line-clamp: 2
Category tabs:   14px display weight 500, opacity 0.4 default → 1 active
Pagination:      14px mono, numbered or load-more button
Newsletter:      180px section padding, section heading scale, single email input + btn-dark
```

#### Implementation Principles

- Semantic HTML (exactly one h1 per page, naming the blog; article cards in `<article>` elements, nav, footer). In Archetype A and C the h1 is the Blog Header title. When Archetype B drops the Blog Header, the h1 does not disappear: render the blog name as the h1 using the label token (`.blog-header-label` in `references/blog-header.md` Pattern 3 — 12px mono uppercase, opacity 0.4, margin-bottom 12px) directly above the featured block; the featured title is then an h2 and grid card titles are h3. Do not promote the featured article title to h1 (it does not name the page and changes when the post rotates)
- Mobile-responsive (flexbox/grid, breakpoint at 767px (`@media (max-width: 767px)`) — grid collapses to 1-col)
- Single HTML file with inline `<style>` — include Google Fonts link for DM Sans + DM Mono
- Placeholder content: generate example article titles and excerpts clearly noted as placeholder. Thumbnail placeholders step one surface level relative to their container (`shared/visual-style.md` §8 Surface nesting rule): inside a `var(--surface-1)` card or band, the placeholder uses `var(--bg)`; directly on a `var(--bg)` page (e.g., Archetype C small-thumbnail rows), it uses `var(--surface-1)`. Add a mono-font label. Never give a placeholder the same surface as its parent — it disappears
- Category filtering: implement with vanilla JS — show/hide cards based on `data-category` attribute. "All" shows everything. No page reload. **Where the featured block sits decides whether it hides**:
  - Featured block **below** the filter bar (Archetype A: Header → Filters → Featured → Grid) — it is part of the filtered area and is multi-category, so hide it while a specific category is active. Mark it `data-hide-on-filter`.
  - Featured block **above** the filter bar (Archetype B: Featured hero → Filters → Grid) — keep it visible and filter only the grid. Hiding content above the clicked control shifts the whole page up (≈450px in testing) and moves the chip out from under the cursor. Do not mark it, and do not put `data-category` on its cards.
  - Mixed-size grids built from row containers (Archetype B `.editorial-top-row` / `.editorial-bottom-row`) — when filtering hides every card in a row, collapse that row so its `margin-bottom` leaves no empty gap. Mark each row container `data-filter-row`.

  Use this stub:
  ```js
  (function() {
      var filters  = document.querySelectorAll('[data-filter]');
      var cards    = document.querySelectorAll('[data-category]');
      var hideable = document.querySelectorAll('[data-hide-on-filter]'); // featured block only when it sits below the filter bar
      var rows     = document.querySelectorAll('[data-filter-row]');     // row containers of a mixed-size grid

      filters.forEach(function(btn) {
          btn.addEventListener('click', function() {
              var cat = btn.dataset.filter;
              filters.forEach(function(b) {
                  b.classList.remove('active');
                  b.setAttribute('aria-pressed', 'false');
              });
              btn.classList.add('active');
              btn.setAttribute('aria-pressed', 'true');
              cards.forEach(function(card) {
                  card.style.display = (cat === 'all' || card.dataset.category === cat) ? '' : 'none';
              });
              hideable.forEach(function(el) {
                  el.style.display = (cat === 'all') ? '' : 'none';
              });
              rows.forEach(function(row) {
                  var anyVisible = Array.prototype.some.call(
                      row.querySelectorAll('[data-category]'),
                      function(card) { return card.style.display !== 'none'; }
                  );
                  row.style.display = anyVisible ? '' : 'none';
              });
          });
      });
  })();
  ```
  Add `data-filter="all"` / `data-filter="engineering"` to filter buttons (use `<button type="button" aria-pressed>`); `data-category="engineering"` to each filterable article card.
- Pagination: for static HTML, show the first page with numbered pagination UI (non-functional links). Add `<!-- Pagination is visual-only in this static build -->` comment
- Entrance animations: scroll reveal + child stagger + card hover lift per `shared/interaction-patterns.md` — all wrapped in `prefers-reduced-motion`, use the combined script template
- Blog header and category filters do NOT get scroll reveal animation (they are above the fold)

#### Content Handling

- Use the user's real content (article titles, categories, dates) when provided
- Generate placeholder content when not provided — clearly note it is example content
- **Never fabricate**: real author names, real publication dates claiming to be real, real article excerpts presenting opinion as fact
- When the user gives no article titles, write generic, obviously placeholder titles: "Getting Started with [Product]", "What's New in v2.0", "[Product] for Enterprise Teams"
- Use placeholder dates from recent months, and list them as placeholders in the QA report

### Step 6: Verify

After generating the page, run through `shared/quality-checklist.md`. Blog-specific critical items:

> Visual checks below (color, shadow, radius, typography, spacing values) are written for Minimal. With another style active, check them against the active style file instead. Visual rules in `references/anti-patterns.md` follow the same precedence; content and structure rules apply in every style.

1. **Card uniformity**: Are all cards in the grid the same height (or aligned by row)? No jagged grid edges
2. **Category filter**: Does the "All" tab show all articles? Does clicking a category show only matching articles? Is the active state visible?
3. **Pagination UI**: Is pagination present only when the blog has 10+ articles (and absent below 10)? Is it centered below the grid? Does it look like real pagination (not a random list of numbers)?
4. **Thumbnail placeholders**: Does each placeholder step one surface level from its container (`var(--bg)` inside a `var(--surface-1)` card; `var(--surface-1)` on a `var(--bg)` page) with a mono-font label? No broken image icons, no placeholder that blends into its card
5. **Featured article** (if present): Is it visually larger/more prominent than regular grid cards? Does it sit above the card grid? Click each category chip: if the featured block sits above the filter bar (Archetype B), does it stay put with no page jump? Does an emptied grid row collapse?
6. **Heading outline**: Exactly one h1, naming the blog — including Archetype B pages with no Blog Header?
7. **Newsletter** (if present): Does it use 180px section padding? Is the email input styled consistently with the design system?
8. **Content navigation feel**: Does the page feel like a browsing interface, not a conversion funnel? No sales language in the header
9. **Animation check**: Cards have scroll reveal + stagger? Hover lift activates after entrance completes? No animation on nav/footer?

If issues are found, fix them before delivering.

### Step 7: Deliver

Provide:
1. The HTML file with instructions to open in a browser
2. A brief note on key design decisions (archetype choice, grid layout, category handling)
3. What's in scope (visual presentation, client-side category filtering) vs. not implemented (server-side pagination, CMS integration, real content loading, search functionality)

---

## Knowledge Files

| File | Content | When to Load |
|------|---------|-------------|
| `shared/visual-style.md` | **Design system**: default tokens, Light/Dark themes, component styles | Step 5 (always — read FIRST) |
| `shared/interaction-patterns.md` | **Motion system**: scroll reveal, stagger, counter, hover lift recipes | Step 5 (always — animation implementation) |
| `references/archetypes.md` | 3 archetypes (A Grid Index / B Editorial / C Minimal List), signals, section composition | Step 2 (always) |
| `references/article-card.md` | Card layout patterns (vertical grid, horizontal row, editorial mixed, minimal list), metadata display, typography tokens | Step 5 (always — the core component) |
| `references/blog-header.md` | Page header patterns, category filter CSS (3 styles: text tabs, pill chips, sidebar list), search input | Step 5 (always) |
| `references/featured-article.md` | Featured article patterns (split grid, full-width hero, bleed hero), metadata, spacing | Step 5 (if featured article is included) |
| `references/newsletter-section.md` | Newsletter patterns (bottom section, inline card, sidebar), email form component, copy strategies | Step 5 (if newsletter is included) |
| `references/section-composition.md` | Section ordering per archetype, grid layout rules, pagination patterns, spacing summary | Step 3 (always) |
| `references/anti-patterns.md` | 12 anti-patterns: uniform grid trap, colorful category tags, card shadows, content fabrication, etc. | Step 5 (always — verify each design choice) |
| `shared/quality-checklist.md` | verification checklist | Step 6 (always) |

Navigation and Footer knowledge lives in `shared/navigation.md` and `shared/footer.md`. Reuse the same nav and footer patterns.

---

## Constraints

- This Skill does NOT require Mobbin, external APIs, or internet access
- V1 scope: page skeleton + layout + components + visual quality
- NOT in V1: server-side pagination, CMS integration, real search, content loading API, real form submission
- Output: runnable frontend code (HTML/CSS/vanilla JS, or matching the user's project stack)
- All design knowledge is pre-distilled in the references/ directory
- Visual style defaults to the shared design system tokens; user-provided brand specs override only the specific values they specify
- Category filtering uses vanilla JS (`data-category` attribute + class toggle). No framework required
- Pagination is visual-only in static HTML builds — the UI is rendered but links are non-functional
- Article content is placeholder unless the user provides real content
