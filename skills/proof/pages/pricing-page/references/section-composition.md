# Section Composition Rules — Pricing Page

> Source: Section arrangement pattern synthesis from 65+ SaaS product Pricing Pages

---

## 1. Recommended Section Order by Archetype

### A. Feature-Tiered

```
Navigation
    ↓
Header (title + subtitle)
    ↓
Billing Toggle (monthly/annual switch)
    ↓
Tier Cards (3–4 columns)
    ↓
Comparison Table (feature comparison)
    ↓
Enterprise Section (optional — inline or standalone)
    ↓
FAQ
    ↓
Bottom CTA (only when page length > 4 sections)
    ↓
Footer
```

### B. Usage-Based

```
Navigation
    ↓
Header (title + subtitle)
    ↓
Billing Toggle (if monthly/annual options exist)
    ↓
Tier Cards (showing included usage + overage pricing)
    ↓
Usage Details / Limits Table
    ↓
FAQ
    ↓
Footer
```

### C. Simple Binary

```
Navigation
    ↓
Header (title + value description)
    ↓
Tier Cards (2 columns, Free vs Pro)
    ↓
FAQ (brief, 3–4 questions)
    ↓
Footer
```

### D. Enterprise-First

```
Navigation
    ↓
Header (title + subtitle)
    ↓
Brief Tier Overview (1–2 public tiers + Enterprise "Contact Sales")
    ↓
Enterprise Section (standalone large section)
    ↓
Social Proof / Trust (logo wall + compliance badges)
    ↓
FAQ
    ↓
Footer
```

---

## 2. Hard Rules Between Sections

These rules must not be violated:

| Rule | Explanation |
|------|-------------|
| **Toggle immediately adjacent to Cards** | Spacing between billing toggle and tier cards is only 24px; no other section is inserted between them |
| **Comparison Table must come after Tier Cards** | Users first see the overview (cards), then the details (table). Reversed, the information flow breaks |
| **FAQ comes after Comparison Table** | FAQ answers questions that arise during the comparison process |
| **Enterprise section does not come after FAQ** | Enterprise is section-level content and should not be split by FAQ |
| **Nav at the top, Footer at the bottom** | Fixed positions; reuse landing page nav / footer patterns |

---

## 3. Soft Rules Between Sections

Can be adjusted based on content, but follow by default:

| Rule | Explanation | Exception |
|------|-------------|-----------|
| **Final CTA only on long pages** | Add a bottom CTA only when the page has 4+ sections | Archetype C typically doesn't need one |
| **Social Proof near Enterprise** | Trust signals support the enterprise value proposition | Can be omitted if there is no enterprise section |
| **Logo wall after Header** | If needed, place between header and cards | Most pricing pages don't need a logo wall |

---

## 4. Spacing Rules

```
Section spacing (vertical space between sections):  180px
Header top padding:                                 80–128px (clamp)
Header to Billing Toggle:                           48px
Billing Toggle to Tier Cards:                       24px (keep tightly associated)
Tier Cards to Comparison Table:                     180px
Section title to content:                           58px
Footer top padding:                                 128px
```

**Key distinction**: the spacing between Billing Toggle and Tier Cards is much smaller than the standard between-section spacing (24px vs 180px), because they form a single interactive unit.

---

## 5. Background Color Rules

```
Navigation:          var(--bg)              transparent / white
Header:              var(--bg)              consistent with nav
Billing Toggle:      var(--bg)              consistent with header
Tier Cards:          var(--bg)              main area
Comparison Table:    var(--bg)              consistent
Enterprise Section:  var(--surface-1)       only when using standalone section (breakout pattern); at most 1
FAQ:                 var(--bg)
Bottom CTA:          var(--bg)
Footer:              var(--bg) or var(--surface-1)
```

**Core principles**:
- Pricing page background is **nearly unified** throughout (var(--bg))
- **At most 1 section** may use var(--surface-1) background — typically the enterprise breakout section
- **Do not alternate background colors** to distinguish sections — spacing and headings already create sufficient section-feel
- Do not use colorful backgrounds, gradients, or dark/light alternation

---

## 6. Decision Guide for Adding / Removing Sections

### When to Add

| Section | Condition for adding |
|---------|---------------------|
| Billing Toggle | User provided both monthly and annual prices, or asked for a toggle (never invent annual prices) |
| How It Works / Switching | Brief names switching or setup effort as the main barrier — place after Tier Cards (or Comparison Table), before Enterprise / FAQ; `var(--bg)` background; layout from `sections/how-it-works/SKILL.md`; steps must be the product's real onboarding/migration steps or labeled placeholders |
| Comparison Table | 4+ features differ across tiers; users need detailed comparison |
| Enterprise Section | Product has enterprise customers + 4+ enterprise-differentiating features |
| Social Proof | Have genuine enterprise customer logos or case studies (Archetype D only) |
| Bottom CTA | Page length exceeds 4 content sections |
| Usage Details | Archetype B; need to explain usage billing details |

### When to Remove

| Section | Condition for removing |
|---------|----------------------|
| Billing Toggle | Only one billing period exists |
| Comparison Table | Fewer than 4 feature differences, or Archetype C |
| Enterprise Section | Product does not target enterprise customers |
| Bottom CTA | Page has only 3 sections (header + cards + footer) |
| FAQ | Fewer than 3 meaningful pricing-related questions |

---

## 7. Minimum Page vs. Full Page

### Minimum Viable Pricing Page (Archetype C)

```
Navigation → Header → Tier Cards (2) → FAQ (3–4 questions) → Footer
```
Approximately 3 content sections; concise and efficient.

### Standard Pricing Page (Archetype A/B)

```
Navigation → Header → Toggle → Tier Cards → Comparison Table → FAQ → Footer
```
Approximately 5 content sections; covers most needs.

### Full Pricing Page (Archetype A + Enterprise / Archetype D)

```
Navigation → Header → Toggle → Tier Cards → Comparison Table → Enterprise → FAQ → Bottom CTA → Footer
```
Approximately 7 content sections. **Do not exceed 8** — a pricing page should help users decide, not overwhelm them with information.

---

## 8. Shared Components with Landing Page

The following components reuse landing page styles and are not redefined on the pricing page:

| Component | Source | Notes |
|-----------|--------|-------|
| Navigation | `shared/navigation.md` | Consistent style; active state marks "Pricing" |
| Footer | `shared/footer.md` | Fully reused |
| Logo Wall | `shared/visual-style.md` Logo Wall token | If pricing page needs one |
| FAQ layout | `sections/faq/SKILL.md` | Layout tokens (Step 3); patterns from `pages/landing-page/references/faq.md` |
| How It Works | `sections/how-it-works/SKILL.md` | Optional; only for a switching / setup-effort barrier (see §6) |
