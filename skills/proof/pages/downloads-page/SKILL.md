# Downloads Page Skill

Generate a runnable Downloads / "Get the App" page with professional visual quality. No Mobbin or external service required at runtime.

**Visual System**: see `shared/visual-style.md` — defines the default design tokens (colors, typography, spacing, components) for Light and Dark themes. Downloads-specific component tokens are in `references/`. Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.

---

## When to Use This Skill

Use this Skill when the user asks you to create a downloads page, "get the app" page, or software distribution page. This includes:
- "Make a downloads page for [product]"
- "Create a page where users can download our app"
- "Build a download page for our CLI tool"
- "Design the /download page for [platform]"

Do NOT use this Skill for:
- Landing pages with a download CTA (use the Landing Page Skill — the download button lives in the hero)
- App store listing pages (those are controlled by Apple/Google, not your site)
- Documentation install guides (those live inside docs, not as a standalone page)
- Changelog or release notes pages (different purpose — use Blog Page Skill or dedicated changelog)

---

## Workflow

### Step 1: Understand the Task

Gather these inputs from the user's request. Do not ask questions in this step — the master skill decides whether to ask (its Step 1). For each input the user does not give, use the default below; facts that are missing become labeled placeholders.

**Required** (must be clear from request or ask):
- Product name and one-line description
- Available platforms (macOS, Windows, Linux, iOS, Android, Web, CLI)

**Use defaults if not provided**:
- Product type → infer from description (desktop app, mobile app, CLI tool, SDK)
- Platform count → determines archetype and layout complexity
- Brand color → **default is the active style's own accent** (Minimal: no brand color, `--accent` = `--text`; Editorial: teal `#20808D`). Only override if user explicitly provides one — see the active style file's Brand Customization section (Minimal: `visual-style.md` §10.1)
- Display font → **default is the active style's display font** (Minimal: DM Sans). Only override if user provides a specific font name — see the active style file's Brand Customization section (Minimal: `visual-style.md` §10.2)
- Technology stack → single HTML file with inline CSS
- Theme → Light (default for most), Dark (for developer tools, dark-brand products)
- Auto-detect OS → yes for Archetype A (default), no for B or C
- System requirements → omit unless user provides them (16/21 products show none)
- Version info → omit unless user provides it (19/21 products show none)

**Brief context** (when called from the master skill):

When the master skill passes a project brief (audience, goal, barriers, evidence), use it in archetype selection (Step 2) and section composition (Step 3):
- Product type (desktop app, CLI tool, SDK, mobile app) → archetype and hero pattern
- Audience (general users vs. developers) → Developer Distribution vs. Platform Selector
- Platform count and priority → layout pattern selection
- Whether install commands are the primary distribution method → Developer Distribution archetype

### Step 2: Select Archetype

Read `references/archetypes.md` and classify the product:

| Signal | Archetype | Default Theme | Core Layout |
|--------|-----------|---------------|-------------|
| Single app, 2+ platforms | A. Platform Selector | Light | Auto-detect CTA + platform list below |
| Multiple distinct apps/tools from one company | B. Multi-Product | Light | Product cards with per-product downloads |
| CLI/SDK installed via terminal command | C. Developer Distribution | Dark | Install command in code block + copy button |

The archetype determines: hero pattern, platform selection UI, content amount, and page length.

**Default: A** (Platform Selector). Choose B or C only when the product clearly fits. See `references/archetypes.md` for the decision matrix.

**Brief-informed selection**: When a project brief is available, apply these rules. When a rule matches, it takes priority over the signal table above:
- Brief indicates developer audience with CLI/terminal workflow → C. Developer Distribution (even if GUI app also exists)
- Brief indicates multiple distinct products → B. Multi-Product
- Brief indicates general consumer audience → A. Platform Selector with auto-detect

### Step 3: Compose Page Elements

Downloads pages are **single-purpose content blocks**, not section stacks. Read `references/section-composition.md` for layout rules.

**Always include**:
1. Navigation (reuse standard nav — `shared/navigation.md`)
2. Hero / Header (product heading + primary download CTA)
3. Footer (reuse standard footer — `shared/footer.md`)

**Include by archetype**:
- **A**: Platform list below hero (buttons, cards, or rows). Optional: separate Mobile section if both desktop and mobile apps exist
- **B**: Product card grid (2-column for primary, 3-column for secondary). Optional: Developer Tools section
- **C**: Install command code block with copy button. Optional: IDE extension section, version archive, feature summary

**Brief-informed additions**:
- Install command block → if brief provides install commands (npm, brew, curl), include regardless of archetype
- IDE/Editor extensions → if brief mentions IDE plugins or extensions, add a secondary section

**Do NOT include**:
- Testimonials, social proof, pricing, feature tours (user has already decided to download)
- Newsletter signup or blog teasers
- Marketing headings like "Get Started" or "Try Free" (use "Download" or "Install")
- Version numbers, file sizes, or system requirements unless the user explicitly provides them — the brief's "available evidence" signal determines this, not agent invention

**Hero pattern** (read `references/download-hero.md`):

| Pattern | Best when | Archetype |
|---------|-----------|-----------|
| Auto-Detect (~60%) | Single app, clear primary platform | A (default) |
| All-Platforms (~25%) | 3-5 platforms, equal importance | A |
| Split (~15%) | CLI + IDE, or product visual alongside | A or C |

### Step 4: Generate Page Spec

Before writing code, produce a brief spec:

```
Page Spec:
- Product: [name] — [one-line description]
- Archetype: [A/B/C] — [name]
- Theme: Light / Dark
- Platforms: [list of platforms]
- Hero pattern: Auto-Detect / All-Platforms / Split
- Auto-detect: yes / no
- Platform selection UI: stacked buttons / card grid / row list / desktop-mobile split
- Brand color: none (default) / [color] — --accent set to [value]
- Display font: default (DM Sans) / [font name]
- Version info: omitted / [version string]
- System requirements: omitted / [requirements]
- Not in scope: [real downloads, file hosting, auto-update, etc.]
```

### Step 5: Build the Page

**First**: Read the active style file in full — `shared/visual-style.md` (Minimal, the default), or `shared/visual-style-business.md` / `shared/visual-style-colorful.md` / `shared/visual-style-editorial.md` when the master skill selected another style. Every CSS value must come from its tokens.

Then implement the page following the spec:

1. Read `references/download-hero.md` for hero pattern tokens
2. Read `references/platform-cards.md` for platform selection UI tokens
3. Read `references/version-info.md` if version/changelog/install commands are needed
4. Read `references/section-composition.md` for layout, spacing, and component patterns
5. Check against `references/anti-patterns.md` — verify each design choice

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
           backdrop-filter: blur(12px) + semi-transparent bg for frosted glass
Radius:    Buttons 2px, inputs 4px, feature cards 8px, content cards 16px
Shadows:   ZERO — depth via background color steps only
Transitions: transform 0.2s ease-in-out (hover), opacity 0.3s linear
Motion:      scroll entrance 0.8s, card stagger 100ms (see shared/interaction-patterns.md)
Grid:      max-width 1080px, padding 0 32px
```

**Downloads-specific tokens**:

```
Content width:     720px centered within 1080px container (for single-column centered layouts)
                   1080px full (for card grids — Archetype B)

Hero spacing:      padding-top: 128px (below fixed nav)
                   padding-bottom: 58px (NOT 180px — platform list is part of hero, not separate section)
                   Narrow: padding-top 80px

Hero heading:      clamp(32px, 4vw, 47px) / 500 / -0.02em / 1.1 (section heading scale, not hero scale)
Hero subtitle:     18px / 400 / 1.6 / opacity 0.5 / max-width 540px / margin-top 24px
Hero CTA:          .btn-dark + .btn-lg (12px 24px / 16px / 500 / 2px radius / var(--accent))
                   margin-top: 48px from subtitle

App icon:          64px × 64px / border-radius 16px / margin-bottom 32px (page-specific token)

Compatibility note: font-family var(--font-mono) / 12px / 400 / +0.72px / uppercase / opacity 0.4
                    margin-top 16px (label style — e.g., "COMPATIBLE WITH APPLE SILICON AND INTEL")

Alt-platform link: 14px / 500 / opacity 0.5 → 1 on hover / margin-top 24px
                   Text: "Not using [OS]? View all download options"

Platform card:     padding 32px / surface-1 / 8px radius / zero shadow
  Icon:            32px × 32px / opacity 0.5
  Name:            20px / 500 / -0.4px tracking / 1.3 line-height (card heading)
  Type label:      12px / mono / 400 / +0.72px / uppercase / opacity 0.4
  Grid:            repeat(auto-fit, minmax(180px, 1fr)) / gap 24px / max-width 720px
  Hover:           translateY(-4px) + border-color var(--surface-2)

Platform row:      padding 16px 0 / border-bottom 1px solid var(--surface-2)
  Name:            16px / 500 (body secondary)
  Arch label:      12px / mono / 400 / +0.72px / uppercase / opacity 0.4
  Download icon:   opacity 0.5 → 1 on hover

Product card (B):  padding 32px / surface-1 / 16px radius (content card)
  Label:           12px / mono / uppercase / opacity 0.4
  Heading:         20px / 500 / -0.4px
  Description:     16px / 500 / 1.6 / opacity 0.5

Install block (C): padding 16px 24px / surface-1 / 8px radius / max-width 540px
  Command:         14px / mono / 400
  Prompt symbol:   opacity 0.4
  Copy button:     icon button / no border / opacity 0.4 → 1 on hover / 16px clipboard SVG

Platform icon:     16px inline in buttons / 32px in cards / 20px in rows
                   Monochrome SVG, color: var(--text) or inherit button text color

Mobile section:    padding-top 128px / padding-bottom 128px (when separated from Desktop)
Footer:            padding-top 128px
```

**Implementation principles**:
- Semantic HTML (one h1 — the page heading)
- Mobile-responsive (flexbox/grid, breakpoint at 767px)
- Single HTML file with inline `<style>` — include Google Fonts link for DM Sans + DM Mono
- Placeholder images: use `var(--surface-1)` background with mono-font label, not broken image links — only for photos or artwork the user must supply. Product screenshots are never a grey box: build them with `shared/product-visuals.md`
- Interactive states: hover `translateY(-1px)` on buttons, `opacity` transition on links
- Focus states: `outline: 2px solid var(--text); outline-offset: 2px` (system `:focus-visible`)
- Entrance animations: scroll reveal on platform sections + card stagger per `shared/interaction-patterns.md` — all wrapped in `prefers-reduced-motion`
- Nav buttons must use explicit overrides if placed inside `.nav-links` (see `shared/navigation.md` CSS specificity section)
- Auto-detect JavaScript: use `navigator.userAgent` / `navigator.platform` to detect OS (see `references/download-hero.md` for implementation)
- Copy button JavaScript: `navigator.clipboard.writeText()` with "Copied" feedback (see `references/version-info.md`)
- Use `padding-top` / `padding-bottom` directional properties, NOT `padding` shorthand, when only overriding one direction on `.container` elements

**Content handling**:
- Use the user's real content when provided (product name, platform list, download URLs, version info)
- Generate example content when not provided, clearly noting it's placeholder
- Default heading: "Download [Product Name]"
- **Never fabricate**: version numbers, file sizes, system requirements, download counts, or testimonials
- Download links use `href="#"` placeholders — note in delivery that real URLs need to be added
- Platform icons: use standard platform SVG icons (Apple, Windows, Linux penguin, etc.) inline in buttons

### Step 6: Verify

After generating the page, run through `shared/quality-checklist.md`. Focus on these critical items:

> Visual checks below (color, shadow, radius, typography, spacing values) are written for Minimal. With another style active, check them against the active style file instead. Visual rules in `references/anti-patterns.md` follow the same precedence; content and structure rules apply in every style.

1. **Color**: Zero hue-tinted grays? CTA uses `var(--accent)`? Chromatic area < 10%?
2. **Shadows**: Zero box-shadow anywhere?
3. **Typography**: Labels in mono/uppercase? Weight 500 dominant? Heading tracking negative?
4. **Radius**: Buttons 2px? Cards 8px? Content cards 16px?
5. **Spacing**: Hero top 128px? Hero bottom 58px (not 180px)? Footer top 128px?
6. **Responsive**: Works at 767px width? Cards collapse to 2 columns? Content readable?
7. **Animation**: `prefers-reduced-motion` guard on all animations? Scroll reveal + card stagger only?

**Downloads-specific checks**:
8. **Auto-detect CTA present** (Archetype A)? Does it show the detected platform?
9. **Escape hatch exists**? "Not using [OS]? View all download options" link below auto-detect CTA?
10. **No marketing content**? No testimonials, feature tours, pricing, or social proof?
11. **Direct heading**? Uses "Download" or "Install" language, not "Get Started" or "Try Free"?
12. **Platform cards uniform**? Same background color, no per-platform gradients or accent colors?
13. **No fabricated metadata**? Version numbers, file sizes, system requirements are user-provided or omitted?
14. **Page complexity matches platform count**? No card grid for 2 platforms, no single button for 6?
15. **No illustrations**? Hero visual is app icon, product screenshot, or absent?

If issues are found, fix them before delivering.

### Step 7: Deliver

Provide:
1. The page file(s) with instructions to open/run
2. A brief note on key design decisions (2-3 sentences): archetype chosen, hero pattern, platform selection UI
3. What's in scope (visual presentation) vs. not implemented (real download hosting, auto-update, file serving)

---

## Knowledge Files

| File | Content | When to Load |
|------|---------|-------------|
| `shared/visual-style.md` | **Design system**: default tokens, Light/Dark themes, component styles, brand customization rules | Step 5 (always — read FIRST) |
| `shared/interaction-patterns.md` | **Motion system**: scroll reveal, card stagger, hover lift recipes | Step 5 (for entrance animations) |
| `references/archetypes.md` | 3 archetypes (A Platform Selector / B Multi-Product / C Developer Distribution), decision matrix | Step 2 (always) |
| `references/section-composition.md` | Section ordering, spacing, component CSS tokens, background rules | Step 3 (always) |
| `references/download-hero.md` | 3 hero patterns (Auto-Detect / All-Platforms / Split), heading tokens, auto-detect JS | Step 5 (always) |
| `references/platform-cards.md` | 4 platform selection patterns (Button List / Card Grid / Row List / Desktop-Mobile Split) | Step 5 (A and B) |
| `references/version-info.md` | Version display, system requirements, changelog, install commands, copy button JS | Step 5 (C, or when user provides version/requirements) |
| `references/anti-patterns.md` | 12 anti-patterns, brand color reconciliation, 15-item verification checklist | Step 5 (always) |
| `shared/quality-checklist.md` | verification checklist | Step 6 (always) |
| `shared/navigation.md` | Navigation component knowledge (CSS specificity, frosted glass, fixed positioning) | Step 5 (always — nav) |
| `shared/footer.md` | Footer component knowledge | Step 5 (always — footer) |

---

## Constraints

- This Skill does NOT require Mobbin, external APIs, or internet access
- V1 scope: page layout + component presentation + visual quality
- NOT in V1: real file hosting, auto-update mechanisms, download tracking analytics, payment gates
- Output: runnable frontend code (HTML/CSS/JS, or matching the user's project stack)
- All design knowledge is pre-distilled in the references/ directory
- Visual style defaults to the shared design system tokens; user-provided brand specs override only the specific values they specify
- Auto-detect OS uses vanilla JavaScript (`navigator.userAgent` / `navigator.platform`)
- Copy-to-clipboard uses vanilla JavaScript (`navigator.clipboard.writeText()`)
- No framework dependency — output is a single HTML file unless the user's project uses a specific framework
