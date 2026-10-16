# FAQ Section — Design Knowledge

> Source: Mobbin research across 22 SaaS product Landing Page FAQ sections (2026-09-28)

---

## Pattern 1: Centered Single-Column Accordion (Most Common)

**When to use**:
- Number of questions ≤ 6
- Answers are medium length (1–3 paragraphs)
- General Landing Page FAQ

**Execution**:
- Centered container (max-width approximately 700–800px)
- Each question on one row; expand / collapse icon on the right
- Questions separated by a thin line or spacing
- First question expanded by default (lets users understand the interaction pattern)
- Expand / collapse icon: +/- or chevron V/^ are both common

**Variants**:
- **Numbered**: prefix questions with 01, 02, 03 (Lemon Squeezy) — adds structural feel
- **Dark theme**: dark background + pill-shaped accordion rows (Mixpanel) — suited for overall dark pages

**Evidence**: Bird, Loops, Sana, Mixpanel, OpenAI, Zendesk
**Evidence status**: Cross-sample inference

---

## Pattern 2: Two-Column Layout (Title + Accordion)

**When to use**:
- Desktop needs to utilize horizontal space
- The title area has additional explanatory text
- A left-fixed title + right-scrollable list effect is desired

**Execution**:
- Left column: section title (+ optional introductory text)
- Right column: accordion list
- Left column approximately 30–35% wide; right column takes the remaining space
- On narrow screens, switch to stacked layout (title above, accordion below)

**Evidence**: Harvest, Podia, Maxima Therapy, Cohere
**Evidence status**: Cross-sample inference

---

## Pattern 3: Two-Column Grid Accordion

**When to use**:
- Number of questions ≥ 6
- Answers are short (1–2 sentences)
- Need to show more questions without making the page too long

**Execution**:
- Two-column grid; each column contains an independent accordion
- Questions distributed evenly across the two columns
- Suited for "display-type" FAQs with short answers

**Evidence**: ToDesktop, 1Password, Square, Miro, Webflow
**Evidence status**: Cross-sample inference

---

## Key Design Decisions

### Question Count
- 3–4 questions: minimal FAQ; suited for simple products or pages with sufficient explanation already
- 5–7 questions: standard FAQ; covers core concerns
- 8+ questions: consider adding category headings, or split into a dedicated FAQ page

### Categorization Strategy
- ≤ 6 questions: no categorization, list directly
- 7+ questions: group by topic (pricing, features, security, support, etc.)
- Category heading format: small bold text, visually distinct from question text

### Headline Choice
| Headline | Suitable tone |
|----------|--------------|
| "Frequently Asked Questions" | Formal, professional |
| "FAQ" | Concise, tech-oriented |
| "Questions & Answers" | Neutral, friendly |
| Creative variant | Strong brand personality (e.g., "There are no stupid questions") |

### Fallback After FAQ
About 30% of products provide a "fallback" entry below the FAQ:
- "Still have questions? Contact us" link
- "Have more questions?" + contact support button
- This is good practice — it acknowledges the FAQ's limitations and provides an alternative path for users

### FAQ + CTA Handoff
An effective pattern observed: a CTA strip immediately after the FAQ section (Loops).
- Logical flow: resolve doubts → take action immediately
- CTA can include a one-line social proof ("Thousands of companies use [Product]")
