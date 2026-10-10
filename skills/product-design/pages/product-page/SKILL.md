# Product Page Skill

Generate a runnable SaaS Product page with professional visual quality. No Mobbin or external service required at runtime.

**Visual System**: see `shared/visual-style.md` — defines the default design tokens (colors, typography, spacing, components) for Light and Dark themes. Product-specific component tokens (hero video, feature showcase, use cases, integrations) are in `references/`. Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.

---

## When to Use This Skill

Use this Skill when the user asks you to create a product page, product tour page, features page, or platform overview page for a SaaS/software product. This includes:
- "Make a Product page for [product]"
- "Create a features page for [tool]"
- "Build a platform overview page"
- "Design a product tour page for [product]"

Do NOT use this Skill for:
- Landing pages (use Landing Page Skill) — landing = first impression + conversion; product = feature depth + education
- Pricing pages (use Pricing Page Skill)
- About pages (use About Page Skill)
- Contact pages (use Contact Page Skill)
- In-app feature dashboards or settings pages

---

## Workflow

### Step 1: Understand the Task

Gather these inputs from the user's request. Do not ask questions in this step — the master skill decides whether to ask (its Step 1). For each input the user does not give, use the default below; facts that are missing become labeled placeholders.

**Required** (must be clear from request or ask):
- Product name and one-line description
- Feature list (at minimum 3 features with names; descriptions and screenshots optional)

**Use defaults if not provided**:
- Product category / audience → infer from description (SaaS tool, platform, developer tool, etc.)
- Feature count → determines archetype: 5+ features = A, 2-4 deep capabilities = C, platform/infra = B
- Use cases / personas → omit the section if none provided
- Integrations → omit the section if none provided
- Brand color → **default is the active style's own accent** (Minimal: no brand color, `--accent` = `--text`; Editorial: teal `#20808D`). Only override if user explicitly provides one — see the active style file's Brand Customization section (Minimal: `visual-style.md` §10.1)
- Display font → **default is the active style's display font** (Minimal: DM Sans). Only override if user provides a specific font name — see the active style file's Brand Customization section (Minimal: `visual-style.md` §10.2)
- Technology stack → single HTML file with inline CSS
- Theme → Light (default for most), Dark (for developer tools / infrastructure platforms)
- CTA language → "Start free trial" + "Request a demo" (dual CTA default)

**Brief context** (when called from the master skill):

When the master skill passes a project brief (audience, goal, barriers, evidence), use it in archetype selection (Step 2) and section composition (Step 3):
- Audience familiarity with the product category → explanation depth and whether to lead with problem/solution
- Feature count and depth needed → Feature Showcase (breadth) vs. Deep-Dive (depth)
- Whether product is infrastructure/platform → Platform Overview archetype
- Available evidence (screenshots, integration list, use case segments) → which sections are possible

### Step 2: Select Archetype

Read `references/archetypes.md` and classify the product:

| Signal | Archetype | Default Theme | Core Characteristic |
|--------|-----------|---------------|---------------------|
| Product has 5+ features, each demonstrable via screenshot | A. Feature Showcase | Light | Feature grid with screenshots → breadth over depth |
| Product is infrastructure, platform, framework, or API-first | B. Platform Overview | Dark | Capability pillars → architecture → stats → integrations + API |
| Product has 2-4 core capabilities needing deep explanation | C. Product Deep-Dive | Light or Dark | 2-col alternating accordion+screenshot → depth over breadth |

The archetype determines: section composition, hero pattern, feature layout, CTA tone, and whether platform-specific sections (architecture, stats) appear.

**Brief-informed selection**: When a project brief is available, apply these rules. When a rule matches, it takes priority over the signal table above:
- Brief indicates audience needs deep technical explanation of few capabilities → C. Product Deep-Dive (even for products with many features)
- Brief indicates product is API-first or infrastructure → B. Platform Overview
- Brief indicates audience is comparing alternatives → add Comparison section regardless of archetype

### Step 3: Compose Sections

Based on the archetype's section list from `references/section-composition.md`, decide which sections to include. Read the relevant `references/*.md` files for each selected section.

**Minimum sections** (always needed):
1. Navigation
2. Hero (product video/screenshot, heading, dual CTA)
3. Logo wall (trust signal)
4. Feature showcase (grid or deep-dive, depending on archetype)
5. CTA (dual: self-serve + demo)
6. Footer

**Add based on archetype and content**:
- Feature Grid Secondary → Archetype A, when 7+ features (use carousel or second grid section)
- Capability Pillars → Archetype B only (2×3 or 3-col with mono labels)
- Architecture Section → Archetype B only (card-based component layout)
- Platform Stats → Archetype B, when impressive scale numbers exist
- Use Cases → Archetype A or C, when the user names distinct personas or industries
- Integrations → Archetype A (optional), B (required), C (optional)
- Social Proof → All archetypes (optional, shared pattern)
- FAQ → Archetype A and C (optional, shared pattern)
- Use Cases → if brief identifies distinct audience segments or personas, even for Archetype B
- Integrations → if brief mentions integration concerns as a barrier, elevate this section's position
- Social Proof → only if real testimonials, logos, or case studies exist in the brief

**Remove if**:
- User provides no content for that section (use cases without segments, integrations without tools)
- Section would require fabricating product-specific content
- Brief indicates no real customer evidence → skip Social Proof rather than fabricating testimonials
- Brief indicates audience already understands the product (existing users exploring features) → skip problem/solution framing, lead with capabilities

**Do NOT add**:
- Illustrations or conceptual graphics instead of product screenshots (8/11 observations use actual UI screenshots)
- Platform architecture section for non-platform products (these only appear for Archetype B)
- Interactive demo embeds (not in V1 scope)

Check `references/section-composition.md` for ordering rules, spacing, and background color rules.

### Step 4: Generate Page Spec

Before writing code, produce a brief spec:

```
Page Spec:
- Product: [name] — [one-line description]
- Archetype: [A/B/C] — [name]
- Theme: Light / Dark
- Sections (in order): [list]
- Hero pattern: Centered with Video (1) / Text Left + Visual Right (2) / Full-Width Visual (3)
- Feature count: [number] — layout: [grid / accordion-split / carousel]
- Use Cases: [3-4 segments with axis / omitted]
- Integrations: [3-6 featured + API CTA / omitted]
- CTA: dual ("Start free" + "Request a demo") / single (which?)
- Brand color: none (default) / [color] — --accent set to [value]
- Display font: default (DM Sans) / [font name] — tracking: [-0.02em / -0.01em]
- Not in scope: [real form submission, routing, video playback, interactive demos, etc.]
```

### Step 5: Build the Page

**First**: Read the active style file in full — `shared/visual-style.md` (Minimal, the default), or `shared/visual-style-business.md` / `shared/visual-style-colorful.md` / `shared/visual-style-editorial.md` when the master skill selected another style. Every CSS value must come from its tokens.

Then implement the page following the spec. For each section:

1. Read the corresponding `references/*.md` knowledge file for the section type
2. Select the pattern that matches the archetype and content
3. Implement strictly following design system tokens:

> **The token blocks below are Minimal defaults.** With another style active, apply *Style precedence* from the master `SKILL.md`: visual values (fonts, weights, colors, radius, shadow, spacing rhythm, button and card styling) come from the active style file; layout, structure, and content rules here still apply.

**Design System Tokens (must follow)**:

```
Fonts:     var(--font-display) default DM Sans + var(--font-mono) default DM Mono + system sans (body)
           Override: swap --font-display value + update Google Fonts link (see the active style file's Brand Customization section; Minimal §10.2)
Weights:   500 (display/nav/button) + 400 (mono/body) — no other weights
Colors:    Light: #FFF / #F5F5F5 / #E9E9E9 / #141414
           Dark:  #0A0A0A / #141414 / #1F1F1F / #EDEDED
           Text hierarchy via opacity (1 / 0.5 / 0.4 / 0.3 / 0.15), NOT different grays
Accent:    var(--accent) default = var(--text) + var(--accent-text) default = var(--text-inverse)
           Override: set --accent to brand color + calculate --accent-text (see the active style file's Brand Customization section; Minimal §10.1)
Spacing:   Section rhythm 180px, hero top 128px, title-to-content 58px
Radius:    Buttons 2px, feature cards 8px, content cards 16px
Shadows:   ZERO — depth via background color steps only
Transitions: transform 0.2s ease-in-out (hover), opacity 0.3s linear
Motion:      scroll entrance 0.8s, card stagger 100ms, hover lift -4px, counter 2000ms (see shared/interaction-patterns.md)
Grid:      max-width 1080px, gutter 24px, side padding 32px
Nav:       height 68px (var(--nav-h)), fixed positioning needs body padding-top
```

**Product-page-specific tokens**:

```
Hero:
  padding-top: 128px                      (hero top — spacing system)
  heading: clamp(48px, 7vw, 80px) / 500 / -0.02em / 1.05
  subtitle: 18px / 400 / 1.6 / opacity 0.5 / max-width 540px / margin-top 24px
  CTA: btn-lg (16px / 500 / 12px 24px / radius 2px) — NOT standard 14px
  dual CTA gap: 12px, margin-top 48px
  video thumbnail: max-width 960px / border-radius 16px / var(--surface-1) bg
  play button: 48px circle / var(--text) bg / centered / scale(1.05) on hover

Feature Grid (Archetype A):
  grid: repeat(3, 1fr) / gap 24px         (3-col default; 2-col for 4 features; 1fr narrow)
  card: var(--surface-1) bg / 8px radius / 32px padding
  screenshot frame: var(--surface-1) bg / 16px radius / overflow hidden
  card heading: 20px / display / 500 / -0.4px / 1.3
  card description: 16px / body / 400 / 1.6 / opacity 0.5
  "Learn more" link: 14px / display / 500 / arrow after / hover opacity 0.7
  section heading: clamp(32px, 4vw, 47px) / 500 / -0.02em / center / margin-bottom 58px

Feature Deep-Dive (Archetype C):
  2-col split: 1fr 1fr / gap 58px / align-items center
  alternate text/screenshot sides per section
  accordion item: 16px / display / 500 / padding 16px 0 / border-bottom 1px solid var(--surface-2)
  active accordion: opacity 1 (inactive: opacity 0.5)
  screenshot: 16px radius / var(--surface-1) bg / occupies ~55-60% width

Use Cases (Archetype A, optional):
  card grid: repeat(3, 1fr) or repeat(4, 1fr) / gap 24px
  card: var(--surface-1) bg / 8px radius / 32px padding (or transparent, no bg)
  heading: 20px / display / 500
  description: 16px / body / 400 / 1.6 / opacity 0.5
  "Learn more" link: 14px / display / 500 / opacity 0.7 hover
  segment count: 3–4 (use the user's segments when given)

Integrations:
  card grid: repeat(3, 1fr) / gap 24px     (3-col default)
  card: var(--surface-1) bg / 8px radius / 32px padding
  logo: 32px height / natural aspect / full color (NOT grayscale)
  card name: 16px / display / 500
  card description: 16px / body / 400 / 1.6 / opacity 0.5
  "View all" link: centered / 14px / display / 500 / arrow after / opacity 0.7 hover
  API CTA row (Archetype B required): heading + description + .btn-outline

CTA Section:
  heading: clamp(32px, 4vw, 47px) / 500 / -0.02em / 1.1 / center
  subtitle: 18px / body / 400 / 1.6 / opacity 0.5 / max-width 540px / margin 24px auto 0
  buttons: flex / gap 12px / center / margin-top 48px
  dual CTA default: .btn-dark .btn-lg "Start free trial" + .btn-outline .btn-lg "Request a demo"
```

4. Check against `references/anti-patterns.md` — verify each design choice traces back to observation evidence, not AI defaults

**Implementation principles**:
- Semantic HTML (one h1 in the hero, sections, nav, footer)
- Mobile-responsive (flexbox/grid, breakpoint at 767px (`@media (max-width: 767px)`))
- Single HTML file with inline `<style>` — include Google Fonts link for DM Sans + DM Mono
- Placeholder images: the background must step relative to its container — use `var(--surface-2)` inside a `var(--surface-1)` card, or `var(--bg)` inside a `var(--surface-2)` container (same-color nested backgrounds are invisible). Add a mono-font label. For product screenshots specifically, use the Synthetic Product Visual recipe (line below)
- Interactive states: hover `transform: translateY(-1px)` on buttons, `opacity` transition on links
- Nav buttons must use explicit overrides if placed inside `.nav-links` (see `shared/navigation.md` CSS specificity section)
- Video play button: pure CSS triangle using border technique (no icon font dependency)
- Accordion for Archetype C: vanilla JS click handler toggling `.active` class (no framework required)
- **Product screenshots**: Use the Synthetic Product Visual recipe from `shared/visual-style.md` when no real screenshots are provided — surface-1 frame + chrome bar + inner panels

**Content handling**:
- Use the user's real content when provided (feature names, descriptions, integration list)
- Generate example content when not provided, clearly noting it's placeholder
- Feature names: acceptable to generate if user provides only the product concept ("Analytics", "Automation", "Integrations")
- Feature descriptions: 1-2 sentences per feature, focused on what the feature DOES, not marketing superlatives
- Customer logos, testimonial quotes, and usage statistics the user didn't give are tagged sample content (fictional companies, wordmarks) — never presented as real
- Integration logos: real logos only, from the sources in the master `SKILL.md` Design Rules (*Real logos only*). Never draw a logo and never use placeholder squares; when no source has the brand, use its name as a text wordmark

### Step 6: Verify

After generating the page, run through `shared/quality-checklist.md`. Focus on these critical items:

> Visual checks below (color, shadow, radius, typography, spacing values) are written for Minimal. With another style active, check them against the active style file instead. Visual rules in `references/anti-patterns.md` follow the same precedence; content and structure rules apply in every style.

1. **Color**: Zero hue-tinted grays? Chromatic color <10%? CTA uses `var(--accent)`? Brand color (if any) only on allowed elements?
2. **Shadows**: Zero box-shadow anywhere? Feature cards, integration cards — no shadows?
3. **Typography**: Three font families? Weight 500 dominant? Labels in mono/uppercase?
4. **Spacing**: Section gap ≥ 180px? Hero top 128px? Title-to-content 58px?
5. **Radius**: Buttons 2px? Feature cards 8px? Screenshot frames 16px? No pill-shaped buttons (999px)?
6. **Responsive**: Feature grid wraps to 1-col? CTA buttons stack? 2-col splits become single column?
7. **Animation**: `prefers-reduced-motion` guard present? Timing matches `shared/interaction-patterns.md`? Card stagger 100ms, hover lift -4px? No animation on nav/footer?

**Product-page-specific checks**:
7. **Hero CTA uses btn-lg?** NOT standard 14px/8px 16px — hero buttons must be 16px/12px 24px
8. **Feature sections use product screenshots?** NOT illustrations, abstract graphics, or conceptual diagrams (8/11 evidence)
9. **Integration cards show full-color logos?** NOT grayscale (grayscale is for social-proof logo walls only)
10. **Play button is pure CSS?** No icon font dependency, no external SVG
11. **Screenshot frames use 16px content card radius?** NOT 8px feature card radius
12. **At most 1-2 sections on `var(--surface-1)` background?** No alternating section backgrounds
13. **Dual CTA language includes "demo"?** Product pages lean toward demo-oriented language (3/8 evidence)
14. **Nav present and functioning?** Missing nav = error
15. **Archetype B includes API/developer CTA in integrations?** Required for platform products
16. **Archetype C accordion works?** Click toggles active state, changes screenshot (if implemented)

If issues are found, fix them before delivering.

### Step 7: Deliver

Provide:
1. The page file(s) with instructions to open/run
2. A brief note on key design decisions (2-3 sentences)
3. What's in scope (visual presentation) vs. not implemented (real video playback, form submission, interactive demos, API integration)

---

## Knowledge Files

| File | Content | When to Load |
|------|---------|-------------|
| `shared/visual-style.md` | **Design system**: default tokens, Light/Dark themes, component styles, brand customization rules | Step 5 (always — read FIRST) |
| `references/archetypes.md` | 3 Product page archetypes (A Feature Showcase / B Platform Overview / C Product Deep-Dive), selection guide, section presence matrix | Step 2 (always) |
| `references/product-hero.md` | Product-specific hero patterns: 3 patterns (centered video, text+visual split, full-width), play button tokens, CTA copy patterns, comparison with Landing hero | Step 5 (always) |
| `references/feature-showcase.md` | **Core**: 4 feature presentation patterns (grid, accordion+tab, carousel, single visual), screenshot framing decision table, "Learn more" link tokens | Step 5 (always) |
| `references/use-cases.md` | Use case / "Who it's for" section: segmentation axes, 2 patterns (card grid, accordion), segment count guidance | Step 5 (when Use Cases section included) |
| `references/integrations.md` | Integration section: 3 patterns (featured grid, logo wall, featured+API), card tokens, API CTA guidance | Step 5 (when Integrations section included) |
| `references/section-composition.md` | Section ordering per archetype, spacing rules, CTA tokens, background alternation, reusable section references | Step 3 (always) |
| `references/anti-patterns.md` | 12 anti-patterns (Visual 5, Content 4, Structural 3), brand color reconciliation, verification checklist | Step 5 (always) |
| `shared/navigation.md` | Nav layout, CSS specificity trap for nav buttons | Step 5 (always) |
| `shared/footer.md` | Footer layout and content | Step 5 (always) |
| `shared/quality-checklist.md` | verification checklist | Step 6 (always) |
| `shared/interaction-patterns.md` | Motion tokens: scroll reveal, stagger, counter, hover lift recipes | Step 5 (always) |

---

## Constraints

- This Skill does NOT require Mobbin, external APIs, or internet access
- V1 scope: page skeleton + layout + components + visual quality
- NOT in V1: real video playback, interactive product demos, form submission, routing, payment, database, complex animations
- Output: runnable frontend code (HTML/CSS, or matching the user's project stack)
- All design knowledge is pre-distilled in the references/ directory
- Visual style defaults to the shared design system tokens; user-provided brand specs override only `--accent` / `--accent-text` and `--font-display`
- Video play button is decorative — clicking it does not play a video (V1 scope limitation)
- Accordion behavior for Archetype C uses vanilla JS — no framework dependency
- Feature screenshots use the Synthetic Product Visual recipe when no real screenshots are provided
