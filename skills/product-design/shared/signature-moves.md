# Signature Moves and Section Rhythm

> Read this after the page skill has chosen its archetype and section list, and before you build sections.
> It does two jobs: (1) it stops every section from using the same layout, and (2) it gives the page one or two memorable moments.
>
> Evidence: Mobbin Sites research, 2026-10-08 — 32 signature-move observations and 8 page-rhythm reconstructions (about 125 section images). Numbers in **Evidence** lines are counts from that sample. Sizes are visual estimates from screenshots, not measured CSS. Lines marked *Inference* are a reading across samples, not a proven rule.

**Precedence.** This file decides *layout variety and emphasis*. It never overrides the active style file (colors, fonts, radii, shadows, spacing) or the master Design Rules (no fabricated evidence, sample content tagging, real logos only). Where a move needs a value, it names a **style role** — look the value up in the active style file. Where no role exists, the move says so (see "Values not in any style file" at the end).

---

## 1. The problem this file fixes

Generated pages tend to repeat one module: small label → centered heading → subtitle → three equal cards. Each section is correct; the page is forgettable.

**Evidence:**
- Of 21 adjacent section pairs seen in one screenshot, only **2 (≈ 10%)** repeat the same layout. Both are from one page (an older Cursor homepage, three stacked "centered heading + screenshot" sections), and that page reads as monotone.
- **≈ 13 of 21 (≈ 60%)** boundaries change the background.
- In the ≈ 8 boundaries where the background stays the same, the layout changes in 6.
- Bold sections per page on 7 SaaS sites: median **≈ 2**. The hero is bold on 6 of 7. The second bold section is usually a walkthrough (sticky list or tabs), a color-band quote, or a big-type band.
- Ramp is the closest real match to the forgettable pattern: 4 of 7 section types are 3-up card grids, ≈ 0–1 bold sections. It still looks professional because of four compensators: background alternation, mixed-width bento, real product fragments in cards, and a carousel. *Inference:* restrained is a valid strategy for finance and trust products; it fails only when it is the *only* strategy and has no compensators.

---

## 2. Rhythm rules (checkable)

These apply **between top-level content sections** — every `data-section` element between the nav and the footer, including the hero. They do not apply to rows inside one section: a series inside a section (three steps with the image on the same side, a set of numbered modules) is normal. *Evidence:* Ditto keeps its 3 step images on the same side; Linear's newer pages repeat one numbered module.

### 2.1 Markup

Every content section carries three attributes next to `data-section`:

```html
<section data-section="features" data-layout="bento" data-bg="alt" data-bold="true">
```

| Attribute | Values | Meaning |
|---|---|---|
| `data-layout` | one tag from §2.2 | The section's dominant layout |
| `data-bg` | `base` · `alt` · `dark` · `scene` | Which background role the section uses (§2.3) |
| `data-bold` | `true` (omit otherwise) | The section is one of the page's signature moves (§3) |

Background is recorded in `data-bg`, not in the layout tag, so "dark band" is not a layout. A dark band with a list of links is `data-layout="list" data-bg="dark"`.

### 2.2 Layout tags

| Tag | What it looks like |
|---|---|
| `centered-stack` | Centered heading and text, with one centered element below (product visual, form, CTA buttons) |
| `split-left` | Text column left, visual right |
| `split-right` | Visual left, text column right |
| `bento` | Grid of tiles with **unequal** sizes (a lead tile, or swapped row widths) |
| `card-grid` | Grid of **equal** cards (3-up, 4-up, 2×3) |
| `list` | Full-width rows separated by hairlines (FAQ, link index, changelog, article list) |
| `walkthrough` | A list or tab set that drives one large visual (only one item active at a time) |
| `full-bleed` | Content that runs to the viewport edges, or a panel inset only a few px from them |
| `big-type` | One oversized phrase is the main element |
| `big-quote` | One quote is the main element |
| `stat-band` | A row or bento of numbers |
| `logo-row` | A row of customer or integration logos |
| `carousel` | A horizontal row that runs past the viewport edge |

Pick the tag from what the reader sees first. A split header (heading left, paragraph right) above a 3-up grid is `card-grid`. An alternating feature-row section is `split-left` (name it by its first row).

### 2.3 Background roles per style

Use only the backgrounds the active style file allows, and never more sections per role than it allows.

| `data-bg` | Minimal | Business | Colorful | Editorial |
|---|---|---|---|---|
| `base` | `var(--bg)` | `var(--bg)` | `var(--bg)` | `var(--bg)` |
| `alt` | `var(--surface-1)` — "Emphasis section", at most 1–2 | `var(--surface-1)` — "Soft emphasis", at most 1–2 | `var(--surface-1)` (style has no cap; *inference*: use at most 1–2, as the other styles do) | `var(--surface-1)` — "Alternate sections", at most 1–2; add a 1px `var(--surface-2)` border (*inference*, not in the style file: Editorial `--surface-1` is "very subtle" on `--bg`) |
| `dark` | `.section-dark` (`var(--text)` band) — **light theme only** | — no role (see §6) | — use `scene` instead | Dark stage `#161616` (`.hero-stage`) — hero or closing section only |
| `scene` | — | — | `.scene` with one `--scene-*` color; at most 2 scene colors per page | — |

On a dark-theme page, never use `var(--text)` as a band color (it is light there). Use `alt` instead.

### 2.4 The rules

| # | Rule | Check | Evidence |
|---|---|---|---|
| R1 | Every content section has `data-layout`, `data-bg`, and (if bold) `data-bold`. | Attribute present on every `data-section` except `nav` and `footer`. | — (markup convention) |
| R2 | **No two adjacent content sections share the same `data-layout`.** If you want a repeated module, make it one section with several rows. | Compare each section's tag with the next one. | 2 of 21 real pairs repeat a layout; both are the one monotone page. |
| R3 | **Change the background at roughly every other boundary.** With *N* content sections there are *N − 1* boundaries; change `data-bg` at **at least ⌊(N − 1) / 2⌋** of them, within the style's caps in §2.3. Each `alt` section in the middle of the page creates two changes. The caps win: on a long page (≈ 10+ sections, or a dark-theme page with no `dark` role) the target can be out of reach — then use every background the caps allow, carry the rest of the rhythm with layout changes (R2, R8), and say so in the QA report. | Count boundaries where `data-bg` differs. | ≈ 60% of real boundaries change background. |
| R4 | **1–2 bold sections per page, the hero included.** Default: a bold hero + one bold mid-page section. Short single-purpose pages (Pricing, Contact, 404, Downloads) use 0 or 1. The giant wordmark footer (§4 M14) is the only allowed extra; it sits on the footer, so it is not counted among the content sections. | Count `data-bold="true"`. | SaaS median ≈ 2; hero bold on 6/7. *Inference:* Oryzo, with 6+ bold sections, is a product-showcase genre, not a SaaS default. |
| R5 | **No signature move twice on one page.** | Each move name appears once. | Ditto: "repeating the big-quote treatment more than once per page cancels it out." |
| R6 | **At most one `card-grid` of three equal cards per page.** Other parallel content uses `bento`, `list`, `split-*`, or `walkthrough`. | Count `card-grid` sections (the checker counts every `card-grid`, whatever the card count). | The forgettable pattern is "3 equal cards, repeated"; Ramp shows it is survivable only with compensators. |
| R7 | **Alternate density.** After a dense section (`card-grid`, `bento`, `list`, `walkthrough`), prefer a sparse one (`big-quote`, `big-type`, `centered-stack`, `stat-band`). | Advisory — not an error. | Ditto list → orange quote band; Steep grid → centered quote; Wispr logos → "4x faster" claim. *Inference.* |
| R8 | When two adjacent sections share a background, the layout change must be visible at a glance (e.g., `card-grid` → `split-left`, not `card-grid` → `bento` with the same card style). | Advisory. | 6 of 8 same-background real pairs changed geometry. *Inference.* |

**A quick worked example (Landing, 7 content sections, Minimal light):**

| # | Section | `data-layout` | `data-bg` | Bold |
|---|---|---|---|---|
| 1 | hero | `centered-stack` (M3 Product rising from the fold) | base | ✓ |
| 2 | logo-wall | `logo-row` | base | |
| 3 | features | `bento` (M5) | alt | |
| 4 | how-it-works | `walkthrough` (M8) | base | ✓ |
| 5 | social-proof | `big-quote` (M10, plain — not bold, see R4) | alt | |
| 6 | faq | `list` | base | |
| 7 | cta | `centered-stack` | dark | |

Layouts never repeat (R2). Background changes at boundaries 2→3, 3→4, 4→5, 5→6, 6→7 = 5 of 6 (R3 needs ≥ 3). Two bold sections (R4). Within caps: 2 `alt` sections, 1 dark band.

---

## 3. What counts as "bold"

A section is bold when one element is far larger, darker, or stranger than anything around it, and it carries the page's main idea. *Evidence:* the strongest observed cases rely on extreme size contrast ("two type sizes only, huge and tiny" — Studio Freight), a product visual that dominates the fold (Linear, Notion, Cursor), or an interaction that shows how the product works (Retool sticky tabs, Dovetail step diagram).

A bold section still uses the style's tokens. Boldness comes from **scale, crop, and structure**, never from new colors, glows, or gradients the style forbids.

---

## 4. Catalog

Seventeen moves. Moves **M1–M9, M14, M15 and M16 need no assets** — an offline agent can build them with a synthetic product visual (`shared/product-visuals.md`, frame tokens in the style file's §8) and the user's own words. **M10–M13 need real material** (a quote, numbers, a comparison, a content set). If the user gave none, M10, M11, and M13 may be filled with **sample content** per the master's *Sample content* rule (tagged `data-sample`, listed in the QA report) — except an About timeline (M13), which never gets invented dates. **M12 never uses sample content**: without a sourced comparison, pick another move. If the user said they *don't have* that material, do not use the move.

Every CSS block below uses CSS variables and style roles only. Before using them, declare these role variables on `:root`, **quoting** the active style file:

| Variable | Style role | Minimal | Business | Colorful | Editorial |
|---|---|---|---|---|---|
| `--fs-hero` | §2 Hero heading | `clamp(48px, 7vw, 80px)` | `clamp(48px, 6vw, 72px)` | `clamp(52px, 6vw, 66px)` | `72px` |
| `--fs-section` | §2 Section heading | `clamp(32px, 4vw, 47px)` | `clamp(32px, 4vw, 48px)` | `clamp(36px, 4vw, 54px)` | `48px` |
| `--fs-feature` | §2 Feature heading (Colorful: Supporting head) | `27px` | `28px` | `32px` | `24px` |
| `--ff-feature` | §2 Feature heading font | `var(--font-display)` | `var(--font-display)` | `var(--font-display)` | `var(--font-body)` |
| `--fs-card` | §2 Card heading | `20px` | `20px` | `20px` | `20px` |
| `--ff-card` | §2 Card heading font | `var(--font-display)` | `var(--font-display)` | `var(--font-body)` | `var(--font-body)` |
| `--fw-display` | §2 hero/section weight | `500` | `600` | `400` | hero `400` / section `500` |
| `--op-sub` | §1 Subtitle/description opacity | `0.5` | `0.5` | `0.75` | `0.6` |
| `--gap-card` | §3 Card gap | `20px` (bento) | `24px` | `24px` | `16px` |
| `--r-card` | §4 Feature card / panel | `8px` | `16px` | `16px` (inner panel) | `16px` (panel) |
| `--r-frame` | §4 Content card / frame | `16px` | `24px` | `24px` (scene frame) | `22px` (product stage) |
| `--fw-feature` | §2 Feature heading weight | `500` | `500` | `400` | `500` |
| `--gap-head` | §3 Section internal (heading to content) | `58px` | `48px` | `48px` | `48px` |
| `--gap-rows` | §3 Space between rows inside one section | `128px` (feature row spacing) | `120px` (section padding) | `120px` (section padding) | `96px` (section padding) |

On narrow screens (< 768px) use the style's narrow-screen table for all spacing; the moves below say how their layout collapses.

---

### M1 · Edge-to-edge headline

`data-layout="big-type"` · no assets

**When it fits:** consumer apps, creative tools, launches, brand moments; About pages with a manifesto; 404 *Brand Moment*. The phrase must be **1–3 short words** that carry the idea (a payoff, not a category).
**Evidence:** Oryzo "it's wearable" ≈ 17–18vw cap height across ≈ 95% of the width, with a small lead-in ("SO PORTABLE,") at ≈ 14px caps, 50% opacity; Glide "Leveling Up" ≈ 16vw across ≈ 85% of the card.

**Build:**
```html
<section data-section="hero" data-layout="big-type" data-bg="base" data-bold="true" class="bigtype">
  <div class="container">
    <p class="label">So portable,</p>
    <h1 class="bigtype-line">it's wearable</h1>
    <p class="bigtype-sub">One sentence that says what the product is.</p>
    <!-- CTA buttons from the style file -->
  </div>
</section>
```
```css
.bigtype-line {
    font-family: var(--font-display);
    font-weight: var(--fw-display);
    font-size: 17vw;               /* evidence: 16–18vw; tune so the line spans 85–95% of the container */
    line-height: 0.9;              /* see §6 — no style role for type this large */
    letter-spacing: -0.02em;       /* hero tracking, all four styles */
    white-space: nowrap;
}
.bigtype-sub {
    font-size: 18px;               /* Body text role; Editorial: 16px */
    opacity: var(--op-sub);
    max-width: 540px;              /* §7 subtitle measure; Editorial: 560px */
}
```
The lead-in uses the style's `.label`. Spacing between lines uses the style's "Hero heading to subheading" and "Subheading to CTA" values. Check the line at 375px: it must not overflow; if it does, the phrase is too long for this move.

**Styles:** best in Colorful and Editorial (serif display at this size is the effect); good in Minimal; weakest in Business (*inference*: Business's trust tone rarely carries a 2-word payoff).
**Failure modes:** a phrase longer than 3 words wraps and loses the edge-to-edge effect; with no subheading the reader never learns what the product does (Studio Freight's version "hides what the product does" on a SaaS page); a text-glow (Oryzo) is not in any style file — do not add one.

---

### M2 · Highlighted headline words

Hero modifier on `centered-stack` or `split-left` · no assets

**When it fits:** products about writing, editing, review, or a workflow with named stages. Each highlighted word must be a product action (Ditto highlights "Draft, review, and ship" — the three stages its product handles).
**Evidence:** Ditto, ≈ 44px bold centered headline, 3 flat highlight blocks, full line height, no radius.

**Build:**
```html
<h1><mark class="hl">Draft</mark>, <mark class="hl">review</mark>, and <mark class="hl">ship</mark> product copy</h1>
```
```css
.hl {
    background: var(--surface-2);   /* see §6 for Colorful scene colors */
    color: inherit;
    border-radius: 0;               /* evidence: no radius */
    -webkit-box-decoration-break: clone;
    box-decoration-break: clone;
}
```
**Styles:** all four. In Editorial, never use the teal accent for highlights (style: teal must not spread to headings).
**Failure modes:** more than 3 highlights is noise; highlighting words that are not product actions is decoration. Combine with M3 when the product has a UI — the pair counts as **one** bold section (the hero).

---

### M3 · Product rising from the fold

Hero, `data-layout="centered-stack"` · no assets (Synthetic Product Visual)

**When it fits:** any software product with a dense UI — the default hero move for Landing archetypes A–C and Product archetype A.
**Evidence:** product visual ≈ 63–78% of viewport width, its top edge at ≈ 35–75% of the first screen's height, cut off by the bottom of the screen (Linear ≈ 72% / 75%, Notion ≈ 63% / 35%, Cursor ≈ 78%). "Cutting the screenshot at the fold invites a scroll."

**Build:** centered headline, subheading, CTA, then the visual from `shared/product-visuals.md` **Recipe 1** (`.pv-rise`, width and fold cut defined there; `data-mock` on the frame). Space above the visual: `margin-top` = the style's "heading to content" value (Minimal 58px).
Keep the hero's vertical spacing to the style's values (hero top, heading → subheading, subheading → CTA) so the mock's top edge is above the fold on a 1440 × 900 screen. Do not add spacing to push it lower.

**Styles:** all four.
**Failure modes:** a sparse or generic mock (grey bars, "Item 1") looks like a template — fill it with the product's real nouns. Do **not** add corner glows or a perspective grid: the research calls glow + grid "a cliché of AI tool sites", and Minimal forbids glows outright.

---

### M4 · Framed hero stage

Hero, `data-layout="full-bleed"` · no assets (Synthetic Product Visual)

**When it fits:** the style has a strong stage color (Colorful scenes, Editorial dark stage), or a Minimal light page that wants one dark moment at the top. *Evidence:* Cursor puts the whole hero in an inset rounded panel (≈ 12px from the viewport edges, ≈ 16px radius), and the code screenshot is cut by the panel's bottom edge — "the page background stays neutral; all the color lives in one framed object."

**Build:** a panel inset from the viewport, holding the headline and the mock; the mock sits flush with the panel's bottom edge.
```css
.hero-stage-panel {
    border-radius: var(--r-frame);
    overflow: hidden;
    padding-bottom: 0;             /* the mock touches the bottom edge */
    text-align: center;
}
.hero-stage-panel .pv-mat {         /* product-visuals.md §3 mat */
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
}
```
Panel background and inset per style:

| Style | Panel |
|---|---|
| Minimal | Light theme: `.section-dark` colors inside the panel. Dark theme: `var(--surface-1)`. Radius `16px` (content card). Inset: see §6. |
| Business | `var(--surface-1)` with the 48px "Product stage panel" radius; brand gradients are allowed *inside* the product stage only |
| Colorful | `.scene` exactly as the style file defines it (`margin: 0 20px`, `24px` radius, one `--scene-*` color) |
| Editorial | `.hero-stage` (`#161616`), "Hero panel" radius `30px`, teal CTA |

**Failure modes:** a color panel with a thin or empty mock is "just wallpaper"; never put a gradient in the page shell (Minimal, Business, Colorful all forbid it).

---

### M5 · Bento with a lead tile

`data-layout="bento"` · no assets

**When it fits:** a features section where one feature clearly matters most. *Evidence:* Cursor's lead tile spans the full width at ≈ 2× the height of three small tiles; Ramp and Retool swap row widths (≈ 60/40 then 40/60; Retool 40/60 then 55/45). "It ranks the features: one hero feature, then supporting ones."

**Build (variant A — lead row):**
```css
.bento {
    display: grid;
    grid-template-columns: repeat(3, 1fr);   /* Minimal §7 bento: 3 columns */
    gap: var(--gap-card);
}
.bento .lead { grid-column: 1 / -1; }        /* full-width lead tile with a mock inside */
```
**Variant B — width swap:**
```css
.bento-swap { display: grid; gap: var(--gap-card); }
.bento-swap .row-a { display: grid; grid-template-columns: 3fr 2fr; gap: var(--gap-card); }
.bento-swap .row-b { display: grid; grid-template-columns: 2fr 3fr; gap: var(--gap-card); }
```
Minimal's own §7 bento ("`.featured` spans 2 columns") is the same idea in a 3-column grid. Tiles use the style's feature card; each tile holds a small **product fragment** (a chip row, one table row, one chat bubble), not an icon — tile and fragment CSS: `shared/product-visuals.md` Recipe 4. Narrow screens: one column.

**Styles:** all four. Counts as a bold section only when the lead tile carries a large mock (Ramp's restrained version is "a de-templating move", not a signature move).
**Failure modes:** an arbitrary lead feature misleads; fewer than 4 features leaves holes.

---

### M6 · Feature list as navigation

`data-layout="walkthrough"` · no assets · needs **8+** features

**When it fits:** a product with many capabilities (Product page, archetype B Platform Overview). *Evidence:* Intercom lists 13 features in a ≈ 62%-wide column; inactive items at ≈ 50% gray, the active one full black with a marker; the matching screenshot sits right and bleeds off the viewport edge. "It shows how wide the product is and still shows depth on one item."

**Build:**
```html
<section data-section="feature-showcase" data-layout="walkthrough" data-bg="base" data-bold="true">
  <div class="container walk">
    <div role="tablist" aria-orientation="vertical" class="walk-list">
      <button role="tab" aria-selected="true" aria-controls="p1">Macros</button>
      <!-- 8–13 more -->
    </div>
    <div class="walk-visual"><div role="tabpanel" id="p1"><!-- mock --></div></div>
  </div>
</section>
```
```css
.walk { display: grid; grid-template-columns: 3fr 2fr; gap: var(--gap-card); }
.walk-list [role="tab"] {
    display: block; width: 100%; text-align: left;
    font-family: var(--ff-card);
    font-size: var(--fs-card);           /* Card heading role (evidence ≈ 20px) */
    border-bottom: 1px solid var(--surface-2);
    opacity: var(--op-sub);
}
.walk-list [role="tab"][aria-selected="true"] { opacity: 1; }
.walk-visual { margin-right: calc(50% - 50vw); }   /* bleed off the right edge */
```
Vanilla JS: clicking a tab sets `aria-selected` and shows its panel. Without JS, show the first panel. Narrow screens: list becomes a horizontal scroll row of tabs above the visual; no bleed.

**Styles:** Minimal, Business, Editorial; Colorful works inside a `.scene`.
**Failure modes:** with 3–4 features it looks empty (use M5 instead); without JS state it is a dead list.

---

### M7 · Big-type list band

`data-layout="list"` · no assets (the rows must link to real pages or anchors)

**When it fits:** a use-case index, a solutions list, "who it's for" — 4–8 short items, each a link. *Evidence:* Ditto's black band: six use cases at ≈ 26px, ≈ 50% white opacity, hairline rules at ≈ 15% opacity, no icons, no images. "Removing imagery makes the band fast to scan."

**Build:** a section on the style's `dark` (or `scene` / `alt`) background; each row is an `<a>` that spans the full width.
```css
.biglist a {
    display: block;
    font-family: var(--ff-feature);
    font-size: var(--fs-feature);         /* evidence ≈ 26px → Feature heading role */
    border-bottom: 1px solid var(--surface-2);
    opacity: var(--op-sub);
    transition: opacity 0.3s linear;      /* Minimal §6 color/opacity transition */
}
.biglist a:hover, .biglist a:focus-visible { opacity: 1; }
/* On a .section-dark band, invert the rule color (style: borders invert to --text-inverse): */
.section-dark .biglist a { border-bottom-color: color-mix(in srgb, var(--text-inverse) 15%, transparent); } /* 15% from evidence */
```
**Styles:** Minimal (`.section-dark`), Colorful (`.scene`), Editorial (`alt`, or the dark stage if it is the closing section); Business uses `alt`.
**Failure modes:** rows that go nowhere are "a big decorative list".

---

### M8 · Sticky chapter tabs

`data-layout="walkthrough"` · no assets

**When it fits:** a long page that tells a staged story (Build → Launch → Scale; Connect → Analyze → Act). Product page B, Landing B SaaS Platform, How It Works for multi-stage products. *Evidence:* Retool — a sticky ≈ 40px tab bar with a progress line under the nav; inside each tab a list of 3 features (≈ 30%) drives a screenshot (≈ 60%). "It turns four page sections into one chapter structure."

**Build:**
```css
.chapters-bar {
    position: sticky;
    top: var(--nav-h);                  /* nav height from the style file */
    height: 40px;                       /* evidence */
    background: var(--bg);
    border-bottom: 1px solid var(--surface-2);
    backdrop-filter: blur(12px);        /* same rule as the fixed nav */
    z-index: 10;
}
.chapters-progress { height: 1px; background: var(--text); transform-origin: left; } /* see §6 */
.chapter { display: grid; grid-template-columns: 1fr 2fr; gap: var(--gap-card); } /* ≈ 30 / 60 */
```
Vanilla JS: an `IntersectionObserver` on each chapter sets the active tab and scales the progress line (`transform: scaleX()`, inside `prefers-reduced-motion: no-preference`). Tabs are anchor links, so the page works without JS. Narrow screens: the bar is **not** sticky (`position: static`) — sticky bar + nav "uses ≈ 80px of a short viewport".

**Styles:** all four.
**Failure modes:** fewer than 3 chapters does not need tabs; chapters that are not real stages are a fake story.

---

### M9 · Step rail + transformation diagram

`data-layout="split-left"` · no assets

**When it fits:** products that turn inputs into an output — AI, data, research, document, automation tools; How It Works sections. *Evidence:* Dovetail — a 5-step vertical rail (active step expanded, others as gray titles) and a node diagram (source cards → "GENERATING DOC" → report) at ≈ 50% width, mono labels inside the cards. "The diagram shows the transformation the product does. This is stronger than a static screenshot."

**Build:** left column = heading + `<ol>` of 4–5 steps (active step shows its description; others at `var(--op-sub)`); right column = diagram built from cards.
```css
.diagram { display: grid; gap: var(--gap-card); justify-items: center; }
.diagram .node {
    background: var(--surface-1);
    border-radius: var(--r-card);
    padding: 16px;                       /* spacing scale value */
    font-family: var(--font-mono);
    font-size: 12px;                     /* Label role */
}
.diagram .link { width: 1px; height: 24px; background: var(--surface-2); } /* connector; 24px = scale value */
```
Fill the nodes with the product's real inputs and output ("3 interview transcripts" → "Tagging themes" → "Insights report"), never "Input → Process → Output". Narrow screens: rail above, diagram below.

**Styles:** all four. Do not use this and M8 on the same page (both are "list drives visual"; *evidence*: Ditto used the pattern twice and the research flags it as overuse).
**Failure modes:** a generic flowchart "says nothing".

---

### M10 · Poster quote

`data-layout="big-quote"` · **needs a real, attributable quote**

**When it fits:** one strong customer quote. *Evidence:* Coda — quote ≈ 34px condensed caps, column ≈ 62% wide, flat brand-color band, tiny attribution, no photo or logo; Ditto — ≈ 40px heavy type, column ≈ 45% wide. "The quote is the only element, so it reads as a statement."

**Build:** section on `dark` / `scene` / `alt`; one `<blockquote>` at `var(--fs-section)` with `font-family: var(--font-display)`, `max-width: 62%` (evidence 45–62%; 100% on narrow screens), attribution in the style's `.label`. Sentence case by default; caps only for quotes under ~40 words (evidence: "long quotes in all caps get hard to read past ~40 words"). Minimal: no decorative quote glyph (Minimal Testimonial rule).
**No quote given:** sample quote from a fictional person at a fictional company, `data-sample` on the section, listed in the QA report. User said no testimonials: do not use this move.
**Styles:** all four. Counts as bold only when it sits on a `dark` or `scene` band.
**Failure modes:** fake quotes passed off as real; using it twice on one page.

---

### M11 · Stat bento with an empty title tile

`data-layout="stat-band"` · **needs 3+ real, sourced numbers**

**When it fits:** About pages, enterprise landing pages, case studies. *Evidence:* Robot.com — a tall title tile (≈ 50% wide × 2 rows, mostly empty) and three number tiles (≈ 25% each), number top-left, label bottom-left, one dark tile. "The empty space in the big tile is confident." Counterexample: 4 of 6 "big number" results were plain 3-up rows with 36–48px numbers — a band, not a focal point.

**Build:**
```css
.statbento { display: grid; grid-template-columns: 2fr 1fr 1fr; grid-template-rows: auto auto; gap: var(--gap-card); }
.statbento .title { grid-row: 1 / 3; }
.statbento .num {
    font-family: var(--font-display);
    font-size: clamp(36px, 5vw, 56px);   /* About page stats-section number token (pages/about-page/references/stats-section.md) */
}
```
Tiles use the style's feature card. Narrow screens: title tile full width, numbers in one column.
**No numbers given:** round illustrative numbers with `data-sample`; user said no real numbers: do not use this move (and skip Stats entirely).
**Failure modes:** invented metrics; fewer than 3 numbers leaves holes.

---

### M12 · Proof as proportion

`data-layout="stat-band"` (or `centered-stack`) · **needs one real, sourced comparison**

**When it fits:** a speed, size, or cost claim the user can back up ("4× faster than X"). *Evidence:* Wispr Flow — "4x faster than typing" at ≈ 72px, then two panels whose widths show the ratio (45 wpm ≈ 20% vs 220 wpm ≈ 65%). "The claim is shown as a proportion, not just stated."

**Build:** headline (`--fs-section` or `--fs-hero`) + two bars inside one card. Set each bar's width **exactly** to `value / max × 100%`; label each bar with its value and unit in `.label` style. Bars: the smaller one `var(--surface-2)`, the larger one `var(--text)` (Minimal/Business/Colorful) or `var(--accent)` only if the active style allows the accent there — none of the four style files lists bars as an accent use, so use `var(--text)`.
**No sourced number:** do not use this move. A sample ratio still reads as a product claim; pick M9 or M5 instead.
**Failure modes:** a ratio that does not match the bar widths; an invented metric.

---

### M13 · Edge-bleeding carousel

`data-layout="carousel"` · **needs 5+ real content items** (articles, reports, customer stories, milestones)

**When it fits:** Blog featured row, About timeline (real dates only), customer stories, report covers. *Evidence:* Ramp report covers ≈ 21% wide, the last one cut by the viewport edge, arrows top-right; Square's timeline bleeds both edges; Webflow's active card ≈ 58% with the next ≈ 12% visible. "Cut-off cards suggest there is more."

**Build:** the row starts at the container's left edge and runs past the viewport's right edge (`margin-right: calc(50% - 50vw)` on the track). Cards ≈ 20–22% of the container (evidence), feature card radius, `scroll-snap-type: x mandatory`. Use the Carousel recipe in `shared/interaction-patterns.md` §12 for arrows and keyboard support. Narrow screens: cards ≈ 80% wide (*inference*: keeps one peek visible).
**No items given:** for Blog, sample article titles with `data-sample`; for an About timeline, never invent dates or milestones — skip the move.
**Failure modes:** 3 items ("nothing to bleed"); a peek with no scrolling "looks like a layout bug".

---

### M14 · Giant wordmark footer

Footer modifier (not a content section; does not need `data-layout`) · no assets

**When it fits:** consumer, creative, design-led, and studio brands with a short name (≤ 8 characters). *Evidence:* Structured (serif ≈ 20vw), BAGGU (bleeds off the bottom edge), MOUTHWASH Studio (≈ 28vw), Zellerfeld — all set ≈ 95–100% of the width, footer links ≈ 10–12px. In the same result set, Calendly and Grain used normal column footers. All 4 examples are fashion or studio brands.

**Build:** after the normal footer columns, one line with the product name:
```css
.footer-wordmark {
    font-family: var(--font-display);
    font-weight: var(--fw-display);
    font-size: 20vw;                     /* evidence: 20–28vw; tune to span 95–100% */
    line-height: 0.8;                    /* see §6 */
    letter-spacing: -0.02em;
    white-space: nowrap;
    overflow: hidden;
    opacity: 1;
}
```
Mark it `aria-hidden="true"` (the nav already names the brand). Footer padding stays the style's footer values.
**Styles:** Colorful, Editorial, Minimal. Avoid on Business and on enterprise B2B (*evidence*: "on B2B SaaS it can feel like a costume").
**R4:** the only move allowed as a third bold element (*inference*: it "does not compete with the content").
**Failure modes:** names longer than 8 characters get too small at full width.

---

### Seen but not cataloged

These moves were observed but need commissioned assets or suit only one genre. Use them only when the user supplies the material.

| Move | Needs | Evidence |
|---|---|---|
| Staggered type block | Studio/manifesto page with no CTA | Studio Freight |
| Art background behind UI | Licensed painting or pattern | Cursor (new site), Intercom |
| Interlocking collage hero | Two real images + SVG notch masks | Retool |
| Annotated object | A physical product photo; software features have no physical locations | Rains, Superpower |
| Full-bleed photo / before-after slider | Art-directed photography | Oryzo, bella, Duolingo store, Wispr Flow CTA |
| Proof ledger (case study + outcome + logos) | A named customer and a real outcome | Retool |

---

### M15 · Step tiles with product

`data-layout="card-grid"` · no assets

**When it fits:** How It Works / getting-started sections with 3 (or 4) steps — the default step layout in every style. *Evidence:* FLORA (three tall tiles, each step's UI filling the tile, the step name set large over it), Mews (three pink mats, each holding a product fragment, numbered caption below), Braintrust (three lilac mats with a real product card each — a job brief, a candidate match, a task list — caption below). The weak versions in the same result set are text-only: Clay, Givingli, PayPal Careers ("01 / 02 / 03" with a title and nothing to look at). Generated pages fell into the weak version in all four styles (2026-10-14 style matrix).

**Build:** three equal tiles. Each tile = a mat (`--pv-mat`) of fixed height holding **one product fragment for that step**, cut by the tile's bottom edge, then the caption below the tile: mono step number, card-heading title, one sentence. The fragment shows the *result* of the step in the product's own UI (the connected address, the routing rule, the closed thread), with the product-visuals content minimums at small scale: 2–4 rows, one status, one proper noun.
```html
<div class="steps">
  <div class="step">
    <div class="pv step-visual" data-mock role="img" aria-label="Email channel connected in settings">
      <div class="pv-mat"><div class="pv-panel">…2–4 rows of the step's real UI…</div></div>
    </div>
    <div class="step-text"><span class="step-num">01</span><h3>Forward your support address</h3><p>Every email becomes a conversation in the shared inbox.</p></div>
  </div>
  <!-- 2 more .step -->
</div>
```
```css
.steps { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--gap-card); }
.step { display: grid; grid-template-rows: auto 1fr; }
.step-visual { --pv-text: 14px; --pv-row: 34px; height: 240px; overflow: hidden; border-radius: var(--r-frame); }
.step-visual .pv-mat { height: 100%; padding: 20px 20px 0; box-sizing: border-box; }
.step-visual .pv-panel { border-bottom-left-radius: 0; border-bottom-right-radius: 0; min-height: 100%; -webkit-mask-image: linear-gradient(to bottom, #000 calc(100% - 56px), transparent); mask-image: linear-gradient(to bottom, #000 calc(100% - 56px), transparent); }  /* = .pv-cut */
.step-text { padding: 24px 4px 0; }
.step-text .step-num { font-family: var(--font-mono); font-size: 12px; letter-spacing: .72px; opacity: .4; }
.step-text h3 { font-family: var(--ff-card); font-size: var(--fs-card); font-weight: 500; margin: 8px 0 0; letter-spacing: -0.01em; }
.step-text p { font-size: 16px; line-height: 1.6; opacity: var(--op-sub); margin: 8px 0 0; }
@media (max-width: 767px) { .steps { grid-template-columns: 1fr; gap: 40px; } }
```
Fixed `px` height on the visual, never `vh`. On an `alt` section the mat steps to `var(--bg)` and panels to `var(--surface-1)` (product-visuals §2).
**Styles:** all four — Minimal mats `var(--surface-1)`; Business `.card` tiles with the §5 shadow; Colorful paper panels on one `--scene-*` mat (the page's second scene); Editorial ruled `.card-static` tiles. Counts as the page's one equal-card grid (R6).
**Failure modes:** a one-line chip as the step's visual; three identical fragments; text-only steps.

---

### M16 · Feature row with a full mat

`data-layout="split-left"` / `"split-right"` · no assets

**When it fits:** the main features of a landing or product page, **two rows** alternating sides. A third feature goes into another move (M15 tiles, an M5 bento, a short grid) — three identical rows plus three step tiles read as one repeated grey card (judged run, 2026-10-14). *Evidence:* the realism rule "scale up, not down" (product-visuals.md §1 rule 10: close-ups at 1.5–2×; full screens shrunk to fit become illegible) and the 2026-10-14 style matrix, where every style placed a ~250px card in a wide column and the judge read it as a thumbnail.

**Build:** text column `5fr`, visual column `7fr`. The visual is a mat that fills its column, padded `40px` with the panel rising from the mat's bottom edge (Recipe 1 cut), mock text one step up (`--pv-text: 14px`, rows 36px). A list mock shows **6 rows and at most 3 columns** (avatar · name + subject · status) so nothing wraps. Text column: mono label with the row number, feature heading, one paragraph, optionally 2–3 ruled points.
```html
<div class="frow">                      <!-- add .is-flipped for the next row -->
  <div class="frow-text"><p class="label">01 · Ownership</p><h3>One owner per thread, visible to everyone</h3><p>…</p>
    <ul class="frow-points"><li>…</li><li>…</li></ul></div>
  <div class="pv frow-visual" data-mock role="img" aria-label="…"><div class="pv-mat"><div class="pv-panel">
    <div class="frow-head"><span class="pv-kpi">Support · Open</span><span class="pv-label">14 open</span></div>
    <!-- 6 .pv-row, grid-template-columns: 28px minmax(0,1fr) 84px -->
  </div></div></div>
</div>
```
```css
.frow { display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: var(--gap-head); align-items: center; }
.frow.is-flipped { grid-template-columns: minmax(0, 7fr) minmax(0, 5fr); }
.frow.is-flipped .frow-text { order: 2; }
.frow + .frow { margin-top: var(--gap-rows); }
.frow-text h3 { font-family: var(--ff-feature); font-size: var(--fs-feature); font-weight: var(--fw-feature); letter-spacing: -0.02em; line-height: 1.2; margin: 16px 0 0; }
.frow-text p { font-size: 18px; line-height: 1.6; opacity: var(--op-sub); margin: 16px 0 0; max-width: 440px; }
.frow-points { list-style: none; padding: 0; margin: 24px 0 0; display: grid; gap: 12px; font-size: 16px; }
.frow-points li { padding-top: 12px; border-top: 1px solid var(--surface-2); }
.frow-visual { --pv-text: 14px; --pv-row: 36px; }           /* 1.1x mock text: the feature visual reads at page scale */
.frow-visual .pv-mat { padding: 40px 40px 0; }                 /* the panel rises from the mat's bottom edge */
.frow-visual .pv-panel { -webkit-mask-image: linear-gradient(to bottom, #000 calc(100% - 56px), transparent); mask-image: linear-gradient(to bottom, #000 calc(100% - 56px), transparent); }  /* = .pv-cut */
.frow-visual .pv-panel { width: 100%; border-bottom-left-radius: 0; border-bottom-right-radius: 0; border-bottom: 0; }
.frow-visual .pv-panel > .pv-row:last-child { border-bottom: 0; }
.frow-head { display: flex; flex-wrap: wrap; gap: 4px 12px; justify-content: space-between; align-items: baseline; padding: 16px 16px 12px; }
@media (max-width: 767px) {
  .frow, .frow.is-flipped { grid-template-columns: 1fr; gap: 32px; } .frow.is-flipped .frow-text { order: 0; }
  .frow + .frow { margin-top: 80px; }
  .frow-visual .pv-mat { padding: 24px 20px 0; }
}
```
**Styles:** all four. Business may put two M16 rows after its M5 bento; Colorful places each row inside a `.scene` (scene chapters); Editorial uses the 260px margin column for the section heading and M16 rows in the wide column.
**Failure modes:** a 4–5 column table that wraps every row; a mat with an empty band above the panel; the same mock in two rows.

---

### M17 · Quote wall

`data-layout="bento"` · **needs quotes** (sample quotes allowed, tagged)

**When it fits:** social proof when there are 2–3 quotes, or when quotes are sample content. *Evidence:* Hex (six quote cards, each under a customer wordmark), Customer.io (three quotes in a row), Intercom (a mosaic mixing quotes and customer marks), Unify (one quote next to a portrait). A single sentence alone on a full-width band — what generated pages produced — read as "sparse" to the judge in three styles; real single-quote sections anchor the quote with a portrait or brand mark, and this skill never invents photos.

**Build:** three figures, the first wider (`1.4fr 1fr 1fr`), all quotes at the same card-heading size and the cards equal in height (a bigger first quote reads as unbalanced); each figure ends with the person (name + role) and the company as a **sample wordmark** (`sections/social-proof/SKILL.md` *Sample wordmarks*). One real quote from the user → M10 instead.
```html
<div class="quotes" data-sample>
  <figure class="quote is-lead"><blockquote>…</blockquote><figcaption><span class="who">Helen Marsh<span>Head of Support</span></span><span class="wm" data-logo-source="wordmark">◆ Larkspur</span></figcaption></figure>
  <figure class="quote">…</figure><figure class="quote">…</figure>
</div>
```
```css
.quotes { display: grid; grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr) minmax(0, 1fr); gap: var(--gap-card); align-items: stretch; }
.quote { margin: 0; display: flex; flex-direction: column; justify-content: space-between; gap: 32px; padding: 32px; background: var(--surface-1); border-radius: var(--r-card); }
.quote blockquote { margin: 0; font-family: var(--ff-card); font-size: var(--fs-card); line-height: 1.45; font-weight: 500; letter-spacing: -0.01em; }
.quote.is-lead { padding: 40px; }                        /* the lead is wider, not louder: same type size keeps the row even */
.quote figcaption { display: flex; align-items: center; justify-content: space-between; gap: 12px; }
.quote .who { font-size: 14px; } .quote .who span { display: block; opacity: .5; }
.quote .wm { font-size: 15px; opacity: .6; white-space: nowrap; }
@media (max-width: 767px) { .quotes { grid-template-columns: 1fr; } .quote.is-lead { padding: 32px; } }
```
**Styles:** all four — Minimal `var(--surface-1)` cards, no glyph; Business `#FFFFFF` cards with the §5 shadow on an `alt` band; Colorful paper cards inside a scene; Editorial `.card-static` ruled cards.
**Failure modes:** one quote alone on a band; star ratings; invented photos.

---

## 5. Selection guide

Choose the page's moves **after** the page skill picks the archetype and section list, and **before** writing any section.

**Step 1 — Pick the hero move (bold #1).**

| Signal from the brief | Hero move |
|---|---|
| Software with a UI (most Landing / Product pages) | **M3** Product rising from the fold |
| Same, and style is Colorful or Editorial, or a Minimal light page that wants a dark entry | **M4** Framed hero stage |
| Product about text, editing, review, or named stages | **M2** + M3 together (one bold section) |
| Consumer / creative / launch / manifesto with a 1–3 word payoff | **M1** Edge-to-edge headline |
| Pricing, Contact, Downloads | No hero move. The page's one bold element (if any) is its core component (tier cards, form, platform list) — follow the page skill. |
| 404 Brand Moment (archetype C) | M1 on the numeral or a short phrase |

**Step 2 — Pick at most one mid-page move (bold #2), from the strongest true signal:**

| Signal | Move |
|---|---|
| 8+ capabilities | M6 Feature list as navigation |
| A staged story (3–5 stages) | M8 Sticky chapter tabs |
| Inputs → output transformation | M9 Step rail + diagram |
| One clearly most-important feature | M5 Bento with a lead tile |
| A real, strong customer quote | M10 Poster quote on a dark/scene band |
| 3+ real numbers | M11 Stat bento |
| One sourced comparison | M12 Proof as proportion |
| A use-case or solutions index | M7 Big-type list band |
| 5+ articles / stories / reports | M13 Edge-bleeding carousel |

If two signals tie, pick the move that sits where the brief's main **barrier** is answered (Step 2 of the master: complexity → M8/M9; trust → M10/M11).

**Step 2b — Default layouts for the common sections (not bold).** Unless a Step 2 move takes the section: main features → 2 **M16** rows alternating sides (Business may lead with M5, then M16); How It Works → **M15** step tiles; social proof → **M10** for one real quote, **M17** for 2–3 quotes or sample quotes. These replace text-only steps, thumbnail-sized feature mocks, and a lone quote on a band — the three sparse sections the 2026-10-14 judged run found in every style.

**Step 3 — Use non-bold versions elsewhere for variety.** M5 without a big mock, M7 on an `alt` background, and M10 on `base` are good *non-bold* layouts that help R2 and R6.

**Step 4 — Restrained pages.** Finance, legal, healthcare, enterprise trust, Business style, and high-intent short pages may use **only** the hero move. Then apply Ramp's four compensators instead: background alternation (R3), a mixed-width bento instead of equal cards, real product fragments inside cards, and a carousel for content sets.

**Step 5 — Closer (optional).** M14 for short-named consumer / creative brands only.

**Step 6 — Fill the table.** Write the section list with `data-layout` / `data-bg` / bold before building, and check R2–R6 on it (as in the §2.4 example). It is cheaper to fix a table than a page.

Record the chosen moves in the delivery note ("Hero: product rising from the fold; mid-page: sticky chapter tabs").

---

## 6. Values not in any style file

These were needed but have no role in any style file. The values used above come from the evidence or are flagged here; a maintainer should add roles to the style files.

| Need | What this file does | Gap |
|---|---|---|
| Line-height for type at 16–28vw (M1, M14) | `0.9` / `0.8` — **not from a style file** | No style defines a line-height for type above hero size. Replace with a style role once one exists. |
| Viewport inset for a Minimal / Business / Editorial hero panel (M4) | Not set; evidence ≈ 12px (Cursor) | Only Colorful defines an inset (`.scene` `margin: 0 20px`). |
| Business dark band | Use `alt` | Business has no dark section role on a light page. |
| Editorial mid-page dark band | Use `alt` | Editorial allows the dark stage for hero or closing sections only. |
| Colorful highlight color (M2) | `var(--surface-2)` | Scene colors are defined as section backgrounds only; using them behind words would be a new use. |
| Progress-line thickness (M8) | `1px` (the system's border width) | No role. |
| Rule color on a `.section-dark` band (M7) | `color-mix(... var(--text-inverse) 15% ...)` — 15% from evidence | Minimal says borders invert to `--text-inverse` but gives no opacity. |
| Stat number size outside About (M11) | About page token `clamp(36px, 5vw, 56px)` | Page-specific token, no shared role. |
| Minimal "more than 2 background colors" vs. `.section-dark` | Allowed per Style precedence | Minimal §8 Section Background Switching says "not allowed: more than 2 background colors", while `.section-dark` adds a third. |
| Checker support | `scripts/check_page.py` checks R1 (markup), R2, R3, R4 (bold count), R6, and unknown tags | R5 (move named twice), R7, and R8 are not machine-checked. |
