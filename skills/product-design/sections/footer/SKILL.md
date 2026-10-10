# Footer Section Skill

Generate a professional Footer section — the closing navigation and information block at the bottom of the page. Works standalone or as part of a full page.

**Visual System**: `shared/visual-style.md` — default design tokens for Light/Dark themes. Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.
**Section Knowledge**: `shared/footer.md` — patterns, variants, and design decisions from 28 real product research.

---

## When to Use

- "Add a footer to my page"
- "Create a site footer with links and social icons"
- "Build the bottom navigation section"
- When a Page Skill needs a Footer — it references this knowledge internally

Do NOT use for:
- App-internal bottom bars or tab navigation
- Single-section landing pages with no navigation needs

---

## Workflow

### Step 1: Understand Inputs

**Required**:
- Product name
- Footer link groups (column names + link labels)

**Page context** (ask if generating standalone — Step 2 branches on it):
- Does the page already have a Bottom CTA section? If unknown, assume yes and skip
  the Pre-footer CTA pattern. A duplicate CTA is worse than a missing one.

**Defaults if not provided**:
- Theme → Light
- Footer pattern → Multi-Column Links (most common)
- Brand color → none (`--accent` = `--text`)
- Display font → the active style's display font (Minimal: DM Sans)
- Social platforms → Twitter/X, LinkedIn, GitHub, YouTube
- Copyright year → current year

### Step 2: Select Pattern

Read `shared/footer.md` and select:

| Pattern | Best When |
|---------|-----------|
| Multi-Column Links + Newsletter | 15-30 links; want email collection; standard SaaS footer |
| Pre-footer CTA + Minimal Links | Page has no separate Bottom CTA section; need conversion close |
| Giant Brand Wordmark | Design-driven brand; strong visual identity; combine with another pattern |
| Minimal Single Row | < 12 links; simple product; page is overall minimalist |

**Key decision**: If the page already has a Bottom CTA section, choose Multi-Column Links or Minimal Single Row — never Pre-footer CTA (avoids duplication).

### Step 3: Build

Read the active style file first (`shared/visual-style.md` for Minimal, the default). The tokens below are Minimal defaults — with another style active, take visual values from that style file per *Style precedence* in the master `SKILL.md`, and keep the layout and structure below:

```
Footer top padding:       128px
Footer bottom padding:    48px
Note:                     The gap between footer content and the section above is
                          the section above's bottom padding (180px) + this 128px = 308px.
                          Footer uses 128px (not 180px) because it is an ending zone, not
                          a content section in the rhythm.

Column layout:            CSS Grid, 3-5 columns, gap 24px
Column sizing:            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr))
                          First column (with logo + description) can span 2 columns
                          if the footer has 4+ link groups
Column title:             12px / mono / 400 / uppercase / +0.72px tracking / opacity 0.4
Column link:              14px / weight 400 / opacity 0.5 → hover opacity 1
Column link line-height:  1.6
Column link gap:          12px (between stacked links)
Column title → first link: 16px
Columns → bottom bar:    58px (standard heading-to-content distance)
Bottom bar padding-top:   32px (above the border-top separator)

Copyright text:           12px / mono / 400 / uppercase / +0.72px tracking / opacity 0.2
Legal links:              14px / weight 400 / opacity 0.4

Social icon size:         20px (SVG viewBox) / opacity 0.4 → hover opacity 1
Social icon gap:          16px

Logo in footer:           Same as nav logo — product name in 18px weight 500
```

**Structure** (top to bottom):
1. [Optional] Pre-footer CTA — only if Pattern 2 selected; large headline + CTA button
2. Main link columns — 3-5 columns with category title + stacked links
3. [Optional] Newsletter — email input + submit button, right column or below links
4. Bottom bar — logo (left) + copyright + legal links (center or left) + social icons (right)
5. [Optional] Giant wordmark — brand name in display font, very large, opacity 0.05-0.1

**Background color rules**:
- Light theme: use `var(--bg)` with a top border `1px solid var(--surface-2)` to separate from content
- Dark theme: use `var(--surface-1)` to create a "page ends here" signal (never a `var(--text)` band — it is light in dark mode)
- Never use brand color as full footer background

**Rules**:
- Column titles use mono font (DM Mono) — same label treatment as rest of system
- Links use the display font at 14px, weight 400 — one step lighter than nav links
- All hierarchy through opacity, not color changes
- No box-shadow anywhere
- No decorative icons next to links
- Social icons are monochrome SVG, not colored brand icons
- Newsletter input follows the system default input style: 4px radius, `var(--bg)` background, `1px solid var(--surface-2)` border, `8px 16px` padding (see `sections/contact-form/SKILL.md`)

#### Motion & Interaction

Footer does not use entrance animations (see `shared/interaction-patterns.md` §15 Anti-Patterns).

### Step 4: Verify

Visual values in this checklist assume Minimal. With another style active, check against the active style file instead.

- [ ] Footer top padding = 128px?
- [ ] Column titles use mono 12px uppercase with +0.72px tracking?
- [ ] Link text uses opacity 0.5 with hover → opacity 1 transition?
- [ ] Copyright text opacity 0.2-0.3?
- [ ] Social icons monochrome, 20px, opacity 0.4 with hover transition?
- [ ] Zero box-shadow on entire footer?
- [ ] Legal links present (Terms, Privacy at minimum)?
- [ ] No CTA duplication (if page has separate CTA section)?
- [ ] Works at 767px width (columns stack to 2-col or single-col)?
- [ ] All colors use `var()` tokens from visual-style.md?

### Step 5: Deliver

Provide the section code (HTML + CSS). Note which pattern was chosen and why.

---

## Constraints

- No Mobbin or external API dependency
- V1: visual presentation only — links are visual, no real navigation targets
- All design knowledge is pre-distilled in the referenced files
- Follow `shared/visual-style.md` tokens exactly — do not invent values
