# Visual Style Guide — Default Design System

> Default design tokens for Light / Dark dual themes

> **Must use — at the end of this file, §12 Style Signature.** Read this file to the last line. Every page in this style needs:
> 1. When the page has a hero (not 404, not a single non-hero section): the hero built from §12.2 "Specimen Field", starting from its HTML example and keeping the `.specimen-field` class (the self-check looks for it)
> 2. At least two items from §12.3 Signature details
> 3. §12.4 Motion personality and §12.6 Drift guard, followed as written
> 4. §12.7 Screenshot test, run against the finished page before delivery

This file defines the default visual style for all page types. Unless the user provides explicit brand design specifications, follow the tokens and principles in this file strictly. Page-type-specific component tokens are supplemented in the corresponding Skill's `references/` directory.

---

## Design Philosophy

Four core principles:

1. **Color silence** — Pure achromatic grays (zero hue tinting); chromatic color only for narrow semantic signals, occupying <10% of visible page area
2. **Shadowless depth** — Zero box-shadow; hierarchy established through background color steps and element layering
3. **Typography as architecture** — Font family switching is the hierarchy signal; weight is locked constant; size alone determines importance
4. **Content as decoration** — Product screenshots/output serve as hero visuals and brand texture; reject illustrations, abstract gradients, stock photos

---

## 1. Color System

### Light Theme

```
--bg:           #FFFFFF        Page background
--surface-1:    #F5F5F5        Cards, code blocks, product screenshot backgrounds
--surface-2:    #E9E9E9        Title bars, dividers, secondary surfaces
--text:         #141414        All text (hierarchy controlled via opacity)
--text-inverse: #FFFFFF        Text on dark surfaces
--accent:       #141414        CTA button background (default = --text; user brand color overrides this value)
--accent-text:  #FFFFFF        CTA button text (default = --text-inverse; adjusted based on accent brightness)
```

**Text hierarchy controlled via opacity, not color**:
```
Primary text:         color: #141414; opacity: 1
Subtitle/description: color: #141414; opacity: 0.5
Auxiliary/label:      color: #141414; opacity: 0.4
Weakest (copyright):  color: #141414; opacity: 0.2
Logo wall:            color: #141414; opacity: 0.45 (raised from 0.15 on 2026-10-14: real logo walls on Mobbin — Granola, incident.io, Mercury — are clearly legible; at 0.15 sample wordmarks read as placeholders)
```

### Dark Theme

```
--bg:           #0A0A0A        Page background
--surface-1:    #141414        Cards, code blocks, product screenshot backgrounds
--surface-2:    #1F1F1F        Title bars, dividers, secondary surfaces
--text:         #EDEDED        All text (hierarchy controlled via opacity)
--text-inverse: #0A0A0A        Text on light surfaces
--accent:       #EDEDED        CTA button background (default = --text)
--accent-text:  #0A0A0A        CTA button text (default = --text-inverse)
```

**Text hierarchy also via opacity**:
```
Primary text:         color: #EDEDED; opacity: 1
Subtitle/description: color: #EDEDED; opacity: 0.5
Auxiliary/label:      color: #EDEDED; opacity: 0.4
Weakest (copyright):  color: #EDEDED; opacity: 0.2
Logo wall:            color: #EDEDED; opacity: 0.45
```

### Accent Color Rules

- **Default accent is the text color**: `--accent` defaults to `--text`; output is identical to no-brand-color
- If the user provides a brand color, only override `--accent` and `--accent-text` (two variables)
- **Chromatic color occupies <10% of visible page area**. Everything else uses achromatic gray scale
- All neutral colors must be pure achromatic (zero hue shift) — no warm gray, cool gray, or blue-gray

**`--accent` allowed uses (exhaustive — do not exceed this list)**:
- ✅ Primary CTA button background (`.btn-dark`, required)
- ✅ Nav CTA button background (optional, syncs with primary CTA)
- ✅ Pricing recommended tier border ring `rgba(accent, 0.2)` (optional)
- ✅ Link hover color (optional)
- ❌ Toggle / Switch active state (functional control, always use `var(--text)`)
- ❌ Icon backgrounds, badge fills, section backgrounds
- ❌ Gradients, glows, semi-transparent overlays

### Absolutely Forbidden

- Different background colors for different sections
- Different accent colors for individual feature cards
- Colored circular/square backgrounds behind icons
- Gradient CTA buttons
- Semi-transparent colored overlays
- Hue-shifted grays (e.g., slate #64748B, zinc #71717A) — use pure gray + opacity

---

## 2. Typography System

### Font Families — Three-Font Switching

| Role | Font | Usage |
|------|------|-------|
| Display (reading) | `'DM Sans', -apple-system, sans-serif` | Headings, body text, navigation, buttons |
| Mono (structural) | `'DM Mono', 'SF Mono', Consolas, monospace` | Labels (LABEL), metadata, counters, code |
| Body (long-form) | `-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif` | FAQ answers, paragraph descriptions |

**Copy this declaration verbatim — do not compose your own fallback chain** (all Skills reference it via `var(--font-display)` etc.):

```css
:root {
    --font-display: 'DM Sans', -apple-system, sans-serif;
    --font-mono:    'DM Mono', 'SF Mono', Consolas, monospace;
    --font-body:    -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
}
```

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
```

**The hierarchy signal is font family switching, not weight variation.** Weight is locked at 500 (display) and 400 (mono/body) — do not use regular/bold within the same role for emphasis.

### Type Scale

```
Hero heading:     clamp(48px, 7vw, 80px)    weight: 500   tracking: -0.02em   line-height: 1.05
Section heading:  clamp(32px, 4vw, 47px)    weight: 500   tracking: -0.02em   line-height: 1.1
Feature heading:  27px                       weight: 500   tracking: -0.54px   line-height: 1.2
Card heading:     20px                       weight: 500   tracking: -0.4px    line-height: 1.3
Body text:        18px                       weight: 400   tracking: normal    line-height: 1.6
Body secondary:   16px                       weight: 500   tracking: normal    line-height: 1.6
Button:           14px                       weight: 500   tracking: normal
Navigation:       14px                       weight: 500   tracking: normal
Label:            12px                       weight: 400   tracking: +0.72px   text-transform: uppercase
```

### Key Rules

1. **Negative tracking scales linearly with font size**: approximately -2% of font size (80px → -1.6px, 47px → -0.94px, 27px → -0.54px)
2. **Weight 500 covers 70%+ of all text**. Only body paragraphs and FAQ answers use weight 400
3. **Hero heading must be at least 3× body text**: body 18px → heading at least 54px
4. **Subtitles change opacity, not color**: same color as heading, opacity 0.5
5. **Labels always**: 12px / mono / 400 / uppercase / +0.72px tracking / opacity 0.3-0.4

---

## 3. Spacing System

### Base Unit: 8px

```
Spacing scale: 6 · 8 · 12 · 16 · 24 · 32 · 58 · 128 · 180 px
```

### Specific Applications

```
Section padding (top and bottom padding for each section):  180px
Note: Visual gap between two adjacent sections = 180 + 180 = 360px. This is intentional —
generous breathing space is a core characteristic of this system (see "more is better" rule #4)
Section internal (heading to content):              58px
Hero top whitespace (nav to hero heading):          128px
Hero heading to subheading:                         24px
Subheading to CTA:                                  48px
Logo wall vertical padding:                         128px
Footer top padding:                                 128px
Footer bottom padding:                              48px (below the copyright bar; majority value across validated pages)
Card internal padding:                              32px
Card gap:                                           20px (bento) / 24px (list)
Grid gutter:                                        24px
Feature row spacing (alternating rows):             128px
```

### Narrow Screen Spacing (< 768px)

Desktop spacing is too large on narrow screens. Reduce according to this reference table. Do not invent intermediate values:

```
Desktop 180px (section rhythm)  →  96px
Desktop 128px (hero top / footer top / logo wall)  →  80px
Desktop 58px (heading to content)  →  40px
Desktop 32px (card padding)  →  24px
Desktop 24px / 20px (gap)  →  keep unchanged
Left/right padding 32px  →  20px
```

### Key Rules

1. **180px is the section rhythm baseline**. Do not use 64px or 96px — that is too tight
2. **128px is the large breathing space** (hero top, footer top, logo wall)
3. **58px is the standard heading-to-content distance**
4. **When in doubt, choose the larger spacing value**
5. **Narrow screens use the reference table above — do not scale linearly**

---

## 4. Border Radius System

```
Button:         2px (sharp, authoritative)
Input:          4px
Feature card:   8px
Content card:   16px (screenshot frame, testimonial card)
Toggle switch:  40px
Search bar:     160px (pill shape)
```

Do not use a single border-radius value for everything. Do not use 999px for fully-rounded buttons.

---

## 5. Shadow System

**Zero shadows.** No element on the entire site uses box-shadow.

Hierarchy is established through:
- Background color steps: #FFFFFF → #F5F5F5 → #E9E9E9 (Light) / #0A0A0A → #141414 → #1F1F1F (Dark)
- Borders: 1px solid surface-2 color value
- Element layering (z-index + overlap)

Rationale: Product screenshots and content already carry their own light and depth cues. Adding artificial shadows at the UI layer creates competing light sources. Keeping the interface flat means the only depth perception comes from the content itself — the product is the richest visual element, not the interface decoration.

---

## 6. Transitions & Motion

```
hover transform:   transform 0.2s ease-in-out (button micro-lift translateY(-1px))
card hover:        transform 0.2s ease-in-out (card lift translateY(-4px) + border-color 0.3s)
color/opacity:     opacity 0.3s linear or color 0.3s linear
scroll entrance:   opacity + transform 0.8s cubic-bezier(0.16, 1, 0.3, 1)
```

Do not use bounce, spring, or transitions longer than 1s.
All animations must be wrapped in `@media (prefers-reduced-motion: no-preference)`.

→ Full pattern recipes and JS implementations: see `shared/interaction-patterns.md`

---

## 7. Grid System

```
Main grid:       max-width 1080px, centered, padding 0 32px
Subtitle measure: max-width 540px (line width cap for hero/section subtitles to prevent long lines)
Bento grid:      3 columns / 20px gap (.featured spans 2 columns)
Alternating rows: 2 columns / 58px gap / align-items: center
Logo row:        flex / 58px gap / center
```

---

## 8. Component Tokens

### Buttons

```css
/* Primary CTA */
.btn-dark {
    display: inline-flex;           /* Required: <a class="btn-dark"> is inline by default;
                                       without this, margin-top and transform are ignored */
    align-items: center;
    gap: 8px;                       /* space between icon and label */
    padding: 8px 16px;
    font-size: 14px;
    font-weight: 500;
    font-family: var(--font-display);
    line-height: 20px;              /* 8 + 20 + 8 = 36px button → 16 + 36 + 16 = 68px nav */
    background: var(--accent);      /* default = --text; brand color overrides this value */
    color: var(--accent-text);      /* default = --text-inverse */
    border: none;
    border-radius: 2px;
    cursor: pointer;
    text-decoration: none;          /* links styled as buttons must not show underline */
    transition: transform 0.2s ease-in-out;
}
.btn-dark:hover { transform: translateY(-1px); }

/* Secondary CTA */
.btn-outline {
    display: inline-flex;           /* Same as .btn-dark — required for <a> elements */
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    font-size: 14px;
    font-weight: 500;
    font-family: var(--font-display);
    line-height: 20px;              /* 8 + 20 + 8 = 36px button → 16 + 36 + 16 = 68px nav */
    background: transparent;
    color: var(--text);
    border: 1px solid var(--surface-2);
    border-radius: 2px;
    cursor: pointer;
    text-decoration: none;
    transition: border-color 0.3s linear;
}
.btn-outline:hover { border-color: var(--text); }

/* Large CTA — used for Hero CTA button group (both primary and secondary).
   Default 14px buttons look small under an 80px heading. Both primary and
   secondary in Hero use btn-lg for visual balance; nav CTA stays 14px
   so the Hero primary button and nav CTA are not pixel-identical */
.btn-lg {
    padding: 12px 24px;
    font-size: 16px;
}

/* ─── DARK SECTION BAND ──────────────────────────────────────────────────────
   .section-dark = a var(--text)-background band inside an otherwise light page.
   This is NOT the same as a dark-theme page.

   Dark-theme page:  --bg = #0A0A0A, --text = #EDEDED. Buttons and text use
                     theme variables and already contrast against the background.
                     Do NOT apply .section-dark to a dark-theme page or its sections.

   .section-dark:    A light-page section whose background is var(--text) = #141414.
                     All text, borders, and buttons must be inverted to --text-inverse.
                     Apply this class whenever you set `background: var(--text)` on a section.

   Usage: <section class="section-dark"> — CTA bands, dark hero overlays, any
   section that sets background: var(--text) in a light-theme page.
   ─────────────────────────────────────────────────────────────────────────── */
.section-dark {
    background: var(--text);
    color: var(--text-inverse);
}

/* Secondary CTA on dark-band sections (.section-dark).
   Must override .btn-outline colors — otherwise color: var(--text) is the same
   as the dark background, making text invisible.
   This is the same class of error as the nav specificity trap documented in navigation.md */
.section-dark .btn-outline {
    color: var(--text-inverse);
    border-color: rgba(255, 255, 255, 0.25);
}
.section-dark .btn-outline:hover { border-color: var(--text-inverse); }

/* Primary CTA on dark backgrounds (e.g., inverted button in dark CTA section).
   With no brand color, --accent = --text = #141414, and the dark section background
   is also var(--text) = #141414 — btn-dark's background: var(--accent) becomes
   invisible against the background.
   The Dark Full-Width variant of the CTA section needs an inverted button: bg = --text-inverse, color = --text */
.section-dark .btn-dark {
    background: var(--text-inverse);
    color: var(--text);
}
.section-dark .btn-dark:hover { transform: translateY(-1px); filter: brightness(0.95); }

/* Keyboard accessibility — zero-shadow system uses outline, not box-shadow */
:focus-visible {
    outline: 2px solid var(--text);
    outline-offset: 2px;
}
.section-dark :focus-visible { outline-color: var(--text-inverse); }

/* Dark Theme: --accent defaults to #EDEDED, --accent-text defaults to #0A0A0A
   With brand color, enhance hover: bright brand colors add filter: brightness(0.9),
   dark brand colors add filter: brightness(1.15) */
```

### Navigation

```css
/* Nav height is a fixed value: 68px = 16px padding × 2 + 36px button height.
   When nav uses position: fixed it leaves the document flow — body must compensate,
   otherwise Hero's 128px top whitespace measures from the viewport top and the
   heading sits under the nav */
:root { --nav-h: 68px; }
body { padding-top: var(--nav-h); }   /* only needed for fixed nav */
/* In-page anchor jumps need to clear the fixed nav:
   [id] { scroll-margin-top: var(--nav-h); }
   Otherwise clicking a nav link scrolls the heading under the nav */

nav {
    padding: 16px 0;    /* Left/right padding is provided by the inner .container,
                           otherwise the logo shifts 32px right of section content edges */
    /* Frosted glass backdrop — prevents content from showing through fixed nav on scroll.
       No opaque background, no border-bottom. */
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}
/* Dark theme nav backdrop */
[data-theme="dark"] nav,
.dark nav {
    background: rgba(10, 10, 10, 0.85);
}
nav > .container {
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;    /* Matches all sections' .container */
}
nav a {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    opacity: 0.5;
    transition: opacity 0.3s linear;
}
nav a:hover { opacity: 1; }
```

### Label

```css
.label {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
}
```

### Card

```css
.card {
    padding: 32px;
    background: var(--surface-1);
    border-radius: 8px;             /* feature card */
    /* zero shadow, zero border */
}

.card-content {
    padding: 32px;
    background: var(--bg);           /* white card inside a surface-1 section */
    border-radius: 16px;             /* content card */
}
```

**Surface nesting rule** — nested background colors must step toward the page background, not repeat the parent:
- Inside `var(--bg)` section → card uses `var(--surface-1)`
- Inside `var(--surface-1)` section or card → nested element uses `var(--bg)` (**not** `var(--surface-1)`)
- Inside `var(--surface-1)` card → placeholder image/screenshot frame uses `var(--bg)`
- Inside `var(--surface-2)` → nested element uses `var(--surface-1)`

Using the same surface level for parent and child makes them invisible against each other. Applies to: thumbnail placeholders inside article cards, screenshot frames inside feature cards, logo squares inside integration cards, product screenshots inside product cards.

### Synthetic Product Visual

> **Full recipe set: `shared/product-visuals.md`** — composition recipes, style binding, content-fill guide, and realism checklist. The tokens below are the frame. Grey placeholder bars are allowed only in background layers (faded, behind a legible focal element), never in the focal visual.

When no product screenshot is available, build a UI mock in HTML/CSS using these tokens. This is the fix for the project's #1 quality issue ("structurally correct but looks AI-generated"). A well-executed synthetic visual reads as a real product interface.

```
Outer frame:    var(--surface-1) / border-radius 16px / padding 12px   ← content card radius
Chrome strip:   var(--surface-2) / border-radius 12px 12px 0 0 / padding 10px 16px
                font-family var(--font-mono) / font-size 12px / font-weight 400 / opacity 0.4
                Content: plausible title — a filename, view name, dashboard name, or URL
Inner panel:    var(--bg) / border-radius 8px / min-height 400px / padding 24px   ← bg, not surface-1
Text inside:    font-size 12px–13px (step down so it reads as UI, not page content)
                font-weight 400 (body weight inside mock UI)
Row height:     28–32px per data row (enough for 12px text + padding)
```

**Pick the mock layout that matches what the product does:**

| Product does | Build this |
|---|---|
| Organizes records, people, tasks | List or table — column headers + 5–8 rows, one row in selected/active state |
| Schedules, tracks time, shows history | Timeline or calendar — labelled axis, 3–5 bars or events |
| Runs, builds, queries, transforms data | Split pane — mono code input + result output below |
| Moves work through stages | Board — 3 columns with headers, 2–3 cards each |
| Reports, measures, monitors | Metric row + one simple chart — numbers in display font, chart from divs |

**Fill with real domain content**: A scheduling tool shows real timezone names; a database tool shows real column names. Generic placeholders ("Item 1", "Lorem ipsum", empty grey rectangles) defeat the entire purpose. The inner panel must contain real rows, columns, labels — never grey bars.

### Logo Wall

```css
.logo-wall {
    padding: 128px 32px;
    text-align: center;
}
.logo-wall-label {
    /* uses .label styles */
    opacity: 0.3;
    margin-bottom: 32px;
}
.logo-placeholder {
    font-family: var(--font-display);
    font-size: 16px;
    font-weight: 500;
    color: var(--text);
    opacity: 0.45;
}
```

### Testimonial

```css
.testimonial {
    padding: 32px;
    background: var(--bg);
    border-radius: 16px;
    /* zero shadow */
}
.testimonial blockquote {
    font-family: var(--font-display);
    font-size: 16px;
    font-weight: 500;
    line-height: 1.6;
    color: var(--text);
    /* no quotation mark decoration */
}
.testimonial-role {
    font-family: var(--font-mono);
    font-size: 12px;          /* label scale — was 11px (off-scale) */
    font-weight: 400;
    letter-spacing: 0.72px;   /* label tracking — was 0.5px (off-scale) */
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;             /* label opacity — was 0.35 (off-ladder) */
}
```

### Text Links

```css
.text-link {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    text-decoration: none;
    transition: opacity 0.3s linear;
}
.text-link::after { content: ' \2192'; }
.text-link:hover { opacity: 0.7; }
```

### Section Background Switching

```
Default:          var(--bg)          Most sections
Emphasis section: var(--surface-1)   At most 1-2 sections (e.g., Social Proof)
Title bar:        var(--surface-2)   Product screenshot window title bars

Not allowed: colored backgrounds, gradient backgrounds, more than 2 background colors
```

---

## 9. Verification Checklist

Check each item after generating a page:

1. **Color silence**: Is chromatic color area <10%? Are neutral colors pure achromatic (zero hue)?
2. **No shadows**: Does any element use box-shadow? If so, remove it
3. **Typography as architecture**: Do labels use mono font? Is weight 500 at 70%+? Is heading tracking negative?
4. **Content as decoration**: Do visual elements come from product content (screenshots/code/work), not illustrations/gradients/abstract graphics?
5. **Spacing rhythm**: Is section spacing ≥ 180px? Is Hero top whitespace ≥ 128px?
6. **Radius grading**: Are buttons 2px? Feature cards 8px? Content cards 16px? Rather than a uniform value?
7. **Opacity hierarchy**: Do subtitles use opacity 0.5 (not a different shade of gray)? Are labels opacity 0.3-0.4?

---

## 10. Brand Customization

When the user provides a brand color or custom font, override the defaults following these rules. With no brand input, `--accent` = `--text`, and output is identical to the default.

### 10.1 Brand Color Override

When the user provides a brand color hex value:

1. Set `--accent` to that color value
2. Calculate `--accent-text`: brand color luminance < 0.5 → `#FFFFFF`; luminance ≥ 0.5 → `#000000`
3. `.btn-dark` automatically uses `var(--accent)` / `var(--accent-text)` — no additional changes needed
4. Optionally select 0-2 secondary uses (from the allowed list above), declared in the Page Spec
5. Hover state: keep `translateY(-1px)`; brand-colored buttons additionally use `filter: brightness(0.9)` (bright brand colors) or `filter: brightness(1.15)` (dark brand colors)
6. All surface, text, and border colors remain achromatic — brand color does not spread to the page frame

### 10.2 Font Override

When the user provides a brand font name:

1. Replace `--font-display` value, keeping the system sans fallback chain
2. Update the Google Fonts `<link>` to load the new font at weights 400 + 500
3. Tracking adjustment:
   - Geometric sans (Inter, Outfit, Plus Jakarta Sans, Manrope) → keep `-0.02em`
   - Humanist sans (Source Sans, Lato, Open Sans, Nunito) → reduce to `-0.01em`
   - Uncertain → keep `-0.02em`
4. Weight fallback: if the font lacks 500, use 600; if only 400/700 available, use 400 for body, 700 for display, and note this in the Page Spec
5. `--font-mono` stays DM Mono unless the user explicitly specifies a mono font
6. `--font-body` stays system sans unless the user explicitly specifies a body font

### 10.3 Multi-Color Palette

When the user provides primary + secondary colors: primary → `--accent`, secondary is written directly into at most 1-2 CSS rules (no new variables introduced), total chromatic area still <10%.

When the user provides a full palette (5+ colors): the deepest or most saturated color → `--accent`, the rest are not used for surface/background. In the delivery notes, explain to the user which colors were used and which were intentionally omitted.

---

## 11. Archetype Adaptations (Landing Page)

> These adaptations are Landing Page-specific. See `pages/landing-page/references/archetypes.md` §"Visual Token Adaptations by Archetype" for the complete table.
> Other page types have their own archetype definitions in their respective `references/archetypes.md` files.
> Style Presets (Phase 7) will each have their own visual-style file — do not copy these archetype notes into Style Preset files.

---

## 12. Style Signature

> What makes a page unmistakably Minimal rather than "Minimal tokens on a generic skeleton". Evidence: flim.ai (Light DNA) and Linear (Dark DNA). Every value below is quoted from §1–§8 of this file unless a DNA file is cited.

### 12.1 Character

Minimal is a **gallery wall for the product**: white walls, black type, and the product's own content hung on a measured grid. flim.ai's taste decisions explain each part. *Chromatic Silence* — pure achromatic surfaces "act like museum walls: they hold content without editorializing it", so the only color on the page comes from the product. *Shadowless Depth* — depth comes from flat surface steps and physically overlapping content, never from a competing light source. *Typography as Architecture* — weight is locked at 500 and size alone carries importance, so the page has exactly two voices: huge display type and tiny mono labels, with very little in between. *Content-as-Chrome* — the hero is a collage of the catalog itself, "proof-of-product". Linear's dark DNA adds the same restraint at night: "brand lives in white, not in color" and depth through a 1px ring, not a shadow. The result should feel precise, quiet, and confident — like an index or a specimen sheet, not a sales page.

### 12.2 Hero showcase (mandatory) — "Specimen Field"

**Composition** (from the flim.ai home hero screenshot):

1. **Top band on `var(--bg)`** — a two-column split, `7fr 5fr`: the hero heading huge and flush left, two or three lines at most; the subtitle and CTAs in the right column, aligned to the heading's top. No centered stack. (flim: wordmark left, three-line statement + CTA right.)
2. **Specimen field below** — a full-bleed `var(--surface-1)` band ruled with a hairline grid (lines `var(--surface-2)`), holding **one focal fragment and exactly two satellites**, one in each side gutter at different heights, overlapping nothing and casting no shadow. The focal fragment takes the middle ~60% (large enough to read as the product, not a widget). Each satellite is a small real-content card at full contrast — a status, a KPI, an avatar stack — at least 200px wide, fully inside the field and at least 24px from the viewport edge. More, smaller, or faded satellites read as "animation leftovers" (three judged runs, 2026-10-14); a name cut by the viewport ("riya Raman") reads as a bug. This is product-visuals.md §1 Placement's "surrounds the headline" (7) pattern adapted to a field below the headline.
3. **One focal fragment** in the middle, sharp and fully legible: Recipe 3 (Isolated hero component) or Recipe 2 (Layered cards) from `shared/product-visuals.md`, at Recipe 3's 1–1.5× scale. All other fragments are **satellites**: small real-content cards (a status pill row, a KPI, an avatar stack, a log line, a search bar) — and any satellite that is only schematic must sit at `opacity: 0.3` or less (product-visuals.md §1 rule 1: "one sharp tile among faded ones", (7), (35)).
4. **Framing**: every fragment uses §8 Synthetic Product Visual tokens — panels `var(--bg)` with `1px solid var(--surface-2)` border on the `var(--surface-1)` field (Surface nesting rule), radius 16px for the focal frame (content card) and 8px for satellites (feature card). No box-shadow anywhere (§5). Overlap is the only depth (flim: "film stills overlap at varied z-positions without drop shadows").
5. **The search-bar satellite** (optional, for products with search or a command palette): the 160px pill radius from §4 — flim's own hero has exactly this pill crossing the field.

**Background**: `var(--bg)` top band; `var(--surface-1)` field with the hairline grid. No gradient fills, no glow, no noise. The grid uses `linear-gradient` only to draw 1px lines in `var(--surface-2)` — it is a ruled line, not a color gradient (§1 forbids gradient fills, not rules).

**Scale**: the heading uses the §2 hero size `clamp(48px, 7vw, 80px)`. The field is the visual weight of the fold — the focal fragment's top edge sits at 55–70% of a 1440 × 900 screen, so a full card header and its first rows are visible without scrolling. That is why the top band and the field's top use the 58px step, not 128px.

**Entrance motion**: satellites stagger in (card distance 24px, 100ms stagger, 0.8s `cubic-bezier(0.16, 1, 0.3, 1)` — interaction-patterns §1). The focal fragment runs **one** §1.5 recipe instead of fading (Rows stream in, Cursor click, or Typing caret, per the product).

```html
<section data-section="hero" data-layout="split-left" data-bg="base" data-bold="true" class="hero-specimen">
  <div class="container hero-specimen-top">
    <h1 class="hero-specimen-title">Every incident, one timeline.</h1>
    <div class="hero-specimen-aside">
      <p class="hero-specimen-sub">Halberd Signal merges alerts, deploys, and chat into one ordered record your on-call can read in ten seconds.</p>
      <div class="hero-specimen-ctas">
        <a href="#" class="btn-dark btn-lg">Start free</a>
        <a href="#" class="btn-outline btn-lg">Read the docs</a>
      </div>
    </div>
  </div>

  <div class="specimen-field">
    <!-- Satellites: real content, small, scattered. Positions are % of the field. -->
    <div class="pv specimen-sat" data-mock role="img" aria-label="Deploy status card" style="left:3%; top:24%; width:16%">
      <div class="pv-panel specimen-sat-card">
        <div class="pv-label">Deploy · api-gateway</div>
        <div class="pv-kpi">v2.41.3</div>
        <span class="pv-pill">Rolled back</span> <span class="pv-muted pv-mono">4m ago</span>
      </div>
    </div>
    <div class="pv specimen-sat" data-mock role="img" aria-label="On-call responders" style="right:3%; top:46%; width:16%">
      <div class="pv-panel specimen-sat-card">
        <div class="pv-label">On call</div>
        <div><span class="pv-avatar">PR</span> <span class="pv-avatar">JK</span> <span class="pv-avatar">MO</span></div>
      </div>
    </div>

    <!-- Focal fragment: Recipe 3 (isolated component), sharp, centered -->
    <div class="pv pv-iso specimen-focal" data-mock role="img" aria-label="Incident INC-2709 timeline in Halberd Signal">
      <div class="pv-panel pv-iso-card">
        <div class="pv-label">INC-2709 · Checkout latency</div>
        <div class="pv-iso-title">p95 latency above 1.2s on /checkout</div>
        <div class="pv-row" data-stream><span class="pv-mono pv-muted">14:02</span> Alert fired — Datadog monitor 4471</div>
        <div class="pv-row" data-stream><span class="pv-mono pv-muted">14:03</span> Priya Raman acknowledged</div>
        <div class="pv-row" data-stream><span class="pv-mono pv-muted">14:04</span> Deploy v2.41.3 linked as likely cause</div>
        <div class="pv-row is-focused" data-stream><span class="pv-mono pv-muted">14:06</span> Rollback of api-gateway v2.41.3 started</div>
        <div class="pv-row" data-stream><span class="pv-mono pv-muted">14:11</span> p95 back to 380 ms — monitoring</div>
        <div class="pv-iso-chips"><span class="pv-pill is-strong">Critical</span><span class="pv-pill">Payments</span><span class="pv-pill is-quiet">Cycle 41</span></div>
      </div>
    </div>
  </div>
</section>
```

```css
/* Requires: §2 font variables, §8 buttons, product-visuals.md §3 base CSS + Recipe 3 CSS */
.hero-specimen { padding-top: 128px; padding-bottom: 0; }            /* §3 hero top; field closes the section */
.hero-specimen-top {
    display: grid;
    grid-template-columns: minmax(0, 7fr) minmax(0, 5fr);            /* heading gets the wider column: ≤ 3 lines */
    gap: 58px;                                                        /* §7 alternating rows gap */
    align-items: start;
    padding-bottom: 58px;                                             /* §3 heading to content: keeps the field in the fold */
}
.hero-specimen-title {
    font-family: var(--font-display);
    font-size: clamp(48px, 7vw, 80px);                                /* §2 hero */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.05;
    margin: 0;
}
.hero-specimen-sub {
    font-size: 18px; line-height: 1.6;                                /* §2 body text */
    opacity: 0.5;                                                     /* §1 subtitle */
    max-width: 540px;                                                 /* §7 subtitle measure */
    margin: 0;
}
.hero-specimen-ctas { display: flex; gap: 12px; margin-top: 48px; }   /* §3 subheading to CTA */

.specimen-field {
    position: relative;
    padding: 58px 32px 128px;                                         /* §3: 58 top keeps the focal card in the fold; 128 bottom */
    background-color: var(--surface-1);
    background-image:
        linear-gradient(var(--surface-2) 1px, transparent 1px),
        linear-gradient(90deg, var(--surface-2) 1px, transparent 1px);
    background-size: 32px 32px;   /* cell ≈ 32px measured in flim.ai-viewport.jpeg; = §3 spacing step 32 */
    overflow: hidden;             /* edge satellites bleed off the viewport */
}
.specimen-sat { position: absolute; z-index: 1; }
.specimen-sat { min-width: 200px; --pv-text: 14px; }
.specimen-sat-card { padding: 16px; display: grid; gap: 8px; justify-items: start; }  /* §3 spacing step; pills keep their width */
.specimen-focal { position: relative; z-index: 2; width: 60%; margin: 0 auto; }  /* the middle band; satellites sit beside it */
.specimen-focal > .pv-panel { border-radius: 16px; }                  /* §4 content card */
.specimen-focal .pv-row { grid-template-columns: 48px 1fr; }

.hl { background: var(--surface-1); color: inherit; border-radius: 0; padding: 0 0.06em; box-decoration-break: clone; } /* flim "Art directors." block; M2 */

@media (prefers-reduced-motion: no-preference) {
    .specimen-sat {
        animation: specimen-in 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;   /* interaction-patterns §1 */
    }
    .specimen-sat:nth-of-type(2) { animation-delay: 100ms; }               /* §1 card stagger */
    @keyframes specimen-in { from { opacity: 0; transform: translateY(24px); } } /* §1 card distance */
}

@media (max-width: 767px) {
    .hero-specimen { padding-top: 80px; }                             /* §3 narrow table */
    .hero-specimen-top { grid-template-columns: 1fr; gap: 24px; padding-bottom: 40px; }
    .specimen-field { padding: 40px 20px 80px; }                      /* §3 narrow: 58 → 40, 128 → 80 */
    .specimen-sat { display: none; }                                  /* keep only the focal fragment */
    .specimen-focal { width: 100%; }
}
```

The focal fragment's rows use §1.5 A "Rows stream in" (`data-stream` already in the markup). Swap the content for the user's product per product-visuals.md §6; keep ≥ 3 proper nouns, one status set, one relative time, one focused row.

**Dark theme**: tokens swap automatically — field `#141414` (`--surface-1`), grid lines and frame borders `#1F1F1F` (`--surface-2`), panels `#0A0A0A` (`--bg`). This is Linear's depth model ("depth through 1px inset border, not drop shadow", `linear.md` Principle 3). Do **not** add a glow behind the focal fragment (product-visuals.md §2 "Minimal on dark"), and do not apply `.section-dark` to the field. `.hl` on dark uses `var(--surface-1)` too.

### 12.3 Signature details

**1. Hairline grid field.** Used once per page (the hero field, or one emphasis section if the hero is a different move). Never on `var(--bg)` sections — the grid belongs to the `surface-1` "workbench". CSS: `.specimen-field` above.

**2. Mono index numbers on a 1px rule.** Repeated items (features, steps, FAQ groups) are numbered `01 / 02 / 03` in the label role and sit on a full-width 1px rule — the specimen-sheet look of flim's footer columns (`flim.ai-footer.jpeg`: mono uppercase column labels over display-type lists).
```css
.index-row { border-top: 1px solid var(--surface-2); padding-top: 24px; display: grid; grid-template-columns: 58px 1fr; gap: 24px; }
.index-num { font-family: var(--font-mono); font-size: 12px; font-weight: 400; letter-spacing: 0.72px; opacity: 0.4; }
```

**3. Two-voice type contrast.** Only display sizes and the 12px mono label are allowed to sit next to each other in a heading block; avoid mid-size intermediaries (no 20px kicker over a 47px heading). flim's 13-step scale is held together by locked weight 500 (Typography as Architecture). The label above a section heading is the `.label` from §8; the heading uses the §2 section scale.

**4. Block highlight on one phrase** — *off by default*. In two judged runs the grey block read as a stray text selection, so use it only when the user asks for an accent, or for a one-word phrase that is clearly a label. One phrase per page (hero only) gets a flat `var(--surface-1)` block with no radius — flim's "Art directors." (`flim.ai-viewport.jpeg`). CSS: `.hl` above. Never a colored highlight, never more than one phrase, and only on one or two words that stay on one line: a block that wraps across lines reads as a stray text selection.

**5. Cropped giant wordmark** — *only for a short-named consumer or creative brand* (signature-moves §5 Step 5; on SaaS pages judges read it as oversized and disconnected). The footer ends with the product name at full width, cropped by the bottom of the page — flim's footer (`flim.ai-footer.jpeg`). Use signature-moves.md M14 CSS verbatim with `color: var(--text)`; on dark, the same token flips it to `#EDEDED`.

### 12.4 Motion personality

Minimal motion is **mechanical and brief**: things arrive and stop; nothing floats, pulses, or loops.

- **Product-serving motions that fit** (interaction-patterns §1.5): A Rows stream in (logs, incidents, inboxes — the default), B Cursor click (one primary action), C Typing caret (search, AI, command palette), E Number ticks (one KPI). Avoid D Toast in the hero — a toast adds a floating layer the field already provides.
- **Timing**: entrance 0.8s `cubic-bezier(0.16, 1, 0.3, 1)` (§6 scroll entrance = interaction-patterns §1); stagger 100ms cards / 80ms small items.
- **Hover**: buttons `transform 0.2s ease-in-out` → `translateY(-1px)`; cards `translateY(-4px)` + `border-color 0.3s`; links and nav `opacity 0.3s linear` (§6, §8 Text Links 0.7, nav 0.5 → 1). Hover never changes color hue or adds a shadow.
- **Never moves**: headings, the hairline grid, the giant wordmark, logo walls (no marquee in Minimal — static `.logo-wall` row), satellites after their entrance (no float, no parallax), and anything on hover beyond the lifts above. No bounce or spring (§6).

### 12.5 Preferred signature moves

Which layout each section uses by default is set in the master `SKILL.md` Step 4.3 *Style layout defaults* table; the notes below adjust how each move looks in this style.

- **M14 Giant wordmark footer** — the most flim-specific move, for consumer and creative brands only. Adjustment: weight 500, `var(--text)`, sits after the copyright line exactly as in `flim.ai-footer.jpeg`; still skip it for names > 8 characters.
- **M1 Edge-to-edge headline** — alternative hero for brand moments, About manifestos, and 404 C; flim's hero wordmark at 125.2px is the precedent. Adjustment: weight 500 only, `var(--text)`, no field below — pair with one mono label line.
- **M7 Big-type list band** — on `.section-dark` (light theme only). Adjustment: list items in display 500, row rules from the M7 recipe; numbering with detail 2's `.index-num`.
- **M5 Bento with a lead tile** — the default features layout; tiles `var(--surface-1)` 8px, zero shadow, fragments on `var(--bg)` panels.

M3 (Product rising from the fold) remains valid when the product is one dense screen, but the Specimen Field is the default.

### 12.6 Drift guard

Forbidden in Minimal because it reads as another style:
- **Business**: any `box-shadow` (even soft blue-gray), rounded 8px buttons, warm off-white `#FCFBF8` or any tinted neutral, 120px section rhythm, brand-gradient stage panels.
- **Colorful**: pill buttons (the 160px pill is for search bars only), pastel scene backgrounds, serif display type, layered paper shadows, illustrated decoration.
- **Editorial**: serif display (Cormorant or any serif), warm canvas `#FAF8F5`, teal or any hard-coded accent, dark stage panel `#161616` at 30px radius.
- **Generic AI**: centered hero with a gradient blob or glow, perspective grid, icons in colored circles, three equal feature cards repeated, bold (700) headings for emphasis, gray-text-by-hex instead of opacity, left-border accent stripes, `--accent` used for badges or section fills (§1 whitelist).

### 12.7 Screenshot test

1. **Two voices only**: the screenshot shows huge 500-weight display type and tiny uppercase mono labels, with no bold weight and no serif anywhere.
2. **The grid is visible and the product hangs on it**: the hero has a ruled `surface-1` field with one sharp, legible product fragment and two small full-contrast satellites beside it, casting no shadow.
3. **Grayscale survives**: convert the screenshot to grayscale and nothing changes except inside `data-mock` status pills/charts and (if given) the brand CTA; the page shell has zero hue.
