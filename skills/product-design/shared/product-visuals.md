# Product Visuals — Synthetic Product Visual Recipes

> The full recipe set for synthetic product visuals: the UI mocks a page shows when the user has no real screenshot.
> Evidence: 55 product visuals from real product sites (Mobbin, 2026-10-08), numbered (1)–(55) below, plus the "signature moves" study (A2.x, A3.x). Counts are out of 55 unless stated.
> The frame tokens in the active style file's §8 still apply. This file decides **what** to show and **how to compose it**. Motion for these visuals: `shared/interaction-patterns.md` §1.5.

When the user gives real screenshots, use them. Everything here is for the case where they don't.

---

## 1. Rules

These rules come from the evidence. Each one names its count.

1. **Never use skeleton bars, empty image boxes, or an icon in a grey square as the main visual.** 52/55 visuals carry legible, specific content. The 3 exceptions are faded background tiles (7) and small bento illustrations (28, 29). None of them is the focal visual of a hero. Grey bars are allowed only in a background layer: faded to opacity ≤ 0.3 and behind a fully legible focal element (7, 35), or at icon scale, under 30% of a tile's height (29).
2. **Show a fragment, not the whole app.** 30/55 show less than one full screen (layered cards 11, isolated component 10, bento 6, cropped close-up 3). Only 11/55 show a full window (7 full screens, 4 code editors). In feature sections, full screens appear in only 3 of about 30. Use a full screen only for a centered hero (Recipe 1).
3. **Meet the content minimums.** In the focal visual:
   - every line that stands for text is real text: a name, a title, or a sentence (52/55);
   - at least 3 proper nouns: people, a fictional customer, project or file names (named people in 19/55);
   - lists and tables have 5–8 rows (Front 6 senders (3), Toggl 6 project rows (5), Monarch 15 categories (36));
   - at least one set of 2–3 status states, such as "In stock / Low stock" or "Critical / Major" (4, 23, 18);
   - at least one relative time or concrete date: "2m ago", "Viewing now", "Feb 3, 2026" (43, 44, 46, 21).
4. **Numbers are specific and non-round.** All 13 finance and analytics visuals use cents or odd values: $3,719.46 (36), $68,026.43 (37), −472.42 (12), 34:18:07 (5), "+7 ↑18%" (4). Two (41, 49) show the cents at lower opacity. This applies **inside `data-mock` only**. Page-level sample claims (stats, metrics in copy) still follow the master SKILL.md *Sample content* rule: round illustrative numbers in `data-sample` elements. A mock row is UI, not a claim.
5. **Exactly one focused state.** 26/55 show one element in a live state: a selected row (3, 12, 36), an active tab (17, 41), an open tooltip (6, 49), highlighted text (25, 46), a focused input (43, 47), or one sharp tile among faded ones (7, 35). Not zero, not several.
6. **Fictional, specific, coherent.** The convincing samples invent one business and fill every field for it: Acme Co (31), Wizard Coffee App (23), Coinvest (42), Flore Farms (45). The parts agree: the same incident ID INC-2709 on desktop and phone (4), the headline quoting the code token `// todo` (25), totals that match line items (36). Invent the business per page (master SKILL.md *Sample content*: no Northwind/Contoso/Acme-style stock names). Never put real third-party brands in a mock: a real name reads as an integration claim.
7. **Plain UI, color from the mat or the data.** 19/55 place the UI on a colored, gradient, or image backing panel (the "mat") with the UI itself white or near-black. Color comes from the mat, chart series, status pills, avatars, or content imagery, not from tinted UI chrome (inferred across 3, 11, 30, 40, 47).
8. **App chrome, not OS chrome.** macOS traffic lights or a custom title bar appear in 7/55, a URL bar in 2/55, and 4 of those 9 are developer tools. Most app visuals show the app's own sidebar and top bar (3, 4, 12, 17, 23, 36). Use traffic lights only for desktop and developer tools.
9. **Crop with intent.** 12/55 bleed off one edge (fold, section, or container) and 2 more fade out at the edges (7, 35). A hero visual cut at the bottom says "there is more below" (4, 17, 36). Cut through content, never through empty padding, and fade the cut: put `.pv-cut` (§3) on the cropped panel so the last 56px dissolve into the mat — a row sliced mid-sentence with a hard edge reads as a rendering bug (every judged run, 2026-10-14). So a cropped panel holds more rows than the crop shows (7–8), and the crop comes from a fixed `px` height on its container — never `vh`, which stretches on tall screens and in full-page screenshots. A list that ends above the crop leaves a white gap that reads as unfinished.
9a. **On a phone, rows wrap; they don't truncate.** At 390px a row keeps 2–3 columns (avatar, name + subject, status). Let the text column wrap to two lines rather than cutting it to "Maya Re…"; drop timestamps or secondary columns first.
10. **Scale up, not down.** Close-ups show components at 1.5–2× real size so the text reads at page scale (18, 37, 40). Full screens shrunk to fit become illegible (1, 9).
11. **One motion cue at most.** Visible cursor in 11/55, typing caret in 2, toast in 2, mid-process state in 3 ("Calculating…" (9), "Step 6 Complete" (23), bars mid-draw (41)). Pick one per visual. The static HTML shows the cue's final state. Animation is optional, from `interaction-patterns.md` §1.5.
12. **Mark the frame.** Put `data-mock` on the outer frame of every synthetic visual (master SKILL.md, Markup conventions). Accessibility convention (not from the evidence): give that frame `role="img"` and an `aria-label` that says what the mock shows, so screen readers skip the fake UI text.

### Placement (24 hero visuals)

- 15/24 sit centered below the headline at 55–80% of the page width. 7/24 sit in a split column. 1 surrounds the headline (7), 1 is the hero itself (21).
- Rising screenshots in the signature-moves study: 63% (Notion, A2.2), 72% (Linear, A2.1), 78% (Cursor, A2.3) of the width, starting at 35–75% of the fold height.
- Do not use the same recipe in two sections in a row. In the signature-moves study, consecutive sections repeated a layout in only 2 of 21 adjacent pairs, and that page read as monotone.

---

## 2. Style binding

The recipes use local custom properties (`--pv-*`). The block in §3 sets them to **Minimal defaults, quoted from `visual-style.md`**. With another style active, replace each one with the role named here. Do not invent values.

| Role | Minimal | Business | Colorful | Editorial |
|---|---|---|---|---|
| `--pv-mat`: backing panel | `var(--surface-1)` | `var(--surface-1)`. A gradient is allowed only inside the product stage (§1 Accent Color Rules): the user's brand colors when given, otherwise the default stage gradient defined in Business §10 Style Signature | one `var(--scene-*)` (§1 Scene Colors). It counts toward the page's limit of 2 scene colors | `var(--surface-1)` with `1px solid var(--surface-2)` border, or the dark stage background (§8 Section Background Switching) |
| `--pv-r-outer`: mat and frame radius | §4 Content card | §4 Content card | §4 Scene frame | §4 Product stage |
| `--pv-r-inner`: UI panel and card radius | §4 Feature card | §4 Feature card | §4 Inner panel | §4 Inner UI |
| `--pv-r-control`: pills, inputs, chips | §4 Input | §4 Input/form field | §4 Control | §4 Control |
| Floating card depth | no shadow; `1px solid var(--surface-2)` border (§5) | §5 Light Theme Card Shadow / Dark Theme Card Depth | §5 Card Shadow / Dark Theme Card Shadow | §5 Floating Surface Shadow |
| Strong status / selected fill | `var(--text)` with `var(--text-inverse)` text | same as Minimal | same as Minimal | `var(--accent)` with `var(--accent-text)` (§1 allows a functional status badge) |

Rules that apply in every style:
- **Surface nesting**: on a `--pv-mat` of `var(--surface-1)`, UI panels use `var(--bg)` (style §8 Card, Surface nesting rule).
- **Mocks in an `alt` section** (`data-bg="alt"`, background `var(--surface-1)`): a `var(--surface-1)` mat, bento tile, or code window disappears into the section. Step every level once: `--pv-mat` and `.pv-tile` become `var(--bg)`, `.pv-panel` becomes `var(--surface-1)`, and `.pv-row.is-focused` becomes `var(--surface-2)` (Surface nesting rule: inside `var(--bg)` → `var(--surface-1)`; inside `var(--surface-1)` → step to a different level).
- **Mock text**: 12–13px, weight 400, rows 28–32px tall (`visual-style.md` §8 Synthetic Product Visual). IDs, timestamps, and code use `var(--font-mono)`. Headline numbers (KPIs, balances) and component titles use the style's **card heading** role: 20px in all four styles, font `var(--font-display)` in Minimal and Business, `var(--font-body)` in Colorful and Editorial (both set card headings in the body font; Editorial forbids serif below 24px).
- **Minimal on dark**: the evidence puts a glow behind dark-page visuals (7, 10, 26). Minimal forbids glows (`visual-style.md` §1). Use the mat or nothing.

**Status and chart colors.** The evidence colors status pills and chart series (green / orange / red; 4, 23, 36). No style file defines semantic status colors, so this file supplies three mock-only colors in §2.1. Use them inside `data-mock` only, together with a differing label text (color is never the only signal). Chart series beyond the one colored series use solid vs dashed lines and the opacity ladder. If the user gives product or brand colors, those may color the data inside the mock instead.

---

### 2.1 Mock UI status colors

Real product UI uses colored statuses and charts; achromatic-only mocks read as placeholders. These colors are allowed **only inside a `data-mock` frame**, in every style (they are the product's UI, not the page's palette):

```css
[data-mock] {
  --mock-positive:  #1F8A65;  /* success, up, paid, healthy — cursor.com product-demo status green */
  --mock-negative:  #CF2D56;  /* error, down, failed, overdue — cursor.com product-demo status red */
  --mock-attention: #FECC33;  /* pending, warning, highlight — flim.ai semantic yellow */
}
```

Use them for status pills (12% fill + full-strength text or dot), deltas (↑ / ↓), and one chart series. **Attention on a light surface**: `#FECC33` is too pale for text, so its pill is a `--mock-attention` dot (or 20% fill) with the label in `var(--text)`. Never darken it into a new yellow — the self-check flags any color not in the style file or this section. Other chart series use `var(--text)` at the style's opacity steps. Keep them to small areas — a status pill, a dot, a delta, one line.

## 3. Shared base CSS

Copy once per page. The values marked "Minimal default" are swapped per §2.

```css
.pv {                                  /* the data-mock outer frame */
    --pv-mat: var(--surface-1);        /* Minimal default — §2 */
    --pv-r-outer: 16px;                /* Minimal default: §4 content card */
    --pv-r-inner: 8px;                 /* Minimal default: §4 feature card */
    --pv-r-control: 4px;               /* Minimal default: §4 input */
    --pv-text: 13px;                   /* visual-style.md §8: text inside a mock */
    --pv-row: 32px;                    /* visual-style.md §8: row height */
    position: relative;
    font-family: var(--font-body);
    font-size: var(--pv-text);
    font-weight: 400;
    color: var(--text);
}
.pv-mat {
    background: var(--pv-mat);
    border-radius: var(--pv-r-outer);
    padding: 6% 6% 0;                  /* UI fills ~88% of the mat: Front (3) ~87%, Cursor (A2.4) ~75% */
    overflow: hidden;
}
.pv-panel {
    background: var(--bg);
    border: 1px solid var(--surface-2);
    border-radius: var(--pv-r-inner);
}
.pv-row {
    display: grid;
    align-items: center;
    gap: 12px;
    min-height: var(--pv-row);
    padding: 0 12px;
    border-top: 1px solid var(--surface-2);
}
.pv-row.is-focused { background: var(--surface-1); }     /* the one focused state */
.pv-mono   { font-family: var(--font-mono); }
.pv-muted  { opacity: 0.5; }                              /* style §1 subtitle opacity */
.pv-label  { font-family: var(--font-mono); text-transform: uppercase; opacity: 0.4; }
.pv-cents  { opacity: 0.5; }                              /* cents dimmed: (41), (49) */
.pv-kpi    { font-family: var(--font-display); font-size: 20px; }  /* Minimal default: card heading (Colorful/Editorial: var(--font-body), §2) */
.pv-pill {
    display: inline-flex;
    align-items: center;
    padding: 0 8px;
    line-height: 1.6;
    border: 1px solid var(--surface-2);
    border-radius: var(--pv-r-control);
}
.pv-pill.is-strong { background: var(--text); color: var(--text-inverse); border-color: transparent; }
.pv-pill.is-quiet  { opacity: 0.5; }
.pv-avatar {
    display: inline-grid;
    place-items: center;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    font-family: var(--font-mono);
    background: var(--surface-2);
}
.pv-avatar:nth-child(3n+2) { background: var(--text); color: var(--text-inverse); }
.pv-avatar:nth-child(3n)   { background: var(--pv-mat); border: 1px solid var(--surface-2); }
.pv-cut {                              /* any panel cut by its frame: the last 56px dissolve, so no row is sliced */
    -webkit-mask-image: linear-gradient(to bottom, #000 calc(100% - 56px), transparent); mask-image: linear-gradient(to bottom, #000 calc(100% - 56px), transparent);
}
@media (max-width: 767px) {            /* rule 9a: rows wrap, secondary columns go, nothing truncates to "Ma…" */
    .pv { --pv-text: 12px; }
    .pv-row { min-height: 0; padding-top: 8px; padding-bottom: 8px; }
    .pv-row > * { white-space: normal; }
    .pv-hide-s { display: none; }      /* put on timestamps, owners, secondary columns */
}
```

Floating cards add the style's floating card depth (§2). In Minimal, write **no** `box-shadow` declaration at all (the self-check flags any shadow in Minimal). Use the border only.

Avatars: initials on three different fills, never identical grey circles (checklist item 6). If the user supplies photos or face illustrations, use those.

---

## 4. Choose a recipe

| Product category | Hero | Feature sections |
|---|---|---|
| Analytics, monitoring | 1 Rising screenshot | 3 Isolated chart card, 4 Bento |
| Developer tool | 6 Code window | 5 Close-up, 4 Bento |
| Collaboration, docs, project tools | 1 Rising screenshot or 2 Layered cards | 3 Isolated (comment thread, share dialog), 5 Close-up |
| AI assistant | 7 Chat | 3 Isolated answer card, 2 Layered cards |
| Fintech, personal finance | 2 Layered cards or 8 Phone | 3 Isolated chart card, 4 Bento |
| Commerce, inventory, operations | 1 Rising screenshot | 2 Layered cards, 3 Isolated order card |
| Design tool, canvas | 1 Rising screenshot (canvas with real artwork) | 5 Close-up, 3 Isolated (cursors, comments) |
| Consumer mobile app | 8 Phone | 8 Phone with toast, 3 Isolated |

The evidence behind the table: dark-theme samples lean toward isolated components, code, and fragments (10, 22, 25, 26, 41, 43, 46, 54); light pages lean toward full screens on mats (3, 11, 36). This is a tendency, not a rule.

---

## 5. Recipes

Each recipe gives the structure and the CSS that adds to §3. Content examples are in §6.

### Recipe 1 — Rising screenshot cut by the fold

**When**: a centered hero for a product with a dense main screen: analytics, inbox, project tracker, commerce back office, design canvas. Evidence: (3), (4), (17), (36); Linear A2.1, Notion A2.2, Cursor A2.3.

**Structure**: the app's own chrome (sidebar + top bar), one main view, one focused row or tab. No OS chrome. The hero section has no bottom padding, so the section edge cuts the visual through content.

```html
<div class="pv pv-rise" data-mock role="img" aria-label="Larkspur Ops dashboard: open orders by status">
  <div class="pv-mat">
    <div class="pv-panel pv-app">
      <aside class="pv-side">  <!-- workspace name + 6–8 nav labels, one active -->  </aside>
      <div class="pv-main">
        <header class="pv-top"> <!-- view title · date range · 1 primary button --> </header>
        <div class="pv-kpis">   <!-- 3–4 KPI cards: label + non-round value + signed delta --> </div>
        <div class="pv-table">  <!-- header row + 5–8 .pv-row rows, one .is-focused --> </div>
      </div>
    </div>
  </div>
</div>
```

```css
.hero { padding-bottom: 0; overflow: hidden; }               /* directional property, not shorthand */
.pv-rise { width: 72%; margin: 0 auto; max-height: 60vh; overflow: hidden; }  /* 63–78% wide (A2.1–A2.3) */
.pv-rise .pv-mat { border-bottom-left-radius: 0; border-bottom-right-radius: 0; }
.pv-rise .pv-panel { -webkit-mask-image: linear-gradient(to bottom, #000 calc(100% - 56px), transparent); mask-image: linear-gradient(to bottom, #000 calc(100% - 56px), transparent); }   /* = .pv-cut */
.pv-app  { display: grid; grid-template-columns: 22% 1fr; min-height: 400px; } /* §8 inner panel min-height */
.pv-side { padding: 16px 12px; border-right: 1px solid var(--surface-2); }
.pv-main { padding: 24px; }                                    /* §8 inner panel padding */
.pv-kpis { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 24px; }
@media (max-width: 767px) {
    .pv-rise { width: 100%; }
    .pv-app  { grid-template-columns: 1fr; }
    .pv-side { display: none; }
    .pv-kpis { grid-template-columns: repeat(2, 1fr); }
}
```

`max-height` sets how much shows above the fold. The visual should start at 35–75% of the fold height (A2.1, A2.2). Check the fold in the browser.

### Recipe 2 — Layered cards over a backing panel

**When**: a split hero or a feature row where two or three related facts tell the story better than one screen: a report with a tooltip, a desktop view with a phone alert, a chat with a code snippet. Evidence: layered cards in 11/55, e.g. (4), (5), (6), (23), (26), (33); mats in 19/55.

**Structure**: one main card (table or chart) and one smaller floating card that **overlaps only the main card's edge** — never its rows, columns, or text. The floating card repeats an ID or name from the main card (4, 23) and holds the focused state or the motion cue. In the evidence the overlap is shallow and falls on the frame's edge or padding: Craft's toast crosses the window's left edge, Framer's caption card crosses the frame's lower-left corner. A floating card that covers the main card's status or time column was the most common visible defect in generated pages (2026-10-14 style matrix): it hides the data the hero exists to show.

```html
<div class="pv pv-layers" data-mock role="img" aria-label="Weekly time report with an open day tooltip">
  <div class="pv-mat">
    <div class="pv-panel pv-layer-main">  <!-- title row + 5–8 rows or a chart --> </div>
    <div class="pv-panel pv-layer-float"> <!-- tooltip, alert, or detail card; same IDs as main --> </div>
  </div>
</div>
```

```css
/* A 3-track grid: main | 32px overlap | float. The main card reserves the overlap as right padding,
   so the floating card can only ever cover padding. Copy verbatim; change only the 0.42fr if needed. */
.pv-layers .pv-mat  { display: grid; grid-template-columns: minmax(0, 1fr) 32px minmax(0, 0.42fr); padding-bottom: 6%; }
.pv-layer-main      { grid-column: 1 / 3; grid-row: 1; padding: 16px 32px 0 0; }   /* 32px = the overlap track */
.pv-layer-float     {
    grid-column: 2 / 4; grid-row: 1;
    align-self: end; margin-bottom: 8%;  /* low on the right, like a note laid on the edge */
    position: relative; z-index: 1;
    padding: 16px;
    /* + the style's floating card depth (§2); in Minimal: the border from .pv-panel only */
}
@media (max-width: 767px) {
    .pv-layers .pv-mat { grid-template-columns: 1fr; }
    .pv-layer-main     { grid-column: 1; padding-right: 0; }
    .pv-layer-float    { grid-column: 1; grid-row: 2; margin: 12px 0 0; }   /* below the main card, never on it */
}
```

### Recipe 3 — Isolated hero component

**When**: one component carries the product's value: an issue composer, a patient record, a share dialog, a spending chart card, a comment thread. It suits dark pages and feature rows. Evidence: 10/55, e.g. Linear composer (10), Ease record (30), Origin chart (40), Slash chart (41), Framer share dialog (43), Loom comment (47).

**Structure**: a breadcrumb or label, a title, one full sentence, 3–4 property chips, and exactly one primary action (10, 22, 30). Show it at 1–1.5× real size, about 55% of the width when centered (10).

```html
<div class="pv pv-iso" data-mock role="img" aria-label="New issue composer in Halberd Tracker">
  <div class="pv-mat">
    <div class="pv-panel pv-iso-card">
      <div class="pv-label">ENG › Billing</div>
      <div class="pv-iso-title">Retry failed invoice webhooks</div>
      <p class="pv-muted">Retries stop after the third 502. We should back off and alert the on-call.</p>
      <div class="pv-iso-chips"><span class="pv-pill">Todo</span><span class="pv-pill">High</span>
        <span class="pv-pill">Priya Raman</span><span class="pv-pill">Cycle 41</span></div>
      <div class="pv-iso-actions"><span class="pv-btn-primary">Create issue</span></div>
    </div>
  </div>
</div>
```

```css
.pv-iso { width: 55%; margin: 0 auto; }
.pv-iso .pv-mat { padding: 6%; }
.pv-iso-card    { padding: 24px; font-size: calc(var(--pv-text) * 1.25); }  /* 1–1.5× real size */
.pv-iso-title   { font-family: var(--font-display); font-size: 20px; margin: 8px 0; } /* Minimal default: card heading (Colorful/Editorial: var(--font-body), §2) */
.pv-iso-chips   { display: flex; flex-wrap: wrap; gap: 8px; margin: 16px 0; }
.pv-iso-actions { display: flex; justify-content: flex-end; }
.pv-btn-primary { padding: 0 12px; line-height: var(--pv-row); border-radius: var(--pv-r-control);
                  background: var(--accent); color: var(--accent-text); }
@media (max-width: 767px) { .pv-iso { width: 100%; } }
```

A split section puts the component in the visual column at full column width.

### Recipe 4 — Bento of UI tiles with one lead tile

**When**: a features section with one clear main feature and 3 supporting ones. Evidence: bento in 6/55, e.g. Slash (37), Origin (38, 39); Cursor's full-width lead tile (A3.3); Ramp's swapped row widths (A3.4).

**Structure**: the lead tile spans the full row and is about twice as tall. Its fragment sits in the right 60% (A3.3). Each small tile holds **one** fragment (one list, one chart, one dialog), never a whole screen (37). The caption has two parts: "**Virtual accounts.** Create separate money pools…" (37). Each fragment is its own `data-mock`.

```html
<div class="pv-bento">
  <article class="pv-tile pv-tile-lead">
    <div class="pv-tile-text"><strong>Lead feature.</strong> One sentence.</div>
    <div class="pv" data-mock role="img" aria-label="…"> <!-- fragment --> </div>
  </article>
  <article class="pv-tile"> <div class="pv" data-mock role="img" aria-label="…">…</div>
    <p><strong>Feature.</strong> One sentence.</p></article>
  <!-- 2 more small tiles -->
</div>
```

```css
.pv-bento { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }  /* Minimal §7 bento */
.pv-tile  { padding: 32px; background: var(--surface-1); border-radius: var(--pv-r-inner); overflow: hidden; }
.pv-tile-lead { grid-column: 1 / -1; display: grid; grid-template-columns: 40% 60%; gap: 24px; }
.pv-tile .pv-panel { background: var(--bg); }                  /* surface nesting */
@media (max-width: 767px) {
    .pv-bento { grid-template-columns: 1fr; }
    .pv-tile-lead { grid-template-columns: 1fr; }
}
```

Grid, gap, and tile padding come from the active style (§7 grid, §3 card padding, §4 feature card radius). A schematic mini-UI (grey bars, dashed guides) is allowed only at icon scale, under 30% of the tile's height (29).

### Recipe 5 — Cropped close-up with callout

**When**: a feature row about one detail: a toggle list, a co-editing highlight, a filter menu. Evidence: close-ups in 3/55 (13, 18, 46) and 1.5–2× scale (18, 37, 40). Callouts are rare (3/55: 32, 46, 55). Add them only when the section names 2–4 specific behaviors.

**Structure**: one part of the UI at 1.5× scale, bleeding off the right and bottom edges (18). Optional callouts: up to 4 short labels, each with a thin rule above it (32), or one mono figure label such as "FIG 2.3" in a corner (46).

```html
<figure class="pv pv-crop" data-mock role="img" aria-label="Studio toggles: Vector, Pixel and Layout on">
  <div class="pv-mat">
    <div class="pv-panel pv-crop-inner"> <!-- 5–6 rows with mixed on/off states, first row .is-focused --> </div>
  </div>
  <span class="pv-fig pv-label">FIG 2.3</span>                    <!-- optional (46) -->
</figure>
<ul class="pv-callouts">                                            <!-- optional (32), max 4 -->
  <li>Inline comments</li><li>Text-to-issue commands</li>
</ul>
```

```css
.pv-crop .pv-mat  { aspect-ratio: 16 / 10; padding: 8% 0 0 8%; }   /* 16:10 frame (1) */
.pv-crop-inner    { width: 125%; font-size: calc(var(--pv-text) * 1.5);
                    border-right: 0; border-bottom: 0; }         /* bleeds right and bottom (18) */
.pv-fig           { position: absolute; top: 16px; left: 16px; }
.pv-callouts      { display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; list-style: none; padding: 0; }
.pv-callouts li   { padding-top: 12px; border-top: 1px solid var(--surface-2); }
@media (max-width: 767px) { .pv-callouts { grid-template-columns: 1fr; } }
```

The callout text uses the style's label or card heading role. Never use a left border on callouts (master Design Rules).

### Recipe 6 — Code or terminal window

**When**: developer tools, APIs, CLIs, infrastructure. Evidence: 4/55 code editors (21, 22, 24, 25). 4 of the 9 visuals with OS or browser chrome are developer tools.

**Structure**: a title bar (three dots + one or more file tabs), line numbers, 12–20 lines of real code (24: 12, 25: 15, 22: ~20), **one** highlighted focal line (25), and a status bar with real details: "Ln 17, Col 3 · Spaces: 2 · UTF-8 · TypeScript" (22) or "main · updated 2 days ago · 78 commits" (21). Optional: a terminal pane with one command and its output (21). If the headline names a code token, show that exact token on the focal line (25).

```html
<div class="pv pv-code" data-mock role="img" aria-label="retry.ts open in the editor with the backoff line highlighted">
  <div class="pv-code-bar"><i></i><i></i><i></i><span class="pv-mono">retry.ts</span>
    <span class="pv-mono pv-muted">queue.ts</span></div>
  <pre class="pv-code-body"><code><span class="ln">14</span>  const delay = <span class="k">backoff</span>(attempt, 250);
<span class="ln is-focused">15</span>  …</code></pre>
  <div class="pv-code-status pv-mono pv-muted">main · Ln 15, Col 9 · Spaces: 2 · UTF-8 · TypeScript</div>
</div>
```

```css
.pv-code { border-radius: var(--pv-r-outer); overflow: hidden; background: var(--surface-1);
           border: 1px solid var(--surface-2); }
.pv-code-bar { display: flex; align-items: center; gap: 8px; padding: 10px 16px;           /* §8 chrome strip */
               background: var(--surface-2); }
.pv-code-bar i { width: 8px; height: 8px; border-radius: 50%; background: var(--text); opacity: 0.2; }
.pv-code-body { margin: 0; padding: 16px 0; font-family: var(--font-mono); font-size: var(--pv-text);
                line-height: 1.6; overflow-x: auto; }
.pv-code-body .ln { display: inline-block; width: 32px; padding-right: 12px; text-align: right; opacity: 0.4; }
.pv-code-body .k  { opacity: 1; }        /* syntax: opacity ladder — keywords 1, names 1, strings 0.5, comments 0.4 */
.pv-code-status { padding: 6px 16px; border-top: 1px solid var(--surface-2); font-size: 12px; }
```

- **Highlight the focal line** by giving its whole line a `var(--surface-2)` background.
- **Dark window on a light page** (as in 21, 22, 25): in Minimal, Business, and Colorful, use `background: var(--text); color: var(--text-inverse)`. In Editorial, use the dark stage background (§8 Section Background Switching).
- **Traffic lights** are drawn as three dots at opacity 0.2 (the weakest-text role). No style defines the red, yellow, and green colors, and the evidence does not need them to read as a window.
- **Syntax colors** are not in any style file, and §2.1 covers statuses, not syntax. Use the opacity ladder; at most the focal token may use `--mock-positive` (as in 25, a green comment).

### Recipe 7 — Chat or AI conversation

**When**: AI assistants, support bots, copilots. Evidence: 6/55 show a chat: Sana (31), Intercom Fin (32), Intercom (33), Le Chat (34), Granola (35), Superpower (52).

**Structure**: a user message with a specific, long question (31: "How does taking intermittent parental leave affect my health insurance coverage?"). The assistant answers in full, and the best answers include a rich artifact: a Gantt chart (34), a map card with an order number (33), or a cited source (32). Below that, an input with a domain placeholder ("Ask anything…", "Type a reply…") or partly typed text with a caret (35). If the section lists capabilities, the conversation shows each one (32).

```html
<div class="pv pv-chat" data-mock role="img" aria-label="Assistant answering a renewal question with a cited source">
  <div class="pv-mat">
    <div class="pv-panel pv-chat-panel">
      <div class="pv-msg pv-msg-user">Which Fernhill accounts renew before March 14, and who owns each one?</div>
      <div class="pv-msg pv-msg-ai">Three accounts renew before March 14 … <div class="pv-panel pv-artifact">
        <!-- 3 rows: account · renewal date · owner avatar --></div>
        <span class="pv-label">Source · CRM export, Feb 3</span></div>
      <div class="pv-chat-input"><span data-type>Draft a renewal note to Jonas</span><span class="pv-caret"></span></div>
    </div>
  </div>
</div>
```

```css
.pv-chat-panel { display: grid; gap: 16px; padding: 24px; }
.pv-msg        { max-width: 80%; line-height: 1.6; }
.pv-msg-user   { justify-self: end; padding: 8px 12px; background: var(--surface-1); border-radius: var(--pv-r-inner); }
.pv-artifact   { margin: 12px 0 8px; }
.pv-chat-input { padding: 12px 16px; border: 1px solid var(--surface-2); border-radius: var(--pv-r-control); }
.pv-caret      { display: inline-block; width: 1px; height: 1em; margin-left: 1px;
                 vertical-align: text-bottom; background: var(--text); }
```

The input uses the style's input or search-bar radius (Minimal: search bar 160px pill) when it is the visual's centerpiece (35).

### Recipe 8 — Phone frame

**When**: consumer mobile apps, personal finance, health, any product whose main surface is a phone. Evidence: device frames in 10/55, e.g. Norma (19), HoneyBook (20), Monarch (48), Aave (49), Superpower (52).

**Structure**: one phone, straight-on or tilted about 10° (48), with a status bar ("9:41"). Show it at real size, not shrunk (rule 10). The phone is often cut by the bottom of its panel (20, 49). Optional: a notification card wider than the phone, overlapping its edge (20). That card is the motion cue.

```html
<div class="pv pv-phone-wrap" data-mock role="img" aria-label="Savings screen: balance and this week's earnings">
  <div class="pv-mat">
    <div class="pv-phone">
      <div class="pv-phone-status pv-mono"><span>9:41</span></div>
      <div class="pv-phone-screen"> <!-- greeting · balance with dimmed cents · signed change · 7-bar chart with one bar focused --> </div>
    </div>
    <div class="pv-panel pv-toast">Priority lead · now — Get back to Dana Whitfield about the March 18 shoot.</div>
  </div>
</div>
```

```css
.pv-phone-wrap .pv-mat { position: relative; padding: 8% 8% 0; max-height: 60vh; }  /* cut by the panel bottom (49) */
.pv-phone {
    width: 100%;
    max-width: 390px;                  /* device width at 1× — real size, not shrunk (rule 10) */
    aspect-ratio: 9 / 19.5;            /* device proportion */
    margin: 0 auto;
    background: var(--bg);
    border: 8px solid var(--text);     /* bezel; on dark pages use var(--surface-2) */
    border-radius: var(--pv-r-outer);  /* GAP: no phone-corner role exists — see note */
    overflow: hidden;
}
.pv-phone-status { display: flex; justify-content: space-between; padding: 12px 24px; font-size: 12px; }
.pv-toast { position: absolute; left: 4%; right: 4%; top: 24%; padding: 12px 16px; }
                                       /* wider than the phone (20); + the style's floating card depth */
```

Tilt (optional, 48): `transform: rotate(-10deg)` on `.pv-phone`. Use it only in a split hero, never with a toast.

**Gap**: real phones have a much larger corner radius than any card role in the style files. Until a style defines a device-frame radius, use `--pv-r-outer`. Report it under "values with no style role".

---

## 6. Content-fill guide

Fill every field. Use non-round numbers, real-looking IDs, and names that differ in length and origin. Keep one fictional business per page and reuse its names across visuals (rule 6). Each row's pattern copies an observed sample.

| Category | Nav / labels | Example rows | Numbers and IDs | Focused state | Pattern from |
|---|---|---|---|---|---|
| **Analytics, monitoring** | Overview · Events · Funnels · Alerts · Settings | "Checkout started · 4,812 · ↑3.6%"; "p95 latency /api/orders · 212 ms"; "INC-3147 · Critical · Payments API · 4m ago" | 18,342 weekly actives; 61.4% conversion; signed deltas "+212", "−9 min" | open tooltip on one chart point | (4), (6), (7) |
| **Developer tool** | file tree: `src/`, `retry.ts`, `queue.ts`, `README.md` | code lines with real identifiers; terminal `$ globex deploy --env staging` → `✓ Deployed 3 functions in 4.7s` | "Ln 15, Col 9", "78 commits", "updated 2 days ago", commit hash `a3f9c21` | the focal code line | (21), (22), (25) |
| **Collaboration, docs** | breadcrumb "Q3 Launch › Meeting notes"; facepile + Share | "Maya Okafor · Viewing now · Owner"; "Jonas Lindqvist · Viewed 3h ago · Can edit"; doc paragraph of real prose | "Feb 3, 2026", "2 hours ago", "Cycle 41" | one highlighted text span with a name tag | (2), (43), (46) |
| **AI assistant** | thread title, model or mode chip, "Ask anything…" | long specific question; full answer with a 3-row table, a cited source, or a step list "Step 4 — Build the SQL query ✓" | order "#48213907", "arrives 11 AM, March 12" | the input with partly typed text | (23), (32), (33), (34) |
| **Fintech, finance** | Accounts · Cards · Transactions · Payments · Reports | "Brightmoor Studio · −$472.42 · Aug 3"; "Office supplies · $1,385.00 (37.2%)"; "Joint savings · $30,412.88" | balances with cents dimmed: $48,382**.09**; "+$17.41 this week"; "38 transactions · average $116.23" | one selected transaction row | (12), (36), (41), (49) |
| **Commerce, operations** | Orders · Products · Inventory · Customers | "Ethiopian Yirgacheffe · 46 bags · In stock"; "Sumatra Mandheling · 7 bags · Low stock"; "Order #10482 · Paid · $86.40" | "Pending orders 240 ↑2%", "Low-stock SKUs 12 ↑3" | one open order in a side panel | (12), (23) |
| **Design tool, canvas** | layers panel, properties panel, toolbar with one active tool | a design with its own real content (a recipe card, a product listing); layer rows "Hero / Title / Button" | "E4FF97 100%", "W 375 H 812", "Saved 88 · Cooked 24" | one selected layer with handles; named cursors "Priya", "Theo" | (11), (13), (45) |

People names: mix origins and lengths (Maya Okafor, Jonas Lindqvist, Priya Raman, Theo Marchetti, Dana Whitfield). Companies: invented per page, coined words, surnames, or places (Halberd, Larkspur, Quarry & Co, Fernhill, Brightmoor) — never the stock placeholder set (Northwind, Contoso, Fabrikam, Globex, Initech, Acme).

**Never**: "Item 1", "User Name", "Lorem ipsum", "$1,000", "100%", "123", "John Doe", "Acme" next to another placeholder, empty table cells, or an input labelled "Input".

---

## 7. Realism checklist

Check each item in the HTML or on the rendered page before delivery. Adapted from the evidence checklist.

1. **No skeletons in the focal visual.** No grey bars standing for text, no empty image frame, no icon alone in a grey square, no blank chart area. Grey bars appear only in faded background layers (opacity ≤ 0.3) or icon-scale tiles.
2. **At least 3 proper nouns.** People, a fictional customer, project or file names, all from one domain.
3. **Numbers are specific and non-round.** Cents, seconds, IDs, signed deltas. No "$1,000", "100%", or "123".
4. **Exactly one focused state.** One selected row, active tab, open tooltip, highlighted span, or focused input.
5. **2–3 status states are visible**, told apart by label plus the §2.1 mock status colors (or by fill: strong / outline / opacity 0.5).
6. **Avatars differ.** Initials on three different fills, or user-supplied photos. Never identical grey circles.
7. **At least one relative time or concrete date.**
8. **A fragment at readable size.** Mock text is 12–13px at 1×, or larger in a close-up. A full screen keeps its KPI numbers readable.
9. **The parts agree.** Totals match their rows, the same ID appears across layered cards, and the visual shows the headline's claim.
9a. **Nothing covers content.** No floating card, cutout, cursor, or decoration sits on top of a row, label, or number. Overlaps fall on edges and padding only. On a 390px screen layered cards stack instead of overlapping.
10. **At most one motion cue**, and the static HTML shows its final state.
11. **App chrome, not generic chrome.** Domain nav labels. Traffic lights only on desktop or developer tools.
12. **Color comes from the mat, the data, or the content.** The UI panels stay `var(--bg)` or `var(--surface-*)`.
13. **Cut with intent.** At most one edge bleeds, and the cut falls through content.
14. **One primary action inside the visual.** The rest are outline or text.
15. **The frame has `data-mock`, `role="img"`, and an `aria-label`.** No real third-party brand names inside.
