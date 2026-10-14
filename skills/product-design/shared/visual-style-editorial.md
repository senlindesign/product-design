# Visual Style Guide — Editorial Preset

> DNA: Perplexity (Light + Dark)
> Tone: Authoritative, knowledge-forward, AI and media-adjacent products. Serif claims, restrained teal.

> **Must use — at the end of this file, §10 Style Signature.** Read this file to the last line. Every page in this style needs:
> 1. When the page has a hero (not 404, not a single non-hero section): the hero built from the "Hero showcase", starting from its HTML example and keeping the `.ed-stage` class (the self-check looks for it)
> 2. At least two items from Signature details
> 3. Motion personality and Drift guard, followed as written
> 4. Screenshot test, run against the finished page before delivery

This file is a self-contained style preset. When this preset is active, follow ALL tokens from this file. Do not mix with `shared/visual-style.md` (Minimal preset) values.

---

## Design Philosophy

Four core principles:

1. **Stage the promise, daylight the proof** — The entry section (hero) may use a dark photographic or near-black stage to make the product feel present and capable. Following sections resolve to warm white — lowering visual strain while visitors examine how it works.
2. **Editorial authority over dashboard familiarity** — Large serif headings make claims feel authored and declarative. Sans-serif handles mechanics, features, and evidence. Mono handles labels and data. This three-voice stack signals that the product has something to say, not just configure.
3. **Chromatic restraint preserves consequence** — The teal accent (`#20808D`) is reserved for actions, links, and status cues only. When most of the page stays neutral, teal still means "do something." Distributing it across headings or backgrounds turns it into ambient noise.
4. **Depth reserved for agency** — Shadows concentrate around interactive surfaces (hero panel, CTA, search input). Static content (pricing cards, feature descriptions) has no shadow. Depth becomes a behavioral cue: the surface that can act feels tangible.

---

## 1. Color System

### Light Theme (Perplexity warm canvas DNA)

```
--bg:           #FAF8F5        Page canvas — warm off-white
--surface-1:    #FDFBFB        Light content surface (very subtle step above bg — nearly invisible on --bg; separate a surface-1 element from --bg with a 1px solid var(--surface-2) border)
--surface-2:    #E8E4DF        Borders, dividers, quiet separators
--text:         #27251E        All text — warm near-black (hierarchy via opacity)
--text-inverse: #FDFBFB        Text on dark surfaces
--accent:       #20808D        Teal — CTA button, links, interactive status (HARDCODED — not black default)
--accent-text:  #FFFFFF        Text on teal buttons
```

**Text hierarchy via opacity (base color #27251E)**:
```
Primary text:         opacity: 1
Subtitle/description: opacity: 0.6
Auxiliary/label:      opacity: 0.45
Weakest (copyright):  opacity: 0.25
Logo wall:            opacity: 0.2
```

### Dark Theme (Perplexity hero-black DNA)

```
--bg:           #161616        Page canvas — near-black (hero entry tone)
--surface-1:    #1A1918        Cards, panels — warm dark (Perplexity's dark surface)
--surface-2:    #2A2826        Borders, dividers, warm charcoal
--text:         #DEDEDE        All text — light gray (hierarchy via opacity)
--text-inverse: #1A1918        Text on light surfaces
--accent:       #20808D        Teal — same as light theme (accent does not flip to white in dark)
--accent-text:  #FFFFFF        Text on teal buttons
```

**Text hierarchy via opacity (base color #DEDEDE)**:
```
Primary text:         opacity: 1
Subtitle/description: opacity: 0.6
Auxiliary/label:      opacity: 0.45
Weakest (copyright):  opacity: 0.25
Logo wall:            opacity: 0.2
```

### Accent Color Rules

**Critical difference from Minimal**: `--accent` in Editorial is ALWAYS `#20808D` (teal). It does NOT default to `var(--text)`. On a dark page, the button is teal, not white.

- If the user provides a brand color, override `--accent` with that color; override `--accent-text` accordingly
- If the user provides NO brand color, teal is the accent — this IS the style's identity
- **`--accent` area < 10% of visible page surface** (teal buttons and links are small — this is easy to maintain)
- Teal should NOT spread to headings, section backgrounds, or decorative elements

**`--accent` allowed uses (exhaustive)**:
- ✅ Primary CTA button background (`.btn-dark`, required)
- ✅ Nav CTA button background (optional)
- ✅ Interactive search panel border glow (optional — hero search input)
- ✅ Link hover color (optional)
- ✅ Status badge background (functional only, e.g., "Available" / "Online")
- ❌ Section backgrounds, even at low opacity
- ❌ Heading color or gradient text
- ❌ Icon backgrounds or badge fills

### Dark/Light Section Contrast (Editorial Pattern)

The Editorial preset often uses a **dark entry + light body** structure:

```
Entry (hero):     dark background (--bg = #161616 on dark theme, or a local dark override on light theme)
Mid-page:         light canvas (--bg = #FAF8F5 on light theme)
Feature sections: alternate between --bg and --surface-1
CTA / closing:    dark background returns (creates a framing effect)
```

For a light-theme page with an Editorial dark-entry hero:
```css
.hero-dark {
    background: #161616;
    color: #DEDEDE;
    /* Use light-theme surface tokens inverted:
       --text-inverse for body text, teal for CTA */
}
```

The dark hero is the "stage." Everything following is the "proof."

### Absolutely Forbidden

- Teal (`#20808D`) used as a section background color
- Gradient text effects on serif headings (it undermines the editorial voice)
- Different background colors for every section (max 2 distinct light backgrounds per page — `--bg` and `--surface-1` — plus the dark hero/CTA band)
- Shadows on static content like pricing cards or feature cards

---

## 2. Typography System

### Font Families

| Role | Font | Usage |
|------|------|-------|
| Display (editorial) | `'Cormorant Garamond', Georgia, serif` | All headings, hero claims, section titles |
| Body (operational) | `'Plus Jakarta Sans', -apple-system, sans-serif` | Body text, navigation, buttons, feature descriptions |
| Mono (structural) | `'JetBrains Mono', 'SF Mono', Consolas, monospace` | Labels (UPPERCASE), metadata, eyebrow labels |

```css
:root {
    --font-display: 'Cormorant Garamond', Georgia, serif;
    --font-mono:    'JetBrains Mono', 'SF Mono', Consolas, monospace;
    --font-body:    'Plus Jakarta Sans', -apple-system, sans-serif;
}
```

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500&family=Plus+Jakarta+Sans:wght@400;500&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
```

**Critical**: `--font-display` is a serif font (Cormorant Garamond). Hero, cross-page hero, and section headings use serif. Feature and card headings (24px and below) use `--font-body`, exactly as the type scale lists — serif below 24px is not allowed. `--font-body` is Plus Jakarta Sans — a humanist geometric sans.

### Type Scale

```
Hero heading:     72px                        weight: 400   tracking: -0.02em   line-height: 1.0
Cross-page hero:  clamp(48px, 5vw, 64px)     weight: 400   tracking: -0.02em   line-height: 1.05
Section heading:  48px                        weight: 500   tracking: -0.02em   line-height: 1.1
Feature heading:  24px (--font-body)          weight: 500   tracking: normal    line-height: 1.3
Card heading:     20px (--font-body)          weight: 500   tracking: normal    line-height: 1.3
Body text:        16px (--font-body)          weight: 400   tracking: normal    line-height: 1.6
Button:           16px (--font-body)          weight: 500   tracking: normal
Navigation:       16px (--font-body)          weight: 400   tracking: normal
Label (eyebrow):  12px (--font-mono)          weight: 400   tracking: +0.96px   text-transform: uppercase
```

**Narrow screens (< 768px)**: hero 48px (the cross-page hero's floor). Section heading 32px — derived, not observed: Perplexity's mobile type was not captured, so this follows the Minimal/Business section-heading floor.

**Key rules**:
1. **Hero (72px) and section headings (48px) use Cormorant Garamond** — large serif reads as authored and declarative
2. **Feature headings (24px) and below switch to Plus Jakarta Sans** — at this size, sans is clearer
3. Hero uses weight 400; section headings weight 500 — the size alone does the authority work at 72px
4. Eyebrow labels use `+0.96px` tracking (Perplexity's mono label tracking)
5. Do not use Cormorant Garamond at sizes below 24px — serif becomes hard to read at small sizes

---

## 3. Spacing System

### Base Unit: 4px (Perplexity DNA)

```
Spacing scale: 4 · 6 · 8 · 10 · 12 · 16 · 24 · 30 · 32 · 48 · 64 · 96 · 112 · 120 · 128 px  (30 = Perplexity's 3-card feature grid gap)
```

### Specific Applications

```
Section padding (standard):                   96px–120px (Perplexity uses 96, 112, 120, 128)
Section internal (heading to content):        48px (Perplexity primary layout row gap)
Hero top whitespace (nav to hero heading):    128px
Hero heading to subheading:                   24px
Subheading to CTA:                            40px
Card internal padding:                        32px
Card gap:                                     16px (Perplexity's tighter grid)
Grid gutter:                                  64px (Perplexity's primary column gap)
Footer top padding:                           128px
```

**Default section padding**: 96px (tighter than Minimal's 180px — editorial pages pack more content). Use 128px for section breaks after long explanatory content.

### Narrow Screen Spacing (< 768px)

```
Desktop 128px (hero top / footer)  →  80px
Desktop 120px (section padding)    →  64px
Desktop 96px (section padding)     →  56px
Desktop 64px (column gap)          →  32px
Desktop 48px (heading to content)  →  32px
Desktop 32px (card padding)        →  24px
Desktop 24px / 16px (gap)          →  keep unchanged
Left/right padding 64px            →  20px
```

---

## 4. Border Radius System

```
Hero panel:      30px   (Perplexity's hero search panel — the most elevated surface)
Product stage:   22px   (large content containers, outer cards)
Panel:           16px   (mid-level content panels, feature cards)
Inner UI:        14px   (nested windows, inner content frames)
Compact UI:      10px   (small cards, pricing cards — Perplexity's pricing card radius)
Control:         8px    (inputs, small surfaces)
Pill:            9999px (all CTA buttons — Perplexity uses pill actions)
```

**Nested radius rule**: `30px` hero panel → `22px` inner floating surface → `14px` secondary nested element. Each nesting level steps one size smaller.

**Note**: Like Colorful, Editorial uses pill buttons (`9999px`). The rounded-biological geometry is consistent with the teal accent philosophy — approachable and direct.

---

## 5. Shadow System

**Interactive surfaces and floating elements use layered shadows. Static content cards use no shadow.**

Shadow depth is a behavioral signal: "this surface can act." Pricing cards (passive) have no shadow. The hero search panel (active) has the deepest shadow.

### Hero Panel Shadow (highest elevation)

For the hero search input, the central interactive product element:
```css
.hero-panel {
    box-shadow:
        0 4px 24px -2px rgba(32, 128, 141, 0.4),   /* teal glow matches accent */
        0 0 0 1px rgba(32, 128, 141, 0.2),           /* teal ring */
        inset 0 1px 0 rgba(255, 255, 255, 0.15);    /* inner highlight */
}
```

### Floating Surface Shadow (standard elevation)

For cards and panels that need to read as interactive or elevated:
```css
.card-floating {
    box-shadow:
        0 2px 8px rgba(0, 0, 0, 0.08),
        0 8px 32px rgba(0, 0, 0, 0.08);
}
```

### Static Content

Pricing cards, feature description cards, and static testimonials: **no box-shadow**. Use `border: 1px solid var(--surface-2)` for definition.

```css
.card-static {
    border: 1px solid var(--surface-2);
    border-radius: 10px;   /* compact panel radius — Perplexity's pricing card */
}
```

---

## 6. Transitions & Motion

```
hover transform:   transform 0.15s ease-out (slightly faster than Minimal — Perplexity uses 150ms)
card hover:        transform 0.2s ease-in-out (card lift translateY(-4px))
color/opacity:     opacity 0.15s linear or color 0.15s linear
scroll entrance:   opacity + transform 0.8s cubic-bezier(0.16, 1, 0.3, 1)
```

→ Full pattern recipes and JS implementations: see `shared/interaction-patterns.md`

---

## 7. Grid System

```
Main grid:         max-width 1440px, centered, padding 0 64px
Content columns:   2-column asymmetric: 260px sidebar + 988px content (Perplexity's primary grid)
Subtitle measure:  max-width 560px (Perplexity uses wider subtitles than Minimal's 540px)
Customer card:     3 × equal columns / 16px gap
Feature grid:      3 × equal columns / 30px gap
```

**Note**: Editorial uses a wider max-width (1440px, full-bleed) vs Minimal's centered 1080px. The wider canvas is appropriate for editorial pages with large hero visuals and two-column article layouts.

---

## 8. Component Tokens

### Buttons

```css
.btn-dark {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 22px;           /* Perplexity's action padding */
    font-size: 16px;
    font-weight: 500;
    font-family: var(--font-body); /* Sans for buttons — not serif */
    line-height: 24px;
    background: var(--accent);    /* Teal #20808D by default */
    color: var(--accent-text);    /* White */
    border: none;
    border-radius: 9999px;        /* Pill — Editorial signature */
    cursor: pointer;
    text-decoration: none;
    transition: transform 0.15s ease-out, filter 0.15s ease-out;
}
.btn-dark:hover {
    transform: translateY(-1px);
    filter: brightness(1.1);      /* Teal brightens on hover */
}

.btn-outline {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 22px;
    font-size: 16px;
    font-weight: 500;
    font-family: var(--font-body);
    line-height: 24px;
    background: transparent;
    color: var(--text);
    border: 1px solid var(--surface-2);
    border-radius: 9999px;
    cursor: pointer;
    text-decoration: none;
    transition: border-color 0.15s linear;
}
.btn-outline:hover { border-color: var(--text); }

/* Small action variant */
.btn-sm {
    padding: 8px 20px;
    font-size: 14px;
}

:focus-visible {
    outline: 2px solid var(--accent);   /* Teal focus outline (not text color) */
    outline-offset: 2px;
}
```

### Navigation

```css
:root { --nav-h: 64px; }
body { padding-top: var(--nav-h); }

nav {
    padding: 12px 0;
    background: rgba(250, 248, 245, 0.88);   /* Light: warm off-white */
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}
[data-theme="dark"] nav {
    background: rgba(22, 22, 22, 0.88);
}
nav > .container {
    max-width: 1440px;
    margin: 0 auto;
    padding: 0 64px;
}
nav a {
    font-family: var(--font-body);
    font-size: 16px;
    font-weight: 400;
    color: var(--text);
    opacity: 0.6;
    text-decoration: none;
    transition: opacity 0.15s linear;
}
nav a:hover { opacity: 1; }

/* Nav CTA: override the link rule for BOTH opacity and color (specificity trap).
   Use .btn-sm in the nav so the bar stays at --nav-h: 64px (a default button makes it 68px). */
nav a.btn-dark { opacity: 1; color: var(--accent-text); }
nav a.btn-outline { opacity: 1; color: var(--text); }
```

### Label (Eyebrow)

```css
.label {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.96px;       /* Perplexity's +0.96px tracking — slightly wider than Minimal's 0.72px */
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.45;
}
```

### Card

```css
/* Static feature card — no shadow */
.card {
    padding: 32px;
    background: var(--surface-1);
    border-radius: 16px;
    border: 1px solid var(--surface-2);
}

/* Floating interactive card — with shadow */
.card-floating {
    padding: 32px;
    background: var(--surface-1);
    border-radius: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,.08), 0 8px 32px rgba(0,0,0,.08);
}

/* Pricing card — compact, no shadow */
.card-pricing {
    padding: 32px;
    background: var(--surface-1);
    border-radius: 10px;           /* compact panel radius */
    border: 1px solid var(--surface-2);
}

/* Pricing recommended tier: teal border ring instead of colored background */
.card-pricing.recommended {
    border-color: rgba(32, 128, 141, 0.4);
    box-shadow: 0 0 0 1px rgba(32, 128, 141, 0.2);
}
```

### Section Background Switching

```
Default sections:      var(--bg)           Most content sections
Alternate sections:    var(--surface-1)    At most 1-2 feature sections (very subtle)
Dark hero section:     #161616             The "stage" — entry or closing section
                                           (even on a light-theme page, the hero can use this)

Not allowed: colored section backgrounds (teal, other brand colors).
Dark entry + light body structure is the primary contrast technique.
```

For a dark hero on a light-theme page:
```css
.hero-stage {
    background: #161616;
    color: #DEDEDE;
    /* Text inside uses --text-inverse values */
}
.hero-stage .btn-dark {
    background: var(--accent);   /* Teal — visible on dark background */
    color: var(--accent-text);
}
```

---

## 9. Brand Customization

### Brand Color Override

When the user provides a brand color:
1. Override `--accent` with the brand color; calculate `--accent-text`
2. If the brand color is dark (luminance < 0.3), check contrast on dark hero sections — may need a lighter tint for the hero CTA
3. If the brand color is teal-family, it can extend to the hero panel shadow (replacing the teal glow tint)
4. If the brand color is warm (red, orange, amber), the teal glow tokens need to be replaced with the brand color's shadow equivalent

**Replacing the teal glow**: The hero panel shadow uses `rgba(32, 128, 141, ...)` — teal-tinted. When a brand color replaces the accent, update this shadow to use the brand color's RGB values instead.

### Font Override

When user provides a brand serif font:
1. Replace `--font-display` with the brand serif, keeping Georgia as fallback
2. Check that the font supports weight 400 and 500 (Cormorant does; not all serifs do)
3. If the brand font is a sans-serif, this is unusual for Editorial — ask whether the user wants to stay with a sans-only editorial approach or maintain the serif/sans split
4. Tracking: serif fonts at large sizes already have negative tracking built into the letterform — keep `-0.02em` or test visually

When user provides a brand sans font (for body):
1. Replace `--font-body` with the brand sans, keeping system-ui as fallback
2. The display role stays Cormorant Garamond unless explicitly overridden

---

## 10. Style Signature

### Character

Editorial reads like a front page that happens to have a working product on it. There is one dark stage, then daylight. The page opens on `#161616`, where a large serif claim sits above one glowing interactive panel, and everything after that resolves to warm paper (`#FAF8F5`). That split comes from the DNA decision "Stage the promise, daylight the proof" (perplexity.ai.md, Taste DNA: the first 900px viewport is dominated by `#161616`/`#1A1918`, and the mid-page and footer go to `#FDFBFB`/`#FAF8F5`). Three voices do the hierarchy work instead of color: the serif makes claims, the sans explains mechanics, and the mono labels evidence ("Editorial Authority Over Dashboard Familiarity"). Teal is rare enough to mean "act" (DNA: about 0.1–0.2% of the sampled area). Depth goes only to the surface that can act ("Depth Is Reserved for Agency"). The result is authored and calm: dense information, few colors, and one luminous object.

### Hero showcase (mandatory)

**Default hero: the Ask Stage.** It is a full-bleed `#161616` stage, with a centered 72px Cormorant claim, a 560px subtitle, and the teal CTA. Under them sits the elevated **hero panel**: a 30px-radius input surface with the teal glow shadow, which is the one place on the page with depth. One inner floating surface (22px radius) shows the product's answer.

- **Composition**: centered stack (DNA: "centered product … heroes"). Signature move M4 (Framed hero stage, Editorial row: `.hero-stage`, 30px radius, teal CTA). The panel is about 752px wide (DNA: hero interaction panel `752 × 164px`, 30px radius). The answer surface overlaps the panel below it, which is product-visuals **Recipe 7 (Chat)** staged as **Recipe 2** layering: the input is the centerpiece (Recipe 7 note: "the input uses the style's input or search-bar radius when it is the visual's centerpiece"), and the answer card floats with Floating Surface Shadow. For non-AI products, swap the answer card for a Recipe 3 isolated component with the same staging.
- **Background**: flat `#161616` by default. The DNA stage is photographic (perplexity.ai.md: hero image `2270 × 1080`, 2.10:1). Use a photo **only if the user supplies one**: set it as `background-image` under the same `#161616` base color, and never generate or fake one. No gradient, no glow behind the text, no grid.
- **Nested radius**: 30px panel → 22px floating answer → 14px inner rows (§4 nested radius rule).
- **Entrance motion**: the heading, subtitle, and CTA are static (visible immediately). The panel runs interaction-patterns §1.5 **C. Typing caret** (2000ms counter duration, plays once). The answer card then enters with the §6 scroll-entrance easing. The HTML holds the final state.

```html
<section data-section="hero" data-layout="full-bleed" data-bg="dark" data-bold="true" class="ed-stage">
  <div class="ed-stage-inner">
    <p class="label ed-stage-label">Research assistant</p>
    <h1 class="ed-claim">Answers you can cite.</h1>
    <p class="ed-sub">One sentence that says what the product does, in the user's own words.</p>
    <div class="ed-ctas">
      <a href="#" class="btn-dark">Try it free</a>
      <a href="#" class="btn-outline">See how it works</a>
    </div>

    <div class="pv ed-ask" data-mock role="img" aria-label="A question being typed into the product, with a cited answer below">
      <div class="ed-panel">
        <div class="ed-panel-input"><span data-type>Which suppliers raised prices after the March tariff change?</span><span class="pv-caret"></span></div>
        <div class="ed-panel-meta"><span class="label">Sources · 14</span><span class="ed-send" aria-hidden="true">↑</span></div>
      </div>
      <div class="ed-answer">
        <p class="label">Answer</p>
        <p class="ed-answer-text">Three of your eleven suppliers raised list prices within 30 days of the change.</p>
        <div class="ed-answer-row"><span>Halden Steel</span><span class="pv-mono">+6.2%</span><span class="ed-cite">[1]</span></div>
        <div class="ed-answer-row"><span>Corvo Packaging</span><span class="pv-mono">+4.0%</span><span class="ed-cite">[2]</span></div>
        <div class="ed-answer-row"><span>Northline Freight</span><span class="pv-mono">+2.5%</span><span class="ed-cite">[3]</span></div>
      </div>
    </div>
  </div>
</section>
```

```css
.ed-stage {
    background: #161616;                     /* §1 Dark Theme --bg / §8 dark hero section */
    color: #DEDEDE;                          /* §1 Dark Theme --text */
    padding-top: 128px;                      /* §3 hero top whitespace */
    padding-bottom: 96px;                    /* §3 default section padding */
    text-align: center;
    overflow: hidden;
}
.ed-stage-inner { max-width: 1440px; margin: 0 auto; padding: 0 64px; }   /* §7 main grid */
.ed-stage .label { color: #DEDEDE; }
.ed-claim {
    font-family: var(--font-display);
    font-size: 72px; font-weight: 400;       /* §2 hero heading */
    letter-spacing: -0.02em; line-height: 1.0;
    margin: 24px 0 0;
}
.ed-sub {
    font-family: var(--font-body); font-size: 16px; line-height: 1.6;
    opacity: 0.6;                            /* §1 subtitle opacity */
    max-width: 560px;                        /* §7 subtitle measure */
    margin: 24px auto 0;                     /* §3 heading to subheading */
}
.ed-ctas { display: flex; gap: 16px; justify-content: center; margin-top: 40px; }  /* §3 subheading to CTA; 16px = §3 card gap */
.ed-stage .btn-outline { color: #DEDEDE; border-color: #2A2826; }                   /* dark-surface override (§1 Dark --surface-2) */
.ed-stage .btn-outline:hover { border-color: #DEDEDE; }

.ed-ask { max-width: 752px; margin: 64px auto 0; text-align: left; }  /* DNA panel width 752px; 64px = §3 scale */
.ed-panel {
    background: #1A1918;                     /* §1 Dark --surface-1 */
    border-radius: 30px;                     /* §4 hero panel */
    padding: 24px;
    box-shadow:                              /* §5 Hero Panel Shadow — the only glow on the page */
        0 4px 24px -2px rgba(32, 128, 141, 0.4),
        0 0 0 1px rgba(32, 128, 141, 0.2),
        inset 0 1px 0 rgba(255, 255, 255, 0.15);
}
.ed-panel-input { font-family: var(--font-body); font-size: 16px; line-height: 1.6; }
.ed-panel-meta { display: flex; justify-content: space-between; align-items: center; margin-top: 24px; }
.ed-send {
    display: inline-grid; place-items: center; width: 32px; height: 32px;
    border-radius: 9999px;                   /* §4 pill */
    background: var(--accent); color: var(--accent-text);
}
.ed-answer {
    position: relative;
    width: 82%;                              /* Recipe 2 main-card width */
    margin: -16px 0 0 auto;                  /* overlaps the panel edge (Recipe 2 layering) */
    padding: 24px;
    background: #1A1918;
    border: 1px solid #2A2826;
    border-radius: 22px;                     /* §4 product stage (nested step under 30px) */
    box-shadow: 0 2px 8px rgba(0,0,0,.08), 0 8px 32px rgba(0,0,0,.08);  /* §5 Floating Surface Shadow */
}
.ed-answer-text { font-size: 16px; line-height: 1.6; margin: 8px 0 16px; }
.ed-answer-row {
    display: grid; grid-template-columns: 1fr auto 32px; gap: 12px; align-items: center;
    min-height: 32px; padding: 0 12px;      /* product-visuals §3 row */
    border-top: 1px solid #2A2826;
    font-size: 13px;
}
.ed-answer-row:first-of-type { border-radius: 14px 14px 0 0; }   /* §4 inner UI */
.ed-cite { font-family: var(--font-mono); font-size: 12px; color: var(--accent); }  /* link-like citation = accent "link" use */

@media (prefers-reduced-motion: no-preference) {
    .ed-answer { transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1); }  /* §6 scroll entrance */
    .ed-answer.is-before { opacity: 0; transform: translateY(16px); }   /* interaction-patterns small-element distance */
}
@media (max-width: 767px) {
    .ed-stage { padding-top: 80px; padding-bottom: 56px; }   /* §3 narrow: 128→80, 96→56 */
    .ed-stage-inner { padding: 0 20px; }
    .ed-claim { font-size: 48px; }                           /* §2 narrow hero */
    .ed-ask { margin-top: 32px; }                            /* §3 narrow: 64→32 */
    .ed-answer { width: 100%; margin-top: 12px; }            /* Recipe 2 narrow collapse */
}
```

Use the typing script from interaction-patterns §1.5 C on `[data-type]`. After it finishes, remove `is-before` from `.ed-answer`. Under reduced motion, both are already in their final state.

**Dark-theme note**: on a dark-theme page the stage *is* the page `--bg` (`#161616`), so it would melt into the next section. Keep the stage dark, and give the section after it `data-bg="alt"` (`var(--surface-1)` `#1A1918`) with a `1px solid var(--surface-2)` top border, so the stage→proof turn stays visible. The teal glow on the panel carries over unchanged (the accent does not flip, §1). On a light-theme page, the hardcoded `#161616`/`#DEDEDE`/`#1A1918`/`#2A2826` above are the local dark override (§1 Dark/Light Section Contrast).

### Signature details

1. **Mono eyebrow over every serif heading.** The three voices stack inside one heading block: mono label, serif claim, sans explanation.
```css
.ed-head .label { display: block; margin-bottom: 24px; }   /* §8 .label; 24px = §3 heading→sub */
.ed-head h2 { font-family: var(--font-display); font-size: 48px; font-weight: 500; letter-spacing: -0.02em; line-height: 1.1; }
.ed-head p  { font-family: var(--font-body); opacity: 0.6; max-width: 560px; margin-top: 24px; }
```
2. **The 260px margin column.** Section headings sit in a left rail and content runs in the wide column, like an article with marginalia (§7 Perplexity primary grid).
```css
.ed-margin { display: grid; grid-template-columns: 260px 1fr; column-gap: 64px; max-width: calc(260px + 64px + 988px); }  /* §7 + §3 gutter */
@media (max-width: 767px) { .ed-margin { grid-template-columns: 1fr; row-gap: 32px; } }
```
3. **Hairline-ruled static cards, no shadow anywhere but the stage.** Depth marks agency. Everything passive is paper with a rule.
```css
.card-static { border: 1px solid var(--surface-2); border-radius: 10px; box-shadow: none; }   /* §5 Static Content */
```
4. **Teal only as a small signal.** Citations, status dots, and the CTA use teal; the text around them stays neutral.
```css
.ed-cite { font-family: var(--font-mono); font-size: 12px; color: var(--accent); }
a.ed-link { color: var(--text); text-decoration: none; transition: color 0.15s linear; }   /* §6 color timing */
a.ed-link:hover { color: var(--accent); }                                                    /* §1 link hover */
```
5. **Dark bookends.** The dark stage returns as the closing CTA, so the page reads stage → daylight → stage (§1 Dark/Light Section Contrast: "CTA / closing: dark background returns").
```css
.ed-closing { background: #161616; color: #DEDEDE; padding: 128px 0; text-align: center; }   /* §3 128px after long content */
```

### Motion personality

The motion is quiet and fast, like a page that answers instead of performs.
- **Fits**: §1.5 **C Typing caret** (hero, the default: it shows the product being asked), **A Rows stream in** (sources or results arriving), and **D Toast** (an answer is ready). Avoid B Cursor click in the hero: the panel is an input, not a button-driven UI.
- **Timing**: hover `transform 0.15s ease-out`; color/opacity `0.15s linear`; card lift `0.2s ease-in-out`; entrance `0.8s cubic-bezier(0.16, 1, 0.3, 1)` (all §6). Typing uses the 2000ms counter duration (interaction-patterns §1). Everything plays once.
- **Hover**: the CTA moves `translateY(-1px)` with `brightness(1.1)`; outline buttons darken their border; links go teal. Static cards do **not** lift. Only `.card-floating` (interactive) gets the `-4px` lift.
- **Never moves**: serif headings (no word-by-word reveal; the claim is a printed statement), the hero panel's glow (no pulse), section backgrounds, and the nav.

### Preferred signature moves

Which layout each section uses by default is set in the master `SKILL.md` Step 4.3 *Style layout defaults* table; the notes below adjust how each move looks in this style.

- **M4 Framed hero stage**, as the default hero above. Editorial row: `.hero-stage` `#161616`, 30px radius, teal CTA. Adjustment: the stage here is full-bleed (DNA "full-bleed dark photographic stage"), not inset. Put the 30px radius on the *panel*, not on the section.
- **M10 Poster quote**: serif `48px` quote, `max-width: 62%`, `.label` attribution. It is bold only on the closing dark stage (Editorial allows `dark` for closing sections only). Otherwise use it on `alt` as a non-bold layout. No decorative quote glyph and no teal.
- **M7 Big-type list band**: on `alt` mid-page, rows in `--font-body` 24px at opacity 0.6 → 1 on hover (`0.15s linear`, §6, replacing the Minimal 0.3s), with `1px solid var(--surface-2)` rules.
- **M1 Edge-to-edge headline**: only for manifesto, About, or 404 Brand Moment pages. Cormorant at 400. The serif at this size is the effect.

### Drift guard

Forbidden, because these turn the page into another style:
- **→ Minimal**: a black (`var(--text)`) primary button, 2px radii, zero shadow everywhere including the hero panel, or 180px section rhythm. Editorial's button is a teal pill and its rhythm is 96–120px.
- **→ Business**: soft blue-gray shadows on every card, all-sans headings, a 48px rounded product-stage panel, or a light hero with a brand-gradient mat.
- **→ Colorful**: pastel scene backgrounds, inset `.scene` hero panels with margin, Playfair, paper-weight four-layer shadows, or more than one tinted band.
- **→ Generic AI**: a teal or purple gradient behind the hero, glow behind the headline text, perspective grids, gradient serif text, teal headings or icon tiles, a word-by-word headline reveal, a fake photo, or a dark band mid-page (dark is for the hero and the closing only).

### Screenshot test

1. **Stage → daylight → stage**: the top roughly 900px is near-black with one teal-ringed rounded panel, the body is warm off-white, and (if there is a closing CTA) the bottom returns to near-black. No other dark band appears.
2. **Serif claims, sans mechanics**: every hero and section heading is visibly a high-contrast serif, and every card heading and body line is sans; mono uppercase labels sit above the headings.
3. **Teal is a pinprick**: teal appears only on the pill CTAs, the panel ring, citations, and links. Squint, and the page is black, cream, and charcoal with a few small teal points.
