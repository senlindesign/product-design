# How It Works Section Skill

Generate a professional How It Works section — a numbered process walkthrough that shows users how to get started. Works standalone or as part of a full page.

**Visual System**: `shared/visual-style.md` — default design tokens for Light/Dark themes. Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.
**Section Knowledge**: `pages/landing-page/references/how-it-works.md` — patterns, variants, and anti-patterns from 20 real product research.

---

## When to Use

- "Add a how it works section"
- "Show users how to get started with [product]"
- "Create a 3-step process section"
- When a Page Skill needs a How It Works — it references this knowledge internally

Do NOT use for:
- Feature lists (use Features section — capability-oriented, not process-oriented)
- Onboarding flows inside an app
- Technical documentation or tutorials

---

## Workflow

### Step 1: Understand Inputs

**Required**:
- Product name
- The actual steps a user takes (what happens at each stage)

**Defaults if not provided**:
- Theme → Light
- Pattern → Horizontal Steps (most common, 75% of observed products)
- Step count → 3
- Numbering style → zero-padded (01, 02, 03)
- Brand color → none (`--accent` = `--text`)
- Display font → the active style's display font (Minimal: DM Sans)

### Step 2: Select Pattern

Read `pages/landing-page/references/how-it-works.md` and select:

| Pattern | Best When |
|---------|-----------|
| Horizontal Steps | 3 short steps (1-2 sentences each); sufficient desktop width for side-by-side |
| Horizontal + Screenshots | Steps map to visible product UI; screenshots make the abstract concrete |
| Horizontal + CTA | The next step after the flow is an action (signup, install) |
| Vertical List | Step descriptions are longer (3+ sentences); steps have sequential dependency; screenshots per step |

**Step count guidance**:
- 3 steps — default; fits 75% of SaaS products
- 4 steps — only if the flow genuinely has 4 distinct stages
- Never 2 (section is unnecessary) or 5+ (too complex for this format)

**Content type** — decide based on product:
- **Action-oriented** ("Sign up", "Paste the script", "Watch visitors") — self-serve products
- **Value-oriented** ("Kickoff", "Model", "Strategize") — B2B / service products

### Step 3: Build

Read the active style file first (`shared/visual-style.md` for Minimal, the default). The tokens below are Minimal defaults — with another style active, take visual values from that style file per *Style precedence* in the master `SKILL.md`, and keep the layout and structure below:

```
Section padding:          180px top and bottom (section rhythm)
Section title → content:  58px gap
Content max-width:        1080px, centered, padding 0 32px

Section title:            clamp(32px, 4vw, 47px) / weight 500 / tracking -0.02em / line-height 1.1
Section subtitle:         18px / weight 400 / opacity 0.5 / max-width 540px / centered

Step number (zero-pad):   12px / mono / weight 400 / uppercase / tracking +0.72px / opacity 0.4
Step number (circled):    14px / weight 500 / var(--text) bg / var(--text-inverse) color / 24px circle
Step title:               20px / weight 500 / tracking -0.4px / line-height 1.3
Step description:         16px / weight 400 / opacity 0.5 / line-height 1.6

Horizontal columns:       3-col (or 4-col) equal-width grid / 24px gap
Vertical list gap:        58px between steps

Step title → description: 12px gap
Step number → title:      16px gap
```

**Numbering style selection** (match brand tone):
- **Zero-padded** (01, 02, 03) — modern, design-forward. Use mono font, opacity 0.4. Default choice.
- **Circled number** (1, 2, 3 in filled circle) — friendly, clear. Use `var(--text)` background, 24px diameter. Not `var(--accent)`: a filled circle behind a numeral is badge fill, which visual-style.md §1 forbids.
- **"Step X" label** — formal, educational. Use mono font, uppercase, opacity 0.4.
- **Large display number** — decorative. Use clamp(48px, 5vw, 64px), opacity 0.1, as background element.

**Connector lines** (optional, Horizontal pattern only):
- 1px solid `var(--surface-2)` between columns
- Or skip connectors entirely — the numbering implies sequence

**Structure** (top to bottom):
1. Section title — `<h2>`, centered, e.g. "How it works"
2. [Optional] Section subtitle — 1 sentence, opacity 0.5
3. Steps container — grid or vertical stack
4. Each step: number → title → description → [optional screenshot]
5. [Optional] CTA below steps — `.btn-dark`, centered, 58px above

**Screenshot frame** (if pattern includes screenshots):
- `var(--surface-1)` background
- 16px border-radius
- Zero box-shadow
- Placed below step description, 24px gap

**Rules**:
- Step titles must start with a verb (action-oriented) or noun (value-oriented) — never "Step 1 is about..."
- All steps have the same visual weight — no step looks "featured"
- No icons unless the user explicitly requests them
- No box-shadow anywhere
- No colored backgrounds per step — all steps share the page background
- Narrow screens (< 768px): horizontal grid collapses to vertical stack

#### Motion & Interaction

Reference: `shared/interaction-patterns.md`

- Scroll reveal on the section container: `translateY(32px)` / `0.8s` / `cubic-bezier(0.16, 1, 0.3, 1)` (§2)
- Step cards stagger at **150ms** interval (large blocks): `translateY(24px)` / `0.6s` duration (§3)
- All animations wrapped in `@media (prefers-reduced-motion: no-preference)`
- Reveal steps in sequence (01, then 02, then 03) to reinforce the process order

### Step 4: Verify

Visual values in this checklist assume Minimal. With another style active, check against the active style file instead.

- [ ] Section vertical padding = 180px?
- [ ] Section title uses `clamp()` and tracks negative?
- [ ] Step numbers use mono font at opacity 0.4 (zero-pad default) or circled style with `var(--text)` background — never `var(--accent)` background?
- [ ] Step titles are 20px / weight 500?
- [ ] Step descriptions are opacity 0.5, same color as titles?
- [ ] All steps have equal visual weight (no "featured" step)?
- [ ] Section title → content gap = 58px?
- [ ] Horizontal grid collapses to vertical stack at 767px?
- [ ] Zero box-shadow on all elements?
- [ ] Screenshots (if any) use `var(--surface-1)` background, not shadow?
- [ ] Step count is 3 or 4 (never 2 or 5+)?

### Step 5: Deliver

Provide the section code (HTML + CSS). Note which pattern was chosen and why.

---

## Constraints

- No Mobbin or external API dependency
- V1: visual presentation only — CTA buttons are visual, no real navigation
- All design knowledge is pre-distilled in the referenced files
- Follow `shared/visual-style.md` tokens exactly — do not invent values
