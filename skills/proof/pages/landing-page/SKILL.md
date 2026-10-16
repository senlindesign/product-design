# Landing Page Skill

Generate a runnable SaaS landing page with professional visual quality. No Mobbin or external service required at runtime.

**Visual System**: see `shared/visual-style.md` — defines the default design tokens (colors, typography, spacing, components) for Light and Dark themes. Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.

---

## When to Use This Skill

Use this Skill when the user asks you to create a landing page, product homepage, or marketing page for a SaaS/software product. This includes:
- "Make a landing page for [product]"
- "Create a homepage for my SaaS"
- "Build a marketing page for [tool/platform/API]"

Do NOT use this Skill for:
- Dashboard, settings, or app-internal pages (different page type)
- E-commerce product detail pages
- Blog or content pages
- Pages where the user has provided a complete, specific design spec to follow exactly

---

## Workflow

### Step 1: Understand the Task

Gather these inputs from the user's request. Do not ask questions in this step — the master skill decides whether to ask (its Step 1). For each input the user does not give, use the default below; facts that are missing become labeled placeholders.

**Required** (must be clear from request or ask):
- Product name and one-line description
- What the product does (core value proposition)

**Use defaults if not provided**:
- Target audience → infer from product type
- Available content (features, testimonials, pricing) → generate appropriate placeholder content, labeled as examples
- Brand color → **default is the active style's own accent** (Minimal: no brand color, --accent = --text; Editorial: teal #20808D). Only override if user explicitly provides one — see the active style file's Brand Customization section (Minimal: visual-style.md §10.1)
- Display font → **default is the active style's display font** (Minimal: DM Sans). Only override if user provides a specific font name — see the active style file's Brand Customization section (Minimal: visual-style.md §10.2)
- Technology stack → use minimal runnable approach (single HTML file with inline CSS, or framework matching the user's project)
- Theme → Light (A. SaaS Tool, D. Creative Tool) or Dark (C. Developer Tool), see archetype guidance

**Brief context** (when called from the master skill):

When the master skill passes a project brief (audience, goal, barriers, evidence), use it in archetype selection (Step 2) and section composition (Step 3):
- Audience type and familiarity → archetype selection and explanation depth
- Primary barrier (trust, complexity, cost) → which objection-handling sections to include
- Available evidence (screenshots, testimonials, metrics) → which sections are possible vs. must be skipped
- Whether product value is sequential or parallel → How It Works vs. feature cards

### Step 2: Select Archetype + Theme

Read `references/archetypes.md` and classify the product:

| Signal | Archetype | Default Theme |
|--------|-----------|---------------|
| Solves one specific problem | A. SaaS Tool | Light |
| Multi-scenario platform | B. SaaS Platform | Light or Dark |
| Developer/API/CLI audience | C. Developer Tool | Dark |
| Designer/creator audience | D. Creative Tool | Light |

The archetype determines: theme (Light/Dark), section composition, CTA tone, and type of product visual in the Hero.

**Brief-informed selection**: When a project brief is available, apply these rules. When a rule matches, it takes priority over the signal table above:
- Audience is enterprise decision-makers evaluating options → B. SaaS Platform (even for focused products)
- Main barrier is trust or credibility → place Social Proof directly after the hero — real testimonials or logos if the user gave them, otherwise sample content (master `SKILL.md` Design Rules → *Sample content*). If the user said they have none, add a security or credibility section instead
- Audience unfamiliar with the product category → add an explanation section (problem/solution or How It Works) before the features

### Step 3: Compose Sections

Based on the archetype's typical section list, decide which sections to include. Read the relevant `references/*.md` files for each selected section.

**Minimum sections** (include on every landing page):
1. Navigation
2. Hero
3. Features (or equivalent product value demonstration)
4. CTA (at least one beyond the Hero CTA)
5. Footer

**Add based on available content**:
- Logo wall / Social Proof → if customer data or logos available
- How It Works → if product is complex or has a multi-step flow
- FAQ → if common questions exist or pricing needs clarification
- Pricing preview → if pricing info is available
- Social Proof → real testimonials, logos, or case studies from the brief; if the brief doesn't mention them, sample content (master `SKILL.md` Design Rules → *Sample content*); if the user said they have none, skip it
- How It Works → if brief indicates product value is sequential, or audience is unfamiliar with the category
- FAQ → if brief identifies specific barriers or objections that need addressing

**Remove if**:
- Content doesn't exist to fill a section meaningfully
- The section would repeat information already covered
- Brief indicates no real metrics or customer data → skip Stats, logo wall, or testimonial sections rather than fabricating
- Brief indicates high-intent audience (email campaign, known users) → shorter page, fewer sections, direct CTA

Check `references/section-composition.md` for ordering rules and conflict detection.

### Step 4: Generate Page Spec

Before writing code, produce a brief spec (in a code comment or short message to the user):

```
Page Spec:
- Product: [name] — [one-line description]
- Archetype: [A/B/C/D] — [name]
- Theme: Light / Dark
- Sections (in order): [list]
- Hero pattern: [centered/split/dark/minimal]
- Features pattern: [bento/alternating/grid]
- Brand color: none (default) / [color] — --accent set to [value], used on [where]
- Display font: default (DM Sans) / [font name] — tracking: [-0.02em / -0.01em]
- CTA strategy: [single/dual/email+button]
- Not in scope: [business logic, real form submission, etc.]
```

### Step 5: Build the Page

**First**: Read the active style file in full — `shared/visual-style.md` (Minimal, the default), or `shared/visual-style-business.md` / `shared/visual-style-colorful.md` / `shared/visual-style-editorial.md` when the master skill selected another style. Every CSS value must come from its tokens.

Then implement the page following the spec. For each section:

1. Read the corresponding `references/*.md` knowledge file for the section type
2. Select the pattern that matches the archetype and content
3. Implement strictly following `visual-style.md` tokens:

> **The token blocks below are Minimal defaults.** With another style active, apply *Style precedence* from the master `SKILL.md`: visual values (fonts, weights, colors, radius, shadow, spacing rhythm, button and card styling) come from the active style file; layout, structure, and content rules here still apply.

**Design System Tokens (must follow)**:

```
Fonts:     var(--font-display) default DM Sans + var(--font-mono) default DM Mono + system sans (body)
Weights:   500 (display/nav/button) + 400 (mono/body) — no other weights
Colors:    Light: #FFF / #F5F5F5 / #E9E9E9 / #141414
           Dark:  #0A0A0A / #141414 / #1F1F1F / #EDEDED
           Text hierarchy via opacity (1 / 0.5 / 0.4 / 0.3 / 0.15), NOT different grays
Accent:    var(--accent) default = var(--text) + var(--accent-text) default = var(--text-inverse)
Spacing:   Section rhythm 180px, hero top 128px, title-to-content 58px
Radius:    Buttons 2px, feature cards 8px, content cards 16px
Shadows:   ZERO — depth via background color steps only
Transitions: transform 0.2s ease-in-out (hover), opacity 0.3s linear
Motion:      scroll entrance 0.8s, card stagger 100ms, hover lift -4px (see shared/interaction-patterns.md)
Grid:      max-width 1080px, gutter 24px, bento 3-col/20px gap
```

4. Check against `references/anti-patterns.md` — verify each design choice traces back to a product/brand characteristic, not an AI default

**Implementation principles**:
- Semantic HTML (one h1, sections, nav, footer)
- Mobile-responsive (flexbox/grid, breakpoint at 767px (`@media (max-width: 767px)`))
- Single HTML file with inline `<style>` — include Google Fonts link for DM Sans + DM Mono
- Placeholder images: use `var(--surface-1)` background with mono-font label, not broken image links — only for photos or artwork the user must supply. Product screenshots are never a grey box: build them with `shared/product-visuals.md`
- Interactive states: hover `transform: translateY(-1px)` on buttons, `opacity` transition on links

**Content handling**:
- Use the user's real content when provided
- Generate example content when not provided, clearly noting it's placeholder
- Never present testimonials, statistics, or company names as real unless the user gave them — anything else is tagged sample content

### Step 6: Verify

After generating the page, run through `shared/quality-checklist.md`. Focus on these critical items:

> Visual checks below (color, shadow, radius, typography, spacing values) are written for Minimal. With another style active, check them against the active style file instead. Visual rules in `references/anti-patterns.md` follow the same precedence; content and structure rules apply in every style.

1. **Color**: Zero hue-tinted grays? Chromatic color <10%? CTA uses var(--accent)? Brand color (if any) only on allowed elements?
2. **Shadows**: Zero box-shadow anywhere? Depth via bg-color steps only?
3. **Typography**: Three font families? Weight 500 dominant? Negative tracking on titles? Labels in mono/uppercase?
4. **Visuals**: Hero visual is product screenshot/code, not illustration?
5. **Spacing**: Section gap ≥ 180px? Hero top ≥ 128px? Title-to-content ≈ 58px?
6. **Radius**: Buttons 2px, feature cards 8px, content cards 16px?
7. **Responsive**: Works at 767px width?
8. **Animation**: `prefers-reduced-motion` guard present? Timing matches `shared/interaction-patterns.md`? No animation on nav/footer?

If issues are found, fix them before delivering.

### Step 7: Deliver

Provide:
1. The page file(s) with instructions to open/run
2. A brief note on key design decisions (2-3 sentences)
3. What's in scope (visual presentation) vs. not implemented (business logic, real data)

---

## Knowledge Files

Load each file at the step in its "When to Load" column:

| File | Content | When to Load |
|------|---------|-------------|
| `shared/visual-style.md` | **Design system**: default tokens, Light/Dark themes, component styles, verification checklist | Step 5 (always — read FIRST) |
| `references/archetypes.md` | 4 sub-types, selection guide, typical sections, theme assignment | Step 2 (always) |
| `references/hero.md` | Hero patterns, headline/CTA/background strategies | Step 5 (always) |
| `references/features.md` | Feature display patterns: bento/alternating/grid | Step 5 (when Features included) |
| `references/social-proof.md` | Trust signal types, logo walls, testimonials | Step 5 (when Social Proof included) |
| `references/cta.md` | CTA placement, copy, visual strategies | Step 5 (when standalone CTA included) |
| `references/faq.md` | Accordion, grouped, layout patterns | Step 5 (when FAQ included) |
| `references/how-it-works.md` | Step displays, numbering, visual approaches | Step 5 (when How It Works included) |
| `shared/footer.md` | Link organization, brand expression | Step 5 (always) |
| `shared/navigation.md` | Menu structure, CTA placement | Step 5 (always) |
| `references/section-composition.md` | Ordering rules, rhythm, dependencies | Step 3 (always) |
| `references/anti-patterns.md` | AI convergence traps, common mistakes | Step 5 (always) |
| `shared/quality-checklist.md` | verification checklist | Step 6 (always) |
| `shared/interaction-patterns.md` | Motion tokens: scroll reveal, stagger, counter, hover lift recipes | Step 5 (always) |

---

## Constraints

- This Skill does NOT require Mobbin, external APIs, or internet access
- V1 scope: page skeleton + layout + components + visual quality
- NOT in V1: real form submission, routing, payment, database, complex animations
- Output: runnable frontend code (HTML/CSS, or matching the user's project stack)
- All design knowledge is pre-distilled in the references/ directory
- Visual style defaults to the built-in design system tokens; user-provided brand specs override only the specific values they specify
