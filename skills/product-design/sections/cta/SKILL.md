# CTA Section Skill

Generate a professional Call-to-Action section — the closing conversion block that drives visitors to act. Works standalone or as part of a full page.

**Visual System**: `shared/visual-style.md` — default design tokens for Light/Dark themes. Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.
**Section Knowledge**: `pages/landing-page/references/cta.md` — patterns, variants, and copy strategies from 20 real product research.

---

## When to Use

- "Add a CTA section at the bottom of my page"
- "Create a final call-to-action block"
- "Build a conversion section with email signup"
- When a Page Skill needs a closing CTA — it references this knowledge internally

Do NOT use for:
- Hero CTA buttons (those belong to the Hero section)
- Inline CTA banners mid-page (use a styled div within the relevant section)
- Pricing page CTA rows (handled by Pricing Skill)

---

## Workflow

### Step 1: Understand Inputs

**Required**:
- Product name
- Primary conversion goal (signup, demo, contact, newsletter)
- CTA button label (e.g. "Start free trial", "Book a demo")

**Page context** (ask if generating standalone — Step 2 branches on it):
- Page theme, and whether the section immediately above is dark. Dark Full-Width
  against a dark neighbour has no contrast left to work with.
- Whether the page has persuasive content above (features, proof, FAQ). Minimal White
  closes on conviction the page already built; with nothing above it, it just ends.
- If both are unknown, use Dark Full-Width on a light page — it is the only pattern
  that carries its own visual weight.

**Defaults if not provided**:
- Theme → Light
- CTA pattern → Dark Full-Width (most common)
- Brand color → none (`--accent` = `--text`)
- Subheadline → omitted
- Reassurance text → omitted

### Step 2: Select Pattern

Read `pages/landing-page/references/cta.md` and select:

| Pattern | Best When |
|---------|-----------|
| Dark Full-Width | Page is light-themed; need a strong visual anchor at the bottom; primary goal is signup/trial |
| Minimal White | Brand is restrained; page already has enough persuasion above; single clear action |
| Dual-Channel | Two distinct audiences (e.g. self-serve + enterprise); need parallel conversion paths |

**Pattern constraints**:
- Dark Full-Width on a **light** page: uses `var(--text)` = #141414 background — strong dark anchor. This is the default and most common choice.
- Dark Full-Width on a **dark** page: uses `var(--text)` = #EDEDED background — produces a **light** section that inverts the page. Still provides maximum visual contrast. Use it. The `.section-dark .btn-dark` override in visual-style.md handles the button inversion.
- Dark Full-Width directly after a dark Hero: the transition from #0A0A0A Hero → #141414 Dark Full-Width has almost no contrast. Insert at least one light/neutral section between them.
- Minimal White: do NOT use if the page lacks persuasive content above — the minimal style relies on prior conviction. On a dark page, Minimal White uses `var(--bg)` = #0A0A0A, so it has **zero visual differentiation** from surrounding sections — avoid it on dark pages entirely.
- Dual-Channel: do NOT use for single conversion goals; columns stack on mobile so ensure each column is self-contained

### Step 3: Build

Read the active style file first (`shared/visual-style.md` for Minimal, the default). The tokens below are Minimal defaults — with another style active, take visual values from that style file per *Style precedence* in the master `SKILL.md`, and keep the layout and structure below:

```
Section padding:       180px top / 180px bottom (system section rhythm — see visual-style.md §3)
                       Note: if this CTA section directly follows the Hero, the visual gap
                       is Hero's bottom padding (180px) + this section's top padding (180px).
                       This 360px gap is intentional — see visual-style.md §3.
Max-width:             1080px centered, padding 0 32px
Headline:              clamp(32px, 4vw, 47px) / weight 500 / tracking -0.02em / line-height 1.1
Subheadline:           18px / weight 400 / opacity 0.5 / max-width 540px
Headline → Sub gap:    24px
Sub → CTA gap:         48px
CTA button (.btn-dark): 14px / weight 500 / 8px 16px padding / 2px radius / var(--accent) bg / var(--accent-text) color
Secondary btn:         .btn-outline — same size, transparent bg, 1px solid var(--surface-2)
CTA group gap:         12px (between primary and secondary buttons; use flex gap, not margin)
Reassurance text:      14px / opacity 0.4 / margin-top 16px
```

**Dark Full-Width variant** (additional tokens):
```
HTML class:            <section class="section-dark"> — REQUIRED.
                       Without this class, text and buttons remain var(--text) on a
                       var(--text) background and are invisible. The class is defined
                       in visual-style.md §8 and triggers all necessary color overrides.
Background:            set by .section-dark { background: var(--text); } — do not set it manually
Text color:            set by .section-dark { color: var(--text-inverse); } — do not set it manually
CTA button:            .section-dark .btn-dark overrides automatically (bg: text-inverse, color: text)
                       .section-dark .btn-outline overrides automatically (color: text-inverse, border: rgba(255,255,255,0.25))
Subheadline opacity:   0.5 (applies to the inherited text-inverse color)
Full viewport width:   width 100%, no max-width on the section container itself (not 100vw — that includes the scrollbar and causes horizontal overflow)
Inner content:         max-width 1080px centered within the full-width bg
```

**Dark Full-Width on a dark-theme page** (special case):
```
On a dark-theme page (--bg = #0A0A0A), var(--text) = #EDEDED.
A dark-band CTA with background: #EDEDED produces a LIGHT section that inverts the page.
This still provides visual contrast. The .section-dark overrides still apply correctly.
Do NOT apply .section-dark to normal dark-theme sections — only to sections that set
background: var(--text) as a deliberate contrast band.
```

**Dual-Channel variant** (additional tokens):
```
Layout:                2-column grid, gap 58px
Column alignment:      each column vertically centered
Column divider:        optional 1px solid var(--surface-2) between columns
Mobile (< 768px):      single column stack, 58px gap between blocks
```

**Structure** (top to bottom):
1. [Optional] Label — mono 12px, uppercase, opacity 0.4
2. Headline — one short, direct line (more urgent than Hero headline)
3. [Optional] Subheadline — 1 sentence max, opacity 0.5
4. CTA group — primary `.btn-dark` + optional secondary `.btn-outline` or email input
5. [Optional] Reassurance — "No credit card required", "Free forever", etc.

**Copy rules** (from knowledge):
- Write the bottom CTA text more directly than the hero CTA — the user has scrolled the full page
- Do NOT duplicate the exact Hero CTA text; add urgency or specificity ("Start your free trial today" vs Hero's "Get started")
- Reassurance text addresses the final objection (cost, commitment, complexity)

**Rules**:
- Center-aligned by default; left-aligned only inside Dual-Channel columns
- No illustrations, gradients, or decorative backgrounds
- No box-shadow anywhere
- Email input (if used): `padding 8px 16px / border-radius 4px / border 1px solid var(--surface-2) / background var(--bg) / font-size 16px` — place inline with button on desktop, stack on mobile

#### Motion & Interaction

Reference: `shared/interaction-patterns.md`

- **Scroll reveal** on the `<section>`: translateY(32px), opacity 0 to 1, 0.8s cubic-bezier(0.16, 1, 0.3, 1) (§2)
- No stagger, no hover lift, no counter — CTA must load clean and fast with a single entrance
- All animations wrapped in `@media (prefers-reduced-motion: no-preference)`

### Step 4: Verify

Visual values in this checklist assume Minimal. With another style active, check against the active style file instead.

- [ ] Section padding 180px top and bottom?
- [ ] Headline uses `clamp()` and negative tracking?
- [ ] Subheadline same color as headline, different only in opacity?
- [ ] CTA button uses `var(--accent)` / `var(--accent-text)` (or inverted equivalents for Dark Full-Width)?
- [ ] Dark Full-Width bg is `var(--text)` (not a random dark color)?
- [ ] Zero box-shadow on the entire section?
- [ ] Reassurance text (if present) is opacity 0.4, not a different gray?
- [ ] Works at 767px width — no horizontal overflow, buttons stack when they do not fit on one line?
- [ ] CTA copy differs from Hero CTA copy?
- [ ] Dual-Channel columns (if used) stack cleanly on mobile?

### Step 5: Deliver

Provide the section code (HTML + CSS). Note which pattern was chosen and why.

---

## Constraints

- No Mobbin or external API dependency
- V1: visual presentation only — CTA buttons are visual, no real form submission or navigation
- All design knowledge is pre-distilled in the referenced files
- Follow `shared/visual-style.md` tokens exactly — do not invent values
