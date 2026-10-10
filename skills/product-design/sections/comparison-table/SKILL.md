# Comparison Table Section Skill

Generate a professional Comparison Table section — a feature comparison grid that lets users scan differences across plans, products, or options. Works standalone or as part of a full page.

**Visual System**: `shared/visual-style.md` — default design tokens for Light/Dark themes. Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.
**Section Knowledge**: `pages/pricing-page/references/comparison-table.md` — patterns, variants, and anti-patterns from 65+ real product research.

---

## When to Use

- "Add a feature comparison table to my pricing page"
- "Create a plan comparison grid"
- "Build a side-by-side product comparison"
- When a Page Skill needs a Comparison Table — it references this knowledge internally
- Outside pricing: product vs. competitor tables, edition comparisons, service tier breakdowns

Do NOT use for:
- Simple feature lists within a single card (use the card's own feature list)
- Fewer than 4 feature differences (list them directly in tier cards instead)
- Data tables for app-internal dashboards or analytics

---

## Workflow

### Step 1: Understand Inputs

**Required**:
- Column subjects (plan names, product names, or options being compared)
- Features to compare (group them by category when the user gives categories)

**Defaults if not provided**:
- Theme -> Light
- Pattern -> Full-Width Comparison Table (most common)
- Brand color -> none (`--accent` = `--text`)
- Display font → the active style's display font (Minimal: DM Sans)
- Feature count -> assume 10-20, grouped into 3-4 categories

### Step 2: Select Pattern

Read `pages/pricing-page/references/comparison-table.md` and select:

| Pattern | Best When |
|---------|-----------|
| Full-Width Table | 3-4 columns, 10-30 features, need category grouping. Default choice. |
| Expandable Table | 15+ features; show 5-8 core rows initially, expand on click |
| With Header CTAs | Table is long (scrolls past one viewport); sticky header with small action buttons per column |

### Step 3: Build

Read the active style file first (`shared/visual-style.md` for Minimal, the default). The tokens below are Minimal defaults — with another style active, take visual values from that style file per *Style precedence* in the master `SKILL.md`, and keep the layout and structure below:

```
Container:            max-width 1080px / margin 0 auto / padding 0 32px
Table:                width 100% / border-collapse collapse / no border on table itself

Header row:           font-family var(--font-display) / 14px / weight 500 / color var(--text)
                      text-align center / padding 16px 12px
                      border-bottom 1px solid var(--surface-2)
                      sticky: position sticky / top var(--nav-h) / background var(--bg) / z-index 10
                      (top: var(--nav-h) = 68px — header row sits flush below the fixed nav,
                       not hidden behind it. top: 0 would slide under the nav on scroll.)
Header first-child:   text-align left / width 35%

Category header:      font-family var(--font-display) / 16px / weight 500 / color var(--text)
                      padding 32px 0 16px 0 / border-bottom 1px solid var(--surface-2)

Data rows:            border-bottom 1px solid var(--surface-2)
Data cells:           font-family var(--font-display) / 14px / weight 400 / color var(--text)
                      padding 16px 12px / line-height 1.6
                      first-child text-align left / others text-align center

Check mark (yes):     character ✓ / color var(--text) / opacity 0.4 / 16px
Check mark (no):      character — (em dash) / color var(--text) / opacity 0.2 / 16px
Text values:          font-family var(--font-display) / 14px / weight 400 / color var(--text) / opacity 1

Expand trigger:       14px / weight 500 / color var(--text) / opacity 0.5
                      background none / border none / cursor pointer
                      hover: opacity 1 / transition opacity 0.3s linear

Header CTA (if used): 12px / padding 6px 12px / margin-top 8px
                      recommended column: .btn-dark / others: .btn-outline
```

**Structure** (top to bottom):
1. [Optional] Section label — mono 12px, uppercase, opacity 0.4
2. [Optional] Section heading — "Compare plans", "Feature comparison"
3. [Optional] Expand trigger — if using Expandable pattern, place above table
4. Table header row — column subjects (plan/product names), first column = "Features" or blank
5. Category header rows — group name spanning full width, separating feature groups
6. Data rows — feature name in first column, values/checks in remaining columns
7. [Optional] Header CTAs — small buttons under each plan name in sticky header

**Rules**:
- Boolean values use ✓ / — only. Never Yes/No, never colored checkmarks (no green/red)
- Text values ("10GB", "Unlimited", "Up to 5 users") are plain text at full opacity
- 10+ features must be grouped into categories with category headers
- Category order: core features first, support/security last
- Each category: 3-8 features
- Zero box-shadow on any element
- Borders use `var(--surface-2)` only, 1px solid
- Mobile: wrap the `<table>` in a separate `<div class="table-scroll-wrapper">` with `overflow-x: auto`.
  Do NOT put overflow-x: auto on the section container — that traps the sticky header and prevents
  horizontal-scroll from working. Do not give the wrapper div a max-width; let it fill the container.
  First column: `position: sticky; left: 0; background: var(--bg); min-width: 160px`

#### Motion & Interaction

Reference: `shared/interaction-patterns.md`

- Scroll reveal on the section container: `translateY(32px)` / `0.8s` / `cubic-bezier(0.16, 1, 0.3, 1)` (§2)
- Table rows stagger at **80ms** interval (small items): `translateY(16px)` / `0.5s` duration (§3)
- All animations wrapped in `@media (prefers-reduced-motion: no-preference)`
- Category header rows do not stagger separately — they follow the same row sequence

### Step 4: Verify

Visual values in this checklist assume Minimal. With another style active, check against the active style file instead.

- [ ] Table container max-width 1080px?
- [ ] Header row is position sticky with `var(--bg)` background?
- [ ] Feature name column is 35% width and left-aligned?
- [ ] Value columns are center-aligned?
- [ ] Boolean values use ✓ (opacity 0.4) and — (opacity 0.2), no color?
- [ ] Category headers have 32px top padding separating groups?
- [ ] All borders are 1px solid `var(--surface-2)`, no other border styles?
- [ ] Zero box-shadow anywhere?
- [ ] Text hierarchy uses opacity, not different colors?
- [ ] Mobile: first column sticky left, table wrapper has overflow-x auto?
- [ ] 10+ features are grouped into categories?
- [ ] Works at 767px width?

### Step 5: Deliver

Provide the section code (HTML + CSS). Note which pattern was chosen and why.

---

## Constraints

- No Mobbin or external API dependency
- V1: visual presentation only — header CTAs are visual, no real navigation
- All design knowledge is pre-distilled in the referenced files
- Follow `shared/visual-style.md` tokens exactly — do not invent values
