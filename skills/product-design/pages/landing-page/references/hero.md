# Hero Section — Design Knowledge

> Source: Mobbin research across 30 SaaS product Landing Page Hero sections (2026-09-28)

---

## Pattern 1: Center-Stacked Hero

**When to use**:
- Product has a UI screenshot or product demo that communicates value
- Standard information flow needed: what is it → why choose it → take action now
- Suitable for most SaaS tool and platform products

**Execution**:
- Structure (top to bottom): [optional: badge/supra-title] → Headline → Subheadline → CTA → product screenshot
- Headline carries the greatest visual weight (typically 40–56px, weight 500 — this design system's weight lock; do not use 700/bold)
- Subheadline is 1–2 sentences, noticeably smaller than the headline (typically 16–20px, regular weight)
- Adequate spacing between CTA and headline; don't let them feel cramped
- Product screenshot typically occupies 70–90% of container width; use a `var(--surface-1)` background frame — not shadow. Box-shadow is prohibited by this design system; device mockup bezels are also excluded from V1
- Between screenshot and background, establish hierarchy via border-radius or background color step (surface-1 vs bg). Box-shadow is prohibited; device bezels are excluded from V1

**Variants**:
- **With subheadline**: Headline conveys value / positioning; subheadline explains specific functionality or audience. Use when the product category is not obvious
- **Without subheadline**: Headline + screenshot only. Use when the product UI itself is strongly convincing (e.g., Front, Framer)
- **With badge/supra-title**: Place a product category label above the headline (e.g., "AI Sales Copilot", "Developer platform"). Use for sub-pages or when rapid category recognition is needed
- **With front-loaded trust signal**: Place a rating, logo wall, or user count above the headline or just after the CTA. Use when credible social proof data is already available

**When not to use**:
- Product cannot be summarized in one screenshot (consider layered multi-view or split layout)
- About / brand pages (consider pure text or immersive layout)
- Developer tools requiring simultaneous display of code and output (consider split layout)

**Evidence**: Craft, incident.io, Harvest, Equals, Twenty, Vizcom, ClickUp and 15+ other products use this pattern
**Evidence status**: Cross-sample inference

---

## Pattern 2: Left-Right Split Hero

**When to use**:
- Both text information and visual content need to be shown simultaneously, each equally important
- Product screenshots or code examples need to appear alongside explanatory text
- Suitable for developer tools (code left/right + explanation) and API products

**Execution**:
- Typically 40–50% text + 50–60% visual
- Text on the left is the most common arrangement (~70%), but visual on the left (e.g., Grammarly) also works — use when the result needs to be seen before the explanation is understood
- Text side keeps standard information flow: Headline → Subheadline → CTA
- Visual side can be: product screenshot, code editor, device mockup, or abstract graphic
- Both columns should stack vertically on narrow screens (text on top)

**Variants**:
- **Text left, image right** (mainstream): ClickUp, Miro, Anchor, Frontify
- **Image left, text right** (reversed): Grammarly — when visual information is a prerequisite for understanding
- **With interactive element**: Miro places an accordion selector on the text side so visitors from different roles see different product screenshots

**When not to use**:
- Product screenshot needs large-area display (center-stacked is better)
- Product is hard to summarize in a single screenshot
- Mobile experience is poor (two columns stacked may break the information flow)

**Evidence**: ClickUp, Miro, Anchor, Frontify, Grammarly, 1Password and 8 other products
**Evidence status**: Cross-sample inference

---

## Pattern 3: Dark Background Hero

**When to use**:
- Target audience is developers or technical users
- Product is a DevOps / API / CLI / code-related tool
- Brand tone leans toward technical, professional, cutting-edge

**Execution**:
- Background: dark gray / near-black (#0A0A0A ~ #1A1A1A); avoid pure black #000
- Text: white or near-white gray
- CTA button: brand color or white, ensuring sufficient contrast against the background
- Code snippets use syntax highlighting (realistic code editor style)
- If using a product screenshot, ensure the screenshot's edges blend naturally with the dark background (avoid a white screenshot appearing harsh on a black background)

**Variants**:
- **Code showcase**: Antimetal, Height, Anchor — code editor or terminal as the primary visual
- **Product screenshot**: incident.io, Twenty, Retool — product UI screenshot on dark background
- **Neon glow**: Shopify Editions — dark + glow effects. ⚠️ Anti-pattern in this design system: no gradients, no glow, no box-shadow. Do not implement.

**When not to use**:
- Product targets non-technical users (e.g., HR, Marketing tools)
- Product screenshots are light-colored UI (will look jarring on a dark background)
- Brand tone leans warm, friendly, or casual

**Evidence**: incident.io, Antimetal, Height, Retool, Shopify Editions, Frontify, Twenty, Vizcom, and others
**Evidence status**: Cross-sample inference. Note: dark ≠ technical is an observed correlation, not a causal rule

---

## Pattern 4: Text-Only / Minimal Hero

**When to use**:
- Brand color is strong and distinctive
- Product definition is simple and can be stated in one sentence
- About pages or brand story pages
- Product value does not depend on the UI's appearance

**Execution**:
- The headline is the sole visual focal point; font size must be large enough (60px+)
- Brand color may be used as background (e.g., Lemon Squeezy purple, Figma gold) in place of a product screenshot. ⚠️ Only viable with a strong brand identity; this design system's <10% chromatic area rule means brand color as a full-bleed background is only appropriate for products with pre-established brand recognition. Default: use `var(--bg)` or `var(--text)` (dark pattern)
- Generous whitespace is the hallmark of this pattern — don't fill blank space with decorative elements
- CTA can be omitted or placed in navigation — the confidence of this pattern comes from "I don't need to sell"

**Variants**:
- **Brand color background**: Lemon Squeezy, Figma — large saturated color area + white text
- **White minimal background**: Cosmos, Kalstore — pure white + black text + generous whitespace
- **Text overlaid on visual**: Readymag — text layered over a blurred background / video

**When not to use**:
- Product is complex and requires explanation (users will be confused without seeing the product)
- Brand has not yet built recognition (a Hero without a screenshot requires brand strength to support it)
- The Landing Page's primary goal is conversion / sign-up

**Evidence**: Cosmos, Kalstore, Lemon Squeezy, Figma (About), Dropbox
**Evidence status**: Observed. Small sample (5), and mostly About / brand pages rather than primary Landing Pages

---

## Headline Strategy Guide

Choose a headline strategy based on product type and audience:

| Strategy | Sentence pattern | When to use | Example |
|----------|-----------------|-------------|---------|
| **Value proposition** | "[most/more] + [outcome] + [method/subject]" | Product has a quantifiable efficiency advantage | "The fastest way for startups to do any analysis" |
| **Action-oriented** | "[verb] + [object] + [modifier]" | Product is a tool; user has a clear task | "Manage operations like a boss" |
| **Product definition** | "[verb] + [product category] + [differentiator]" | New category or needs explanation | "Build your Enterprise CRM at AI Speed" |
| **Vision** | "[verb] + [audience] + [ideal state]" | Platform product; value is indirect | "Empower teams to go from idea to outcome faster" |
| **Developer** | Mix code syntax + human language | Technical audience | "Turn // todo into tasks" |
| **Plain and direct** | "[What the product is]. [Period.]" | Simple product, confident brand | "Calendars and notebooks. That's it." |

**General rules**:
- Headline length is typically 5–12 words
- Include at least one specific noun (avoid purely abstract vocabulary)
- If the headline alone can explain what the product is + why it's good, the subheadline can be omitted

---

## CTA Strategy Guide

| Strategy | When to use | Execution |
|----------|-------------|-----------|
| **Single primary CTA** | Free trial available, single conversion path | "Get Started" / "Start for free" / "Try for free" — solid button, brand color |
| **Dual CTA (primary + secondary)** | Serving both self-serve users and enterprise customers | Primary CTA filled + secondary CTA outlined or text link. E.g., "Start free" + "Book a demo" |
| **Email + CTA** | Want to reduce sign-up friction | Input field + button side by side. Add reassurance alongside ("Free forever. No credit card.") |
| **Link CTA** | Developer product, low-pressure conversion | "View docs →" / "Read more →" — text link, not a button |
| **No Hero CTA** | Minimal brand, or CTA is in nav | CTA only in the top-right of navigation. Hero stays clean. Requires brand strength |

**Reassurance text next to CTA**:
Observed in ~30% of Heroes — text placed beside or below the CTA to eliminate hesitation:
- "Free forever. No credit card." (ClickUp)
- "Free 30-day trial. No credit card required." (Harvest)
- "No trial, no contract, no risk." (Lemon Squeezy)

---

## Transition from Hero to the Next Section

| Transition type | Example | Effect |
|----------------|---------|--------|
| **Logo wall** | ClickUp ("JOIN 800,000+...") | Natural flow: Hero → trust → Features |
| **Text bridge** | Readymag ("You're in good company") | Guides eye downward |
| **Gradient / arc** | ClickUp (arc gradient at bottom) | Visual cue to scroll down. ⚠️ Not used: gradients are prohibited in this design system |
| **Direct cut** | Craft, Front | No transition; immediate next section |
| **Feature tab** | incident.io, ClickUp | Tabs at Hero bottom hint at more content below |
