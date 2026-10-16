# Landing Page Archetypes & Selection Guide

> Source: Mobbin research synthesis across 30+ SaaS product Landing Pages (2026-09-28)

---

## Archetype Definitions

### A. SaaS Tool

**Typical products**: Mixpanel, Harvest, Toggl Track, Equals, Amplemarket, ClickUp
**Core characteristic**: Product solves a specific problem; features are the primary selling point

**When to use**:
- Product has a clear feature set (analytics, tracking, management, automation)
- Users make purchase decisions based on features / price
- Product UI can visually demonstrate value

**Typical section composition**:
1. Hero (center-stacked + product screenshot + Email/CTA)
2. Logo wall (trust signal)
3. Features (3–6 feature cards or alternating image-text)
4. How It Works (optional — omit if product is simple)
5. Social Proof (customer quotes + metrics)
6. Pricing preview or CTA
7. FAQ
8. Footer

**Visual tendencies**:
- White background (#FFF / #FAFAFA), no tinted backgrounds
- Product screenshot is prominent and shows real data — the screenshot itself is the color source
- Medium-high information density, but generous spacing (section padding 180px per visual-style.md §3)
- CTA typically includes reassurance ("Free trial, no credit card")
- Extremely restrained color: black/white/gray dominant, brand color used only on CTA button (reference: Height, Clockwise)

---

### B. SaaS Platform

**Typical products**: Linear, Miro, Front, Craft, Notion, Slack
**Core characteristic**: Product is a work platform / ecosystem; emphasizes experience and collaboration

**When to use**:
- Product covers multiple use cases
- Users choose based on experience / ecosystem fit
- Storytelling is needed (why this platform is better than point solutions)

**Typical section composition**:
1. Hero (centered or split layout + multi-scene showcase)
2. Scenario / audience group display
3. Features (fewer features, each explained in more depth)
4. Social Proof (recognizable brand logos + specific case stories)
5. Integration / ecosystem showcase (optional)
6. CTA
7. Footer

**Visual tendencies**:
- Generous whitespace, section padding 180px (per visual-style.md §3)
- Large headlines (48–64px) + tight tracking = design comes from typography, not decoration
- Emotional copy (vision-forward headlines)
- Restrained color: near-black or white background + minimal brand color. Reference: Linear (nearly zero chromatic color), Notion (color only on CTA)
- Product screenshots displayed directly, no colorful background cards

---

### C. Developer Tool

**Typical products**: Cursor, Supabase, Vercel, Retool, Anchor, Height, incident.io
**Core characteristic**: Targeted at technical users; code / API / CLI is the core interaction

**When to use**:
- Primary audience is developers
- Product involves code, APIs, CLI, deployment, and other technical concepts
- Users make decisions through documentation and technical capability

**Typical section composition**:
1. Hero (dark background + code snippet or product screenshot)
2. Code examples / API showcase
3. Features (capability-focused, may include code examples)
4. How It Works (integration steps or 3-step getting started)
5. Social Proof (GitHub stars, recognizable tech company logos)
6. Documentation / resource entry points
7. CTA (low-pressure: "View docs" / "Start building")
8. Footer

**Visual tendencies**:
- Dark background (#0A0A0A–#111111; avoid saturated darks like slate/navy)
- Code blocks, terminal windows, API responses as visual elements — syntax highlighting already provides sufficient color
- Monospace font for code; headlines still use sans-serif
- Low-pressure CTAs ("View docs" rather than "Buy now"), small buttons
- GitHub stars, npm download counts as trust signals
- Copy is concise and direct; avoid marketing speak
- No added chromatic decoration — code and product screenshots are the color (reference: Vercel, GitHub, Antimetal)

---

### D. Creative / Design Tool

**Typical products**: Figma, Framer, Canva, Runway, Vizcom, Readymag
**Core characteristic**: Product helps users create visual content; the product's output is itself the best showcase

**When to use**:
- Product is a design / creative / content creation tool
- Product output (work / designs / video) is more persuasive than the product interface
- Users are designers, creators, or content producers

**Typical section composition**:
1. Hero (work showcase or product UI + output results)
2. Template / work gallery
3. Features (tool capabilities, with work examples)
4. Use Cases
5. Community / ecosystem showcase
6. Social Proof (user work, recognized creators)
7. CTA
8. Footer

**Visual tendencies**:
- Page frame stays neutral (black / white / gray); the work showcase area may be colorful (because that is product output)
- Product output (work) rather than UI screenshots as primary visual
- Brand personality expressed through typography and spatial composition, not large areas of color
- Community / template ecosystem as differentiating showcase
- Principle: frame does less (pure black and white), content does more (work provides color)

---

## Selection Process

```
1. Who is the product's primary audience?
   ├─ Developers / technical users → C. Developer Tool
   ├─ Designers / creators → D. Creative Tool
   └─ Business / ops / general
       ├─ Product solves one specific problem → A. SaaS Tool
       └─ Product is a multi-scenario platform → B. SaaS Platform

2. After choosing an archetype, adjust the section composition based on actual content:
   - Have a product screenshot? → Add Hero screenshot
   - Have customer data? → Add Social Proof
   - Is the product complex? → Add How It Works
   - Have a pricing plan? → Add Pricing preview or link
   - Have common questions? → Add FAQ
```

---

## Shared Rules Across All Archetypes

Regardless of which archetype you choose:
1. **Hero must answer**: what is this product, who is it for, why is it good (at least implicitly)
2. **Above-the-fold information density**: don't stack all information in the first screen. Headline + 1–2 sentences + CTA is enough
3. **Trust signal timing**: if you have a logo wall or data, placing it after the Hero and before Features works well
4. **Visual rhythm**: build section-feel through spacing variation and layout variation, not different background colors. Most sections maintain the same background. See `shared/visual-style.md`
5. **CTA repetition**: place CTA at least once in the Hero and once at the page bottom. An additional CTA mid-page after Features or Social Proof is optional

---

## Visual Token Adaptations by Archetype

All archetypes share the base tokens in `shared/visual-style.md`. The following aspects differ:

### A. SaaS Tool → Light Theme
- Background `#FFFFFF`, CTA uses `var(--accent)` (default `#141414`)
- Product screenshots placed in surface-1 rounded frames

### B. SaaS Platform → Light or Dark Theme
- Light: same as A
- Dark: background `#0A0A0A`, CTA `#EDEDED` (white)
- Headings can be larger (clamp upper bound raised to 80px+)
- More generous whitespace (section spacing can go to 200px+)

### C. Developer Tool → Dark Theme
- Background `#0A0A0A`, CTA `#EDEDED`
- Code blocks use surface-1 (`#141414`) background + surface-2 (`#1F1F1F`) title bar
- Syntax highlighting in terminal provides the only chromatic color (green success, yellow warning, etc.)
- Recommended terminal syntax highlight colors (used only inside code/terminal mocks, not UI elements):
  - green (success/addition): `#4ADE80`
  - red (error/deletion): `#F87171`
  - yellow (warning/change): `#FBBF24`
  - blue (info/keyword): `#60A5FA`
  - cyan (string/path): `#22D3EE`
- The page frame itself has zero chromatic color

### D. Creative Tool → Light Theme (preferred)
- Page frame stays pure achromatic
- Product output (work/designs/photos) is the only source of color
- Gallery/showcase areas can be colorful, but the frame does not add color
- Principle: the frame is the museum white wall; the content is the painting
