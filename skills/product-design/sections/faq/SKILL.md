# FAQ Section Skill

Generate a professional FAQ section — an accordion-based block that addresses common questions and reduces friction before conversion. Works standalone or as part of a full page.

**Visual System**: `shared/visual-style.md` — default design tokens for Light/Dark themes. Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.
**Section Knowledge**: `pages/landing-page/references/faq.md` — patterns, variants, and anti-patterns from 22 real product research.

---

## When to Use

- "Add a FAQ section to my page"
- "Create a frequently asked questions block"
- "Build an accordion Q&A section for [product]"
- When a Page Skill needs a FAQ — it references this knowledge internally

Do NOT use for:
- Help center / knowledge base pages (different structure and navigation)
- In-app tooltips or contextual help

---

## Workflow

### Step 1: Understand Inputs

**Required**:
- Product name
- 3-8 question/answer pairs (or enough product context to generate them)

**Defaults if not provided**:
- Theme → Light
- Layout → Centered Single-Column Accordion (most common)
- Question count → 5 (standard coverage)
- Title → "Frequently Asked Questions"
- Brand color → none (`--accent` = `--text`)
- Display font → the active style's display font (Minimal: DM Sans)

### Step 2: Select Pattern

Read `pages/landing-page/references/faq.md` and select:

| Pattern | Best When |
|---------|-----------|
| Centered Single-Column Accordion | Questions ≤ 6; answers are 1-3 paragraphs; standard FAQ |
| Two-Column (Title + Accordion) | Desktop needs horizontal space usage; title area has extra description text; left-fixed title + right scrollable list |
| Two-Column Grid Accordion | Questions ≥ 6; answers are short (1-2 sentences); need density without page stretch |

**Variants** (apply on top of any pattern):
- **Numbered** — prefix questions with 01, 02, 03 for added structure
- **With bottom CTA** — "Still have questions? Contact us" link below the accordion

**Question count guidance**:
- 3-4: minimal, product is simple or page already explains well
- 5-7: standard, covers core concerns
- 8+: add category subheadings, or recommend a dedicated FAQ page

### Step 3: Build

Read the active style file first (`shared/visual-style.md` for Minimal, the default). The tokens below are Minimal defaults — with another style active, take visual values from that style file per *Style precedence* in the master `SKILL.md`, and keep the layout and structure below:

```
Section padding:          180px top and bottom (section rhythm)
Section title:            clamp(32px, 4vw, 47px) / weight 500 / tracking -0.02em / line-height 1.1
Title → subtitle gap:     24px
Title → accordion gap:    58px (standard title-to-content distance)
Accordion max-width:      700-800px (centered single-column) or 100% (two-column layouts)

Question text:            20px / weight 500 / tracking -0.4px / line-height 1.3 / DM Sans
Answer text:              18px / weight 400 / tracking normal / line-height 1.6 / system sans (Body font)
Answer opacity:           0.5
Question → answer gap:    16px
Item vertical padding:    24px top and bottom
Item separator:           1px solid var(--surface-2)

Expand/collapse icon:     + / - or chevron V / ^, 20px, opacity 0.4
Icon transition:          transform 0.3s ease (rotate for + icon); from interaction-patterns.md §10
Answer reveal transition: max-height 0.4s cubic-bezier(0.16, 1, 0.3, 1); from interaction-patterns.md §10

Bottom CTA text:          16px / weight 500 / opacity 0.5
Bottom CTA gap:           58px below last item
```

**Two-column (Title + Accordion) specifics**:
```
Left column:              30-35% width (title + optional subtitle)
Right column:             remaining space (accordion)
Narrow screen (<768px):   stack vertically — title on top, accordion below
```

**Two-column Grid specifics**:
```
Grid columns:             2 equal columns
Column gap:               24px
Questions split evenly between columns
Narrow screen (<768px):   single column
```

**Structure** (top to bottom):
1. Section title — one `<h2>`, centered or left-aligned per pattern
2. [Optional] Subtitle — 1-2 sentences, opacity 0.5, max-width 540px
3. Accordion list — JS toggle using `initAccordion()` pattern (see §10 of `shared/interaction-patterns.md`); each item = `<button class="accordion-trigger">` + `<div class="accordion-body">`. Do NOT use `<details>`/`<summary>` — no smooth animation support.
4. [Optional] Bottom CTA — "Still have questions?" with contact link

**Rules**:
- Default-expand the first question so users understand the interaction model
- Questions are full sentences, not fragments — no trailing "..."
- Answers use Body font (system sans), not Display font — the family switch signals the shift from heading to content
- No box-shadow on accordion items — use `var(--surface-2)` border or spacing for separation
- Title uses "Frequently Asked Questions" unless user specifies otherwise — avoid forced creativity

#### Motion & Interaction

Reference: `shared/interaction-patterns.md`

- **Scroll reveal** on the `<section>`: translateY(32px), opacity 0 to 1, 0.8s cubic-bezier(0.16, 1, 0.3, 1) (§2)
- **Accordion open/close**: Use `initAccordion()` from `shared/interaction-patterns.md §10` — `max-height` transition with keyboard navigation and ARIA. This is a UI interaction, not an entrance animation. Do NOT use `<details>`/`<summary>` — it does not support smooth `max-height` transitions without hacks.
- No stagger on individual FAQ items — they are a single list, not a grid of independent cards
- All animations wrapped in `@media (prefers-reduced-motion: no-preference)`

### Step 4: Verify

Visual values in this checklist assume Minimal. With another style active, check against the active style file instead.

- [ ] Section padding is 180px top and bottom?
- [ ] Title uses `clamp()` and tracks negative?
- [ ] Title-to-accordion gap is 58px?
- [ ] Question text is 20px / weight 500 / DM Sans?
- [ ] Answer text is 18px / weight 400 / system sans (Body font)?
- [ ] Answer text uses opacity 0.5, same color as question?
- [ ] First question is expanded by default?
- [ ] Item separators use `var(--surface-2)`, not box-shadow?
- [ ] Expand/collapse icon is present and transitions smoothly?
- [ ] Works at 767px width (stacks to single column if two-column)?
- [ ] Zero box-shadow anywhere in the section?

### Step 5: Deliver

Provide the section code (HTML + CSS + minimal JS for accordion toggle). Note which pattern was chosen and why.

---

## Constraints

- No Mobbin or external API dependency
- V1: visual presentation only — bottom CTA links are visual, no real navigation
- All design knowledge is pre-distilled in the referenced files
- Follow `shared/visual-style.md` tokens exactly — do not invent values
- Accordion JS must be vanilla — no framework dependency
