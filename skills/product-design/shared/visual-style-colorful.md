# Visual Style Guide — Colorful Preset

> DNA: Craft (Light + derived Dark)
> Tone: Editorial warmth, creative tools, consumer SaaS. Color creates rooms, not controls.

> **Must use — at the end of this file, §10 Style Signature.** Read this file to the last line. Every page in this style needs:
> 1. When the page has a hero (not 404, not a single non-hero section): the hero built from the "Hero showcase", starting from its HTML example and keeping the `.hero-scene` class (the self-check looks for it)
> 2. At least two items from Signature details
> 3. Motion personality and Drift guard, followed as written
> 4. Screenshot test, run against the finished page before delivery

This file is a self-contained style preset. When this preset is active, follow ALL tokens from this file. Do not mix with `shared/visual-style.md` (Minimal preset) values.

---

## Design Philosophy

Four core principles:

1. **Color lives in rooms, not on controls** — Brand colors (blues, greens, lavenders, peaches) are used as full-bleed scene backgrounds for individual sections. Primary actions stay black/white. A visitor feels the story has moved into a new chapter without learning a new action language.
2. **Paper weight over glass effects** — Cards feel like physical documents: warm off-white sheets, a four-layer black shadow, and `24px` rounded outer corners with `12–16px` inner windows. Content has weight and edge.
3. **Serif for the narrative, sans for the work** — Playfair Display carries claims and headlines. DM Sans handles explanation, controls, and UI. The voice shifts between editorial (serif) and operational (sans) as the page moves from selling to explaining.
4. **Scrolling as punctuation** — 120px is standard rhythm. Intentional expansions to 168–336px mark scene transitions. Empty space is not wasted; it is the pause between chapters.

---

## 1. Color System

### Light Theme (Craft DNA)

```
--bg:           #FCF9F7        Page canvas — warm off-white (vs pure white)
--surface-1:    #F5F5F7        Secondary panels, cool neutral surface
--surface-2:    #E4E4E8        Borders, dividers, compact UI rings
--text:         #030302        All text — near-black, warm (hierarchy via opacity)
--text-inverse: #FFFFFF        Text on dark or scene-colored surfaces
--accent:       #030302        CTA button background (default = --text; brand color overrides)
--accent-text:  #FFFFFF        CTA button text
```

**Text hierarchy via opacity (base color #030302)**:
```
Primary text:         opacity: 1
Subtitle/description: opacity: 0.75    (slightly less reduced — warm backgrounds need less contrast)
Auxiliary/label:      opacity: 0.5
Weakest (copyright):  opacity: 0.35
Logo wall:            opacity: 0.5
```

### Scene Colors (Light Theme)

Large section backgrounds (one per content chapter). Use **2–3 distinct scene colors per page, at least one of them warm** (`--scene-peach` or `--scene-yellow`), one per content chapter; the hero sky counts as the blue. Craft never runs a page on cool colors alone: its hero carries a yellow lined notebook and its product cards are pink, yellow, green, and blue (craft.do, Mobbin 2026-10-14). Never apply scene colors to buttons, icons, badges, or borders.

```
--scene-blue:     #B8CAF5    Periwinkle — Write/hero scenes, feature emphasis
--scene-green:    #9BD8A9    Sage green — brand/values scenes, social proof
--scene-lavender: #D5ACD8    Lavender — pricing tier segmentation, personality
--scene-peach:    #F6CB98    Warm peach — CTA warmth, conversion sections
--scene-yellow:   #FFE48D    Notebook yellow — sampled from the lined notebook in the craft.do hero; social proof, steps, a warm chapter
```

### Content Tints (inside product mocks only)

Craft's own UI is colorful: in its "All Docs" view every document card has its own pale tint and a matching rule. Inside a `data-mock`, content items (document cards, notes, tags, calendar blocks) may each carry one of these — sampled from the craft.do hero (Mobbin, 2026-10-14). Use 3–5 different tints in a mock; the mock's chrome (sidebar, toolbar) stays `var(--bg)`.

```css
[data-mock] {
  --tint-pink:   #FFE1F7;
  --tint-yellow: #FFFFD9;
  --tint-green:  #CAEBD2;
  --tint-blue:   #DDFCFF;
  --tint-peach:  #FDF4E4;
}
.pv-doc { background: var(--bg); border: 2px solid var(--tint-pink); border-radius: 12px; }   /* or fill the card with the tint */
```
Dark theme: use each tint at 18% over `var(--surface-1)` (`color-mix(in srgb, var(--tint-pink) 18%, var(--surface-1))`).

### Dark Theme (derived from Craft system)

```
--bg:           #0E0D0B        Page canvas — warm near-black
--surface-1:    #1C1B18        Cards, panels — warm dark gray
--surface-2:    #2A2924        Borders, dividers — warm charcoal
--text:         #F0EDE8        All text — warm off-white (hierarchy via opacity)
--text-inverse: #0E0D0B        Text on light or scene-colored surfaces
--accent:       #F0EDE8        CTA button background (default = --text)
--accent-text:  #0E0D0B        CTA button text
```

**Text hierarchy via opacity (base color #F0EDE8)**:
```
Primary text:         opacity: 1
Subtitle/description: opacity: 0.75
Auxiliary/label:      opacity: 0.5
Weakest (copyright):  opacity: 0.35
Logo wall:            opacity: 0.5
```

### Scene Colors (Dark Theme)

Same hue family as light, shifted to darker, richer values. Used as section backgrounds.

```
--scene-blue:     #1E3258    Deep navy — blue scenes in dark mode
--scene-green:    #1A3D22    Deep forest — green scenes in dark mode
--scene-lavender: #3D2045    Deep plum — lavender scenes in dark mode
--scene-peach:    #4A2E18    Deep amber — peach/warm scenes in dark mode
--scene-yellow:   #46391A    Deep ochre — yellow scenes in dark mode (the light yellow shifted to the same depth as the other dark scenes)
```

### Accent Color Rules

- Default accent is `var(--text)` (near-black or near-white). Brand color overrides only `--accent` and `--accent-text`.
- Scene colors (`--scene-*`) are NOT accent colors. They are background fills for section elements only.
- **CTA buttons, nav links, and all controls stay black/white** — scene colors never touch interactive controls.
- Chromatic color (scene backgrounds) may occupy up to 40% of total page area across 2–3 scenes. This is higher than Minimal's <10% rule because scenes are large page-level areas, not accent details.
- Within a scene, all text, buttons, and icons remain black/white (never colored to match the scene tint).

**Absolutely Forbidden**:
- Scene color used as button background or hover state
- Multiple scene colors per section
- Scene colors on nav or footer
- Icon backgrounds in scene colors
- Gradient scenes (flat scene color only — no gradients)

---

## 2. Typography System

### Font Families

| Role | Font | Usage |
|------|------|-------|
| Display (editorial) | `'Playfair Display', Georgia, serif` | All headings, hero claims, section titles |
| Body (operational) | `'DM Sans', -apple-system, sans-serif` | Body paragraphs, navigation, buttons, UI |
| Mono (structural) | `'JetBrains Mono', 'SF Mono', Consolas, monospace` | Labels (UPPERCASE), metadata, code |

```css
:root {
    --font-display: 'Playfair Display', Georgia, serif;
    --font-mono:    'JetBrains Mono', 'SF Mono', Consolas, monospace;
    --font-body:    'DM Sans', -apple-system, sans-serif;
}
```

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=DM+Sans:wght@400;500&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
```

**Critical**: `--font-display` is a serif font (Playfair Display) in Colorful, whereas Minimal uses a sans. The role of DM Sans shifts to `--font-body`. Do not confuse the role assignments.

### Type Scale

```
Hero heading:     clamp(52px, 6vw, 66px)    weight: 400   tracking: -0.02em   line-height: 1.0
Section heading:  clamp(36px, 4vw, 54px)    weight: 400   tracking: -0.02em   line-height: 1.05
Feature heading:  46px                       weight: 400   tracking: -0.02em   line-height: 1.15
Supporting head:  32px                       weight: 400   tracking: -0.02em   line-height: 1.2
Card heading:     20px (--font-body)         weight: 500   tracking: normal    line-height: 1.3
Body text:        18px (--font-body)         weight: 400   tracking: normal    line-height: 1.6
Body secondary:   16px (--font-body)         weight: 400   tracking: normal    line-height: 1.6
Button:           16px (--font-body)         weight: 500   tracking: -0.02em
Navigation:       16px (--font-body)         weight: 400   tracking: -0.02em
Label:            12px (--font-mono)         weight: 400   tracking: +0.72px   text-transform: uppercase
```

**Key rules**:
1. **All headings use Playfair Display at weight 400** — the serif letterform carries authority without bold weight
2. **Card headings and all UI elements use DM Sans** (the body/operational font)
3. Serif at weight 400 reads heavier than sans at 400 at the same size — do not over-bold
4. Negative tracking at `-0.02em` applies consistently across all serif heading sizes
5. Labels always: 12px / mono / 400 / uppercase / +0.72px tracking / opacity 0.5

---

## 3. Spacing System

### Base Unit: 4px (Craft DNA)

```
Spacing scale: 4 · 8 · 12 · 16 · 24 · 32 · 48 · 60 · 120 · 168 px
```

### Specific Applications

```
Section padding (standard):                120px (repeated across all pages)
Dramatic scene transition (optional):      168–336px (for major chapter breaks)
Section internal (heading to content):     48px
Hero top whitespace:                       120px
Hero heading to subheading:                24px
Subheading to CTA:                         48px
Card internal padding:                     32px
Card gap:                                  24px
Grid gutter:                               24px
Footer top padding:                        120px
```

**Scene transition rule**: When a colored scene section is followed by a differently colored scene or the default canvas, expand the section's bottom padding to 168px (or 336px for major story breaks). This pause is the punctuation.

### Narrow Screen Spacing (< 768px)

```
Desktop 120px (section rhythm)  →  64px
Desktop 168px (dramatic pause)  →  96px
Desktop 120px (hero top)        →  72px
Desktop 48px (heading-to-content) →  32px
Desktop 32px (card padding)     →  24px
Desktop 24px (gap)              →  keep unchanged
Left/right padding 32px         →  20px
```

---

## 4. Border Radius System

```
Scene frame:     24px   (hero canvas, large cards, gallery modules — the primary card radius)
Inner panel:     16px   (nested product UI panels, medium cards)
Compact panel:   12px   (tightly nested windows, preview elements)
Control:         8px    (toggles, inputs, chips)
Small control:   4px    (small badges, compact tags)
Pill action:     9999px (all buttons — primary CTA, secondary)
```

**Nested radius rule**: `24px` scene frame → `16px` inner window → `8px` control → pill for the primary action. Each nesting level steps one radius size smaller.

**Note**: Pill buttons are a key aesthetic signal of Colorful — do not use 2px buttons from Minimal.

---

## 5. Shadow System

**Cards and document-like objects use a four-layer paper shadow. Page shell (footer, full-width bars) uses no shadow. The one exception is the floating pill nav, which carries its own light shadow (§8 Navigation).**

This shadow is the metaphor for "paper weight" — each document card appears to have physical presence and an edge.

### Card Shadow (both themes)

```css
.card {
    box-shadow:
        0 50px 40px rgba(0, 0, 0, 0.01),
        0 50px 40px rgba(0, 0, 0, 0.02),
        0 20px 40px rgba(0, 0, 0, 0.05),
        0 3px 10px  rgba(0, 0, 0, 0.08);
}
```

The visible edge comes from the tightest layer (`0 3px 10px 0.08`). The wide layers add ambient depth. Neutral black (no color tint) — the scene's hue carries the mood, not the shadow.

### Dark Theme Card Shadow (heavier)

```css
[data-theme="dark"] .card {
    box-shadow:
        0 50px 40px rgba(0, 0, 0, 0.10),
        0 50px 40px rgba(0, 0, 0, 0.15),
        0 20px 40px rgba(0, 0, 0, 0.20),
        0 3px 10px  rgba(0, 0, 0, 0.30);
}
```

### Inner UI Shadow

For elements inside card interiors (nested UI panels, inner segments):
```css
.card-inner {
    box-shadow: inset 0 0 0 1px rgba(0, 0, 0, 0.10);
}
```

---

## 6. Transitions & Motion

```
hover transform:   transform 0.2s ease-in-out (button micro-lift translateY(-1px))
card hover:        transform 0.2s ease-in-out (card lift translateY(-4px); shadow deepens)
color/opacity:     opacity 0.3s linear or color 0.3s linear
scroll entrance:   opacity + transform 0.8s cubic-bezier(0.16, 1, 0.3, 1)
```

→ Full pattern recipes and JS implementations: see `shared/interaction-patterns.md`

---

## 7. Grid System

```
Main grid:        max-width 920px, centered, padding 0 32px
Wide media:       max-width 1172px (hero scenes, product demos — allowed to escape core grid)
Subtitle measure: max-width 540px
3-col gallery:    3 × columns / 24px gap
6-col layout:     6 × 160px / 40px gutter (for feature sections; totals 1160px, so it uses the wide media width, not the 920px core grid)
```

**Note**: The `920px` core content width (from Craft) is narrower than Minimal's `1080px`. This creates a centered, editorial feel with wider margins.

---

## 8. Component Tokens

### Buttons

```css
.btn-dark {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 14px 28px;           /* Generous padding for pill shape */
    font-size: 16px;
    font-weight: 500;
    font-family: var(--font-body); /* Pill buttons use DM Sans (operational font), not serif */
    line-height: 24px;
    background: var(--accent);
    color: var(--accent-text);
    border: none;
    border-radius: 9999px;        /* Full pill — Colorful signature */
    cursor: pointer;
    text-decoration: none;
    transition: transform 0.2s ease-in-out;
}
.btn-dark:hover { transform: translateY(-1px); }

.btn-outline {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 14px 28px;
    font-size: 16px;
    font-weight: 500;
    font-family: var(--font-body);
    line-height: 24px;
    background: transparent;
    color: var(--text);
    border: 1px solid rgba(3, 3, 2, 0.2);
    border-radius: 9999px;
    cursor: pointer;
    text-decoration: none;
    transition: border-color 0.3s linear;
}
.btn-outline:hover { border-color: var(--text); }
[data-theme="dark"] .btn-outline {
    border-color: rgba(240, 237, 232, 0.2);
}

:focus-visible {
    outline: 2px solid var(--text);
    outline-offset: 3px;
}
```

### Navigation (Floating Pill — Craft pattern)

```css
:root { --nav-h: 94px; }  /* rendered height: 12 + 1 + 8 + 52 (pill CTA) + 8 + 1 + 12 */
body { padding-top: var(--nav-h); }

nav {
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 100;
    padding: 12px 0;
    /* Craft floating pill nav style: centered container with pill background */
}
nav > .container {
    max-width: 920px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(252, 249, 247, 0.92);
    border-radius: 9999px;
    border: 1px solid var(--surface-2);
    padding: 8px 8px 8px 24px;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: 0 2px 8px rgba(0,0,0,0.06), 0 8px 24px rgba(0,0,0,0.04);
}
[data-theme="dark"] nav > .container {
    background: rgba(14, 13, 11, 0.92);
    border-color: var(--surface-2);
}
nav a {
    font-family: var(--font-body);
    font-size: 16px;
    font-weight: 400;
    color: var(--text);
    opacity: 0.75;
    text-decoration: none;
    transition: opacity 0.3s linear;
    letter-spacing: -0.02em;
}
nav a:hover { opacity: 1; }

/* Nav CTA: override the link rule for BOTH opacity and color (specificity trap) */
nav a.btn-dark { opacity: 1; color: var(--accent-text); }
nav a.btn-outline { opacity: 1; color: var(--text); }
```

**Mobile menu**: `backdrop-filter` on the pill makes it the containing block for any `position: fixed` descendant, so a fixed mobile menu placed inside the pill is positioned against the pill, not the viewport. Render the mobile menu panel as a sibling of `nav`, not a child.

### Label

```css
.label {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.5;
}
```

### Scene Section

A large colored background section. Choose one `--scene-*` color per section.

```css
.scene {
    background: var(--scene-blue);   /* or --scene-green, --scene-lavender, --scene-peach */
    border-radius: 24px;             /* scene frame radius — the defining visual element */
    padding: 80px 60px;              /* generous internal padding */
    margin: 0 20px;                  /* 20px canvas inset from viewport edge (Craft pattern) */
}

/* On narrow screens: full-bleed */
@media (max-width: 767px) {
    .scene {
        border-radius: 16px;
        margin: 0 12px;
        padding: 60px 32px;
    }
}
```

**Default scene sequence** (pick 3 distinct colors at most, one warm): hero sky (`--scene-blue`) → first feature chapter in `--scene-green` → steps or social proof in `--scene-yellow` → closing CTA in `--scene-yellow` again or on the canvas. Swap yellow for peach when the product is about money, commerce, or food. Never two adjacent scenes in the same color; keep at least one canvas (`var(--bg)`) section between scenes.

All text inside `.scene` uses `var(--text)` color — scene backgrounds are light pastels in light mode, so black text has full contrast. In dark mode, scene backgrounds are dark, so use `var(--text)` (warm off-white) which also contrasts correctly.

### Card

```css
.card {
    padding: 32px;
    background: var(--bg);           /* white/off-black card inside scene */
    border-radius: 24px;             /* scene card radius */
    box-shadow:
        0 50px 40px rgba(0,0,0,.01),
        0 50px 40px rgba(0,0,0,.02),
        0 20px 40px rgba(0,0,0,.05),
        0 3px 10px rgba(0,0,0,.08);
}

/* Feature card (smaller, inside grid) */
.card-feature {
    padding: 24px;
    background: var(--bg);
    border-radius: 16px;
    box-shadow: 0 3px 10px rgba(0,0,0,.08);
}
```

On the default page canvas (outside a `.scene`), a card on `var(--bg)` has no visible edge in dark mode — black shadows vanish on a near-black canvas. Step it up one surface:

```css
.card, .card-feature { background: var(--surface-1); }
.scene .card, .scene .card-feature { background: var(--bg); }
```

**Surface nesting rule**:
- On the default canvas → card uses `var(--surface-1)`
- Inside a `.scene` → card uses `var(--bg)` (white/off-black)
- Inside `.card` (24px, scene-level) → nested element uses `var(--surface-1)` (cool neutral step)
- Inside `var(--surface-1)` → nested screenshot uses `var(--bg)`

---

## 9. Brand Customization

### Brand Color Override

When the user provides a brand color:
1. Set `--accent` to that color; calculate `--accent-text`
2. Pill buttons use the brand color as background — the pill shape carries the brand character
3. The brand color should NOT replace scene colors — scenes stay in the `--scene-*` palette
4. If the brand color is in the same family as one of the scene colors (e.g., brand is deep blue → `--scene-blue`), it can be used as that scene's background, replacing the default pastel
5. Chromatic area: the brand color on pill buttons is small; scene areas add up to ~30% — still acceptable when scenes use pastels

### Scene Color Replacement

When the user provides 1–4 brand-aligned palette colors:
- Replace the corresponding `--scene-*` variables with the provided values
- Keep the warm neutral base (#FCF9F7 / #F5F5F7) unchanged
- Scene replacement is the only permitted way to introduce additional brand colors

---

## 10. Style Signature

### Character

Colorful feels like walking through a well-made picture book about software: a warm paper canvas (`#FCF9F7`), one pastel room at a time, a serif sentence that makes a claim, and below it a physical sheet of product that casts a real shadow. The DNA's taste decisions explain each part: Craft chooses 54–66px serif headlines and confines sans UI to product demonstrations (voice shift from story to work); it puts blue, green, lavender, and peach on page-sized scenes while every action stays black/white ("color creates rooms, not controls"); it spends 120px rhythm with expansions to 168–444px so each scene can register; and it chooses opaque warm sheets with a four-layer shadow over glass or border-only boxes (the same shadow on 72 sampled elements). The result is warmth with authority — never playful clutter.

### Hero showcase (mandatory)

**Composition — "Scene with paper on the table."** Signature move M4 (Framed hero stage), Colorful row: the whole hero is one `.scene` panel, inset `20px` from the viewport (`margin: 0 20px`, DNA "Viewport canvas inset 20px"), `24px` radius. The hero scene is a **sky** (`shared/atmosphere.md` Recipe 2): a vertical gradient from `--scene-blue` `#B8CAF5` (the DNA "Sky / periwinkle field", `craft.do.md` line 63) lightening toward the horizon where the product sits, a fine grain overlay, 2–3 soft **halftone-dot clouds** bleeding off the left/right edges (Recipe 3a; Paper Shaders 3b optional). **One paper cutout: Craft's yellow lined notebook** (`atmosphere.md` Recipe 4 `.cut-notebook`, in `--scene-yellow` `#FFE48D`), tucked behind the product window's lower right corner and peeking ≤ 80px past it — the warm counterweight to the blue sky, exactly as in the craft.do hero. No other cutouts: the zigzag, ink scrap, blob, and torn sheet read as stray artifacts in judged runs (2026-10-14). Under 768px keep one cloud. Inside: centered mono label, Playfair hero claim, 75%-opacity subtitle at the 540px measure, a black pill CTA — the text occupies the middle third of the frame (DNA Layout: "hero text occupies roughly the middle third"). Below it, product-visuals **Recipe 2 (Layered cards over a backing panel)** staged as paper: a warm-white main document sheet (`var(--bg)`, `16px` inner radius, four-layer card shadow) rising from the scene's bottom edge and cut by it, plus one smaller floating sheet laid on the main sheet's right edge (Recipe 2: it overlaps only the 32px edge track, never the rows) that carries the focused state. The scene itself is the `--pv-mat` (product-visuals §2: Colorful mat = one `--scene-*`), so the hero uses 1 of the page's 2–3 scene colors.

**Background**: page shell `var(--bg)` flat; all color and texture live inside the hero sky. The sky gradient and clouds are hero-only — later scenes stay one flat `--scene-*` color. Cutouts and clouds stay out of the centered text column; nothing moves.

**Entrance**: the text block uses interaction-patterns §2 scroll entrance tokens (0.8s `cubic-bezier(0.16, 1, 0.3, 1)`, 32px). The mock uses §1.5 **D. Toast slides in** on the floating sheet (300ms after load, hero trigger) — the main sheet is static, the floating paper arrives. One motion cue only.

```html
<section data-section="hero" data-layout="full-bleed" data-bg="scene" class="hero-scene-wrap">
  <div class="scene hero-scene">
    <div class="hero-scene-copy">
      <p class="label">For writing teams</p>
      <h1 class="hero-title">Docs that read like they were made by hand</h1>
      <p class="hero-sub">Quill gives small writing teams one place to draft, review and publish, with comments that read like margin notes.</p>
      <div class="hero-actions">
        <a href="#" class="btn-dark">Start writing</a>
        <a href="#" class="btn-outline">See a sample</a>
      </div>
    </div>

    <div class="cut cut-notebook" aria-hidden="true"></div>
    <div class="pv pv-layers hero-paper" data-mock role="img" aria-label="Project brief document with a comment card from a teammate">
      <div class="pv-mat">
        <div class="pv-panel pv-layer-main card-paper">
          <div class="paper-head">
            <span class="pv-label">Brief · Q3 launch</span>
            <span class="pv-pill">Draft</span>
          </div>
          <div class="paper-body">
            <p class="pv-kpi">Launch plan</p>
            <div class="pv-row" style="grid-template-columns: 1fr auto;"><span>Positioning statement</span><span class="pv-mono pv-muted">Mon</span></div>
            <div class="pv-row is-focused" style="grid-template-columns: 1fr auto;"><span>Pricing page copy</span><span class="pv-pill is-strong">In review</span></div>
            <div class="pv-row" style="grid-template-columns: 1fr auto;"><span>Launch email</span><span class="pv-mono pv-muted">Thu</span></div>
            <div class="pv-row" style="grid-template-columns: 1fr auto;"><span>Press list</span><span class="pv-pill is-quiet">Todo</span></div>
          </div>
        </div>
        <div class="pv-panel pv-layer-float pv-toast card-paper is-warm">
          <p class="pv-label">Comment · Pricing page copy</p>
          <p>"Tighten the second line, then ship."</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

```css
/* product-visuals §2 binding, Colorful column */
.pv {
    --pv-mat: transparent;          /* the hero .scene IS the mat (one --scene-*) */
    --pv-r-outer: 24px;             /* §4 Scene frame */
    --pv-r-inner: 16px;             /* §4 Inner panel */
    --pv-r-control: 8px;            /* §4 Control */
}
.pv-kpi { font-family: var(--font-body); font-size: 20px; font-weight: 500; }  /* §2 card heading */

.hero-scene-wrap { padding-top: 0; }                 /* body already offsets --nav-h */
.hero-scene {
    position: relative; isolation: isolate;
    background: linear-gradient(180deg,               /* atmosphere.md Recipe 2: sky from --scene-blue */
        color-mix(in srgb, #B8CAF5 88%, #4890E3) 0%,
        #B8CAF5 38%,
        color-mix(in srgb, #B8CAF5 45%, #FCF9F7) 78%,
        color-mix(in srgb, #B8CAF5 25%, #FCF9F7) 100%);   /* still 1 of max 2 scene colors */
    padding: 120px 60px 0;                            /* §3 hero top whitespace; mock flush to bottom (M4) */
    overflow: hidden;
    text-align: center;
}
.hero-scene-copy { max-width: 920px; margin: 0 auto; }      /* §7 main grid */
.hero-title {
    font-family: var(--font-display);
    font-size: clamp(52px, 6vw, 66px);
    font-weight: 400;
    letter-spacing: -0.02em;
    line-height: 1.0;
    margin: 16px 0 0;
}
.hero-sub {
    font-family: var(--font-body);
    font-size: 18px; line-height: 1.6;
    opacity: 0.75;
    max-width: 540px;                                 /* §7 subtitle measure */
    margin: 24px auto 0;                              /* §3 heading → subheading */
}
.hero-actions { display: flex; gap: 12px; justify-content: center; margin-top: 48px; } /* §3 subheading → CTA */

.hero-paper { max-width: 1172px; margin: 60px auto 0; }     /* §7 wide media; 60 from §3 scale */
.hero-paper .pv-mat { padding: 0 6%; border-bottom-left-radius: 0; border-bottom-right-radius: 0; }
.card-paper {
    text-align: left;
    background: var(--bg);
    border: none;
    box-shadow:                                       /* §5 Card Shadow */
        0 50px 40px rgba(0,0,0,.01),
        0 50px 40px rgba(0,0,0,.02),
        0 20px 40px rgba(0,0,0,.05),
        0 3px 10px  rgba(0,0,0,.08);
}
.hero-paper .pv-layer-main {
    border-bottom-left-radius: 0; border-bottom-right-radius: 0;  /* cut by the scene edge */
    -webkit-mask-image: linear-gradient(to bottom, #000 calc(100% - 56px), transparent); mask-image: linear-gradient(to bottom, #000 calc(100% - 56px), transparent);   /* product-visuals .pv-cut */
    padding: 32px 32px 48px 0;                        /* §3 card padding; 32px right = Recipe 2 overlap track */
}
.hero-paper .pv-row { padding: 0 32px; }              /* rows align with the sheet head */
.paper-head { display: flex; justify-content: space-between; align-items: center; padding: 0 32px 24px; }
.paper-body .pv-kpi { padding: 0 32px 16px; margin: 0; }
.hero-paper .pv-layer-float { padding: 24px; margin-bottom: 12%; }   /* Recipe 2 grid places it on the sheet's right edge */
.hero-paper .is-warm { background: var(--tint-peach); }              /* §1 Content Tints: the warm sheet (craft.do "Write" scene) */
.pv-layer-float p:last-child { margin: 8px 0 0; font-size: 16px; }   /* §2 body secondary */

[data-theme="dark"] .card-paper {
    background: var(--surface-1);                     /* step up: §8 surface nesting on dark scenes */
    box-shadow:                                       /* §5 Dark Theme Card Shadow */
        0 50px 40px rgba(0,0,0,.10),
        0 50px 40px rgba(0,0,0,.15),
        0 20px 40px rgba(0,0,0,.20),
        0 3px 10px  rgba(0,0,0,.30);
}

@media (max-width: 767px) {
    .hero-scene { padding: 72px 32px 0; }             /* §3 narrow hero top; §8 .scene narrow padding */
    .hero-actions { flex-direction: column; align-items: center; }
}
@media (prefers-reduced-motion: no-preference) {
    .hero-scene-copy > * { animation: hero-rise 0.8s cubic-bezier(0.16, 1, 0.3, 1) both; }
    .hero-scene-copy > :nth-child(2) { animation-delay: 100ms; }
    .hero-scene-copy > :nth-child(3) { animation-delay: 200ms; }
    .hero-scene-copy > :nth-child(4) { animation-delay: 300ms; }
    @keyframes hero-rise { from { opacity: 0; transform: translateY(32px); } }
}
/* Sky layers — copy from atmosphere.md: .sky-grain (R2), .ht-cloud (R3a), and the one cutout .cut-notebook (R4, yellow).
   Markup order inside .hero-scene: grain, clouds, notebook (all aria-hidden), copy, then the paper mock. */
.hero-scene .cut-notebook { right: 6%; bottom: -60px; width: 340px; height: 300px; z-index: 1; }  /* behind the paper (z 2), lower right */
.hero-scene-copy, .hero-paper { position: relative; z-index: 2; }
/* Floating sheet: interaction-patterns §1.5 D (Toast slides in) — CSS + JS copied from there */
```

**Dark theme**: the sky uses the deep variant (`--scene-blue: #1E3258`) lightening to `color-mix(in srgb, #1E3258 70%, #F0EDE8)` at the horizon; halftone clouds drop to `rgba(255,255,255,.25)` dots, and the white cutouts become `var(--surface-1)`; text stays `var(--text)` (warm off-white). Paper sheets step up to `var(--surface-1)` with the heavier dark shadow — a `var(--bg)` sheet on a deep navy scene reads as a hole, not paper. The pill CTA inverts via `--accent`.

### Signature details

1. **The 20px canvas inset.** Every scene floats inside the page with `margin: 0 20px` and `24px` radius — color is an object on the table, never a full-bleed band. `.scene { margin: 0 20px; border-radius: 24px; }`
2. **Paper with weight.** Any document-like object (product sheets, pricing cards, quote cards) carries the four-layer shadow and an opaque warm sheet; ordinary text groups get none. `box-shadow: 0 50px 40px rgba(0,0,0,.01), 0 50px 40px rgba(0,0,0,.02), 0 20px 40px rgba(0,0,0,.05), 0 3px 10px rgba(0,0,0,.08);`
3. **Stepped curves down to a pill.** 24 → 16 → 8 → pill, visible in one glance at the hero. `.scene{border-radius:24px} .pv-panel{border-radius:16px} .pv-pill{border-radius:8px} .btn-dark{border-radius:9999px}`
4. **Serif claim, sans work.** Headline in Playfair 400 at `-0.02em`; everything inside a mock, button, or card heading in DM Sans. `h1,h2{font-family:var(--font-display);font-weight:400;letter-spacing:-0.02em} .pv,.btn-dark,.card h3{font-family:var(--font-body)}`
5. **Pause after a scene.** A scene followed by the canvas or a different scene gets the dramatic bottom space. `.scene + section { padding-top: 168px; }` (§3 scene transition rule; 96px under 768px).

### Motion personality

Unhurried and tactile: things land like paper being set down. Fits from interaction-patterns §1.5: **D (Toast slides in)** for a floating sheet, **A (Rows stream in)** for a document list gaining entries, **C (Typing caret)** for writing products. Avoid B (cursor click) as the default — it reads as a SaaS dashboard demo. Easing and duration: entrance `0.8s cubic-bezier(0.16, 1, 0.3, 1)` (§6 and interaction-patterns §1), card stagger 100ms. Hover: paper cards lift `translateY(-4px)` with `transform 0.2s ease-in-out` and the shadow deepens; pills lift `translateY(-1px)`; links/opacity `0.3s linear`. **Never moves**: scene backgrounds (no color shift, parallax, or scroll-tinted transitions), headlines after entrance, the nav pill, and anything in a loop.

### Preferred signature moves

Which layout each section uses by default is set in the master `SKILL.md` Step 4.3 *Style layout defaults* table; the notes below adjust how each move looks in this style.

- **M4 Framed hero stage** — the default hero (above). Colorful-specific: the panel is the sky `.scene` (atmosphere.md R2–R4); the mock must be dense paper, not a thin strip (M4 "wallpaper" failure mode).
- **M2 Highlighted headline words** — set the key word in Playfair *italic* weight 400 instead of a color mark; never highlight with a scene color (scenes are rooms, not marks). *Note: italic is not loaded by the §2 font link — gap below.*
- **M10 Poster quote** — inside a warm or green scene (`--scene-yellow`, `--scene-peach`, or `--scene-green`), one large serif quote at section-heading size on a single paper card. Only with a real quote from the user.
- **M5 Bento with a lead tile** — on the default canvas: tiles are paper cards (`var(--surface-1)` on canvas, 24px radius, four-layer shadow); the lead tile may sit inside a scene. Never give each tile its own scene color.

### Drift guard

- **Toward Minimal**: 2px buttons, zero shadow, all-sans headings, achromatic page with no scene, 180px rhythm.
- **Toward Business**: blue-gray tinted shadows, 8px rounded rectangle buttons, sans hero with a gradient product stage, logo-wall-first trust layout.
- **Toward Editorial**: teal accent, Cormorant headings, near-black `#161616` stage band, dark/light alternating sections.
- **Toward generic AI**: mesh backgrounds, gradients outside the hero sky, floating colored blobs not cut as paper, scene color on buttons/icons/badges, emoji or icon tiles in pastel circles, 4+ scene colors, page-level feature cards each in a different pastel (tints belong to the product's own content inside a mock — §1 Content Tints), glassmorphism panels, full-bleed edge-to-edge color bands (losing the 20px inset), bold serif (600+).

### Screenshot test

1. **The hero is a sky panel floating inside the page** (periwinkle lightening to the horizon, grain, halftone clouds at the edges, a paper product sheet rising from the bottom edge — no cutouts). Below it, **pastel rounded panels float** with a visible warm-white gutter on both sides at the top of the screenshot, and two or three pastels appear in the page, at least one warm (peach or yellow); the product mocks show tinted content cards.
2. **The biggest text is a serif at regular weight**, while every button is a black (or white, in dark) pill.
3. **At least one product sheet visibly casts a soft, deep shadow** on a colored scene — it reads as paper resting on color, not a bordered box.
