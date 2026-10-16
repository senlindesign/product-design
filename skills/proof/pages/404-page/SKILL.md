# 404 Page Skill

Generate a runnable 404 error page with professional visual quality. No Mobbin or external service required at runtime.

**Visual System**: see `shared/visual-style.md` — defines the default design tokens (colors, typography, spacing, components) for Light and Dark themes. 404-specific component tokens are in `references/`. Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.

---

## When to Use This Skill

Use this Skill when the user asks you to create a 404 page, "page not found" page, or error page for a website or web application. This includes:
- "Make a 404 page for [product]"
- "Create a page-not-found page"
- "Build an error page for my site"
- "Design the 404 for [tool/platform]"

Do NOT use this Skill for:
- Server error pages (500, 502, 503) — different content and recovery actions
- Maintenance / "coming soon" pages — different purpose
- In-app empty states or "no results" screens
- Landing pages, pricing pages, or other standard page types

---

## Workflow

### Step 1: Understand the Task

Gather these inputs from the user's request. Do not ask questions in this step — the master skill decides whether to ask (its Step 1). For each input the user does not give, use the default below; facts that are missing become labeled placeholders.

**Required** (must be clear from request or ask):
- Product name and one-line description

**Use defaults if not provided**:
- Product type → infer from description (SaaS tool, developer platform, creative tool, consumer brand)
- Brand color → **default is the active style's own accent** (Minimal: no brand color, `--accent` = `--text`; Editorial: teal `#20808D`). Only override if user explicitly provides one — see the active style file's Brand Customization section (Minimal: `visual-style.md` §10.1)
- Display font → **default is the active style's display font** (Minimal: DM Sans). Only override if user provides a specific font name — see the active style file's Brand Customization section (Minimal: `visual-style.md` §10.2)
- Technology stack → single HTML file with inline CSS
- Theme → Light (default for most), Dark (for developer tools, dark-brand products)
- Visual strategy → Typographic display numeral (default, see Step 3)
- Recovery destinations → Home only (Archetype A) unless user provides a destination list

**Brief context** (when called from the master skill):

When the master skill passes a project brief (audience, goal, barriers, evidence), use it in archetype selection (Step 2) and section composition (Step 3):
- Product complexity (single app vs. multi-product platform) → whether recovery navigation is needed
- Brand personality (minimal vs. expressive) → visual treatment strategy
- Available assets (logo, product screenshots) → visual treatment options

### Step 2: Select Archetype

Read `references/archetypes.md` and classify the product:

| Signal | Archetype | Default Theme | Core Composition |
|--------|-----------|---------------|------------------|
| Simple product, one main entry point | A. Minimal Redirect | Light | Numeral/heading + body + one button |
| Multi-product platform, docs site, content hub | B. Navigational Recovery | Light | Error message + destination list/cards/search |
| Design-driven brand, creative tool, strong personality | C. Brand Moment | Light or Dark | Giant visual/type + minimal copy + button |

The archetype determines: visual strategy, content amount, layout (viewport-fill vs scrollable), and recovery mechanism.

**Default: A** (Minimal Redirect). Choose B or C only when the product clearly fits.

**Brief-informed selection**: When a project brief is available, apply these rules. When a rule matches, it takes priority over the signal table above:
- Brief indicates multi-product platform or documentation site → B. Navigational Recovery (users need help finding the right section)
- Brief indicates strong brand personality or creative identity → C. Brand Moment
- Brief indicates minimal, utility-focused product → A. Minimal Redirect (default)

### Step 3: Compose Page Elements

A 404 page is a **single content block**, not a section stack. Read `references/section-composition.md` for layout rules.

**Always include**:
1. Navigation (reuse standard nav — user's primary escape route)
2. Error content block (numeral/heading/body/button — see below)

**Include by archetype**:
- A: one button ("Go home"). Optional: display numeral or watermark
- B: destination list, cards, or search. Optional: small label above heading
- C: giant visual element (typographic numeral, oversized heading, or product reference)

**Optional**:
- Footer (default yes; below the fold for viewport-fill layouts)

**Do NOT include**:
- Multiple stacked sections (Features, Social Proof, CTA, FAQ)
- Newsletter signup, testimonials, pricing teaser
- Status page or uptime indicators (404 ≠ service outage)

**Brief-informed visual strategy**: If the user provides a product illustration, use Product-content reference. If the user provides only a logo, use Brand-mark manipulation. If the user provides no assets, use the Typographic display numeral.

**Visual strategy** (read `references/visual-treatment.md`):

| Strategy | Best when | Requires user assets? |
|----------|-----------|-----------------------|
| Typographic display numeral (default) | Any archetype, no user assets | No |
| Oversized heading | C, short heading (1–3 words) | No |
| Nothing / whitespace | Ultra-minimal A | No |
| Product-content reference | C, user describes product output | User provides description |
| Brand-mark manipulation | C, user provides logo | User provides logo |

### Step 4: Generate Page Spec

Before writing code, produce a brief spec:

```
Page Spec:
- Product: [name] — [one-line description]
- Archetype: [A/B/C] — [name]
- Theme: Light / Dark
- Visual strategy: [typographic numeral / oversized heading / nothing / product reference / brand mark]
- Numeral presentation: [display / low-contrast / watermark / label / none]
- Heading: "[text]" — tone: [literal / apologetic / humorous]
- Recovery: [button to home / button + destination list / inline links]
- Destinations (B only): [list of suggested pages]
- Brand color: none (default) / [color] — --accent set to [value]
- Display font: default (DM Sans) / [font name]
- Not in scope: [real navigation, form submission, etc.]
```

### Step 5: Build the Page

**First**: Read the active style file in full — `shared/visual-style.md` (Minimal, the default), or `shared/visual-style-business.md` / `shared/visual-style-colorful.md` / `shared/visual-style-editorial.md` when the master skill selected another style. Every CSS value must come from its tokens.

Then implement the page following the spec:

1. Read `references/error-display.md` for numeral, heading, body copy tokens
2. Read `references/recovery-actions.md` for button, link, destination tokens
3. Read `references/visual-treatment.md` for visual strategy implementation
4. Check against `references/anti-patterns.md` — verify each design choice

> **The token blocks below are Minimal defaults.** With another style active, apply *Style precedence* from the master `SKILL.md`: visual values (fonts, weights, colors, radius, shadow, spacing rhythm, button and card styling) come from the active style file; layout, structure, and content rules here still apply.

**Design System Tokens (must follow)**:

```
Fonts:     var(--font-display) default DM Sans + var(--font-mono) default DM Mono + system sans (body)
Weights:   500 (display/nav/button) + 400 (mono/body) — no other weights
Colors:    Light: #FFF / #F5F5F5 / #E9E9E9 / #141414
           Dark:  #0A0A0A / #141414 / #1F1F1F / #EDEDED
           Text hierarchy via opacity (1 / 0.5 / 0.4 / 0.3 / 0.15), NOT different grays
Accent:    var(--accent) default = var(--text) + var(--accent-text) default = var(--text-inverse)
Nav:       --nav-h: 68px; body { padding-top: var(--nav-h); } for fixed nav
Radius:    Buttons 2px, inputs 4px, feature cards 8px, content cards 16px
Shadows:   ZERO — depth via background color steps only
Transitions: transform 0.2s ease-in-out (hover), opacity 0.3s linear
Motion:      optional heading text reveal only — no scroll/stagger (see shared/interaction-patterns.md)
Grid:      max-width 1080px, padding 0 32px
```

**404-specific tokens**:

```
Viewport fill:     min-height: calc(100vh - var(--nav-h))
                   display: flex; align-items: center; justify-content: center
                   padding: 0 32px
Content max-width: 540px (system subtitle measure) for A/C centered
                   1080px (system container) for B with cards/list

Display numeral:   font: var(--font-display) / 500 / -0.02em / line-height 1
                   size: clamp(120px, 20vw, 200px)
                   color: var(--text)
                   Full contrast: opacity 1 (sole focal point, no heading alongside)
                   Low contrast:  opacity 0.10–0.15 (alongside a heading)
                   Watermark:     opacity 0.08 / position absolute / z-index 0

Mono numeral:      font: var(--font-mono) / 400 / +0.72px / line-height 1
                   size: clamp(120px, 20vw, 200px)
                   color: var(--text)

Heading:           clamp(32px, 4vw, 47px) / 500 / -0.02em / 1.1 (default, section scale)
                   clamp(64px, 12vw, 200px) / 500 / -0.02em / 1 (C oversized)

Body:              18px / 400 / 1.6 / var(--font-body) / opacity 0.5
                   max-width: 540px

Label:             12px / mono / 400 / +0.72px / uppercase / opacity 0.4

Content block spacing (internal, NOT section rhythm):
  Label/numeral → heading:  16px (24px if numeral ≥ 80px)
  Heading → body:           16px
  Body → action:            32px

Two-column split:  display: flex; gap: 58px; each column flex: 1
                   max-width: 1080px; padding: 0 32px
                   < 768px: flex-direction: column

Button:            .btn-dark (8px 16px / 14px / 500 / 2px radius / var(--accent))
Outline button:    .btn-outline (8px 16px / 14px / 500 / 2px / transparent + border)
Button group gap:  16px

Destination list row: padding 16px 0 / border 1px solid var(--surface-2)
                      title: 16px / 500 / var(--text) / opacity 1
                      desc: 14px / 400 / opacity 0.5 / margin-top 6px
                      arrow: opacity 0.4 / margin-left 24px
                      hover: border-color var(--text) / transition: border-color 0.3s linear
                      (do NOT apply row-level opacity — individual element opacities already handle hierarchy)

Destination card:  .card token (32px / surface-1 / 8px radius)
                   hover: translateY(-1px)
                   grid: repeat(auto-fit, minmax(240px, 1fr)) / gap 24px

Search input:      border: 1px solid var(--surface-2) / radius 4px / bg var(--bg)
                   padding: 8px 16px / font-size: 16px
                   focus: border-color var(--text)
                   max-width: 500px
                   Placeholder: name the product's content types
```

**Implementation principles**:
- Semantic HTML (one h1 — either the heading or the numeral when it replaces the heading)
- Mobile-responsive (flexbox, breakpoint at 767px (`@media (max-width: 767px)`))
- Single HTML file with inline `<style>` — include Google Fonts link for DM Sans + DM Mono
- No real navigation targets — links use `href="#"` or descriptive placeholders
- Interactive states: hover `translateY(-1px)` on buttons, `opacity` transition on links
- Focus states: `outline: 2px solid var(--text); outline-offset: 2px` (system `:focus-visible`)
- Nav buttons must use explicit overrides if placed inside `.nav-links` (see `shared/navigation.md` CSS specificity section)
- **No JavaScript required** — 404 pages have no interactive state

**Content handling**:
- Use the user's real content when provided (product name, nav links, destination URLs)
- Generate example content when not provided, clearly noting it's placeholder
- Default heading: "Page not found" (literal tone)
- Default body: "The page you're looking for doesn't exist or has been moved." (one sentence)
- Default button: "Go home"
- Humor only when the product domain provides a natural angle — never fabricate puns
- Never fabricate request paths, server names, or stack traces

### Step 6: Verify

After generating the page, run through `shared/quality-checklist.md`. Focus on these critical items:

> Visual checks below (color, shadow, radius, typography, spacing values) are written for Minimal. With another style active, check them against the active style file instead. Visual rules in `references/anti-patterns.md` follow the same precedence; content and structure rules apply in every style.

1. **Color**: Zero hue-tinted grays? CTA uses `var(--accent)`? Chromatic area < 10%?
2. **Shadows**: Zero box-shadow anywhere?
3. **Typography**: Labels in mono/uppercase? Weight 500 dominant? Heading tracking negative?
4. **Radius**: Buttons 2px? Input 4px (if search present)?
5. **Anti-patterns**: No illustration? No pill button? No gradient numeral? No decorative border?
6. **Responsive**: Content readable at 767px? Columns stack? Numeral scales down?
7. **Animation**: `prefers-reduced-motion` guard if text reveal used? No scroll reveal (single viewport block)?

**404-specific checks**:
7. **Navigation present**: Full site nav visible?
8. **Recovery action exists**: At least one button or link back to a real destination?
9. **Numeral hierarchy**: If numeral and heading coexist, is the numeral at reduced opacity (0.10–0.15)?
10. **No competing focal points**: Only one element at full contrast as the visual lead?
11. **Viewport-fill layout**: Content vertically centered (A/C)? min-height calc correct?
12. **No fabricated content**: No fake URLs, server names, or stack traces?
13. **Button copy specific**: Not generic "Submit"? Matches the likely audience action?

If issues are found, fix them before delivering.

### Step 7: Deliver

Provide:
1. The page file(s) with instructions to open/run
2. A brief note on key design decisions (2–3 sentences): archetype chosen, visual strategy, heading tone
3. What's in scope (visual presentation) vs. not implemented (real navigation, form submission)

---

## Knowledge Files

| File | Content | When to Load |
|------|---------|-------------|
| `shared/visual-style.md` | **Design system**: default tokens, Light/Dark themes, component styles, brand customization rules | Step 5 (always — read FIRST) |
| `references/archetypes.md` | 3 archetypes (A Minimal / B Recovery / C Brand), selection guide, cross-archetype rules | Step 2 (always) |
| `references/error-display.md` | Numeral tokens (display, mono, watermark, label), heading (tone, size, copy), body copy | Step 5 (always) |
| `references/recovery-actions.md` | Button tokens, text links, search input, destination list/cards/inline links, copy variants | Step 5 (always) |
| `references/visual-treatment.md` | 5 visual strategies (numeral, oversized heading, nothing, product reference, brand mark), selection guide | Step 3 + Step 5 |
| `references/section-composition.md` | Viewport-fill layout, nav/footer rules, content width, internal spacing, two-column split, background colors | Step 3 (always) |
| `references/anti-patterns.md` | 12 anti-patterns, brand color reconciliation, 12-item verification checklist | Step 5 (always) |
| `shared/navigation.md` | Nav layout, CSS specificity trap for nav buttons | Step 5 (always) |
| `shared/footer.md` | Footer layout and content | Step 5 (when footer included) |
| `shared/quality-checklist.md` | verification checklist | Step 6 (always) |
| `shared/interaction-patterns.md` | Motion tokens: scroll reveal, stagger, counter, hover lift recipes | Step 5 (optional — 404 uses minimal motion) |

---

## Constraints

- This Skill does NOT require Mobbin, external APIs, or internet access
- V1 scope: page skeleton + layout + visual quality
- NOT in V1: real navigation targets, form submission, route detection, redirect logic
- Output: runnable frontend code (HTML/CSS, or matching the user's project stack)
- All design knowledge is pre-distilled in the references/ directory
- Visual style defaults to the shared design system tokens; user-provided brand specs override only `--accent` / `--accent-text` and `--font-display`
- No JavaScript required — 404 pages are static content
- Navigation links in examples use `href="#"` — no real routing
