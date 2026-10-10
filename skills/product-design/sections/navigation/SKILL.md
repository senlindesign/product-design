# Navigation Section Skill

Generate a professional Navigation bar -- the persistent top-level wayfinding element. Works standalone or as part of a full page.

**Visual System**: `shared/visual-style.md` -- default design tokens for Light/Dark themes (Section 8: Nav + Button tokens). Business, Colorful, and Editorial use their own style files — see *Style precedence* in the master `SKILL.md`.
**Section Knowledge**: `shared/navigation.md` -- patterns, CTA strategies, and anti-patterns from 23 real product research.

---

## When to Use

- "Add a navigation bar to my page"
- "Create a site header with logo and links"
- "Build a nav for [product]"
- When a Page Skill needs a Navigation -- it references this knowledge internally

Do NOT use for:
- In-app navigation (sidebar, tab bar, breadcrumb)
- Dashboard top bars with user avatar / settings
- Mobile-only bottom navigation

---

## Workflow

### Step 1: Understand Inputs

**Required**:
- Product name (used as logo text if no logo image provided)
- Navigation items (page names / labels)

**Defaults if not provided**:
- Theme -> Light
- Pattern -> Logo Left + Nav Left-Center + Dual CTA Right (most common)
- Nav items -> Product, Pricing, Docs, Blog (4 items)
- CTA pair -> "Log in" (text link) + "Get Started" (filled button)
- Brand color -> none (`--accent` = `--text`)
- Display font → the active style's display font (Minimal: DM Sans)
- Sticky -> yes

### Step 2: Select Pattern

Read `shared/navigation.md` and select:

| Pattern | Best When |
|---------|-----------|
| Logo Left + Nav Left-Center + Dual CTA Right | Standard SaaS with 4-6 nav items; needs both login and primary conversion entry |
| Logo Left + Nav Center + Actions Right | Brand-forward product with fewer than 5 nav items; design/creative products seeking visual symmetry |
| Transparent Overlay | Hero uses a dark background, full-bleed image, or video; immersive first-screen experience desired |

**Nav item count guidance**:

| Count | When | Examples |
|-------|------|----------|
| 3-4 | Simple product line, early-stage | Bird, Wellfound, Frontify |
| 5-6 | Standard SaaS, feature-rich | Mixpanel, Claude, Maze, Mora |
| 7+ | Large platform -- use with caution (information overload) | Resend, beehiiv |

**CTA pairing**:

| Combination | When | Examples |
|-------------|------|----------|
| Login + "Get Started" / "Sign up" | Self-serve signup product | Linear, Equals, Resend |
| Login + "Contact sales" / "Book demo" | Enterprise / high-ACV product | AngelList, Frontify |
| Login + "Contact sales" + "Try [Product]" | Serving both individual and enterprise | Claude, Intercom |

### Step 3: Build

Read the active style file first (`shared/visual-style.md` for Minimal, the default). The tokens below are Minimal defaults — with another style active, take visual values from that style file per *Style precedence* in the master `SKILL.md`, and keep the layout and structure below:

```
Nav height:           68px (--nav-h) = 16px padding x 2 + 36px button
Nav padding:          16px 0 vertical only — put the 32px horizontal padding on the
                      inner .container, NOT on <nav>. If you pad <nav> directly the
                      logo lands 32px right of every section's content edge.
Nav background:       frosted glass — rgba(255,255,255,0.85) + backdrop-filter: blur(12px) (Light)
                      rgba(10,10,10,0.85) + backdrop-filter: blur(12px) (Dark)
                      This prevents page content from bleeding through the fixed nav on scroll.
                      See shared/visual-style.md §8 Navigation for the full CSS block.
Sticky:               position: fixed; top: 0; width: 100%; z-index: 1000
                      A fixed nav leaves the document flow — you MUST add
                      body { padding-top: var(--nav-h) }, or the Hero's 128px top
                      padding measures from the viewport top and the headline
                      sits under the nav.
Anchor offset:        When nav links target in-page anchors (e.g. href="#features"),
                      the target section needs `scroll-margin-top: var(--nav-h)` or
                      the heading scrolls behind the fixed nav. Add this to any
                      element with an `id` attribute.
Content max-width:    1080px, centered on the inner .container (match page grid)

Logo text:            18px / weight 500 / font-display / opacity 1
Logo icon height:     24-32px (if image provided)

Nav links:            14px / weight 500 / font-display
Nav link color:       var(--text) / opacity 0.5
Nav link hover:       opacity 1 / transition: opacity 0.3s linear

CTA button (primary): 14px / 8px 16px padding / 2px radius / var(--accent) bg / var(--accent-text) color
CTA button (secondary): 14px / 8px 16px padding / 2px radius / transparent bg / 1px solid var(--surface-2) border
Login link:           same as nav links (text only, no button chrome)

Nav link gap:         32px (flex gap between nav link items)
Logo-to-links gap:    48px (space between logo and first nav link)
Actions gap:          16px (flex gap between login link and CTA button)
```

**Structure** (left to right):
1. Logo -- product name as text (weight 500, full opacity) or image
2. Nav links -- 3-6 items, grouped in a container (`.nav-links`)
3. CTA group -- Login (text) + Primary CTA (`.btn-dark`), grouped in a separate container (`.nav-actions`)

**CSS Specificity Trap -- CRITICAL**:

If nav links use `.nav-links a { color: var(--text); opacity: 0.5; }` to dim them, and CTA buttons are also `<a>` elements inside `.nav-links`, the `.nav-links a` selector (specificity 0-1-1) beats `.btn-dark` (specificity 0-1-0). This causes two bugs:
- Button opacity drops to 0.5 (half-transparent button)
- Button text color overridden to `var(--text)`, making text invisible on a `var(--text)` background

**Solution -- use separate containers** (recommended):
```html
<nav>
  <div class="container"><!-- Required: provides 1080px max-width + 0 32px side padding -->
    <a class="nav-logo" href="/">ProductName</a>
    <div class="nav-links">
      <!-- Only plain text links here -->
      <a href="/product">Product</a>
      <a href="/pricing">Pricing</a>
    </div>
    <div class="nav-actions">
      <!-- Buttons here -- outside .nav-links scope -->
      <a href="/login" class="nav-login">Log in</a>
      <a href="/signup" class="btn-dark">Get Started</a>
    </div>
  </div>
</nav>
```

The `.container` wrapper is required — without it, nav content has no side padding and no max-width cap, so the logo and links touch the viewport edge on wide screens.

The `.nav-links a` rule never reaches the buttons because they live in `.nav-actions`. If buttons must live inside `.nav-links`, override explicitly with `.nav-links .btn-dark { opacity: 1; color: var(--accent-text); background: var(--accent); }`.

**Transparent Overlay variant** (dark Hero with overlay nav):
- `background: transparent; backdrop-filter: none` (fully transparent — used only at page load when nav is at the top of a dark hero)
- Switch to frosted glass on scroll: use `window.addEventListener('scroll', ...)` to toggle a `.scrolled` class
- All text and links: `color: var(--text-inverse); opacity: 0.5` (links) / `opacity: 1` (logo, CTA)
- CTA uses `.btn-outline` with white border instead of `.btn-dark`
- Ensure Hero background is dark enough for WCAG contrast

**Mobile (below 768px)**:
- Hide `.nav-links` and `.nav-actions` (except hamburger); show a hamburger button
- Logo stays visible at left; hamburger at right
- Hamburger: 24px wide, three lines of `2px` height, spaced `6px` apart, `color: var(--text)`
- Tapping hamburger reveals a full-width dropdown panel:
  ```
  Panel background:     var(--bg)
  Panel padding:        24px 20px (matches narrow-screen side padding)
  Panel border-top:     1px solid var(--surface-2)
  Panel items:          stacked vertically, 20px gap
  Panel link style:     same as desktop nav links (14px / weight 500 / opacity 0.5)
  Panel CTA:            full-width `.btn-dark`, margin-top 8px
  ```
- Use `initMobileNav()` from `shared/interaction-patterns.md §11` — includes outside-click close, Escape key, and focus-return to toggle. Note `top: var(--nav-h)` is mandatory so the dropdown opens below the fixed nav bar.

**Rules**:
- No box-shadow on nav -- ever
- No border-bottom by default
- No background gradient
- Logo opacity is always 1 (never dimmed like nav links)
- Nav links and CTA must be vertically centered with the logo

#### Motion & Interaction

Navigation does not use entrance animations (see `shared/interaction-patterns.md` §15 Anti-Patterns).

### Step 4: Verify

Visual values in this checklist assume Minimal. With another style active, check against the active style file instead.

- [ ] Nav has `padding: 16px 0` with the 32px horizontal padding on the inner `.container`?
- [ ] If nav is `position: fixed`, does `body` carry `padding-top: var(--nav-h)`?
- [ ] Nav links are 14px / weight 500 / opacity 0.5 with hover -> opacity 1?
- [ ] CTA buttons use `var(--accent)` / `var(--accent-text)`, not hardcoded colors?
- [ ] CTA buttons are NOT inside `.nav-links` container (or have explicit specificity override)?
- [ ] Logo is full opacity 1 (not dimmed like links)?
- [ ] Zero box-shadow on nav?
- [ ] Zero border-bottom on nav?
- [ ] Sticky positioning with appropriate z-index?
- [ ] Works at 767px width (hamburger menu, links hidden)?
- [ ] Content max-width matches page grid (1080px)?
- [ ] Transparent variant: text readable against dark Hero background (if applicable)?
- [ ] Elements with `id` attributes have `scroll-margin-top: var(--nav-h)` to offset the fixed nav?

### Step 5: Deliver

Provide the section code (HTML + CSS + mobile JS toggle). Note which pattern was chosen and why.

---

## Constraints

- No Mobbin or external API dependency
- V1: visual presentation only -- nav links are styled anchors, no real routing
- V1: mobile menu is show/hide toggle only, no slide animations
- No mega-menu / dropdown sub-navigation in V1
- All design knowledge is pre-distilled in the referenced files
- Follow `shared/visual-style.md` tokens exactly -- do not invent values
