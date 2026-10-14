# Visual Style Guide — Business Preset

> DNA: Calendly (Light) × Linear (Dark)
> Tone: Warm, professional, structured. For B2B SaaS, scheduling tools, enterprise platforms.

> **Must use — at the end of this file, §10 Style Signature.** Read this file to the last line. Every page in this style needs:
> 1. When the page has a hero (not 404, not a single non-hero section): the hero built from the "Hero showcase", starting from its HTML example and keeping the `.biz-stage` class (the self-check looks for it)
> 2. At least two items from Signature details
> 3. Motion personality and Drift guard, followed as written
> 4. Screenshot test, run against the finished page before delivery

This file is a self-contained style preset. When this preset is active, follow ALL tokens from this file. Do not mix with `shared/visual-style.md` (Minimal preset) values.

---

## Design Philosophy

Four core principles:

1. **Warmth before neutrality** — Off-white base (#FCFBF8) reads as inviting, not clinical. Depth comes from soft blue-gray shadows, not background steps alone.
2. **Rounded geometry signals approachability** — Buttons (8px), cards (16–24px), and product stages (48px) use consistent rounded corners. No sharp edges anywhere.
3. **Typography as guidance** — Plus Jakarta Sans conveys structure and clarity: 600 for hero and section headings, 500 below 28px. Body text (Inter 400) is legible and efficient. Weight contrasts are moderate — this is a working tool, not a gallery.
4. **Color lives inside the product stage** — The page shell stays warm neutral. Brand color and gradients are permitted only inside product screenshots or demonstrating the product UI itself. The surrounding layout stays calm.

---

## 1. Color System

### Light Theme (Calendly DNA)

```
--bg:           #FCFBF8        Page background — warm off-white
--surface-1:    #F5F3EE        Cards, input fields, secondary panels
--surface-2:    #D8DCE0        Borders, dividers, title bars
--text:         #071A31        All text — deep blue-black (hierarchy via opacity)
--text-inverse: #FFFFFF        Text on dark surfaces
--accent:       #071A31        CTA button background (default = --text; brand color overrides)
--accent-text:  #FFFFFF        CTA button text
```

**Text hierarchy via opacity (base color #071A31)**:
```
Primary text:         opacity: 1
Subtitle/description: opacity: 0.5
Auxiliary/label:      opacity: 0.4
Weakest (copyright):  opacity: 0.2
Logo wall:            opacity: 0.15
```

### Dark Theme (Linear DNA)

```
--bg:           #09090B        Page background — deep cool near-black
--surface-1:    #131418        Cards, panels (subtle step above bg)
--surface-2:    #1D2028        Borders, dividers, card rings
--text:         #F2F4F7        All text — cool off-white (hierarchy via opacity)
--text-inverse: #09090B        Text on light surfaces
--accent:       #F2F4F7        CTA button background (default = --text)
--accent-text:  #09090B        CTA button text
```

**Text hierarchy via opacity (base color #F2F4F7)**:
```
Primary text:         opacity: 1
Subtitle/description: opacity: 0.5
Auxiliary/label:      opacity: 0.4
Weakest (copyright):  opacity: 0.2
Logo wall:            opacity: 0.15
```

### Accent Color Rules

- **Default accent is the text color**: `--accent` defaults to `--text`. Output is identical to no-brand-color.
- If the user provides a brand color, only override `--accent` and `--accent-text`.
- **Chromatic color < 10% of visible page area**. Page shell stays warm neutral.
- Color-tinted product stages (gradients inside UI demos) are permitted but scoped to the product demo element only.

**`--accent` allowed uses (exhaustive)**:
- ✅ Primary CTA button background (`.btn-dark`, required)
- ✅ Nav CTA button background (optional)
- ✅ Pricing recommended tier border ring `rgba(accent, 0.15)` (optional)
- ✅ Link hover color (optional)
- ✅ Pricing selected-plan card border or background tint (Calendly pattern — optional, at most 1 tier)
- ❌ Toggle / Switch active state (always use `var(--text)`)
- ❌ Icon backgrounds, badge fills, general section backgrounds
- ❌ Gradients in the page shell (only inside product stage elements)

### Absolutely Forbidden

- Different background colors for different sections (except product stage areas)
- Colored circular/square backgrounds behind icons
- Pure achromatic black (#000000) as text color — use `#071A31` (light) or `#F2F4F7` (dark)
- Box-shadows on page shell elements (nav, footer) — shadow reserved for cards only

---

## 2. Typography System

### Font Families

| Role | Font | Usage |
|------|------|-------|
| Display | `'Plus Jakarta Sans', -apple-system, sans-serif` | Headings, navigation, buttons, UI labels |
| Body | `'Inter', -apple-system, sans-serif` | Body paragraphs, FAQ answers, long-form text |
| Mono | `'JetBrains Mono', 'SF Mono', Consolas, monospace` | Labels (UPPERCASE), metadata, code |

```css
:root {
    --font-display: 'Plus Jakarta Sans', -apple-system, sans-serif;
    --font-mono:    'JetBrains Mono', 'SF Mono', Consolas, monospace;
    --font-body:    'Inter', -apple-system, sans-serif;
}
```

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600&family=Inter:wght@400;500&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
```

### Type Scale

```
Hero heading:     clamp(48px, 6vw, 72px)    weight: 600   tracking: -0.02em   line-height: 1.1
Section heading:  clamp(32px, 4vw, 48px)    weight: 600   tracking: -0.02em   line-height: 1.1
Feature heading:  28px                       weight: 500   tracking: -0.02em   line-height: 1.2
Card heading:     20px                       weight: 500   tracking: normal    line-height: 1.3
Body text:        18px                       weight: 400   tracking: normal    line-height: 1.6
Body secondary:   16px                       weight: 400   tracking: normal    line-height: 1.6
Button:           16px                       weight: 500   tracking: normal
Navigation:       14px                       weight: 500   tracking: normal
Label:            12px                       weight: 400   tracking: +0.72px   text-transform: uppercase
```

**Key rules**:
1. Hero (72px) uses weight 600 — Plus Jakarta Sans has a readable geometric 600 weight
2. Section headings (48px) also weight 600 for structural authority
3. Below 28px, switch to weight 500 (feature headings) or 400 (body)
4. Subtitles change opacity, not weight or color
5. Labels always: 12px / mono / 400 / uppercase / +0.72px tracking / opacity 0.4

---

## 3. Spacing System

### Base Unit: 4px (Calendly DNA)

```
Spacing scale: 4 · 8 · 12 · 16 · 24 · 32 · 48 · 56 · 64 · 120 px
```

### Specific Applications

```
Section padding (top and bottom):          120px
Note: Visual gap between adjacent sections = 120 + 120 = 240px.
Section internal (heading to content):     48px
Hero top whitespace (nav to hero heading): 120px
Hero heading to subheading:                24px
Subheading to CTA:                         48px
Card internal padding:                     32px
Card gap:                                  24px
Grid gutter:                               24px
Footer top padding:                        120px
Logo wall vertical padding:                120px
```

### Narrow Screen Spacing (< 768px)

```
Desktop 120px (section / hero top / footer)  →  64px
Desktop 64px (large component gaps)          →  40px
Desktop 48px (heading to content)            →  32px
Desktop 32px (card padding)                  →  24px
Desktop 24px (gap)                           →  keep unchanged
Left/right padding 32px                      →  20px
```

---

## 4. Border Radius System

```
Button:              8px    (warm, rounded — not sharp like Minimal)
Input/form field:    8px
Feature card:        16px
Content card:        24px   (product stage container)
Product stage panel: 48px   (Calendly's large nested container)
Toggle:              9999px (pill)
```

Nested radius rule: outer container uses the larger radius, inner content one step smaller. Example: product stage 48px → inner panel 40px → inner CTA 16px.

---

## 5. Shadow System

**Cards use soft blue-gray shadows. Page shell elements (nav, footer) use no shadow.**

This is the primary difference from Minimal (which uses zero shadows everywhere). Shadows in Business signal interactivity and depth without adding visual drama.

### Light Theme Card Shadow

```css
.card {
    box-shadow:
        0 4px 5px rgba(71, 103, 136, 0.04),
        0 8px 15px rgba(71, 103, 136, 0.03),
        0 30px 50px rgba(71, 103, 136, 0.08);
}
```

### Dark Theme Card Depth

In dark mode, cards are distinguished by a 1px inset border ring (Linear pattern). No drop shadows.

```css
/* Dark theme only */
.card {
    box-shadow: inset 0 0 0 1px var(--surface-2);
    /* For truly elevated/floating cards: add 0 2px 4px rgba(0,0,0,0.4) */
}
```

### Light Theme Product Stage Nested Shadow

For the inner pricing panel or interactive product demo nested inside an outer card:
```css
.card-inner {
    box-shadow:
        0 4px 5px rgba(71, 103, 136, 0.04),
        0 8px 15px rgba(71, 103, 136, 0.03),
        0 15px 30px rgba(71, 103, 136, 0.06);
}
```

---

## 6. Transitions & Motion

```
hover transform:   transform 0.2s ease-in-out (button micro-lift translateY(-1px))
card hover:        transform 0.2s ease-in-out (card lift translateY(-4px) + box-shadow softens)
color/opacity:     opacity 0.3s linear or color 0.3s linear
scroll entrance:   opacity + transform 0.8s cubic-bezier(0.16, 1, 0.3, 1)
```

→ Full pattern recipes and JS implementations: see `shared/interaction-patterns.md`

---

## 7. Grid System

```
Main grid:        max-width 1200px, centered, padding 0 32px
Subtitle measure: max-width 540px (line width cap for subtitles)
4-col pricing:    4 × equal columns / 24px gap (Calendly's pricing grid)
Feature grid:     320px fixed + 516px fluid, 64px gap (for feature explanation sections)
```

---

## 8. Component Tokens

### Buttons

```css
.btn-dark {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 24px;           /* More generous than Minimal's 8px 16px */
    font-size: 16px;
    font-weight: 500;
    font-family: var(--font-display);
    line-height: 24px;
    background: var(--accent);
    color: var(--accent-text);
    border: none;
    border-radius: 8px;           /* Rounded, not sharp */
    cursor: pointer;
    text-decoration: none;
    transition: transform 0.2s ease-in-out;
}
.btn-dark:hover { transform: translateY(-1px); }

.btn-outline {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: 500;
    font-family: var(--font-display);
    line-height: 24px;
    background: transparent;
    color: var(--text);
    border: 1px solid var(--surface-2);
    border-radius: 8px;
    cursor: pointer;
    text-decoration: none;
    transition: border-color 0.3s linear;
}
.btn-outline:hover { border-color: var(--text); }

/* Dark theme: a --surface-2 border disappears on a --surface-1 card.
   Use dark --text (#F2F4F7) at the ladder's 0.2 step instead. */
[data-theme="dark"] .card .btn-outline { border-color: rgba(242, 244, 247, 0.2); }

/* Small button variant (nav CTA) */
.btn-sm {
    padding: 8px 16px;
    font-size: 14px;
}

:focus-visible {
    outline: 2px solid var(--text);
    outline-offset: 2px;
}
```

### Navigation

```css
:root { --nav-h: 72px; }   /* Slightly taller than Minimal's 68px — more generous */
body { padding-top: var(--nav-h); }

nav {
    padding: 16px 0;
    background: rgba(252, 251, 248, 0.9);   /* Light: warm off-white */
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}
[data-theme="dark"] nav {
    background: rgba(9, 9, 11, 0.9);
}
nav > .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 32px;
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
    border-radius: 16px;
    box-shadow: 0 4px 5px rgba(71,103,136,.04), 0 8px 15px rgba(71,103,136,.03), 0 30px 50px rgba(71,103,136,.08);
}
[data-theme="dark"] .card {
    box-shadow: inset 0 0 0 1px var(--surface-2);
}

/* White card on warm-surface background */
.card-white {
    padding: 32px;
    background: #FFFFFF;
    border-radius: 24px;
    box-shadow: 0 4px 5px rgba(71,103,136,.04), 0 8px 15px rgba(71,103,136,.03), 0 30px 50px rgba(71,103,136,.08);
}
```

**Surface nesting rule** (same as Minimal, adapted for Business surfaces):
- Inside `var(--bg)` section → card uses `var(--surface-1)` or `#FFFFFF`
- Inside `var(--surface-1)` section → nested element uses `var(--bg)` (**not** `var(--surface-1)`)
- Inside a card → screenshot frame / inner panel uses `var(--bg)`

### Section Backgrounds

```
Default:          var(--bg)          Most sections
Soft emphasis:    var(--surface-1)   At most 1-2 sections (feature blocks, pricing background)
White card area:  #FFFFFF            Pricing cards, testimonial cards on --surface-1 background

Not allowed: colored section backgrounds (brand gradient backgrounds).
Product stage elements (demo screenshots, hero artwork) may use brand gradients internally.
```

---

## 9. Brand Customization

### Brand Color Override

When the user provides a brand color:
1. Set `--accent` to that color; calculate `--accent-text` (luminance < 0.5 → `#FFFFFF`; ≥ 0.5 → `#000000`)
2. Optionally: apply to the pricing selected-tier card border at `rgba(accent, 0.15)` opacity
3. Hover: `filter: brightness(0.9)` (bright brand) or `filter: brightness(1.15)` (dark brand)
4. Pricing selected-plan: permitted to use `var(--accent)` as a card border color (Calendly pattern)
5. All surface and text colors remain warm neutral — brand color does not spread to the page shell

### Font Override

When user provides a brand font:
1. Replace `--font-display` value, keeping the geometric sans fallback chain
2. Update the Google Fonts `<link>` to load weights 400 + 500 + 600
3. Tracking: geometric sans → keep `-0.02em`; humanist sans → reduce to `-0.01em`

---

## 10. Style Signature

### Character

Business feels like dependable infrastructure with one expansive window into the product. The shell is calm and warm — `#FCFBF8` canvas, deep blue-black `#071A31` text, 120px pauses — because Calendly's DNA "chose `120px` section pauses and open warm surfaces over enclosing every content block in a card" so each promise is understood before the next arrives (taste decision 1). All expression is concentrated in one place: a large rounded product stage, where Calendly "chose blue-to-violet atmospheric gradients inside large `64px`-radius product stages over spreading saturated brand color through the page shell" (taste decision 2) — in practice a soft multi-hue mesh (sky blue, lavender/pink, mint) with a white glow behind the product card, not a two-stop blend. Curves carry warmth; shadows stay accountable — nested curves with blue-tinted depth at 3–8% opacity, never dramatic black shadows (taste decision 4). Centered composition for the promise, left-aligned for operational detail (taste decision 3). Where Minimal is flat and sharp, Colorful is playful scenes, and Editorial is serif contrast, Business is **soft, layered, and trustworthy: a stage of floating panels with real depth**.

### Hero showcase (mandatory)

**Composition**: `centered-stack`. Centered heading + subtitle + two buttons, then a full-container **product stage** (48px radius, §4 "Product stage panel") holding a Recipe 2 layered-cards mock (`shared/product-visuals.md` Recipe 2). The main panel rises from the stage's bottom edge and is cut by it (M3 + M4 Business row); one floating panel with the §5 nested shadow overlaps it and carries the motion cue. Radii nest per §4: stage 48px → main panel 40px → controls 8px (input radius). Inside the stage only, a **mesh gradient** (`shared/atmosphere.md` Recipe 1; §1 Accent Color Rules, "color-tinted product stages… permitted") built from the full Calendly Scheduling hero SVG palette (`#175295`, `#1E5EA7`, `#4890E3`, `#6BB1FF`, `#5DDFD7`, `#B89FFA`, `#EBB0FF`, `calendly.com.md` line 31): sky blue top-left, lavender/pink bottom-left, mint/aqua right, a white glow behind the card, fine grain. Never a two-stop blue → violet blend. The main card sits in a **frosted ring** (translucent white band, `backdrop-filter: blur(12px)`), and when the user names real integrations, 1–3 **app-icon tiles** (real logos, atmosphere.md Recipe 5) overlap the card's top-right corner. If the user supplies brand colors, keep the mesh structure (3+ hues + glow) and swap the hues.

**Recipe choice**: Recipe 2 by default (scheduling, finance, ops, collaboration). For analytics/commerce use Recipe 1's panel inside the same stage; for developer tools use Recipe 6 inside the same stage. The stage, gradient, and nested shadow stay identical — they are the Business signature, not the recipe.

**Background**: page shell `var(--bg)`, no section color, no glow, no grid. The mesh (and its glow) never leaves the stage.

**Entrance**: heading block uses §6 scroll entrance (0.8s `cubic-bezier(0.16, 1, 0.3, 1)`, 32px section distance per interaction-patterns §1). The mock does not fade; it runs §1.5 B (cursor clicks the confirm button), which replaces the reveal for the stage.

```html
<section data-section="hero" data-layout="centered-stack" data-bg="base" data-bold="true" class="biz-hero">
  <div class="container">
    <div class="biz-hero-copy">
      <p class="label">Scheduling for revenue teams</p>
      <h1>Every meeting booked, routed, and ready</h1>
      <p class="biz-hero-sub">Northwind routes inbound requests to the right rep and confirms the time before the lead goes cold.</p>
      <div class="biz-hero-ctas">
        <a class="btn-dark" href="#">Start for free</a>
        <a class="btn-outline" href="#">Talk to sales</a>
      </div>
    </div>

    <div class="biz-stage">
      <div class="pv pv-layers" data-mock role="img" aria-label="Northwind routing board with a booking confirmation card">
        <div class="pv-panel pv-layer-main">
          <div class="pv-row" style="grid-template-columns: 1fr auto; border-top: 0">
            <span class="pv-kpi">Inbound this week</span><span class="pv-label">Oct 6 – Oct 10</span>
          </div>
          <div class="pv-row" style="grid-template-columns: 24px 1fr auto auto"><span class="pv-avatar">MR</span><span>Maya Reyes · Acme Logistics</span><span class="pv-mono pv-muted">Tue 10:30</span><span class="pv-pill">Routed</span></div>
          <div class="pv-row is-focused" style="grid-template-columns: 24px 1fr auto auto"><span class="pv-avatar">DK</span><span>Dev Kapoor · Globex</span><span class="pv-mono pv-muted">Tue 14:00</span><span class="pv-pill is-strong">Pending</span></div>
          <div class="pv-row" style="grid-template-columns: 24px 1fr auto auto"><span class="pv-avatar">LS</span><span>Lena Sato · Initech</span><span class="pv-mono pv-muted">Wed 09:15</span><span class="pv-pill">Routed</span></div>
          <div class="pv-row" style="grid-template-columns: 24px 1fr auto auto"><span class="pv-avatar">JO</span><span>Jon Okafor · Umbrella</span><span class="pv-mono pv-muted">Wed 11:45</span><span class="pv-pill is-quiet">Declined</span></div>
        </div>
        <div class="pv-panel pv-layer-float biz-float">
          <p class="pv-label">Confirm · Dev Kapoor</p>
          <p class="pv-kpi">Tue, Oct 7 · 14:00</p>
          <p class="pv-muted">30 min · Video call · Owner: Maya R.</p>
          <span id="pv-confirm" class="pv-target is-focused biz-confirm">Confirm booking</span>
          <span class="pv-cursor" data-cursor-for="pv-confirm" style="left: 70%; top: 82%" aria-hidden="true">
            <svg viewBox="0 0 14 20"><path d="M1 1v16l4.5-4 3 6.5 2.5-1-3-6.5H14z"/></svg>
          </span>
        </div>
      </div>
    </div>
  </div>
</section>
```

```css
.biz-hero { padding-top: 120px; padding-bottom: 120px; }            /* §3 hero top / section padding — directional, not shorthand */
.biz-hero-copy { text-align: center; }
.biz-hero h1 {
    font-family: var(--font-display);
    font-size: clamp(48px, 6vw, 72px); font-weight: 600;          /* §2 hero heading */
    letter-spacing: -0.02em; line-height: 1.1;
    margin: 16px auto 0; max-width: 18ch;
}
.biz-hero-sub {
    font-family: var(--font-body); font-size: 18px; line-height: 1.6; /* §2 body text */
    opacity: 0.5; max-width: 540px; margin: 24px auto 0;          /* §1 subtitle opacity, §7 measure, §3 heading→sub */
}
.biz-hero-ctas { display: flex; gap: 12px; justify-content: center; margin-top: 48px; } /* §3 sub→CTA */

/* The stage: 48px panel, gradient lives only here */
.biz-stage {
    position: relative;
    margin-top: 64px;                                              /* §3 spacing scale: large component gap */
    padding: 64px 64px 0;                                          /* mock rises from the bottom edge (M4) */
    border-radius: 48px;                                           /* §4 product stage panel */
    overflow: hidden;
    isolation: isolate;
    background:                                                    /* atmosphere.md Recipe 1, calendly.com.md line 31 */
        radial-gradient(38% 46% at 50% 62%, rgba(255,255,255,.95) 0%, rgba(255,255,255,0) 100%),  /* glow behind card */
        radial-gradient(48% 70% at 4% 6%,   #6BB1FF 0%, transparent 72%),
        radial-gradient(40% 60% at 30% 0%,  color-mix(in srgb, #4890E3 55%, #FFFFFF) 0%, transparent 70%),
        radial-gradient(46% 70% at 0% 100%, #B89FFA 0%, transparent 72%),
        radial-gradient(40% 60% at 32% 104%,#EBB0FF 0%, transparent 70%),
        radial-gradient(46% 72% at 100% 78%,#5DDFD7 0%, transparent 72%),
        radial-gradient(40% 55% at 96% 4%,  color-mix(in srgb, #6BB1FF 60%, #5DDFD7) 0%, transparent 70%),
        color-mix(in srgb, #6BB1FF 22%, #FFFFFF);
    box-shadow: 0 4px 5px rgba(71,103,136,.04), 0 8px 15px rgba(71,103,136,.03), 0 30px 50px rgba(71,103,136,.08); /* §5 card */
}
.biz-stage::after { content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none; opacity: .12; mix-blend-mode: soft-light;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"); } /* grain, atmosphere.md R1 */
/* Frosted ring: wrap .pv-layer-main in <div class="frost-ring"> — see atmosphere.md Recipe 1; app tiles: Recipe 5 */
.biz-stage .pv { --pv-r-outer: 48px; --pv-r-inner: 16px; --pv-r-control: 8px; }   /* §4 per product-visuals §2 Business column */
.biz-stage .pv-layer-main {
    width: 82%;
    margin: 0 auto;
    padding: 24px 0 0;
    background: #FFFFFF;                                           /* §8 white card on tinted stage */
    border: 0;
    border-radius: 40px 40px 0 0;                                  /* §4 nested: 48 → 40, cut by the stage edge */
    box-shadow: 0 4px 5px rgba(71,103,136,.04), 0 8px 15px rgba(71,103,136,.03), 0 15px 30px rgba(71,103,136,.06); /* §5 nested */
}
.biz-stage .pv-row { padding: 0 32px; }                            /* §3 card internal padding */
.biz-float {
    position: absolute; right: 4%; bottom: 12%; width: 36%;
    padding: 24px;
    background: #FFFFFF;
    border: 0;
    border-radius: 24px;                                           /* §4 content card */
    box-shadow: 0 4px 5px rgba(71,103,136,.04), 0 8px 15px rgba(71,103,136,.03), 0 30px 50px rgba(71,103,136,.08); /* §5 card */
}
.biz-float > * + * { margin-top: 8px; }
.biz-confirm {
    display: inline-flex; margin-top: 16px; padding: 8px 16px;     /* §8 .btn-sm */
    font-family: var(--font-display); font-size: 14px; font-weight: 500;
    border: 1px solid var(--surface-2); border-radius: 8px;
}
.biz-confirm.is-focused { background: var(--accent); color: var(--accent-text); border-color: transparent; }

@media (prefers-reduced-motion: no-preference) {
    .biz-hero-copy { transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1); }
    .biz-hero-copy.is-before { opacity: 0; transform: translateY(32px); }
}

@media (max-width: 767px) {
    .biz-hero { padding-top: 64px; padding-bottom: 64px; }        /* §3 narrow */
    .biz-stage { padding: 40px 20px 0; border-radius: 24px; margin-top: 40px; } /* §3 narrow 64→40, 32→20; radius steps to content card */
    .biz-stage .pv-layer-main { width: 100%; border-radius: 16px 16px 0 0; }
    .biz-stage .pv-row { padding: 0 16px; }
    .biz-float { position: static; width: 100%; margin: 12px 0 0; }
}
```

Add the §1.5 shared trigger + recipe B script from `shared/interaction-patterns.md` unchanged. The static markup is the final (confirmed) state.

**Dark theme**: keep the stage, swap the depth model to Linear's. Stage background becomes `var(--surface-1)` with `box-shadow: inset 0 0 0 1px var(--surface-2)` (§5 Dark Theme Card Depth); the mesh survives only as its hue radials at `color-mix(in srgb, <hue> 45%, transparent)` over `var(--surface-1)` (drop the base color and white glow; frosted ring becomes `rgba(255,255,255,.06)`) so the stage reads as a lit window in a near-black shell — Linear's single pink gradient moment is the precedent (`linear.md`, "a single editorial moment, not a system"). Inner panels use `var(--bg)` with `inset 0 0 0 1px var(--surface-2)`; the floating card adds the elevated `0 2px 4px rgba(0,0,0,0.4)` from §5. No `#FFFFFF` panels in dark.

### Signature details

1. **Nested-curve stack** — every enclosure steps down one radius: 48 → 40 → 24/16 → 8 (§4, Calendly `64/48/40/16` chain).
```css
.stage { border-radius: 48px; } .stage > .panel { border-radius: 40px; }
.panel .card { border-radius: 16px; } .panel .control { border-radius: 8px; }
```
2. **Blue-tinted three-layer shadow on raised objects only** — cards and floating panels, never nav/footer/sections (§5).
```css
.card-white { box-shadow: 0 4px 5px rgba(71,103,136,.04), 0 8px 15px rgba(71,103,136,.03), 0 30px 50px rgba(71,103,136,.08); }
```
3. **White card on warm surface** — the soft-emphasis section (`--surface-1`) holds `#FFFFFF` 24px cards; the two warm neutrals plus pure white are the whole shell palette (§8).
```css
[data-bg="alt"] { background: var(--surface-1); }
[data-bg="alt"] .card-white { background: #FFFFFF; border-radius: 24px; }
```
4. **Centered promise, left-aligned operations** — section headers that state a promise are centered; any list, price, or comparison below starts from a left edge (Calendly taste decision 3).
```css
.section-head { text-align: center; max-width: 540px; margin: 0 auto 48px; }
.section-body { text-align: left; }
```
5. **One accent ring on the chosen thing** — the selected tier or recommended option gets an `--accent` ring, nothing else (§1 allowed uses, §9).
```css
.tier.is-selected { box-shadow: 0 0 0 2px var(--accent), 0 30px 50px rgba(71,103,136,.08); }
```

### Motion personality

Measured and reassuring: things settle, nothing performs. Use §1.5 **B (cursor clicks)** for the hero — a confirmed action is the Business story — and **D (toast)** or **E (number ticks)** for feature mocks; one recipe per mock. Timing: entrance `opacity + transform 0.8s cubic-bezier(0.16, 1, 0.3, 1)` (§6 = interaction-patterns §1); hover `transform 0.2s ease-in-out`; color/opacity `0.3s linear`. Hover: buttons lift `translateY(-1px)`, cards lift `translateY(-4px)` and the shadow softens (§6); outline buttons change border color only. Never moves: nav, footer, section backgrounds, the stage gradient (no animated or shifting gradients), headings after entrance, logo walls (no marquee in Business — calm shell). Scroll reveal on at most half the content sections.

### Preferred signature moves

Which layout each section uses by default is set in the master `SKILL.md` Step 4.3 *Style layout defaults* table; the notes below adjust how each move looks in this style.

- **M4 Framed hero stage** — the default hero (above). Business adjustment: 48px radius, multi-hue mesh inside only, frosted ring around the card, mock cut by the stage bottom.
- **M3 Product rising from the fold** — combined with M4; visual top edge must still sit above the fold at 1440 × 900 with the 120px hero top.
- **M5 Bento with a lead tile** — tiles are `.card` (16px, §5 shadow); the lead tile may reuse a small stage (24px radius) with the gradient — counts as a product stage, keep to one per page besides the hero (*inference*: preserves "Scheduling confines its gradient to one rounded hero").
- **M11 Stat bento** — enterprise trust pages; title tile on `--surface-1`, number tiles `#FFFFFF` with §5 shadow; real numbers, or tagged sample numbers per `shared/signature-moves.md` §4 (catalog intro) — never when the user said there are none.

### Drift guard

Forbidden here because it reads as another style or as generic AI:
- **→ Minimal**: 2px buttons, zero shadow, pure grey `#141414` text, 180px rhythm, `.section-dark` black bands.
- **→ Colorful**: pill buttons, serif display, pastel scene section backgrounds, more than one tinted stage area beyond the hero + one bento tile.
- **→ Editorial**: Cormorant/serif headlines, teal accent, dark/light alternating section stage, italic emphasis.
- **→ Generic AI**: gradient on the page shell or text, a two-stop blue → violet stage gradient, glow behind (outside) the stage, perspective grid, black `rgba(0,0,0,…)` drop shadows in light theme, colored icon circles, left-border accent stripes, every section fading up, shadows on nav/footer.

### Screenshot test

1. The hero has one large 48px-rounded stage with a soft multi-hue mesh interior (sky blue, lavender/pink, mint, white glow behind the card) and white floating panels with soft blue-gray shadow; nothing else on the page is saturated.
2. The shell is warm off-white with deep navy text (not grey, not black), and raised cards visibly float with soft shadow while sections are flat.
3. Buttons are 8px rounded rectangles in Plus Jakarta Sans — neither sharp nor pill — and section pauses are a uniform ~240px between sections.
