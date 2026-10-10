# Anti-Patterns — Pricing Page

> Sourced from Mobbin sample analysis + AI generation convergence observations.
> Each pattern in this file describes what NOT to do and why.

---

## Part 1: Visual Convergence Errors

These are the 10 visual patterns most likely to make a pricing page look "AI-generated":

### 1. Gradient Tier Cards

**Anti-pattern**: Each tier card has a subtle gradient background (e.g., from white to light blue to purple).

**Why it's wrong**: Real products (Notion, Linear, Figma, Vercel) almost exclusively use flat-color tier cards. Gradients add noise and weaken the information hierarchy.

**Correct approach**: All tier cards, including the recommended one, use `var(--bg)` (flat). The recommended tier is marked by the subtle ring border and plain label from tier-cards.md, not a gradient or a different background.

---

### 2. Per-Tier Accent Colors

**Anti-pattern**: Free = gray badge, Pro = blue badge, Business = purple badge, Enterprise = gold badge — each tier gets its own color.

**Why it's wrong**: Violates the Chromatic Silence principle. Multiple chromatic colors on one page create visual chaos; price comparison becomes visually harder, not easier.

**Correct approach**: The recommended tier gets a plain label (12px / mono / uppercase / `var(--text)` at opacity 0.4, no fill — see tier-cards.md Recommended Tier Badge Token). All other tiers have no label.

---

### 3. Oversized Price Display

**Anti-pattern**: Price numbers use extremely large fonts (80–120px or larger), occupying most of the card.

**Why it's wrong**: While emphasizing price is correct, oversized numbers crowd out the feature list and CTA, making it harder to compare tiers.

**Correct approach**: Price display uses `clamp(36px, 5vw, 48px)` — prominent but not dominating. See tier-cards.md for the complete Price Display Token.

---

### 4. Pill Buttons on Tier Cards

**Anti-pattern**: Tier card CTA buttons use `border-radius: 999px` (pill shape).

**Why it's wrong**: The design system uses `border-radius: 2px` for buttons. Pill buttons make the page look "consumer app" rather than professional SaaS, and create inconsistency with buttons elsewhere on the page.

**Correct approach**: Tier card CTA uses `.btn-dark` or `.btn-outline`, both using `border-radius: 2px`.

---

### 5. Box-Shadow on Tier Cards

**Anti-pattern**: Tier cards have `box-shadow: 0 4px 24px rgba(0,0,0,0.1)` or similar shadows to "elevate" them.

**Why it's wrong**: The design system explicitly prohibits decorative shadows. The zero box-shadow rule: hierarchy is established through background color steps, not shadows.

**Correct approach**: Tier card distinction uses `border: 1px solid var(--surface-2)` on every card + the recommended card's subtle ring border (see tier-cards.md), not shadows.

---

### 6. Decorative Feature Icons

**Anti-pattern**: Each feature list item uses a colorful icon (green checkmark, emoji, branded icon) preceding the text.

**Why it's wrong**: Violates the Chromatic Silence principle. The standard is a monochrome checkmark (✓ with `color: var(--text); opacity: 0.4`) or a plain bullet, not decorative icons.

**Correct approach**: Feature list items use plain text or the standard ✓ checkmark. No icons, emojis, or color.

---

### 7. Neon / High-Saturation Badges

**Anti-pattern**: "Recommended" badge uses bright green, orange, or purple backgrounds; high saturation, high contrast.

**Why it's wrong**: Violates the Chromatic Silence principle. A single colored element occupying less than 1% of the page area technically complies, but high-saturation badges signal "cheap" rather than "premium."

**Correct approach**: Recommended marker is a plain monochrome label — `color: var(--text); opacity: 0.4`, no background fill, no pill (see tier-cards.md).

---

### 8. Toggle Uses Accent Color as Fill

**Anti-pattern**: Monthly/Annual toggle switch uses `var(--accent)` or a bright color as the active state fill.

**Why it's wrong**: Breaks design system consistency. Billing toggles should be part of the neutral color system, not decorative elements.

**Correct approach**: Toggle active option uses `var(--text)` as background + `var(--text-inverse)` as label color; see billing-toggle.md for the complete Token.

---

### 9. Five or More Tier Cards in One Row

**Anti-pattern**: Display 5, 6, or 7 pricing tier cards in one row on the page.

**Why it's wrong**: Each card becomes too narrow (especially on 1280px screens), feature lists get compressed, and the CTA buttons are almost unclickable. Information density exceeds the readable threshold.

**Correct approach**: Maximum 4 tiers. If more are needed, use a tab or dropdown to switch between tier groups.

---

### 10. Comparison Table Without Categories

**Anti-pattern**: All features listed in a single unbroken list (20–30 rows) with no category headers.

**Why it's wrong**: An uncategorized table is impossible to scan. Users can't quickly find the security or support features they care about; they have to read row by row.

**Correct approach**: 10+ features must have category headers. See comparison-table.md for Category Header Token and Feature Category Suggestions.

---

## Part 2: Brand Color Adjustment Rules

The design system provides `--accent` as a brand color override variable. Pricing pages should follow the same constraints as other pages:

**Allowed uses of `--accent`** (exhaustive — from `shared/visual-style.md` §1):
- ✅ Primary CTA button background (`.btn-dark`, required)
- ✅ Nav CTA button background (optional, syncs with primary CTA)
- ✅ Pricing recommended tier border ring `rgba(accent, 0.2)` (optional)
- ✅ Link hover color (optional)

**Prohibited uses of `--accent`**:
- ❌ Toggle / Switch active state (always use `var(--text)`)
- ❌ Badge or label fills
- ❌ Icon backgrounds, section backgrounds
- ❌ Comparison table ✓ color
- ❌ Any large area fill (> 5% of page area)
- ❌ Gradients, glows, semi-transparent overlays

When brand color input is provided, the above constraint does not change — the constraint is for the design system, not for a specific color. Even if `--accent` is set to a neutral gray, its usage scope is still limited to the allowed list.

---

## Part 3: Content Errors

### 1. Fabricated Prices

**Anti-pattern**: Use typical SaaS prices ($9 / $29 / $99) as placeholders.

**Why it's wrong**: Users seeing the pricing page expect real pricing. Placeholder prices create misleading pricing expectations; if a developer uses this page as a template, they may forget to replace the numbers.

**Correct approach**: When the user has not provided pricing, use sample prices (master `SKILL.md` Design Rules → *Sample content*): round, plausible numbers for the category, each tier tagged `data-sample`, and the QA report says "Prices are sample — replace before publishing".

---

### 2. Fake Features

**Anti-pattern**: Fill in feature lists with typical SaaS feature text ("Unlimited projects", "Advanced analytics", "Priority support") without verifying whether these are actual product features.

**Why it's wrong**: The feature list is part of the product's promise. Fake features are misleading.

**Correct approach**: When the user has not provided feature lists, write sample features drawn from what the user said the product does (not generic SaaS filler), tagged `data-sample` and listed in the QA report, like prices.

---

### 3. Identical CTA Text Across All Tiers

**Anti-pattern**: Free / Pro / Business / Enterprise tier cards all use "Get Started" as the CTA.

**Why it's wrong**: Doesn't reflect the actual user conversion path. Enterprise users should "Contact Sales" rather than "Get Started."

**Correct approach**: CTA text differentiated by tier:
- Free: "Get Started Free" or "Start for Free"
- Pro / Business: "Get Started" or "Start Free Trial"
- Enterprise: "Contact Sales" or "Talk to Sales"

---

## Part 4: Structural Anti-Patterns

### 1. Missing Billing Toggle When Both Monthly and Annual Exist

**Anti-pattern**: Product offers both monthly and annual pricing, but the page only shows one pricing period.

**Why it's wrong**: Users who want the annual discount can't find it; they may assume there's no annual option.

**Correct approach**: When the product has both billing periods, the billing toggle is required. See billing-toggle.md.

---

### 2. Comparison Table Before Tier Cards

**Anti-pattern**: Comparison table appears first, tier cards appear after.

**Why it's wrong**: Violates the information architecture principle: overview first, then details. Users need to understand what the tiers are before they can understand how they compare.

**Correct approach**: Tier cards always come before the comparison table. See section-composition.md Hard Rules.

---

### 3. Multiple Sections Using Different Background Colors

**Anti-pattern**: Header = white, tier cards = light gray, comparison table = light blue, enterprise = dark, FAQ = light yellow — a different background color per section.

**Why it's wrong**: Violates the Chromatic Silence principle + pricing page background unity rule. A pricing page should have nearly unified background throughout.

**Correct approach**: At most 1 section uses `var(--surface-1)` (typically the enterprise breakout section). All other sections use `var(--bg)`.

---

## Part 5: Verification Checklist

Before delivering a pricing page, verify the following 10 points:

| # | Check Item | Pass Criteria |
|---|-----------|---------------|
| 1 | Tier cards: no gradient backgrounds | All cards use flat colors |
| 2 | Tier cards: no box-shadow | Only border + background-color for distinction |
| 3 | Recommended badge: monochrome | Plain label, `var(--text)` at opacity 0.4, no fill, no chromatic color |
| 4 | CTA button border-radius | `border-radius: 2px`, not pill shape |
| 5 | Price numbers: appropriate size | `clamp(36px, 5vw, 48px)`, not 80px+ |
| 6 | Feature icons: no decorative icons | Plain ✓ or text, no colorful icons |
| 7 | Billing toggle active state | Uses `var(--text)`, not accent color or chromatic color |
| 8 | Comparison table: has categories | 10+ features must be grouped under category headers |
| 9 | Pricing: sample prices tagged | Prices/features the user didn't give carry `data-sample` and are listed in the QA report |
| 10 | Background unity | At most 1 section uses `var(--surface-1)` |
