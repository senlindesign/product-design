# Social Proof Section — Design Knowledge

> Source: Mobbin research across 27 SaaS product Landing Page Social Proof sections (2026-09-28)

---

## Pattern 1: Logo Wall (Most Common)

**When to use**:
- Have 5+ recognizable customer / partner logos
- Need to establish trust quickly after the Hero
- The logos themselves have sufficient brand recognition

**Execution**:
- Centered headline + single-row or two-row logo arrangement
- Logo count: 5–8 (single row), 10–12 (double row)
- All logos unified to a single color (gray or white) to avoid visual competition
- Logos are uniform in size, equally spaced horizontally
- Common headlines: "Trusted by...", "Powering...", "Loved by..."

**Headline wording**:
| Headline | Tone |
|----------|------|
| "Trusted by teams at" | Neutral, professional (Grammarly, Granola) |
| "Trusted by the world's leading enterprises" | Enterprise-grade, authoritative (Cursor) |
| "Powering the world's best product teams" | Capability-oriented (Linear) |
| "Loved by [role] at" | Warm, community feel (Cycle: "Loved by product folks at") |
| "Trusted by engineers at" | Targeting a specific role (Cursor) |
| "[number]+ companies trust..." | Quantified trust (Customer.io: "7,500+") |

**Variants**:
- **Dark background logo wall**: dark / black background + white logos (Linear, Structured) — maintains visual continuity after a dark Hero
- **Logo wall embedded in Hero**: logo wall as part of the Hero bottom rather than a standalone section (Notion, Cursor) — most compact placement
- **Large logo grid**: 24+ logos arranged in 3 rows (Cursor enterprise page) — suited for showcasing large enterprise customers
- **Scrolling logo strip**: logos auto-scroll horizontally (Givingli) — suited when there are many logos but space is limited

**When not to use**:
- Logos have low brand recognition (small company / startup logos don't produce trust)
- Fewer than 4 logos — too few looks awkward

**Evidence**: Grammarly, Notion, Linear, Cursor, Granola, Hashnode, Cycle, Adaline, Tines, Structured
**Evidence status**: Cross-sample inference

---

## Pattern 2: Testimonial Card Grid

**When to use**:
- Have 3+ genuine customer quotes
- Quotes come from recognizable companies / titles
- Need to show specific usage experience

**Execution**:
- 3 equal-width columns (most common); each card contains:
  1. Customer company logo
  2. Quote text (1–3 sentences)
  3. Name + title + company name
  4. Optional: person's photo
- Cards have a light background or border to distinguish from the page background
- Key phrases in quotes can be **bolded** for emphasis
- Quote text uses quotation marks or citation marks (" " or 99 icons)

**Variants**:
- **With photo**: circular photo + name + title (Whereby, Cursor) — adds personalized trust
- **With link**: each card bottom has "View success story" / "Visit site ->" (Wellfound, Grain) — encourages deeper exploration
- **With quantified data**: quote includes specific numbers (Cursor: "over 45% of our code changes are now fully written by AI") — most persuasive
- **Long quote**: each card contains 2–3 paragraphs (Customer.io, Autosend) — suited for in-depth endorsements of complex B2B products

**When not to use**:
- Quote sources are not verifiable — do not fabricate them
- Quotes are too generic ("Great product!") — quotes without specific context or data lack persuasive power

**Evidence**: Cursor, Whereby, Wellfound, Hex, Autosend, Grain, Tines
**Evidence status**: Cross-sample inference

---

## Pattern 3: Logo Wall + Testimonials Combined

**When to use**:
- Have both logo assets and customer quotes
- Need to show quantity (breadth) and depth in the same area

**Execution**:
- Above: headline + logo wall (shows quantity / breadth)
- Below: 2–3 selected testimonial cards (shows depth)
- Or reverse: testimonials first, then logo wall as supplement
- Visually maintain a single-area feel (shared background color)

**Variants**:
- **Tab filtering**: switch between different testimonials + logos by industry / category tabs (Mixpanel) — suited for customers spanning multiple industries
- **Number + logo + testimonial**: headline includes customer count + logo wall + selected quotes (Mixpanel: "Delighting 8,000+ paying customers")

**Evidence**: Grain, Tines, Mixpanel, Customer.io, Jitter
**Evidence status**: Cross-sample inference

---

## Pattern 4: Large Enterprise Testimonial List

**When to use**:
- Customers are high-profile enterprises (Nike, Google level)
- Brand tone is premium and formal
- Each quote is substantial enough to stand alone

**Execution**:
- Vertical list; each quote occupies one row
- Large customer logo on the left, quote text on the right
- Longer quotes (2–3 sentences) with name and title
- Dark background adds a premium feel
- Quotes separated by dividers or spacing

**When not to use**:
- Customer brand recognition is not high — displaying unknown logos in a large format backfires

**Evidence**: Instrument (Nike, Levi's, Google)
**Evidence status**: Observed; small sample

---

## Pattern 5: Bento / Mosaic Social Proof

**When to use**:
- Brand tone is creative, editorial
- Have a mix of customer photos, logos, and quotes
- Want the social proof area itself to be visually engaging

**Execution**:
- Irregular grid mixing photos, logos, and quote cards
- Cards of varying sizes create visual hierarchy
- Photo cards and logo cards alternate
- Hover may reveal more information

**Evidence**: Intercom ("The results speak for themselves, so do our customers")
**Evidence status**: Observed; small sample

---

## Key Design Decisions

### Choosing the Right Social Proof Format
| Format | When to use | Assets needed |
|--------|-------------|---------------|
| Logo wall | Have recognizable customers but no detailed quotes | 5+ customer logos (with usage permission) |
| Testimonial cards | Have specific customer feedback | Quote text + name + title |
| Numbers / statistics | Have verifiable customer data | Specific numbers (e.g., "8,000+ customers") |
| Case study link | Have an in-depth case story | Case page URL |
| Rating / badge | Have third-party platform ratings | G2, Product Hunt, Capterra, etc. |

### Logo Wall Placement
- **Bottom of Hero** (most common): logo wall embedded in the bottom of the Hero section, as part of the Hero. Saves space; visible above the fold
- **Independent section after Hero**: a standalone light / white bar. Suited when there are many logos or independent display is needed
- **After Features**: show functionality first, then use logos to prove real-world adoption. Stronger logical flow

### Testimonial Quality Standards
Prioritize quotes that contain:
1. **Specific numbers**: "save more than $1M in churn" (Hex/ClickUp)
2. **Before / after contrast**: "shortened processes from hours to minutes" (Hex/AllTrails)
3. **Specific context**: "send transactional emails directly as part of their decision flow" (Customer.io)
4. **Bolded key words**: bold results or feelings within the quote

Avoid quotes that:
- Are pure sentiment with no detail: "Great product, love it!"
- Come from unverifiable sources
- Are fabricated (violates project principles)

### Person Information Display
| Element | Necessity | Reason |
|---------|-----------|--------|
| Name | Required | Anonymous quotes lack trust |
| Title | Required | Shows the quoter is qualified to evaluate |
| Company name | Required | Brand endorsement |
| Company logo | Recommended | Visual recognition is faster than text |
| Portrait photo | Optional | Adds personalization, but requires a real photo |

### Relationship with Other Sections
- **Logo wall + Hero**: the logo wall can be part of the Hero (trust strip at the bottom). See [[hero]]
- **Testimonials + Features**: testimonials can be embedded inside the Features section (Intercom pattern). See [[features]]
- **Testimonials + CTA**: embed a one-line social proof in the CTA ("Join 3,000+ businesses"). See [[cta]]
- A standalone Social Proof section typically comes after Features — show functional claims first, then support them with evidence
