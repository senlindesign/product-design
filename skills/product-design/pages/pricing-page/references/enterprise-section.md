# Enterprise Section — Design Knowledge

> Source: Mobbin research synthesis across 65+ SaaS product Pricing Page enterprise-related areas

---

## When to Include an Enterprise Section

| Condition | Recommendation |
|-----------|---------------|
| Product has enterprise customers AND 4+ pricing tiers | **Standalone section** (breakout pattern) |
| Product has an enterprise option, 3 tiers (including enterprise) | **Inline tier card** (enterprise as the last card) |
| Product has no enterprise positioning | **Do not include** |
| Product is entirely "Contact Sales" (Archetype D) | **Enterprise is the main body**; tier cards become supplementary |

---

## Pattern 1: Inline Tier Card (Enterprise as the Last Card)

**When to use**:
- Enterprise is part of the tier array (Free / Pro / Enterprise)
- Enterprise's feature list is not much longer than other tiers
- No need for large-scale display of trust signals

**Execution**:

```css
.tier-card.enterprise {
    /* shares base token with other tier cards */
    padding: 32px;
    background: var(--bg);
    border: 1px solid var(--surface-2);
    border-radius: 16px;
}

.enterprise-price-custom {
    font-family: var(--font-display);
    font-size: clamp(36px, 5vw, 48px);    /* same level as other tier prices */
    font-weight: 500;
    color: var(--text);
    letter-spacing: -0.02em;
    /* display "Custom" or "Let's chat" in place of a price */
}

.enterprise-cta {
    /* use .btn-outline, not .btn-dark */
    /* text: "Contact Sales" or "Talk to Sales" */
}
```

**Enterprise feature list characteristics**:
- Opens with "Everything in Business, plus:"
- Focuses on security / compliance / support: SSO, SAML, audit logs, dedicated AM, SLA, custom contracts
- No need to list base features — references the next-lower tier

**Evidence**: Notion, Linear, GitHub, Figma, Slack
**Evidence status**: Cross-sample inference

---

## Pattern 2: Breakout Section (Standalone Full-Width Section)

**When to use**:
- Enterprise needs independent space to showcase its differentiated value
- There are separate trust signals to display (compliance badges, enterprise logos)
- Page tier cards already have 3–4 tiers; adding Enterprise to the card array would be too crowded

**Execution**:

**Section Token**:
```css
.enterprise-section {
    background: var(--surface-1);          /* #F5F5F5 (Light) / #141414 (Dark) */
    padding: 128px 32px;
    /* at most 1 section in the entire pricing page uses surface-1 background */
}

.enterprise-section-inner {
    max-width: 1080px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 58px;
    align-items: center;
}
```

**Left column: text + feature list**:
```css
.enterprise-headline {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);    /* section title */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
}

.enterprise-description {
    font-family: var(--font-body);
    font-size: 16px;
    font-weight: 400;
    color: var(--text);
    opacity: 0.5;
    margin-top: 16px;
    line-height: 1.6;
}
```

**Right column: CTA card**:
```css
.enterprise-cta-card {
    padding: 32px;
    background: var(--bg);                 /* white card on surface-1 */
    border-radius: 16px;
    text-align: center;
}
```

**Variants**:
- **Headline choices**: "Bring [Product] to your organization" / "Enterprise-grade [Product]" / "Built for enterprise"
- **Feature display**: a 2×3 or 3×2 grid of feature highlights (icon + short description), or a simple checklist

**When not to use**:
- Enterprise has no differentiated features beyond other tiers
- Page overall aims for simplicity (Archetype C)

**Evidence**: Slack, Asana, ClickUp, Datadog
**Evidence status**: Cross-sample inference

---

## Enterprise Feature Checklist

### Common Feature Categories

**Security & Compliance**:
- Single Sign-On (SSO) — SAML, OIDC
- Audit logs / Activity tracking
- SOC 2 Type II compliance
- GDPR / HIPAA compliance
- Data residency / region selection
- Advanced encryption (at rest & in transit)

**Admin & Control**:
- Admin console / dashboard
- User provisioning (SCIM)
- Custom roles & permissions
- Domain verification
- IP allowlisting

**Support**:
- Dedicated account manager
- Priority support / SLA guarantees
- Onboarding & training
- Custom implementation

**Customization**:
- Custom contracts & invoicing
- Volume discounts
- Custom integrations
- API rate limit increase

**Rule**: don't list all features. Select 6–8 that best demonstrate enterprise differentiation.

---

## Enterprise Logo Wall

**When to use**: have 4+ recognizable enterprise customers to display.

```css
.enterprise-logos {
    display: flex;
    gap: 58px;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 32px;
}

.enterprise-logo {
    font-family: var(--font-display);
    font-size: 16px;
    font-weight: 500;
    color: var(--text);
    opacity: 0.15;                         /* standard logo wall opacity */
}
```

**Style**: consistent with the landing page logo wall — see Logo Wall token in `shared/visual-style.md`.

---

## Final CTA Pattern

**When to use**: page is long enough (4+ sections) and needs a final CTA before the footer.

```css
.final-cta {
    text-align: center;
    padding: 128px 32px;
    max-width: 720px;
    margin: 0 auto;
}

.final-cta-headline {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
    margin-bottom: 24px;
}

.final-cta-subtext {
    font-family: var(--font-body);
    font-size: 16px;
    font-weight: 400;
    color: var(--text);
    opacity: 0.5;
    margin-bottom: 32px;
}
```

**Headline choices**:
- "Get started with [Product]" — general purpose (action invitation; `shared/copy.md` bans question headlines in CTA bands)
- "Bring [Product] to your team" — enterprise-oriented
- "Start building today" — developer product

**CTA button**: use `.btn-dark` (primary), text "Get started" or "Contact sales" (sentence case, `shared/copy.md` §6).

**When not to use**:
- Page has only 3 sections (header + cards + footer) — an additional CTA is redundant
- Archetype C (Simple Binary) — the page is already short enough

---

## Mobile Adaptation

```css
@media (max-width: 767px) {
    .enterprise-section-inner {
        grid-template-columns: 1fr;
        gap: 32px;
    }
    
    .enterprise-logos {
        gap: 32px;
    }
}
```
