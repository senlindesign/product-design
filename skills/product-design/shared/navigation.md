# Navigation Section — Design Knowledge

> Source: 23 SaaS product Landing Page Navigation studies via Mobbin (2026-09-28)

---

## Pattern 1: Logo Left + Nav Left-Center + Dual CTA Right (Most Common)

**When to use**:
- Default choice for most SaaS products
- 4-6 pages need to be exposed in the navigation
- Need to provide both login and primary conversion entry points

**Implementation guidance**:
- Left: Brand logo (icon + text, or text only)
- Center-left: 4-6 nav items, some with dropdown menus
- Right: Login (text link or outline button) + primary CTA (filled button)
- Nav bar fixed at the top of the page (sticky)
- Background: frosted glass (semi-transparent with backdrop blur) — prevents content from bleeding through on scroll
  - Light: `background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);`
  - Dark: `background: rgba(10, 10, 10, 0.85); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);`

**Nav item count guidance**:
| Count | When | Examples |
|-------|------|----------|
| 3-4 | Simple product line, early-stage product | Bird, Wellfound, Frontify |
| 5-6 | Standard SaaS, feature-rich | Mixpanel, Claude, Maze, Mora |
| 7+ | Large platform — use with caution (information overload risk) | Resend, beehiiv |

**CTA combination strategy**:
| Combination | When | Examples |
|-------------|------|----------|
| Login + "Get Started" / "Sign up" | Self-serve signup product | Linear, Equals, Resend |
| Login + "Contact sales" / "Book demo" | Enterprise / high-ACV product | AngelList, Frontify, Garden |
| Login + "Contact sales" + "Try [Product]" | Serving both individual and enterprise users | Claude, Intercom |

**Evidence**: Mixpanel, Claude, Maze, Intercom, Equals, Mora, beehiiv, AngelList
**Evidence status**: Cross-sample inference

---

## Pattern 2: Logo Left + Nav Center + Actions Right

**When to use**:
- Strong brand tone, want the navigation itself to be visually elegant
- Simple product line (fewer than 4 nav items)
- Design/creative products

**Implementation guidance**:
- Logo fixed at the left edge
- Nav items center-aligned, creating visual symmetry
- All-caps + widened letter-spacing for design sensibility
- Nav items are typically direct links (no dropdowns), maintaining visual cleanliness
- Right edge: 1 CTA (outline or filled button)

**When not to use**:
- More than 5 nav items (center alignment becomes too spread out on wide screens)
- Need for complex dropdown menus (breaks the symmetry)

**Evidence**: Clay, Runway, Hex
**Evidence status**: Observed

---

## Pattern 3: Transparent Overlay Navigation

**When to use**:
- Hero area uses a dark background, full-bleed image, or video
- Want the nav to blend visually with the Hero
- Brand values an immersive first-screen experience

**Implementation guidance**:
- Nav bar background transparent or semi-transparent (frosted glass effect)
- Text uses white (ensure readability on dark background)
- Can switch to solid background on scroll (improves readability)
- CTA button uses outline style (white border) instead of filled
- Ensure the background image/gradient is dark enough for WCAG contrast standards

**When not to use**:
- Hero background has uneven brightness (some areas too light, making text unreadable)
- Need high-contrast navigation (e.g., for visually impaired users)

**Evidence**: Linear, Frontify, Runway, T1 Energy, Clay, AngelList, Resend (~35%)
**Evidence status**: Cross-sample inference

---

## Key Design Decisions

### Nav Item Naming
| Naming style | Description | When | Examples |
|-------------|-------------|------|----------|
| Feature-based | Product / Solutions / Resources / Pricing | Default choice, user habit | Mixpanel, Mora |
| Verb/intent | Reach / Grow / Manage / Automate | Organized by user goals | Bird |
| Question-style | What? / Why? / How? | Educating the market about a new category | mymind |
| All-caps spaced | RESEARCH / PRODUCT / STUDIOS | Design/creative brands | Clay, Runway, Maze |

### Dropdown Menu (Mega-menu)
When to use:
- Product is feature-rich, needs to expose category structure at the nav level
- Each category has 3+ sub-items

Mega-menu layout options:
- **Two-column**: left column feature list + right column scenarios/use cases (Mixpanel)
- **With icon descriptions**: each sub-item has icon + title + description (Intercom)
- **Vertical full-screen**: full-screen overlay site map (beehiiv) — only appropriate when features are extremely numerous

When not to use:
- 4 or fewer nav items, each pointing to a single page (Linear, Clay)
- Minimalist brand positioning

### Announcement Bar
- Appears in ~30% of samples
- Position: above the nav bar, full-width
- Content: new feature launches, industry reports, achievement data
- Visual: `var(--surface-1)` background (achromatic) + one line of text + link. Brand accent color is NOT used for section backgrounds — see `visual-style.md` §1 accent whitelist
- Dismissible (X button)
- Do not put newsletter signups or complex interactions in the announcement bar

### CTA Button Visual Hierarchy
Visual weight escalation for multiple right-side action items:
```
Login (plain text) < Contact sales (outline button) < Get Started (filled button)
```
- Primary CTA uses brand color or dark fill
- Secondary actions use outline or plain text
- Maximum 2-3 visible actions — more than 3 increases decision burden

### CSS Implementation Trap: `.nav-links a` Overriding Button Styles
If nav links use `.nav-links a { color: var(--text); opacity: 0.5 }` for dimming, and buttons (`.btn-dark`/`.btn-outline`) are also `<a>` elements, they get overridden. `.nav-links a` (class+element = specificity 0-1-1) has higher priority than `.btn-dark` or `.btn-outline` (class = 0-1-0), causing:
- opacity becomes 0.5 → button is semi-transparent
- color is overridden → text color matches background color, text becomes invisible

**Two solutions (choose one)**:

1. **Separate containers** (recommended): nav links go in `.nav-links`, buttons go in a separate `.nav-actions` — they don't affect each other
2. **Explicit override**: use `.nav-links .btn-dark` (specificity 0-2-0) to override opacity, color, and background:
   ```css
   .nav-links .btn-dark {
       opacity: 1;
       color: var(--accent-text);
       background: var(--accent);
   }
   .nav-links .btn-outline {
       opacity: 1;
       color: var(--text);
       border-color: var(--surface-2);
   }
   ```

Overriding opacity alone is not enough — you must also override color, otherwise the text is invisible.

### Nav Background vs. Page Background
- If Hero is light: nav uses white background, natural transition
- If Hero is dark: nav uses transparent background overlay, or matches the Hero color
- Avoid nav and Hero using different dark colors — creates visual disconnect

---

## CSS Tokens (required — quote these verbatim, do not author independently)

These values are the source of truth for all Page Skills and Section Skills that render a navigation bar.

```css
/* Height and document flow */
:root { --nav-h: 68px; }        /* 16px padding × 2 + 36px button height */
body { padding-top: var(--nav-h); }   /* only when nav is position: fixed */
[id] { scroll-margin-top: var(--nav-h); }  /* anchor links clear fixed nav */

/* Fixed positioning */
nav {
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;
    padding: 16px 0;            /* vertical only — horizontal goes on inner .container */
}

/* Frosted glass backdrop (Light theme) */
nav {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}

/* Frosted glass backdrop (Dark theme) */
[data-theme="dark"] nav,
.dark nav {
    background: rgba(10, 10, 10, 0.85);
}

/* Inner container — aligns nav content with section content edges */
nav > .container {
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
    display: flex;
    align-items: center;
}

/* Spacing between nav regions */
.nav-logo {
    font-family: var(--font-display);
    font-size: 16px;
    font-weight: 500;
    color: var(--text);
    text-decoration: none;
    flex-shrink: 0;
}

.nav-links {
    display: flex;
    align-items: center;
    gap: 32px;                  /* space between individual nav link items */
    margin-left: 48px;          /* logo → first nav link (wider than link gap) */
    flex: 1;
}

.nav-links a {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    opacity: 0.5;
    text-decoration: none;
    transition: opacity 0.3s linear;
}
.nav-links a:hover { opacity: 1; }

.nav-actions {
    display: flex;
    align-items: center;
    gap: 16px;                  /* space between Login link and CTA button */
    margin-left: auto;
}

/* Narrow screen */
@media (max-width: 767px) {
    .nav-links { display: none; }   /* collapse to hamburger — see mobile nav pattern */
}
```

**Note on 48px logo-to-links gap**: This value sits between spacing scale entries 32px and 58px. It was observed consistently in composition tests and is registered here as a nav-specific token. Do not use 48px for other components — use the nearest scale entry (32px or 58px) instead.
