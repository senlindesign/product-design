# Skill Workflow Template — Shared Across Page Types

> Shared workflow skeleton for all Proof page skills. Each SKILL.md references this template and supplements it with page-type-specific content.

---

## SKILL.md Structure

Each SKILL.md is organized in the following order:

```
# [Page Type] Skill
One-line description + Visual System reference

## When to Use This Skill        ← page-type-specific
## Workflow (Steps 1-7)          ← shared skeleton + page-type-specific content
## Knowledge Files               ← page-type-specific
## Constraints                   ← mostly shared
```

---

## Generic Workflow

### Step 1: Understand the Task

Gather inputs from the user's request. Ask only for inputs that would significantly change the page approach; use reasonable defaults for the rest.

**Required** (must be clear from request or ask):
- Product name and one-line description
- `[PAGE-TYPE-SPECIFIC]` additional required inputs (e.g., tier count for pricing)

**Use defaults if not provided**:
- Target audience / product type signals → infer from description
- Brand color → **default is the active style's own accent** (Minimal: no brand color, `--accent` = `--text`; Editorial: teal `#20808D`). Only add a brand color if the user explicitly provides one — see the active style file's Brand Customization section (Minimal: `visual-style.md` §10.1)
- Display font → **default is the active style's display font** (Minimal: DM Sans). Only override if user provides a specific font name — see the active style file's Brand Customization section (Minimal: `visual-style.md` §10.2)
- Technology stack → single HTML file with inline CSS, or framework matching the user's project
- Theme → Light (default for most) or Dark (developer tools)
- `[PAGE-TYPE-SPECIFIC]` additional defaults (e.g., tier names/prices for pricing, section content for landing)

### Step 2: Select Archetype

Read `references/archetypes.md` and classify the product.

`[PAGE-TYPE-SPECIFIC]` Archetype table — each page type defines 3-4 archetypes with signals, default theme, and key differentiators.

The archetype determines: theme (Light/Dark), section composition, CTA tone, and page-type-specific layout decisions.

### Step 3: Compose Sections

Based on the archetype, decide which sections to include. Read the relevant `references/*.md` files for each selected section.

`[PAGE-TYPE-SPECIFIC]` — define minimum sections (always needed), conditional sections (add based on content/archetype), and removal criteria.

Check `references/section-composition.md` for ordering rules, spacing, and conflict detection.

### Step 4: Generate Page Spec

Before writing code, produce a brief spec (in a code comment or short message to the user):

```
Page Spec:
- Product: [name] — [one-line description]
- Archetype: [A/B/C/D] — [name]
- Theme: Light / Dark
- Sections (in order): [list]
- Brand color: none (default) / [color] — --accent set to [value], used on [where]
- Display font: default (DM Sans) / [font name] — tracking: [-0.02em / -0.01em]
- Not in scope: [business logic, real form submission, etc.]
```

`[PAGE-TYPE-SPECIFIC]` additional spec fields (e.g., hero pattern for landing, tier layout for pricing).

### Step 5: Build the Page

**First**: Read the active style file in full — `shared/visual-style.md` (Minimal, the default), or `shared/visual-style-business.md` / `shared/visual-style-colorful.md` / `shared/visual-style-editorial.md` when the master skill selected another style. Every CSS value must come from its tokens. Token blocks in a page skill are Minimal defaults; *Style precedence* in the master `SKILL.md` decides conflicts.

Then implement the page following the spec. For each section:

1. Read the corresponding `references/*.md` knowledge file for the section type
2. Select the pattern that matches the archetype and content
3. Implement strictly following design system tokens (see below)
4. Check against `references/anti-patterns.md` — verify each design choice traces back to a product/brand characteristic, not an AI default

#### Design System Tokens (must follow)

```
Fonts:     var(--font-display) default DM Sans + var(--font-mono) default DM Mono + system sans (body)
           Override: swap --font-display value + update Google Fonts link (see the active style file's Brand Customization section; Minimal §10.2)
Weights:   500 (display/nav/button) + 400 (mono/body) — no other weights
Colors:    Light: #FFF / #F5F5F5 / #E9E9E9 / #141414
           Dark:  #0A0A0A / #141414 / #1F1F1F / #EDEDED
           Text hierarchy via opacity (1 / 0.5 / 0.4 / 0.3 / 0.15), NOT different grays
Accent:    var(--accent) default = var(--text) + var(--accent-text) default = var(--text-inverse)
           Override: set --accent to brand color + calculate --accent-text (see the active style file's Brand Customization section; Minimal §10.1)
Spacing:   Section rhythm 180px, title-to-content 58px
Radius:    Buttons 2px, feature cards 8px, content cards 16px
Shadows:   ZERO — depth via background color steps only
Transitions: transform 0.2s ease-in-out (hover), opacity 0.3s linear
Motion:      scroll entrance 0.8s, card stagger 100ms, counter 2000ms (see shared/interaction-patterns.md)
Grid:      max-width 1080px, gutter 24px
```

`[PAGE-TYPE-SPECIFIC]` additional tokens (e.g., pricing: price number size, tier card padding, toggle dimensions; landing: hero top 128px, bento 3-col/20px gap).

#### Implementation Principles

- Semantic HTML (one h1, sections, nav, footer)
- Mobile-responsive (flexbox/grid, breakpoint at 767px (`@media (max-width: 767px)`))
- Single HTML file with inline `<style>` — include Google Fonts link for DM Sans + DM Mono
- Placeholder images: background must step toward the page background — inside a `var(--surface-1)` card use `var(--bg)`; inside a `var(--bg)` section use `var(--surface-1)`. Never repeat the same surface value (e.g., do not use `var(--surface-1)` inside a `var(--surface-1)` card — the placeholder becomes invisible)
- Interactive states: hover `transform: translateY(-1px)` on buttons, `opacity` transition on links
- Entrance animations: scroll reveal + child stagger + counter animation per `shared/interaction-patterns.md` — all wrapped in `prefers-reduced-motion`, use the combined script template
- `[PAGE-TYPE-SPECIFIC]` additional principles (e.g., pricing: billing toggle JS, comparison table checkmarks)

#### Content Handling

- Use the user's real content when provided
- Generate example content when not provided, clearly noting it's placeholder
- Never fabricate testimonials, statistics, or company names as real
- `[PAGE-TYPE-SPECIFIC]` content rules (e.g., pricing: placeholder prices should be realistic for the product type)

### Step 6: Verify

After generating the page, run through `shared/quality-checklist.md`. Shared critical items:

1. **Color**: Zero hue-tinted grays? Chromatic color <10%? CTA uses `var(--accent)`? Brand color (if any) only on allowed elements?
2. **Shadows**: Zero box-shadow anywhere? Depth via bg-color steps only?
3. **Typography**: Three font families? Weight 500 dominant? Labels in mono/uppercase?
4. **Spacing**: Section gap >= 180px? Title-to-content ~ 58px?
5. **Radius**: Buttons 2px?
6. **Responsive**: Works at 767px width?

`[PAGE-TYPE-SPECIFIC]` additional verification checks (e.g., landing: hero visual is product screenshot not illustration, hero top >= 128px; pricing: toggle works, CTA differentiation, enterprise handling).

If issues are found, fix them before delivering.

### Step 7: Deliver

Provide:
1. The page file(s) with instructions to open/run
2. A brief note on key design decisions (2-3 sentences)
3. What's in scope (visual presentation) vs. not implemented (business logic, real data)

---

## Knowledge Files (shared entries)

Every SKILL.md's Knowledge Files table should include these shared rows:

| File | Content | When to Load |
|------|---------|-------------|
| `shared/visual-style.md` | **Design system**: default tokens, Light/Dark themes, component styles | Step 5 (always — read FIRST) |
| `references/archetypes.md` | Sub-types, selection guide, typical sections | Step 2 (always) |
| `references/section-composition.md` | Ordering rules, spacing, dependencies | Step 3 (always) |
| `references/anti-patterns.md` | AI convergence traps, common mistakes | Step 5 (always) |
| `shared/quality-checklist.md` | Verification checklist | Step 6 (always) |

`[PAGE-TYPE-SPECIFIC]` additional knowledge files for each section type the page uses.

Navigation and Footer knowledge lives in `shared/navigation.md` and `shared/footer.md`.

---

## Constraints (shared)

- This Skill does NOT require Mobbin, external APIs, or internet access
- V1 scope: page skeleton + layout + components + visual quality
- NOT in V1: real form submission, routing, payment, database, complex animations
- Output: runnable frontend code (HTML/CSS, or matching the user's project stack)
- All design knowledge is pre-distilled in the references/ directory
- Visual style defaults to the shared design system tokens; user-provided brand specs override only the specific values they specify
- `[PAGE-TYPE-SPECIFIC]` additional constraints (e.g., pricing: billing toggle uses vanilla JS)
