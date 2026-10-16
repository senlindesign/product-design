# Contact Form Section Skill

Generate a professional Contact Form section -- fields, labels, submit button, and optional privacy checkbox. Works standalone (embedded in any page) or as part of a Contact Page Skill.

**Visual System**: `shared/visual-style.md` -- default design tokens for Light/Dark themes. Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.
**Section Knowledge**: `pages/contact-page/references/contact-form.md` -- patterns, field rules, input styles, and CSS tokens from 22 real product research.

---

## When to Use

- "Add a contact form to my page"
- "Build a demo request form section"
- "Create a feedback/inquiry form for the landing page"
- When a Page Skill needs a Contact Form -- it references this knowledge internally
- Embedding a form in a support page, footer area, or modal

Do NOT use for:
- Login / signup / authentication forms (different field set and flow)
- Search bars or filter controls
- Multi-step wizards or checkout flows
- Newsletter signup (single email field -- too simple for this Skill)

---

## Workflow

### Step 1: Understand Inputs

**Required**:
- Purpose of the form (general contact, demo request, support inquiry)
- Approximate number of fields or field list

**Defaults if not provided**:
- Theme -> Light
- Layout -> Split (info left + form right) when the form is a page's main content — this is the source's recommended default and the most common Contact layout. Centered single column only when embedding the form inside another page, where there is no info column to pair it with
- Input style -> Full Border (Style A)
- Label placement -> Above input
- Submit -> Full-width solid button
- Fields -> Name, Email, Message (3-field minimum)
- Brand color -> none (`--accent` = `--text`)

### Step 2: Select Pattern

Read `pages/contact-page/references/contact-form.md` and select a layout and input style.

**Layout patterns**:

| Layout | Best When | Form Max-Width |
|--------|-----------|----------------|
| Centered single column | 3-5 fields, form is the sole focus of the section | 560px |
| Centered wide | 5-7 fields with dual-column field pairs (First/Last, Email/Phone) | 720px |
| Split (left info + right form) | Need to show brand info, value props, or contact details alongside form | 1080px container, 50/50 grid |
| Card container | Form needs visual separation from page background | 560px (incl. 32px padding) |

**Input styles**:

| Style | Best When | Border | Background | Radius |
|-------|-----------|--------|------------|--------|
| Full Border (A) | Default, any archetype, 4+ fields | 1px solid `--surface-2` | `--bg` | 4px |
| Underline (B) | Minimal aesthetic, 3-5 fields only | bottom only, 1px `--surface-2` | transparent | 0 |
| Filled (C) | Pure white/black background, 5+ fields | 1px transparent (focus: `--text`) | `--surface-1` | 4px |

**Label placement**:

| Style | Best When |
|-------|-----------|
| Above input (default) | 4+ fields, best accessibility |
| Mono uppercase above | Paired with underline inputs for editorial feel |
| Placeholder-only | Extreme minimalism, 3 fields max, self-evident fields |

### Step 3: Build

Read the active style file first (`shared/visual-style.md` for Minimal, the default). The tokens below are Minimal defaults — with another style active, take visual values from that style file per *Style precedence* in the master `SKILL.md`, and keep the layout and structure below:

**Input fields (Full Border default)**:
```
Padding:              8px 16px
Font:                 var(--font-body), 16px, weight 400
                      (body font for user-entered content — display font weight lock is 500,
                       which is too heavy for text the user types)
Border:               1px solid var(--surface-2)
Radius:               4px
Focus:                border-color -> var(--text); transition: border-color 0.3s linear
                      :focus { outline: none }
                      :focus-visible { outline: 2px solid var(--text); outline-offset: 2px }
                      (:focus-visible shows the ring on keyboard navigation only,
                       keeping the clean look for mouse/touch without losing accessibility)
Placeholder:          color var(--text), opacity 0.3
Transition:           border-color 0.3s linear
```

**Labels (above input)**:
```
Font:                 var(--font-display), 14px, weight 500
Color:                var(--text), opacity 0.5
Margin-bottom:        8px
```

**Labels (mono variant)**:
```
Font:                 var(--font-mono), 12px, weight 400
Tracking:             +0.72px, uppercase
Color:                var(--text), opacity 0.4
Margin-bottom:        8px
```

**Textarea**:
```
Min-height:           120px (4-5 lines)
Max-height:           240px
Resize:               vertical only
Line-height:          1.6
Same border/bg as inputs -- no special treatment
Always last text field before submit
```

**Field spacing**:
```
Field group gap:      24px (margin-bottom on each .form-group)
Dual-column gap:      16px (grid gap between paired fields)
Dual-column pairs:    First+Last, Email+Phone, Company+Size, Country+City
Never pair with:      Textarea, two dropdowns side by side
Narrow breakpoint:    480px -> dual columns stack to single
```

**Submit button**:
```
Width:                100% (default) or auto
Padding:              8px 16px
Font:                 var(--font-display), 14px, weight 500
Background:           var(--accent)
Color:                var(--accent-text)
Border:               none
Radius:               2px
Margin-top:           24px
Hover:                transform translateY(-1px)
Transition:           transform 0.2s ease-in-out
```

**Submit button (outline variant)**:
```
Background:           transparent
Color:                var(--text)
Border:               1px solid var(--surface-2)
Hover:                border-color -> var(--text)
```

**Privacy checkbox (optional)**:
```
Gap:                  12px (flex row)
Checkbox:             18px x 18px, accent-color var(--text)
Label:                var(--font-body), 14px, weight 400, opacity 0.5
Link:                 underline, opacity 0.5
Margin-top:           16px
```

**Container tokens by layout**:
```
Centered:             max-width 560px, margin 0 auto, padding 0 32px
Centered wide:        max-width 720px, margin 0 auto, padding 0 32px
Split:                grid 1fr 1fr, gap 58px, max-width 1080px, align-items start
Card:                 background var(--surface-1), padding 32px, radius 16px
```

**Structure** (top to bottom):
1. [If centered] Section heading -- `<h2>`, section title scale, center-aligned
2. Form fields -- in order of importance, dual-column pairs where applicable
3. [Optional] Subject/Reason dropdown or radio group
4. Textarea -- always last text input
5. [Optional] Privacy checkbox
6. Submit button

**Mobile (≤ 767px)**:
- Split layout collapses to single column (info stacks above form)
- Dual-column fields collapse to single column at 480px
- Submit button always full-width on mobile

**Rules**:
- All inputs in a form must use the same style (A, B, or C) -- never mix
- Textarea inherits the same border/background as text inputs
- No box-shadow on any form element
- Focus state = border-color change to `var(--text)`. Use `:focus { outline: none }` + `:focus-visible { outline: 2px solid var(--text); outline-offset: 2px }` — never suppress `:focus-visible`, as it is the only visible indicator for keyboard users
- Select dropdowns use custom arrow (CSS triangle, opacity 0.4)

#### Motion & Interaction

Reference: `shared/interaction-patterns.md`

- Scroll reveal on the section container: `translateY(32px)` / `0.8s` / `cubic-bezier(0.16, 1, 0.3, 1)` (§2)
- Input focus transition already defined above: `border-color 0.3s linear` (from `shared/visual-style.md`)
- Do not stagger individual form fields -- the form is a single unit, not a card grid
- All animations wrapped in `@media (prefers-reduced-motion: no-preference)`

### Step 4: Verify

Visual values in this checklist assume Minimal. With another style active, check against the active style file instead.

- [ ] All inputs use the same style (border, background, radius consistent)?
- [ ] Every `<input>` and `<textarea>` has an associated `<label>` (visible or `aria-label`)?
- [ ] Focus states work on all fields (border-color transitions to `--text`)?
- [ ] Field vertical spacing is 24px between groups?
- [ ] Textarea has min-height 120px and resize: vertical?
- [ ] Submit button uses `var(--accent)` / `var(--accent-text)`?
- [ ] Submit button radius is 2px?
- [ ] No box-shadow on any element?
- [ ] Dual-column pairs stack at 480px?
- [ ] Split layout stacks at 767px?
- [ ] Placeholder text uses opacity 0.3, not a separate gray color?
- [ ] Form max-width matches chosen layout (560/720/1080)?

### Step 5: Deliver

Provide the section code (HTML + CSS). Note which layout and input style were chosen and why. If embedded in a larger page, provide the section as a droppable block.

---

## Constraints

- No Mobbin or external API dependency
- V1: visual presentation only -- form does not submit, no validation logic, no success/error states
- All design knowledge is pre-distilled in the referenced files
- Follow `shared/visual-style.md` tokens exactly -- do not invent values
- CTA text defaults to "Send message" for general contact, "Request a demo" for sales/demo forms
