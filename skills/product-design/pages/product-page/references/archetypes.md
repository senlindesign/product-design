# Product Page Archetypes & Selection Guide

> Source: Mobbin research synthesis across ~44 unique products, ~51 section observations (2026-10-02)

---

## Archetype Definitions

### A. Feature Showcase (Default)

**Typical products**: ClickUp, Figma, Plain, Better Stack, Twenty, Mixpanel, Sana, Grain
**Core characteristic**: Multi-feature SaaS product where each feature gets brief visual coverage; breadth over depth

**When to use**:
- Product has 5+ distinct features worth showing
- Each feature can be represented by a product screenshot
- Users evaluate by scanning capabilities before committing
- Standard B2B SaaS with a feature set as the primary selling point

**Section composition** (8-12 sections):
1. Nav (shared)
2. Hero (centered or 2-col split, product video/screenshot, heading + dual CTA)
3. Logo wall (trust signal, shared social-proof pattern)
4. Feature grid (3-col or 2-col cards, 3-6 features per section, screenshot + heading + description)
5. Feature grid secondary (optional: "...and so much more" framing, 3-6 additional features)
6. Use cases (optional: 3-4 persona or industry cards)
7. Integrations (optional: 3-6 featured integration cards + API CTA)
8. Social proof (optional, customer quotes or testimonial, shared pattern)
9. CTA (dual: "Start free" + "Request a demo")
10. FAQ (optional, shared pattern)
11. Footer (shared)

**Visual tendencies**:
- Light theme dominant
- High feature density but each feature gets limited depth (heading + 1-2 sentences + screenshot)
- Product screenshots are the primary visual content (8/11 feature observations use actual UI screenshots)
- "Learn more" links on feature cards point to dedicated feature sub-pages
- Carousel or horizontal scroll for 7+ features (ClickUp 7-dot pagination, Figma "1/4" counter)

---

### B. Platform Overview

**Typical products**: Vercel, Cloudflare Workers, Shopify Commerce, Customer.io
**Core characteristic**: Infrastructure or platform product targeting developers or technical decision-makers; shows architecture and capabilities

**When to use**:
- Product is a platform, framework, or infrastructure layer (not a point solution)
- Primary audience is developers, architects, or technical buyers
- Product value is in the system design, not individual features
- "Build on top of us" is the core message

**Section composition** (7-10 sections):
1. Nav (shared)
2. Hero (dark theme common, stats + capabilities, or centered heading + product visual)
3. Logo wall (enterprise trust signal, shared pattern)
4. Capability pillars (2x3 or 3-col grid, each with mono label + heading + description)
5. Architecture section (card-based component layout or flow diagram, mono labels)
6. Platform stats (large numbers: API calls, uptime, messages sent)
7. Integrations (required: categorized cards + "Build your own" / API CTA)
8. CTA (dual: "Get started free" + "Book a demo")
9. Footer (shared)

**Visual tendencies**:
- Dark theme more common than other archetypes (Vercel, Cloudflare, Customer.io all use dark)
- Mono uppercase labels for component/capability names (12px / 400 / mono / uppercase / +0.72px / opacity 0.4)
- Large stat numbers as proof points (Customer.io: "35 Billion Messages", "4 Billion+ API calls")
- No product screenshots in architecture sections — text and diagrams only
- "0 to IPO" or "at scale" messaging; enterprise credibility signals

---

### C. Product Deep-Dive

**Typical products**: Intercom, incident.io, Rox, Grain
**Core characteristic**: Focused product with 2-4 major capability areas, each getting substantial dedicated coverage

**When to use**:
- Product has 2-4 core capabilities that each need deep explanation
- Each capability has a distinct user flow or use case
- Users need to understand HOW each capability works, not just WHAT it does
- Products where a quick feature grid would undersell the depth

**Section composition** (6-9 sections):
1. Nav (shared)
2. Hero (2-col split: heading + CTA left, video/screenshot right)
3. Logo wall (optional, shared pattern)
4. Feature deep-dive 1 (2-col: text + accordion/list left, screenshot right)
5. Feature deep-dive 2 (2-col: screenshot left, text + accordion/list right — alternating)
6. Feature deep-dive 3 (optional, continuing alternation)
7. Social proof (optional, customer quote or case study, shared pattern)
8. CTA (dual: "Start free" + "Request a demo")
9. Footer (shared)

**Visual tendencies**:
- 2-col text + screenshot split is the dominant layout (4/11 feature observations)
- Accordion/expandable lists for sub-features within each capability (Rox: 6 items, Intercom: 3 items)
- Screenshot presumably changes when selecting different accordion items (interactive behavior)
- Each capability section has its own heading + description + "Learn more" link
- Fewer total sections but each section has more vertical depth
- Dark theme variant exists (incident.io, Rox) but light is equally common

---

## Decision Matrix

| Signal | Recommended Archetype |
|--------|----------------------|
| Product has 5+ features, each demonstrable via screenshot | **A. Feature Showcase** |
| Product is infrastructure, framework, or platform | **B. Platform Overview** |
| Product has 2-4 core capabilities needing deep explanation | **C. Product Deep-Dive** |
| Primary audience is developers or technical buyers | **B. Platform Overview** |
| "Build on top of us" or "API-first" messaging | **B. Platform Overview** |
| Each feature links to its own sub-page | **A. Feature Showcase** |
| Product solves one problem deeply (e.g., incident management) | **C. Product Deep-Dive** |
| User needs to understand workflow, not just feature list | **C. Product Deep-Dive** |

**When the signal is ambiguous**: Default to **A. Feature Showcase** — it is the most common pattern (~55% of samples) and works as a safe baseline.

---

## Section Presence by Archetype

| Section | A. Feature Showcase | B. Platform Overview | C. Product Deep-Dive |
|---------|:-------------------:|:--------------------:|:--------------------:|
| Nav | Required | Required | Required |
| Hero | Required | Required | Required |
| Logo wall | Required | Required | Optional |
| Feature grid / cards | Required (1-2 sections) | Skip | Skip |
| Capability pillars | Skip | Required | Skip |
| Architecture section | Skip | Required | Skip |
| Feature deep-dive (2-col) | Skip | Skip | Required (2-4 sections) |
| Platform stats | Skip | Optional | Skip |
| Use cases | Optional | Skip | Skip |
| Integrations | Optional | Required | Optional |
| Social proof | Optional | Optional | Optional |
| CTA | Required | Required | Required |
| FAQ | Optional | Skip | Optional |
| Footer | Required | Required | Required |

---

## Evidence Summary

| Archetype | Sample count | Percentage | Key exemplars |
|-----------|:----------:|:----------:|---------------|
| A. Feature Showcase | ~24 | ~55% | ClickUp (carousel, 7 features), Figma (counter, 4 features), Plain (3x2 minimal grid), Twenty (3-col screenshots), Mixpanel (categorized 2-col), Better Stack (dark 3x2) |
| B. Platform Overview | ~11 | ~25% | Vercel (capability grid + card architecture), Cloudflare Workers (flow diagram), Shopify Commerce (platform benefits + partner categories), Customer.io (stats + capabilities) |
| C. Product Deep-Dive | ~9 | ~20% | Intercom (accordion + screenshot), incident.io (stacked list + screenshot), Rox (accordion 6 items + screenshot), Grain (alternating 2-col) |

**Total**: ~44 unique products across ~51 section observations.

---

## Archetype-Specific Content Guidelines

### A. Feature Showcase
- Feature count per grid section: 3-6 (most common: 3 or 6)
- Each feature: heading + 1-2 sentence description + product screenshot
- Optional "Learn more" link per feature (5/11 feature observations include this)
- Second feature section can use "...and so much more" framing (Plain pattern)
- Carousel pattern for 7+ features with pagination dots or counter

### B. Platform Overview
- Capability labels use the standard `.label` token
- Architecture section uses card-based layouts (Vercel pattern), not SVG diagrams
- Include specific numbers as proof points (uptime, API call volume, processing scale)
- Integration section must include API/developer CTA (3/8 integration observations include this)

### C. Product Deep-Dive
- 2-4 capability sections, each as a 2-col split
- Alternate text/screenshot sides (text-left/screenshot-right, then screenshot-left/text-right)
- Accordion items per capability: 3-6 (Intercom: 3, Rox: 6)
- Each capability has its own "Learn more" link to a dedicated sub-page
- Screenshot occupies ~55-60% of the 2-col width, text ~40-45%
