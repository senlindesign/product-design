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
4. **Depth reserved for the product** — Depth concentrates on the product itself: the hero's paper window on the dark stage, and floating surfaces that can act. Static content (pricing cards, feature descriptions) has no shadow; it is ruled with hairlines instead.

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
Logo wall:            opacity: 0.45
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
Logo wall:            opacity: 0.45
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
- ✅ Citation numerals and source numbers inside a product mock (they are links)
- ✅ Link hover color (optional)
- ✅ Status badge background (functional only, e.g., "Available" / "Online")
- ❌ Section backgrounds, even at low opacity
- ❌ Heading color or gradient text
- ❌ Icon backgrounds or badge fills
- ❌ Glows, glow rings, or tinted shadows of any kind

### Dark/Light Section Contrast (Editorial Pattern)

The Editorial preset often uses a **dark entry + light body** structure:

```
Entry (hero):     dark background (--bg = #161616 on dark theme, or a local dark override on light theme)
Body:             light canvas (--bg = #FAF8F5 on light theme), feature sections alternating --bg / --surface-1
Mid-page band:    ONE dark band (#161616) in the middle of the body — the proof (M17 / M10) or one
                  feature showcase — so the page reads dark → light → dark → light → dark
CTA / closing:    dark background returns (creates a framing effect)
```

**Why a mid-page band.** With dark only at the two ends, everything between them is one long light run and the rhythm goes flat (maintainer review, 2026-10-14). Editorial-tech sites break the light body once with a dark chapter: Craft's "Touch to feel the difference" band in an otherwise light page, FLORA's dark admin section. Rules: exactly one mid-page dark band; never adjacent to the hero or the closing stage (at least one light section on each side); same tokens as the stage (`#161616`, text `#DEDEDE`, cards `#1A1918` with `1px solid #2A2826`); teal stays a pinprick.

```css
.ed-band { background: #161616; color: #DEDEDE; }                                  /* the stage tokens, mid-page */
.ed-band .label { color: #DEDEDE; }
.ed-band .card-static, .ed-band .quote { background: #1A1918; border-color: #2A2826; }   /* §1 Dark --surface-1 / --surface-2 */
.ed-band .pv-mat { background: #1A1918; border-color: #2A2826; }
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
Front-page hero:  clamp(56px, 6.2vw, 96px)   weight: 400   tracking: -0.02em   line-height: 1.0   (the Style Signature hero masthead)
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
Search panel:    30px   (a search or ask input when it is the centerpiece of a product mock)
Product stage:   22px   (large content containers, outer cards)
Panel:           16px   (mid-level content panels, feature cards)
Inner UI:        14px   (nested windows, inner content frames)
Compact UI:      10px   (small cards, pricing cards — Perplexity's pricing card radius)
Control:         8px    (inputs, small surfaces)
Pill:            9999px (all CTA buttons — Perplexity uses pill actions)
```

**Nested radius rule**: `22px` product stage / hero window → `14px` inner UI → `8px` control. A `30px` search panel nests a `22px` floating surface. Each nesting level steps one size smaller.

**Note**: Like Colorful, Editorial uses pill buttons (`9999px`). The rounded-biological geometry is consistent with the teal accent philosophy — approachable and direct.

---

## 5. Shadow System

**Interactive surfaces and floating elements use layered shadows. Static content cards use no shadow.**

Shadow depth marks the product. Pricing cards and feature cards (passive) have no shadow. The hero's paper window has the deepest shadow.

### Stage Window Shadow (highest elevation — the hero window on the dark stage)

```css
.ed-window {
    box-shadow:
        0 0 0 1px rgba(255, 255, 255, 0.06),   /* hairline edge against #161616 */
        0 32px 80px rgba(0, 0, 0, 0.45);       /* the window sits above the stage */
}
```

No tinted or glowing shadows anywhere: the earlier teal-glow hero panel read as a stock AI template and has been removed.

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
/* A page that opens on the dark stage (the Style Signature hero) uses the stage's nav in either theme,
   so the first screen is one dark piece instead of a cream bar on black (Grok, Perplexity). */
body:has(.ed-stage) nav { background: rgba(22, 22, 22, 0.88); }
body:has(.ed-stage) nav a { color: #DEDEDE; }
body:has(.ed-stage) nav a.btn-dark { color: var(--accent-text); }
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
Dark sections:         #161616             The "stage" — the hero, ONE mid-page band, and the closing section
                                           (on a light-theme page too: the dark bands are the rhythm)

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
3. Replace the teal everywhere it appears as a signal: CTA, citation numerals, link hover, focus outline


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

Editorial reads like a front page that happens to have a working product on it. There is one dark stage, then daylight. The page opens on `#161616`, where a large serif claim is set like a front-page headline above one paper window of the product, and everything after that resolves to warm paper (`#FAF8F5`). That split comes from the DNA decision "Stage the promise, daylight the proof" (perplexity.ai.md, Taste DNA: the first 900px viewport is dominated by `#161616`/`#1A1918`, and the mid-page and footer go to `#FDFBFB`/`#FAF8F5`). Three voices do the hierarchy work instead of color: the serif makes claims, the sans explains mechanics, and the mono labels evidence ("Editorial Authority Over Dashboard Familiarity"). Teal is rare enough to mean "act" (DNA: about 0.1–0.2% of the sampled area). Depth goes only to the product. The result is authored and calm: dense information, few colors, and one bright paper object on black.

### Hero showcase (mandatory)

**Default hero: the Front Page.** It is a full-bleed `#161616` stage set like a newspaper front page. A masthead row holds the claim on the left (front-page size, two lines, one phrase in Cormorant *italic*) and the subtitle and CTAs on the right, aligned to the claim's last line. A hairline rule closes the masthead. Under it a **paper window** — the product in warm daylight colors (`--bg` `#FAF8F5`), dense and legible, with three columns: navigation · the main object · a **margin column** of evidence. The window is cut by the bottom of the stage. It is the one surface on the page with depth.

- **Why this and not a glowing input.** A lone glowing input box on a black stage is the stock look of AI product templates, and it shows no product. Real editorial-tech heroes show the product as a printed, dense artifact under a set headline: Grok (headline left, subtitle right, product window below in a framed stage), Shopify Editions (serif masthead, product page below), Granola (serif claim, the input surrounded by the user's real notes, never alone). Never build the hero around an input with nothing else in it, and never add a glow ring.
- **Fit the window to the product.** The three columns always mean the same thing; fill them with the product's own nouns (product-visuals.md §6):

  | Product | Left column | Main column | Margin column (evidence) |
  |---|---|---|---|
  | AI / research / search | workspace + saved questions | the question, a full answer with superscript citations, a 3–5 row result table | numbered sources with type, date, page or quote |
  | Inbox / support / CRM | inbox views with counts | one conversation thread: customer message, teammate's internal note, draft reply | customer details, assignee, tags, history |
  | Docs / knowledge | doc tree | the document with one highlighted passage | comments and version history |
  | Analytics / finance | report list | a chart + 5-row table, one row focused | definitions, filters, data freshness |
  | Developer tool | file tree | code with one focused line (Recipe 6 content, light) | PR checks, reviewers, deploy log |

- **Composition**: masthead grid `7fr 4fr`, 64px column gap (§7 gutter). Claim at the §2 front-page size; subtitle at the §7 560px measure. The window starts 64px below the rule and at 50–65% of a 1440 × 900 fold. Margin column 260px (§7 margin column), left column 18%.
- **Background**: flat `#161616`. A user-supplied photo may sit under it; never generate or fake one. No gradient, no glow, no grid behind the text.
- **Color**: teal appears only on the CTA, the citation numerals, and source numbers. Status data inside the window uses the product-visuals §2.1 mock colors.
- **Entrance motion**: the masthead is static (a printed statement). Inside the window, one §1.5 cue: **A Rows stream in** on the result table or thread, or **C Typing caret** on the question line. The HTML holds the final state.

```html
<section data-section="hero" data-layout="full-bleed" data-bg="dark" data-bold="true" class="ed-stage">
  <div class="ed-stage-inner">
    <div class="ed-masthead">
      <div>
        <p class="label">Research assistant for procurement</p>
        <h1 class="ed-claim">Answers your supplier data <em>can back up.</em></h1>
      </div>
      <div>
        <p class="ed-sub">Ledger reads your contracts, invoices and supplier emails, then answers questions about them with a source for every line.</p>
        <div class="ed-ctas">
          <a href="#" class="btn-dark">Try it free</a>
          <a href="#" class="btn-outline">See a sample answer</a>
        </div>
      </div>
    </div>

    <div class="pv ed-window" data-mock role="img" aria-label="Ledger answering which suppliers raised prices, with cited sources">
      <aside class="ed-side">
        <div class="ed-ws"><i></i>Halden Foods</div>
        <a class="is-on">Ask</a><a>Suppliers <span class="pv-muted">41</span></a><a>Contracts <span class="pv-muted">118</span></a><a>Invoices</a>
        <p class="label ed-group">Recent</p>
        <a>Q3 freight surcharges</a><a>Renewals before Mar 14</a><a>Packaging spend by site</a>
      </aside>
      <div class="ed-main">
        <p class="label">Ask · Today 09:42</p>
        <p class="ed-q"><span data-type>Which suppliers raised prices after the March tariff change?</span></p>
        <p class="ed-ans">Three of your eleven steel and packaging suppliers raised list prices within 30 days of the change<sup>1</sup>. Corvo Packaging tied its increase to the tariff by name<sup>2</sup>; the other two cite energy costs<sup>3</sup>.</p>
        <div class="ed-table">
          <div class="ed-tr" data-stream><span>Halvard Steel</span><span class="pv-mono is-neg">+6.2%</span><span class="pv-mono pv-muted">Mar 19</span><span class="ed-num">1</span></div>
          <div class="ed-tr is-focused" data-stream><span>Corvo Packaging</span><span class="pv-mono is-neg">+4.0%</span><span class="pv-mono pv-muted">Mar 22</span><span class="ed-num">2</span></div>
          <div class="ed-tr" data-stream><span>Northline Freight</span><span class="pv-mono is-neg">+2.5%</span><span class="pv-mono pv-muted">Apr 2</span><span class="ed-num">3</span></div>
        </div>
      </div>
      <aside class="ed-margin">
        <p class="label">Sources · 14</p>
        <div class="ed-src"><b>1</b><p><strong>Price notice — Halvard Steel</strong><span class="pv-muted">PDF · Mar 19 · p. 2</span></p></div>
        <div class="ed-src"><b>2</b><p><strong>Email from Ana Corvo</strong><span class="pv-muted">“…in line with the new tariff schedule.”</span></p></div>
        <div class="ed-src"><b>3</b><p><strong>Invoice #INV-20417</strong><span class="pv-muted">Northline · Apr 2</span></p></div>
        <div class="ed-src pv-muted"><b>4</b><p><strong>Master agreement 2024</strong><span>Clause 7.3 · price review</span></p></div>
      </aside>
    </div>
  </div>
</section>
```

```css
.ed-stage {
    background: #161616; color: #DEDEDE;     /* §1 Dark Theme --bg / --text: the stage */
    padding-top: 128px;                      /* §3 hero top whitespace */
    padding-bottom: 0;                       /* the window is cut by the stage edge */
    overflow: hidden;
}
.ed-stage-inner { max-width: 1440px; margin: 0 auto; padding: 0 64px; }   /* §7 main grid */
.ed-stage > .ed-stage-inner > .ed-masthead .label { color: #DEDEDE; }      /* masthead label only, not the window's */
.ed-masthead {
    display: grid; grid-template-columns: minmax(0, 7fr) minmax(0, 4fr);
    column-gap: 64px; align-items: end;      /* §7 grid gutter; subtitle sits on the claim's baseline row */
    padding-bottom: 48px;                    /* §3 heading to content */
    border-bottom: 1px solid #2A2826;        /* §1 Dark --surface-2: the masthead rule */
}
.ed-claim {
    font-family: var(--font-display);
    font-size: clamp(56px, 6.2vw, 96px); font-weight: 400;   /* §2 front-page hero */
    letter-spacing: -0.02em; line-height: 1.0;
    margin: 24px 0 0;
}
.ed-claim em { font-style: italic; }         /* one phrase only (M2, Editorial row) */
.ed-sub { font-size: 16px; line-height: 1.6; opacity: 0.6; max-width: 560px; margin: 0; }  /* §2 body, §1 subtitle, §7 measure */
.ed-ctas { display: flex; gap: 16px; margin-top: 32px; }
.ed-stage .btn-outline { color: #DEDEDE; border-color: #2A2826; }
.ed-stage .btn-outline:hover { border-color: #DEDEDE; }

/* The paper window: light Editorial tokens inside the dark stage */
.ed-window {
    --bg: #FAF8F5; --surface-1: #FDFBFB; --surface-2: #E8E4DF; --text: #27251E;   /* §1 Light Theme, scoped */
    margin-top: 64px;                        /* §3 scale */
    height: 540px;                           /* Recipe 1 crop at 60% of a 900px fold; px, not vh — vh breaks on tall or short screens */
    display: grid; grid-template-columns: 18% minmax(0, 1fr) 260px;   /* §7 margin column */
    background: var(--bg); color: var(--text);
    border-radius: 22px 22px 0 0;            /* §4 product stage */
    box-shadow: 0 0 0 1px rgba(255,255,255,.06), 0 32px 80px rgba(0,0,0,.45);  /* §5 Stage Window Shadow */
    overflow: hidden; font-size: 13px;       /* product-visuals §3 mock text */
    -webkit-mask-image: linear-gradient(to bottom, #000 calc(100% - 56px), transparent); mask-image: linear-gradient(to bottom, #000 calc(100% - 56px), transparent);   /* product-visuals .pv-cut: the stage edge dissolves the window */
}
.ed-window .label { color: var(--text); }    /* window labels use the light text, not the stage's */
.ed-side { padding: 24px 16px; border-right: 1px solid var(--surface-2); display: grid; align-content: start; gap: 2px; }
.ed-ws { display: flex; gap: 8px; align-items: center; font-weight: 500; font-size: 14px; margin-bottom: 16px; }
.ed-ws i { width: 20px; height: 20px; border-radius: 8px; background: var(--text); }   /* §4 control */
.ed-side a { display: flex; justify-content: space-between; padding: 6px 8px; border-radius: 8px; opacity: 0.6; }
.ed-side a.is-on { background: var(--surface-2); opacity: 1; }
.ed-group { margin: 16px 8px 6px; }
.ed-main { padding: 32px 48px; overflow: hidden; }
.ed-q { font-size: 20px; font-weight: 500; line-height: 1.3; margin: 12px 0 16px; max-width: 560px; }  /* §2 card heading */
.ed-ans { font-size: 16px; line-height: 1.6; max-width: 600px; margin: 0; }                            /* §2 body */
.ed-ans sup, .ed-num, .ed-src b { font-family: var(--font-mono); font-size: 12px; color: var(--accent); }  /* §1: citations are links */
.ed-table { margin-top: 16px; max-width: 600px; border-top: 1px solid var(--surface-2); }
.ed-tr { display: grid; grid-template-columns: 1fr 80px 80px 24px; gap: 12px; align-items: center; min-height: 32px; border-bottom: 1px solid var(--surface-2); }
.ed-tr.is-focused { background: var(--surface-2); margin: 0 -8px; padding: 0 8px; border-radius: 8px; }
.is-neg { color: var(--mock-negative); }     /* product-visuals §2.1 */
.ed-margin { padding: 32px 24px; border-left: 1px solid var(--surface-2); display: grid; align-content: start; gap: 16px; }
.ed-src { display: grid; grid-template-columns: 24px 1fr; gap: 8px; }
.ed-src p { margin: 0; line-height: 1.45; } .ed-src strong { display: block; font-weight: 500; }

@media (max-width: 767px) {
    .ed-stage { padding-top: 80px; }                          /* §3 narrow: 128 → 80 */
    .ed-stage-inner { padding: 0 20px; }
    .ed-masthead { grid-template-columns: 1fr; row-gap: 24px; padding-bottom: 32px; }
    .ed-claim { font-size: 48px; }                            /* §2 narrow hero */
    .ed-window { grid-template-columns: 1fr; margin-top: 32px; height: 480px; }
    .ed-side, .ed-margin { display: none; }                   /* keep the main column */
    .ed-main { padding: 24px 20px; }
    .ed-tr { grid-template-columns: 1fr 64px 24px; } .ed-tr > :nth-child(3) { display: none; }
}
```

Motion: copy the §1.5 shared trigger and recipe A (or C) from `shared/interaction-patterns.md` unchanged. Under reduced motion everything is already in its final state.

**Dark-theme page**: the stage *is* the page `--bg` (`#161616`), so give the section after it `data-bg="alt"` (`var(--surface-1)` `#1A1918`) with a `1px solid var(--surface-2)` top border, so the stage→proof turn stays visible. The window keeps its scoped light tokens in both themes: daylight inside the stage is the point. On a light-theme page, the hardcoded `#161616`/`#DEDEDE`/`#2A2826` above are the local dark override (§1 Dark/Light Section Contrast).

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
5. **Dark bookends.** The dark stage returns as the closing CTA, with one dark band mid-page, so the page reads stage → daylight → band → daylight → stage (§1 Dark/Light Section Contrast).
```css
.ed-closing { background: #161616; color: #DEDEDE; padding: 128px 0; text-align: center; }   /* §3 128px after long content */
```

### Motion personality

The motion is quiet and fast, like a page that answers instead of performs.
- **Fits**: §1.5 **A Rows stream in** (results, sources, or a thread arriving in the hero window — the default), **C Typing caret** (the question line, for ask/search products), and **D Toast** (an answer is ready, in feature mocks). Avoid B Cursor click in the hero: the window is read, not clicked.
- **Timing**: hover `transform 0.15s ease-out`; color/opacity `0.15s linear`; card lift `0.2s ease-in-out`; entrance `0.8s cubic-bezier(0.16, 1, 0.3, 1)` (all §6). Typing uses the 2000ms counter duration (interaction-patterns §1). Everything plays once.
- **Hover**: the CTA moves `translateY(-1px)` with `brightness(1.1)`; outline buttons darken their border; links go teal. Static cards do **not** lift. Only `.card-floating` (interactive) gets the `-4px` lift.
- **Never moves**: serif headings (no word-by-word reveal; the claim is a printed statement), the hero window (no float or tilt), section backgrounds, and the nav.

### Preferred signature moves

Which layout each section uses by default is set in the master `SKILL.md` Step 4.3 *Style layout defaults* table; the notes below adjust how each move looks in this style.

- **M4 Framed hero stage + M3 Product rising from the fold**, as the default hero above. Editorial row: full-bleed `#161616` stage (DNA "full-bleed dark photographic stage"), a light paper window with the 22px product-stage radius cut by the stage bottom, teal CTA.
- **M10 Poster quote**: serif `48px` quote, `max-width: 62%`, `.label` attribution. Bold on the mid-page dark band (`.ed-band`, the default home for social proof) or the closing stage; otherwise on `alt` as a non-bold layout. No decorative quote glyph and no teal.
- **M7 Big-type list band**: on `alt` mid-page, rows in `--font-body` 24px at opacity 0.6 → 1 on hover (`0.15s linear`, §6, replacing the Minimal 0.3s), with `1px solid var(--surface-2)` rules.
- **M1 Edge-to-edge headline**: only for manifesto, About, or 404 Brand Moment pages. Cormorant at 400. The serif at this size is the effect.

### Drift guard

Forbidden, because these turn the page into another style:
- **→ Minimal**: a black (`var(--text)`) primary button, 2px radii, zero shadow everywhere including the hero window, or 180px section rhythm. Editorial's button is a teal pill and its rhythm is 96–120px.
- **→ Business**: soft blue-gray shadows on every card, all-sans headings, a 48px rounded product-stage panel, or a light hero with a brand-gradient mat.
- **→ Colorful**: pastel scene backgrounds, inset `.scene` hero panels with margin, Playfair, paper-weight four-layer shadows, or more than one tinted band.
- **→ Generic AI**: a lone input box as the hero visual, a glowing ring or teal shadow around any panel, everything centered in one column, a teal or purple gradient behind the hero, glow behind the headline text, perspective grids, gradient serif text, teal headings or icon tiles, a word-by-word headline reveal, a fake photo, or more than one dark band mid-page (one band, not stripes).

### Screenshot test

1. **Stage → daylight → stage**: the top roughly 900px is near-black with a left-set serif masthead, a hairline rule, and a warm paper product window cut by the stage's bottom edge (dense, legible, three columns); the body is warm off-white with **one** near-black band in the middle, and (if there is a closing CTA) the bottom returns to near-black: dark → light → dark → light → dark.
2. **Serif claims, sans mechanics**: every hero and section heading is visibly a high-contrast serif, and every card heading and body line is sans; mono uppercase labels sit above the headings.
3. **Teal is a pinprick**: teal appears only on the pill CTAs, the panel ring, citations, and links. Squint, and the page is black, cream, and charcoal with a few small teal points.
