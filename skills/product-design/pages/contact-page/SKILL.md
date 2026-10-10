# Contact Page Skill

Generate a runnable SaaS contact page with professional visual quality. No Mobbin or external service required at runtime.

**Visual System**: see `shared/visual-style.md` — defines the default design tokens (colors, typography, spacing, components) for Light and Dark themes. Contact-specific component tokens are in `references/`. Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.

---

## When to Use This Skill

Use this Skill when the user asks you to create a contact page, "get in touch" page, demo request page, or support contact page for a SaaS/software product. This includes:
- "Make a contact page for [product]"
- "Create a 'get in touch' page"
- "Build a demo request form page"
- "Design the contact us page for [tool/platform]"

Do NOT use this Skill for:
- Landing pages (use Landing Page Skill)
- Pricing pages (use Pricing Page Skill)
- Help center / knowledge base pages (documentation, not contact)
- In-app support widgets or chat interfaces
- Newsletter signup pages (single-field, not contact)

---

## Workflow

### Step 1: Understand the Task

Gather these inputs from the user's request. Do not ask questions in this step — the master skill decides whether to ask (its Step 1). For each input the user does not give, use the default below; facts that are missing become labeled placeholders.

**Required** (must be clear from request or ask):
- Product name and one-line description
- Primary purpose: general contact / sales demo / support inquiry / multi-department

**Use defaults if not provided**:
- Contact departments → infer from product type (single department for simple products, Sales + Support for mid-size)
- Form fields → generate appropriate fields based on archetype (see Step 2)
- Contact information → generate placeholder email/address, labeled as examples
- Brand color → **default is the active style's own accent** (Minimal: no brand color, `--accent` = `--text`; Editorial: teal `#20808D`). Only override if user explicitly provides one — see the active style file's Brand Customization section (Minimal: `visual-style.md` §10.1)
- Display font → **default is the active style's display font** (Minimal: DM Sans). Only override if user provides a specific font name — see the active style file's Brand Customization section (Minimal: `visual-style.md` §10.2)
- Technology stack → single HTML file with inline CSS
- Theme → Light (default for most), Dark (for developer tools)

**Brief context** (when called from the master skill):

When the master skill passes a project brief (audience, goal, barriers, evidence), use it in archetype selection (Step 2) and section composition (Step 3):
- Contact purpose (general inquiry, sales demo, support) → archetype selection
- Audience type (enterprise prospect vs. existing customer vs. general) → form complexity and qualification fields
- Available contact channels (email, phone, address, chat) → what to display in contact info section
- Whether sales conversion is the goal → social proof placement and CTA tone

### Step 2: Select Archetype

Read `references/archetypes.md` and classify the product:

| Signal | Archetype | Default Theme | Core Component |
|--------|-----------|---------------|----------------|
| Simple product, one team | A. Simple Contact | Light | One form + contact info sidebar |
| Multiple teams (sales/support/partnerships) | B. Department Routing | Light | 2-4 department cards |
| High-value enterprise, demo-driven | C. Sales-Focused | Light | Demo form with qualification fields + social proof |
| Mature product with help center | D. Support Hub | Light or Dark | Search/categories first, contact as fallback |

The archetype determines: form field composition, page layout (form vs cards), social proof presence, and CTA tone.

**Brief-informed selection**: When a project brief is available, apply these rules. When a rule matches, it takes priority over the signal table above:
- Brief indicates primary goal is booking demos or sales conversations → C. Sales-Focused (even for simpler products)
- Brief indicates multiple distinct inquiry types → B. Department Routing
- Brief indicates support/help-center context → D. Support Hub

### Step 3: Compose Sections

Based on the archetype's section list from `references/section-composition.md`, decide which sections to include. Read the relevant `references/*.md` files for each selected section.

**Minimum sections** (always needed):
1. Navigation
2. Page Header (or integrated into Contact Section for Archetype C)
3. Contact Section (form / cards / search depending on archetype)
4. Footer

**Add based on archetype and content**:
- Contact Info → if there are real contact details to show (email, phone, address)
- Department Cards → Archetype B only
- Social Proof → Archetype C, real customer logos or testimonials if the user gave them, otherwise sample content (master `SKILL.md` Design Rules → *Sample content*) (fictional wordmarks, never bracket strips); leave it out if the user said they have none
- FAQ → if common contact-related questions exist (3-4 questions max)
- Social Proof → if brief provides customer logos and the page goal is sales conversion (Archetype C). Skip for support-focused pages
- FAQ → if brief identifies common contact-related questions or barriers to reaching out

**Remove if**:
- Content doesn't exist to fill a section meaningfully
- Contact Info section would only contain a generic email (put it inline with the form instead)
- Brief indicates the page is for existing customers (support) → skip sales-oriented social proof and qualification fields

**Do NOT add**:
- Bottom CTA (Contact Page is short, no need for repeated CTA)
- Map/Location (complex to implement, rarely adds value for SaaS)
- Multiple forms on one page

Check `references/section-composition.md` for ordering rules, spacing, and conflict detection.

### Step 4: Generate Page Spec

Before writing code, produce a brief spec:

```
Page Spec:
- Product: [name] — [one-line description]
- Archetype: [A/B/C/D] — [name]
- Theme: Light / Dark
- Form fields: [list with required/optional markers]
- Sections (in order): [list]
- Contact info: [email, phone, address — or "placeholder"]
- Departments (B only): [list with CTA text]
- Social proof (C only): [customer logos / testimonial / both]
- Brand color: none (default) / [color] — --accent set to [value]
- Display font: default (DM Sans) / [font name] — tracking: [-0.02em / -0.01em]
- Not in scope: [real form submission, email delivery, CRM integration, etc.]
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
Spacing:   Section rhythm 180px, header top 80px, title-to-content 58px
Radius:    Buttons 2px, inputs 4px, dept cards 8px, content cards 16px
Shadows:   ZERO — depth via background color steps only
Transitions: transform 0.2s ease-in-out (hover), opacity 0.3s linear
Motion:      scroll entrance 0.8s, input focus 0.2s (see shared/interaction-patterns.md)
Grid:      max-width 1080px, gutter 24px
```

**Contact-specific tokens**:

```
Page header padding-top:   80px (more compact than Landing Page's 128px)
Header to content:         58px

Form input:      border: 1px solid var(--surface-2) / radius 4px / bg var(--bg)
                 padding: 8px 16px / font-size: 16px / font-family: var(--font-display)
                 focus: border-color var(--text) / outline none
Input label:     font-family: var(--font-display) / 14px / weight 500 / opacity 0.5
                 margin-bottom: 8px
Field group gap: 24px (margin-bottom between field groups)
Textarea:        min-height: 120px / resize: vertical / same styling as input
Select:          appearance: none / same styling as input / custom arrow via bg SVG
Submit button:   .btn-dark styles: bg var(--accent) / color var(--accent-text) / radius 2px
                 padding: 8px 16px / font: 14px/500 var(--font-display) / width: 100%
Privacy text:    font-size: 14px / opacity 0.4 / margin-top: 16px
Checkbox:        16px × 16px / border: 1px solid var(--surface-2) / radius 2px

Split layout:    grid 1fr 1fr / gap 58px
Centered form:   max-width 640px / margin 0 auto

Dept card:       bg var(--surface-1) / radius 8px / padding 32px
                 icon: 40px / opacity 0.5 / gap 24px between cards
Dept card CTA:   primary (Sales) = .btn-dark / others = .btn-outline

Social proof:    customer logos: opacity 0.15 / gap 58px / grayscale
                 testimonial quote: 16px / weight 500 / line-height 1.6 (no italic — not in design system)
```

4. Check against `references/anti-patterns.md` — verify each design choice

**Implementation principles**:
- Semantic HTML (one h1, sections, nav, footer)
- Mobile-responsive (flexbox/grid, breakpoint at 767px (`@media (max-width: 767px)`))
- Single HTML file with inline `<style>` — include Google Fonts link for DM Sans + DM Mono
- Placeholder images: use `var(--surface-1)` background with mono-font label, not broken image links — only for photos or artwork the user must supply. Product screenshots are never a grey box: build them with `shared/product-visuals.md`
- Interactive states: hover `transform: translateY(-1px)` on buttons, `opacity` transition on links
- Form fields: include `required` attribute on mandatory fields, use `type="email"` for email
- **No real form submission** — form `action="#"` with `onsubmit="return false"` or no action
- Nav buttons must use explicit overrides if placed inside `.nav-links` (see `shared/navigation.md` CSS specificity section)

**Content handling**:
- Use the user's real content when provided (company name, email, address, departments)
- Every contact detail the user provides (email, phone, address) must appear on the page — even in form-first archetypes like C, show it beside or below the form
- Generate example content when not provided, clearly noting it's placeholder
- Never fabricate real email addresses, phone numbers, or physical addresses as real
- When the user gives no contact info, use obviously placeholder values (e.g., "hello@yourcompany.com", "123 Example Street")

### Step 6: Verify

After generating the page, run through `shared/quality-checklist.md`. Focus on these critical items:

> Visual checks below (color, shadow, radius, typography, spacing values) are written for Minimal. With another style active, check them against the active style file instead. Visual rules in `references/anti-patterns.md` follow the same precedence; content and structure rules apply in every style.

1. **Color**: Zero hue-tinted grays? CTA uses `var(--accent)`? Brand color (if any) only on allowed elements?
2. **Shadows**: Zero box-shadow anywhere? Form inputs use border, not shadow?
3. **Typography**: Labels in mono/uppercase where appropriate? Input text 16px? Section titles in display font?
4. **Spacing**: Section gap ≥ 180px? Header padding-top 80px? Field gaps 24px?
5. **Radius**: Inputs 4px? Buttons 2px? Dept cards 8px?
6. **Anti-patterns**: No gradient form backgrounds? No per-department accent colors? No decorative border-top on form?
7. **Responsive**: Form fills width on mobile? Dept cards stack? Split layout becomes single column?
8. **Animation**: `prefers-reduced-motion` guard present? Timing matches `shared/interaction-patterns.md`? No animation on nav/footer?

**Contact-specific checks**:
8. **Nav buttons visible**: Nav CTA button text visible against background? (Check CSS specificity — see shared/navigation.md)
9. **Input consistency**: All inputs (text/textarea/select) use same border/radius/bg style?
10. **Form fields appropriate**: Field count matches archetype? (A: 3-5, B: 4-6, C: 5-9)
11. **CTA text specific**: Submit button text matches archetype? (Not generic "Submit")
12. **Dept card CTAs differentiated** (B only): Each card has unique CTA text? Primary dept uses filled button?

If issues are found, fix them before delivering.

### Step 7: Deliver

Provide:
1. The page file(s) with instructions to open/run
2. A brief note on key design decisions (2-3 sentences)
3. What's in scope (visual presentation) vs. not implemented (real form submission, email delivery, CRM)

---

## Knowledge Files

| File | Content | When to Load |
|------|---------|-------------|
| `shared/visual-style.md` | **Design system**: default tokens, Light/Dark themes, component styles, brand customization rules | Step 5 (always — read FIRST) |
| `references/archetypes.md` | 4 contact page sub-types, selection guide, section combinations | Step 2 (always) |
| `references/contact-form.md` | **Core**: form layout, field composition, input styling, button patterns, two-column rules | Step 5 (always for A/B/C) |
| `references/contact-info.md` | Contact details display, multi-office, department contacts, social links | Step 5 (when contact info section included) |
| `references/department-routing.md` | Routing card layout, CTA differentiation, icon treatment, grid CSS | Step 5 (Archetype B only) |
| `references/page-header.md` | Header title strategy, label, subtitle, layout patterns, spacing | Step 5 (always for A/B/D) |
| `references/section-composition.md` | Section ordering, hard/soft rules, spacing, background colors | Step 3 (always) |
| `references/anti-patterns.md` | AI convergence traps, form errors, layout errors, visual errors, brand color reconciliation | Step 5 (always) |
| `shared/navigation.md` | Nav layout, CSS specificity trap for nav buttons | Step 5 (always) |
| `shared/footer.md` | Footer layout and content | Step 5 (always) |
| `shared/quality-checklist.md` | verification checklist | Step 6 (always) |
| `shared/interaction-patterns.md` | Motion tokens: scroll reveal, stagger, counter, hover lift recipes | Step 5 (always) |

---

## Constraints

- This Skill does NOT require Mobbin, external APIs, or internet access
- V1 scope: page skeleton + layout + components + visual quality
- NOT in V1: real form submission, email delivery, CRM integration, CAPTCHA, calendar/booking integration
- Output: runnable frontend code (HTML/CSS, or matching the user's project stack)
- All design knowledge is pre-distilled in the references/ directory
- Visual style defaults to the shared design system tokens; user-provided brand specs override only `--accent` / `--accent-text` and `--font-display`
- Set the form `action` to `#` or leave it empty — no real backend
- Contact information in examples must be obviously placeholder (not real company data)
