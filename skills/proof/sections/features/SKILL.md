# Features Section Skill

Generate a professional Features section — the block that communicates what the product does. Works standalone or as part of a full page.

**Visual System**: `shared/visual-style.md` — default design tokens for Light/Dark themes. Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.
**Section Knowledge**: `pages/landing-page/references/features.md` — patterns, variants, and anti-patterns from 26 real product research.

---

## When to Use

- "Add a features section to my page"
- "Show the product's key capabilities"
- "Build a grid of features for [product]"
- When a Page Skill needs a Features block — it references this knowledge internally

Do NOT use for:
- Pricing feature comparison tables (use Comparison Table section)
- Single-feature deep dives that belong in a Hero or dedicated product page
- Social proof / testimonials (use Social Proof section)

---

## Workflow

### Step 1: Understand Inputs

**Required**:
- Product name
- List of features (name + short description each)

**Defaults if not provided**:
- Theme → Light
- Pattern → for a product with a UI, 2 **M16 feature rows** (`shared/signature-moves.md`: product fragment at 7/12 width, alternating sides) for the main features; an Equal Grid only for a short "also included" list after them. An equal grid of icon cards as the *only* features section is the most recognisable template layout
- Feature count → 2 main features (rows) + up to 6 secondary (grid)
- Visual element → a product fragment per main feature; icons only in the secondary grid
- Brand color → none (`--accent` = `--text`)
- Display font → the active style's display font (Minimal: DM Sans)

### Step 2: Select Pattern

Read `pages/landing-page/references/features.md` and select:

| Pattern | Best When |
|---------|-----------|
| Equal Grid | 3-6 features of equal weight; each explainable in 1-2 sentences |
| Image-Text Alternating | Features need product screenshots to explain; 3-4 deep features |
| Full-Width Screenshot | Product UI itself is the best demo; one core interface to showcase |

**Feature count guide**:

| Count | Layout | Reason |
|-------|--------|--------|
| 3 | 3-col row or alternating | Room for depth per feature |
| 4 | 2x2 grid or alternating | Balance depth and breadth |
| 6 | 3x2 grid | Most common sweet spot |
| 8+ | Tab switching or grouped list | Prevents page bloat |
| 12+ | No-description checklist or tabbed categories | Dense platforms only |

### Step 3: Build

Read the active style file first (`shared/visual-style.md` for Minimal, the default). The tokens below are Minimal defaults — with another style active, take visual values from that style file per *Style precedence* in the master `SKILL.md`, and keep the layout and structure below:

**Section-level spacing**:
```
Section top/bottom padding:       180px (between sections)
Section title to content gap:     58px
Grid gutter (between cards):      24px
```

**Section header** (centered above the grid):
```
Label (optional):    12px / mono / 400 / uppercase / +0.72px tracking / opacity 0.4
Section title:       clamp(32px, 4vw, 47px) / weight 500 / tracking -0.02em / line-height 1.1
Section subtitle:    18px / weight 400 / opacity 0.5 / max-width 540px / centered
Label → Title gap:   16px
Title → Subtitle:    24px
```

**Feature card (Equal Grid pattern)**:
```
Card padding:        32px
Card radius:         8px
Card background:     var(--surface-1) or transparent (choose one, apply to all)
Icon size:           24-32px / opacity 0.5 / var(--text) color
Icon → Title gap:    16px
Card title:          20px / weight 500 / tracking -0.4px / line-height 1.3
Title → Description: 12px
Card description:    16px / weight 500 / opacity 0.5 / line-height 1.6
```

**Image-Text Alternating pattern**:
```
Text width:          ~40%
Image width:         ~60%
Image container:     var(--surface-1) bg / 16px radius
Row gap:             128px (between alternating rows)
Text title:          27px / weight 500 / tracking -0.54px / line-height 1.2
Text description:    18px / weight 400 / opacity 0.5 / line-height 1.6
```

**Grid responsive behavior**:
```
Desktop (>1024px):   3 columns
Tablet (768-1024px): 2 columns
Mobile (<768px):     1 column
```

**Rules**:
- Icons must be uniform style and size across all cards — do not mix styles
- All cards identical structure: icon + title + description (or all without icons)
- No box-shadow — use `var(--surface-1)` background or spacing alone for separation
- No colored icon backgrounds (no circles, no squares behind icons)
- No per-card accent colors — all cards use `var(--text)` only

#### Motion & Interaction

Reference: `shared/interaction-patterns.md`

- **Scroll reveal** on the `<section>`: translateY(32px), opacity 0 to 1, 0.8s cubic-bezier(0.16, 1, 0.3, 1) (§2)
- **Card stagger**: each card enters with 100ms interval, translateY(24px), 0.6s duration (§3)
- **Card hover lift**: translateY(-4px), transition 0.2s ease-in-out, with `border-color: var(--surface-2)` highlight (§4)
- **Reveal-to-hover handoff**: after entrance completes, swap `.reveal` for `.reveal-done` so hover `transform` does not conflict with entrance `transform` (§4)
- All animations wrapped in `@media (prefers-reduced-motion: no-preference)`

### Step 4: Verify

Visual values in this checklist assume Minimal. With another style active, check against the active style file instead.

- [ ] Section padding is 180px top and bottom?
- [ ] Section title uses `clamp()` and tracks negative?
- [ ] Title-to-content gap is 58px?
- [ ] All cards have identical structure (no one-off layouts)?
- [ ] Card titles are 20px / 500 weight with -0.4px tracking?
- [ ] Descriptions use opacity 0.5, not a different gray color?
- [ ] Icons are same size and style across all cards?
- [ ] No box-shadow anywhere in the section?
- [ ] No colored icon backgrounds?
- [ ] Grid collapses to 2-col at 767px, 1-col on mobile?
- [ ] Zero hue-tinted grays (no slate, zinc, cool-gray)?

### Step 5: Deliver

Provide the section code (HTML + CSS). Note which pattern was chosen and why.

---

## Constraints

- No Mobbin or external API dependency
- V1: visual presentation only — links and CTAs are visual, no real navigation
- All design knowledge is pre-distilled in the referenced files
- Follow `shared/visual-style.md` tokens exactly — do not invent values
