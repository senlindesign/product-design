# Tier Cards — Design Knowledge

> Source: Mobbin research synthesis across 65+ SaaS product Pricing Page tier card sections

---

## Pattern 1: 3-Column Tier Cards (Recommended Default)

**When to use**:
- Product has 3 pricing tiers (Free / Pro / Business or Starter / Pro / Enterprise)
- Most common SaaS pricing pattern; best visual balance
- Middle tier is the recommended choice

**Execution**:

**Container Token**:
```css
.tier-cards-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    max-width: 1080px;       /* consistent with main grid */
    margin: 0 auto;
    padding: 0 32px;
}
```

**Single Card Token**:
```css
.tier-card {
    padding: 32px;
    background: var(--bg);              /* #FFFFFF (Light) / #0A0A0A (Dark) */
    border: 1px solid var(--surface-2); /* #E9E9E9 (Light) / #1F1F1F (Dark) */
    border-radius: 16px;               /* content-card level */
    /* zero shadow */
}
```

**Card internal vertical order** (top to bottom):
1. **Badge** (optional) — recommended tier shows "Recommended" (use "Most Popular" only when the user states it is true)
2. **Plan Name** — 20px / weight 500 / DM Sans / tracking -0.4px
3. **Description** — 14px / weight 400 / opacity 0.5 / 1–2 sentence positioning description
4. **Price** — see Price Display Token below
5. **CTA Button** — see CTA Button Differentiation below
6. **Separator** — 1px solid var(--surface-2), margin 24px 0
7. **Feature List** — see Feature List Token below

**Variants**:
- **4 columns**: when there are 4 tiers (including Enterprise), reduce gap to 20px and card padding to 24px to prevent excessive narrowness
- **2 columns**: Archetype C (Simple Binary); cards are wider (max-width 480px each), centered

**When not to use**:
- 5+ tiers in one row — split Enterprise into a standalone section
- Card content volume differs too greatly (one with 3 features, another with 20) — consider a comparison table instead

**Evidence**: Notion, Linear, Slack, GitHub, Figma, Asana and 20+ other products
**Evidence status**: Cross-sample inference

---

## Price Display Token

**Execution**:
```css
.price-amount {
    font-family: var(--font-display);   /* DM Sans */
    font-size: clamp(36px, 5vw, 48px);
    font-weight: 500;
    color: var(--text);                 /* #141414 (Light) / #EDEDED (Dark) */
    letter-spacing: -0.02em;
    line-height: 1.1;
}

.price-currency {
    font-family: var(--font-display);
    font-size: clamp(24px, 3vw, 32px); /* slightly smaller than the number */
    font-weight: 500;
    vertical-align: top;               /* or baseline, aligned to top of number */
}

.price-period {
    font-family: var(--font-body);     /* body font at 400 — display font weight lock is 500 */
    font-size: 14px;
    font-weight: 400;
    color: var(--text);
    opacity: 0.5;
    margin-left: 2px;                  /* follows price closely */
}

.price-billing-note {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    color: var(--text);
    opacity: 0.4;
    margin-top: 4px;
    /* e.g., "billed annually" */
}
```

**Price variants**:
- **Free tier**: display "$0" (don't omit the number); period shows "/forever" or "/month"
- **Enterprise tier**: replace the price area with "Custom" or "Let's chat" at the same font size (clamp 36–48px), weight 500
- **Annual discount**: show the monthly equivalent price + "/mo"; note "billed annually" below

---

## Annual Discount Badge Token

```css
.discount-badge {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.5;
    background: var(--surface-1);       /* #F5F5F5 (Light) / #141414 (Dark) */
    padding: 4px 8px;
    border-radius: 4px;
    /* position: adjacent to annual price, or next to billing toggle */
}
```

Content is typically "-20%" or "SAVE 20%". Do not use a colorful background or brand color.

---

## Recommended Tier Badge Token

```css
.recommended-badge {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    /* position: top of card, above Plan Name */
    margin-bottom: 12px;
}
```

**Variants**:
- **Badge text**: plain text "RECOMMENDED" by default, using system label style. "MOST POPULAR" is a factual claim — use it only when the user states it is true
- **Subtle full-border ring** (recommended): hardcode the RGBA values — CSS custom properties cannot be used inside `rgba()` without the RGB-channel trick. Use:
  ```css
  /* Light theme recommended card */
  .tier-card.recommended { border: 1.5px solid rgba(20, 20, 20, 0.15); }
  /* Dark theme recommended card */
  .tier-card.recommended { border: 1.5px solid rgba(237, 237, 237, 0.15); }
  ```
  More natural than `border-top` only; doesn't create a harsh single-edge emphasis line
- **Do not use**: `border-top: 2px solid var(--text)` (too harsh; AI convergence trait), colorful badge, gradient background, glow effect, pill-shaped emphasis badge

---

## Feature List Token

```css
.feature-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.feature-list li {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 8px 0;
    font-family: var(--font-body);
    font-size: 14px;
    font-weight: 400;
    color: var(--text);
    line-height: 1.5;
}

.feature-list .check {
    color: var(--text);
    opacity: 0.4;
    font-size: 14px;
    flex-shrink: 0;
    /* use ✓ character or simple SVG checkmark */
}

.feature-list .feature-intro {
    font-weight: 500;
    font-size: 14px;
    color: var(--text);
    opacity: 0.5;
    padding: 8px 0 4px 0;
    /* e.g., "Everything in Pro, plus:" */
}
```

**Rules**:
- Checkmarks unified to opacity 0.4 text color; do not use green or brand color
- "Everything in [Plan], plus:" as the opening line for higher-tier feature lists, weight 500
- Recommended feature counts: Free 3–5 items, Pro 5–8 items, Business/Enterprise 6–10 items
- When more than 8 features exist, consider showing only key features + a "See all features" link to the comparison table

---

## CTA Button Differentiation

| Tier | Button style | Text example |
|------|-------------|--------------|
| Free | `.btn-outline` | "Get Started" / "Start Free" |
| Recommended (Pro) | `.btn-dark` (primary, filled) | "Start Trial" / "Get Started" |
| Business | `.btn-outline` | "Start Trial" / "Upgrade" |
| Enterprise | `.btn-outline` | "Contact Sales" / "Talk to Sales" |

**Rules**:
- Only the recommended tier uses a filled (`.btn-dark`) button; all others use outline
- Unified button size: `padding: 8px 16px; font-size: 14px; border-radius: 2px`
- Do not give each tier a different colored button
- Button width: `width: 100%` to fill the card width

---

## Mobile Adaptation

```css
@media (max-width: 767px) {
    .tier-cards-container {
        grid-template-columns: 1fr;
        gap: 16px;
        max-width: 480px;
    }
}

@media (min-width: 769px) and (max-width: 1024px) {
    .tier-cards-container {
        grid-template-columns: repeat(2, 1fr);
        /* 3rd/4th card wraps to next row */
    }
}
```

The recommended tier can be placed first on mobile (visual priority), adjusted via CSS order.
