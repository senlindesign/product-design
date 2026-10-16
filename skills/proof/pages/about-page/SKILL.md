# About Page Skill

Generate a runnable SaaS About page with professional visual quality. No Mobbin or external service required at runtime.

**Visual System**: see `shared/visual-style.md` — defines the default design tokens (colors, typography, spacing, components) for Light and Dark themes. About-specific component tokens (team grid, stats row, timeline, values layout) are in `references/`. Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.

---

## When to Use This Skill

Use this Skill when the user asks you to create an About page, company story page, team page, or "who we are" page for a SaaS/software product. This includes:
- "Make an About page for [product]"
- "Create a company story page"
- "Build a 'meet the team' page"
- "Design the About Us page for [tool/platform]"

Do NOT use this Skill for:
- Landing pages (use Landing Page Skill)
- Pricing pages (use Pricing Page Skill)
- Contact pages (use Contact Page Skill)
- Careers / job listing pages (dedicated career page, not About)
- In-app settings or profile pages

---

## Workflow

### Step 1: Understand the Task

Gather these inputs from the user's request. Do not ask questions in this step — the master skill decides whether to ask (its Step 1). For each input the user does not give, use the default below; facts that are missing become labeled placeholders.

**Required** (must be clear from request or ask):
- Product name and one-line description
- Primary intent: company story / team showcase / mission statement

**Use defaults if not provided**:
- Team members → sample team cards (fictional names, roles, illustrated avatars) tagged `data-sample`, unless the user said to leave the team out
- Company stats → omit the stats section entirely if no real numbers provided
- Company story → use clearly templated placeholder text
- Values → generate 3-4 generic value titles with placeholder descriptions
- Milestones → omit the timeline section if none provided
- Brand color → **default is the active style's own accent** (Minimal: no brand color, `--accent` = `--text`; Editorial: teal `#20808D`). Only override if user explicitly provides one — see the active style file's Brand Customization section (Minimal: `visual-style.md` §10.1)
- Display font → **default is the active style's display font** (Minimal: DM Sans). Only override if user provides a specific font name — see the active style file's Brand Customization section (Minimal: `visual-style.md` §10.2)
- Technology stack → single HTML file with inline CSS
- Theme → Light (default for most), Dark (for developer tools)

**Brief context** (when called from the master skill):

When the master skill passes a project brief (audience, goal, barriers, evidence), use it in archetype selection (Step 2) and section composition (Step 3):
- Primary intent (hiring, investor relations, customer trust, brand identity) → archetype and CTA focus
- Team as differentiator (small expert team vs. large organization) → Team-First vs. Company Story
- Mission or values as differentiator → Mission-Driven archetype
- Available content (team photos, real stats, milestones, founding story) → which sections are possible

### Step 2: Select Archetype

Read `references/archetypes.md` and classify the product:

| Signal | Archetype | Default Theme | Core Characteristic |
|--------|-----------|---------------|---------------------|
| Established product, history to tell, medium-large team | A. Company Story | Light | Mission hero → story → team (leadership) → stats → values → CTA |
| Small startup/studio, team IS the brand identity | B. Team-First | Light or Dark | Brief hero → full team grid (dominant) → brief values → CTA |
| Strong ideological position, social mission, trust-driven | C. Mission-Driven | Light or Dark | Belief statement hero → values (dominant) → stats → team (secondary) → CTA |

The archetype determines: section composition, section emphasis (which section dominates), CTA tone, and whether timeline/investors sections appear.

**Brief-informed selection**: When a project brief is available, apply these rules. When a rule matches, it takes priority over the signal table above:
- Brief indicates the team itself is the selling point (agency, studio, consultancy) → B. Team-First
- Brief indicates strong ideological position or social mission → C. Mission-Driven
- Brief indicates established company with history and milestones → A. Company Story
- Brief mentions hiring as a page goal → emphasize team section and add careers CTA

### Step 3: Compose Sections

Based on the archetype's section list from `references/section-composition.md`, decide which sections to include. Read the relevant `references/*.md` files for each selected section.

**Minimum sections** (always needed):
1. Navigation
2. Hero (text-only, mission statement heading, no CTA button)
3. Team (grid layout — leadership-only or full team depending on archetype)
4. CTA (careers-focused)
5. Footer

**Add based on archetype and content**:
- Story / Origin → Archetype A (required), C (optional), B (skip or brief)
- Stats → A and C (required when user provides numbers), B (optional — small teams have fewer impressive numbers)
- Values → all archetypes include it; C makes it dominant, B keeps it brief
- Timeline → A and C only, when user provides 5+ milestones
- Investor / Partner logos → A and C only, when user provides logos (reuse social-proof logo wall pattern)
- Stats → real numbers from the brief (team size, customers, revenue, founding year); if the brief doesn't mention them, sample content (master `SKILL.md` Design Rules → *Sample content*) with round illustrative numbers; if the user said there are none, leave it out
- Timeline → only if brief provides 5+ dated milestones. Skip entirely rather than inventing company history
- Investor/Partner logos → only if brief provides real investor or partner names

**Remove if**:
- User provides no content for that section (stats without numbers, timeline without milestones)
- Section would require fabricating company-specific content
- Brief provides no team member information → sample content (master `SKILL.md` Design Rules → *Sample content*): fictional names and roles with illustrated avatars, tagged `data-sample`
- Brief provides no company history → skip timeline and origin story sections, focus on values and team

**Do NOT add**:
- Product screenshots in the hero (About hero is text-only — 0/11 observed heroes had product screenshots)
- Office photo gallery (fabrication risk, "content as decoration" principle)
- Map embed (complex, rarely adds value for SaaS)

Check `references/section-composition.md` for ordering rules, spacing, and background color rules.

### Step 4: Generate Page Spec

Before writing code, produce a brief spec:

```
Page Spec:
- Product: [name] — [one-line description]
- Archetype: [A/B/C] — [name]
- Theme: Light / Dark
- Sections (in order): [list]
- Team: [leadership only (6-12) / full team (all)] — [real names or placeholders]
- Stats: [4 numbers from user / omitted]
- Values: [3-5 values — real or placeholder]
- Timeline: [included with X milestones / omitted]
- CTA target: careers / contact / mission invitation
- Brand color: none (default) / [color] — --accent set to [value]
- Display font: default (DM Sans) / [font name] — tracking: [-0.02em / -0.01em]
- Not in scope: [real form submission, routing, career applications, etc.]
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
Spacing:   Section rhythm 180px, hero top 128px, title-to-content 58px
Radius:    Buttons 2px, feature cards 8px, content cards 16px
Shadows:   ZERO — depth via background color steps only
Transitions: transform 0.2s ease-in-out (hover), opacity 0.3s linear
Motion:      scroll entrance 0.8s, card stagger 100ms, counter 2000ms (see shared/interaction-patterns.md)
Grid:      max-width 1080px, gutter 24px, side padding 32px
Nav:       height 68px (var(--nav-h)), fixed positioning needs body padding-top
```

**About-specific tokens**:

```
Hero:
  padding-top: 128px                      (hero top — spacing system)
  heading max-width: 720px                (page-specific: wider than subtitle 540px, narrower than grid 1080px)
  heading: clamp(32px, 4vw, 47px)         (section heading — type scale; About hero uses section scale, not Landing hero scale)
  body: 18px / opacity 0.5 / max-width 540px  (subtitle measure)
  NO CTA button in hero (10/11 observed)
  NO product screenshots (0/11 observed)

Team grid:
  grid: repeat(3, 1fr) / gap 32px 24px   (3-col default; 4-col for 15+ people)
  photo: 96px × 96px / border-radius 50% / object-fit cover
  photo placeholder: var(--surface-1) bg / border-radius 50%
  name: 16px / display / 500
  title: 14px / display / 500 / opacity 0.5
  photo-to-name gap: 16px
  card: text-align center

Stats row:
  layout: flex / justify-content space-between / text-align center
  number: clamp(36px, 5vw, 56px) / display / 500 / -0.02em tracking
  label: 14px / display / 500 / opacity 0.5 / margin-top 8px
  show only stats the user gives, up to 4 (e.g., team size, year founded, customers, geography); no stats from the user → no stats section
  optional: var(--surface-1) full-width band

Values:
  default layout: numbered list (01, 02, 03 in mono/0.4)
  number column: 48px (page-specific)
  title: 20px / display / 500
  description: 16px / body / 400 / opacity 0.5
  3–5 values
  NO colored icons, NO icon backgrounds

Timeline (when included):
  center line: 2px width / var(--surface-2) / absolute positioned
  nodes: 8px × 8px / border-radius 50% / border 2px solid var(--surface-2) / bg var(--bg)
  alternating grid: 1fr 1fr / gap 24px
  year label: 12px / mono / 400 / 0.72px tracking / uppercase / opacity 0.4
  entry title: 20px / display / 500
  entry description: 16px / body / 400 / opacity 0.5
  entry spacing: 58px padding-bottom
  narrow: collapse to single column, line shifts to left edge at 20px

CTA section:
  heading: "Join the team" / "We're hiring" / "Work with us" (NOT "Start free trial")
  button: "See open positions" / "View careers" / "Get in touch" (careers or contact, NOT product conversion)
  0/6 observed About CTAs linked to product signup
```

4. Check against `references/anti-patterns.md` — verify each design choice traces back to observation evidence, not AI defaults

**Implementation principles**:
- Semantic HTML (one h1 in the hero, sections, nav, footer)
- Mobile-responsive (flexbox/grid, breakpoint at 767px (`@media (max-width: 767px)`))
- Single HTML file with inline `<style>` — include Google Fonts link for DM Sans + DM Mono
- Placeholder images: use `var(--surface-1)` background with circle shape for team photos, not broken image links or AI-generated faces
- Interactive states: hover `transform: translateY(-1px)` on buttons, `opacity` transition on links
- Nav buttons must use explicit overrides if placed inside `.nav-links` (see `shared/navigation.md` CSS specificity section)
- **No fabricated content**: team names, company stats, founding stories, and milestones must come from user input or be clearly marked as placeholders

**Content handling**:
- Use the user's real content when provided (team names, stats, story, values)
- Generate example content when not provided, clearly noting it's placeholder
- Team: names the user gave, otherwise fictional sample names and roles tagged `data-sample` — never real people's names
- Stats: omit the section if the user said there are no numbers; otherwise unsourced numbers are tagged sample content
- Story: use templated framing like "Founded in [year], [Company] was born from..."
- Values: generic titles are acceptable as starting points (e.g., "Innovation", "Quality") but mark as placeholder

### Step 6: Verify

After generating the page, run through `shared/quality-checklist.md`. Focus on these critical items:

> Visual checks below (color, shadow, radius, typography, spacing values) are written for Minimal. With another style active, check them against the active style file instead. Visual rules in `references/anti-patterns.md` follow the same precedence; content and structure rules apply in every style.

1. **Color**: Zero hue-tinted grays? Chromatic color <10%? CTA uses `var(--accent)`? Brand color (if any) only on allowed elements?
2. **Shadows**: Zero box-shadow anywhere? Team cards, value cards — no shadows?
3. **Typography**: Three font families? Weight 500 dominant? Labels in mono/uppercase?
4. **Spacing**: Section gap ≥ 180px? Hero top 128px? Title-to-content 58px?
5. **Radius**: Buttons 2px? No pill-shaped buttons (999px)?
6. **Responsive**: Team grid wraps? Stats row becomes 2×2? Timeline collapses to single column?
7. **Animation**: `prefers-reduced-motion` guard present? Counter 2000ms? Stagger 100ms (team/values), 150ms (timeline) per `shared/interaction-patterns.md`? No animation on nav/footer?

**About-specific checks**:
7. **Hero is text-only?** No product screenshots, no illustrations, no CTA button
8. **CTA links to careers or contact?** NOT to product signup / free trial
9. **All team photos real or placeholder?** No stock photos, no AI-generated faces. Placeholders use `var(--surface-1)` + `border-radius: 50%`
10. **All stats user-provided or section omitted?** No fabricated metrics
11. **Story content user-provided or clearly templated?** No fabricated founding narratives
12. **Value cards have colored icon backgrounds?** If yes, remove them — all values use same styling
13. **Stat numbers use `color: var(--text)` at full opacity?** NOT `var(--accent)` — numbers are too large for chromatic color
14. **Nav present and functioning?** Missing nav = error
15. **At most 1-2 sections on `var(--surface-1)` background?** No alternating backgrounds

If issues are found, fix them before delivering.

### Step 7: Deliver

Provide:
1. The page file(s) with instructions to open/run
2. A brief note on key design decisions (2-3 sentences)
3. What's in scope (visual presentation) vs. not implemented (real career applications, form submission, team management)

---

## Knowledge Files

| File | Content | When to Load |
|------|---------|-------------|
| `shared/visual-style.md` | **Design system**: default tokens, Light/Dark themes, component styles, brand customization rules | Step 5 (always — read FIRST) |
| `references/archetypes.md` | 3 About page archetypes (A Company Story / B Team-First / C Mission-Driven), selection guide, section combinations | Step 2 (always) |
| `references/about-hero.md` | About-specific hero patterns: text-only, mission statement heading, no CTA, heading scale differences from Landing hero | Step 5 (always) |
| `references/team-section.md` | **Core**: team grid layout, circle photos, person card tokens, 3/4-col variants, content depth variants, multi-tier structure | Step 5 (always) |
| `references/values-section.md` | Values/principles display: numbered list default, 4 layout variants, 3-5 values, no icons | Step 5 (always) |
| `references/stats-section.md` | Company stats: horizontal row, large number typography, up to 4 user-provided stats, optional surface-1 band | Step 5 (when stats section included) |
| `references/timeline-section.md` | Timeline/milestones: vertical alternating default, center line + node CSS, narrow screen collapse, horizontal variant note | Step 5 (when timeline section included) |
| `references/section-composition.md` | Section ordering per archetype, background alternation rules, CTA guidance, nav/footer notes | Step 3 (always) |
| `references/anti-patterns.md` | 10 anti-patterns, brand color reconciliation, 15-item verification checklist | Step 5 (always) |
| `shared/navigation.md` | Nav layout, CSS specificity trap for nav buttons | Step 5 (always) |
| `shared/footer.md` | Footer layout and content | Step 5 (always) |
| `shared/quality-checklist.md` | verification checklist | Step 6 (always) |
| `shared/interaction-patterns.md` | Motion tokens: scroll reveal, stagger, counter, hover lift recipes | Step 5 (always) |

---

## Constraints

- This Skill does NOT require Mobbin, external APIs, or internet access
- V1 scope: page skeleton + layout + components + visual quality
- NOT in V1: real career applications, form submission, team management, content management, complex animations
- Output: runnable frontend code (HTML/CSS, or matching the user's project stack)
- All design knowledge is pre-distilled in the references/ directory
- Visual style defaults to the shared design system tokens; user-provided brand specs override only `--accent` / `--accent-text` and `--font-display`
- Team member content is user-provided or tagged sample content — never real people's names or photos
- Company stats are user-provided or tagged sample content; omitted when the user says there are none
- Company story is user-provided or tagged sample content — never presented as the company's real history
