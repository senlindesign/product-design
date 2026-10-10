# Hero Section Skill

Generate a professional Hero section — the first content block visitors see. Works standalone or as part of a full page.

**Visual System**: `shared/visual-style.md` — default design tokens for Light/Dark themes. Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.
**Section Knowledge**: `pages/landing-page/references/hero.md` — patterns, variants, and anti-patterns from 30+ real product research.

---

## When to Use

- "Add a hero section to my page"
- "Create a hero banner for [product]"
- "Build the above-the-fold section"
- When a Page Skill needs a Hero — it references this knowledge internally

Do NOT use for:
- Blog post headers (different content structure)
- App-internal welcome screens

---

## Workflow

### Step 1: Understand Inputs

**Required**:
- Product name and one-line description
- Core value proposition (what + for whom + why)

**Defaults if not provided**:
- Theme → Light
- Hero pattern → Centered Stack (most common)
- Brand color → none (`--accent` = `--text`)
- Display font → the active style's display font (Minimal: DM Sans)

### Step 2: Select Pattern

Read `pages/landing-page/references/hero.md` and select:

| Pattern | Best When |
|---------|-----------|
| Centered Stack | Product has one strong UI screenshot; standard value pitch |
| Split (text + visual) | Need to show product context alongside explanation |
| Dark Background | Developer/technical audience; DevOps, API, CLI, or code tooling |
| Text-Only | Brand/narrative page; no product visual available |

**Dark Background** is a full pattern, not a theme toggle: background #0A0A0A–#1A1A1A (never pure #000), light text, and the main visual is a syntax-highlighted code block or terminal. Do NOT use it when the product serves non-technical users or when the only screenshot is a light UI — a light screenshot on a dark background reads as pasted-on.

**Button visibility on Dark Background hero**: `--accent` defaults to `var(--text)` = `#141414` on a light-theme page. A `.btn-dark { background: var(--accent) }` is nearly invisible on a `#141414` dark hero. Two options — choose one:
- **Dark-theme page** (recommended): set the page to dark theme (`--bg: #0A0A0A; --text: #EDEDED`). Then `--accent = #EDEDED` and the button is automatically visible.
- **Section-level override**: add `class="section-dark"` to the `<section>` element. This sets `background: var(--text) = #141414` and enables all `.section-dark .btn-dark` overrides (button becomes `background: var(--text-inverse)`). The background will be `#141414`, not `#0A0A0A` — slightly lighter, but buttons are visible.

### Step 3: Build

Read the active style file first (`shared/visual-style.md` for Minimal, the default). The tokens below are Minimal defaults — with another style active, take visual values from that style file per *Style precedence* in the master `SKILL.md`, and keep the layout and structure below:

```
Hero top padding:     128px, measured from the bottom of the nav. If the nav is
                      position: fixed it is out of flow — set
                      body { padding-top: var(--nav-h) } (68px) so this 128px
                      starts below the nav instead of at the viewport top.
Hero bottom padding:  180px (matches section rhythm — the visual gap between Hero
                      content bottom and the next section's content top will be
                      180 + 180 = 360px, which is the system's intended spacing)
Headline:             clamp(48px, 7vw, 80px) / weight 500 / tracking -0.02em / line-height 1.05
                      max-width 900px — without a measure the line breaks land arbitrarily
Subheadline:          18px / weight 400 / opacity 0.5 / max-width 540px
Headline → Sub gap:   24px
Sub → CTA gap:        48px
CTA → Visual gap:     58px
CTA button:           .btn-lg — 16px / 12px 24px padding / 2px radius / var(--accent) bg
                      Hero uses the large variant; nav CTA stays 14px so the two
                      do not read as the same button
CTA group gap:        12px (between primary and secondary buttons; flex gap)
                      Both buttons in Hero use .btn-lg for visual balance
Product visual:       70-90% width / surface-1 bg / 16px radius frame
                      See "Synthetic Product Visual" below — offline you will never
                      have a real screenshot, so you must construct one
```

**Structure** (top to bottom):
1. [Optional] Label — mono 12px, uppercase, opacity 0.4
2. Headline — one `<h1>`, the single biggest text on the page
3. [Optional] Subheadline — 1-2 sentences, opacity 0.5
4. CTA group — primary `.btn-dark` + optional secondary `.btn-outline`
5. Product visual — screenshot in `surface-1` frame, or text-only if no visual

**Rules**:
- Headline must be ≥3x body text size
- No illustrations, gradients, or abstract graphics — product content only
- No box-shadow — use background color steps for depth
- Center-aligned by default; left-aligned only for Split pattern

#### Synthetic Product Visual

"Use a product screenshot" is not actionable offline — there is no screenshot. The
visual occupies roughly half the Hero's area, so leaving it to improvisation is what
makes a page read as AI-generated. Build it out of real UI, in HTML/CSS.

**See `shared/visual-style.md` §8 → "Synthetic Product Visual"** for the complete token set, layout table (5 mock layout types by product category), and fill rules.

Key principle: fill the mock with content from the product's own domain. A scheduling tool shows real timezone names; a database tool shows real column names. Generic placeholders ("Item 1", "Lorem ipsum", empty grey rectangles) defeat the entire purpose.

#### Motion & Interaction

Reference: `shared/interaction-patterns.md`

- Do NOT apply scroll reveal — Hero is the first section visitors see; delaying its content is an anti-pattern (§13 Page-Type Map, §15 Anti-Patterns)
- Optional: **Text reveal** on `<h1>` — words appear one by one with 60ms stagger, 0.6s duration, translateY(12px), cubic-bezier(0.16, 1, 0.3, 1). Skip if heading exceeds 7 words (§7)
- Optional: **Counter animation** on KPI numbers — 2000ms duration, ease-out cubic: `1 - (1-t)^3`, triggered on `DOMContentLoaded` (not scroll — Hero is above the fold so IntersectionObserver never fires). Use `data-count-to` attributes; initial text must equal the final display value, not "0" (§5 and Hero load-trigger snippet in `shared/interaction-patterns.md`)
- All animations wrapped in `@media (prefers-reduced-motion: no-preference)`

### Step 4: Verify

Visual values in this checklist assume Minimal. With another style active, check against the active style file instead.

- [ ] Top padding ≥ 128px?
- [ ] Bottom padding = 180px (section rhythm)?
- [ ] Headline uses `clamp()` and tracks negative?
- [ ] Subheadline same color as headline, different only in opacity?
- [ ] CTA uses `var(--accent)` / `var(--accent-text)`?
- [ ] Product visual uses `var(--surface-1)` background, not shadow?
- [ ] Product visual contains real UI — labelled rows/columns/values from the product's
      own domain, not grey placeholder bars or "Item 1"?
- [ ] Works at 767px width?
- [ ] Zero box-shadow?

### Step 5: Deliver

Provide the section code (HTML + CSS). Note which pattern was chosen and why.

---

## Constraints

- No Mobbin or external API dependency
- V1: visual presentation only — CTA buttons are visual, no real navigation
- All design knowledge is pre-distilled in the referenced files
- Follow `shared/visual-style.md` tokens exactly — do not invent values
