# Anti-Patterns — About Page

> Source: ~53 section observations across ~41 unique products + lessons from Landing/Pricing/Contact/404/Section Skills practice. Every rule validated against `shared/visual-style.md`.

---

## 1. Visual Errors

### 1.1 Stock Team Photos or AI-Generated Faces

**Problem**: The team section uses stock photography, AI-generated portraits, or generic silhouette avatars.
**Why it's wrong**: The design system's fourth principle is "Content as decoration" — reject stock photos (`shared/visual-style.md` Design Philosophy, item 4). Stock team photos are the single most obvious marker of an AI-generated About page. Real products use actual team member photos.
**Correct approach**: Use placeholder rectangles with name + title text. The placeholder communicates "photo goes here" without fabricating faces.

```css
.team-photo-placeholder {
    width: 96px;
    height: 96px;
    background: var(--surface-1);     /* #F5F5F5 light / #141414 dark */
    border-radius: 50%;               /* circle — matches team-section.md default */
}
```

**Checklist item**: Are all team photos either real (user-provided) or replaced with surface-1 placeholders?

---

### 1.2 Colored Icon Backgrounds for Values

**Problem**: Each value card has an icon on a colored circular or square background (e.g., green circle + lightbulb icon, blue circle + shield icon).
**Why it's wrong**: `shared/visual-style.md` section 1 explicitly prohibits icon backgrounds and badge fills: "`--accent` allowed uses (exhaustive)" lists only CTA button, nav CTA, pricing tier border, and link hover. "Icon backgrounds, badge fills, section backgrounds" are marked with a red cross. Evidence: 6/8 values observations use no icons at all.
**Correct approach**: Omit icons entirely (6/8 values observations are text-only). If a visual marker is needed, use a number or index: `01` / `02` / `03` in `var(--font-mono)` at `opacity: 0.4`.

```css
.value-number {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    color: var(--text);
    opacity: 0.4;
    margin-bottom: 16px;
}
```

**Checklist item**: Do any icons have colored backgrounds? If yes, remove the backgrounds or replace icons with numbered indices.

---

### 1.3 Illustrated Timeline Nodes

**Problem**: Timeline milestones use custom illustrations, 3D icons, or decorative graphics at each node point.
**Why it's wrong**: Custom illustrations violate "Content as decoration" (Design Philosophy, item 4). Evidence: 3/6 timeline observations use no visuals per milestone. The 2/6 that use illustrations (Apollo horizontal, Going) are highly brand-specific and not reproducible in a generic system. The system's alternative is a simple circle node.
**Correct approach**: Use small circles (`8px` diameter) on the timeline line, styled with `var(--surface-2)` border.

```css
.timeline-node {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    border: 2px solid var(--surface-2);   /* matches line color */
    background: var(--bg);
}
```

**Checklist item**: Are timeline nodes simple circles without illustrations?

---

### 1.4 Different Accent Colors per Value Card

**Problem**: Each value card uses a unique accent color (green for "Growth", blue for "Trust", purple for "Innovation").
**Why it's wrong**: The system uses a single accent color (`shared/visual-style.md` section 1: "chromatic color occupies <10% of visible page area"; section 1 forbidden list: "Different accent colors for individual feature cards"). About page values are no exception.
**Correct approach**: All value cards use the same styling. Differentiation comes from the content (title + description), not from color coding.
**Checklist item**: Do all value cards/items use the same color treatment?

---

### 1.5 Product Screenshots in About Hero

**Problem**: The About hero contains a product screenshot, dashboard preview, or app interface visual.
**Why it's wrong**: Evidence from 11 hero observations: 3/11 are text-only, 6/11 include team/workplace photos, 2/11 include brand illustrations — but 0/11 include product screenshots. The About hero's job is to state the company's identity, not demonstrate the product. Product screenshots belong on the Landing page hero. See `about-hero.md`.
**Correct approach**: About hero is a text section. Centered heading + body text. No visual element.
**Checklist item**: Is the About hero free of product screenshots?

---

### 1.6 Giant Team Photos Dominating the Layout

**Problem**: Full-bleed team group photos, office photography galleries, or culture photo montages that occupy large portions of the page.
**Why it's wrong**: The system's "Content as decoration" principle means product content (screenshots/output) is the visual, not photography. Photos that the user cannot provide are a fabrication risk. Evidence: while 11/12 team observations include photos, they are contained within grid cards (headshots), not full-bleed layouts. Full-bleed photos (ElevenLabs photo strip, Dropbox background photo) are exceptions.
**Correct approach**: Team member photos appear as contained elements within the grid (square or circle, constrained to card width). If the user provides no photos, use `var(--surface-1)` placeholder rectangles. Never fabricate team photos.

```css
.team-member-photo {
    width: 96px;
    height: 96px;
    background: var(--surface-1);     /* placeholder when no real photo provided */
    border-radius: 50%;               /* circle — matches team-section.md default */
    object-fit: cover;                /* when real photo is provided */
}
```

**Checklist item**: Are team photos contained within grid cards, not full-bleed?

---

### 1.7 Decorative Gradients on Timeline Lines

**Problem**: The timeline's connecting line uses a gradient (e.g., purple-to-blue, gray-to-transparent).
**Why it's wrong**: The system uses zero gradients (`shared/visual-style.md` section 1: "Gradient CTA buttons" forbidden; "Semi-transparent colored overlays" forbidden). Evidence: ClickUp uses gradient dots on its timeline — this is a brand-specific treatment, not reproducible in the system.
**Correct approach**: Timeline line is a solid 2px line in `var(--surface-2)`.

```css
.timeline-line {
    width: 2px;
    background: var(--surface-2);     /* #E9E9E9 light / #1F1F1F dark */
}
```

**Checklist item**: Is the timeline line a solid color without gradients?

---

### 1.8 Box-Shadow on Team Cards or Value Cards

**Problem**: Team member cards or value cards use `box-shadow` for depth.
**Why it's wrong**: The system uses zero shadows (`shared/visual-style.md` section 5: "No element on the entire site uses box-shadow"). Hierarchy is established through background color steps (`var(--bg)` / `var(--surface-1)` / `var(--surface-2)`) and borders.
**Correct approach**: Cards use `background: var(--surface-1)` with no shadow. For additional depth, use `border: 1px solid var(--surface-2)`.
**Checklist item**: Does any card element use box-shadow? If yes, remove it.

---

### 1.9 Serif or Italic Headings

**Problem**: Section headings use a serif font, italic styling, or decorative typeface for an "editorial" or "premium" feel.
**Why it's wrong**: The system locks display text to `var(--font-display)` (DM Sans) at weight 500 (`shared/visual-style.md` section 2). Evidence: while 5/11 hero observations and 3/12 team observations use serif headings (Intercom, Webflow, Miro), these are brand-specific choices. The system does not include serif in its three-font stack. Hierarchy comes from font family switching (display vs mono vs body), not from serif/sans contrast.
**Correct approach**: All headings use `font-family: var(--font-display); font-weight: 500`. No serif, no italic, no weight 700.
**Checklist item**: Are all headings in DM Sans at weight 500?

---

### 1.10 CTA Pushing Product Conversion

**Problem**: The About page CTA section uses "Start free trial" / "Get started" / "Sign up now" — the same conversion CTA as the Landing page.
**Why it's wrong**: Evidence: 5/6 CTA observations link to careers ("Join the team" / "See open positions"). 0/6 link to product signup. The About page's natural endpoint is "join this team" or "work with us." Product conversion CTAs on the About page feel misplaced — the user came to learn about the company, not to buy.
**Correct approach**: CTA heading: "Join the team" / "Join us" / "We're hiring" / "Work with us". Button text: "See open positions" / "View careers" / "Get in touch". If the company is not hiring, use a contact-focused CTA ("Get in touch" / "Say hello").
**Checklist item**: Does the CTA link to careers or contact, NOT to product signup?

---

## 2. Content Errors

### 2.1 Fabricated Company Metrics

**Problem**: The stats section shows invented numbers ("10,000+ customers", "50 countries") that are not provided by the user.
**Why it's wrong**: Same principle as the Landing page: no fabricated metrics (`shared/quality-checklist.md`). Stats must come from user input. If the user provides no stats, omit the stats section entirely.
**Correct approach**: Stats section content is user-provided. If the user says "we have 200 employees, founded in 2020, serve 5000 customers in 30 countries" — use exactly those numbers. If no stats are provided, skip the section.
**Checklist item**: Are all stats real (user-provided) or is the section omitted?

---

### 2.2 Fabricated Team Member Names and Titles

**Problem**: The team section shows invented names, titles, and bios.
**Why it's wrong**: Invented identities presented as real staff are deceptive.
**Correct approach**: Use the names the user gave. Otherwise use sample content (master `SKILL.md` Design Rules → *Sample content*): fictional names and roles with illustrated avatars, tagged `data-sample` and listed in the QA report. Never use real people's names or photos.
**Checklist item**: Is every team member either user-provided or tagged `data-sample`?

---

### 2.3 Fabricated Founding Story

**Problem**: The story/origin section contains an invented narrative about the company's founding.
**Why it's wrong**: A fabricated origin story is fiction presented as fact.
**Correct approach**: Use the user's story. Otherwise write a sample story (master `SKILL.md` Design Rules → *Sample content*) built only from what the user said (the problem, the product, the audience) with no invented dates, founders, or funding, tagged `data-sample` and listed in the QA report.
**Checklist item**: Is the story user-provided or tagged `data-sample`?

---

## 3. Structural Errors

### 3.1 Alternating Section Background Colors

**Problem**: Sections alternate between white and gray backgrounds (hero white, team gray, values white, stats gray).
**Why it's wrong**: `shared/visual-style.md` section 8: "Not allowed: different background colors for different sections." At most 1-2 sections use `var(--surface-1)`, the rest use `var(--bg)`. Evidence: most observed About pages maintain a consistent background with at most one differentiated band (stats section).
**Correct approach**: Default all sections to `var(--bg)`. Optionally, the stats section can use `var(--surface-1)` as a full-width band. See `section-composition.md`.
**Checklist item**: Are at most 1-2 sections on `var(--surface-1)`, with the rest on `var(--bg)`?

---

### 3.2 Values Section with Too Many Items

**Problem**: The values section displays 7+ values in a dense grid.
**Why it's wrong**: Evidence: value count ranges from 3-5 across observations (3: Grain; 4: Webflow, Attio; 5: Mews, Wispr Flow). No observation shows 7+ values. More than 5 values dilutes each one and creates visual clutter.
**Correct approach**: 3-5 values. If the user provides more, suggest consolidation or split into primary (displayed) and secondary (linked to a full values page).
**Checklist item**: Does the values section have 3-5 items?

---

### 3.3 Stats Section with Descriptions Instead of Labels

**Problem**: Each stat has a title, a paragraph of description, and a number — turning the stats section into a content-heavy feature section.
**Why it's wrong**: Evidence: 3/5 stats observations show number + label only (no descriptions). Stats are meant to impress at a glance — adding descriptions dilutes the visual impact of large numbers and slows the scanning pace.
**Correct approach**: Each stat is: large number + short label (2-4 words). No paragraphs. The Intercom sidebar pattern (number + label + description) is the exception, not the rule.

```css
.stat-number {
    font-family: var(--font-display);
    font-size: clamp(36px, 5vw, 56px);   /* page-specific: between section heading and hero heading */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
}

.stat-label {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;                /* button/nav — type scale */
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    margin-top: 8px;
}
```

**Checklist item**: Are stats displayed as number + short label without paragraphs?

---

## 4. When the User Provides a Brand Color

Adjustments when `--accent` is overridden with a brand color:

- **CTA button** changes from default (black/white) to the brand color via `var(--accent)` / `var(--accent-text)`. Standard `.btn-dark` behavior
- **1.2 does not relax**: No colored icon backgrounds, even in the brand color. The accent allowed-use list is exhaustive
- **1.4 does not relax**: No per-value-card color variation. All values use the same styling
- **1.7 does not relax**: Timeline line stays `var(--surface-2)`, not the brand color
- **1.8 does not relax**: Zero box-shadow, even for branded hover states. Use `transform: translateY(-1px)` + `filter: brightness()` per `shared/visual-style.md` section 10.1
- **1.9 does not relax**: Headings stay DM Sans 500, not a brand serif
- **Stat numbers stay `color: var(--text)`**: Numbers are too large for chromatic color (same reasoning as 404 numeral — occupies too much visual area)
- **Chromatic area < 10%** does not relax. On an About page, the CTA button is the primary chromatic element. Optional: link hover can use `var(--accent)` (allowed use)
- **Team photo placeholders stay `var(--surface-1)`**: Do not tint placeholders with the brand color

---

## 5. Verification Checklist

After generating the About page, verify the following:

1. **Is the hero text-only?** No product screenshots, no illustrations, no brand mascots
2. **Does the hero have a CTA button?** It should NOT (exception: careers link is acceptable)
3. **Does the CTA section link to careers or contact?** NOT to product signup/trial
4. **Are all team photos real (user-provided) or placeholder rectangles?** No stock photos, no AI faces
5. **Are all stats real (user-provided) or is the section omitted?** No fabricated metrics
6. **Is the story content user-provided or clearly templated?** No fabricated narratives
7. **Do value cards have colored icon backgrounds?** If yes, remove them
8. **Does any element use box-shadow?** If yes, remove it
9. **Is the page background `var(--bg)` with at most 1-2 `var(--surface-1)` sections?** No colored backgrounds
10. **Are all headings in DM Sans at weight 500?** No serif, no italic, no weight 700
11. **Is the button border-radius 2px?** No pills (999px)
12. **Are values limited to 3-5 items?** No 7+ value grids
13. **Is chromatic color area < 10%?** Only CTA button + optional link hover use `var(--accent)`
14. **Are stats displayed as number + short label?** No paragraph descriptions
15. **Is the full site navigation present?** Missing nav = error
