# Pricing Header — Design Knowledge

> Source: Mobbin research synthesis across 65+ SaaS product Pricing Page header / hero areas

---

## Pattern 1: Simple Centered Header (Recommended Default)

**When to use**:
- Standard choice for most Pricing Pages
- Product has clear pricing plans that don't require extra explanation
- Suitable for Archetype A (Feature-Tiered) and C (Simple Binary)

**Execution**:

**Structure** (top to bottom): [optional: PRICING label] → Headline → Subheadline → [optional: Billing Toggle]

**Token**:
```css
.pricing-header {
    text-align: center;
    padding-top: clamp(80px, 10vw, 128px);   /* shorter than landing page hero */
    padding-bottom: 48px;                      /* to billing toggle or tier cards */
    max-width: 720px;
    margin: 0 auto;
}
```

**PRICING Label** (optional):
```css
.pricing-label {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    margin-bottom: 16px;
}
```

**Headline Token**:
```css
.pricing-headline {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);       /* section title level, not Hero level */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
}
```

**Subheadline Token**:
```css
.pricing-subheadline {
    font-family: var(--font-body);
    font-size: 18px;
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    margin-top: 16px;
    max-width: 540px;
    margin-left: auto;
    margin-right: auto;
}
```

**Evidence**: Notion, Linear, GitHub, Figma, Slack and 25+ other products
**Evidence status**: Cross-sample inference

---

## Headline Strategy

Choose a headline style based on the product and page purpose:

| Strategy | Sentence form | When to use | Example |
|----------|--------------|-------------|---------|
| **Question type** | "Which plan is right for you?" | User needs help choosing; multi-tier product | GitHub, Asana |
| **Action type** | "Choose your plan" / "Pick a plan" | Direct guidance to action; confident product | Linear, Slack |
| **Simple label** | "Pricing" | Minimal tone; no sales language needed | Vercel, Supabase |
| **Value type** | "Simple pricing for every team" | Emphasize simplicity / transparency; eliminate pricing anxiety | Notion, ClickUp |
| **Commitment type** | "Start free, scale as you grow" | Has free tier; emphasize low barrier to entry | Figma |

**Rules**:
- Headline should not be too long — 5–10 words is enough
- Do not repeat the product name (navigation already has it)
- Do not use "Affordable" / "Cheap" — implies low value

---

## Subheadline Strategy

The core purpose of the subheadline is to **eliminate hesitation**:

**Common reassurance patterns**:
- "Cancel anytime. No questions asked."
- "Start free. No credit card required."
- "Free for individuals. Pay only when your team grows."
- "All plans include a 14-day free trial."

**Rules**:
- 1–2 sentences only; do not write paragraphs
- Focus on reducing risk (free trial, cancel anytime, no credit card)
- If the headline already includes reassurance ("Start free, scale as you grow"), the subheadline can be omitted

---

## Pattern 2: Header with Tabs

**When to use**:
- Product has multiple billing dimensions: Plans vs API, Site vs Workspace, Individual vs Team
- The tier structure differs completely across dimensions

**Execution**:
```css
.pricing-tabs {
    display: flex;
    justify-content: center;
    gap: 0;
    border-bottom: 1px solid var(--surface-2);
    margin-top: 32px;
}

.pricing-tab {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    padding: 12px 24px;
    border: none;
    background: transparent;
    color: var(--text);
    opacity: 0.5;
    cursor: pointer;
    border-bottom: 2px solid transparent;
    margin-bottom: -1px;
    transition: opacity 0.3s linear;
}

.pricing-tab.active {
    opacity: 1;
    border-bottom-color: var(--text);
}
```

**Position**: after the headline + subheadline, before the billing toggle (or replacing the billing toggle).

**When not to use**:
- Only Monthly / Annual distinction — use a billing toggle rather than tabs
- More than 3 tabs — mobile would be crowded

**Evidence**: Vercel (Hobby / Pro / Enterprise), Notion (Plans / Add-ons)
**Evidence status**: Observed; small sample

---

## Pattern 3: Header with Currency Selector

**When to use**:
- Product offers pricing in multiple currencies across different regions
- Users can select USD / EUR / GBP, etc.

**Execution**:
```css
.currency-selector {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 400;
    color: var(--text);
    opacity: 0.5;
    background: transparent;
    border: 1px solid var(--surface-2);
    border-radius: 4px;
    padding: 6px 12px;
    cursor: pointer;
}
```

**Position**: top right of the header or in the auxiliary control area below the headline. Keep it unobtrusive; it should not be more prominent than the billing toggle.

**When not to use**:
- Product is priced in only one market — no currency selector needed
- V1 scope: real currency conversion logic is not implemented — visual display only

---

## Pattern 4: Header with Logo Wall

**When to use**:
- Product needs to front-load trust signals on the pricing page
- Common for Archetype D (Enterprise-First)

**Execution**:
- Logo wall placed after the subheadline, before the billing toggle
- Use the same logo wall style as the landing page (see Logo Wall token in `shared/visual-style.md`)
- Label: "Trusted by 10,000+ teams" or "Powering the best teams"
- Occupies less vertical space — single row of logos, no multi-row grid

**When not to use**:
- Most pricing pages don't need a logo wall (the landing page already established trust)
- Fewer than 4 genuine customer logos to display

---

## Vertical Spacing Reference

```
Bottom of Nav → top of Header:          80–128px (clamp)
PRICING label → Headline:               16px
Headline → Subheadline:                 16px
Subheadline → Product tabs:             32px
Subheadline → Billing toggle:           48px (= visual-style.md "Subheading to CTA")
Tabs/Toggle → Tier Cards:              24px (toggle and cards form one unit — see section-composition.md)
```

The header area is more compact overall than a landing page Hero — the main body of a pricing page is the tier cards; the header is a quick transition.
