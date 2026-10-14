# Social Proof Section Skill

Generate a professional Social Proof section — testimonials, logo walls, stats, or ratings that establish credibility. Works standalone or as part of a full page.

**Visual System**: `shared/visual-style.md` — default design tokens for Light/Dark themes. Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.
**Section Knowledge**: `pages/landing-page/references/social-proof.md` — patterns, variants, and anti-patterns from 27 real product research.

---

## When to Use

- "Add a social proof section to my page"
- "Show customer testimonials"
- "Add a logo wall / trusted-by section"
- "Build a section with customer quotes and company logos"
- When a Page Skill needs Social Proof — it references this knowledge internally

Do NOT use for:
- Full case study pages (different content structure)
- Product review aggregation pages
- User-generated content feeds

---

## Workflow

### Step 1: Understand Inputs

**Required**:
- Product name
- Social proof assets available (logos, quotes, stats, ratings — at least one category)

**Defaults if not provided**:
- Theme --> Light
- Pattern --> Logo Wall (most common, lowest asset requirement)
- Brand color --> none (`--accent` = `--text`)
- Display font → the active style's display font (Minimal: DM Sans)

### Step 2: Select Pattern

Read `pages/landing-page/references/social-proof.md` and select:

| Pattern | Best When | Minimum Assets |
|---------|-----------|----------------|
| Logo Wall | Have 5+ recognizable client logos, need quick trust signal after Hero | 5 logos |
| Testimonial Cards | Have 3+ real customer quotes with names and titles | 3 quotes + attribution |
| Logo Wall + Testimonials | Have both logo assets and detailed quotes; need breadth and depth | 5 logos + 2-3 quotes |
| Enterprise Testimonial List | Clients are high-profile brands (Nike/Google tier); premium tone | 3+ quotes from major brands |
| Bento / Mosaic | Have mixed evidence types (quotes, metrics, logos) and want one dense block | 4-6 mixed tiles |

A logo wall of real customers shows only customers the user names. Take each logo from the sources in *Real logos only* (master `SKILL.md`): Simple Icons in one color suits a grayscale wall (`https://cdn.simpleicons.org/<slug>/<hex>`); a brand that no library has becomes a text wordmark. Never draw a logo and never show `[Company]` placeholder logos.

Stats / numbers are not a standalone pattern — they are a content type that slots into Bento / Mosaic or sits alongside a Logo Wall.

**Logo Wall sub-variants**:
- Single row (5-8 logos) — standard
- Double row (10-12 logos) — many clients
- Hero-embedded — logos at bottom of Hero section, not a separate section
- Scrolling marquee — many logos, limited horizontal space

**Testimonial sub-variants**:
- With avatars — circular photo + name + title (more personal)
- With quantified results — quotes containing specific numbers (most persuasive)
- With case study links — "View success story" CTA per card

### Step 3: Build

Read the active style file first (`shared/visual-style.md` for Minimal, the default). The tokens below are Minimal defaults — with another style active, take visual values from that style file per *Style precedence* in the master `SKILL.md`, and keep the layout and structure below:

**Logo Wall tokens**:
```
Section padding:        128px 32px (top/bottom, left/right)
Label:                  mono 12px / 400 / uppercase / +0.72px tracking / opacity 0.3
Label --> logos gap:     32px
Logo text placeholders: 16px / display font / weight 500 / opacity 0.15
Logo horizontal gap:    58px
Logo vertical align:    center
```

**Testimonial Card tokens**:
```
Section padding:        180px 32px (system section rhythm — 128px is Logo Wall only)
Card padding:           32px
Card background:        var(--bg) on surface-1 section, or var(--surface-1) on bg section
Card border-radius:     16px
Card shadow:            none (zero box-shadow)
Card gap:               24px (between cards)
Grid:                   3-column on desktop, 1-column below 768px

Quote font:             display / 16px / weight 500 / line-height 1.6
Quote color:            var(--text), no decorative quotation marks
Attribution font:       mono / 12px / uppercase / +0.72px tracking / opacity 0.4
Avatar:                 40px circle (if used)
Name + title gap:       4px
```

**Section title tokens**:
```
Section title:          clamp(32px, 4vw, 47px) / weight 500 / tracking -0.02em / line-height 1.1
Subtitle:               18px / weight 400 / opacity 0.5 / max-width 540px
Title --> subtitle gap: 24px
Title --> content gap:  58px
```

**Structure by pattern**:

**Logo Wall** (top to bottom):
1. [Optional] Label — "TRUSTED BY TEAMS AT" / "POWERING" / "LOVED BY" in mono 12px uppercase, opacity 0.3
2. Logo row(s) — all logos monochrome, opacity 0.15, horizontally centered, equal size

**Testimonial Cards** (top to bottom):
1. [Optional] Section label — mono 12px uppercase, opacity 0.4
2. Section title — e.g. "What our customers say"
3. 3-column card grid, each card containing:
   - Quote text (no decorative quote marks)
   - Attribution: Name / Title, Company in mono 12px uppercase, opacity 0.4
   - [Optional] Avatar photo, 40px circle

**Logo Wall + Testimonials** (top to bottom):
1. Label + Logo row (Logo Wall pattern)
2. 58px gap
3. 2-3 Testimonial cards below

**Rules**:
- All logos must be monochrome — use text placeholders at opacity 0.15 if no SVG assets
- No box-shadow on any element
- Testimonial background and section background must differ by one step: card on `var(--bg)` if section is `var(--surface-1)`, or card on `var(--surface-1)` if section is `var(--bg)`
- Attribution always in mono font, never in display font
- Center-aligned by default for both Logo Wall and Testimonial Cards
- Section padding: 128px top/bottom for bare Logo Wall only; 180px for Testimonial Cards and all other patterns (matches system section rhythm)

#### Motion & Interaction

Reference: `shared/interaction-patterns.md`

- **Scroll reveal** on the `<section>`: translateY(32px), opacity 0 to 1, 0.8s cubic-bezier(0.16, 1, 0.3, 1) (§2)
- **Stagger**: testimonial cards and logo items enter with 80ms interval, translateY(16px), 0.5s duration. Use `data-stagger-child="small"` for logos (§3)
- Optional: **Marquee** for logo walls — 30s per full cycle, pure CSS, pauses on hover. Duplicate logo set for seamless loop (§6)
- All animations wrapped in `@media (prefers-reduced-motion: no-preference)`; marquee uses `@media (prefers-reduced-motion: reduce)` to disable

### Step 4: Verify

Visual values in this checklist assume Minimal. With another style active, check against the active style file instead.

- [ ] No fabricated testimonials or fake company names?
- [ ] Logo placeholders at opacity 0.15 (not higher)?
- [ ] Attribution uses mono font at 11px / uppercase / opacity 0.35?
- [ ] Quote text at 16px / weight 500 / line-height 1.6?
- [ ] Card padding is 32px with 16px border-radius?
- [ ] Zero box-shadow on cards and all other elements?
- [ ] Section vertical padding — 128px for a bare Logo Wall, 180px for every other pattern?
- [ ] Card background differs from section background by one surface step?
- [ ] Logos are monochrome and equal-sized?
- [ ] Works at 767px width (cards stack to single column)?
- [ ] All quotes include real attribution (name + title + company)?

### Step 5: Deliver

Provide the section code (HTML + CSS). Note which pattern was chosen and why.

---

## Constraints

- No Mobbin or external API dependency
- V1: visual presentation only — links and CTAs are visual, no real navigation
- All design knowledge is pre-distilled in the referenced files
- Follow `shared/visual-style.md` tokens exactly — do not invent values
- Testimonials the user didn't give are sample content (master `SKILL.md` Design Rules → *Sample content*): finished-looking quotes from fictional people, tagged `data-sample`, never presented as real
- Logo walls without user-given customers use invented companies (master `SKILL.md` *Sample content*) as **sample wordmarks**, tagged `data-sample` — never real customer logos
- **Sample wordmarks** — a row of names in one font at one weight reads as a placeholder strip. Real walls (Granola, incident.io, Linear customers) mix letterforms because every brand is different. Give each wordmark its own treatment using only the style's fonts: vary weight (400 / 500 / 600 where loaded), case (Title, lowercase, UPPERCASE with +0.08em tracking), family (display / body / mono), and optionally one leading geometric glyph from `● ◆ ▲ ✳ ◐ ■` at 0.9em. No two adjacent wordmarks share a treatment. Height and opacity stay uniform (the style's logo-wall opacity), so the row stays calm:
  ```html
  <div class="logo-row" data-section="logo-wall" data-layout="logo-row" data-bg="base" data-sample>
    <span class="wm" data-logo-source="wordmark" style="font-family:var(--font-display);font-weight:600">◆ Halberd</span>
    <span class="wm" data-logo-source="wordmark" style="font-family:var(--font-body);text-transform:lowercase">larkspur</span>
    <span class="wm" data-logo-source="wordmark" style="font-family:var(--font-mono);text-transform:uppercase;letter-spacing:.08em">Quarry &amp; Co</span>
    <span class="wm" data-logo-source="wordmark" style="font-family:var(--font-display);font-style:italic">Fernhill</span>
    <span class="wm" data-logo-source="wordmark" style="font-family:var(--font-body);font-weight:500">✳ brightmoor</span>
  </div>
  ```
