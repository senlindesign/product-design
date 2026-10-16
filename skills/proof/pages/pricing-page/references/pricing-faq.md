# Pricing FAQ — Design Knowledge

> Source: Mobbin research synthesis across 65+ SaaS product Pricing Page FAQ sections

---

## Difference from Landing Page FAQ

Pricing FAQ reuses the same layout patterns as the Landing Page FAQ (centered single-column accordion / two-column layout / two-column grid) in terms of structure and layout. Layout tokens live in `sections/faq/SKILL.md` (Step 3: Build); pattern selection in `pages/landing-page/references/faq.md`.

This file focuses on the **content strategy and question selection rules** specific to pricing FAQs.

---

## Default Question Set

When the user has not provided FAQ content, select 5–7 questions from the following as defaults:

### Core Questions (recommend including at least the first 4)

1. **"Which plan is right for me?"**
   - Answer structure: recommend by user role / scenario → "Individual? Start with Free. Team of 5–20? Pro is ideal. Larger org? Business or Enterprise."

2. **"Can I try [Product] for free?"**
   - Key points: whether there is a free tier, trial length, credit card required
   - Example: "Yes — our Free plan is free forever. Pro and Business plans include a 14-day free trial, no credit card required."

3. **"How does billing work?"**
   - Key points: monthly / annual billing, billing cycle, payment methods
   - Example: "We offer monthly billing[, and annual billing at [X]% off — only if the user provides annual pricing]. We accept [payment methods]."

4. **"Can I change or cancel my plan?"**
   - Key points: upgrade / downgrade process, cancellation policy, data retention
   - Example: "You can upgrade, downgrade, or cancel anytime from your account settings. When you cancel, you keep access until the end of your billing period."

### Supplementary Questions (select based on product characteristics)

5. **"Do you offer discounts for nonprofits/education/startups?"**
   - When to include: product has special pricing programs

6. **"What happens if I exceed my plan limits?"**
   - When to include: Archetype B (Usage-Based) — products with usage limits
   - Key points: whether auto-upgrade occurs, whether overage fees apply, whether service is restricted

7. **"Is my data secure?"**
   - When to include: Archetype D (Enterprise-First), or product handles sensitive data
   - Key points: encryption, compliance certifications (SOC 2, GDPR), data storage location

8. **"Can I get a refund?"**
   - When to include: paid product without a free trial

9. **"Do you offer enterprise pricing?"**
   - When to include: there is an enterprise tier but the page shows "Contact Sales"

10. **"What payment methods do you accept?"**
    - When to include: serving global customers; need to explain payment coverage

---

## Layout Choice

| Question count | Recommended layout | Reason |
|----------------|--------------------|--------|
| 3–4 | Centered single-column accordion | Simple; doesn't take up too much page space |
| 5–7 | Two-column layout (title left + accordion right) | Uses horizontal space; title area can add "Still have questions?" link |
| 8+ | Two-column grid accordion | Reduces vertical footprint; note that answers shouldn't be too long |

**Layout tokens are the same as the Landing Page FAQ** — reuse the token block in `sections/faq/SKILL.md` (Step 3: Build); do not redefine here.

---

## Section Token

```css
.pricing-faq {
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
}

.pricing-faq-title {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);    /* section title level */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
}
```

---

## Headline Choice

| Headline | Suitable tone |
|----------|--------------|
| "Frequently asked questions" | Standard, professional (recommended default) |
| "Pricing FAQs" | Direct; clearly about pricing |
| "Questions about pricing" | Neutral, clear |
| "Have questions?" | Conversational, friendly |

**Do not use**:
- Creative / playful headlines ("Money talks" / "Let's talk dollars") — pricing is a serious decision
- "FAQ" as three standalone letters — not friendly enough for non-technical users

---

## Position and Handoff

**Position**:
- After the Comparison Table (if present)
- After the Enterprise Section (if there is a standalone enterprise section)
- Always before the final CTA and Footer

**Spacing**:
- Section above to FAQ title: 180px (standard section spacing)
- FAQ title to first question: 58px (standard title-to-content distance)
- Last FAQ question to section below: 180px

**Fallback after FAQ**:
- "Still have questions? Contact our team" link placed below the FAQ
- Use a text link with 16px / weight 500 / opacity 0.5, 58px below the last item (matches `sections/faq/SKILL.md` Bottom CTA); underline on hover
- Links to the contact page or support email

---

## Content Writing Rules

1. **Questions in natural language** — don't use technical jargon. "How does billing work?" is better than "What is the billing cycle?"
2. **Concise answers**: 2–4 sentences per answer. Don't write paragraph-style explanations
3. **Lead with the conclusion**: "Yes, you can cancel anytime." — then add details
4. **Avoid legal language**: pricing FAQ is not the Terms of Service
5. **Don't fabricate policies**: if the user has not provided specific pricing policies, use generic placeholder content and note it in the delivery notes
