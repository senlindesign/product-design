# Pricing Page Archetypes & Selection Guide

> Source: Mobbin research synthesis across 65+ SaaS / tool product Pricing Pages

---

## Archetype Definitions

### A. Feature-Tiered

**Typical products**: Notion, Linear, Slack, GitHub, Figma, Asana, ClickUp
**Core characteristic**: 3–4 pricing tiers; features progressively unlocked by tier — Free → Pro → Business → Enterprise

**When to use**:
- Product's feature set can be stratified by user role / team size
- Users make purchase decisions based on "which features do I need"
- A Free or Starter tier exists that allows self-serve sign-up
- Feature lists differ meaningfully across tiers (not just usage limits)

**Typical section composition**:
1. Navigation
2. Header (title + subtitle + optional billing toggle)
3. Billing Toggle (monthly / annual switch — only when annual pricing is provided or requested)
4. Tier Cards (3–4 columns)
5. Comparison Table (feature comparison table)
6. Enterprise Section (optional — inline in cards or standalone section)
7. FAQ
8. Bottom CTA
9. Footer

**Visual tendencies**:
- Light theme dominant (#FFFFFF background)
- Comparison table is almost always present (helps users choose)
- Recommended tier identified by a plain label and subtle ring border (see tier-cards.md), not a colorful background
- High information density, but spacing remains generous

---

### B. Usage-Based

**Typical products**: Vercel, Supabase, OpenAI, Twilio, AWS, Cloudflare
**Core characteristic**: billing by API calls, storage, bandwidth, and other usage metrics; base plan + overage

**When to use**:
- Product value is directly tied to usage volume
- "Free quota + pay-as-you-go for overages" model is in use
- Users need to understand usage limits and unit pricing
- More than 1 billing dimension exists (API calls + storage + bandwidth)

**Typical section composition**:
1. Navigation
2. Header (title + subtitle)
3. Billing Toggle (if monthly / annual options exist)
4. Tier Cards (showing "included usage" + "additional cost per unit")
5. Usage Details / Limits Table
6. Calculator / Usage Slider (optional)
7. FAQ
8. Footer

**Visual tendencies**:
- Dark (#0A0A0A) or light — depends on product tone
- Tier cards are content-denser: each tier must show included quotas
- Comparison table focuses on usage limits rather than feature differences
- May include a calculator or slider to help estimate costs

---

### C. Simple Binary

**Typical products**: Superhuman, Raycast, Bear, Craft, iA Writer, Todoist
**Core characteristic**: Free + Paid (only two choices), or just one paid plan

**When to use**:
- Product's feature set is unified and not suitable for stratification
- Payment unlocks "all premium features" rather than progressively unlocking
- Pricing is simple and can be stated in one sentence
- Product targets individual users rather than enterprises

**Typical section composition**:
1. Navigation
2. Header (title + value information)
3. Tier Cards (2 columns, Free vs Pro)
4. Feature List (optional — single-column display of Pro features)
5. FAQ (brief, 3–4 questions)
6. Footer

**Visual tendencies**:
- Overall layout is simpler; fewer sections
- 2 cards side by side, usually one white and one dark (or one `var(--bg)` and one `var(--surface-1)`) for contrast
- No comparison table needed — feature differences written directly in the cards
- More space for value description and brand information
- More generous spacing; whitespace matters more than information density

---

### D. Enterprise-First

**Typical products**: Datadog, Snowflake, Palantir, Scale AI, Salesforce
**Core characteristic**: public pricing is minimized; "Contact Sales" is the primary CTA

**When to use**:
- Product primarily targets enterprise customers (100+ person teams)
- Pricing needs to be customized based on volume / contract
- Security / compliance is a key factor in purchase decisions
- May have a public free / starter tier, but core revenue comes from enterprise

**Typical section composition**:
1. Navigation
2. Header (title + subtitle)
3. Brief Tier Overview (1–2 public tiers + Enterprise "Contact Sales")
4. Enterprise Section (standalone large section; detailed enterprise features)
5. Social Proof / Trust (logo wall + compliance badges + case studies)
6. FAQ
7. Footer

**Visual tendencies**:
- Highest density of trust signals (logo wall, compliance certifications, customer case studies)
- Enterprise section is the page's center of gravity; more prominent than tier cards
- "Contact Sales" appears repeatedly (header, enterprise section, bottom CTA)
- Comparison table focuses on security / compliance / support / SLA
- Overall page tone is more authoritative; avoid a "light and casual" feel

---

## Selection Process

```
1. How many pricing tiers does the product have?
   ├─ 1–2 → C. Simple Binary
   └─ 3+
       ├─ Pricing mainly by usage (API / storage / bandwidth)? → B. Usage-Based
       └─ Pricing mainly by feature unlock?
           ├─ Top tier is "Contact Sales" AND enterprise customers are core? → D. Enterprise-First
           └─ Otherwise → A. Feature-Tiered

2. After choosing an archetype, verify:
   - Have comparison table content? → A/B includes it; C typically omits it
   - Have usage calculator? → B includes it; others omit
   - Have enterprise logo wall / compliance badges? → D highlights them; A optional
   - Only 2 cards? → Even if product is complex, use C's concise layout
```

---

## Shared Rules Across All Archetypes

Regardless of which archetype you choose:

1. **Price must be the visual focal point**: within a tier card, the price number is the largest element (36–48px), second only to the page headline in visual hierarchy
2. **Recommended tier must have visual identification**: plain label + subtle ring border (tier-cards.md; no `border-top` emphasis) — but not a colorful background. Use system label style (12px / mono / uppercase / 0.4 opacity)
3. **CTA button differentiation**: recommended tier uses primary (filled) CTA; others use outline. Do not give all tiers the same button
4. **Do not fabricate prices**: if the user hasn't provided pricing data, use sample prices (master `SKILL.md` Design Rules → *Sample content*), tagged `data-sample` and named in the QA report
5. **FAQ focuses on pricing concerns**: at minimum include three core questions — "free trial?", "billing method?", "upgrade / downgrade?"
6. **Mobile adaptation**: tier cards must stack vertically on narrow screens; comparison table uses horizontal scrolling or stacks by plan
