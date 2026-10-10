# Pricing Page Skill

Generate a runnable SaaS pricing page with professional visual quality. No Mobbin or external service required at runtime.

**Visual System**: see `shared/visual-style.md` — defines the default design tokens (colors, typography, spacing, components) for Light and Dark themes. Pricing-specific component tokens are in `references/`. Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.

---

## When to Use This Skill

Use this Skill when the user asks you to create a pricing page, plan comparison page, or subscription page for a SaaS/software product. This includes:
- "Make a pricing page for [product]"
- "Create a plan comparison page"
- "Build a pricing section for my SaaS"
- "Design the pricing for [tool/platform/API]"

Do NOT use this Skill for:
- Landing pages (use Landing Page Skill)
- Dashboard or app-internal billing settings
- E-commerce product catalog pages
- Single-product purchase pages without tier comparison

---

## Workflow

### Step 1: Understand the Task

Gather these inputs from the user's request. Do not ask questions in this step — the master skill decides whether to ask (its Step 1). For each input the user does not give, use the default below; facts that are missing become labeled placeholders.

**Required** (must be clear from request or ask):
- Product name and one-line description
- Number of tiers and their names (or let the Skill choose defaults)

**Use defaults if not provided**:
- Tier names → Free / Pro / Business (3-tier) or Free / Pro (2-tier)
- Pricing amounts → sample prices (master `SKILL.md` Design Rules → *Sample content*): round, plausible numbers, tagged `data-sample`, named in the QA report — never presented as real
- Features per tier → bracketed placeholders (`[Feature 1]`), labeled the same way
- Billing options → show the billing toggle only when the user provides annual pricing or asks for it; otherwise omit it (never invent annual prices or a discount)
- Brand color → **default is the active style's own accent** (Minimal: no brand color, --accent = --text; Editorial: teal #20808D). Only override if user explicitly provides one — see the active style file's Brand Customization section (Minimal: visual-style.md §10.1)
- Display font → **default is the active style's display font** (Minimal: DM Sans). Only override if user provides a specific font name — see the active style file's Brand Customization section (Minimal: visual-style.md §10.2)
- Technology stack → single HTML file with inline CSS
- Theme → Light (default for most), Dark (for developer tools)

**Brief context** (when called from the master skill):

When the master skill passes a project brief (audience, goal, barriers, evidence), use it in archetype selection (Step 2) and section composition (Step 3):
- Sales model (self-serve vs. sales-led) → archetype and whether enterprise section appears
- Main barrier (price sensitivity, feature confusion, trust) → FAQ focus and comparison table inclusion; switching / setup effort → optional How It Works section
- Competitor context → whether comparison-style positioning is appropriate
- Available evidence (customer logos, case studies) → whether social proof appears near pricing

### Step 2: Select Archetype

Read `references/archetypes.md` and classify the product:

| Signal | Archetype | Default Theme | Tier Count |
|--------|-----------|---------------|------------|
| Features unlock per tier | A. Feature-Tiered | Light | 3-4 |
| Usage/API-based pricing | B. Usage-Based | Light or Dark | 2-3 + custom |
| One paid plan or Free+Paid only | C. Simple Binary | Light | 2 |
| No public pricing, sales-driven | D. Enterprise-First | Light | 1-2 + enterprise |

The archetype determines: section composition, tier card layout, whether comparison table is needed, and CTA tone.

**Brief-informed selection**: When a project brief is available, apply these rules. When a rule matches, it takes priority over the signal table above:
- Brief indicates sales-led model with no public pricing → D. Enterprise-First (even if product has tiers internally)
- Brief indicates main barrier is "which plan is right for me?" → prioritize comparison table (Archetype A)
- Brief indicates usage-based billing or API metering → B. Usage-Based

### Step 3: Compose Sections

Based on the archetype's section list from `references/section-composition.md`, decide which sections to include. Read the relevant `references/*.md` files for each selected section.

**Minimum sections** (include on every pricing page):
1. Navigation
2. Pricing Header
3. Tier Cards
4. Footer

**Add based on archetype and content**:
- Billing Toggle → only if the user provides annual pricing or asks for a toggle (any archetype)
- Comparison Table → include for Archetype A and B when the user gives features per tier. Omit for C. Omit when no features are given — a table of placeholders adds nothing
- Enterprise Section → if 4+ tiers or enterprise customers exist
- FAQ → include by default (billing, cancellation, trial questions). Omit only when the user asks. Answers that need facts the user did not give become labeled placeholders
- Bottom CTA → only if page is long (4+ sections between header and footer)
- Social Proof → if brief provides customer logos or testimonials, place near tier cards to reinforce trust at decision point
- Enterprise Section → if brief mentions enterprise buyers, compliance needs, or custom pricing conversations
- How It Works / Switching → include when the brief names switching or setup effort as the main barrier (a FAQ entry alone is not enough); layout from `sections/how-it-works/SKILL.md`, placement in `references/section-composition.md` §6

**Remove if**:
- Content doesn't exist to fill a section meaningfully
- The section would repeat information already in tier cards
- Brief indicates no competitor differentiation → skip comparison-style positioning in FAQ
- Brief indicates single-product simplicity → skip comparison table for Archetype C

Check `references/section-composition.md` for ordering rules and spacing specifics.

### Step 4: Generate Page Spec

Before writing code, produce a brief spec:

```
Page Spec:
- Product: [name] — [one-line description]
- Archetype: [A/B/C/D] — [name]
- Theme: Light / Dark
- Tiers: [list with prices]
- Billing toggle: yes/no
- Sections (in order): [list]
- Comparison table: yes/no (estimated feature count)
- Enterprise section: inline / breakout / none
- Brand color: none (default) / [color] — --accent set to [value], used on [where]
- Display font: default (DM Sans) / [font name] — tracking: [-0.02em / -0.01em]
- Not in scope: [business logic, real payment, etc.]
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
Weights:   500 (display/nav/button) + 400 (mono/body) — no other weights
Colors:    Light: #FFF / #F5F5F5 / #E9E9E9 / #141414
           Dark:  #0A0A0A / #141414 / #1F1F1F / #EDEDED
           Text hierarchy via opacity (1 / 0.5 / 0.4 / 0.3 / 0.15), NOT different grays
Accent:    var(--accent) default = var(--text) + var(--accent-text) default = var(--text-inverse)
Spacing:   Section rhythm 180px, header top 80-128px, title-to-content 58px
Radius:    Buttons 2px, feature cards 8px, content/tier cards 16px
Shadows:   ZERO — depth via background color steps only
Transitions: transform 0.2s ease-in-out (hover), opacity 0.3s linear
Motion:      scroll entrance 0.8s, card stagger 100ms, hover lift -4px (see shared/interaction-patterns.md)
Grid:      max-width 1080px, gutter 24px, tier cards 3-col/24px gap
```

**Pricing-specific tokens**:

```
Price number:    clamp(36px, 5vw, 48px) / weight 500 / DM Sans / tracking -0.02em
Currency $:      Same font, same size or slightly smaller
Period /mo:      14px / weight 400 / opacity 0.5
Plan name:       20px / weight 500 / tracking -0.4px
Plan desc:       14px / weight 400 / opacity 0.5
Feature check:   ✓ character / opacity 0.4 / 14px (matches feature text)
Feature dash:    — character / opacity 0.2 / 14px
Discount badge:  12px / DM Mono / uppercase / opacity 0.5 / surface-1 bg / 4px radius
Toggle:          surface-1 bg / 40px radius / 36-40px height / 14px/500 labels
Tier card:       padding 32px / bg var(--bg) / border 1px solid surface-2 / radius 16px
Recommended:     plain label "RECOMMENDED" 12px/mono/uppercase/0.4 opacity, no fill ("MOST POPULAR" only if user states it) + subtle ring border: 1.5px solid rgba(text, 0.15)
Recommended (branded): with brand color, ring border uses rgba(accent, 0.2) instead of rgba(text, 0.15)
```

4. Check against `references/anti-patterns.md` — verify each design choice

**Implementation principles**:
- Semantic HTML (one h1, sections, nav, footer)
- Mobile-responsive (flexbox/grid, breakpoint at 767px (`@media (max-width: 767px)`))
- Single HTML file with inline `<style>` — include Google Fonts link for DM Sans + DM Mono
- Interactive states: hover `transform: translateY(-1px)` on buttons, `opacity` transition on links
- Billing toggle: JavaScript to switch displayed prices (monthly ↔ annual)
- Comparison table checkmarks: plain ✓ text character, not SVG icons

**Content handling**:
- Use the user's real content when provided (tier names, prices, features)
- When content is not provided, use placeholders that are clearly labeled as placeholder on the page and named in the delivery note; never present them as real
- Never present testimonials, statistics, or company names as real unless the user gave them — anything else is tagged sample content
- Placeholder prices use bracketed form (`$X/mo`), not realistic-looking numbers

### Step 6: Verify

After generating the page, run through `shared/quality-checklist.md`. Focus on these critical items:

> Visual checks below (color, shadow, radius, typography, spacing values) are written for Minimal. With another style active, check them against the active style file instead. Visual rules in `references/anti-patterns.md` follow the same precedence; content and structure rules apply in every style.

1. **Color**: Zero hue-tinted grays? All tiers same color scheme? CTA uses var(--accent)? Brand color (if any) only on allowed elements?
2. **Shadows**: Zero box-shadow anywhere? Tier cards use border, not shadow?
3. **Typography**: Price number ≤ 48px? Plan name 20px? Labels in mono/uppercase?
4. **Spacing**: Section gap ≥ 180px? Toggle directly above cards (24px gap)?
5. **Radius**: Tier cards 16px? Buttons 2px? Toggle pill 40px?
6. **Anti-patterns**: No gradient cards? No per-tier accent colors? No decorative icons in feature lists?
7. **Responsive**: Tier cards stack on mobile? Comparison table scrolls horizontally?
8. **Animation**: `prefers-reduced-motion` guard present? Timing matches `shared/interaction-patterns.md`? No animation on nav/footer?

**Pricing-specific checks**:
8. **Toggle works** (if included): Monthly/Annual toggle switches prices via JavaScript? Toggle active color stays var(--text) even with brand color?
9. **CTA differentiation**: Recommended tier has filled CTA, others have outline?
10. **Enterprise handling**: Enterprise tier shows "Custom"/"Contact Sales" instead of price?

If issues are found, fix them before delivering.

### Step 7: Deliver

Provide:
1. The page file(s) with instructions to open/run
2. A brief note on key design decisions (2-3 sentences)
3. What's in scope (visual presentation, toggle interaction) vs. not implemented (real payment, plan switching)

---

## Knowledge Files

Load each file at the step in its "When to Load" column:

| File | Content | When to Load |
|------|---------|-------------|
| `shared/visual-style.md` | **Design system**: default tokens, Light/Dark themes, component styles | Step 5 (always — read FIRST) |
| `references/archetypes.md` | 4 pricing sub-types, selection guide, typical sections | Step 2 (always) |
| `references/tier-cards.md` | Tier card layout, price display, feature lists, CTA buttons | Step 5 (always) |
| `references/billing-toggle.md` | Toggle design, discount badge, default state | Step 5 (when toggle included) |
| `references/comparison-table.md` | Feature comparison table layout, check/dash marks, categories | Step 5 (when comparison table included) |
| `references/pricing-header.md` | Page header, headline strategies, subheadline, tabs | Step 5 (always) |
| `references/pricing-faq.md` | FAQ questions, accordion layout, positioning | Step 5 (when FAQ included) |
| `references/enterprise-section.md` | Enterprise tier display, inline vs breakout, logo wall | Step 5 (when enterprise section included) |
| `references/section-composition.md` | Section ordering, spacing rules, combination logic | Step 3 (always) |
| `references/anti-patterns.md` | AI convergence traps, visual/content/structural errors | Step 5 (always) |
| `shared/navigation.md` | Menu structure, CTA placement | Step 5 (always) |
| `shared/footer.md` | Link organization, brand expression | Step 5 (always) |
| `shared/quality-checklist.md` | verification checklist | Step 6 (always) |
| `shared/interaction-patterns.md` | Motion tokens: scroll reveal, stagger, counter, hover lift recipes | Step 5 (always) |

---

## Constraints

- This Skill does NOT require Mobbin, external APIs, or internet access
- V1 scope: page skeleton + layout + tier cards + comparison table + billing toggle interaction
- NOT in V1: real payment processing, plan switching logic, CRM integration, complex animations
- Output: runnable frontend code (HTML/CSS/JS, or matching the user's project stack)
- All design knowledge is pre-distilled in the references/ directory
- Visual style defaults to the shared design system tokens; user-provided brand specs override only the specific values they specify
- Billing toggle uses vanilla JavaScript for price switching — no framework required
